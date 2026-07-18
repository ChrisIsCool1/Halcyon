# Discovered Forge Terms

<!-- forge-doc-scope: R: -->

## `AddCounter`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `Description$`: TODO: Describe this parameter.
- `EffectOnly$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AddOneLessCounters`, `AddOneMoreCounter`, `AddOneMoreCounters`, `DoubleCounters`, `HalfCounters`, `OneMore`, `OnlyOnePoison`, `Twice`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inZoneBattlefield+Other`, `Creature.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield,Vehicle.YouCtrl+inZoneBattlefield`, `Permanent.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield,Spacecraft.YouCtrl+inZoneBattlefield,Planet.YouCtrl+inZoneBattlefield`, `Orc.YouCtrl+inZoneBattlefield,Army.YouCtrl+inZoneBattlefield,Goblin.YouCtrl+inZoneBattlefield`, `Card.Self`, `Creature.YouCtrl+inZoneBattlefield,Artifact.YouCtrl+inZoneBattlefield`, `Permanent.YourTeamCtrl+inZoneBattlefield`, `Creature.inZoneBattlefield`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Triggered.Modular`
- `ValidCounterType$`: TODO: Describe this parameter.
  Observed values: `ENERGY`, `M1M1`, `P1P1`, `POISON`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inZoneBattlefield,Planeswalker.YouCtrl+inZoneBattlefield,You`, `Permanent.inZoneBattlefield,Player`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `AssembleContraption`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AssembleTwo`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Rigger.YouCtrl`

## `Attached`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ChooseCard`, `ChooseColor`, `ChooseName`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature`

## `BeginPhase`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `Description$`: TODO: Describe this parameter.
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `Other`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `Draw`, `Untap`, `Upkeep`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBGainLife`
- `Skip$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `BeginTurn`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ExtraTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+tapped`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBUntap`
- `Skip$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `Cascade`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplacementResult$`: TODO: Describe this parameter.
  Observed values: `Updated`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBLand`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CopySpell`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AddOneMore`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSpell$`: TODO: Describe this parameter.
  Observed values: `Spell`

## `Counter`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$Presence_Dragon.1.0`, `X`, `Y`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Instant.YouOwn,Sorcery.YouOwn`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBRemove`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE5`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Instant.YouCtrl,Sorcery.YouCtrl,Dragon.YouCtrl`, `Card.cmcGE5+wasCastByYou`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.YouCtrl`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell,Activated,Triggered`, `Spell.Creature`, `Spell.Creature+powerGE5+YouCtrl`, `Spell.Creature+YouCtrl`, `Spell.Creature+YouCtrl,Spell.Enchantment+YouCtrl`, `Spell.Green+YouCtrl`, `Spell.hasKeywordFlash+wasCastByYou`, `Spell.Human+YouCtrl`, `Spell.Instant+YouCtrl,Spell.Sorcery+YouCtrl`, `Spell.nonCreature+YouCtrl`, `Spell.Sliver`, `Spell.YouCtrl`

## `CreateToken`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Description$`: TODO: Describe this parameter.
- `EffectOnly$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+IsSolved`, `Card.Self+AttachedTo Creature`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `Copy`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBCopy`, `DBReplace`, `DoubleToken`, `GenericChoice`, `HalveToken`, `TokenReplace`, `TripleToken`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `ValidToken$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.YouCtrl`, `Card.OppCtrl`, `Card.YouCtrl`, `Clue`, `Clue,Food,Treasure`, `Creature.YouCtrl`, `Treasure`

## `DamageDone`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `ProtectFriendly`
- `AlwaysReplace$`: TODO: Describe this parameter.
  Observed values: `True`
- `CauseIsSource$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.isMonarch`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `DamageAmount$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE4`, `LE3`, `LTX`
- `DamageTarget$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Equipped`, `ReplacedSourceController`, `ReplacedTargetController`, `Self`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `Description$`: TODO: Describe this parameter.
- `ExecuteMode$`: TODO: Describe this parameter.
  Observed values: `PerSource`, `PerTarget`
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCombat$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+Other`, `Card.Self+untapped`, `Card.equipping`, `Artifact.Creature+YouCtrl+attacking`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `Prevent$`: TODO: Describe this parameter.
  Observed values: `True`
- `PreventionEffect$`: TODO: Describe this parameter.
  Observed values: `True`
- `RelativeToSource$`: TODO: Describe this parameter.
  Observed values: `Creature.SharesColorWith`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AddCounters`, `ChangeZone`, `ChoosePlayer`, `Counters`, `CountersAndMill`, `DamageReplace`, `DBDraw`, `DBImmediateTrigger`, `DBRemoveCounters`, `DBReplace`, `Dmg2`, `Dmg3`, `DmgEnchanted`, `DmgEquipped`, `DmgHalfDown`, `DmgMe`, `DmgMinus1`, `DmgPlus`, `DmgPlus1`, `DmgPlus2`, `DmgSelf`, `DmgTriple`, `DmgTwice`, `DoubleMill`, `Exile`, `ExileCards`, `ExileTop`, `GainLife`, `HarshDmg`, `HostilityTokens`, `Mill`, `ReplaceDamage`, `RollDamage`, `Sac`, `SekkiCounters`, `ShuffleCreature`
- `Revolt$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ4`, `EQ5`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Spell.IsTargeting Self`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Card.YouCtrl,Emblem.YouCtrl`, `Card.RedSource`, `Artifact.Creature+inZoneBattlefield`, `Artifact`, `Creature.EnchantedBy+nonEnchantment`, `Creature.blockingSource`, `Spell`, `Card.RememberedPlayerCtrl,Emblem.RememberedPlayerCtrl`, `Card.ChosenCtrl,Emblem.ChosenCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Permanent,Player`, `Permanent.OppCtrl,Opponent`, `Player`, `You,Permanent.Other+YouCtrl`, `You`, `Card.Self`, `Creature.Self`, `Creature.EnchantedBy`, `Permanent.ChosenCtrl,Player.Chosen`, `Permanent.RememberedPlayerCtrl,Player.IsRemembered`

## `Destroy`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `Regeneration$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `CracklingEgress`, `DBRegeneration`, `HarmoniousEgress`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.EnchantedBy`

## `Draw`

TODO: Write documentation.

**Parameters:**
- `ActivePhases$`: TODO: Describe this parameter.
  Observed values: `Draw`
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `AICheckSVar$`: TODO: Describe this parameter.
  Observed values: `AIHandling`
- `AISVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Description$`: TODO: Describe this parameter.
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE6_QUEST`, `Card.YouOwn`
- `NotFirstCardInDrawStep$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Library`
- `Prevent$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AbundantChoice`, `AddCounters`, `CheckLoseCondition`, `Counter`, `DBChooseOpp`, `DBDig`, `Dig`, `DiscardOne`, `DrawTwo`, `EnduringRevealTop`, `ExileTop`, `ExileTwo`, `Reanimate`, `RepParallelThoughts`, `RepTreasure`, `RepYouDraw`, `RevealedDraw`, `RevealTop`, `SanctuaryEffect`, `Tutor`, `Win`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Activated.Cycling+nonLand`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Chosen`, `You`

## `DrawCards`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Description$`: TODO: Describe this parameter.
- `Number$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DrawEach`, `DrawPlusOne`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE1`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`, `You`

## `Explore`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBScry`, `Explore1`
- `ValidExplorer$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `GainLife`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DoubleLife`, `LichDraw`, `LoseLife`, `NoLife`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Y`
- `Description$`: TODO: Describe this parameter.
- `Prevent$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `Draw`, `GainDouble`, `GainLife`, `ReplaceGainLife`, `RLoseLife`
- `SourceController$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE5`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `SpellAbility`

## `GameLoss`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `CheckFourthSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarLX`
- `CheckSecondSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarCX`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarAX`
- `CheckThirdSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarEX`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+AttachedTo Creature`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ExileSetLife`, `ShuffleDrawSetLife`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidLoseReason$`: TODO: Describe this parameter.
  Observed values: `LifeReachedZero`, `Milled`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`

## `GameWin`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `CheckFourthSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarLX`
- `CheckSecondSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarCX`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarAX`
- `CheckThirdSVar$`: TODO: Describe this parameter.
  Observed values: `AvatarEX`
- `Description$`: TODO: Describe this parameter.
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `Learn`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `Return`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `LifeReduced`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `IsDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `Monarch$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `LoseTwice`, `ReduceLoss`, `Transform`
- `Result$`: TODO: Describe this parameter.
  Observed values: `LE0`, `LT1`, `LT7`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`, `You.lifeGE1`, `You.lifeGE7`

## `LoseMana`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplacementResult$`: TODO: Describe this parameter.
  Observed values: `Replaced`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ConvertMana`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Mill`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `MillPlus4`, `MillTwice`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`

## `Moved`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Hand`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `RaidTest`
- `Cycling$`: TODO: Describe this parameter.
  Observed values: `False`
- `DayTime$`: TODO: Describe this parameter.
  Observed values: `Neither`
- `Description$`: TODO: Describe this parameter.
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Discard$`: TODO: Describe this parameter.
  Observed values: `True`
- `EffectOnly$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExcludeDestination$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `FoundSearchingLibrary$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+tapped`, `Card.Self+untapped`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`, `Control`, `Copy`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Graveyard,Library`, `Hand`, `Library`, `Stack`
- `Prevent$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplacementResult$`: TODO: Describe this parameter.
  Observed values: `Updated`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AddExtraCounter`, `BecomeDino`, `CamelTapped`, `ChooseCT`, `ChooseP`, `CryptExile`, `DBChangeZone`, `DBChooseBasic`, `DBChooseOpp`, `DBCopy`, `DBExile`, `DBPump`, `DBPutCounter`, `DBReveal`, `DBShuffle`, `DBTap`, `DevourCreatsAndWalkers`, `Discard`, `DiscardToLibrary`, `DoDay`, `EntersTapped`, `EnterWithCounters`, `EnterWithP1P1`, `ETBCounter`, `ETBCounters`, `ETBTapped`, `ETBUntapped`, `Exile`, `ExileCreature`, `GatherDust`, `LandTapped`, `LoseLife`, `MoldChoice`, `MorphChoice`, `MoveExile`, `MoveToPlay`, `NissaChosenRep`, `PayBeforeETB`, `PayLife`, `PlasmaChoice`, `RepExile`, `ReturnToHand`, `Reveal`, `SacBeforeETB`, `SphereTapped`, `SurpriseETB`, `ToExile`, `ToHand`, `ToLibrary`, `TrigPrepare`, `TrigSac`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.YouOwn+withCycling,Card.YouOwn+withTypeCycling`, `Card.Creature+!token+OppOwn`, `Permanent`, `Land.OppCtrl+nonBasic`, `Creature.cmcNotChosenEvenOdd`, `Creature.OppCtrl`, `Artifact.OppCtrl,Creature.OppCtrl`, `Dinosaur.YouCtrl+Other`, `Creature.!token+!wasCast`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `LandAbility.OppCtrl,Spell.wasCast+Permanent+CastSa Spell.OppCtrl`, `LandAbility.YouCtrl`, `SpellAbility.OppCtrl`
- `ValidLKI$`: TODO: Describe this parameter.
  Observed values: `Card.!token+YouDontCtrl+OppOwn`, `Card.Black,Card.Red`, `Card.CastSa Spell.MayPlaySource`, `Card.Creature+!token+OppCtrl`, `Card.Creature+OppCtrl`, `Creature.!token`, `Creature.!token+OppCtrl`, `Creature.DamagedBy`, `Creature.DamagedBy Enchanted`, `Creature.DamagedByCard.YouCtrl;Emblem.YouCtrl`, `Creature.enchanted+YouCtrl`, `Creature.OppCtrl`, `Creature.Other`, `Permanent`, `Permanent.nonland`, `Warlock.YouCtrl`

## `PayLife`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `LEY`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ExileTop`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Planeswalk`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `DBPlanarScry`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `ProduceMana`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `Description$`: TODO: Describe this parameter.
- `ManaAmount$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ProduceAny`, `ProduceB`, `ProduceC`, `ProduceColorless`, `ProduceG`, `ProduceR`, `ProduceThrice`, `ProduceTwice`, `ProduceU`, `ProduceW`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidActivator$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Land`, `Permanent`, `Land.Basic+YouCtrl`, `Plains`, `Island`, `Swamp`, `Mountain`, `Forest`, `Land.Basic`

## `Proliferate`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DoubleLife`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ProlifTwice`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `RemoveCounter`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `IsDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `ReduceLoss`
- `Result$`: TODO: Describe this parameter.
  Observed values: `LT1`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Planeswalker.YouCtrl+ChosenType`, `Permanent.OppCtrl`
- `ValidCounterType$`: TODO: Describe this parameter.
  Observed values: `LOYALTY`, `STUN`

## `RollDice`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `PlusRoll`, `SwapRoll`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSides$`: TODO: Describe this parameter.
  Observed values: `6`

## `RollPlanarDice`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `PlusRoll`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Scry`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `Draw`, `ScryP1`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Transform`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `Attach`, `Copy`, `DBChoose`, `DBEffect`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `TurnFaceUp`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`, `Copy`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplacementResult$`: TODO: Describe this parameter.
  Observed values: `Updated`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `AddCounters`, `DBAttach`, `DBCopy`, `MorphChoice`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Permanent.OppCtrl`, `Card.EnchantedBy+faceDown`

## `Untap`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `AddSVar$`: TODO: Describe this parameter.
  Observed values: `FrozenSolidDestroy`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Reflection.YouCtrl`, `Card.Self+counters_GE1_PUPA`, `Card.Self+counters_GE1_NET`, `Permanent.Snow+Other+YouCtrl`
- `Layer$`: TODO: Describe this parameter.
  Observed values: `CantHappen`
- `ReplaceWith$`: TODO: Describe this parameter.
  Observed values: `RepPutCounter`, `RepRemoveCounter`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.ChosenType`, `Creature.EnchantedBy`, `Creature.Legendary`, `Land.nonBasic`, `Creature.withFlying`, `Card.EnchantedBy`, `Creature.AttachedBy`, `Card.EquippedBy`, `Island`
- `ValidStepTurnToController$`: TODO: Describe this parameter.
  Observed values: `You`
