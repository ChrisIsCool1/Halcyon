# Authored Script Documentation

Each `##` heading is the exact script term shown by the editor. Add a short paragraph,
then optional `**Signature:**` and `**Example:**` lines. Use the developer commands:

`forge-content-manager docs extract --cards-dir <cardsfolder> --preset keyword --output discoveries.md`

`forge-content-manager docs sync --discoveries discoveries.md --catalog scripting_docs/catalog/keywords.md`

`forge-content-manager docs compile --guides-dir scripting_docs --catalog-dir scripting_docs/catalog --output scripting_docs/script_documentation.sqlite3 --version 1`
