---
title: Using Auto for description autofill
summary: Turn a natural-language card description into a matching Forge script expansion.
---

# Using Auto for description autofill

The Script Editor now supports the `Auto` option for description autofill. It searches descriptions discovered from your documentation pack and offers matching script expansions while you type.

## How to use it

1. Open the **Script Editor** tab.
2. Start a new line with `Auto:`.
3. Type part of the description you want to find.
4. Choose a suggestion from the completion list and press **Enter**.

For example:

```text
Auto: Face-down creatures get +1/+1.
```

When you accept a suggestion, Halcyon replaces the whole `Auto:` line with the matching Forge script. The expanded lines may include the original ability and any related `SVar` lines it needs.

## Getting useful results

- Use the wording that appears in the card description.
- Start with a distinctive phrase rather than a single common word.
- Keep the caret on the `Auto:` line while choosing a result.
- If no results appear, check that the Script Documentation Pack has been built from a cards folder containing the relevant scripts.

## What Auto does not do

`Auto:` is a search and expansion aid. It does not validate the final script or invent a new ability. Review the inserted script, adjust it for your card, and use the editor's documentation and reference tools when you need more context.
