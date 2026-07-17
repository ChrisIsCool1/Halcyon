"""Tests for mined documentation sources and compiled documentation packs."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from forge_content_manager.devtools import AbilityFamily, extract_ability_families, extract_keyword_families, extract_preset, extract_terms, refresh_documentation, sync_catalog, write_ability_discoveries, write_discoveries, write_keyword_discoveries
from forge_content_manager.services.documentation_pack import DocumentationRecord, compile_pack, load_pack, parse_markdown_catalog, validate_pack
from forge_content_manager.services.script_authoring_service import ScriptAuthoringService


class DocumentationPackTests(unittest.TestCase):
    def test_extract_deduplicates_and_sorts_custom_pattern(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.txt").write_text("K:Vigilance\nK:Trample\n", encoding="utf-8")
            (root / "two.txt").write_text("K:Vigilance\n", encoding="utf-8")
            self.assertEqual(extract_terms(root, r"(?m)^K:(.+)$"), ["Trample", "Vigilance"])

    def test_extract_reports_progress_against_precounted_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "one.txt").write_text("K:Vigilance\n", encoding="utf-8")
            (root / "two.txt").write_text("K:Trample\n", encoding="utf-8")
            updates: list[tuple[int, int]] = []
            extract_terms(root, r"(?m)^K:(.+)$", lambda completed, total: updates.append((completed, total)))
            self.assertEqual(updates[0], (0, 2))
            self.assertEqual(updates[-1], (2, 2))

    def test_extracts_scripts_from_multiple_subdirectories(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "a").mkdir()
            (root / "b").mkdir()
            (root / "a" / "one.txt").write_text("S:Mode$ Continuous | Affected$ Creature\n", encoding="utf-8")
            (root / "b" / "two.txt").write_text("S:Mode$ Continuous | Affected$ Artifact\n", encoding="utf-8")
            updates: list[tuple[int, int]] = []
            families = extract_ability_families(root, "S", lambda completed, total: updates.append((completed, total)))
            self.assertEqual(families[0].parameters["Affected"], ["Creature", "Artifact"])
            self.assertEqual(updates[0], (0, 2))
            self.assertEqual(updates[-1], (2, 2))

    def test_extract_preset_writes_the_requested_output_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cards = root / "cards"
            output = root / "discoveries" / "keyword.md"
            cards.mkdir()
            (cards / "sample.txt").write_text("K:Trample\n", encoding="utf-8")

            self.assertEqual(extract_preset(cards, "keyword", output), 1)
            self.assertEqual(output.read_text(encoding="utf-8").splitlines()[0], "# Discovered Forge Terms")
            self.assertIn("## `Trample`", output.read_text(encoding="utf-8"))

    def test_keyword_extraction_groups_argument_slots(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "keywords.txt").write_text(
                "K:Affinity:Bird\nK:Affinity:Creature.Artifact:artifact creature\n"
                "K:etbCounter:DIVINITY:1:CheckSVar$ FromHand:CARDNAME enters with a divinity counter\n",
                encoding="utf-8",
            )
            families = {family.title: family for family in extract_keyword_families(root)}
            self.assertEqual(families["Affinity"].arguments, [{"Bird", "Creature.Artifact"}, {"artifact creature"}])
            self.assertEqual(len(families["etbCounter"].arguments), 4)
            output = root / "keywords.md"
            write_keyword_discoveries(output, list(families.values()), "Keywords")
            content = output.read_text(encoding="utf-8")
            self.assertIn("## `Affinity:<Selector>:[<Label>]`", content)
            self.assertIn("Observed values: `Bird`, `Creature.Artifact`", content)
            self.assertIn("## `etbCounter:<Selector>:[<Label>]:[<Argument 3>]:[<Argument 4>]`", content)
            self.assertIn("<!-- forge-doc-scope: K: -->", content)

    def test_keyword_case_variants_remain_separate_families(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "keywords.txt").write_text("K:TapOrUntapAll\nK:TaporUntapAll\n", encoding="utf-8")
            self.assertEqual([family.title for family in extract_keyword_families(root)], ["TapOrUntapAll", "TaporUntapAll"])

    def test_ability_extraction_groups_parameters_without_svar_labels(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "abilities.txt").write_text(
                "A:SP$ ChangeZone | Origin$ Battlefield | Destination$ Hand\n"
                "SVar:DBExile:DB$ ChangeZone | Origin$ Battlefield | Destination$ Exile\n"
                "T:Mode$ Attacks | Execute$ TrigDraw\n"
                "SVar:LaterTrigger:Mode$ Attacks | Execute$ TrigToken\n",
                encoding="utf-8",
            )
            abilities = {family.title: family for family in extract_ability_families(root, "A")}
            triggers = {family.title: family for family in extract_ability_families(root, "T")}
            self.assertEqual(abilities["ChangeZone"].parameters["Destination"], ["Hand", "Exile"])
            self.assertNotIn("DBExile", abilities)
            self.assertEqual(triggers["Attacks"].parameters["Execute"], ["TrigDraw", "TrigToken"])
            output = root / "abilities.md"
            write_ability_discoveries(output, list(abilities.values()), "Abilities", "A")
            self.assertIn("- `Destination$`: TODO: Describe this parameter.", output.read_text(encoding="utf-8"))

    def test_static_and_replacement_extraction_groups_parameters(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "modes.txt").write_text(
                "S:Mode$ Continuous | Affected$ Creature | AddPower$ 2\n"
                "R:Event$ Untap | ValidCard$ Creature | Layer$ CantHappen\n",
                encoding="utf-8",
            )
            statics = {family.title: family for family in extract_ability_families(root, "S")}
            replacements = {family.title: family for family in extract_ability_families(root, "R")}
            self.assertEqual(statics["Continuous"].parameters["AddPower"], ["2"])
            self.assertEqual(replacements["Untap"].parameters["Layer"], ["CantHappen"])
            output = root / "static.md"
            write_ability_discoveries(output, list(statics.values()), "Static Modes", "S")
            self.assertIn("- `Affected$`: TODO: Describe this parameter.", output.read_text(encoding="utf-8"))

    def test_catalog_parameter_records_are_scoped_to_their_family(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "abilities.md").write_text(
                "# Abilities\n\n<!-- forge-doc-scope: A: -->\n\n## `ChangeZone`\n\nMoves a card.\n\n**Parameters:**\n- `Origin$`: Source zone.\n  Observed values: `Battlefield`, `Hand`\n",
                encoding="utf-8",
            )
            records = parse_markdown_catalog(root)
            parameter = next(record for record in records if record.name == "Origin$")
            self.assertEqual(parameter.scope, "A:ChangeZone")
            self.assertEqual(parameter.parameters, ("Battlefield", "Hand"))

    def test_ability_discovery_omits_free_text_values_and_caps_cost_values(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "abilities.md"
            write_ability_discoveries(output, [AbilityFamily("Draw", {
                "SpellDescription": ["Draw a card."],
                "TgtPrompt": ["Choose a player"],
                "Cost": [str(value) for value in range(12)],
            })], "Abilities", "A")
            content = output.read_text(encoding="utf-8")
            self.assertIn("- `SpellDescription$`: TODO: Describe this parameter.\n- `TgtPrompt$`", content)
            self.assertNotIn("Draw a card.", content)
            self.assertEqual(content.count("`0`"), 1)
            self.assertNotIn("`10`", content)

    def test_refresh_regenerates_families_and_compiles_the_pack(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cards = root / "cards"
            cards.mkdir()
            (cards / "sample.txt").write_text(
                "A:SP$ Draw | NumCards$ 1\nT:Mode$ Attacks | Execute$ TrigDraw\nSVar:TrigDraw:DB$ Draw\n",
                encoding="utf-8",
            )
            catalog, pack = root / "catalog", root / "documentation.sqlite3"
            self.assertEqual(refresh_documentation(cards, catalog, None, pack), (1, 1))
            self.assertIn("## `Draw`", (catalog / "ability-mode.md").read_text(encoding="utf-8"))
            self.assertIn("## `Attacks`", (catalog / "trigger-mode.md").read_text(encoding="utf-8"))
            self.assertEqual(validate_pack(pack), "2")

    def test_sync_preserves_existing_authored_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            discoveries, catalog = root / "found.md", root / "keywords.md"
            write_discoveries(discoveries, ["K:Trample", "K:Vigilance"], "Found")
            catalog.write_text("# Keywords\n\n## `K:Vigilance`\n\nAuthored explanation.\n", encoding="utf-8")
            self.assertEqual(sync_catalog(discoveries, catalog), 1)
            content = catalog.read_text(encoding="utf-8")
            self.assertIn("Authored explanation.", content)
            self.assertIn("## `K:Trample`", content)

    def test_sync_keeps_discovery_argument_details(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            discoveries, catalog = root / "found.md", root / "keywords.md"
            discoveries.write_text("# Found\n\n## `Affinity:<Selector>`\n\nTODO: Write documentation.\n\n**Arguments:**\n- **Selector:** observed.\n", encoding="utf-8")
            self.assertEqual(sync_catalog(discoveries, catalog), 1)
            self.assertIn("**Arguments:**", catalog.read_text(encoding="utf-8"))

    def test_sync_copies_discovery_scope_to_new_catalog(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            discoveries, catalog = root / "found.md", root / "abilities.md"
            discoveries.write_text("# Found\n\n<!-- forge-doc-scope: A: -->\n\n## `AssembleContraption`\n\nDocumentation.\n", encoding="utf-8")
            sync_catalog(discoveries, catalog)
            self.assertIn("<!-- forge-doc-scope: A: -->", catalog.read_text(encoding="utf-8"))

    def test_compiled_pack_validates_and_resolves_context(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pack = Path(directory) / "documentation.sqlite3"
            compile_pack(pack, [
                DocumentationRecord("K:Vigilance", "Keywords", "Attacks without tapping."),
                DocumentationRecord("Affinity:<Selector>:[<Label>]", "Keywords", "Reduces costs for matching permanents."),
                DocumentationRecord("AssembleContraption", "Ability modes", "Creates a Contraption.", scope="A"),
                DocumentationRecord("AssembleContraption", "Replacement modes", "Replaces a Contraption event.", scope="R"),
                DocumentationRecord("Mode$ Attacks", "Trigger modes", "Triggers when this attacks."),
                DocumentationRecord("ValidTgts$", "Parameters", "Defines legal targets."),
            ], "test-1")
            self.assertEqual(validate_pack(pack), "test-1")
            self.assertEqual(len(load_pack(pack)), 6)
            service = ScriptAuthoringService(Path("missing"), Path(directory) / "cards.sqlite3", pack)
            self.assertEqual(service.lookup_context("K:Vigilance", 6).description, "Attacks without tapping.")
            self.assertEqual(service.lookup_context("K:Affinity:Creature.Artifact:artifact creature", 16).description, "Reduces costs for matching permanents.")
            self.assertEqual(service.lookup_context("T:Mode$ Attacks | Execute$ X", 12).description, "Triggers when this attacks.")
            self.assertEqual(service.lookup_context("A:SP$ Pump | ValidTgts$ Creature", 23).description, "Defines legal targets.")
            self.assertEqual(service.lookup_context("A:SP$ AssembleContraption", 15).description, "Creates a Contraption.")
            self.assertEqual(service.lookup_context("R:Event$ AssembleContraption", 17).description, "Replaces a Contraption event.")

    def test_context_completion_uses_family_parameters_and_svar_ability_scope(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            pack = Path(directory) / "documentation.sqlite3"
            compile_pack(pack, [
                DocumentationRecord("ChangeZone", "Abilities", "Moves a card.", ("Origin$",), scope="A"),
                DocumentationRecord("Origin$", "ChangeZone parameter", "Source zone.", ("Battlefield", "Hand"), scope="A:ChangeZone"),
                DocumentationRecord("Attacks", "Triggers", "Attacking trigger.", ("Execute$",), scope="T"),
            ])
            service = ScriptAuthoringService(Path("missing"), Path(directory) / "cards.sqlite3", pack)
            self.assertEqual([item.name for item in service.complete_context("A:SP$ ChangeZone | Ori", 22, "Ori")], ["Origin$"])
            self.assertEqual([item.name for item in service.complete_context("SVar:DoThing:DB$ ChangeZone | Origin$ B", 39, "B")], ["Battlefield"])
            self.assertEqual(service.scope_for_line("SVar:Delay:DB$ DelayedTrigger | Mode$ Phase"), "A")

    def test_unresolved_svar_references_are_reported_without_rejecting_the_script(self) -> None:
        text = "T:Mode$ Attacks | Execute$ TrigDraw | Triggers$ MissingTrigger\nSVar:DBToken:DB$ Token | SubAbility$ Missing | ReplaceWith$ MissingReplacement\nSVar:TrigDraw:DB$ Draw\n"
        references = ScriptAuthoringService.unresolved_svar_references(text)
        self.assertEqual(
            [(item.label, item.value, item.line_number) for item in references],
            [("Triggers", "MissingTrigger", 1), ("SubAbility", "Missing", 2), ("ReplaceWith", "MissingReplacement", 2)],
        )

    def test_invalid_pack_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            invalid = Path(directory) / "not-a-pack.sqlite3"
            invalid.write_text("not sqlite", encoding="utf-8")
            with self.assertRaises(ValueError):
                validate_pack(invalid)


if __name__ == "__main__":
    unittest.main()
