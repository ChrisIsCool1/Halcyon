# Authored Script Documentation

Each `##` heading is the exact script term shown by the editor. Add a short paragraph,
then optional `**Signature:**` and `**Example:**` lines. Use the developer commands:

Ability and trigger family entries may also include a `**Parameters:**` list. Use
one bullet per parameter, such as ``- `Origin$`: Describe the source zone.``, then
an indented `Observed values:` line. These entries compile as family-scoped help and
completion values rather than global parameter documentation.

Add `<!-- forge-doc-scope: K: -->` near the top of each category file. Valid scopes
are the Forge line prefixes such as `K:`, `A:`, `T:`, `S:`, and `R:`; the editor only
uses entries from the scope matching the current line. Headings are case-sensitive,
so distinct Forge spellings such as `TapOrUntapAll` and `TaporUntapAll` remain separate.

`forge-content-manager docs extract --cards-dir <cardsfolder> --preset keyword --output discoveries.md`

`forge-content-manager docs sync --discoveries discoveries.md --catalog scripting_docs/catalog/keywords.md`

`forge-content-manager docs compile --guides-dir scripting_docs --catalog-dir scripting_docs/catalog --output scripting_docs/script_documentation.sqlite3 --version 1`
