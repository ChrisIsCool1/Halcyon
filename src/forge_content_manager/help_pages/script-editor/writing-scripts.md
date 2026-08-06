---
title: Writing Forge scripts
summary: The basic structure of a Forge card script and the editor tools available to you.
---
# Writing Forge scripts

Forge card scripts are made from fields and ability lines. The Script Editor is intentionally non-validating, so it lets you draft freely while providing documentation and completion suggestions where it can.

## Common building blocks

- `Name:` sets the card's display name.
- `ManaCost:` sets the mana cost.
- `Types:` sets the card's types and subtypes.
- `Oracle:` contains displayed rules text.
- `A:`, `T:`, `S:`, and `R:` describe activated, triggered, static, and replacement abilities.
- `SVar:` names a reusable sub-ability.

Place one field or ability on each line. Use the documentation panel beside the editor to inspect recognized terms and parameters.

## Completion and references

Type at least two characters of a term to see context-aware suggestions. If you configure a Forge `cardsfolder` in Settings, the Reference Cards panel can also search and insert existing scripts.

Before importing, review warnings for unresolved `SVar` references and make sure the script still says what you intend.
