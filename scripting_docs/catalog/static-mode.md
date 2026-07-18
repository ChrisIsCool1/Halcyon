# Discovered Forge Terms

<!-- forge-doc-scope: S: -->

## `ActivateAbilityAsIfHaste`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.Other+YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl`

## `AlternativeCost`

TODO: Write documentation.

**Parameters:**
- `Announce$`: TODO: Describe this parameter.
  Observed values: `X`
- `CheckSecondSVar$`: TODO: Describe this parameter.
  Observed values: `Y`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ArtifactsEntered`, `CardsToGraveyard`, `CreaturesDmg`, `CreaturesEntered`, `GreenCreats`, `LandsEntered`, `OppCastThisTurn`, `OppLifeGained`, `SetTrap`, `TrapTrigger`, `X`, `Y`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `NotPlayerTurn`, `PlayerTurn`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Plains>`, `U`, `ExileFromHand<2/Card.Green>`, `tapXType<1/Creature>`, `0`, `1 W`, `BR`, `1 B`, `1 G`, `B`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `0`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Command`, `Graveyard`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Plains.YouCtrl`, `Creature.attacking`, `Creature`, `Swamp.YouCtrl`, `Card.IsCommander+YouCtrl`, `Forest.YouCtrl`, `Creature.White+attacking`, `Creature.attacking+Black+withFlying`
- `ManaRestriction$`: TODO: Describe this parameter.
  Observed values: `Treasure`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE13`, `GE3`, `GE4`
- `StackDescription$`: TODO: Describe this parameter.
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE2`, `GE3`, `GE7`, `LT1`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.Zombie`, `Card.Rune`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Crew+Vehicle`, `Activated.Cycling`, `Activated.Equip`, `Spell`, `Spell.Samurai`, `Spell.Self`
- `XAlternative$`: TODO: Describe this parameter.
  Observed values: `Count$CardManaCost`

## `AssignCombatDamageAsUnblocked`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+attacking`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EnchantedBy`, `Creature.YouCtrl+nonHuman`, `Creature.NoAbilities+YouCtrl`, `Creature.YouCtrl`

## `AttackRequirement`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidAttacker$`: TODO: Describe this parameter.
  Observed values: `Card.counters_GE1_MAGNET`, `Card.Self`, `Creature.OppCtrl`, `Creature.YouCtrl`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Card.counters_GE1_MAGNET`, `Card.Self`, `Creature.OppCtrl`

## `AttackRestrict`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+tapped`
- `MaxAttackers$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `ValidDefender$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `You`

## `BlockRestrict`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `MaxBlockers$`: TODO: Describe this parameter.
  Observed values: `1`, `2`

## `BlockTapped`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.tapped+YouCtrl`

## `CanAttackDefender`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Hellbent`, `Metalcraft`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.powerGE4+YouCtrl`, `Gate.YouCtrl`, `Lesson.YouOwn`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GE8`
- `ValidAttacked$`: TODO: Describe this parameter.
  Observed values: `Player.attackedYouTheirLastTurn`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.EnchantedBy`, `Creature.withDefender+YouCtrl`, `Card.Self`, `Card.Self+IsMonstrous`, `Card.Self+HasCounters`, `Card.Self+counters_GE3_JUDGMENT`, `Creature.YouCtrl`, `Creature.YouCtrl+modified`, `Card.Self+powerGE7`, `Card.Self+powerGE5`

## `CanAttackIfHaste`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self+!ThisTurnEntered`, `Creature.EnchantedBy`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Opponent,Planeswalker.OppCtrl`

## `CanBlockIfReach`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidAttacker$`: TODO: Describe this parameter.
  Observed values: `Dragon`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `CanExhaust`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Description$`: TODO: Describe this parameter.
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `You`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `LT1`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CantAttach`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+untapped`
- `Target$`: TODO: Describe this parameter.
  Observed values: `Artifact.nonCreature+YouCtrl`, `Card.Self`, `Creature.EnchantedBy`, `Creature.nonLegendary`, `Creature.powerLT3`, `Creature.toughnessLT4`, `Land.EnchantedBy`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Aura.Other`, `Card.Self`, `Card.Equipment`
- `ValidCardToTarget$`: TODO: Describe this parameter.
  Observed values: `Aura.!Attached`

## `CantAttack`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `ExtraTurn`
- `DefenderNotNearestToYouInChosenDirection$`: TODO: Describe this parameter.
  Observed values: `True`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Mountain`, `Island`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+powerEQ1+toughnessEQ1`, `Artifact.YouCtrl+Other`, `Creature`, `Knight.YouCtrl,Soldier.YouCtrl`, `Creature.powerGE4+YouCtrl+Other`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GT1`, `LE3`, `LT5`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LE4`, `LT1`, `LT7`
- `Target$`: TODO: Describe this parameter.
  Observed values: `Card.Self+AttachedTo Creature`, `Player.!IsRemembered`, `Player.attackedBySourceThisTurn`, `Player.CardOwner`, `Player.CardOwner,Planeswalker.ControlledBy Player.CardOwner`, `You`, `You,Planeswalker.YouCtrl`
- `UnlessDefender$`: TODO: Describe this parameter.
  Observed values: `!controlsCreature.untapped+powerGE3`, `!controlsCreature.untapped+powerLE2`, `!controlsLand.untapped`, `controlsCreature.withFlying`, `controlsEnchantment,Permanent.enchanted`, `controlsForest`, `controlsIsland`, `controlsLand.Snow`, `controlsMountain`, `controlsPermanent.Blue`, `controlsSwamp`, `HasCardsInGraveyard_Card_GE7`, `hasFewerCreaturesInPlayThanYou`, `hasFewerLandsInPlayThanYou`, `isMonarch`, `IsPoisoned`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+nonArtifact+!namedAkron Legionnaire`, `Card.Self`, `Creature.ControlledBy Opponent.castSpellThisTurn`, `Creature`, `Creature.EquippedBy`, `Creature.EnchantedBy`, `Creature.withoutFlying+!hasKeywordLandwalk:Island`, `Creature.Inkling`, `Creature.Black`, `Creature.powerGTX`

## `CantAttack,CantBlock`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `PlayerCountPropertyYou$HasPropertyMaxSpeed`, `X`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Giant.Other+YouCtrl`, `Creature.Other+YouCtrl`, `Creature.PairedWith+withSoulbond`, `Card.YouOwn`, `Card`, `Creature.Other+YouCtrl+powerGE4`, `Permanent.YouOwn`, `Land.YouCtrl`, `Enchantment`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LE2`, `LE6`, `LE7`, `LT7`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Hand`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE2`, `LT3`, `LT5`, `LT8`, `NE1`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EnchantedBy+nonHuman`, `Creature.EnchantedBy`, `Creature.EnchantedBy+ControlledBy Player.Other`, `Sculpture.YouCtrl`, `Creature.Self`, `Creature.counters_GE1_BRIBERY`, `Creature.OppCtrl+HasCounters`, `Creature.Black`, `Creature.namedRock Lobster`

## `CantAttack,CantBlock,CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`, `Card.EnchantedBy`, `Creature.withFlying`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.!ManaAbility`, `Activated.hasTapCost`

## `CantAttack,CantBlock,CantCrew`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`

## `CantAttack,CantBlock,CantCrew,CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.EnchantedBy`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.!ManaAbility`

## `CantAttack,CantBlock,CantTransform`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`

## `CantAttackUnless`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `X`, `Y`, `2`, `Sac<1/Land>`, `Return<1/Enchantment>`, `tapXType<1/Creature.!attacking>`, `Sac<2/Island>`, `WP`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+untapped`
- `RememberingAttacker$`: TODO: Describe this parameter.
  Observed values: `True`
- `Target$`: TODO: Describe this parameter.
  Observed values: `Planeswalker.YouCtrl`, `You`, `You,Planeswalker.YouCtrl`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.AttachedBy`, `Creature.nonBlack`, `Creature.Self`, `Creature.Green`, `Card.Self`, `Creature.HasCounters`, `Creature.Black`

## `CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.EnchantedBy`, `Player.NonActive`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `PlayerTurn`
- `Description$`: TODO: Describe this parameter.
- `Phases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Artifact,Creature,Planeswalker`, `Artifact`, `Creature`, `Artifact,Creature`, `Creature.EnchantedBy`, `Card.NamedCard`, `Card.EnchantedBy`, `Artifact,Creature,Enchantment`, `Artifact.OppCtrl`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.!ManaAbility`, `Activated.!ManaAbility+!Loyalty`, `Activated.Cycling`, `Activated.Loyalty`

## `CantBeCast`

TODO: Write documentation.

**Parameters:**
- `Caster$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent.attackedWithCreaturesThisTurn`, `Opponent.withMoreArtifactsThanYou`, `Opponent.withMoreCreaturesThanYou`, `Opponent.withMoreEnchantmentsThanYou`, `Player`, `Player.Active`, `Player.attackedBySourceThisCombat`, `Player.EnchantedBy`, `Player.EnchantedController`, `Player.NonActive`, `Player.Opponent`, `Player.Opponent+attackedYouTheirCurrentTurn,Player.Opponent+attackedYouCtrlTheirCurrentTurn_Planeswalker`, `You`, `You.attackedWithCreaturesThisTurn`, `You.NonActive`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$YourTurns`, `X`, `XJockey`, `Z`
- `cmcGT$`: TODO: Describe this parameter.
  Observed values: `Land`, `Turns`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `PlayerTurn`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Command`, `Graveyard,Hand,Library,Command,Stack`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Snow.Land+YouCtrl`, `Card.Self+AttachedTo Creature`, `Permanent.namedTidal Influence`, `Card.Self+attacking`
- `NumLimitEachTurn$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `OnlySorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Exile,Hand,Library,Command`, `Graveyard`, `Graveyard,Exile`, `Graveyard,Library`, `Hand`
- `Phases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LE0`, `LE3`, `LE7`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Card.NamedCard`, `Card`, `Card.ChosenType`, `Card.nonLand+sharesNameWith Remembered.ExiledWithSource`, `Card.Self`, `Card.nonLand+sharesNameWith ValidExile Card.ExiledWithSource`, `Card.setARN`, `Permanent`, `Card.sharesNameWith NonToken`

## `CantBeCopied`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `CantBeSuspected`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`

## `CantBlock`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `NotPlayerTurn`, `Threshold`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Land.YouCtrl+untapped`, `Minotaur.Other+YouCtrl`, `Wolf.Other+YouCtrl,Werewolf.Other+YouCtrl`, `Zombie.Other+YouCtrl`, `Vampire.YouCtrl`, `Card.EnchantedBy+YouDontCtrl`, `Goblin.YouCtrl,Orc.YouCtrl`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GEX`, `LT4`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.IsGoaded+OppCtrl`, `Creature.EnchantedBy`, `Creature.Self`, `Creature.EquippedBy`, `Creature.Beast`, `Creature.EnchantedBy+Black`, `Creature.White,Creature.Blue`, `Creature.Black`

## `CantBlockBy`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$CommittedCrimeThisTurn.1.0`, `JoinedParty`, `SaccedThisTurn`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Blessing`, `PlayerTurn`, `Threshold`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Land.Snow+DefenderCtrl`, `Artifact.DefenderCtrl`, `Enchantment.DefenderCtrl`, `Card.Other+attacking`, `Card.Self+tapped`, `Card.attacking`, `Card.Self+counters_GE1_LEVEL`, `Land.DefenderCtrl+untapped`, `Planeswalker.Jace+YouCtrl`, `Creature.YouCtrl+Other`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE3`, `GE8`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQY`, `GE2`, `GE8`, `LT3`
- `ValidAttacker$`: TODO: Describe this parameter.
  Observed values: `Card.EnchantedBy`, `Card.Self`, `Card.Self+attacking`, `Card.Self+counters_GE4_OIL`, `Card.Self+enchanted`, `Creature`, `Creature.Artifact`, `Creature.Black`, `Creature.Blue+YouCtrl`, `Creature.Detective`, `Creature.enchanted+YouCtrl`, `Creature.EnchantedBy`, `Creature.EnchantedBy+attacking`, `Creature.EnchantedBy+Blue`, `Creature.EquippedBy`, `Creature.EquippedBy+powerLE3`, `Creature.Human`, `Creature.Kraken+YouCtrl,Creature.Leviathan+YouCtrl,Creature.Octopus+YouCtrl,Creature.Serpent+YouCtrl`, `Creature.NoAbilities+YouCtrl`, `Creature.powerGE2`, `Creature.powerGE3`, `Creature.powerGTX`, `Creature.powerLE2`, `Creature.Self`, `Creature.Self+attacking`, `Creature.Self,Creature.EnchantedBy`, `Creature.Sliver`, `Creature.Warrior`, `Creature.White+powerGE2`, `Creature.withoutFlying`, `Creature.YouCtrl`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+powerLE1,Creature.YouCtrl+toughnessLE1`, `Creature.YouCtrl+powerLE2`, `Detective.YouCtrl`, `Fish.YouCtrl`, `Juggernaut.YouCtrl`, `Spider.YouCtrl`
- `ValidAttackerRelative$`: TODO: Describe this parameter.
  Observed values: `Creature.powerGEIronclawX`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Artifact.Creature`, `Card.nonVehicle`, `Creature.!ControlledBy EnchantedOwner`, `Creature.!NoAbilities`, `Creature.Artifact`, `Creature.Black`, `Creature.Black,Creature.Red`, `Creature.Blue`, `Creature.ControlledBy Player.isMonarch`, `Creature.Coward`, `Creature.Dinosaur`, `Creature.Eldrazi+Scion`, `Creature.enchanted,Creature.Enchantment`, `Creature.EnchantedBy`, `Creature.EnchantedBy+nonDetective,Creature.EnchantedBy+YouDontCtrl`, `Creature.Glimmer`, `Creature.Green`, `Creature.Human`, `Creature.Knight,Creature.Wall`, `Creature.noName`, `Creature.nonArtifact`, `Creature.nonArtifact+nonRed`, `Creature.nonArtifact+nonWhite`, `Creature.nonBlack`, `Creature.nonBlue`, `Creature.nonKraken+nonLeviathan+nonOctopus+nonSerpent`, `Creature.nonLegendary`, `Creature.nonRogue`, `Creature.nonSliver`, `Creature.nonSpirit`, `Creature.nonWall`, `Creature.OppCtrl+cmcEven`, `Creature.Ox`, `Creature.powerGE2`, `Creature.powerGE3`, `Creature.powerGE4`, `Creature.powerGE7`, `Creature.powerGTX`, `Creature.powerLE1`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.powerLEX`, `Creature.powerLTX`, `Creature.powerLTY`, `Creature.Red`, `Creature.Saproling`, `Creature.Self`, `Creature.Spirit`, `Creature.token`, `Creature.toughnessGE3`, `Creature.Vampire,Creature.Zombie`, `Creature.Wall`, `Creature.White`, `Creature.withDefender`, `Creature.withFlying`, `Creature.withHorsemanship`, `Creature.withoutDefender`, `Creature.withoutFlying`, `Creature.withoutFlying+nonWall`, `Creature.withoutFlying+withoutReach`, `Creature.withoutFlying+withoutReach+OppCtrl`, `Creature.YouDontCtrl+powerLTX`
- `ValidDefender$`: TODO: Describe this parameter.
  Observed values: `Player.Condition Counters.RAD`

## `CantBlockUnless`

TODO: Write documentation.

**Parameters:**
- `Attacker$`: TODO: Describe this parameter.
  Observed values: `Creature.AttachedBy`, `Creature.powerGE3`, `Creature.YouCtrl`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `Y`, `PayLife<1>`, `tapXType<1/Creature.!blocking>`, `2`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+attacking`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.AttachedBy`, `Creature.nonBlue`, `Card.Self`

## `CantChangeDayTime`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `NewTime$`: TODO: Describe this parameter.
  Observed values: `Night`

## `CantChangeLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CantDiscard`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ForCost$`: TODO: Describe this parameter.
  Observed values: `False`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CantDraw`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `DrawLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`

## `CantExile`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ForCost$`: TODO: Describe this parameter.
  Observed values: `False`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+token`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Triggered.YouCtrl`

## `CantGainLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.EnchantedBy`, `Player.Opponent`

## `CantPayLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ForCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Spell,Activated`, `Spell,Activated.!ManaAbility`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `CantPhaseIn`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.phasedOutPermanent`

## `CantPlayLand`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `RockyX`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Land`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `Player$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent.withMoreLandsThanYou`, `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.setARN`, `Land.nonBasic+sharesNameWith NonToken`, `Land.NamedCard`, `Land`

## `CantPreventDamage`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `IsCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE5`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Spell.Self`, `Card.Self`, `Creature.YouCtrl`

## `CantPutCounter`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `M1M1`, `P1P1`, `POISON`
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Card.EnchantedBy`, `Creature.YouCtrl`, `Card.Self+inZoneBattlefield`, `Creature.inZoneBattlefield,Artifact.inZoneBattlefield,Enchantment.inZoneBattlefield,Land.inZoneBattlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`

## `CantSacrifice`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ForCost$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.EquippedBy`, `Creature.YouCtrl+YouDontOwn`, `Card.YouCtrl`, `Creature.YouCtrl+token`, `Permanent.nonLand`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Spell,Activated`, `SpellAbility.OppCtrl`, `Triggered.YouCtrl`

## `CantTarget`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.Opponent`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Graveyard`, `Graveyard`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SourceCanOnlyTarget$`: TODO: Describe this parameter.
  Observed values: `Wall`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated,Triggered`, `Spell`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Aura`, `Spell.Self`, `Card.Black,Card.Red`, `Card.nonGreen`, `Card.Blue,Card.Black`, `Card.Black`, `Card.White`, `Card.Blue`, `Card.Red`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`, `Card.EnchantedBy`, `Card.Self`, `Creature`, `Permanent.untapped`, `Creature.untapped`, `Card.Self+!attackedThisTurn+!blockedThisTurn`, `Creature.YouCtrl`, `Land`

## `CantTransform`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.Werewolf+nonHuman+YouCtrl`

## `CantVenture`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent.VenturedThisTurn`

## `CastWithFlash`

TODO: Write documentation.

**Parameters:**
- `Caster$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Ferocious`, `PlayerTurn`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking`, `Permanent.Green+YouCtrl,Permanent.Blue+YouCtrl`, `Faerie.YouCtrl`, `Card.Self+powerEven`, `Card.Self+powerOdd`, `Creature.YouCtrl+attacking+Legendary`, `Lesson.YouOwn`, `Instant.YouOwn,Sorcery.YouOwn`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Creature.blocking`
- `Phases$`: TODO: Describe this parameter.
  Observed values: `End of Turn`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GE3`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Enchantment`, `Spirit`, `Card.Self`, `Card`, `Sorcery`, `Artifact,Card.Legendary`, `Card.nonCreature`, `Creature`, `Artifact,Card.Colorless`, `Ally,Artifact`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Equip`, `Activated.Loyalty`, `Spell`, `Spell.IsTargeting Valid Card.IsCommander`, `Spell.IsTargeting Valid Permanent.YouCtrl`, `Spell.XCostLE3`

## `ColorlessDamageSource`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.Black+inZoneBattlefield,Permanent.Red+inZoneBattlefield,Spell.Black+inZoneStack,Spell.Red+inZoneStack`

## `CombatDamageToughness`

TODO: Write documentation.

**Parameters:**
- `Condition$`: TODO: Describe this parameter.
  Observed values: `PlayerTurn`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.powerLTtoughness+YouCtrl`, `Creature.withDefender+YouCtrl`, `Creature.YouCtrl`, `Creature.EquippedBy+powerLTtoughness`, `Creature`, `Creature.EnchantedBy`, `Creature.EnchantedBy+withVigilance`, `Card.Self`

## `Continuous`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `AddAbility$`: TODO: Describe this parameter.
  Observed values: `AnyMana`, `AbundantGrowthTap`, `Damage`, `AdagioCopy`, `ABMana`, `ABPump`, `GainLife`, `ABDealDamage`, `ArcheryDamage`, `Pump`
- `AddAllCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `AddColor$`: TODO: Describe this parameter.
  Observed values: `Black`, `Blue`, `ChosenColor`, `White`
- `AddHiddenKeyword$`: TODO: Describe this parameter.
  Observed values: `All creatures able to block CARDNAME do so.`, `CARDNAME can only attack alone.`, `CARDNAME can't attack alone.`, `CARDNAME can't attack or block.`, `CARDNAME can't block.`, `CARDNAME count as Flame Burst.`, `CARDNAME count as Muscle Burst.`, `CARDNAME must be blocked if able.`, `Lethal damage dealt to CARDNAME is determined by its power rather than its toughness.`, `Other players can't gain control of CARDNAME.`, `This card doesn't untap during your next untap step.`
- `AdditionalOptionalVote$`: TODO: Describe this parameter.
  Observed values: `1`
- `AdditionalVillainousChoice$`: TODO: Describe this parameter.
  Observed values: `1`
- `AdditionalVote$`: TODO: Describe this parameter.
  Observed values: `1`
- `AddKeyword$`: TODO: Describe this parameter.
  Observed values: `Vigilance`, `Cascade`, `Flying`, `Shroud`, `Protection from black`, `Protection from red`, `Protection:Player.Opponent:each of your opponents`, `Lifelink`, `First Strike & MustBeBlockedBy Creature.Dalek`, `Indestructible`
- `AddNames$`: TODO: Describe this parameter.
  Observed values: `AllNonLegendaryCreatureNames`
- `AddPower$`: TODO: Describe this parameter.
  Observed values: `+2`, `+X`, `-1`, `-13`, `-2`, `-3`, `-4`, `-5`, `-6`, `-AffectedX`, `-AttackingX`, `-NotAttackingX`, `-X`, `1`, `10`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `AffectedX`, `Count$CardNumAttacksThisGame/Twice`, `Count$YourSpeed`, `X`, `Y`, `Z`
- `AddReplacementEffect$`: TODO: Describe this parameter.
  Observed values: `DamageRep`, `DBUntap`, `Draw`, `PulmonicMoveToLibrary`, `RDamage1`, `RDamage2`, `RepDraw`, `This & Other`, `YouCantLose & OppCantWin`
- `AddStaticAbility$`: TODO: Describe this parameter.
  Observed values: `AnthemStatic`, `BloodEquip`, `BroodshipStatic`, `BuffTokens`, `BurgeoningUntap`, `CarrierStatic`, `CraftStatic`, `DBStatic`, `DragonReduce`, `DragonsST`, `EquipAB`, `EquipPump`, `ExplorationStatic`, `FoodEquip`, `FreebieReaving`, `Hexproof`, `MarduHarmonicon`, `Masarmonicon`, `MaxSpeedStatic`, `NoMaxHandSize`, `NoSacEOT`, `PowerGrave`, `RaiseCost`, `Roomharmonicon`, `RuneFlightST`, `RuneMightST`, `RuneMortalityST`, `RuneSpeedST`, `RuneSustenanceST`, `SBoost`, `SCantBlock`, `SedgeSliverST`, `SelfDT & WideFS`, `SPump1`, `SPump2`, `Static`, `StaticLook`, `StaticPump`, `STFirstStrike`, `SultaiStatic`, `TemurStatic`, `TreasureEquip`
- `AddSVar$`: TODO: Describe this parameter.
  Observed values: `AE`, `AnimalBoneyardX`, `DNEq`, `AtRaVZombie`, `EnMe`, `AvariceUpkeepSVar`, `BearUmbraUntap & HasAttackEffect`, `SlasherSac & SlasherTarget`, `EqMe`, `DelayedReturn,TrigReturn`
- `AddToughness$`: TODO: Describe this parameter.
  Observed values: `-1`, `-2`, `-3`, `-4`, `-AffectedX`, `-AttackingY`, `-NotAttackingY`, `-X`, `1`, `10`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `AffectedX`, `Count$CardNumAttacksThisGame/Twice`, `X`, `Y`, `Z`
- `AddTrigger$`: TODO: Describe this parameter.
  Observed values: `DrawTrig`, `Dies`, `AttacksPlayer`, `AttackTrig`, `TrigDamageDone`, `AtRaVDie`, `TrigSpellCast & TrigDrawn`, `UpkeepCostTrigger`, `AvariceUpkeepTrig`, `AbzanTrigger`
- `AddType$`: TODO: Describe this parameter.
  Observed values: `ChosenType`, `Creature`, `Symbiote`, `Creature & Elf`, `Creature & Frog`, `Angel`, `Land`, `Equipment`, `Forest & Land`, `Wizard`
- `AdjustLandPlays$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `Unlimited`
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Permanent.Other+YouCtrl`, `Creature.enchanted+YouCtrl`, `Card.Self`, `Creature.Other+YouCtrl`, `Creature.Land+YouCtrl`, `Card.YouCtrl+YouOwn+wasCastFromHand+cmcLEX`, `Card.nonLand+YouOwn+withCycling,Card.nonLand+YouOwn+withTypeCycling`, `Card.EnchantedBy`, `Creature.EnchantedBy`, `Creature`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Library`, `Battlefield,Stack`, `Exile`, `Exile,Graveyard`, `Graveyard`, `Graveyard,Stack`, `Hand`, `Hand,Graveyard,Exile,Command,Library`, `Hand,Graveyard,Exile,Library,Command`, `Hand,Graveyard,Exile,Library,Command,Stack`, `Hand,Graveyard,Library,Exile,Command`, `Hand,Library,Graveyard,Exile,Command`, `Hand,Library,Graveyard,Exile,Command,Stack`, `Library`, `Library,Battlefield`, `Library,Hand`, `Stack`, `Stack,Battlefield`
- `CalcKeywordN$`: TODO: Describe this parameter.
  Observed values: `X`
- `CanBlockAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `7`, `99`, `X`
- `CanBlockAny$`: TODO: Describe this parameter.
  Observed values: `True`
- `CantHaveKeyword$`: TODO: Describe this parameter.
  Observed values: `Deathtouch`, `First Strike`, `Flying`, `Hexproof`, `Trample`
- `ChangeColorWordsTo$`: TODO: Describe this parameter.
  Observed values: `ChosenColor`
- `CharacteristicDefining$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `CheckSecondSVar$`: TODO: Describe this parameter.
  Observed values: `Y`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Celebration`, `CheckArtifact`, `CheckAttacking`, `CheckBattle`, `CheckCreature`, `CheckEnchantment`, `CheckInstant`, `CheckKindred`, `CheckLand`, `CheckPlaneswalker`, `CheckSorcery`, `Count$CommittedCrimeThisTurn.1.0`, `Count$YouRolledThisTurn6`, `CurrentLife`, `RaidTest`, `SaccThisTurn`, `VarFSLif`, `VarFSVig`, `VarVigLif`, `X`, `Y`, `Z`
- `CheckThirdSVar$`: TODO: Describe this parameter.
  Observed values: `Z`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Blessing`, `Delirium`, `Desert`, `FatefulHour`, `Hellbent`, `MaxSpeed`, `Metalcraft`, `Monarch`, `NotPlayerTurn`, `PlayerTurn`, `Threshold`
- `ControlOpponentsSearchingLibrary$`: TODO: Describe this parameter.
  Observed values: `You`
- `DeclaresBlockers$`: TODO: Describe this parameter.
  Observed values: `AttackingPlayer`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Command`, `Exile`, `Exile,Graveyard`, `Graveyard`, `Stack`
- `ExcludeZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `FromDraftNotes$`: TODO: Describe this parameter.
  Observed values: `Animus of Predation`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `Player.isMonarch`, `You`
- `GainsAbilitiesLimitPerTurn$`: TODO: Describe this parameter.
  Observed values: `1`
- `GainsAbilitiesOf$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouOwn`, `Card.ChosenCard`, `Card.counters_GE1_BRAIN`, `Card.ExiledWithSource`, `Card.IsImprinted+ExiledWithSource`, `Card.YouOwn+counters_GE1_CAGE`, `Creature`, `Creature.ExiledWithSource`, `Creature.Legendary+YouCtrl`, `Creature.OppCtrl`, `Creature.Other+counters_GE1_P1P1`, `Creature.TopLibrary+YouCtrl,Artifact.TopLibrary+YouCtrl`, `Creature.YouCtrl+!sharesNameWith Self`, `Goblin.TopLibrary+YouCtrl`, `Land`, `Land.ExiledWithSource`, `Land.OppCtrl`, `Permanent.Other`, `Planeswalker.Other`
- `GainsAbilitiesOfDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ExiledWith`, `Self`
- `GainsAbilitiesOfZones$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Library`
- `GainsTriggerAbsOf$`: TODO: Describe this parameter.
  Observed values: `Card.ChosenCard`, `Card.ExiledWithSource`
- `GainsValidAbilities$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.!Loyalty`, `Activated.!ManaAbility`, `Activated.Loyalty`
- `GainTextAbilities$`: TODO: Describe this parameter.
  Observed values: `VolrathDiscard`
- `GainTextOf$`: TODO: Describe this parameter.
  Observed values: `TopOfGraveyard.Creature`
- `GameStage$`: TODO: Describe this parameter.
  Observed values: `Play`
- `Goad$`: TODO: Describe this parameter.
  Observed values: `True`
- `IgnoreEffectCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Lesson.YouOwn`, `Permanent.White+YouCtrl,Permanent.Black+YouCtrl`, `Permanent.Black+YouCtrl,Permanent.Green+YouCtrl`, `Artifact.YouCtrl`, `Permanent.YouOwn`, `Card.Self+attacking`, `Card.IsCommander+YouOwn+YouCtrl`, `Human.YouCtrl`, `Creature.nonWhite+nonArtifact+YouCtrl`, `Mountain.YouCtrl`
- `KeywordDefined$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `ManaConversion$`: TODO: Describe this parameter.
  Observed values: `AnyType->AnyColor`
- `MayLookAt$`: TODO: Describe this parameter.
  Observed values: `Player`, `True`, `You`
- `MayPlay$`: TODO: Describe this parameter.
  Observed values: `True`, `You`
- `MayPlayAltManaCost$`: TODO: Describe this parameter.
  Observed values: `0`, `CollectEvidence<10>`, `PayEnergy<1>`, `PayEnergy<8>`, `PayLife<ConvertedManaCost>`, `U`, `U U U U ExileFromGrave<4/Instant;Sorcery/instant or sorcery cards>`
- `MayPlayDontGrantZonePermissions$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayIgnoreColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayIgnoreType$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `MayPlayPlayer$`: TODO: Describe this parameter.
  Observed values: `ActivePlayer`, `CardOwner`, `Exiler`, `Player`, `Player.Active`
- `MayPlaySnowIgnoreColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayText$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Battle`, `Creature`, `Enchantment`, `Land`, `Planeswalker`
- `MayPlayWithFlash$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayWithoutManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `Phases$`: TODO: Describe this parameter.
  Observed values: `End of Turn`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE10`, `GE2`, `GE3`, `GE4`, `GE5`, `GE6`, `GE7`, `GE8`, `GE9`, `LT3`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Library`, `Stack`
- `RaiseCost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Card>`, `Discard<2/Card>`, `ExileFromGrave<1/Creature.Other/another creature card>`, `ExileFromGrave<3/Card/other cards>`, `ExileFromGrave<4/Instant;Sorcery/instant or sorcery cards>`, `PayLife<1>`, `PayLife<2> Sac<1/Artifact;Creature/artifact or creature>`, `PayLife<3>`, `PayLife<3> Discard<1/Card>`, `RemoveAnyCounter<1/Any/Creature>`, `RemoveAnyCounter<3/Any/Creature>`, `RemoveAnyCounter<6/Any/Creature>`, `Sac<1/Creature>`, `Sac<1/Permanent.nonLand/nonland permanent>`, `X`
- `RaiseMaxHandSize$`: TODO: Describe this parameter.
  Observed values: `-1`, `-2`, `-3`, `-4`, `-7`, `1`, `2`
- `RemoveAllAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveArtifactTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveKeyword$`: TODO: Describe this parameter.
  Observed values: `Deathtouch`, `First Strike`, `Flying`, `Flying & Landwalk:Island`, `Hexproof`, `Infect`, `Trample`
- `RemoveLandTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveNonManaAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveType$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Legendary`, `Planeswalker`, `Snow`
- `ReplaceGraveyard$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SecondSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE30`
- `SetColor$`: TODO: Describe this parameter.
  Observed values: `All`, `Black`, `Blue`, `ChosenColor`, `Colorless`, `Green`, `Green & White`, `Red`, `White`
- `SetMaxHandSize$`: TODO: Describe this parameter.
  Observed values: `11`, `2`, `20`, `4`, `5`, `8`, `Unlimited`, `X`, `Y`
- `SetName$`: TODO: Describe this parameter.
  Observed values: `ChosenName`, `Humble Merchant`, `Legitimate Businessperson`, `Radiant Swan`, `Sol Ring`
- `SetPower$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `16`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `AffectedX`, `ConsumingPT`, `Count$ValidGraveyard Card.YouOwn$CardTypes`, `ExiledCMC`, `LifePaidOnETB`, `TotalPower`, `X`, `Y`
- `SetToughness$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `AffectedX`, `ConsumingPT`, `Count$ValidGraveyard Card.YouOwn$CardTypes/Plus.1`, `LifePaidOnETB`, `TotalToughness`, `X`, `Y`
- `SharedKeywordsZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`
- `SharedRestrictions$`: TODO: Describe this parameter.
  Observed values: `Card.ExiledWithSource`, `Card.IsImprinted+ExiledWithSource`, `Creature`, `Creature.!namedEscaped Shapeshifter+OppCtrl`, `Creature.counters_GE1_BLOOD`, `Creature.delved`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQY`, `GE1`, `GE10`, `GE2`, `GE25`, `GE3`, `GE30`, `GE4`, `GE5`, `GE6`, `GE7`, `GE8`, `GEY`, `GEZ`, `GT1`, `GT4`, `GT9`, `GTY`, `LE1`, `LE10`, `LE20`, `LEX`, `LEY`, `LT1`, `LT5`, `LT7`, `LT8`
- `TopCardOfLibraryIs$`: TODO: Describe this parameter.
  Observed values: `Card.Black`, `Creature`, `Creature,Artifact`, `Goblin`, `Land`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Spell.cmcGE4`, `Spell.cmcLE2`, `Spell.cmcLE3`, `Spell.Creature+powerGE4`, `Spell.Insect`, `Spell.Knight`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell.Bestow`, `Spell.Blitz`, `Spell.Mutate`, `Spell.Warp`

## `Continuous,CantAttack,CantBlock,CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`
- `Description$`: TODO: Describe this parameter.
- `IgnoreEffectCost$`: TODO: Describe this parameter.
  Observed values: `ExileFromGrave<3/Card>`, `Sac<1/Permanent>`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.EnchantedBy`

## `Continuous,CantPlayLand,CantBeCast`

TODO: Write documentation.

**Parameters:**
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Player.withMostPermanentInPlay`
- `Caster$`: TODO: Describe this parameter.
  Observed values: `Player.withMostPermanentInPlay`
- `Description$`: TODO: Describe this parameter.
- `IgnoreEffectCost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/Permanent>`
- `Player$`: TODO: Describe this parameter.
  Observed values: `Player.withMostPermanentInPlay`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature,Enchantment,Land`

## `CountersRemain`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Devotion`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `DisableTriggers`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.OppCtrl+inZoneBattlefield`, `Creature.OppCtrl+inZoneBattlefield`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature,Artifact`, `Permanent`
- `ValidMode$`: TODO: Describe this parameter.
  Observed values: `ChangesZone,ChangesZoneAll`
- `ValidTrigger$`: TODO: Describe this parameter.
  Observed values: `Triggered.Ward`

## `FlipCoinDoubler`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `FlipCoinMod`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$YouFlipThisTurn`
- `Description$`: TODO: Describe this parameter.
- `Result$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `GainLifeRadiation`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `IgnoreHexproof`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `You`
- `Description$`: TODO: Describe this parameter.
- `ValidEntity$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Permanent.OppCtrl,Opponent`

## `IgnoreLandWalk`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Creature.EnchantedBy`
- `ValidKeyword$`: TODO: Describe this parameter.
  Observed values: `Landwalk:Forest`, `Landwalk:Island`, `Landwalk:Mountain`, `Landwalk:Plains`, `Landwalk:Swamp`

## `IgnoreLegendRule`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.namedBrothers Yamazaki`, `Permanent.Legendary+YouCtrl+namedSyr Joshua and Syr Saxon`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.namedBrothers Yamazaki`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl`, `Sliver.YouCtrl`, `Spider.YouCtrl`, `Permanent.YouCtrl+Legendary+namedSyr Joshua and Syr Saxon`, `Creature.YouCtrl+token`, `Card.IsCommander+YouCtrl`

## `InfectDamage`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `UnlifeCondition`
- `Description$`: TODO: Describe this parameter.
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE0`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `You`

## `ManaBurn`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.

## `ManaConvert`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ManaConversion$`: TODO: Describe this parameter.
  Observed values: `AnyType->AnyColor`, `AnyType->AnyType`, `Blue->AnyColor`, `White->AnyColor nonWhite<-C`, `White->Red`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inZoneBattlefield`, `Case.YouCtrl`, `Creature.YouCtrl+cmcEQChosen`, `Card.Self`, `Card.YouDontOwn+YouCtrl`, `Planeswalker.YouCtrl`, `Card.NamedCard`, `Creature.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Spell`, `Spell,Activated`

## `MaxCounter`

TODO: Write documentation.

**Parameters:**
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `DREAM`
- `Description$`: TODO: Describe this parameter.
- `MaxNum$`: TODO: Describe this parameter.
  Observed values: `7`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `MinMaxBlocker`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouOwn`
- `Max$`: TODO: Describe this parameter.
  Observed values: `1`
- `Min$`: TODO: Describe this parameter.
  Observed values: `3`, `6`, `All`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EnchantedBy`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl`, `Creature.Self`, `Creature.YouCtrl+HasCounters`, `Boar.YouCtrl`, `Creature.EquippedBy`, `Creature.YouCtrl+withMenace`

## `MustAttack`

TODO: Write documentation.

**Parameters:**
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Threshold`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.namedAdvocate of the Beast+YouCtrl`, `Ally.Other+YouCtrl`
- `MustAttack$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCreature$`: TODO: Describe this parameter.
  Observed values: `Card.EquippedBy`, `Card.Self`, `Card.Self,Creature.EnchantedBy`, `Creature`, `Creature.EnchantedBy`, `Creature.EnchantedPlayerCtrl`, `Creature.Goblin`, `Creature.Goblin+Other+YouCtrl`, `Creature.OppCtrl`, `Creature.YouCtrl`, `Juggernaut.YouCtrl`, `Skeleton.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent.NotedDefender`

## `MustBlock`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCreature$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Self,Card.EnchantedBy`, `Creature`

## `MustTarget`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell.OppCtrl,Activated.OppCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Flagbearer`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `NoCleanupDamage`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.OppCtrl`

## `NumLoyaltyAct`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Twice$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Planeswalker.YouCtrl`, `Card.Self`

## `OptionalAttackCost`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Exert<1/CARDNAME>`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.Self+notExertedThisTurn`
- `Trigger$`: TODO: Describe this parameter.
  Observed values: `DBDraw`, `TrigCanNotBlock`, `TrigChangeZone`, `TrigCopy`, `TrigDealDamage`, `TrigEffect`, `TrigExile`, `TrigPump`, `TrigPumpAll`, `TrigUntapAll`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `OptionalCost`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `You`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `CollectEvidence<8>`, `CollectEvidence<6>`, `Blight<1>`, `ChooseCreatureType<1> Behold<2/Creature.ChosenType>`, `PayLife<2>`, `Behold<1/Dragon>`, `Reveal<1/Dragon>`, `RevealOrChoose<1/Dragon>`, `Sac<1/Creature.nonDemon/non-Demon creature>`, `Waterbend<2>`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`
- `ReduceColor$`: TODO: Describe this parameter.
  Observed values: `B`, `G`, `R`, `U`, `W`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Permanent.Blue`, `Permanent.White`, `Permanent.Black`, `Permanent.Red`, `Permanent.Green`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`

## `Panharmonicon`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Description$`: TODO: Describe this parameter.
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Shrine.YouCtrl`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidActivator$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouCtrl`, `Creature.YouCtrl+Legendary`, `Doctor.YouCtrl`, `Card.Self+equipped,Equipment.Attached`, `Creature.YouCtrl+powerLE2`, `Card.YouCtrl+Colorless+Other`, `Dungeon.YouOwn`, `Shaman.YouCtrl,Wizard.Other+YouCtrl`, `Ally.YouCtrl`, `Creature.Other+YouCtrl+ChosenType`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature`, `Creature`, `Creature.YouCtrl`, `Instant,Sorcery`, `Land`, `Land.YouCtrl,Bird.YouCtrl`, `Permanent`, `Permanent.Legendary,Artifact`, `Wizard.YouCtrl`
- `ValidMode$`: TODO: Describe this parameter.
  Observed values: `Attacks,AttackersDeclared,AttackersDeclaredOneTarget`, `BecomesTarget,BecomesTargetOnce`, `ChangesZone,ChangesZoneAll`, `DamageDone,DamageDoneOnce,DamageDealtOnce,DamageAll`, `DamageDoneOnce,DamageDone`, `Drawn`, `RoomEntered`, `SpellCast,SpellCopy,SpellCastOrCopy`, `TurnFaceUp`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Player`, `Creature.YouCtrl`
- `ValidTurned$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Stack`, `Command`

## `PhaseReversed`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `PlayerMustAttack`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `MustAttack$`: TODO: Describe this parameter.
  Observed values: `You,Planeswalker.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `PlotZone`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.TopLibrary+YouCtrl+nonLand`

## `RaiseCost`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.EnchantedBy`, `Player.NonActive`, `Player.Opponent`, `You`
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `AdditionalCostPayTimesG`, `AdditionalCostPayTimesR`, `IncreaseCost`, `PseudoKicker`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `NotPlayerTurn`, `PlayerTurn`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Discard<X/Creature/creature(s)>`, `W`, `B`, `Waterbend<5>`, `Sac<1/Land>`, `AddCounter<1/LOYALTY>`, `BeholdExile<1/Kithkin>`, `BeholdExile<1/Elemental>`, `BeholdExile<1/Goblin>`, `BeholdExile<1/Elf>`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Command`, `Stack`
- `ForEachShard$`: TODO: Describe this parameter.
  Observed values: `Black`
- `OnlyFirstSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `Relative$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Ability`, `Spell`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.White`, `Card.Black`, `Card.NamedCard`, `Card.ChosenType`, `Artifact,Enchantment`, `Card.wasCastFromGraveyard,Card.wasCastFromExile`, `Rebel.!token`, `Card.OppOwn+DrawnThisTurn`, `Planeswalker.YouCtrl`
- `ValidSpell$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.!ManaAbility`, `Activated.Loyalty`, `Activated.ManaAbility`, `Spell`, `Spell,Activated.!ManaAbility`, `Spell.Flashback`, `Static.MorphUp`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Dragon`, `Card.IsCommander+YouCtrl+inZoneBattlefield`, `Spell.Self`, `Creature.YouCtrl+inZoneBattlefield,Planeswalker.YouCtrl+inZoneBattlefield`, `Merfolk.YouCtrl+inZoneBattlefield`, `Creature`

## `ReduceCost`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.Opponent`, `You`, `You.Active`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Hand`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `6`, `8`, `AffectedX`, `Col`, `CommanderCast`, `CostReduction`, `Count$CountersRemovedThisTurn ENERGY You`, `Count$ValidGraveyard Land.YouOwn`, `Count$YouDrewThisTurn`, `Count$YourSpeed`, `ReduceCost`, `SacrificedPermanentsTypes`, `Tapped`, `X`, `XGrave`, `Y`, `Z`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ArtAct`, `Count$CommittedCrimeThisTurn.1.0`, `Count$Valid Creature.nonHuman+YouCtrl`, `NeedHope`, `OppCastThisTurn`, `RaidTest`, `X`, `Y`, `YouCastThisTurn`, `YourLife`
- `Color$`: TODO: Describe this parameter.
  Observed values: `1 U`, `2 U`, `2 U U`, `B`, `B R`, `G`, `R`, `U`, `U U U`, `W B`, `W U B R G`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Metalcraft`, `Night`, `NotPlayerTurn`, `PlayerTurn`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Command`, `Command`, `Stack`
- `FirstForetell$`: TODO: Describe this parameter.
  Observed values: `True`
- `IgnoreGeneric$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Wizard.YouCtrl`, `Creature.Legendary+YouCtrl`, `Artifact.YouCtrl`, `Enchantment.YouCtrl`, `Creature.YouCtrl+powerGE4`, `Desert.YouCtrl`, `Card.YouOwn`, `Card.Self+tapped`, `Zombie.YouCtrl`, `Card.IsCommander+YouOwn+YouCtrl`
- `MinMana$`: TODO: Describe this parameter.
  Observed values: `1`
- `OnlyFirstSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `Phases$`: TODO: Describe this parameter.
  Observed values: `End of Turn`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE10`, `GE2`, `GE3`, `GE8`, `GE9`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `Relative$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE10`, `GE2`, `GE3`, `GE4`, `GE7`, `GT9`, `LE1`, `LE3`, `LE5`, `LEY`, `LTZ`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Ability`, `Foretell`, `Spell`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`, `Card`, `Demon,Horror,Nightmare`, `Creature`, `Instant,Sorcery`, `Card.Artifact`, `Kithkin,Soldier`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Permanent.AdventureCard`
- `ValidSpell$`: TODO: Describe this parameter.
  Observed values: `Activated.!ManaAbility`, `Activated.Boast`, `Activated.Cycling`, `Activated.Equip`, `Activated.Exhaust`, `Activated.Ninjutsu`, `Activated.YouCtrl`, `Spell.Bargain`, `Spell.Blitz`, `Spell.Buyback`, `Spell.Dash`, `Spell.Flashback`, `Spell.Instant,Spell.Sorcery`, `Spell.isCastFaceDown`, `Spell.Kicked`, `Static.Foretelling`, `Static.Plotting`, `Static.Unlock`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Player.EnchantedBy`, `Creature.Legendary+YouCtrl`, `Creature.tapped`, `Creature.wasDealtDamageThisTurn`, `Permanent.Black`, `Creature.attacking`, `Creature.blocking`, `Creature.attacking,Creature.tapped`, `Creature.Colorless`

## `SetCost`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `3`
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+untapped`
- `RaiseTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`

## `SurveilNum`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Num$`: TODO: Describe this parameter.
  Observed values: `2`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `TapPowerValue`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`, `Creature.powerLTtoughness+YouCtrl`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Crew+Vehicle`, `Activated.Crew+Vehicle,Activated.Saddle+Mount`, `Activated.Crew+Vehicle,Activated.Station`, `Activated.Saddle+Mount,Activated.Crew+Vehicle`, `Activated.Station`
- `Value$`: TODO: Describe this parameter.
  Observed values: `2`, `Toughness`

## `TurnReversed`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Description$`: TODO: Describe this parameter.
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GT2`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `UnspentMana`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ManaType$`: TODO: Describe this parameter.
  Observed values: `Green`, `Red`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `UntapOtherPlayer`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE4_QUEST`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`, `Permanent`, `Permanent.YouCtrl`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.Green+YouCtrl,Creature.Blue+YouCtrl`, `Archer.YouCtrl`, `Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouCtrl`

## `WitherDamage`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
