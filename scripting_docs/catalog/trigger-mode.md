# Discovered Forge Terms

<!-- forge-doc-scope: T: -->

## `Abandoned`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.Self`

## `AbilityCast`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `LifePaid`, `Sacrificed`
- `Execute$`: TODO: Describe this parameter.
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsValid$`: TODO: Describe this parameter.
  Observed values: `Player,Creature.inZoneBattlefield`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.AttachedBy`, `Artifact.inZoneBattlefield,Creature.inZoneBattlefield`, `Artifact.inZoneBattlefield`, `Creature.EquippedBy+inRealZoneBattlefield`, `Elemental.inZoneBattlefield`, `Planeswalker.Chandra`, `Planeswalker.EnchantedBy+inRealZoneBattlefield`, `Artifact.inZoneBattlefield,Creature.inZoneBattlefield,Land.inZoneBattlefield`, `Artifact`, `Card.Self`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.!hasTapCost`, `Activated.!ManaAbility`, `Activated.Boast`, `Activated.Eternalize,Activated.Embalm`, `Activated.Exhaust`, `Activated.Exhaust+!ManaAbility`, `Activated.Loyalty`, `Activated.Ninjutsu`, `Activated.OppCtrl`, `Activated.Outlast`, `SpellAbility`, `SpellAbility.!ManaAbility`, `SpellAbility.!ManaAbility+hasTapCost`, `SpellAbility.!ManaAbility+ManaSpent GE4`
- `ValidSAonCard$`: TODO: Describe this parameter.
  Observed values: `Activated.YouCtrl`

## `AbilityResolves`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `ActivateOnce`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Saga.YouCtrl`, `Card.Self`
- `ValidSpellAbility$`: TODO: Describe this parameter.
  Observed values: `Ability.LastChapter`, `SpellAbility.ManaAbility`, `Triggered.LastChapter`

## `AbilityTriggered`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggeredOwnAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidDestination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidMode$`: TODO: Describe this parameter.
  Observed values: `Attacks,AttackersDeclared,AttackersDeclaredOneTarget`, `ChangesZone,ChangesZoneAll`, `CounterAdded`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Creature.YouCtrl`, `Saga.YouCtrl`
- `ValidSpellAbility$`: TODO: Describe this parameter.
  Observed values: `Triggered.LastChapter`

## `Adapt`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`

## `AlternativeCost`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ReavingX`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `0`, `PayLife<ConvertedManaCost>`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `LT1`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Unearth`, `Spell`

## `Always`

TODO: Write documentation.

**Parameters:**
- `CardsInGraveyardGE$`: TODO: Describe this parameter.
  Observed values: `1`
- `CardsInHandGE$`: TODO: Describe this parameter.
  Observed values: `2`
- `CardsInHandLE$`: TODO: Describe this parameter.
  Observed values: `2`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `NumScrolls`, `OpponentSmallest`, `X`
- `Execute$`: TODO: Describe this parameter.
- `HasColorCreatureInPlay$`: TODO: Describe this parameter.
  Observed values: `GWU`, `RGW`
- `HasColorInGraveyard$`: TODO: Describe this parameter.
  Observed values: `U`
- `HasCreatureInPlay$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_EQ0_P1P1`, `Swamp.YouCtrl`, `Creature.counters_GE4_FUSE`, `Card.Self+OwnerDoesntControl`, `Permanent.!token+setARN+Other`, `Artifact.YouCtrl`, `Island.YouCtrl`, `Card.Self+counters_EQ0_ICE`, `Card.Self+counters_GEX_CHARGE+YouCtrl`, `Card.Self+counters_GE5_PLOT`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self+Enchantment`
- `LifeAmount$`: TODO: Describe this parameter.
  Observed values: `GE20`, `GE30`, `LE10`
- `LifeTotal$`: TODO: Describe this parameter.
  Observed values: `You`
- `LowPriority$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxRollsPerTurn$`: TODO: Describe this parameter.
  Observed values: `9`
- `MinTurn$`: TODO: Describe this parameter.
  Observed values: `1`, `3`
- `OppHasCreatureInPlay$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE7`
- `PresentCompare2$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentPlayer2$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Library`
- `PresentZone2$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `ResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `IsPresent`, `IsPresent2`
- `RollInMain1$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE10`, `LE10`, `LEY`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`

## `AssignCombatDamageAsUnblocked`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.EffectSource`, `Card.IsRemembered`, `Creature.YouCtrl`

## `AssignNoCombatDamage`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource`, `Card.IsRemembered`

## `Attached`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetRelativeToSource$`: TODO: Describe this parameter.
  Observed values: `Permanent.nonLand+OppCtrl+cmcLEX`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Aura`, `Aura.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Card.Self`, `Creature.YouCtrl`

## `AttackerBlocked`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.Wall+Other+sharesBlockingAssignmentWith`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Creature.nonWall+sharesBlockingAssignmentWith`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentCompare2$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Card.EquippedBy`, `Card.Self`, `Creature`, `Creature.Artifact`, `Creature.Black`, `Creature.Blue,Creature.Black`, `Creature.Colorless`, `Orc`
- `ValidBlockerAmount$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Card.Self`, `Card.IsRemembered`, `Creature.enchanted+YouCtrl`, `Beast`, `Card.AttachedBy`, `Card.YouCtrl`, `Creature.withoutFlying`, `Creature.YouCtrl`, `Creature.withFlying`

## `AttackerBlockedByCreature`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Psionic Adept —`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidBlocked$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Card.AttachedBy`, `Card.EffectSource`, `Card.EnchantedBy`, `Card.Self`, `Creature`, `Creature.Artifact`, `Creature.AttachedBy`, `Creature.ChosenColor`, `Creature.EnchantedBy`, `Creature.equipped`, `Creature.Green`, `Creature.Green,Creature.White`, `Creature.nonArtifact+nonDragon`, `Creature.nonBlack`, `Creature.nonWall`, `Creature.powerLE1`, `Creature.toughnessLE3`, `Creature.Vampire`, `Creature.Wall`, `Creature.wasDealtDamageThisTurn`, `Creature.White`, `Creature.withDeathtouch`, `LessPowerThanAttacker`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.Green,Creature.White`, `Card.Self`, `Creature`, `Creature.powerLE1`, `Creature.AttachedBy`, `Creature.nonWall`, `Creature.equipped`, `Creature.nonBlack`, `Creature.White`, `Creature.wasDealtDamageThisTurn`

## `AttackerBlockedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `AttackersDeclared`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AttackedTarget$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Planeswalker.YouCtrl`, `Player`, `Player.EnchantedBy`, `Player.EnchantedBy,Planeswalker.EnchantedPlayerCtrl`, `Player.IsPoisoned`, `You`, `You,Planeswalker.YouCtrl`
- `AttackingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.EnchantedBy`, `Player.Opponent`, `Player.Other`, `You`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.isMonarch`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `NatureShields`, `PackTactics`, `X`, `Y`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `AttackerHasUnattackedOpp`
- `Execute$`: TODO: Describe this parameter.
- `FirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+IsSolved`, `Creature.attacking+Other+YouCtrl+Legendary`, `Creature.attackingYou`, `Creature.YouCtrl+attacking+nonWall`, `Card.untapped`, `Card.StrictlySelf`, `Card.tapped`, `Creature.attacking`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackingPlayer`, `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `EQX`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `GE2`, `GE4`, `GE6`, `GE8`, `GTX`
- `Threshold$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Exile`, `Command`, `Graveyard`
- `ValidAttackers$`: TODO: Describe this parameter.
  Observed values: `Bard.YouCtrl`, `Bird.YouCtrl`, `Card.Knight+YouCtrl`, `Card.Self`, `Card.Self,Card.IsCommander+YouOwn`, `Creature`, `Creature.!token`, `Creature.Artifact+YouCtrl`, `Creature.attackingYou`, `Creature.Bird+YouCtrl`, `Creature.Elf+YouCtrl`, `Creature.EnchantedBy Aura.YouCtrl`, `Creature.IsSuspected+YouCtrl`, `Creature.Legendary`, `Creature.Legendary+YouCtrl`, `Creature.modified+YouCtrl`, `Creature.nonGideon`, `Creature.nonHuman+YouCtrl`, `Creature.Soldier`, `Creature.withFlying`, `Creature.YouCtrl`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+nonGnome`, `Creature.YouCtrl+Other+withFlying`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+Rat`, `Creature.YourTeamCtrl`, `Devil.YouCtrl`, `Dinosaur.YouCtrl`, `Dragon.YouCtrl`, `Elf.YouCtrl`, `Faerie.YouCtrl`, `Goblin.YouCtrl`, `Goblin.YouCtrl,Orc.YouCtrl`, `God.YouCtrl`, `Insect.YouCtrl`, `Knight.YouCtrl`, `Lizard.YouCtrl`, `Phyrexian.YouCtrl`, `Rogue.YouCtrl`, `Spider`, `Treefolk.YouCtrl`, `Vampire.!token+YouCtrl`, `Vampire.YouCtrl`, `Vehicle.YouCtrl`, `Wraith`, `Zombie.YouCtrl`
- `ValidAttackersAmount$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `GE2`, `GE3`, `GE4`, `GE5`, `GE8`

## `AttackersDeclaredOneTarget`

TODO: Write documentation.

**Parameters:**
- `AttackedTarget$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent,Planeswalker.OppCtrl`, `Opponent.lifeGTX`, `Player`, `Player,Planeswalker`, `Player.hasInitiative`, `You`
- `AttackingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.Opponent`, `You`
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidAttackers$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.Demon+YouCtrl`, `Creature.Merfolk+YouCtrl`, `Creature.powerEQChosen,Creature.toughnessEQChosen`, `Creature.token+YouCtrl`, `Creature.Warrior+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+!Toy`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+powerLE1`, `Dragon.YouCtrl`, `Halfling.YouCtrl`
- `ValidAttackersAmount$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE2`

## `AttackerUnblocked`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EnchantedBy`, `Card.IsRemembered`, `Creature.YouCtrl`, `Creature`, `Creature.Legendary+YouCtrl`, `Rogue.YouCtrl`
- `ValidDefender$`: TODO: Describe this parameter.
  Observed values: `Player`, `You,Planeswalker.YouCtrl`

## `AttackerUnblockedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidAttackingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `ValidDefenders$`: TODO: Describe this parameter.
  Observed values: `You`

## `Attacks`

TODO: Write documentation.

**Parameters:**
- `Alone$`: TODO: Describe this parameter.
  Observed values: `True`
- `AttackDifferentPlayers$`: TODO: Describe this parameter.
  Observed values: `True`
- `Attacked$`: TODO: Describe this parameter.
  Observed values: `Battle`, `Opponent`, `Player`, `Player.Chosen`, `Player.controlsLand_GE8`, `Player.EnchantedBy`, `Player.Opponent`, `Player.Opponent,Planeswalker.OppCtrl`, `Player.withMostLife`, `You`, `You,Card.EffectSource`, `You,Planeswalker.YouCtrl`, `You,Planeswalker.YouCtrl,Battle.ProtectedBy You`
- `Blessing$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.hasInitiative`, `You.withMostLife`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Celebration`, `PackTactics`, `X`, `Y`, `YouLifeGained`, `Zombies`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `AttackedPlayerWithMostLife`, `NoOpponentHasMoreLifeThanAttacked`
- `DefendingPlayerPoisoned$`: TODO: Describe this parameter.
  Observed values: `True`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `Desert$`: TODO: Describe this parameter.
  Observed values: `True`
- `Execute$`: TODO: Describe this parameter.
- `FirstAttack$`: TODO: Describe this parameter.
  Observed values: `True`
- `FirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+powerGE6`, `Creature.attacking+Other`, `Warrior.Other+YourTeamCtrl`, `Card.YouCtrl`, `Blood.token+DefenderCtrl`, `Artifact.YouCtrl`, `Dinosaur.YouCtrl`, `Card.Self+IsRenowned`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+HasCounters`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Enchantment.YouCtrl`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `Metalcraft$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Parley —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE2`, `GE3`, `GE8`, `LE2`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Hand`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`, `GE2`, `GE3`, `GE4`, `GE6`, `GE8`, `GTX`, `GTY`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `1`
- `Threshold$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EnchantedBy`, `Card.EquippedBy`, `Creature.NamedCard+YouCtrl`, `Samurai.YouCtrl,Warrior.YouCtrl`, `Card.Self+IsSaddled`, `Creature.Self`, `Creature.YouCtrl`, `Card.AttachedBy`, `Creature.EquippedBy`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.OppCtrl`

## `AttackVigilance`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource+untapped`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `BecomeMonarch`

TODO: Write documentation.

**Parameters:**
- `BeginTurn$`: TODO: Describe this parameter.
  Observed values: `You`
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.OpponentOf Remembered`, `You`

## `BecomeMonstrous`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `BecomeRenowned`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`

## `BecomesCrewed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `FirstTimeCrewed$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidCrewAmount$`: TODO: Describe this parameter.
  Observed values: `2`

## `BecomesPlotted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `BecomesSaddled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `FirstTimeSaddled$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSaddled$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `BecomesTarget`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `Valiant$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Ability.numTargets EQ1`, `SpellAbility.OppCtrl`, `Spell`, `SpellAbility.YouCtrl`, `Spell.Aura`, `Activated.Creature+Other+namedGoblin Artisans`, `Spell.YouCtrl`, `Ability.Backup`, `Spell.OppCtrl`, `SpellAbility`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `You`, `Permanent.YouCtrl+inZoneBattlefield`, `Creature.EnchantedBy`, `Permanent.YouCtrl+Other+inZoneBattlefield`, `Card.Creature+inZoneBattlefield`, `Card.AttachedBy`, `Cleric.Creature+YouCtrl+inZoneBattlefield`, `Creature.Sliver+YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+counters_GE1_P1P1+inZoneBattlefield`

## `BecomesTargetOnce`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Card.!namedPsychic Battle`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`, `Activated`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `You,Permanent.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield`

## `BlockersDeclared`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `BlockRestrict`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `MaxBlockers$`: TODO: Describe this parameter.
  Observed values: `1`
- `ValidDefender$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `Blocks`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Dinosaur.YouCtrl`, `Creature.blockedBySource`, `Planeswalker.Vraska+YouCtrl`, `Creature.nonHuman+Other+YouCtrl`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidBlocked$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.Black`, `Creature.Blue,Creature.Black`, `Orc`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.OppCtrl`, `Card.AttachedBy`, `Creature.YouCtrl`, `Card.EquippedBy`, `Card.EnchantedBy`, `Creature.YouCtrl+withDefender`

## `CanAdapt`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`

## `CanAttackDefender`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.IsRemembered`, `Card.EffectSource`, `Card.Self`, `Card.IsRemembered`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+withDefender`

## `CantAttack`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `HasTarget`
- `DefenderNotNearestToYouInChosenDirection$`: TODO: Describe this parameter.
  Observed values: `True`
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `Target$`: TODO: Describe this parameter.
  Observed values: `Player.CardOwner`, `Player.IsRemembered`, `Player.IsRemembered,Permanent.RememberedPlayerCtrl`, `Player.IsRemembered,Planeswalker.ControlledBy Remembered`, `Player.IsRemembered,Planeswalker.RememberedPlayerCtrl`, `You`, `You,Permanent.YouCtrl`, `You,Planeswalker.YouCtrl`
- `UnlessDefender$`: TODO: Describe this parameter.
  Observed values: `controlsIsland`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.ChosenCtrl`, `Creature.nonLand`, `Creature.YouCtrl`, `Card.EffectSource`, `Creature.!RememberedPlayerCtrl`, `Card.Self`, `Creature.!IsRemembered`, `Card.IsRemembered`, `Creature.IsRemembered`

## `CantAttack,CantBlock`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`

## `CantAttack,CantBlock,CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`

## `CantAttackUnless`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2`, `PayLife<2>`, `XChosen`, `WhipgrassClericNum`
- `Description$`: TODO: Describe this parameter.
- `Target$`: TODO: Describe this parameter.
  Observed values: `You`, `You,Planeswalker.YouCtrl`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Card.Self`

## `CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.IsRemembered`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.IsRemembered`, `Planeswalker`, `Permanent.IsRemembered`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.!ManaAbility`, `Activated.Loyalty`, `Activated.nonLand,Activated.ManaAbilityCantPaidFor`

## `CantBeCast`

TODO: Write documentation.

**Parameters:**
- `Caster$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.!IsRemembered`, `Player.IsRemembered`, `Player.Other`, `You`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `NumCount`
- `Description$`: TODO: Describe this parameter.
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Instant,Sorcery`, `Card.nonLand+NamedCard`, `Card.nonCreature`, `Card.!wasCastFromTheirHand`, `Creature`, `Card`, `Card.NamedCard`, `Card.IsRemembered`, `Card.cmcEQX`, `Card.Creature`

## `CantBecomeMonarch`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CantBlock`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.IsRemembered`, `Creature.OppCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.powerLTtoughness`, `Creature.OppCtrl+powerLEX`, `Creature.Self`

## `CantBlockBy`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidAttacker$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource`, `Card.IsRemembered`, `Card.Self`, `Creature`, `Creature.Black+YouCtrl`, `Creature.EffectSource`, `Creature.IsRemembered`, `Creature.namedLeitmotif Composer`, `Creature.Self`, `Creature.YouCtrl`, `Giant,Warrior`
- `ValidBlocker$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Creature.ChosenColor`, `Creature.IsRemembered`, `Creature.nonArtifact+nonRed`, `Creature.nonBlack`, `Creature.nonSnow`, `Creature.nonSpirit`, `Creature.nonWall`, `Creature.OppCtrl`, `Creature.powerGE3`, `Creature.powerGTX`, `Creature.powerLE2`, `Creature.RememberedPlayerCtrl`, `Creature.Self`, `Creature.token`, `Creature.Wall`, `Creature.withoutDefender`, `Creature.withoutFlying+!IsImprinted+YouCtrl`, `Creature.withoutFlying+RememberedPlayerCtrl`, `Creature.withoutFlying+withoutReach`, `Creature.withoutHaste`
- `ValidBlockerRelative$`: TODO: Describe this parameter.
  Observed values: `Creature.DifferentSector`

## `CantBlockUnless`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `XChosen`, `WhipgrassClericNum`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `CantChangeLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CantGainLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.IsRemembered`, `Player.Opponent`, `You`

## `CantLoseLife`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`

## `CantPhaseIn`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource+faceUp`, `Card.EffectSource+tapped`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.phasedOutIsRemembered`

## `CantPhaseOut`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`

## `CantPlayLand`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `Player$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.IsRemembered`, `Player.Other`, `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.NamedCard`, `Land`

## `CantPreventDamage`

TODO: Write documentation.

**Parameters:**
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Creature.IsRemembered`
- `Description$`: TODO: Describe this parameter.

## `CantPutCounter`

TODO: Write documentation.

**Parameters:**
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `POISON`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`, `You`

## `CantRegenerate`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.DamagedBy`, `Card.IsRemembered`, `Creature.DamagedBy Remembered`

## `CantSacrifice`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered+YouCtrl`, `Card.Self`, `Card.IsRemembered`

## `CantTarget`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.Opponent`
- `Description$`: TODO: Describe this parameter.
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell,Activated`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Blue,Card.Black`, `Card.Blue+OppCtrl,Card.Black+OppCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Permanent.YouCtrl`, `Card.Permanent,Player`, `Card.IsRemembered`

## `CaseSolved`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Case`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CastWithFlash`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Exile,Graveyard,Hand,Library,Command`
- `Caster$`: TODO: Describe this parameter.
  Observed values: `You`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`, `Dinosaur`, `Sorcery`, `Card.ChosenType`, `Card.Creature`, `Planeswalker.YouCtrl`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Loyalty`, `Spell`

## `Championed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Faerie`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `ChangesController`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredOriginalController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.IsRemembered`, `Card.OppCtrl`
- `ValidOriginalController$`: TODO: Describe this parameter.
  Observed values: `Player.Other`, `You`

## `ChangesZone`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Adamant$`: TODO: Describe this parameter.
  Observed values: `Any`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BadETB`, `SafeToHold`
- `Blessing$`: TODO: Describe this parameter.
  Observed values: `True`
- `BoonAmount$`: TODO: Describe this parameter.
  Observed values: `12`
- `CheckOnTriggeredCard$`: TODO: Describe this parameter.
  Observed values: `X EQ0`, `X GE1`, `X GE4`, `X GT1`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `BB`, `CastSA>Count$Adamant_2.Black.2.0`, `CastSA>Count$Adamant_2.Blue.2.0`, `CastSA>Count$Adamant_2.Green.2.0`, `CastSA>Count$Adamant_2.Red.2.0`, `CastSA>Count$Adamant_2.White.2.0`, `CastSA>Count$OptionalGenericCostPaid.1.0`, `Count$CardCounters.ALL`, `Count$Presence_Dragon.1.0`, `Count$Valid Land.YouCtrl`, `Morbid`, `NoMonarch`, `RaidTest`, `RR`, `TreasureCheck`, `UU`, `W`, `X`, `Y`, `YourLife`, `Z`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Evolve`
- `ConditionYouCastThisTurn$`: TODO: Describe this parameter.
  Observed values: `EQ2`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `Desert$`: TODO: Describe this parameter.
  Observed values: `True`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Ante,Command,Exile,Hand,Library`, `Any`, `Battlefield`, `Command`, `Exile`, `Graveyard`, `Graveyard,Command`, `Graveyard,Exile`, `Hand`, `Library`, `Stack`
- `ExcludedDestinations$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ExcludedOrigins$`: TODO: Describe this parameter.
  Observed values: `Graveyard,Exile`, `Hand`
- `Execute$`: TODO: Describe this parameter.
- `ForgetOnCast$`: TODO: Describe this parameter.
  Observed values: `Card.nonCreature+YouCtrl`
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `Hidden$`: TODO: Describe this parameter.
  Observed values: `True`
- `Host$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Knight.YouCtrl+Other`, `Card.StrictlySelf`, `Spirit.Other+YouCtrl`, `Planeswalker.Vraska+YouCtrl`, `Card.Self+namedAwestruck Cygnet`, `Creature.YouCtrl+powerGE4`, `Permanent.Snow+YouCtrl+Other`, `Card.Self+counters_GE3_QUEST`, `Card.YouCtrl`, `Card.Self+counters_GE1_M1M1`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Enchantment.YouCtrl`
- `ManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `B`, `G`, `R`, `U`, `W`
- `ManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`, `G`, `R`
- `Metalcraft$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `NotThisAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`, `You`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Any`, `AttractionDeck`, `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`, `Hand,Graveyard,Exile,Stack,Library,Command`, `Hand,Library`, `Library`, `Library,Hand`, `Library,Hand,Exile,Command,Stack`, `Stack`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Declare Attackers`, `Main1,Main2`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE2`, `GE3`, `GE4`, `GE5`, `GE6`, `GE7`, `LE9`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`, `Library`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Revolt$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `GE2`, `GE20`, `GE3`, `GE4`, `GE7`, `GTX`, `GTY`, `GTZ`, `LT1`, `LT4`, `LT7`, `LTY`
- `Threshold$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.Other+YouCtrl`, `Insect.YouCtrl+Other`, `Creature.DamagedBy`, `Card.AttachedBy`, `Creature.YouCtrl+!token`, `Creature.IsRemembered`, `Land.YouCtrl`, `Beast.YouCtrl`, `Creature`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`

## `ChangesZoneAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `BoonAmount$`: TODO: Describe this parameter.
  Observed values: `3`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$ValidSelf Card.IsSuspected`, `Z`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Ante,Command,Exile,Hand,Library`, `Any`, `Battlefield`, `Exile`, `Graveyard`, `Library`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `InvertValidCause$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE1_M1M1`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Any`, `Battlefield`, `Battlefield,Graveyard`, `Graveyard`, `Hand`, `Library`, `Library,Graveyard`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Graveyard`, `Command`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Cat.Other+YouCtrl`, `Card.YouOwn`, `Vampire.YouCtrl`, `Creature.Other+YouCtrl`, `Card.token+YouCtrl`, `Creature.basePowerEQ1+baseToughnessEQ1+Other+YouCtrl`, `Creature`, `Permanent.nonCreature+nonLand+YouCtrl`, `Permanent.token+YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `LandAbility`, `SpellAbility.YouCtrl`

## `ChaosEnsues`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`

## `ClaimPrize`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Attraction.YouCtrl`

## `Clashed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `Won$`: TODO: Describe this parameter.
  Observed values: `False`, `True`

## `ClassLevelGained`

TODO: Write documentation.

**Parameters:**
- `ClassLevel$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `CollectEvidence`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CombatDamageToughness`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.Self`

## `CommitCrime`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `ConjureAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Continuous`

TODO: Write documentation.

**Parameters:**
- `AddAbility$`: TODO: Describe this parameter.
  Observed values: `Mana`, `ArlinnDealDamage`, `ABPump`, `ABDraw`, `ABMana`, `ABDealDamage`, `BlackTap`, `AnimateIsland`, `ABMana & ABToken`, `AddMana`
- `AddColor$`: TODO: Describe this parameter.
  Observed values: `Black`
- `AddHiddenKeyword$`: TODO: Describe this parameter.
  Observed values: `CARDNAME can't attack or block.`, `CARDNAME can't block.`, `This card doesn't untap during your next untap step.`
- `AddKeyword$`: TODO: Describe this parameter.
  Observed values: `Flying`, `Improvise`, `Haste`, `Indestructible`, `Cascade`, `Double Strike & Haste`, `Enchant:Creature.YouCtrl:creature you control`, `Double Strike`, `Affinity:Artifact`, `Storm`
- `AddPower$`: TODO: Describe this parameter.
  Observed values: `+2`, `-1`, `1`, `2`, `3`, `ConvertedManaCost`, `X`
- `AddReplacementEffect$`: TODO: Describe this parameter.
  Observed values: `ReplaceDies`
- `AddStaticAbility$`: TODO: Describe this parameter.
  Observed values: `AttackOwner`, `P1Pump`, `SpendAnyMana`, `STAura`, `Unblockable`
- `AddSVar$`: TODO: Describe this parameter.
  Observed values: `ArlinnX`
- `AddToughness$`: TODO: Describe this parameter.
  Observed values: `+2`, `-1`, `1`, `2`, `3`, `X`
- `AddTrigger$`: TODO: Describe this parameter.
  Observed values: `DamageTrig`, `BecomesTapped`, `DealsCDTrig`, `MannequinBecomesTarget`, `MathasDeath`, `ObsidianBlazeTrig`, `ETB`
- `AddType$`: TODO: Describe this parameter.
  Observed values: `Creature & Spirit`, `Zombie`, `Island`, `Enchantment`, `Angel & Warrior`, `Nightmare`, `Artifact & Creature & Robot`, `Aura & Enchantment`, `Spirit`, `Swamp`
- `AdjustLandPlays$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `Z`
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.IsRemembered+nonLand`, `Treasure.YouCtrl`, `Card.ChosenCard`, `Creature.YouCtrl+IsRemembered`, `Planeswalker.YouCtrl+IsRemembered`, `Artifact.YouCtrl+IsRemembered`, `Enchantment.YouCtrl+IsRemembered`, `Instant.YouCtrl+IsRemembered`, `Sorcery.YouCtrl+IsRemembered`
- `AffectedDefined$`: TODO: Describe this parameter.
  Observed values: `EffectSource`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Stack`, `Exile`, `Exile,Stack`, `Graveyard`, `Graveyard,Exile`, `Hand`, `Hand,Graveyard,Exile,Library,Command`, `Hand,Graveyard,Library,Exile,Command`, `Library`, `Sideboard`, `Stack`
- `CharacteristicDefining$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ElkinSVar`, `X`, `Y`, `YouCastThisTurn`, `Z`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `PlayerTurn`
- `ControlVote$`: TODO: Describe this parameter.
  Observed values: `True`
- `DeclaresAttackers$`: TODO: Describe this parameter.
  Observed values: `You`
- `DeclaresBlockers$`: TODO: Describe this parameter.
  Observed values: `You`
- `Description$`: TODO: Describe this parameter.
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Command`, `Exile`, `Graveyard`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `You`
- `GainsAbilitiesOfDefined$`: TODO: Describe this parameter.
  Observed values: `RememberedLKI`
- `Goad$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE4_LEVEL`, `Planeswalker.Lukka+YouCtrl`, `Swamp.YouCtrl`
- `ManaConversion$`: TODO: Describe this parameter.
  Observed values: `Blue->AnyColor`
- `MayLookAt$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`
- `MayPlay$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayAltManaCost$`: TODO: Describe this parameter.
  Observed values: `0`, `ConvertedManaCost`, `PayLife<ConvertedManaCost>`, `R`, `Waterbend<ConvertedManaCost>`, `WB`
- `MayPlayDontGrantZonePermissions$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayIgnoreColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayIgnoreType$`: TODO: Describe this parameter.
  Observed values: `True`
- `MayPlayLimit$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `MayPlayPlayer$`: TODO: Describe this parameter.
  Observed values: `CardOwner`
- `MayPlayText$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Battle`, `Creature`, `Enchantment`, `Instant`, `Kindred`, `Planeswalker`, `Sorcery`
- `MayPlayWithoutManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `RaiseCost$`: TODO: Describe this parameter.
  Observed values: `Forage`, `Sac<1/Land>`
- `RaiseMaxHandSize$`: TODO: Describe this parameter.
  Observed values: `-3`
- `RemoveAllAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveKeyword$`: TODO: Describe this parameter.
  Observed values: `Flying`
- `RemoveLandTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`, `You may look at the card and you may cast it if it's a creature.`
- `SetColor$`: TODO: Describe this parameter.
  Observed values: `Black`, `Green`
- `SetMaxHandSize$`: TODO: Describe this parameter.
  Observed values: `Unlimited`
- `SetName$`: TODO: Describe this parameter.
  Observed values: `Moon`
- `SetPower$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `4`, `5`, `8`, `9`, `AffectedX`, `X`, `Y`
- `SetToughness$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `4`, `5`, `8`, `9`, `AffectedX`, `X`, `Y`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE3`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Spell.Equipment`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell.Sneak`

## `CounterAdded`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `CounterAmount$`: TODO: Describe this parameter.
  Observed values: `EQ12`, `EQ5`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `HOUR`, `LORE`, `M1M1`, `P1P1`, `PLAN`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.YouCtrl`, `Saga.YouCtrl`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `You`

## `CounterAddedAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `LOYALTY`, `P1P1`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Human.YouCtrl`, `Planeswalker.YouCtrl`

## `CounterAddedOnce`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Loy`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `ENERGY`, `LOYALTY`, `M1M1`, `P1P1`, `TIME`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.StrictlySelf`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GTBeeb`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouCtrl`, `Creature.inRealZoneBattlefield`, `Card.Self`, `Permanent.Other+YouCtrl+inZoneBattlefield`, `Creature.YouCtrl`, `Creature.Self`, `Creature.Other+YouCtrl`, `Creature`, `Permanent.YouCtrl+inRealZoneBattlefield`, `Creature.Other+inZoneBattlefield+Colorless`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `You`

## `Countered`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.wasCastByYou`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`, `SpellAbility.YouCtrl`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell.Creature+wasCastByYou`

## `CounterPlayerAddedAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Card.Self+inRealZoneBattlefield`, `Creature.inRealZoneBattlefield`, `Creature.YouDontCtrl+inRealZoneBattlefield`, `Permanent.inRealZoneBattlefield,Player`
- `ValidObjectToSource$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inRealZoneBattlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `You`, `Opponent`

## `CounterRemoved`

TODO: Write documentation.

**Parameters:**
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `HONE`, `ORE`, `P1P1`, `TIME`
- `Execute$`: TODO: Describe this parameter.
- `NewCounterAmount$`: TODO: Describe this parameter.
  Observed values: `0`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Self+counters_EQ0_TIME`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `CounterRemovedOnce`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Beeb`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `LOYALTY`, `TIME`
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GTLoy`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `CounterTypeAddedAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl+inZoneBattlefield`

## `CrankContraption`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Crewed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Phase$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCrew$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Self,Creature.Legendary+Other+YouCtrl`

## `Cycled`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Other+YouOwn`, `Card`, `Card.Other`, `Card.YouCtrl`, `Card.YouOwn`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `DamageAll`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Pirate.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl`, `Creature.Zombie+YouCtrl`, `Creature.Warrior`, `Creature.OppCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Opponent`

## `DamageDealtOnce`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE7`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.AttachedBy`, `Creature.EquippedBy`, `Sliver.inZoneBattlefield`, `Creature.YouCtrl`, `Spell.YouCtrl`, `Instant.Red,Sorcery.Red,Creature.Red+inZoneBattlefield`, `Creature.IsRemembered`, `Card.nonCreature+YouCtrl`, `Card.RedSource+YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.blocking`, `Creature`, `Player,Permanent`

## `DamageDone`

TODO: Write documentation.

**Parameters:**
- `Blessing$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.committedCrimeThisTurn`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Monarch`, `X`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `DamageAmount$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQTargetToughness`, `GE3`, `GE5`, `GE6`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `Execute$`: TODO: Describe this parameter.
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.StrictlySelf`, `Card.Self+counters_LT4_P1P1`, `Card.untapped`, `Card.Self+ThisTurnEntered`, `Creature.Other+YouCtrl`, `Card.Self+IsMonstrous`, `Island.YouCtrl`, `Swamp.YouCtrl`, `Permanent.Blue+YouCtrl,Permanent.Red+YouCtrl`
- `Metalcraft$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceController`, `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `StackDescription$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE2`, `GT0`
- `TargetRelativeToCause$`: TODO: Describe this parameter.
  Observed values: `Creature.targetedBy`
- `TargetRelativeToSource$`: TODO: Describe this parameter.
  Observed values: `Player.CardOwner`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Spell.numTargets EQ1`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Gamma.YouCtrl,Villain.YouCtrl`, `Creature.IsRemembered`, `Card.Self,Creature.EquippedBy`, `Vehicle.YouCtrl`, `Creature.YouCtrl`, `Creature.IsRenowned+YouCtrl`, `Creature.modified+YouCtrl`, `Card.OppCtrl,Emblem.OppCtrl`, `Card.IsCommander+YouOwn`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Player`, `Creature.nonWall`, `Player,Battle`, `Opponent`, `Card.Self`, `You`, `Creature`, `Player,Planeswalker`, `Opponent,Battle`, `Player.Opponent`

## `DamageDoneOnce`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Monarch`, `X`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `DamageAmount$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE4`
- `DamageSource$`: TODO: Describe this parameter.
  Observed values: `Any`
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.StrictlySelf`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LT8`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.Faerie+YouCtrl`, `Rogue.YouCtrl`, `Creature.Gorgon+YouCtrl,Creature.Snake+YouCtrl`, `Creature.Artifact+YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Creature.YouCtrl`, `Creature.Dragon+YouCtrl`, `Card.Self`, `Card`, `Squirrel.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`, `Card.Self`, `Card.IsRemembered`, `Card.AttachedBy`, `Creature.EquippedBy`, `Creature.EnchantedBy`, `Creature`, `Card.Self,Creature.PairedWith`, `Creature.OppCtrl`

## `DamagePreventedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `You`

## `DayTimeChanges`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`

## `Destroyed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.nonCreature+YouCtrl`, `Artifact.nonCreature`
- `ValidCauser$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`

## `Devoured`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidDevoured$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `Discarded`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Plains.YouCtrl`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.OppOwn`, `Land.OppOwn`, `Card.Self`, `Card.YouCtrl`, `Card.YouCtrl+withMadness`, `Card.Other+YouOwn`, `Creature.YouCtrl`, `Land.YouCtrl`, `Card.nonLand+nonCreature+YouCtrl`, `Card.YouCtrl+Other`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`

## `DiscardedAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.nonLand`, `Card`, `Land`, `Card.Artifact`, `Card.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.OppCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`

## `Discover`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Drawn`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.isMonarch`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Z`
- `Execute$`: TODO: Describe this parameter.
- `FirstCardInDrawStep$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `ForReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.Red+YouCtrl`
- `Number$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `5`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.YouCtrl`, `Card.NamedCard+OwnedBy Player.Chosen`, `Card.OppOwn`, `Card.OwnedBy Player.EnchantedBy`, `Card.YouOwn+Dragon`, `Card.YouOwn`, `Card`, `Card.Land`, `Card.nonLand`, `Card.OppCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Active`, `Player.Opponent`, `Player.Opponent+Active+controlsArtifact.namedWedding Ring`, `Player.Opponent+NonActive`

## `DungeonCompleted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `ElementalBend`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Enlisted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidEnlisted$`: TODO: Describe this parameter.
  Observed values: `Creature.!token`

## `Evolved`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `ExcessDamage`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `False`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl+DamagedByGiant.YouCtrl;Wizard.YouCtrl;Spell.YouCtrl,Planeswalker.OppCtrl+DamagedByGiant.YouCtrl;Wizard.YouCtrl;Spell.YouCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`

## `ExcessDamageAll`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `False`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`

## `Exerted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `Exiled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`
- `WhileKeyword$`: TODO: Describe this parameter.
  Observed values: `Ability.Craft`

## `Exploited`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.nonHuman`, `Creature.!token`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Card.Self`

## `Explores`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `ValidExplored$`: TODO: Describe this parameter.
  Observed values: `Card.nonLand`, `Land`

## `Fight`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `FightOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `FlippedCoin`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidResult$`: TODO: Describe this parameter.
  Observed values: `Lose`, `Win`

## `Forage`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Foretell`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `FullyUnlock`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Room`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `GiveGift`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `IgnoreHexproof`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `You`
- `Description$`: TODO: Describe this parameter.
- `ValidEntity$`: TODO: Describe this parameter.
  Observed values: `Opponent,Creature.OppCtrl`

## `IgnoreLegendRule`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouCtrl`

## `IgnoreShroud`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`
- `Description$`: TODO: Describe this parameter.
- `ValidEntity$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource`

## `Investigated`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `LandPlayed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+Enchantment`, `Card.Self+Creature`
- `NotFirstLand$`: TODO: Describe this parameter.
  Observed values: `True`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Ante,Command,Exile,Graveyard,Library`, `Exile`, `Exile,Library,Graveyard`, `Hand`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Land.IsRemembered`, `Land.OppCtrl`, `Land.sharesCardTypeWith ValidExile Card.ExiledWithSource`, `Land.YouOwn+sharesCardTypeWith Imprinted.ExiledWithSource`, `Land.Other+YouCtrl`, `Land.YouCtrl`, `Land.nonBasic+OppCtrl`, `Land`, `Island.YouCtrl`, `Card.ExiledWithSourceLKI`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.MayPlaySource`

## `LifeGained`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Spell$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Opponent+Active+controlsArtifact.namedWedding Ring`, `You`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Instant.White,Sorcery.White`

## `LifeLost`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent.Active`, `You`

## `LifeLostAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidAmountEach$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `LosesGame`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Chosen`, `Player.EnchantedBy`, `Player.Opponent`, `Player.Other`, `Player.Other+wasAttackedThisTurnBy Assassin.YouCtrl`

## `ManaAdded`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Player$`: TODO: Describe this parameter.
  Observed values: `You`
- `Produced$`: TODO: Describe this parameter.
  Observed values: `ChosenColor`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.!ManaAbility`, `SpellAbility.ManaAbility`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Land`

## `ManaConvert`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `ManaConversion$`: TODO: Describe this parameter.
  Observed values: `AnyType->AnyColor`, `AnyType->AnyType`, `C->AnyColor`, `White->AnyColor`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.Self`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell.MayPlaySource`

## `ManaExpend`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `4`, `6`, `8`
- `Execute$`: TODO: Describe this parameter.
- `Player$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `ManifestDread`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Mentored`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.EquippedBy`

## `Milled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.StrictlySelf`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.nonLand`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `MilledAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.nonLand`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `MilledOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `MinMaxBlocker`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Max$`: TODO: Describe this parameter.
  Observed values: `1`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.EffectSource`

## `MustAttack`

TODO: Write documentation.

**Parameters:**
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `MustAttack$`: TODO: Describe this parameter.
  Observed values: `CardOwner`, `ChosenPlayer`, `EffectSource`, `Player`, `Player.IsRemembered`, `Player.Other`, `Remembered`, `Remembered.NonActive`, `RememberedPlayer`, `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCreature$`: TODO: Describe this parameter.
  Observed values: `Card.ChosenType`, `Card.EffectSource`, `Card.IsRemembered`, `Card.Self`, `Creature`, `Creature.ActivePlayerCtrl`, `Creature.IsRemembered`, `Creature.OppCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.RememberedPlayerCtrl+ActivePlayerCtrl`, `Creature.YouCtrl+ChosenCardStrict`

## `MustBlock`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCreature$`: TODO: Describe this parameter.
  Observed values: `Card.ChosenCardStrict`, `Card.IsRemembered`, `Creature`, `Creature.OppCtrl`

## `Mutates`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`

## `NewGame`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`

## `NoCleanupDamage`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self+inZoneBattlefield`, `Card.Self`, `Creature`

## `NumLoyaltyAct`

TODO: Write documentation.

**Parameters:**
- `Additional$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `Description$`: TODO: Describe this parameter.
- `OnlySourceAbs$`: TODO: Describe this parameter.
  Observed values: `True`
- `Twice$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.EffectSource`, `Planeswalker.YouCtrl`

## `Panharmonicon`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Dungeon.YouOwn`, `Card.Self,Emblem.YouOwn`, `Permanent.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidMode$`: TODO: Describe this parameter.
  Observed values: `Attacks,AttackersDeclared,AttackersDeclaredOneTarget`, `ChangesZone,ChangesZoneAll`, `RoomEntered`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Battlefield,Command`

## `PayCumulativeUpkeep`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Paid$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `PayEcho`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Paid$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `PayLife`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Phase`

TODO: Write documentation.

**Parameters:**
- `APlayerHasMoreLifeThanEachOther$`: TODO: Describe this parameter.
  Observed values: `True`
- `APlayerHasMostCardsInHand$`: TODO: Describe this parameter.
  Observed values: `True`
- `Blessing$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent.isMonarch`, `Player.withMostTypeCreatureOnly`, `Player.withMostTypeWizardOnly`, `You.damageDoneSingleSource GE5`, `You.hasInitiative`, `You.isMonarch`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ActiveLands`, `ArtifactsEntered`, `AttackedThisTurn`, `CardsDiscarded`, `CardsInHand`, `CardsThem`, `CarpetX`, `Celebration`, `CheckLandTypes`, `ClueResearch`, `Contractors`, `Count$ThisTurnCast_Instant.YouCtrl,Sorcery.YouCtrl`, `Count$ThisTurnEntered_Graveyard_Creature.!token`, `DiedThisTurn`, `DragonCheck`, `DrewLastTurn`, `ElfEntered`, `FaceDown`, `FoodCheck`, `Hits`, `HumanEntered`, `LifeGained`, `Morbid`, `NoCharge`, `NumCast`, `OppHand`, `PlayerCountHasLost$Amount`, `RaidTest`, `Safe`, `TrigCast`, `TrigCount`, `TrigHand`, `Turns`, `X`, `Y`, `YouCycled`, `YouLifeGained`, `YouTeamLifeGained`, `Z`
- `Delirium$`: TODO: Describe this parameter.
  Observed values: `True`
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `Execute$`: TODO: Describe this parameter.
- `FirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `FirstUpkeep$`: TODO: Describe this parameter.
  Observed values: `True`
- `FirstUpkeepThisGame$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.YouOwn`, `Card.tapped`, `Planeswalker.Basri+YouCtrl`, `Permanent.YouDontOwn+YouCtrl`, `Card.EnchantedBy+!attackedThisTurn`, `Card.Self+!attackedThisTurn`, `Card.Self+counters_GE4_QUEST`, `Planeswalker.Ajani+YouCtrl`, `Card.Self+counters_GE1_SCREAM`, `Permanent.YouCtrl+Blue,Permanent.YouCtrl+Black`
- `IsPresent2$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self+!IsSolved`, `Creature.YouCtrl+YouOwn+namedBruna; the Fading Light`, `Creature.YouCtrl+YouOwn+namedFang; Fearless l'Cie`, `Creature.YouCtrl+YouOwn+namedMidnight Scavengers`, `Land.YouCtrl+YouOwn+namedArgoth; Sanctum of Nature`
- `LifeAmount$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE40`, `GE50`, `GEW`, `LE10`, `LE5`
- `LifeTotal$`: TODO: Describe this parameter.
  Observed values: `ActivePlayer`, `You`
- `Metalcraft$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `NotPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `TriggeredPlayer`, `You`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `BeginCombat`, `Cleanup`, `Declare Attackers`, `Draw`, `End of Turn`, `End Of Turn`, `EndCombat`, `Main`, `Main1`, `Main1,Main2`, `Main2`, `Untap`, `Upkeep`
- `PhaseCount$`: TODO: Describe this parameter.
  Observed values: `2`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ13`, `EQX`, `GE10`, `GE14`, `GE15`, `GE2`, `GE20`, `GE200`, `GE3`, `GE30`, `GE4`, `GE5`, `GE6`, `GE7`, `GT6`, `LE2`, `LE3`, `LT6`
- `PresentCompare2$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentPlayer2$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`, `Library`
- `PresentZone2$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Revolt$`: TODO: Describe this parameter.
  Observed values: `None`, `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `StackDescription$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ11`, `EQ13`, `EQ2`, `EQ4`, `GE1`, `GE10`, `GE2`, `GE3`, `GE30`, `GE4`, `GE5`, `GE6`, `GE7`, `GE8`, `GEY`, `GT0`, `GT1`, `GTCardsYou`, `GTHighestOpp`, `GTRivalLands`, `GTW`, `GTX`, `GTY`, `LE1`, `LE10`, `LE2`, `LT1`, `LT7`, `LT8`, `LTY`, `NE0`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredPlayer`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Graveyard`, `Command`, `Exile`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent.EnchantedBy`, `Player`, `Player.Chosen`, `Player.controlsCard.IsRemembered`, `Player.controlsCreature.IsRemembered_GE1`, `Player.EnchantedBy`, `Player.EnchantedController`, `Player.isMonarch`, `Player.IsRemembered`, `Player.Opponent`, `Player.Other`, `Player.Other+!IsRemembered`, `You`, `You.descended`
- `WerewolfTransformCondition$`: TODO: Describe this parameter.
  Observed values: `True`
- `WerewolfUntransformCondition$`: TODO: Describe this parameter.
  Observed values: `True`

## `PhaseIn`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self,Spirit.YouCtrl+Other`, `Card.Self`

## `PhaseOut`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.phasedOutSelf`

## `PhaseOutAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Permanent.phasedOutOther`

## `PlanarDice`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Result$`: TODO: Describe this parameter.
  Observed values: `Blank`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `PlaneswalkedFrom`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Plane`, `Plane.Self`

## `PlaneswalkedTo`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Plane.Self`

## `Proliferate`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.StrictlySelf`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `RaiseCost`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `8`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `B`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `UnlessValidTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.ActivePlayerCtrl`, `Card`, `Card.Self`, `Card.IsRemembered+CastSa Spell.MayPlaySource`, `Card.nonCreature`, `Card.IsRemembered`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl+inZoneBattlefield`, `You,Card.YouCtrl+inZoneBattlefield`

## `Random`

TODO: Write documentation.

**Parameters:**
- `Chance$`: TODO: Describe this parameter.
  Observed values: `20`, `30`
- `MinTurn$`: TODO: Describe this parameter.
  Observed values: `5`

## `ReduceCost`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`, `You`
- `AffectedZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `Count$ChosenNumber`, `CurrPower`, `Num`, `X`
- `Color$`: TODO: Describe this parameter.
  Observed values: `B`, `R G`
- `Description$`: TODO: Describe this parameter.
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`
- `IgnoreGeneric$`: TODO: Describe this parameter.
  Observed values: `True`
- `OnlyFirstSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Ability`, `Spell`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Dragon`, `Card.nonCreature`, `Card.Historic`, `Legendary`, `Card.NamedCard`, `Card.wasCastFromExile`, `Card`, `Creature.Dragon`, `Instant,Sorcery`
- `ValidSpell$`: TODO: Describe this parameter.
  Observed values: `Activated.Equip`, `Spell.MayPlaySource`, `Static.isTurnFaceUp`

## `RingTemptsYou`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+Other`, `Creature.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `RolledDie`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Natural$`: TODO: Describe this parameter.
  Observed values: `True`
- `Number$`: TODO: Describe this parameter.
  Observed values: `3`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `RolledToVisitAttractions$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidResult$`: TODO: Describe this parameter.
  Observed values: `1`, `1,2`, `2`, `20`, `4`, `6`, `EQ1`, `EQ6`, `GE3`, `GE4`, `GE5`, `Highest`, `LE3`
- `ValidSides$`: TODO: Describe this parameter.
  Observed values: `6`

## `RolledDieOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Sacrificed`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Any`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Exile`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.token`, `Creature.Other`, `Elemental.!token`, `Food.YouCtrl,Clue.YouCtrl`, `Artifact.!token+Other,Creature.!token+Other`, `Land`, `Card.Self`, `Artifact`, `Permanent.YouCtrl`, `Blood.token+YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`
- `WhileKeyword$`: TODO: Describe this parameter.
  Observed values: `Spell.withEmerge`

## `SacrificedOnce`

TODO: Write documentation.

**Parameters:**
- `BoonAmount$`: TODO: Describe this parameter.
  Observed values: `2`
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Food`, `Permanent`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Saddled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Phase$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCrew$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Scry`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Island.YouCtrl`, `Card.tapped`, `Card`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ToBottom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `SearchedLibrary`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `SearchOwnLibrary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.Opponent`

## `SeekAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `SetInMotion`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.!OnGoing`

## `Shuffled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `ShuffleBySelfControlled$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShuffleFromEffect$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`

## `Specializes`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `SpellAbilityCast`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `HasXManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsSingleTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsValid$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated,Spell`, `Instant,Sorcery,Activated`, `Instant.YouCtrl,Sorcery.YouCtrl,Activated.YouCtrl`, `Spell`, `Spell,Activated`, `Spell.nonCreature`, `SpellAbility.!ManaAbility`, `SpellAbility.ManaFromTreasure`

## `SpellAbilityCopy`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsSingleTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `SpellCast`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivatorThisTurnCast$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQ2`, `EQ3`, `GT1`
- `ActivatorThisTurnCastEach$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `CanTargetOtherCondition$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Permanent.nonLand+OppCtrl+!ControlledBy TargetedController`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `AltCostPaid`, `CastSA>Count$Adamant_1.Colorless.0.1`, `CastSA>Count$Adamant_1.Colorless.1.0`, `CastSA>Count$xPaid`, `Morbid`, `NumCast`, `NumColoredCast`, `X`, `Y`
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `Execute$`: TODO: Describe this parameter.
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `HasXManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_LT3_CHARGE`, `Card.Self+IsSolved`, `Card.Self+suspended`, `Card.StrictlySelf`, `Card.Self+attacking`, `Card.Self+counters_EQ1_FETCH`, `Card.Self+Enchantment`, `Card.Self+Creature`, `Card.tapped`, `Card.suspended+Self`
- `IsSingleTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoColoredMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `TriggeredActivator`, `You`
- `OrderDuplicates$`: TODO: Describe this parameter.
  Observed values: `True`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Main1,Main2`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SnowSpentForCardsColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQ2`, `EQ4`, `GE8`, `LT7`
- `TargetsValid$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.inZoneBattlefield`, `Creature.NamedCard+YouCtrl+inZoneBattlefield`, `Creature.Other+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield,Artifact.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Creature.YouDontCtrl`, `Golem.inZoneBattlefield`, `Opponent,Permanent.OppCtrl+inZoneBattlefield`, `Permanent.inZoneBattlefield`, `Permanent.modified+YouCtrl`, `Permanent.nonLand+OppCtrl+inZoneBattlefield`, `Permanent.YouCtrl+Other+inZoneBattlefield`, `You,Creature.YouCtrl+inZoneBattlefield`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Exile`, `Command`, `Exile`, `Graveyard`, `Stack`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Opponent.NonActive`, `Player`, `Player.Active`, `Player.Active+!IsRemembered`, `Player.Chosen`, `Player.EnchantedBy`, `Player.NonActive`, `Player.Opponent`, `Player.Opponent+Active`, `Player.Other`, `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Lesson`, `Card.Self`, `Instant,Sorcery`, `Card.nonCreature`, `Creature.withoutFlying`, `Card`, `Card.!wasCastFromTheirHand`, `Creature`, `Creature,Planeswalker`, `Instant,Sorcery,Otter.!CastSaSource`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Instant.singleTarget,Sorcery.singleTarget`, `Spell.Kicked`, `Spell.ManaFromCard.StrictlySelf`, `Spell.ManaFromCreature_3`, `Spell.ManaFromTreasure`, `Spell.ManaSpent EQ0`, `Spell.ManaSpent GE4`, `Spell.ManaSpent GE7`, `Spell.ManaSpent GTX`, `Spell.MayPlaySource`, `Spell.Modal`, `Spell.numTargets GE1`, `Spell.singleTarget`, `Spell.Warp`
- `ValidSAonCard$`: TODO: Describe this parameter.
  Observed values: `Spell.Creature+sharesNameWith YourGraveyard,Spell.Planeswalker+sharesNameWith YourGraveyard`, `Spell.ManaSpent GE4`, `Spell.ManaSpent GE8`, `Spell.ManaSpent LTX`, `Spell.YouDontOwn`

## `SpellCastOrCopy`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Instant,Sorcery`

## `SpellCopy`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.EnchantedBy`, `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Instant`, `Instant,Sorcery`

## `Stationed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidCrew$`: TODO: Describe this parameter.
  Observed values: `Creature`

## `Surveil`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.StrictlySelf`, `Card`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `PresentPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `TapAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Merfolk.!token+YouCtrl`

## `Taps`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Attacker$`: TODO: Describe this parameter.
  Observed values: `False`
- `Execute$`: TODO: Describe this parameter.
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE1_M1M1`, `Card.Self+enchanted,Card.Self+equipped`
- `NoResolvingCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.AttachedBy`, `Land.FortifiedBy`, `Creature`, `Creature.OppCtrl`, `Artifact`, `Merfolk.YouCtrl`, `Mountain.OppCtrl`, `Forest.OppCtrl`, `Dwarf.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `TapsForMana`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.NonActive`, `You`
- `CheckDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `You.isMonarch`
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.tapped`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`, `You`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `Produced$`: TODO: Describe this parameter.
  Observed values: `C`, `ChosenColor`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Land`, `Creature`, `Card.AttachedBy`, `Swamp`, `Land.nonBasic`, `Card.FortifiedBy`, `Mountain`, `Card.EnchantedBy`, `Permanent`, `Land.sharesNameWith Imprinted`

## `TokenCreated`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Blood.token+YouCtrl`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE5`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidToken$`: TODO: Describe this parameter.
  Observed values: `Blood`, `Card.token+YouCtrl`

## `TokenCreatedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OnlyFirst$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidToken$`: TODO: Describe this parameter.
  Observed values: `Creature.YouOwn`

## `Trains`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Transformed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `ResolvedLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Permanent.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+nonHuman+inZoneBattlefield`, `Creature.EquippedBy`, `Phyrexian.YouCtrl+inZoneBattlefield`

## `TurnBegin`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `TurnFaceUp`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Permanent`, `Detective.YouCtrl`, `Card.Self,Permanent.Other+YouCtrl`, `Permanent.YouCtrl`, `Card.Self,Creature.Other+YouCtrl`, `Card.AttachedBy`, `Creature.YouCtrl`, `Permanent.inZoneBattlefield`, `Permanent.Creature+YouCtrl+Other`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.YouCtrl`

## `Unattached`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidAttachment$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Permanent`

## `UnlockDoor`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `ThisDoor$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `UnspentMana`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ManaType$`: TODO: Describe this parameter.
  Observed values: `Red`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `UntapAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `Phase$`: TODO: Describe this parameter.
  Observed values: `Untap`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `UntapOtherPlayer`

TODO: Write documentation.

**Parameters:**
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouCtrl`, `Card.Self`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `Untaps`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Execute$`: TODO: Describe this parameter.
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `Untap`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.EquippedBy`, `Card.EffectSource`, `Card`, `Card.Self+ActivePlayerCtrl`, `Card.Self,Creature.Other+YouCtrl+cmcGE5`, `Permanent.YouCtrl`

## `VisitAttraction`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Attraction.YouCtrl`, `Attraction.IsRemembered`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Vote`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
- `List$`: TODO: Describe this parameter.
  Observed values: `OppVotedDiff`, `OppVotedSame`, `OppVotedSame,OppVotedDiff`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
