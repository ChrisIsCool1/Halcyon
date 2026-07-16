# `halcyon docs` CLI reference

`halcyon docs` contains maintainer tools for discovering Forge script
terms and building the SQLite documentation pack used by the Script Editor. These
commands work from local text and Markdown files; they do not modify a Forge
installation or include source card scripts in the generated documentation pack.

Run the commands after installing the project in editable mode:

```powershell
python -m pip install -e .
halcyon docs --help
```

## Typical workflow

1. Use `extract` to scan a local Forge `cardsfolder` and create editable discovery
   entries.
2. Replace the generated `TODO` text with concise, authored documentation.
3. Use `sync` to add only previously unseen entries to the appropriate catalog file.
4. Use `compile` to build `script_documentation.sqlite3` for the application.

For example:

```powershell
halcyon docs extract --cards-dir <cardsfolder> --preset keyword --output discoveries.md
halcyon docs sync --discoveries discoveries.md --catalog scripting_docs/catalog/keywords.md
halcyon docs compile --guides-dir scripting_docs --catalog-dir scripting_docs/catalog --output scripting_docs/script_documentation.sqlite3 --version 1
```

To generate discovery files for every bundled preset at once:

```powershell
halcyon docs extract_all_presets --cards-dir <cardsfolder> --output-dir discoveries
```

This creates one Markdown file per preset in the output directory, such as
`keyword.md`, `ability-mode.md`, and `parameter.md`.

To regenerate the ability and trigger catalogs and rebuild the pack in one command:

```powershell
halcyon docs refresh --cards-dir scripting_docs/cards/cardsfolder
```

Replace `<cardsfolder>` with the directory containing Forge's card-script `.txt`
files. Scanning is recursive, so it can be the root of the complete cards folder or
a smaller directory while authoring a focused catalog.

## `extract`

```text
halcyon docs extract --cards-dir PATH (--preset NAME | --pattern REGEX) --output PATH [--title TEXT]
```

Scans every `*.txt` file below `--cards-dir` as UTF-8 and writes a Markdown
discovery file. Files that cannot be read as UTF-8 are skipped. Progress and status
messages are written to standard error, leaving standard output free for automation.

Arguments:

- `--cards-dir PATH` (required): Forge card-script directory to scan recursively.
- `--preset NAME`: Selects one bundled expression. This must be supplied instead of
  `--pattern`.
- `--pattern REGEX`: A custom Python regular expression. It must contain at least
  one capture group; the first group becomes the discovered term. This must be
  supplied instead of `--preset`.
- `--output PATH` (required): Markdown file to create or replace. Parent directories
  are created as needed.
- `--title TEXT`: Heading for the generated Markdown document. The default is
  `Discovered Forge Terms`.

`extract` also accepts `--pattern <regex>` with one capture group for custom term families.
The presets colon-delimit keyword forms into one Markdown entry per
keyword title. For example, `Affinity:Bird` and `Affinity:Creature.Artifact:artifact creature` become one editable
`Affinity:<Selector>:[<Label>]` entry in the keywords doc. The generated entry lists observed values
for each argument slot; these values are taken directly from the scanned scripts, but they aren't a complete validity list.
The cardsfolder scripts themselves are still the source of truth in case of conflict!

Whenever you see something like `TODO: Write documentation.` or `Describe parameter` in the outputted docs, that's where you
can go and make edits. These will be visible to the Script Editor after running `halcyon compile` or `halcyon refresh`.

### Presets

| Preset             | Finds                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `keyword`          | Values on `K:` lines. Unlike other presets, it groups related colon-delimited forms by keyword title.                                             |
| `ability-mode`     | Ability families from `A:` lines and `SVar` ability definitions using `DB$`, `SP$`, or `AB$`, including observed pipe-delimited parameter values. |
| `trigger-mode`     | Trigger families from `T:` lines and `SVar` definitions using `Mode$`, including observed pipe-delimited parameter values.                        |
| `static-mode`      | Static modes from `S:Mode$` lines.                                                                                                                |
| `replacement-mode` | Replacement events from `R:Event$` lines.                                                                                                         |
| `parameter`        | Pipe-delimited parameter names ending in `$`, such as `ValidTgts$`.                                                                               |

The `ability-mode`, `trigger-mode`, `static-mode`, and `replacement-mode` presets produce one section per mode family,
with a `**Parameters:**` list containing editable documentation and observed values
for each `Label$`. Their compiled parameter records stay scoped to that family, so
autocomplete values are offered only in the matching mode family. Parameters for abilities, triggers,
static effects, and replacement effects are delimited by pipes.

- Free-text parameters (like `SpellDescription$`, `TriggerDescription$`,
  `StackDescription$`, and `TgtPrompt$`) omit their observed text.
- Parameters like `Cost$` retain only the first ten distinct values encountered. They're useful to have references for, but
  there's a lot of them to sift through.

Other non-keyword modes produce one `## \`term\``section for each distinct exact
match, sorted case-insensitively. The body starts with`TODO: Write documentation.`

### Custom-pattern example

Use a raw regex appropriate for your shell. This example finds values in `SVars` of
the form `Foo$Bar`:

```powershell
halcyon docs extract --cards-dir <cardsfolder> --pattern '(?m)^SVar:[^:]+:Foo\$([^|\r\n]+)' --output discoveries/foo.md --title 'Foo values'
```

The regular expression must have a capture group for the value to record. If it has
more than one group, only the first is used. If you try to run `extract`
with both `--preset` and `--pattern` defined, or neither of them, it won't let you. Exactly one is required.

## `extract_all_presets`

```text
halcyon docs extract_all_presets --cards-dir PATH --output-dir PATH
```

Scans the card scripts with every bundled preset and writes one Markdown discovery
file per preset into `--output-dir`. Existing files with the same names are replaced;
the output directory and its parents are created as needed.

## `sync`

```text
halcyon docs sync --discoveries PATH --catalog PATH
```

Adds complete missing `##` sections from a discovery file to a catalog Markdown file.
Section names are compared case-sensitively. Existing catalog sections are never
edited, replaced, reordered, or refreshed, which makes this safe to run repeatedly
while preserving authored documentation. Use this when a new Forge release drops and you need to write
documentation updates for new stuff.

Arguments:

- `--discoveries PATH` (required): Markdown output from `extract`, normally edited
  by a maintainer before syncing.
- `--catalog PATH` (required): Destination category file. If it does not already
  exist, `sync` creates it with a title inferred from its filename.

`sync` writes the number of added entries to standard output. It does not interpret
or validate the prose in the copied sections. Review generated `TODO` entries before
compiling, because the compiler requires each final entry to have a description.

## `refresh`

```text
halcyon docs refresh --cards-dir PATH [--catalog-dir PATH] [--guides-dir PATH] [--output PATH] [--version TEXT]
```

Regenerates `ability-mode.md` and `trigger-mode.md` from the card scripts, then
compiles the complete documentation pack. It replaces those two catalog files, so
make any authored edits elsewhere or commit them before refreshing. Defaults target
the repository's `scripting_docs/catalog`, `scripting_docs`, and
`scripting_docs/script_documentation.sqlite3`; only `--cards-dir` is required.

## `compile`

```text
halcyon docs compile --catalog-dir PATH [--guides-dir PATH] --output PATH [--version TEXT]
```

Builds a deterministic SQLite documentation pack. The output contains searchable
documentation records and metadata only; it does not copy Forge card scripts.

Arguments:

- `--catalog-dir PATH` (required): Directory of authored category Markdown files.
  Only Markdown files directly in this directory are read; subdirectories are not
  scanned.
- `--guides-dir PATH`: Optional directory containing the bundled legacy scripting
  guides. When supplied, their headings are included as fallback records.
- `--output PATH` (required): Destination `.sqlite3` pack. Parent directories are
  created as needed, and an existing destination is replaced after a successful
  build.
- `--version TEXT`: Content-version label stored in the pack metadata. Default: `1`.

Catalog entries use this compact format:

```markdown
## `Term name`

One concise description shown by the editor.

**Signature:** `Required$ | AnotherRequired$`
**Example:** `DB$ Draw | NumCards$ 1`
```

Add a file-level scope tag directly below the title, for example
`<!-- forge-doc-scope: A: -->`. The bundled presets write this tag automatically.
Its value identifies the Forge line prefix (`K:`, `A:`, `T:`, `S:`, or `R:`), and the
editor only considers entries with the matching scope for the current line. The heading
is case-sensitive, so distinct Forge-exported spellings remain distinct entries. The first
non-empty line that is not a `**Signature:**`, `**Example:**`, or HTML comment is
used as the description. `Signature` is optional and uses `|` to separate required
parameters. `Example` is optional.

When both `--guides-dir` and `--catalog-dir` contain the same heading in the same
scope, the catalog record wins. Compilation fails if any final record has no name or
description, or if two final records use the same exact scope and heading. Fix
those catalog issues and rerun the command; the existing output pack is left intact
until the replacement has been built successfully.

## Useful checks

Use the built-in help when you need the exact parser usage or the current preset
names:

```powershell
halcyon docs --help
halcyon docs extract --help
halcyon docs sync --help
halcyon docs compile --help
```
