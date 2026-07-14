# Trigger Modes

<!-- forge-doc-scope: T: -->

## `Abandoned`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `EffectCleanup`
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
  Observed values: `TrigChangeZone`, `TrigCopy`, `TrigCopyAbility`, `TrigCopySpell`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy1`, `TrigDig`, `TrigDmg`, `TrigDraw`, `TrigGain`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigStore`, `TrigToken`
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
  Observed values: `Artifact`, `Artifact.inZoneBattlefield`, `Artifact.inZoneBattlefield,Creature.inZoneBattlefield`, `Artifact.inZoneBattlefield,Creature.inZoneBattlefield,Land.inZoneBattlefield`, `Card.AttachedBy`, `Card.inZoneGraveyard`, `Card.Self`, `Creature.EnchantedBy`, `Creature.EquippedBy+inRealZoneBattlefield`, `Creature.inZoneBattlefield,Land.inZoneBattlefield`, `Creature.YouOwn`, `Elemental.inZoneBattlefield`, `Permanent.inZoneBattlefield`, `Planeswalker.Chandra`, `Planeswalker.ChosenType`, `Planeswalker.EnchantedBy+inRealZoneBattlefield`, `Planeswalker.Sarkhan`
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
  Observed values: `TrigDigUntil`, `TrigDrain`, `TrigPutCounter`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Saga.YouCtrl`
- `ValidSpellAbility$`: TODO: Describe this parameter.
  Observed values: `Ability.LastChapter`, `SpellAbility.ManaAbility`, `Triggered.LastChapter`

## `AbilityTriggered`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBProbingTelepathy`, `TrigBigToken`, `TrigCounter`, `TrigPutCounter`
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
  Observed values: `ExileSelf`
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
  Observed values: `ExileEffect`, `RolledWalk`, `Sacrifice`, `TrigChange`, `TrigDestroy`, `TrigDestroyAll`, `TrigExile`, `TrigFlip`, `TrigLoseGame`, `TrigLurkingJackalsAnimate`, `TrigOpalAvengerAnimate`, `TrigRemove`, `TrigRepeatEach`, `TrigSac`, `TrigSacrifice`, `TrigSacSelf`, `TrigToken`, `TrigTransform`, `TrigVCAnimate`, `TrigWin`, `TrigWinGame`
- `HasColorCreatureInPlay$`: TODO: Describe this parameter.
  Observed values: `GWU`, `RGW`
- `HasColorInGraveyard$`: TODO: Describe this parameter.
  Observed values: `U`
- `HasCreatureInPlay$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.Other+YouCtrl`, `Artifact.YouCtrl`, `Card.Other`, `Card.Self+counters_EQ0_ICE`, `Card.Self+counters_EQ0_P1P1`, `Card.Self+counters_GE1000_TIME`, `Card.Self+counters_GE3_PLAGUE`, `Card.Self+counters_GE4_DEPLETION`, `Card.Self+counters_GE4_PAGE`, `Card.Self+counters_GE4_TIDE`, `Card.Self+counters_GE5_PLOT`, `Card.Self+counters_GE9_INCARNATION`, `Card.Self+counters_GEX_CHARGE+YouCtrl`, `Card.Self+counters_LE2_LOYALTY`, `Card.Self+Enchantment`, `Card.Self+OwnerDoesntControl`, `Card.Self+withFlying`, `Card.Thrull+YouCtrl`, `Card.TopLibrary+YouCtrl+!IsRemembered`, `Card.YouCtrl`, `Creature`, `Creature.counters_GE4_FUSE`, `Creature.OppCtrl`, `Creature.Other+YouCtrl`, `Creature.powerGE4+OppCtrl`, `Creature.Self+powerGE7`, `Creature.toughnessLE2+YouCtrl`, `Dwarf.YouCtrl`, `Enchantment.YouCtrl`, `Forest.YouCtrl`, `Island.YouCtrl`, `Land`, `Land.Snow+YouCtrl`, `Land.YouCtrl`, `Permanent.!token+ChosenColor+ChosenCtrl`, `Permanent.!token+setARN+Other`, `Permanent.counters_GE1_PHYLACTERY+YouCtrl`, `Permanent.YouCtrl+ChosenColor`, `Swamp.YouCtrl`, `Vampire.YouCtrl+Legendary`
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
  Observed values: `Card.EffectSource`, `Card.IsRemembered`, `Card.Self`, `Creature.YouCtrl`

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
  Observed values: `DBClone`, `TrigChoose`, `TrigClone`, `TrigCopy`, `TrigGainControl`, `TrigTap`, `TrigToken`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetRelativeToSource$`: TODO: Describe this parameter.
  Observed values: `Permanent.nonLand+OppCtrl+cmcLEX`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Aura`, `Aura.YouCtrl`, `Card.Self`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature.YouCtrl`

## `AttackerBlocked`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `ABBarrelingPump`, `AddSpores`, `DelayedTrig`, `DelTrig`, `HalfHeartTrigSacrifice`, `LaccolithDmg`, `MakeEffective`, `PumpSelf`, `StormsurgeKrakenDraw`, `TrigBlockedPump`, `TrigBounce`, `TrigCharm`, `TrigChooseBlockers`, `TrigClash`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDiscard`, `TrigDrain`, `TrigDraw`, `TrigExile`, `TrigFog`, `TrigGain`, `TrigMill`, `TrigNoDamage`, `TrigPeek`, `TrigPump`, `TrigPump2`, `TrigPutCounter`, `TrigRegen`, `TrigReturn`, `TrigSac`, `TrigTap`, `TrigTapAll`, `TrigToken`, `TrigTokenBlocking`, `TrigUntap`, `TrigUntapAll`, `TrigUntapRemove`
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
  Observed values: `Beast`, `Card.AttachedBy`, `Card.EquippedBy`, `Card.IsRemembered`, `Card.Self`, `Card.Self,Creature.EquippedBy`, `Card.YouCtrl`, `Creature`, `Creature.attacking Opponent`, `Creature.Black,Creature.Red`, `Creature.enchanted+YouCtrl`, `Creature.EquippedBy`, `Creature.withFlying`, `Creature.withoutFlying`, `Creature.YouCtrl`, `Creature.YouCtrl+withMenace`, `Goblin.YouCtrl+Other`, `Rat.YouCtrl`, `Sliver`

## `AttackerBlockedByCreature`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `ABDestroy`, `DBLoseLife`, `DelayAttackTrig`, `DelTrig`, `DelTrigAttacker`, `DelTrigBlocked`, `DelTrigBlocker`, `DestroyAttacker`, `DestroyBlocker`, `PumpAttacker`, `PumpBlocker`, `RetaliationTrigPump`, `RogueDamage`, `TrigAnimateAttacker`, `TrigAnimateBlocker`, `TrigAnimateDefender`, `TrigBlocked`, `TrigBlockedPump`, `TrigBlocks`, `TrigChangeZone`, `TrigDamage`, `TrigDamageAttacker`, `TrigDamageBlocker`, `TrigDealDamage`, `TrigDealDamageAttack`, `TrigDealDamageBlock`, `TrigDestroy`, `TrigDestroyAttacker`, `TrigDestroyBlocked`, `TrigDestroyBlocker`, `TrigDraw`, `TrigEffect`, `TrigEndCombat`, `TrigExile`, `TrigLoseLife`, `TrigPhaseAttacker`, `TrigPhaseBlocker`, `TrigPump`, `TrigPumpAttacker`, `TrigPumpBlocker`, `TrigPumpShark`, `TrigPutCounter`
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
  Observed values: `Card.AttachedBy`, `Card.EffectSource`, `Card.EnchantedBy`, `Card.Self`, `Creature`, `Creature.AttachedBy`, `Creature.EnchantedBy`, `Creature.equipped`, `Creature.Green,Creature.White`, `Creature.IsRemembered`, `Creature.nonBlack`, `Creature.nonWall`, `Creature.powerLE1`, `Creature.toughnessLE3`, `Creature.Vampire`, `Creature.wasDealtDamageThisTurn`, `Creature.White`, `Creature.withDeathtouch`, `LessPowerThanBlocker`

## `AttackerBlockedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDraw`, `TrigPump`, `TrigTreasure`
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
  Observed values: `DBDamage`, `DBDraw`, `DBGainLife`, `DBLoseLife`, `DBPump`, `DBPutCounter`, `DBRepeat`, `DBToken`, `DBTransform`, `DBUnTapAll`, `DelTrigEOC`, `TrigAnimate`, `TrigBolster`, `TrigChangeZone`, `TrigCharm`, `TrigChoose`, `TrigConjure`, `TrigConnive`, `TrigCopy`, `TrigCounter`, `TrigCounterAttacker`, `TrigCounters`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDig`, `TrigDiscard`, `TrigDiscover`, `TrigDmg`, `TrigDoubleCounters`, `TrigDraft`, `TrigDrain`, `TrigDraw`, `TrigEarthbend`, `TrigEffect`, `TrigEnergy`, `TrigExile`, `TrigExperience`, `TrigFight`, `TrigFood`, `TrigGainControl`, `TrigGainLife`, `TrigGenericChoice`, `TrigImmediateTrig`, `TrigIndestructible`, `TrigInvestigate`, `TrigLoot`, `TrigLoseLife`, `TrigMana`, `TrigMill`, `TrigPopulate`, `TrigPrepare`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigRepeat`, `TrigRepeatDefender`, `TrigRepeatEach`, `TrigReturn`, `TrigSac`, `TrigScry`, `TrigSearch`, `TrigState`, `TrigSuppression`, `TrigSurveil`, `TrigTapOrUntap`, `TrigTheyDraw`, `TrigToken`, `TrigTransform`, `TrigTreasure`, `TrigUnblockable`, `TrigUntap`, `TrigUntapAll`, `TrigWalkerPump`
- `FirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+IsSolved`, `Card.StrictlySelf`, `Card.tapped`, `Card.untapped`, `Creature.attacking`, `Creature.attacking+Other+YouCtrl+Legendary`, `Creature.attackingYou`, `Creature.YouCtrl+attacking+nonWall`
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
  Observed values: `DBTreasure`, `TrigAnimate`, `TrigCharm`, `TrigCopy`, `TrigDealDamage`, `TrigDraw`, `TrigDrawAndDamage`, `TrigExile`, `TrigFood`, `TrigGoad`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigRadiation`, `TrigReveal`, `TrigTap`, `TrigToken`
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
  Observed values: `Damage`, `DBChangeZone`, `DBNoCombatDamage`, `FarrelDmg`, `FrenzyPump`, `GainLife`, `TrigActivateManaAbility`, `TrigChange`, `TrigDamage`, `TrigDestroy`, `TrigDestroyCreature`, `TrigDig`, `TrigDiscard`, `TrigDiscards`, `TrigDraw`, `TrigExile`, `TrigGainControl`, `TrigGainLife`, `TrigLoseLife`, `TrigPlay`, `TrigPoison`, `TrigPump`, `TrigSacrifice`, `TrigToken`, `TrigTransform`, `TrigUntap`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.Self`, `Creature`, `Creature.EnchantedBy`, `Creature.Legendary+YouCtrl`, `Creature.YouCtrl`, `Rogue.YouCtrl`
- `ValidDefender$`: TODO: Describe this parameter.
  Observed values: `Player`, `You,Planeswalker.YouCtrl`

## `AttackerUnblockedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDraw2`
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
  Observed values: `Abandon`, `ABImpulse`, `AnimosityPump`, `AnthemPump`, `ArmorConjure`, `Aurify`, `BearUmbraUntap`, `CCCToken`, `CheckPower`, `CoinFlip`, `DBAnimate`, `DBAttach`, `DBBlight`, `DBChangeZone`, `DBClone`, `DBCounter`, `DBDealDamage`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDmg`, `DBDraw`, `DBEffect`, `DBExile`, `DBFlip`, `DBLoop`, `DBMustBlock`, `DBNoCombatDamage`, `DBOpen`, `DBPump`, `DBRepeat`, `DBSacrifice`, `DBScry`, `DBTap`, `DBTreasure`, `DBTrigRollDice`, `DBUnblockable`, `DBUntap`, `DBVenture`, `Debuff`, `DebuffAttacker10`, `DelayedTransform`, `DelayedTrig`, `DelayTrig`, `DelBounce`, `DelTrig`, `DelTrigDestroy`, `Detain`, `DmgDistro`, `DragonWake`, `DrawACard`, `EachName`, `FlipCoin`, `GrothamaFight`, `HeraldsWarCry`, `HeroPump`, `JacePump`, `LaunchTokenAttacking`, `LiftMountain`, `MtendaLionPump`, `NorinExile`, `PatronLife`, `Pump`, `PumpTrample`, `RubblebeltWarCry`, `SaintTraftToken`, `StayTapped`, `TamiyoPump`, `TapOneEach`, `TgtNoBlock`, `ThorncasterDmg`, `TowerAboveTrigBlock`, `TrigAddCombat`, `TrigAmass`, `TrigAngelToken`, `TrigAnimate`, `TrigAnimateAll`, `TrigAttach`, `TrigAttackAttach`, `TrigBattalionDmg`, `TrigBattalionEffect`, `TrigBattalionPump`, `TrigBattleCry`, `TrigBolster`, `TrigBorrow`, `TrigBounce`, `TrigBranch`, `TrigCanNotBlock`, `TrigCantBlock`, `TrigCast`, `TrigChange`, `TrigChangeZone`, `TrigCharge`, `TrigCharm`, `TrigChoice`, `TrigChoose`, `TrigChooseNumber`, `TrigChoosePump`, `TrigClash`, `TrigClearRem`, `TrigClockworkRemoveCounter`, `TrigClone`, `TrigConjure`, `TrigConnive`, `TrigCopy`, `TrigCopyPermanent`, `TrigCounter`, `TrigCounters`, `TrigCurse`, `TrigDamage`, `TrigDamage1`, `TrigDamageAll`, `TrigDealDamage`, `TrigDebuff`, `TrigDelayedTrig`, `TrigDelayedTrigger`, `TrigDelTrig`, `TrigDestroy`, `TrigDestroy2`, `TrigDestroyAll`, `TrigDig`, `TrigDigMulti`, `TrigDigUntil`, `TrigDiscard`, `TrigDiscover`, `TrigDmg`, `TrigDouble`, `TrigDoubleCounters`, `TrigDoubleLife`, `TrigDoublePower`, `TrigDoubleToughness`, `TrigDraft`, `TrigDrain`, `TrigDraw`, `TrigDraw1`, `TrigDraw2`, `TrigDread`, `TrigEarthbend`, `TrigEff`, `TrigEffect`, `TrigEggCounter`, `TrigEndure`, `TrigEnergy`, `TrigExchangeDamage`, `TrigExile`, `TrigExileN`, `TrigExperience`, `TrigExplore`, `TrigFight`, `TrigFlashback`, `TrigFlicker`, `TrigFlipCoins`, `TrigFlying`, `TrigFood`, `TrigForceBlock`, `TrigFormidable`, `TrigGain`, `TrigGainControl`, `TrigGainLife`, `TrigGetCooler`, `TrigGoad`, `TrigGuess`, `TrigHeist`, `TrigImmediate`, `TrigImmediateTrig`, `TrigInfectionCounter`, `TrigInstantEffect`, `TrigInvestigate`, `TrigJoinForces`, `TrigLimitBlock`, `TrigLook`, `TrigLoot`, `TrigLose`, `TrigLoseLife`, `TrigLoseLifeAttack`, `TrigLure`, `TrigMana`, `TrigMassacre`, `TrigMill`, `TrigMustBlock`, `TrigNameCard`, `TrigOdricEffect`, `TrigPeek`, `TrigPlay`, `TrigPrepare`, `TrigProliferate`, `TrigProvoke`, `TrigPump`, `TrigPump1`, `TrigPump2`, `TrigPumpA`, `TrigPumpAll`, `TrigPumpAtt`, `TrigPumpAttack`, `TrigPut`, `TrigPutCounter`, `TrigPutCounter1`, `TrigPutCounterAll`, `TrigPutCounters`, `TrigRadiation`, `TrigRamp`, `TrigRandom`, `TrigReanimate`, `TrigRemoveCounter`, `TrigRepeat`, `TrigRepeatTypes`, `TrigReturn`, `TrigReveal`, `TrigRoll`, `TrigRollDice`, `TrigSac`, `TrigSacrifice`, `TrigSacUnless`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSelectTargetCreature`, `TrigShrink`, `TrigShuffle`, `TrigSoulcall`, `TrigStangg`, `TrigSteal`, `TrigStunCounter`, `TrigSurveil`, `TrigSuspect`, `TrigTap`, `TrigTapAll`, `TrigTapOrUntap`, `TrigTapUnTap`, `TrigTarget`, `TrigTempt`, `TrigToken`, `TrigTokenAttacking`, `TrigTransform`, `TrigTreasure`, `TrigTrigger`, `TrigUnblockable`, `TrigUntap`, `TrigUntapAll`, `TrigUntapAllSnow`, `TrigVenture`, `TrigVillainousChoice`, `TrigVote`, `TrigWinGame`, `TripPump`
- `FirstAttack$`: TODO: Describe this parameter.
  Observed values: `True`
- `FirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Artifact.YouCtrl,Enchantment.YouCtrl`, `Blood.token+DefenderCtrl`, `Blood.token+YouCtrl`, `Card.DefenderCtrl`, `Card.ExiledWithSource`, `Card.Self+attackedThisCombat`, `Card.Self+enchanted`, `Card.Self+equipped`, `Card.Self+IsRenowned`, `Card.Self+IsSuspected`, `Card.Self+modified`, `Card.Self+powerGE6`, `Card.Self+withDefender`, `Card.Self+withFirst Strike`, `Card.Time Lord+YouCtrl`, `Card.YouCtrl`, `Creature.attacking+!EquippedBy`, `Creature.attacking+Other`, `Creature.Dinosaur+YouCtrl`, `Creature.Glimmer+DefenderCtrl`, `Creature.greatestPower+YouCtrl`, `Creature.nonHuman+Other+YouCtrl`, `Creature.Pirate+Other+!token+YouCtrl`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+namedDarkstar`, `Creature.YouCtrl+powerGE4`, `Creature.YouOwn`, `Devil.token+YouCtrl`, `Dinosaur.YouCtrl`, `Dinosaur.YouCtrl+Other`, `Human.attacking+Other`, `Land.untapped+YouCtrl`, `Land.YouCtrl`, `Monkey.Legendary+YouCtrl`, `Permanent.Black+!token+DefenderCtrl`, `Permanent.Black+DefenderCtrl`, `Permanent.Dragon+YouCtrl`, `Permanent.token+YouCtrl`, `Planeswalker.Chandra+YouCtrl`, `Planeswalker.Ral+YouCtrl`, `Planeswalker.Teferi+YouCtrl`, `Planeswalker.Vraska+YouCtrl`, `Wall.DefenderCtrl`, `Warrior.attacking+Other`, `Warrior.Other+YourTeamCtrl`
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
  Observed values: `Army.YouCtrl`, `Assassin.YouCtrl`, `Bat.YouCtrl`, `Berserker`, `Boar.YouCtrl`, `Card`, `Card.AttachedBy`, `Card.AttachedBy+powerLE2`, `Card.EnchantedBy`, `Card.EquippedBy`, `Card.IsCommander+YouOwn`, `Card.Knight+YouCtrl`, `Card.Kraken,Card.Leviathan,Card.Merfolk,Card.Octopus,Card.Serpent`, `Card.Self`, `Card.Self+IsSaddled`, `Card.Self,Card.IsCommander+YouCtrl`, `Card.Self,Creature.EnchantedBy`, `Card.Self,Creature.EquippedBy`, `Creature`, `Creature.!token+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.Assassin+YouCtrl`, `Creature.Cat+Other+YouCtrl`, `Creature.ChosenType+YouCtrl`, `Creature.counters_GE1_MAGNET`, `Creature.counters_GE1_P1P1`, `Creature.Elf+YouCtrl`, `Creature.enchanted`, `Creature.enchanted+YouCtrl,Creature.Enchantment+YouCtrl`, `Creature.enchanted+YouCtrl,Creature.YouCtrl+equipped`, `Creature.EnchantedBy`, `Creature.equalPT+YouCtrl`, `Creature.equipped+YouCtrl`, `Creature.equipped+YouCtrl+Other`, `Creature.EquippedBy`, `Creature.HasCounters`, `Creature.IsCommander+YouCtrl`, `Creature.IsGoaded`, `Creature.IsRemembered`, `Creature.modified+YouCtrl`, `Creature.NamedCard+YouCtrl`, `Creature.nonHuman+YouCtrl`, `Creature.OppCtrl`, `Creature.powerGE4`, `Creature.powerLE1+YouCtrl`, `Creature.powerLE2+YouCtrl`, `Creature.Self`, `Creature.Vampire+YouCtrl`, `Creature.White+YouCtrl`, `Creature.withFlying`, `Creature.withFlying+YouCtrl,Creature.withHaste+YouCtrl`, `Creature.withoutFlying`, `Creature.withToxic+Other+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+basePowerEQ2+baseToughnessEQ2`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+enlistedThisCombat`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+hasManaAbility`, `Creature.YouCtrl+Historic`, `Creature.YouCtrl+OppOwn`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+withDeathtouch`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withHaste`, `Creature.YouCtrl+withMenace`, `Creature.YouCtrl+withReach`, `Creature.YouCtrl+withTrample`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl+YouOwn`, `Creature.Zombie+token+YouCtrl+powerGE6`, `Dragon.YouCtrl`, `Frog.YouCtrl`, `Insect.YouCtrl,Leech.YouCtrl,Slug.YouCtrl,Worm.YouCtrl`, `Minotaur.YouCtrl`, `Mount.YouCtrl,Vehicle.YouCtrl`, `Pirate.YouCtrl`, `Samurai.YouCtrl,Warrior.YouCtrl`, `Sliver.YouCtrl`, `Vehicle.CrewedBySourceThisTurn`, `Vehicle.YouCtrl`, `Warrior`, `Wolf.YouCtrl`
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
  Observed values: `TrigConvert`, `TrigDrain`, `TrigEffect`, `TrigReturn`, `TrigSac`
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
  Observed values: `ExileAll`, `TrigAnimate`, `TrigCopy`, `TrigDamageAll`, `TrigDestroy`, `TrigDestroyAll`, `TrigDmg`, `TrigExile`, `TrigGoad`, `TrigPump`, `TrigPutCounter`, `TrigSac`, `TrigTap`, `TrigToken`
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
  Observed values: `TrigDraw`, `TrigSearch`
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
  Observed values: `DBAnimate`, `DBPumpAll`, `TrigAnimate`, `TrigClone`
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
  Observed values: `TrigDealDamage`, `TrigPump`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `BecomesSaddled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigMill`
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
  Observed values: `Abandon`, `CrystallineNautilusSac`, `DBFight`, `DBForget`, `DBGainLife`, `DBToken`, `DismissSac`, `GlasskiteCounter`, `KiraGlassSpinnerCounter`, `LivewireDamage`, `MakeshiftSac`, `NaduDig`, `OpalineTrigDraw`, `PhantasmalImageSac`, `SlasherSac`, `TrigAirbend`, `TrigBlink`, `TrigBounce`, `TrigChange`, `TrigChangeZone`, `TrigChoose`, `TrigConnive`, `TrigCopy`, `TrigCounter`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDmg`, `TrigDrain`, `TrigDraw`, `TrigExile`, `TrigFight`, `TrigGainControl`, `TrigLoseLife`, `TrigLoseLife5`, `TrigMill`, `TrigPeekAndReveal`, `TrigPhaseOut`, `TrigPoison`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterTriggered`, `TrigReturn`, `TrigSac`, `TrigShuffle`, `TrigTap`, `TrigToken`, `TrigUntap`, `WildPump`
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
  Observed values: `Ability.Backup`, `Ability.Land+namedLabyrinth of Skophos+YouCtrl`, `Ability.numTargets EQ1`, `Activated.Creature+Other+namedGoblin Artisans`, `Instant,Sorcery`, `Spell`, `Spell.Aura`, `Spell.OppCtrl`, `Spell.YouCtrl`, `SpellAbility`, `SpellAbility.OppCtrl`, `SpellAbility.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.AttachedBy`, `Card.Creature+inZoneBattlefield`, `Card.EnchantedBy`, `Card.Self`, `Card.Self,Spirit.YouCtrl+Other+inZoneBattlefield`, `Cleric.Creature+YouCtrl+inZoneBattlefield`, `Creature.EnchantedBy`, `Creature.inZoneBattlefield`, `Creature.inZoneBattlefield+YouCtrl`, `Creature.OppCtrl+inZoneBattlefield`, `Creature.Other`, `Creature.Other+YouCtrl+inZoneBattlefield`, `Creature.Self`, `Creature.Sliver+YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+counters_GE1_P1P1+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield,Planeswalker.YouCtrl+inZoneBattlefield`, `Creature.YouCtrl+inZoneBattlefield,Spell.Creature+YouCtrl`, `Dragon.inZoneBattlefield+YouCtrl`, `Dragon.YouCtrl+inZoneBattlefield`, `Permanent.YouCtrl+inZoneBattlefield`, `Permanent.YouCtrl+Other+inZoneBattlefield`, `Player.Chosen`, `Spell`, `Wolf.YouCtrl+inZoneBattlefield,Werewolf.YouCtrl+inZoneBattlefield`, `You`, `You,Permanent.YouCtrl+inZoneBattlefield`, `You,Permanent.YouCtrl+Other+inZoneBattlefield`

## `BecomesTargetOnce`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDmg`, `TrigDraw`, `TrigReveal`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Card.!namedPsychic Battle`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Activated`, `SpellAbility.OppCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inZoneBattlefield`, `You,Permanent.YouCtrl+inZoneBattlefield`

## `BlockersDeclared`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `WarFlip`
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
  Observed values: `Animate`, `Aurify`, `ChangeControl`, `CoinFlip`, `DBNoCombatDamage`, `DelayedTrig`, `DelayTrig`, `DelTrig`, `DelTrigDestroy`, `EffDraw`, `FlipCoin`, `HeroPump`, `Pump`, `PumpSelf`, `TrigBlockedPump`, `TrigBounce`, `TrigCharm`, `TrigChooseAttackers`, `TrigClockworkRemoveCounter`, `TrigDamage`, `TrigDamage2`, `TrigDealDamage`, `TrigDebuff`, `TrigDestroy3`, `TrigDigUntil`, `TrigDrain`, `TrigDraw`, `TrigEnergy`, `TrigExchangePower`, `TrigGainLife`, `TrigJoinForces`, `TrigLoot`, `TrigLoseLife`, `TrigLoseLifeBlock`, `TrigMill`, `TrigPoison`, `TrigPrevent`, `TrigPump`, `TrigPump1`, `TrigPump2`, `TrigPumpAll`, `TrigPumpB`, `TrigPumpBlo`, `TrigPumpBlock`, `TrigPutCounter`, `TrigPutCounter2`, `TrigRem`, `TrigRemoveCounter`, `TrigReturn`, `TrigRoll`, `TrigSac`, `TrigScry`, `TrigToken`, `TrigUntap`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.blockedBySource`, `Creature.nonHuman+Other+YouCtrl`, `Dinosaur.YouCtrl`, `Planeswalker.Vraska+YouCtrl`
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
  Observed values: `Card.AttachedBy`, `Card.EnchantedBy`, `Card.EquippedBy`, `Card.Self`, `Creature`, `Creature.OppCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+withDefender`

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
  Observed values: `Card.EffectSource`, `Card.IsRemembered`, `Card.Self`, `Creature.IsRemembered`
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
  Observed values: `Card.EffectSource`, `Card.IsRemembered`, `Card.Self`, `Creature`, `Creature.!IsRemembered`, `Creature.!RememberedPlayerCtrl`, `Creature.ChosenCtrl`, `Creature.IsRemembered`, `Creature.nonChosenCard`, `Creature.nonLand`, `Creature.RememberedPlayerCtrl`, `Creature.withoutFlying+!hasKeywordLandwalk:Island`, `Creature.YouCtrl`, `Creature.YouCtrl+!ChosenCardStrict`

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
  Observed values: `Card.Self`, `Creature`

## `CantBeActivated`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.IsRemembered`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.IsRemembered`, `Permanent.IsRemembered`, `Planeswalker`
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
  Observed values: `Card`, `Card.!wasCastFromTheirHand`, `Card.cmcEQX`, `Card.Creature`, `Card.IsRemembered`, `Card.NamedCard`, `Card.nonCreature`, `Card.nonLand`, `Card.nonLand+NamedCard`, `Card.nonLand+sharesNameWith RememberedLKI`, `Creature`, `Creature,Planeswalker`, `Instant,Sorcery`

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
  Observed values: `Creature.IsRemembered`, `Creature.OppCtrl`, `Creature.OppCtrl+powerLEX`, `Creature.powerLTtoughness`, `Creature.RememberedPlayerCtrl`, `Creature.Self`

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
  Observed values: `Card.IsRemembered`, `Creature.DamagedBy`, `Creature.DamagedBy Remembered`

## `CantSacrifice`

TODO: Write documentation.

**Parameters:**
- `ActiveZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Description$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.IsRemembered+YouCtrl`, `Card.Self`

## `CantTarget`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.Opponent`
- `Description$`: TODO: Describe this parameter.
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell,Activated`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Blue+OppCtrl,Card.Black+OppCtrl`, `Card.Blue,Card.Black`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.Permanent,Player`, `Creature.YouCtrl`, `Permanent.YouCtrl`

## `CaseSolved`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDig`
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
  Observed values: `Card`, `Card.ChosenType`, `Card.Creature`, `Creature`, `Dinosaur`, `Planeswalker.YouCtrl`, `Sorcery`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Loyalty`, `Spell`

## `Championed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigTapAll`
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
  Observed values: `DBChangeZoneAll`, `GoToYard`, `TrigChoose`, `TrigDraw`, `TrigExile`, `TrigToken`, `TrigUnattach`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerController$`: TODO: Describe this parameter.
  Observed values: `TriggeredOriginalController`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.OppCtrl`, `Card.Self`
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
  Observed values: `Abandon`, `ABDraw`, `ABMana`, `AbnormalEnduranceTrigChangeZone`, `AirFight`, `AndJusticeForAll`, `AngelicSalvation`, `AssassinsFlip`, `AtRaVZombie`, `AuthorityExile`, `BailOutChangeZone`, `BarricadePumped`, `BehemothPump`, `BereavementDiscard`, `BlazeDmg`, `BringBackThoughts`, `CastEach`, `Catalogue`, `CatharsCounters`, `CemeteryPucaCopy`, `ChooseCreatures`, `ChooseOpp`, `ChooseP`, `CleanTheBlade`, `ConstrictingExile`, `CoRNonDmg`, `CoRSpiritDmg`, `DamageAndMoreDamage`, `DBAddTurn`, `DBAmass`, `DBAnimate`, `DBAskOpponentDrawOrPlay`, `DBAttach`, `DBBoon`, `DBCardChoice`, `DBChangeZone`, `DBChangeZoneAll`, `DBChoice`, `DBChoosePlayer`, `DBChooseSb`, `DBCleanImprinted`, `DBCleanup`, `DBCleanup2`, `DBCopy`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDestroy`, `DBDestroyAll`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDmg`, `DBDraw`, `DBEffect`, `DBExchangeText`, `DBExile`, `DBExileMe`, `DBFetch`, `DBFight`, `DBFight13U`, `DBForEach`, `DBForget`, `DBGainLife`, `DBLose`, `DBLoseLife`, `DBMana`, `DBMill`, `DBOpen`, `DBPhaseIn`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBPutCounterAll`, `DBRemember`, `DBRepeat`, `DBReturn`, `DBSac`, `DBSacrifice`, `DBSacSelf`, `DBScry`, `DBSearch`, `DBSeek`, `DBTap`, `DBToken`, `DBTokens`, `DBTreasure`, `DBTreasureTokens`, `DBTrigger`, `DBVenture`, `DeathGift`, `DelayedReturn`, `DelayedTrig`, `DelTrig`, `DelTrigLeaves`, `DelTrigReturn`, `DelTrigSlowtrip`, `DestroyOneEach`, `DestroyRemembered`, `Detain`, `DevilTakeYou`, `Disinter`, `Dmg1`, `DmgDistro`, `DrawACard`, `DropMountain`, `EachOpponent`, `EatMyThoughts`, `EatSomeDays`, `EffDealDamage`, `EffMassToken`, `EliteDefence`, `EquipmentSelection`, `ETBExileAbility`, `ETBExileReturn`, `EternalCounters`, `EverFlameCopy`, `ExileAll`, `ExileAndToken`, `ExileDraw`, `ExileEffect`, `ExileOneEach`, `ExileSelf`, `ExileTop`, `ExileTwin`, `FeatherDuster`, `ForgetCard`, `FreeCard`, `GalufPutCounter`, `GetUp`, `GoodWood`, `GoToYard`, `GraveAuras`, `GrinningDiscard`, `GuestList`, `HarmonicDestroy`, `HatchlingFight`, `HavenLife`, `HeroAttach`, `HistoricExile`, `HofriTrigReturn`, `HonorGained`, `HuatliDraw`, `InfernalDraw`, `KickedGiant`, `LavabellyTrigDmg`, `LazavCopy`, `Life`, `LiftMountain`, `LoseTrack`, `LukkaDmg`, `MathasPayoffDraw`, `MesmericFateseal`, `MindFishing`, `NurturingPump`, `OnHostLost`, `OppRevealX`, `OrbToken`, `OssuaryCounters`, `PaymentCheck`, `PerigeeBeckonerTrigChangeZone`, `PhantomSearch`, `PounceAdvantage`, `PumpRandom`, `PutKeywordCounter`, `RaiseDead`, `RDCopy`, `ReanimateDmg`, `RememberController`, `RememberInitialAttach`, `RemoveCounters`, `RepeatEachOpp`, `RepeatPayment`, `ResetSVars`, `RestorationExile`, `ReturnOneEach`, `RevenantSkipCombat`, `RollD20`, `SacMount`, `SacTarget`, `SacTwin`, `SarkanCopy`, `ScoutSearch`, `ScytheReturn`, `SetupSearch`, `ShowstopperTrigDamage`, `ShuffleCard`, `SmallBurnination`, `SquadronEnlist`, `SupernaturalStaminaTrigChangeZone`, `SVar2`, `SwarmSpread`, `TailSpikes`, `TakenumaDraw`, `TakeOneEach`, `TamiyoReturn`, `TempAttackTax`, `ThicketKicker`, `ThornbiteTrigUntap`, `ThunderDamage`, `Token`, `TokenAndLife`, `TrigAbandon`, `TrigABChangeZone`, `TrigAbsolve`, `TrigAdd`, `TrigAddCounter`, `TrigAddMana`, `TrigAddOrRemoveCounter`, `TrigAddPhase`, `TrigAirbend`, `TrigAmass`, `TrigAnimate`, `TrigAnimateAll`, `TrigAnimateTomb`, `TrigAssemble`, `TrigAttach`, `TrigAttachAll`, `TrigAuraAttach`, `TrigAurify`, `TrigBattleCry`, `TrigBird`, `TrigBite`, `TrigBlight`, `TrigBlink`, `TrigBlood`, `TrigBodySnatcherExileMe`, `TrigBolster`, `TrigBoon`, `TrigBottom`, `TrigBounce`, `TrigBounceAll`, `TrigBounceMe`, `TrigBranch`, `TrigCanNotBlock`, `TrigCantBlock`, `TrigCataclysm`, `TrigChange`, `TrigChange2`, `TrigChangeAll`, `TrigChangeAttacker`, `TrigChangeHand`, `TrigChangeInstant`, `TrigChangeZone`, `TrigChangeZone1`, `TrigChangeZone2`, `TrigChangeZoneAll`, `TrigChangeZoneBis`, `TrigChangeZoneBlue`, `TrigChangeZoneRed`, `TrigCharge`, `TrigCharm`, `TrigChoice`, `TrigChoose`, `TrigChooseBis`, `TrigChooseColor`, `TrigChooseCT`, `TrigChooseDirection`, `TrigChooseExile`, `TrigChooseNumber`, `TrigChooseOpp`, `TrigChoosePlayer`, `TrigChooseThree`, `TrigChooseType`, `TrigClash`, `TrigCloak`, `TrigClone`, `TrigClue`, `TrigConjure`, `TrigConjure1`, `TrigConnive`, `TrigControl`, `TrigCopy`, `TrigCopyEquip`, `TrigCopyPermanent`, `TrigCounter`, `TrigCounterAbility`, `TrigCounterDist`, `TrigCounters`, `TrigCurse`, `TrigDamage`, `TrigDamage2`, `TrigDamageAll`, `TrigDamageAllFlyers`, `TrigDamageAllFlyersAndPlayers`, `TrigDamageAllNonFlyers`, `TrigDamageCreature`, `TrigDamageDies`, `TrigDamageEach`, `TrigDay`, `TrigDealDamage`, `TrigDealDamage1`, `TrigDealDamage2pts`, `TrigDealDamage4pts`, `TrigDeath`, `TrigDebuff`, `TrigDelay`, `TrigDelay2`, `TrigDelayedTrig`, `TrigDelayedTrigger`, `TrigDelayTransform`, `TrigDelayTrigger`, `TrigDestroy`, `TrigDestroyA`, `TrigDestroyAll`, `TrigDestroyE`, `TrigDestroyYourLand`, `TrigDiceRoll`, `TrigDiesToken`, `TrigDig`, `TrigDigMulti`, `TrigDigShrine`, `TrigDigUntil`, `TrigDiscard`, `TrigDiscardThree`, `TrigDiscover`, `TrigDmg`, `TrigDmg1`, `TrigDmgOpp`, `TrigDouble`, `TrigDoubleCounters`, `TrigDoublePower`, `TrigDraft`, `TrigDrain`, `TrigDraw`, `TrigDraw1`, `TrigDraw2`, `TrigDrawDiscard`, `TrigDread`, `TrigDualCopy`, `TrigDualExile`, `TrigDualExileAll`, `TrigEach`, `TrigEachAttacker`, `TrigEachOpp`, `TrigEarthbend`, `TrigEffect`, `TrigEndure`, `TrigEnduringBounce`, `TrigEnergy`, `TrigEvidence`, `TrigExchange`, `TrigExchangeControl`, `TrigExchangeLife`, `TrigExcruciator`, `TrigExile`, `TrigExile1`, `TrigExile2`, `TrigExileAll`, `TrigExileAllSerfs`, `TrigExileAndBounce`, `TrigExileCreature`, `TrigExileGrave`, `TrigExileHand`, `TrigExileMe`, `TrigExileN`, `TrigExileSelf`, `TrigExileUnless`, `TrigExileYourLibrary`, `TrigExperience`, `TrigExploration`, `TrigExplore`, `TrigFaceUp`, `TrigFetch`, `TrigFight`, `TrigFightBis`, `TrigFlashback`, `TrigFlip`, `TrigFlipCoin`, `TrigFlipDamage`, `TrigFlying`, `TrigFood`, `TrigForget`, `TrigGain`, `TrigGainControl`, `TrigGainCounter`, `TrigGainLife`, `TrigGainLife1`, `TrigGainLife2`, `TrigGenericChoice`, `TriggeredBounce`, `TrigGoad`, `TrigGrave`, `TrigGraveyard`, `TrigHeist`, `TrigHexproof`, `TrigHit`, `TrigHumanToken`, `TrigImmediate`, `TrigImmediateTrig`, `TrigImmediateTrigger`, `TrigImprint`, `TrigIncrementCounters`, `TrigIncubate`, `TrigInitiative`, `TrigIntensify`, `TrigInvestigate`, `TrigJaddiLifestriderTap`, `TrigKeeperCascade`, `TrigKicker`, `TrigKicker2`, `TrigKnowledgeExile`, `TrigLands`, `TrigLearn`, `TrigLibrary`, `TrigLife`, `TrigLifelineDelay`, `TrigLook`, `TrigLoot`, `TrigLose`, `TrigLoseLife`, `TrigLoseLife1`, `TrigLoseLife2`, `TrigLoseLifeEmblem`, `TrigMakeCard`, `TrigMakeToken`, `TrigMana`, `TrigManifest`, `TrigManifestDread`, `TrigMarkBattlefield`, `TrigMartyrsSacrifice`, `TrigMassacre`, `TrigMesmericBounce`, `TrigMesmericExile`, `TrigMill`, `TrigMill1`, `TrigMinsc`, `TrigMonarch`, `TrigMoreMassacre`, `TrigMove`, `TrigMoveCounter`, `TrigMoveCounters`, `TrigNameCard`, `TrigNantukoDiscardLand`, `TrigNausea`, `TrigNoLose`, `TrigNote`, `TrigNoteNum`, `TrigOpenAttraction`, `TrigOppToken`, `TrigPay`, `TrigPayCost`, `TrigPeek`, `TrigPeekAndReveal`, `TrigPhaseOut`, `TrigPhases`, `TrigPickCard`, `TrigPlay`, `TrigPoison`, `TrigPopulate`, `TrigPrepare`, `TrigPrevent`, `TrigPrivateResearchDraw`, `TrigProcess`, `TrigProliferate`, `TrigProt`, `TrigProteanCopy`, `TrigProtect`, `TrigProvoke`, `TrigPump`, `TrigPump1`, `TrigPumpAll`, `TrigPumpCurse`, `TrigPumpEOT`, `TrigPumpETB`, `TrigPut`, `TrigPutCounter`, `TrigPutCounter1`, `TrigPutCounter2`, `TrigPutCounterAll`, `TrigPutCounterAll1`, `TrigPutCounterAll2`, `TrigPutCounterOpp`, `TrigPutCounterQuest`, `TrigPutCounters`, `TrigPutCountersAll`, `TrigRadiate`, `TrigRadiation`, `TrigRamp`, `TrigRandom`, `TrigReanimate`, `TrigRearrange`, `TrigRecall`, `TrigRemove`, `TrigRemoveCounter`, `TrigRemoveCounters`, `TrigRemoveFromCombat`, `TrigRepeat`, `TrigRepeatEach`, `TrigReset`, `TrigReturn`, `TrigReturn1`, `TrigReturn2`, `TrigReturnArti`, `TrigReturnCreatures`, `TrigReturnFromGraveyard`, `TrigReturnOther`, `TrigReturnOwner`, `TrigReveal`, `TrigRevealUntil`, `TrigRevive`, `TrigRoll`, `TrigRollDice`, `TrigRollETB`, `TrigSac`, `TrigSacAll`, `TrigSacPerm`, `TrigSacrifice`, `TrigSacrificeAll`, `TrigSacrificeBlack`, `TrigSacrificeBlue`, `TrigSacUnless`, `TrigSacZom`, `TrigSaddle`, `TrigScry`, `TrigSearch`, `TrigSearchHand`, `TrigSeek`, `TrigSeekLand`, `TrigSeekNonLand`, `TrigSeekTwo`, `TrigSetLife`, `TrigShuffle`, `TrigShuffleBack`, `TrigSkip`, `TrigSkipCombat`, `TrigSkipDraw`, `TrigSkipPhase`, `TrigSmallToken`, `TrigSpellweaverExile`, `TrigSrcy`, `TrigStangg`, `TrigSurveil`, `TrigSuspect`, `TrigTap`, `TrigTapAll`, `TrigTapOrUntap`, `TrigTaporUntapAll`, `TrigTarget`, `TrigTempt`, `TrigTgtOpp`, `TrigToken`, `TrigToken1`, `TrigToken2`, `TrigTokenChoice`, `TrigTokenSenior`, `TrigTokenTiny`, `TrigTransform`, `TrigTransform1`, `TrigTransform2`, `TrigTrap`, `TrigTreasure`, `TrigTremor`, `TrigTuck`, `TrigTurnFaceDown`, `TrigTutor`, `TrigTutorEquip`, `TrigUnattach`, `TrigUnblockable`, `TrigUnspecialize`, `TrigUntap`, `TrigUntapAll`, `TrigUrzaConstruct`, `TrigVenture`, `TrigVesuvaCopy`, `TrigVote`, `TrigWipeCounters`, `TrigYouLose`, `TripleGoat`, `TriReturn`, `TroubleMaking`, `TuktukDestroy`, `UnscytheTrigExile`, `USCopy`, `VampiricCounters`, `VampiricEmbraceCounters`, `VensersBounce`, `VerdantRebirthTrigChangeZone`, `VizierSearch`, `WeftwinderConjure`, `WhirlYou`, `WortETB`, `ZealotGained`
- `ForgetOnCast$`: TODO: Describe this parameter.
  Observed values: `Card.nonCreature+YouCtrl`
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `Hidden$`: TODO: Describe this parameter.
  Observed values: `True`
- `Host$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Artifact.YouCtrl,Enchantment.YouCtrl`, `Card.EnchantedBy+withFlying`, `Card.Outlaw+StrictlyOther+YouCtrl`, `Card.Self`, `Card.Self+counters_GE1_LOYALTY`, `Card.Self+counters_GE1_M1M1`, `Card.Self+counters_GE3_QUEST`, `Card.Self+Enchantment`, `Card.Self+namedAwestruck Cygnet`, `Card.Self+suspended`, `Card.StrictlySelf`, `Card.untapped`, `Card.YouCtrl`, `Card.YouCtrl+IsRingbearer`, `Card.YouCtrl+Other+Elf`, `Card.YouCtrl+token`, `Creature`, `Creature.Colorless+Other+YouCtrl`, `Creature.EnchantedBy+Red`, `Creature.EnchantedBy+withToxic`, `Creature.EnchantedBy+Wolf,Creature.EnchantedBy+Werewolf`, `Creature.IsImprinted`, `Creature.Other`, `Creature.Other+YouCtrl+counters_GE1_P1P1`, `Creature.Other+YouCtrl+powerGE4`, `Creature.Pirate+Other+YouCtrl`, `Creature.tapped+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+named"Name Sticker" Goblin`, `Creature.YouCtrl+namedBoo`, `Creature.YouCtrl+Other+namedFaerie Miscreant`, `Creature.YouCtrl+powerGE4`, `Enchantment.YouCtrl`, `Equipment.YouCtrl`, `Forest.YouCtrl`, `Gate.YouCtrl`, `Human.Other+YouCtrl`, `Island.YouCtrl`, `Knight.YouCtrl+Other`, `Land.tapped+YouCtrl`, `Land.YouCtrl`, `Land.YouCtrl+nonBasic`, `Mountain.YouCtrl`, `Permanent.Black+YouCtrl`, `Permanent.Blue+YouCtrl`, `Permanent.EnchantedBy+greatestPower`, `Permanent.EnchantedBy+tapped`, `Permanent.faceDown+YouCtrl`, `Permanent.Green+YouCtrl`, `Permanent.Snow+YouCtrl+Other`, `Permanent.Zombie+Other+YouCtrl`, `Plains.YouCtrl`, `Planeswalker.Vraska+YouCtrl`, `Planet.YouCtrl`, `Spirit.Other+YouCtrl`, `Swamp.YouCtrl`, `Wizard.Other+YouCtrl`
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
  Observed values: `Ally.Other+YouCtrl`, `Ally.YouCtrl+Other`, `Angel.Other+YouCtrl`, `Angel.YouCtrl`, `Artifact`, `Artifact,Creature,Enchantment`, `Artifact.!token+Other+YouCtrl`, `Artifact.!token+YouCtrl`, `Artifact.!token+YouCtrl+Other,Card.Self`, `Artifact.Creature+Other,Card.Self`, `Artifact.OppCtrl`, `Artifact.OppOwn`, `Artifact.Other`, `Artifact.Other+!token+YouCtrl`, `Artifact.Other+YouCtrl`, `Artifact.Other+YouCtrl,Creature.Other+YouCtrl`, `Artifact.YouCtrl`, `Artifact.YouCtrl+!token`, `Artifact.YouCtrl+cmcGE3+Other`, `Artifact.YouCtrl+HasCounters`, `Artifact.YouCtrl+IsRemembered`, `Artifact.YouCtrl+Other`, `Artifact.YouCtrl+Other,Creature.YouCtrl+Other`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouCtrl,Enchantment.YouCtrl`, `Artifact.YouCtrl,Permanent.Artificer+YouCtrl`, `Artifact.YouOwn`, `Artifact.YouOwn+!token`, `Attraction.YouCtrl`, `Aura.YouCtrl`, `Aura.YouCtrl+wasCastByYou`, `Aura.YouCtrl+YouOwn`, `Aura.YouCtrl,Equipment.YouCtrl`, `Bear.YouCtrl+Other`, `Beast`, `Beast.YouCtrl`, `Bird.Other+!token+YouCtrl`, `Bird.YouOwn`, `Card`, `Card.!token`, `Card.!token+Land`, `Card.!token+nonBlack`, `Card.!token+OppOwn`, `Card.!token+Other`, `Card.!token+YouOwn`, `Card.!token+YouOwn+Other`, `Card.!wasCastFromYourHandByYou+Self`, `Card.ActivePlayerCtrl+!token`, `Card.AttachedBy`, `Card.AttachedBy+Historic`, `Card.AttachedBy+Human`, `Card.Black+!token+OppOwn`, `Card.ChosenCard`, `Card.ChosenCard,Card.IsRemembered`, `Card.ChosenCardStrict`, `Card.Creature`, `Card.Creature+!token+YouOwn`, `Card.Creature+Other+YouOwn`, `Card.EffectSource`, `Card.EnchantedBy`, `Card.EnchantedBy+Horror`, `Card.Equipment+YouCtrl`, `Card.EquippedBy`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.IsImprinted+ExiledWithSource`, `Card.IsImprinted+ExiledWithSourceLKI`, `Card.IsImprinted,Card.IsRemembered`, `Card.IsRemembered`, `Card.IsRemembered+ExiledWithSource`, `Card.IsUnearthed`, `Card.Knight+YouCtrl`, `Card.Land+YouOwn`, `Card.Legendary+Other+YouCtrl`, `Card.NamedCard+YouCtrl`, `Card.Ninja+YouCtrl`, `Card.nonLand+YouOwn`, `Card.OppCtrl+IsCommander`, `Card.OppOwn`, `Card.Other+Human`, `Card.Outlaw+YouCtrl`, `Card.Self`, `Card.Self+!blocking`, `Card.Self+!HasCounters`, `Card.Self+!token`, `Card.Self+AttachedTo Card`, `Card.Self+attacking`, `Card.Self+bargained`, `Card.Self+counters_EQ0_DEATH`, `Card.Self+counters_EQ0_OIL`, `Card.Self+counters_EQ0_TIME`, `Card.Self+counters_GE1_DEATH`, `Card.Self+counters_GE1_M1M1`, `Card.Self+counters_GE1_P1P1`, `Card.Self+counters_GE1_P1P1,Creature.Other+YouCtrl+counters_GE1_P1P1`, `Card.Self+counters_GE1_REVIVAL`, `Card.Self+counters_GE2_P1P1`, `Card.Self+Creature`, `Card.Self+Creature+nonLand`, `Card.Self+dealtCombatDamageThisTurn Player`, `Card.Self+enchanted`, `Card.Self+equipped`, `Card.Self+gotBlockedThisTurn`, `Card.Self+HasCounters`, `Card.Self+HasCounters,Creature.Other+YouCtrl+HasCounters`, `Card.Self+kicked`, `Card.Self+kicked 1`, `Card.Self+kicked 2`, `Card.Self+madness`, `Card.Self+nonAura`, `Card.Self+nonDemon`, `Card.Self+nonSpirit`, `Card.Self+NotedGuessPhantasm`, `Card.Self+powerGE3`, `Card.Self+powerGE4`, `Card.Self+PromisedGift`, `Card.Self+prowled`, `Card.Self+sneaked`, `Card.Self+spectacle`, `Card.Self+surged`, `Card.Self+untapped`, `Card.Self+wasCast`, `Card.Self+wasCast+webSlinged`, `Card.Self+wasCastByYou`, `Card.Self+wasCastFromYourGraveyard`, `Card.Self+wasCastFromYourGraveyardByYou`, `Card.Self+wasCastFromYourGraveyardByYou,Creature.YouCtrl+wasCastFromYourGraveyardByYou`, `Card.Self+YouOwn`, `Card.Self+YouOwn,Creature.YouOwn+Other`, `Card.Self,Aetherborn.Other+YouCtrl`, `Card.Self,Ally.Other+YouCtrl`, `Card.Self,Artifact.Other`, `Card.Self,Artifact.Other+DoubleFaced+YouCtrl`, `Card.Self,Artifact.Other+YouCtrl`, `Card.Self,Artifact.YouCtrl+cmcGE3`, `Card.Self,Artifact.YouCtrl+Other`, `Card.Self,Artifact.YouCtrl+Other+!token`, `Card.Self,Bird.Other+YouCtrl`, `Card.Self,Card.Equipment+Other+YouCtrl`, `Card.Self,Card.namedVerdant Dread`, `Card.Self,Card.Sphinx+Other+YouCtrl`, `Card.Self,Cat.!token+Other+YouCtrl`, `Card.Self,Cat.Other+YouCtrl`, `Card.Self,Cleric.YouCtrl+Other`, `Card.Self,Creature.!token+Other+YouCtrl`, `Card.Self,Creature.!token+powerLE2+YouCtrl`, `Card.Self,Creature.!token+YouCtrl`, `Card.Self,Creature.Artifact+YouCtrl+Other`, `Card.Self,Creature.Black+Other+YouCtrl`, `Card.Self,Creature.Colorless+YouCtrl`, `Card.Self,Creature.Human+Other+YouCtrl`, `Card.Self,Creature.Legendary+YouCtrl`, `Card.Self,Creature.Legendary+YouCtrl+Other`, `Card.Self,Creature.Lhurgoyf+YouCtrl`, `Card.Self,Creature.nonHuman+Other+YouCtrl`, `Card.Self,Creature.Other`, `Card.Self,Creature.Other+!token+YouCtrl`, `Card.Self,Creature.Other+Ally+YouCtrl`, `Card.Self,Creature.Other+Cat+YouCtrl`, `Card.Self,Creature.Other+cmcGE4+YouCtrl`, `Card.Self,Creature.Other+Legendary+YouCtrl`, `Card.Self,Creature.Other+powerGE4+YouCtrl`, `Card.Self,Creature.Other+powerGE5+YouCtrl`, `Card.Self,Creature.Other+powerLTtoughness+YouCtrl`, `Card.Self,Creature.Other+YouCtrl`, `Card.Self,Creature.Other+YouCtrl+withFlash,Creature.Other+YouCtrl+withHaste`, `Card.Self,Creature.Other+YouCtrl+withFlying`, `Card.Self,Creature.Other+YouCtrl,Artifact.Other+YouCtrl`, `Card.Self,Creature.powerGE4+Other`, `Card.Self,Creature.powerGE4+Other+YouCtrl`, `Card.Self,Creature.powerLE3+YouCtrl+Other`, `Card.Self,Creature.YouCtrl`, `Card.Self,Creature.YouCtrl+Other`, `Card.Self,Creature.YouCtrl+Other+Human`, `Card.Self,Creature.YouOwn+Other`, `Card.Self,Dinosaur.withFlying+Other+YouCtrl`, `Card.Self,Dinosaur.YouCtrl+Other`, `Card.Self,Dragon.Other+YouCtrl`, `Card.Self,Dragon.YouCtrl`, `Card.Self,Dwarf.Other+YouCtrl,Equipment.YouCtrl`, `Card.Self,Elemental.Other+YouCtrl`, `Card.Self,Elf.Other+YouCtrl`, `Card.Self,Elf.Other+YouCtrl,Faerie.Other+YouCtrl`, `Card.Self,Enchantment.!token+Other+YouCtrl`, `Card.Self,Enchantment.Other+YouCtrl`, `Card.Self,Enchantment.YouCtrl`, `Card.Self,Enchantment.YouCtrl+Other`, `Card.Self,Goblin.Other`, `Card.Self,Goblin.Other+YouCtrl`, `Card.Self,Hero.Other+YouCtrl`, `Card.Self,Human.Other+YouCtrl`, `Card.Self,Hydra.Other+!token+YouCtrl`, `Card.Self,Kavu.Other+YouCtrl`, `Card.Self,Kithkin.YouCtrl+Other`, `Card.Self,Land.Other+YouCtrl`, `Card.Self,Lizard.Other+YouCtrl`, `Card.Self,Minotaur.!token+Other+YouCtrl`, `Card.Self,Mutant.Other+YouCtrl`, `Card.Self,Nightmare.Other+YouCtrl,Horror.Other+YouCtrl`, `Card.Self,Permanent.!token+Historic+Other+YouCtrl`, `Card.Self,Permanent.nonLand+YouCtrl+Other`, `Card.Self,Permanent.Snow+Other+YouCtrl`, `Card.Self,Phyrexian.!token+YouCtrl`, `Card.Self,Phyrexian.Other+YouCtrl`, `Card.Self,Pirate.Other+YouCtrl`, `Card.Self,Rabbit.Other+YouCtrl`, `Card.Self,Rat.Other+YouCtrl`, `Card.Self,Rogue.Other+YouCtrl`, `Card.Self,Shrine.!token+Other+YouCtrl`, `Card.Self,Spirit.Other+!token+YouCtrl`, `Card.Self,Spirit.YouCtrl+Other`, `Card.Self,Treefolk.Other+YouCtrl`, `Card.Self,Vampire.Other+!token+YouCtrl`, `Card.Self,Vampire.Other+YouCtrl`, `Card.Self,Warrior.Other+YouCtrl`, `Card.Self,Warrior.Other+YourTeamCtrl`, `Card.Self,Wolf.Other+YouCtrl,Werewolf.Other+YouCtrl`, `Card.Self,Zombie.!token+Other+YouCtrl,Mutant.!token+Other+YouCtrl`, `Card.Self,Zombie.Other`, `Card.Self,Zombie.Other+YouCtrl`, `Card.Snake+!token+YouCtrl`, `Card.Spirit+Other+YouCtrl`, `Card.token`, `Card.token+YouCtrl`, `Card.wasCast+Self`, `Card.wasCastByYou+Self`, `Card.wasCastFromYourHandByYou+Self`, `Card.YouCtrl+counters_GE1_P1P1`, `Card.YouDontOwn`, `Card.YouOwn`, `Card.Zombie+YouCtrl`, `Cartouche.YouCtrl`, `Cave.YouCtrl`, `Cleric.Other+YouCtrl`, `Cleric.Other+YouCtrl,Angel.Other+YouCtrl`, `Cleric.Other,Card.Self`, `Clue.YouCtrl`, `Creature`, `Creature.!IsRemembered`, `Creature.!token`, `Creature.!token+ChosenType+YouCtrl`, `Creature.!token+nonAngel+YouCtrl`, `Creature.!token+OppCtrl`, `Creature.!token+OppOwn`, `Creature.!token+Other`, `Creature.!token+Other+YouCtrl`, `Creature.!token+YouCtrl`, `Creature.!token+YouCtrl+!wasCastFromYourHandByYou`, `Creature.!token+YouCtrl+counters_GE1_P1P1`, `Creature.!token+YouCtrl+doesNotShareNameWith YourGraveyard+doesNotShareNameWith OtherYourBattlefield`, `Creature.!token+YouCtrl+Other`, `Creature.!token+YouOwn`, `Creature.Artifact+!token+YouCtrl`, `Creature.Artifact+YouCtrl+Other+!token,Vehicle.YouCtrl+Other+!token`, `Creature.attacking`, `Creature.attacking+IsGoaded,Creature.blocking+IsGoaded`, `Creature.attacking+YouCtrl`, `Creature.attacking+YouCtrl,Creature.blocking+OppCtrl`, `Creature.Black+Other+YouCtrl`, `Creature.Black+YouCtrl`, `Creature.blockingSource`, `Creature.Blue+YouCtrl`, `Creature.Blue+YouCtrl+Other`, `Creature.ChosenType`, `Creature.ChosenType+YouCtrl`, `Creature.cmcGE6`, `Creature.counters_GE1_BOUNTY`, `Creature.counters_GE1_COIN`, `Creature.counters_GE1_FUNGUS`, `Creature.counters_GE1_INFECTION`, `Creature.counters_GE1_M1M1`, `Creature.DamagedBy`, `Creature.DamagedBy Equipped`, `Creature.DamagedBy RememberedLKI`, `Creature.enchanted`, `Creature.EnchantedBy`, `Creature.EnchantedBy Aura.YouCtrl`, `Creature.EnchantedBy,Creature.YouCtrl+modified+!EnchantedBy`, `Creature.EnchantedPlayerCtr+!token`, `Creature.EnchantedPlayerCtrl`, `Creature.equalPT+YouCtrl`, `Creature.equipped+YouCtrl+Other`, `Creature.EquippedBy`, `Creature.EquippedBy,Creature.Self`, `Creature.faceDown+YouCtrl`, `Creature.Goblin+YouCtrl`, `Creature.Green`, `Creature.Green+!token`, `Creature.Green+YouCtrl`, `Creature.Human+YouCtrl+Other,Card.Self`, `Creature.IsImprinted`, `Creature.IsRemembered`, `Creature.IsRemembered+YouOwn`, `Creature.Kithkin+YouOwn+attacking,Creature.Elf+YouOwn+attacking`, `Creature.Legendary+HasCounters`, `Creature.Legendary+OppCtrl`, `Creature.Legendary+Other+YouCtrl`, `Creature.Legendary+Other+YouCtrl,Creature.cmcEQ1+Other+YouCtrl`, `Creature.Legendary+YouCtrl`, `Creature.Legendary+YouCtrl+cmcGE4`, `Creature.modified+YouCtrl`, `Creature.MultiColor+Other+YouCtrl`, `Creature.nonAngel+YouCtrl`, `Creature.nonArtifact+Other`, `Creature.nonBlack`, `Creature.nonHuman+Other+YouCtrl`, `Creature.nonLand+YouCtrl`, `Creature.nonSpirit+YouCtrl+Other`, `Creature.nonWhite`, `Creature.OppCtrl`, `Creature.OppCtrl+!token`, `Creature.OppCtrl+counters_GE1_BOUNTY`, `Creature.OppCtrl+counters_GE1_M1M1`, `Creature.OppCtrl+HasCounters`, `Creature.OppCtrl+IsSuspected`, `Creature.OppCtrl+NotedType`, `Creature.OppCtrl+toughnessLT1`, `Creature.OppCtrl+untapped,Artifact.OppCtrl+untapped`, `Creature.OppOwn`, `Creature.Other`, `Creature.Other+!token+!wasCast+YouCtrl`, `Creature.Other+!token+enchanted+YouCtrl,Creature.Other+!token+equipped+YouCtrl`, `Creature.Other+!token+YouCtrl`, `Creature.Other+!token+YouCtrl,Card.Self`, `Creature.Other+!wasCast+YouCtrl`, `Creature.Other+attackingAlone,Creature.Other+blockingAlone`, `Creature.Other+ChosenType+YouCtrl`, `Creature.Other+Colorless+YouCtrl`, `Creature.Other+DamagedBySpider.YouCtrl`, `Creature.Other+enchanted+YouCtrl,Creature.Other+equipped+YouCtrl,Card.Self+equipped,Card.Self+enchanted`, `Creature.Other+modified+YouCtrl`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl+!token+cmcGE1`, `Creature.Other+YouCtrl+basePowerEQ1`, `Creature.Other+YouCtrl+Black`, `Creature.Other+YouCtrl+Green`, `Creature.Other+YouCtrl+HasCounters`, `Creature.Other+YouCtrl+Red`, `Creature.Other+YouCtrl+withFlying`, `Creature.Other+YouCtrl,Artifact.Other+YouCtrl`, `Creature.Other+YouCtrl,Card.Self`, `Creature.Other+YouCtrl,Land.YouCtrl`, `Creature.Other+YouCtrl,Planeswalker.YouCtrl`, `Creature.Other+YouCtrl,Planeswalker.YouCtrl+Other,Card.Self`, `Creature.Other,Artifact.Other`, `Creature.Other,Card.Self`, `Creature.powerEQ1+toughnessEQ1+YouCtrl`, `Creature.powerGE3+Other+YouCtrl`, `Creature.powerGE3+YouCtrl`, `Creature.powerGE4`, `Creature.powerGE4+Other+YouCtrl`, `Creature.powerGE4+YouCtrl`, `Creature.powerGE4+YouCtrl+!token`, `Creature.powerGE5+Other+YouCtrl`, `Creature.powerGE5+YouCtrl`, `Creature.powerGTX`, `Creature.powerLE1+YouOwn`, `Creature.powerLE2+Other+YouCtrl`, `Creature.powerLE2+YouCtrl`, `Creature.powerLE2+YouCtrl+Other`, `Creature.Rogue`, `Creature.Self`, `Creature.Shaman`, `Creature.Soldier`, `Creature.token`, `Creature.token+YouCtrl`, `Creature.toughnessGE4+YouOwn`, `Creature.Warrior`, `Creature.wasCast`, `Creature.wasCastByYou+YouCtrl`, `Creature.wasCastByYou+YouCtrl+Other`, `Creature.wasCastFromYourHandByYou+YouCtrl`, `Creature.White`, `Creature.White+YouCtrl+Other`, `Creature.withDefender+YouCtrl`, `Creature.withDefender+YouCtrl+Other`, `Creature.withFlying`, `Creature.withFlying+DamagedBy`, `Creature.withFlying+Other+YouCtrl`, `Creature.withShadow`, `Creature.Wizard`, `Creature.YouCtrl`, `Creature.YouCtrl+!token`, `Creature.YouCtrl+!token+counters_GE1_OIL`, `Creature.YouCtrl+!token+counters_GE1_P1P1`, `Creature.YouCtrl+!token+HasCounters`, `Creature.YouCtrl+!token+Other`, `Creature.YouCtrl+!token,Card.Self`, `Creature.YouCtrl+attacking`, `Creature.YouCtrl+cmcGE5`, `Creature.YouCtrl+cmcGTX`, `Creature.YouCtrl+counters_GE1_IMPOSTOR`, `Creature.YouCtrl+counters_GE1_OIL`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+IsRemembered`, `Creature.YouCtrl+IsUnearthed`, `Creature.YouCtrl+Legendary`, `Creature.YouCtrl+modified`, `Creature.YouCtrl+modified+!token`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other+counters_GE1_P1P1`, `Creature.YouCtrl+Other+namedGladewalker Ritualist`, `Creature.YouCtrl+Other+wasCastFromGraveyardByYou,Card.Self+wasCastFromGraveyardByYou`, `Creature.YouCtrl+Other+withFlying`, `Creature.YouCtrl+Other,Artifact.YouCtrl+Other`, `Creature.YouCtrl+Other,Card.Self`, `Creature.YouCtrl+Other,Vehicle.YouCtrl+Other`, `Creature.YouCtrl+powerGTX+Other`, `Creature.YouCtrl+powerLE1,Creature.YouCtrl+toughnessLE1`, `Creature.YouCtrl+sharesCreatureTypeWith`, `Creature.YouCtrl+toughnessGE4`, `Creature.YouCtrl+withDefender`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withoutFlying`, `Creature.YouCtrl+YouOwn`, `Creature.YouCtrl,Enchantment.YouCtrl`, `Creature.YouCtrl,Planeswalker.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl+counters_GE1_SLIME`, `Creature.YouDontOwn+YouCtrl`, `Creature.YouOwn`, `Creature.YouOwn+Other`, `Creature.YouOwn+YouCtrl+Other+wasCastFromGraveyard`, `Curse.YouOwn`, `Demon.YouCtrl`, `Demon.YouCtrl+Other`, `Desert.!token+YouOwn`, `Desert.YouCtrl`, `Desert.YouOwn`, `Detective.YouCtrl`, `Detective.YouCtrl+Other`, `Detective.YouCtrl+Other,Card.Self`, `Dinosaur.YouCtrl`, `Dinosaur.YouCtrl+Other`, `Djinn,Efreet`, `Dragon`, `Dragon.YouCtrl`, `Dragon.YouCtrl+!token+Other`, `Egg.YouCtrl`, `Eldrazi.Other+YouCtrl`, `Elemental.Other+YouCtrl`, `Elemental.YouCtrl`, `Elf.!token+Other`, `Elf.!token+Other+YouCtrl,Berserker.!token+Other+YouCtrl`, `Elf.!token+Other+YouOwn`, `Elf.Other`, `Elf.Other+YouCtrl`, `Elf.Other+YouCtrl,Berserker.Other+YouCtrl`, `Elf.YouCtrl`, `Employee.YouCtrl`, `Enchantment`, `Enchantment.Other+YouCtrl`, `Enchantment.YouCtrl`, `Equipment.YouCtrl`, `Equipment.YouCtrl+!token+Other`, `Equipment.YouCtrl,Aura.YouCtrl`, `Faerie.Other+YouCtrl`, `Food`, `Forest`, `Forest.YouCtrl`, `Forest.YouCtrl,Swamp.YouCtrl`, `Frog.Other+YouCtrl,Rabbit.Other+YouCtrl,Raccoon.Other+YouCtrl,Squirrel.Other+YouCtrl`, `Gate.YouCtrl`, `Goblin.Other+YouCtrl`, `Goblin.Other,Card.Self`, `Goblin.YouCtrl`, `God`, `Hamster.YouCtrl,Mouse.YouCtrl,Rat.YouCtrl,Squirrel.YouCtrl`, `Hero.Other+YouCtrl`, `Human.Other+!token+YouCtrl`, `Human.Other+YouCtrl`, `Human.YouCtrl`, `Illusion.YouCtrl`, `Insect.YouCtrl+Other`, `Instant.YouOwn,Sorcery.YouOwn`, `Island,Card.Blue`, `Island.YouCtrl`, `Island.YouCtrl,Swamp.YouCtrl`, `Kavu.Other`, `Kithkin.YouOwn`, `Knight.!token+YouCtrl`, `Knight.Other+YouCtrl`, `Land`, `Land.!token+YouCtrl`, `Land.!token+YouOwn`, `Land.EnchantedPlayerCtrl`, `Land.nonBasic`, `Land.nonBasic+OppCtrl`, `Land.OppCtrl`, `Land.OppCtrl+ControllerControlsMoreLand`, `Land.sharesNameWith Imprinted+OppCtrl`, `Land.tapped+YouCtrl`, `Land.YouCtrl`, `Land.YouCtrl+YouDontOwn`, `Land.YouOwn`, `Merfolk.Other+YouCtrl`, `Merfolk.YouCtrl+Other`, `Mount.YouCtrl`, `Mountain.YouCtrl`, `Mutant.YouCtrl`, `Mutant.YouCtrl,Ninja.YouCtrl,Turtle.YouCtrl`, `Ninja.YouCtrl`, `Permanent`, `Permanent.!token`, `Permanent.!token+Legendary+Other+YouCtrl`, `Permanent.!token+YouOwn`, `Permanent.Artificer+YouCtrl`, `Permanent.ChosenType+YouCtrl`, `Permanent.faceDown+YouCtrl`, `Permanent.Legendary+Other`, `Permanent.Lhurgoyf+YouOwn`, `Permanent.Merfolk+YouCtrl+Other`, `Permanent.nonBasic`, `Permanent.nonCreature`, `Permanent.OppCtrl`, `Permanent.OppCtrl+counters_GE1_BOUNTY`, `Permanent.OppOwn+YouCtrl+nonLand`, `Permanent.Other`, `Permanent.Other+YouCtrl+Snow`, `Permanent.Outlaw+YouCtrl+Other`, `Permanent.Snow+Other+YouCtrl`, `Permanent.tapped+YouCtrl`, `Permanent.token+YouCtrl`, `Permanent.Transformed+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+ChosenType`, `Permanent.YouCtrl+HasCounters`, `Permanent.YouCtrl+nonArtifact`, `Permanent.YouCtrl+Other`, `Permanent.YouCtrl+Other+!token`, `Permanent.YouCtrl+Other+HasCounters`, `Permanent.YouOwn`, `Phoenix.Other+YouCtrl`, `Phyrexian.YouCtrl`, `Pirate.Other+YouCtrl`, `Plains.YouCtrl`, `Planeswalker.YouCtrl`, `Rat`, `Rat.Other+YouCtrl`, `Samurai.YouCtrl`, `Saproling.YouCtrl`, `Scarecrow.Other+YouCtrl`, `Shrine.Other+YouCtrl`, `Sliver.!token+YouCtrl`, `Soldier.Other+!token+YouCtrl`, `Spider.YouCtrl`, `Spirit.!token+Other+YouCtrl`, `Spirit.Other+YouCtrl`, `Spirit.YouCtrl`, `Spirit.YouOwn,Card.YouOwn+withDisturb`, `Squirrel.Other+YouCtrl,Food.Other+YouCtrl`, `Swamp`, `Swamp,Card.Black`, `Swamp.YouCtrl`, `Tentacle.YouCtrl`, `Treefolk.YouCtrl+Other`, `Vampire.Other+!token+YouCtrl`, `Vampire.Other+YouCtrl`, `Vampire.Other+YouCtrl,Card.Self`, `Vampire.YouCtrl`, `Vehicle.YouCtrl`, `Villain.Other+YouCtrl`, `Villain.YouCtrl`, `Warrior.Other+YourTeamCtrl`, `Werewolf.YouCtrl`, `Wizard.YouCtrl+!token+Other`, `Wolf.YouCtrl`, `Zombie.!token+YouCtrl`, `Zombie.!token+YouCtrl+Other,Card.Self`, `Zombie.OppCtrl`, `Zombie.Other+YouCtrl`, `Zombie.Other+YouCtrl+withoutDecayed`, `Zombie.YouCtrl`, `Zombie.YouCtrl+Other`, `Zombie.YouCtrl+powerNOTbasePower,Mutant.YouCtrl+powerNOTbasePower`
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
  Observed values: `DBDraw`, `DBMakeCard`, `ExileSelf`, `LoseGain`, `TrigChangeZone`, `TrigChangeZoneAll`, `TrigCharm`, `TrigChoose`, `TrigConjure`, `TrigConvert`, `TrigCopy`, `TrigCounter`, `TrigDamage`, `TrigDealDamage`, `TrigDrain`, `TrigDraw`, `TrigEffect`, `TrigExile`, `TrigExperience`, `TrigExplore`, `TrigGainLife`, `TrigInvestigate`, `TrigLoseLife`, `TrigMill`, `TrigPrepare`, `TrigPump`, `TrigPutCounter`, `TrigPutCounters`, `TrigRemoveCounter`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSurveil`, `TrigToken`, `TrigTreasure`, `TrigUntapAll`, `TrigVenture`
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
  Observed values: `Artifact.YouCtrl`, `Artifact.YouCtrl+!token`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouOwn`, `Artifact.YouOwn,Creature.YouOwn`, `Card.!token`, `Card.!token+!copiedSpell`, `Card.OppOwn+!token+nonCopiedSpell`, `Card.Other+!token+!copiedSpell`, `Card.token+OppCtrl`, `Card.token+YouCtrl`, `Card.YouOwn`, `Cat.Other+YouCtrl`, `Creature`, `Creature.!token`, `Creature.!token+wasCastFromExile,Creature.!token+ThisTurnEnteredFrom_Exile`, `Creature.!token+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.attacking+Legendary+Other+YouCtrl`, `Creature.attacking+YouCtrl`, `Creature.basePowerEQ1+baseToughnessEQ1+Other+YouCtrl`, `Creature.cmcLE3+YouCtrl`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl+wasCastFromGraveyard,Creature.Other+YouCtrl+ThisTurnEnteredFrom_Graveyard`, `Creature.Other+YouCtrl,Artifact.Other+YouCtrl`, `Creature.powerLE2+YouCtrl+Other`, `Creature.YouCtrl`, `Creature.YouCtrl+!token+!wasCast,Creature.YouCtrl+!token+CastSa Spell.ManaSpent EQ0`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+ThisTurnEnteredFrom_Graveyard,Creature.YouCtrl+wasCastFromGraveyard`, `Creature.YouOwn`, `Creature.YouOwn+!token`, `Creature.YouOwn,Artifact.YouOwn`, `Elf.Other+YouCtrl`, `Enchantment.YouCtrl`, `Human.YouCtrl,Warrior.YouCtrl`, `Land.OppCtrl`, `Land.YouCtrl+!token`, `Land.YouOwn`, `Land.YouOwn+!token`, `Merfolk.YouCtrl`, `Permanent.nonCreature+nonLand+YouCtrl`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouOwn+!token`, `Rabbit.Other+YouCtrl,Bat.Other+YouCtrl,Bird.Other+YouCtrl,Mouse.Other+YouCtrl`, `Vampire.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `LandAbility`, `SpellAbility.YouCtrl`

## `ChaosEnsues`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBFetch`, `DBPutCounter`, `PanopticonDraw`, `RolledChaos`, `TrigAnimateAll`, `TrigChooseColor`, `TrigDamage`, `TrigDamageAll`, `TrigDetain`, `TrigDigUntil`, `TrigDiscard`, `TrigEffect`, `TrigEndTurn`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigReanimate`, `TrigRedistribute`, `TrigRepeat`, `TrigReturn`, `TrigReturnOneEach`, `TrigReverseOrder`, `TrigSetState`, `TrigSteal`, `TrigSwitch`, `TrigTimeTravel`, `TrigToken`, `TrigTreasure`, `TrigVote`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`

## `ClaimPrize`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBDestroy`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Attraction.YouCtrl`

## `Clashed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDraw`, `TrigTapL`, `TrigTapW`, `TrigTokenL`, `TrigTokenW`
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
  Observed values: `TrigAnimateLand`, `TrigBounce`, `TrigChangeZone`, `TrigCopy`, `TrigDig`, `TrigDigUntil`, `TrigDraw`, `TrigReanimate`
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
  Observed values: `TrigInvestigate`, `TrigToken`
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
  Observed values: `TrigChange`, `TrigDig`, `TrigExile`, `TrigLoot`, `TrigLoseLife`, `TrigMill`, `TrigProliferate`, `TrigPump`, `TrigPutCounter`, `TrigReturn`, `TrigSurveil`, `TrigToken`, `TrigUntap`
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
  Observed values: `TrigPump`, `TrigPutCounter`
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
  Observed values: `ABDealDamage`, `ABDraw`, `ABMana`, `ABMana & ABToken`, `ABPump`, `AddMana`, `AnimateIsland`, `ArlinnDealDamage`, `BlackTap`, `ColorlessMana`, `Mana`, `TreasureSac`
- `AddColor$`: TODO: Describe this parameter.
  Observed values: `Black`
- `AddHiddenKeyword$`: TODO: Describe this parameter.
  Observed values: `CARDNAME can't attack or block.`, `CARDNAME can't block.`, `This card doesn't untap during your next untap step.`
- `AddKeyword$`: TODO: Describe this parameter.
  Observed values: `Affinity:Artifact`, `CantSearchLibrary`, `CARDNAME can't block.`, `Cascade`, `Convoke`, `Deathtouch`, `Deathtouch & Haste`, `Double Strike`, `Double Strike & Haste`, `Double Strike & Trample & Hexproof & Haste`, `Enchant:Creature.YouCtrl:creature you control`, `Enchant:Forest.YouCtrl:Forest you control`, `First Strike`, `Flying`, `Haste`, `Hexproof`, `Hexproof & Indestructible`, `Hexproof & Reach`, `Improvise`, `Indestructible`, `Lifelink`, `Menace`, `Piracy`, `Prevent all combat damage that would be dealt by CARDNAME.`, `Prevent all damage that would be dealt by CARDNAME.`, `Reach & Trample & Ward:2`, `Retrace`, `Shaman's Trance`, `Sneak:3 B`, `Storm`, `Trample`, `Trample & Haste`, `Undaunted`, `UntapAdjust:Permanent:2`, `Vigilance`, `Vigilance & Hexproof`, `Vigilance & Trample & Indestructible`, `Ward:1`
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
  Observed values: `BecomesTapped`, `DamageTrig`, `DealsCDTrig`, `ETB`, `MannequinBecomesTarget`, `MathasDeath`, `ObsidianBlazeTrig`
- `AddType$`: TODO: Describe this parameter.
  Observed values: `AllBasicLandType`, `Angel`, `Angel & Warrior`, `Artifact`, `Artifact & Creature & Robot`, `Artifact & Treasure`, `Aura & Enchantment`, `ChosenType2`, `Creature`, `Creature & Elemental`, `Creature & Spirit`, `Demon`, `Enchantment`, `Enchantment & Aura`, `Hero`, `Island`, `Land`, `Mutant`, `Nightmare`, `Phyrexian`, `Skeleton`, `Spirit`, `Spirit & Detective`, `Swamp`, `Vampire`, `Warlock`, `Wraith`, `Zombie`
- `AdjustLandPlays$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `Z`
- `Affected$`: TODO: Describe this parameter.
  Observed values: `Artifact.nonCreature`, `Artifact.RememberedPlayerCtrl,Creature.RememberedPlayerCtrl`, `Artifact.YouCtrl`, `Artifact.YouCtrl+IsRemembered`, `Artifact.YouCtrl+Other`, `Artifact.YouCtrl,Creature.YouCtrl,Enchantment.YouCtrl,Land.YouCtrl`, `Battle.YouCtrl+IsRemembered`, `Card.CastSa Spell.MayPlaySource`, `Card.ChosenCard`, `Card.ChosenType`, `Card.counters_GE1_DISCOVERY`, `Card.Creature+IsRemembered+nonLand`, `Card.Creature+YouCtrl`, `Card.EffectSource`, `Card.EnchantedBy`, `Card.ExiledWithEffectSource`, `Card.ExiledWithEffectSource+nonLand`, `Card.ExiledWithEffectSource+YouOwn`, `Card.ExiledWithSource`, `Card.foretold+YouOwn+nonLand`, `Card.Instant+IsRemembered,Card.Sorcery+IsRemembered`, `Card.Instant+YouCtrl`, `Card.Instant,Card.Sorcery`, `Card.IsImprinted`, `Card.IsImprinted+IsRemembered`, `Card.IsRemembered`, `Card.IsRemembered+!IsImprinted`, `Card.IsRemembered+Adventure`, `Card.IsRemembered+Artifact+nonLand`, `Card.IsRemembered+Creature`, `Card.IsRemembered+nonCreature+nonLand`, `Card.IsRemembered+nonLand`, `Card.IsRemembered+numColorsEQ3`, `Card.IsRemembered+Permanent+nonLand`, `Card.IsRemembered+Red+nonLand`, `Card.IsRemembered+YouOwn,Card.IsRemembered+cmcLTX`, `Card.nonCreature+YouCtrl`, `Card.nonLand+IsRemembered`, `Card.nonLand+YouOwn`, `Card.OppOwn`, `Card.Other+IsCommander+YouCtrl`, `Card.Permanent+YouOwn`, `Card.RememberedPlayerCtrl`, `Card.RememberedPlayerOwn`, `Card.Self`, `Card.Self+attacking`, `Card.Self+counters_GE1_DIVINITY`, `Card.Self+nonLand`, `Card.Self+untapped`, `Card.Sorcery+YouCtrl`, `Card.TopGraveyard+Instant+YouCtrl,Card.TopGraveyard+Sorcery+YouCtrl`, `Card.TopLibrary+RememberedPlayerCtrl`, `Card.TopLibrary+YouCtrl`, `Card.TopLibrary+YouCtrl+IsRemembered`, `Card.YouCtrl`, `Card.YouCtrl+nonLand`, `Card.YouCtrl+YouOwn+wasCastFromHand`, `Card.YouOwn`, `Card.YouOwn+faceUp`, `Card.YouOwn+IsRemembered`, `Creature`, `Creature.!IsRemembered+RememberedPlayerCtrl`, `Creature.cmcEQChosen`, `Creature.cmcEven`, `Creature.cmcOdd`, `Creature.Coward`, `Creature.EnchantedBy`, `Creature.EquippedBy`, `Creature.ExiledWithEffectSource+nonLand`, `Creature.faceDown+YouDontCtrl`, `Creature.Green,Creature.White`, `Creature.IsRemembered`, `Creature.Legendary+YouCtrl+Other+tapped`, `Creature.Merfolk+YouCtrl+Other`, `Creature.MonoColor`, `Creature.nonArtifact`, `Creature.nonGreen`, `Creature.nonLand+TopLibrary+YouCtrl`, `Creature.nonLand+YouCtrl`, `Creature.nonLand+YouOwn`, `Creature.nonRed`, `Creature.Other+YouCtrl`, `Creature.powerLE1`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.Red`, `Creature.Red,Creature.Green`, `Creature.RememberedPlayerCtrl`, `Creature.RememberedPlayerCtrl,Land.RememberedPlayerCtrl`, `Creature.sameName+Other`, `Creature.token+YouCtrl`, `Creature.withDefender`, `Creature.withoutFlying`, `Creature.withoutFlying+OppCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+ChosenType`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+IsRemembered`, `Creature.YouCtrl+Other`, `Creature.YouOwn`, `Enchantment.YouCtrl+IsRemembered`, `Equipment.IsRemembered`, `Instant.IsRemembered,Sorcery.IsRemembered`, `Instant.YouCtrl+IsRemembered`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouOwn,Sorcery.YouOwn`, `Island.YouCtrl`, `Kindred.YouCtrl+IsRemembered`, `Knight.YouCtrl`, `Land.ChosenType`, `Land.EnchantedBy`, `Land.IsRemembered`, `Land.Plains+Basic`, `Land.RememberedPlayerCtrl`, `Land.YouCtrl`, `Land.YouOwn`, `Mountain.YouCtrl`, `Ninja.YouCtrl`, `Permanent.IsRemembered`, `Permanent.nonLand+YouOwn`, `Permanent.YouCtrl+HasCounters`, `Planeswalker.Davriel+YouCtrl`, `Planeswalker.YouCtrl+IsRemembered`, `Player`, `Player.Opponent`, `Sorcery.YouCtrl+IsRemembered`, `Swamp.YouCtrl`, `Treasure.YouCtrl`, `You`, `Zombie.YouCtrl`
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
  Observed values: `DBDraw`, `FathomDraw`, `TrigChangeAll`, `TrigDraw`, `TrigPutCounter`, `TrigSac`, `TrigSeek`, `TrigToken`
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
  Observed values: `TrigDraw`, `TrigPutCounter`
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
  Observed values: `RemoveCounter`, `TrigChange`, `TrigChangeZone`, `TrigCharge`, `TrigConvert`, `TrigCreate`, `TrigDamage`, `TrigDealDamage`, `TrigDelayedTrigger`, `TrigDrain`, `TrigDraw`, `TrigGainLife`, `TrigInvestigate`, `TrigLoseLife`, `TrigMana`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigSearch`, `TrigSquirrel`, `TrigTap`, `TrigToken`
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
  Observed values: `Card.Self`, `Creature`, `Creature.inRealZoneBattlefield`, `Creature.nonHydra+Other+YouCtrl`, `Creature.Other+inZoneBattlefield+Colorless`, `Creature.Other+YouCtrl`, `Creature.Self`, `Creature.YouCtrl`, `Creature.YouCtrl+inZoneBattlefield`, `Permanent.Other+YouCtrl+inZoneBattlefield`, `Permanent.YouCtrl`, `Permanent.YouCtrl+inRealZoneBattlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `You`

## `Countered`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBDraw`, `TrackValidCounters`, `TrigLoot`, `TrigToken`
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
  Observed values: `DBDraw`, `TrigCounter`, `TrigDamage`, `TrigEffect`, `TrigPutCountersOther`, `TrigTap`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Card.Self+inRealZoneBattlefield`, `Creature.inRealZoneBattlefield`, `Creature.YouDontCtrl+inRealZoneBattlefield`, `Permanent.inRealZoneBattlefield,Player`
- `ValidObjectToSource$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl+inRealZoneBattlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `CounterRemoved`

TODO: Write documentation.

**Parameters:**
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `HONE`, `ORE`, `P1P1`, `TIME`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBCast`, `DBCastWithoutPayingManaCost`, `DBDamage`, `ProteanPutCounter`, `TrigDestroy`, `TrigDraw`, `TrigEffect`, `TrigLoseLife`, `TrigPut`, `TrigSurveil`, `TrigToken`
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
  Observed values: `TrigDmg`, `TrigSac`, `TrigScry`
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
  Observed values: `TrigAnimate`, `TrigDraw`, `TrigPutCounter`
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
  Observed values: `TrigCrank`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Crewed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigEffect`, `TrigPump`, `TrigSpeedway`
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
  Observed values: `DBEffect`, `DBGainLifeBis`, `TrigAnimate`, `TrigBounce`, `TrigCanNotBlock`, `TrigChangeZone`, `TrigClone`, `TrigCounter`, `TrigDamage`, `TrigDamageAll`, `TrigDealDamage2`, `TrigDestroy`, `TrigDestroyAll`, `TrigDiscard`, `TrigExile`, `TrigGainLife`, `TrigImmediateTrig`, `TrigLoseLife`, `TrigMill`, `TrigPrevent`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigReturn`, `TrigTap`, `TrigTapOrUntap`, `TrigToken`, `TrigToken2`, `TrigTreasure`, `TrigUntap`
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
  Observed values: `Card`, `Card.Other`, `Card.Other+YouOwn`, `Card.Self`, `Card.YouCtrl`, `Card.YouOwn`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `DamageAll`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigBranch`, `TrigDraw`, `TrigExileTop`, `TrigMonarch`, `TrigProliferate`, `TrigToken`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Creature.Warrior`, `Creature.YouCtrl`, `Creature.Zombie+YouCtrl`, `Pirate.YouCtrl+inZoneBattlefield`
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
  Observed values: `Eff`, `GainLife`, `GenjuTrigGain`, `KiyomaroGainLife`, `RollCounters`, `TrigBlood`, `TrigBounce`, `TrigCast`, `TrigChange`, `TrigChangeZone`, `TrigCharm`, `TrigDamage`, `TrigDestroy`, `TrigDrawCard`, `TrigExile`, `TrigGain`, `TrigGainLife`, `TrigInvestigate`, `TrigLoseLife`, `TrigManifest`, `TrigMill`, `TrigPutCounter`, `TrigRollDice`, `TrigSac`, `TrigSacLore`, `TrigToken`, `TrigTransform`, `TrigUntap`, `VigorousLife`, `VolverTrigGain`
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
  Observed values: `Card.AttachedBy`, `Card.nonCreature+YouCtrl`, `Card.RedSource+YouCtrl`, `Card.Self`, `Creature.EquippedBy`, `Creature.IsRemembered`, `Creature.YouCtrl`, `Instant.Red,Sorcery.Red,Creature.Red+inZoneBattlefield`, `Sliver.inZoneBattlefield`, `Spell.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.blocking`, `Player,Permanent`

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
  Observed values: `BalshanDig`, `CharismaticControl`, `CuriousObsessionDraw`, `Damage`, `DBChoosePermanent`, `DBCopy`, `DBCounter`, `DBDamage`, `DBDig`, `DBDraw`, `DBLose`, `DBLoseLife`, `DBScry`, `DBToken`, `DBTransform`, `DBVenture`, `DeathGift`, `DelTrig`, `DelTrigSimic`, `Eff`, `Eff1`, `Eff2`, `EmblemTrigChangeZone`, `ExileTwo`, `GamaDamage`, `HelmTrigDiscard`, `HelmTrigDraw`, `HunterProwessX`, `LoseGame`, `MangarasRetribution`, `MephidrossCounters`, `MoreDamage`, `NafsEffect`, `NoteDamaged`, `OpenIntoWonderDraw`, `PhageAvatarDestroy`, `PhageAvatarDestroy2`, `PoisonTarget`, `RemoveCounter`, `SakuraManaSingle`, `SixthSenseDraw`, `SnakeUmbraDraw`, `TalonPutCounter`, `TandemLookoutTrigDraw`, `TapTarget`, `TemperedCounters`, `ToHand`, `Traitor`, `TrigAddPhase`, `TrigAddTurn`, `TrigAmass`, `TrigAnimate`, `TrigAssemble`, `TrigBlink`, `TrigBoon`, `TrigBounce`, `TrigBranch`, `TrigCascade`, `TrigCast`, `TrigCastFromYard`, `TrigChange`, `TrigChangeZone`, `TrigCharm`, `TrigChoice`, `TrigChoose`, `TrigChooseCard`, `TrigChooseColor`, `TrigClearRem`, `TrigCloak`, `TrigConjure`, `TrigConnive`, `TrigControl`, `TrigConvert`, `TrigCopy`, `TrigCounter`, `TrigCounters`, `TrigDamage`, `TrigDamageAll`, `TrigDealDamage`, `TrigDealDamage1`, `TrigDealDamage2`, `TrigDelayedTrigger`, `TrigDelayTrig`, `TrigDelTrig`, `TrigDestroy`, `TrigDestroy19`, `TrigDestroyAll`, `TrigDestroyPlaneswalker`, `TrigDig`, `TrigDigUntil`, `TrigDiscard`, `TrigDiscardDraw`, `TrigDiscardOpp`, `TrigDiscover`, `TrigDmg`, `TrigDmgBlockers`, `TrigDouble`, `TrigDrain`, `TrigDraw`, `TrigDrawD`, `TrigDrawDiscard`, `TrigDrawN`, `TrigEffect`, `TrigEmblem`, `TrigEnergy`, `TrigExchange`, `TrigExchangeControl`, `TrigExile`, `TrigExplore`, `TrigFleshReaverDamage`, `TrigFlip`, `TrigFood`, `TrigGain`, `TrigGainControl`, `TrigGainLife`, `TrigGoad`, `TrigGuess`, `TrigHeist`, `TrigImmediateTrig`, `TrigImmediateTrigger`, `TrigImmTrigger`, `TrigIncrementCounters`, `TrigInvestigate`, `TrigLoop`, `TrigLoot`, `TrigLose`, `TrigLoseLife`, `TrigLoseLifeOpp`, `TrigLoyalty`, `TrigMill`, `TrigMonarch`, `TrigNameCard`, `TrigNekoTeLoseLife`, `TrigNekoTeTap`, `TrigNote`, `TrigOpenAttraction`, `TrigOppDiscard`, `TrigPayCost`, `TrigPeek`, `TrigPlay`, `TrigPoison`, `TrigPrepare`, `TrigProliferate`, `TrigPump`, `TrigPut`, `TrigPutCounter`, `TrigPutCounters`, `TrigRadiation`, `TrigRamp`, `TrigRandom`, `TrigReassemble`, `TrigRemember`, `TrigRememberPlayer`, `TrigRemove`, `TrigRemoveCounter`, `TrigReturn`, `TrigReveal`, `TrigRoll`, `TrigSac`, `TrigSac2`, `TrigSacOpp`, `TrigSacrifice`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSetLife`, `TrigSkipCombat`, `TrigSkipPhase`, `TrigSlug`, `TrigSpell`, `TrigSurveil`, `TrigSuspect`, `TrigTap`, `TrigTapOrUntap`, `TrigTempt`, `TrigTheyLose`, `TrigTimeTravel`, `TrigToken`, `TrigTokenFoodClue`, `TrigTransform`, `TrigTreasure`, `TrigTrig`, `TrigUnlock`, `TrigUntap`, `TrigUntapAll`, `TrigVenture`, `TrigVote`, `TrigZombie`, `VraskaGaze`, `WarriorLessonDraw`
- `Hellbent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_LT4_P1P1`, `Card.Self+IsMonstrous`, `Card.Self+ThisTurnEntered`, `Card.StrictlySelf`, `Card.untapped`, `Creature.Other+YouCtrl`, `Island.YouCtrl`, `Permanent.Blue+YouCtrl,Permanent.Red+YouCtrl`, `Swamp.YouCtrl`
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
  Observed values: `Archer.YouCtrl+inZoneBattlefield`, `Army.YouCtrl`, `Artifact.Creature+YouCtrl`, `Assassin.YouCtrl`, `Card,Emblem`, `Card.AttachedBy`, `Card.ChosenCardStrict`, `Card.ChosenColor`, `Card.EffectSource`, `Card.EnchantedBy`, `Card.EquippedBy`, `Card.Horror+YouCtrl`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.namedGollum; Obsessed Stalker`, `Card.OppCtrl,Emblem.OppCtrl`, `Card.Other+YouCtrl,Emblem.YouCtrl`, `Card.Self`, `Card.Self+!token,Creature.EquippedBy+!token`, `Card.Self+counters_EQ0_Indestructible`, `Card.Self,Creature.enchanted+YouCtrl`, `Card.Self,Creature.EnchantedBy`, `Card.Self,Creature.EquippedBy`, `Card.Self,Creature.Other+sameName`, `Card.Self,Spirit.Other+!token+YouCtrl`, `Card.Self,Tyranid.YouCtrl`, `Card.YouCtrl,Emblem.YouCtrl`, `Creature`, `Creature.!IsRemembered`, `Creature.!token+Artifact+YouCtrl`, `Creature.!token+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.AttachedBy`, `Creature.attacking`, `Creature.ChosenColor+inZoneBattlefield`, `Creature.EnchantedBy`, `Creature.EquippedBy`, `Creature.hadToAttackThisCombat`, `Creature.Historic+YouCtrl`, `Creature.inZoneBattlefield`, `Creature.IsCommander+YouCtrl`, `Creature.IsGoaded`, `Creature.IsRemembered`, `Creature.IsRenowned+YouCtrl`, `Creature.Legendary+YouCtrl`, `Creature.modified+YouCtrl`, `Creature.NamedCard`, `Creature.NamedCard+YouCtrl`, `Creature.Self`, `Creature.token+YouCtrl`, `Creature.Warrior+YouCtrl`, `Creature.withSkulk`, `Creature.YouCtrl`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+enchanted`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+EquippedByValid Equipment.Legendary`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+Land`, `Creature.YouCtrl+modified`, `Creature.YouCtrl+powerLE2`, `Creature.YouCtrl+ThisTurnEntered`, `Creature.YouCtrl+turnedFaceUpThisTurn`, `Creature.YouCtrl+withDeathtouch`, `Creature.YouCtrl+withDeathtouch+inZoneBattlefield`, `Creature.YouCtrl+withToxic`, `Dog.YouCtrl`, `Gamma.YouCtrl,Villain.YouCtrl`, `Goblin`, `Goblin.YouCtrl`, `Goblin.YouCtrl,Orc.YouCtrl`, `Goblin.YouCtrl,Rogue.YouCtrl`, `Griffin.YouCtrl`, `Human`, `Instant,Sorcery`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Knight.YouCtrl`, `Kraken.YouCtrl,Leviathan.YouCtrl,Octopus.YouCtrl,Serpent.YouCtrl`, `Ninja.YouCtrl`, `Permanent`, `Permanent.Assassin+YouCtrl`, `Permanent.Dinosaur+YouCtrl`, `Permanent.inZoneBattlefield`, `Permanent.Merfolk+YouCtrl`, `Salamander`, `Saproling.YouCtrl`, `Sliver`, `Snake.YouCtrl`, `Sorcery.!IsRemembered`, `Sorcery.Red,Instant.Red`, `Spell.Instant+YouCtrl+Red,Spell.Sorcery+YouCtrl+Red,Planeswalker.YouCtrl+Red`, `Spell.Instant+YouCtrl,Spell.Sorcery+YouCtrl,Card.Self`, `Vampire.YouCtrl`, `Vehicle.YouCtrl`, `Warrior.YouCtrl`, `Wolf.YouCtrl,Werewolf.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature`, `Creature,Opponent`, `Creature,Player`, `Creature.blocking`, `Creature.IsRemembered`, `Creature.nonWall`, `Creature.Self`, `Creature.wasDealtExcessDamageThisTurn`, `Creature.White+YouCtrl,You`, `Dinosaur`, `Goblin,Orc`, `Opponent`, `Opponent,Battle`, `Planeswalker`, `Planeswalker.EnchantedBy`, `Player`, `Player,Battle`, `Player,Permanent`, `Player,Planeswalker`, `Player.attackedYouTheirLastTurn`, `Player.controlsLand.counters\_GE1\_CONTESTED`, `Player.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Player.OriginalHostRemembered`, `Player.Other`, `Player.TriggeredDefendingPlayer`, `Player.wasDealtCombatDamageThisTurnBySourceTimes EQ1`, `Player.wasDealtDamageThisTurnBySource GE10`, `Player.withMoreLandsThanYou`, `Spider`, `Vampire`, `You`, `You,Permanent.YouCtrl`

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
  Observed values: `DBDraw`, `DBInvestigate`, `DBReveal`, `DBTapAll`, `DBToken`, `DealDamage`, `DmgOther`, `FungusCounters`, `LoseLife`, `PutCounterAll`, `SpitefulDmg`, `SVar1`, `TrigCast`, `TrigChange`, `TrigChangeZone`, `TrigCharm`, `TrigChoose`, `TrigConjure`, `TrigConjure2`, `TrigConvert`, `TrigCopy`, `TrigCopyPermanent`, `TrigDamage`, `TrigDamageAll`, `TrigDealDamage`, `TrigDestroy`, `TrigDestroy2`, `TrigDig`, `TrigDigUntil`, `TrigDraw`, `TrigEnergy`, `TrigExile`, `TrigExplore`, `TrigFight2`, `TrigFlipSac`, `TrigGain`, `TrigGainGontrol`, `TrigGainLife`, `TrigGoad`, `TrigInvestigate`, `TrigLoseLife`, `TrigLoseLifeChosen`, `TrigLoseLifeRemembered`, `TrigLoseOrSac`, `TrigLoyalty`, `TrigMana`, `TrigMill`, `TrigMonarch`, `TrigPeek`, `TrigPlay`, `TrigPoison`, `TrigPrepare`, `TrigProliferate`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigRemCounter`, `TrigSac`, `TrigSearchLand`, `TrigSeek`, `TrigToken`, `TrigTreasure`, `TrigUntap`, `TrigUntapAll`, `TrigVenture`, `TrigYouDiscard`
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
  Observed values: `Ally.YouCtrl`, `Assassin.YouCtrl`, `Card`, `Card.Outlaw+YouCtrl`, `Card.Self`, `Creature`, `Creature.!token+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.Bird+YouCtrl`, `Creature.Cat+YouCtrl`, `Creature.Colorless+YouCtrl`, `Creature.Dragon+YouCtrl`, `Creature.Enchantment+YouCtrl`, `Creature.faceDown+YouCtrl`, `Creature.Faerie+YouCtrl`, `Creature.Gorgon+YouCtrl,Creature.Snake+YouCtrl`, `Creature.IsRemembered`, `Creature.Ninja+YouCtrl,Creature.Rogue+YouCtrl`, `Creature.nonHuman+YouCtrl`, `Creature.OppCtrl`, `Creature.token+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+!token`, `Creature.YouCtrl+!token+Other`, `Creature.YouCtrl+basePowerEQ0`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+powerGE7`, `Creature.YouCtrl+powerGTbasePower`, `Creature.YouCtrl+ThisTurnEntered`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withTrample`, `Dragon.YouCtrl`, `Faerie.YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Merfolk.YouCtrl`, `Mutant.YouCtrl,Ninja.YouCtrl,Turtle.YouCtrl`, `Pirate.YouCtrl`, `Rogue.YouCtrl`, `Scout.YouCtrl,Pirate.YouCtrl,Rogue.YouCtrl`, `Squirrel.YouCtrl`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Card.AttachedBy`, `Card.IsRemembered`, `Card.Self`, `Card.Self,Creature.PairedWith`, `Creature`, `Creature.EnchantedBy`, `Creature.EquippedBy`, `Creature.OppCtrl`, `Creature.OppCtrl+counters_GE1_BOUNTY,Planeswalker.OppCtrl+counters_GE1_BOUNTY`, `Creature.Self`, `Creature.YouCtrl`, `Creature.YouCtrl+withFlash,Creature.YouCtrl+withHaste`, `Dinosaur.YouCtrl`, `Dragon.YouCtrl`, `Opponent`, `Permanent.YouCtrl`, `Player`, `Player,Battle`, `Player.Chosen`, `Player.EnchantedBy`, `Player.IsRemembered`, `You`, `You,Planeswalker.YouCtrl`

## `DamagePreventedOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigPut`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `You`

## `DayTimeChanges`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBDig`, `DBDraw`, `DBGainLife`, `TrigDamage`, `TrigDig`, `TrigDiscard`, `TrigPutCounter`, `TrigReturn`, `TrigTapOrUntap`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`

## `Destroyed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrackValidDestroy`, `TrigDamage`, `TrigDestroy`
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
  Observed values: `Artifact.nonCreature`, `Permanent.nonCreature+YouCtrl`
- `ValidCauser$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`

## `Devoured`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigToken`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidDevoured$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `Discarded`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DelTrig`, `TrigAmass`, `TrigChange`, `TrigCharm`, `TrigChoosePlayer`, `TrigConjure`, `TrigCopy`, `TrigCounter`, `TrigDamage`, `TrigDealDamage`, `TrigDelay`, `TrigDiscardedToken`, `TrigDouble`, `TrigDoubleDmg`, `TrigDrain`, `TrigDraw`, `TrigExile`, `TrigFight`, `TrigGainLife`, `TrigImmediateTrig`, `TrigLoseLife`, `TrigMana`, `TrigMill`, `TrigPlay`, `TrigPump`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigReturn`, `TrigScry`, `TrigTapOrUntap`, `TrigToken`, `TrigTokenCopy`, `TrigTreasure`, `TrigUntap`
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
  Observed values: `Card`, `Card.nonLand`, `Card.nonLand+nonCreature+OppOwn`, `Card.nonLand+nonCreature+YouCtrl`, `Card.nonLand+YouCtrl`, `Card.OppOwn`, `Card.Other+YouOwn`, `Card.Self`, `Card.YouCtrl`, `Card.YouCtrl+Other`, `Card.YouCtrl+withMadness`, `Card.YouOwn`, `Card.YouOwn+Other`, `Creature.OppOwn`, `Creature.YouCtrl`, `Creature.YouOwn`, `Island.YouCtrl,Pirate.YouCtrl,Vehicle.YouCtrl`, `Land.OppOwn`, `Land.YouCtrl`, `Land.YouOwn`, `Permanent.!token+OppCtrl`, `Spirit.YouOwn,Card.YouOwn+withDisturb`
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
  Observed values: `TrigDealDamage1`, `TrigDig`, `TrigDraw`, `TrigEffect`, `TrigExile`, `TrigInvestigate`, `TrigLoseLife`, `TrigMana`, `TrigPowerstone`, `TrigPump`, `TrigPureChange`, `TrigPutCounter`, `TrigSeek`, `TrigToken`
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Artifact`, `Card.nonLand`, `Card.YouCtrl`, `Land`
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
  Observed values: `TrigDiscover`, `TrigDmg`
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
  Observed values: `DBDamage`, `DBDestroySelf`, `DBLoseLife`, `DBPump`, `DBReveal`, `DivinerTrigPump`, `EffSpellCast`, `LoseGain`, `TrapTriggered`, `TrigAmass`, `TrigAnimate`, `TrigAttach`, `TrigChange`, `TrigChangeZone`, `TrigConjure`, `TrigCopy`, `TrigDamage`, `TrigDealDamage`, `TrigDebuff`, `TrigDig`, `TrigDmg`, `TrigDrain`, `TrigDraw`, `TrigDropLand`, `TrigExile`, `TrigGain`, `TrigGainLife`, `TrigImmediateTrig`, `TrigLose`, `TrigLoseLife`, `TrigMill`, `TrigPrepare`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigReturn`, `TrigSac`, `TrigToken`, `TrigTransform`, `TrigUnblockable`, `TrigUntap`
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
  Observed values: `Card`, `Card.Land`, `Card.NamedCard+OwnedBy Player.Chosen`, `Card.nonLand`, `Card.OppCtrl`, `Card.OppOwn`, `Card.OwnedBy Opponent.NonActive`, `Card.OwnedBy Player.EnchantedBy`, `Card.YouCtrl`, `Card.YouOwn`, `Card.YouOwn+Dragon`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Active`, `Player.Opponent`, `Player.Opponent+Active+controlsArtifact.namedWedding Ring`, `Player.Opponent+NonActive`

## `DungeonCompleted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBReturn`, `TrigToken`
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
  Observed values: `TrigDraw`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Enlisted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigBoon`, `TrigConjure`, `TrigScry`
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
  Observed values: `TrigCopy`, `TrigPutCounterAll`
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
  Observed values: `TrigAmass`, `TrigDamage`, `TrigDraw`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Creature.OppCtrl+DamagedByGiant.YouCtrl;Wizard.YouCtrl;Spell.YouCtrl,Planeswalker.OppCtrl+DamagedByGiant.YouCtrl;Wizard.YouCtrl;Spell.YouCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`

## `ExcessDamageAll`

TODO: Write documentation.

**Parameters:**
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `False`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigTreasure`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`

## `Exerted`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDamageAll`, `TrigDig`, `TrigDiscard`, `TrigPumpAll`, `TrigTap`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `Exiled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigGainLife`, `TrigPutCounter`
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
  Observed values: `TrigChange`, `TrigChangeZone`, `TrigChangeZoneAll`, `TrigCounter`, `TrigDestroy`, `TrigDig`, `TrigDrain`, `TrigDraw`, `TrigExile`, `TrigMassacre`, `TrigPump`, `TrigPutCounterAll`, `TrigSac`, `TrigScry`, `TrigSearch`, `TrigSubmerge`, `TrigToken`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.!token`, `Creature.nonHuman`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.YouCtrl`

## `Explores`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBPutCounter`, `TrigChangeZone`, `TrigDebuff`, `TrigPump`, `TrigPutCounter`
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
  Observed values: `DelTrigPutCounter`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `FightOnce`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDraw`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`

## `FlippedCoin`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDraw`, `TrigOppDmg`, `TrigPump`, `TrigPutCounter`, `TrigToken`, `TrigToken2`, `TrigYouDmg`
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
  Observed values: `TrigPutCounter`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Foretell`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigPump`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `FullyUnlock`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigChange`, `TrigConjure`, `TrigDraw`, `TrigEffect`, `TrigLoseLife`, `TrigMill`, `TrigPump`, `TrigPutCounter`, `TrigSurveil`, `TrigTap`, `TrigToken`
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
  Observed values: `TrigDraw`
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
  Observed values: `TrigDmg`, `TrigInvestigate`
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
  Observed values: `DBAnimate`, `DBPain`, `DBTokens`, `ExileSelf`, `StoreVar`, `TrigAnimate`, `TrigBounce`, `TrigBranch`, `TrigConjure`, `TrigCopyLand`, `TrigCounter`, `TrigDamage`, `TrigDealDamage`, `TrigDraw`, `TrigDropLand`, `TrigExileTop`, `TrigFind`, `TrigFood`, `TrigGainLife`, `TrigHiddenStagAnimateOppLand`, `TrigHiddenStagAnimateYourLand`, `TrigLoseLife`, `TrigPutCounter`, `TrigRemoveSelf`, `TrigSac`, `TrigToken`, `TrigTransform`, `TrigUntap`, `WarningGiven`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+Creature`, `Card.Self+Enchantment`
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
  Observed values: `Card.ExiledWithSourceLKI`, `Creature.YouCtrl`, `Desert`, `Island.YouCtrl`, `Land`, `Land.ExiledWithSourceLKI`, `Land.IsRemembered`, `Land.Legendary+YouCtrl`, `Land.nonBasic+OppCtrl`, `Land.numTypesGE2+YouCtrl`, `Land.OppCtrl`, `Land.Other+YouCtrl`, `Land.sharesCardTypeWith ValidExile Card.ExiledWithSource`, `Land.YouCtrl`, `Land.YouCtrl+sharesNameWith Remembered`, `Land.YouCtrl+YouDontOwn`, `Land.YouOwn+sharesCardTypeWith Imprinted.ExiledWithSource`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.MayPlaySource`

## `LifeGained`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBToken`, `LightOfPromisePutCounter`, `SunbondPutCounter`, `TrigChange`, `TrigChoose`, `TrigConvert`, `TrigDamage`, `TrigDealDamage`, `TrigDrain`, `TrigDraw`, `TrigDraw2`, `TrigEnergy`, `TrigExplore`, `TrigGainLife`, `TrigImmediateTrig`, `TrigLoseLife`, `TrigPrepare`, `TrigPump`, `TrigPumpAll`, `TrigPut`, `TrigPutCounter`, `TrigPutCounter1`, `TrigPutCounterAll`, `TrigPutCounters`, `TrigReturn`, `TrigStore`, `TrigSurveil`, `TrigToken`, `TrigUntap`, `VizkopaMageDrain`
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
  Observed values: `TrigDamageOpp`, `TrigDiscard`, `TrigDraw`, `TrigEnergy`, `TrigExile`, `TrigLifeGain`, `TrigLimDulSac`, `TrigMill`, `TrigPump`, `TrigPutCounter`, `TrigSac`, `TrigToken`
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
  Observed values: `TrigPlay`, `TrigPutCounter`
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
  Observed values: `TrigCounter`, `TrigExile`, `TrigGainLife`, `TrigWinGame`
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
  Observed values: `TrigMana`
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
  Observed values: `DealDamage`, `TrigChangeZone`, `TrigDraw`, `TrigExile`, `TrigGainControl`, `TrigGainLife`, `TrigPump`, `TrigPutCounter`
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
  Observed values: `TrigReturn`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Mentored`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigPutCounter`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature.EquippedBy`

## `Milled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigGainLife`, `TrigReturn`
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
  Observed values: `TrigDraw`, `TrigPutCounter`, `TrigToken`
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
  Observed values: `TrigPutCounterAll`, `TrigToken`
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
  Observed values: `Card.EffectSource`, `Card.Self`

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
  Observed values: `TrigBounce`, `TrigChange`, `TrigChangeZone`, `TrigDealDamage`, `TrigDestroy`, `TrigDigUntil`, `TrigDiscard`, `TrigDraw`, `TrigExile`, `TrigGainControl`, `TrigGainLife`, `TrigLoseLife`, `TrigPlay`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigSac`, `TrigTap`, `TrigToken`
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
  Observed values: `TrigChooseCT`, `TrigDiscard`, `TrigPayLife`, `TrigToken`, `TrigWorldknit`
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
  Observed values: `Card.Self`, `Card.Self+inZoneBattlefield`, `Creature`

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
  Observed values: `Card.Self,Emblem.YouOwn`, `Dungeon.YouOwn`, `Permanent.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidMode$`: TODO: Describe this parameter.
  Observed values: `Attacks,AttackersDeclared,AttackersDeclaredOneTarget`, `ChangesZone,ChangesZoneAll`, `RoomEntered`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Command`, `Command`

## `PayCumulativeUpkeep`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDmg`, `TrigExileAll`, `TrigPump`, `TrigSearch`
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
  Observed values: `TrigDraw`
- `Paid$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `PayLife`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigPutCounter`
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
  Observed values: `Abandon`, `ABGainLife`, `AcademicDraw`, `AcquireScrolls`, `AddUpkeep`, `AgyremReturn`, `AgyremReturn2`, `AnimateDB`, `ApathyDiscard`, `ArtifactMana`, `AtlasDraw`, `AvariceUpkeepSVar`, `Bleed`, `BloodExile`, `Boost`, `BounceAethermage`, `BreachReturn`, `BuildCounter`, `BuildPressure`, `CaptiveClash`, `ChandraDmg`, `ChangeControl`, `ChargeCounter`, `ChooseCreature`, `ChooseName`, `ChooseNumber`, `ChooseType`, `CleanupAndRemember`, `CommanderToken`, `ConjurerExile`, `ConsumingFervorPutCounter`, `CopyArtifact`, `CryptoplasmCopy`, `DalekCreation`, `DBAbandon`, `DBAbandonCheck`, `DBAnimate`, `DBAttach`, `DBChoice`, `DBChooseCard`, `DBCleanup`, `DBCleanupStatic`, `DBCopy`, `DBCopyPermanent`, `DBDestroy`, `DBDig`, `DBDisease`, `DBDragon`, `DBDrawSeven`, `DBExchangeLife`, `DBForget`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBLife`, `DBLose`, `DBMana`, `DBPay`, `DBPump`, `DBPutCounter`, `DBRemoveCounter`, `DBRepeat`, `DBReset`, `DBReturn`, `DBReveal`, `DBSacSelf`, `DBScry`, `DBSelectRecipient`, `DBTap`, `DBToken`, `DBTransform`, `DBTreasureToken`, `DBTrigger`, `DBWin`, `DelayedBoon`, `DelayedScars`, `DelinaTrigExile`, `DestroyRemembered`, `Detain`, `DrainLife`, `DrawDamageOther`, `DrawLoselife`, `DreampodsDig`, `EffMana`, `EffSetLife`, `EffToken`, `EffTrigTutor`, `EmblemTrigChangeZone`, `EmblemTrigToken`, `EvosCounter`, `ExchangeCards`, `Exile`, `ExileEffect`, `ExileSelf`, `ExileTwo`, `FarmsteadGainLife`, `Filter`, `FlickerformReturn`, `FluesSacrifice`, `FourthSac`, `FurnaceDiscard`, `GainLife`, `GhostClear`, `GhostCounter`, `GimmeSome`, `ImpatientDamage`, `InevitableSac`, `InstillTrigSac`, `InvocationTrigExile`, `IrmaCopy`, `JustCleanup`, `KaloniaCounter`, `KioraToken`, `LetheMill`, `LiegesSearch`, `Lose3`, `LoseGlyph`, `LoseSpores`, `LyzoldasDiscard`, `MagmaticDamage`, `ManaGain`, `Meld`, `Mill`, `MusiciansSpite`, `NecroticPlagueSac`, `NettlevineSac`, `NUCounter`, `ObsidianBlazeDmg`, `OppPick`, `PanopticonDraw`, `PilloryLoseLife`, `PlagueTrigDmg`, `PreventEffect`, `ProgenitorCopy`, `PseudoDraw`, `PsychicSlap`, `PutCounter`, `PutCounterAll`, `PutCounterOneEach`, `PutPlagueCounter`, `QuicksilverScry`, `RaiseDead`, `RelicBaneLoseLife`, `RemoveCounters`, `RepeatOpp`, `RepeatOpps`, `RepeatPlayer`, `ReturnedBattlefield`, `RivalDamage`, `RonsoCounter`, `SacAllOthers`, `SacrificeEquippee`, `SacToAbandon`, `SacToIdol`, `SakuraManaSingle`, `SakuraManaTriple`, `SarkhanDiscard`, `SarkhanDraw`, `SelfDestruct`, `SenEffect`, `ShadowDestroyEnchanted`, `SituationalEthics`, `Solved`, `SolveFalcon`, `SorinSac`, `SyphonLife`, `TabernacleDestroy`, `TapCreature`, `TapThis`, `TeaseYou`, `TezzeretAnimate`, `ThuneCounter`, `Trig1Damage`, `TrigAbandon`, `TrigAch`, `TrigAddCounter`, `TrigAdditionalCombat`, `TrigAddMana`, `TrigAddOrRemoveCounter`, `TrigAddPhase`, `TrigAetherDig`, `TrigAllDamage`, `TrigAmass`, `TrigAnimate`, `TrigAnimateAll`, `TrigAttach`, `TrigAttacks`, `TrigBanding`, `TrigBolster`, `TrigBounce`, `TrigBranch`, `TrigCantAttack`, `TrigCast`, `TrigChange`, `TrigChangeAll`, `TrigChangeBattlefield`, `TrigChangeHandExile`, `TrigChangeZone`, `TrigChangeZoneYou`, `TrigChangZone`, `TrigCharm`, `TrigCheatCreature`, `TrigChoice`, `TrigChoose`, `TrigChooseCard`, `TrigChooseCardType`, `TrigChooseColor`, `TrigChooseCurse`, `TrigChooseDirection`, `TrigChooseDmg`, `TrigChooseNumber`, `TrigChooseOneToDestroy`, `TrigChooseOpp`, `TrigChoosePlayer`, `TrigChoosePlayer1`, `TrigChooseRandom`, `TrigChooseToTap`, `TrigCL`, `TrigClash`, `TrigCloak`, `TrigClone`, `TrigCloneCopy`, `TrigColor`, `TrigConjure`, `TrigConnive`, `TrigControl`, `TrigConvert`, `TrigCopy`, `TrigCopyPermanent`, `TrigCoralDiscard`, `TrigCorrode`, `TrigCount`, `TrigCounter`, `TrigCounters`, `TrigCreateAndMill`, `TrigCruelDiscard`, `TrigCumUpkeep`, `TrigCurseArtifactSacrifice`, `TrigCursePayUP`, `TrigDamage`, `TrigDamage4`, `TrigDamageAll`, `TrigDamageOpp`, `TrigDealDamage`, `TrigDealDamage2`, `TrigDestroy`, `TrigDestroyAll`, `TrigDig`, `TrigDigUntil`, `TrigDiscard`, `TrigDiscover`, `TrigDisruptionAura`, `TrigDmg`, `TrigDmg2`, `TrigDmgOpp`, `TrigDoom`, `TrigDouble`, `TrigDoubleCounters`, `TrigDraft`, `TrigDrain`, `TrigDraw`, `TrigDraw1`, `TrigDraw2`, `TrigDrawCard`, `TrigDrawUpkeep`, `TrigDread`, `TrigEarthbend`, `TrigEffect`, `TrigElderSpawnSacrifice`, `TrigEndure`, `TrigEnergy`, `TrigEquipoise`, `TrigEssenceLeak`, `TrigEvidence`, `TrigEvoke`, `TrigExchange`, `TrigExchangeChoose`, `TrigExile`, `TrigExileDelirium`, `TrigExileEnchanted`, `TrigExileSelf`, `TrigExperience`, `TrigExplore`, `TrigExtraTurn`, `TrigFerociousDraw`, `TrigFlip`, `TrigFlipCoin`, `TrigFlipUpkeep`, `TrigFlying`, `TrigFood`, `TrigFoodToken`, `TrigForget`, `TrigGain`, `TrigGainControl`, `TrigGainControl2`, `TrigGainCtrl`, `TrigGainLife`, `TrigGenericChoice`, `TrigGeo`, `TriggeredParoxysm`, `TrigGetCreature`, `TrigGetMana`, `TrigGoad`, `TrigGraveyard`, `TrigHeist`, `TrigHorror`, `TrigImmediate`, `TrigImmediateTrig`, `TrigImmediateTrigger`, `TrigInvestigate`, `TrigInvestigateEach`, `TrigKinship`, `TrigKyrenExile`, `TrigLandship`, `TrigLife`, `TrigLook`, `TrigLoop`, `TrigLoot`, `TrigLose`, `TrigLose1`, `TrigLoseDelay`, `TrigLoseLife`, `TrigLoseLifeDiscard`, `TrigLoseLifeEachOpp`, `TrigMana`, `TrigManifest`, `TrigMarkCouldAttack`, `TrigMaySacorDiscard`, `TrigMend`, `TrigMill`, `TrigMill2`, `TrigMillSK`, `TrigMillYou`, `TrigMisfortune`, `TrigMoveCounter`, `TrigMustAttackBlock`, `TrigNecromancy`, `TrigNight`, `TrigNoKeeper`, `TrigNotKicked`, `TrigNoZombies`, `TrigOathofDruids`, `TrigOathofGhouls`, `TrigOathofMages`, `TrigOathofScholars`, `TrigOmenExileCard`, `TrigOppControl`, `TrigPayCost`, `TrigPeek`, `TrigPendrellFlux`, `TrigPerpetual`, `TrigPerpetualP1P1`, `TrigPhase`, `TrigPhaseLands`, `TrigPhoenix`, `TrigPlay`, `TrigPoison`, `TrigPopulate`, `TrigPrepare`, `TrigPrivateResearchPutCounter`, `TrigProliferate`, `TrigPump`, `TrigPump1`, `TrigPumpAll`, `TrigPut`, `TrigPutCounter`, `TrigPutCounter1`, `TrigPutCounter2`, `TrigPutCounterAll`, `TrigPutCounters`, `TrigPutHunger`, `TrigRandom`, `TrigRandomPump`, `TrigRearrange`, `TrigRem`, `TrigRemove`, `TrigRemoveAll`, `TrigRemoveCounter`, `TrigRemoveCtr`, `TrigRepeat`, `TrigRepeatEach`, `TrigReroll`, `TrigReset`, `TrigRetrieve`, `TrigReturn`, `TrigReturnAll`, `TrigReveal`, `TrigRevealToWin`, `TrigRoll`, `TrigRollDice`, `TrigRollEnd`, `TrigRollUpkeep`, `TrigRope`, `TrigSac`, `TrigSac2`, `TrigSacDiscard`, `TrigSacrifice`, `TrigSacrificeSwamp`, `TrigSacSelf`, `TrigSacYou`, `TrigSaddle`, `TrigSands`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSetLife`, `TrigSkipPhase`, `TrigSolve`, `TrigStore`, `TrigStrife`, `TrigSubCounter`, `TrigSurveil`, `TrigTap`, `TrigTapAll`, `TrigTapOrUntap`, `TrigTarget`, `TrigTargetAuraEquip`, `TrigTempt`, `TrigToken`, `TrigToken1`, `TrigToken2`, `TrigTokenDemon`, `TrigTorment`, `TrigTough`, `TrigToughDraw`, `TrigTransform`, `TrigTransform2`, `TrigTransformBis`, `TrigTreasure`, `TrigTwoPile`, `TrigUnblockable`, `TrigUntap`, `TrigUntapAll`, `TrigUpkeep`, `TrigVenture`, `TrigVote`, `TrigWarp`, `TrigWarrior`, `TrigWin`, `TrigWinGame`, `TrigWinsGame`, `TrigWinsLife`, `TrigWish`, `TrigZarielCombat`, `TripPumpOpp`, `TripTapOpp`, `UntapMerfolk`, `UntapMyr`, `ValkasCounter`, `VerdantToken`, `VesDopCopy`, `VesShapeTurn`, `VillainousChoice`, `WinGame`, `XanEffect`, `XathridCounter`
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
  Observed values: `Artifact.YouCtrl`, `Artifact.YouOwn,Creature.YouOwn`, `Assassin.Legendary+YouCtrl`, `Aura.Attached`, `Bird.YouCtrl`, `Boon.YouOwn`, `Card`, `Card.!attackedThisTurn+Self`, `Card.ActivePlayerCtrl`, `Card.AttachedBy+powerGE4`, `Card.Creature+YouOwn`, `Card.EnchantedBy+!attackedThisTurn`, `Card.EnchantedBy+AttachedTo Creature`, `Card.EquippedBy+!dealtCombatDamageThisTurn Creature`, `Card.IsCommander+YouCtrl`, `Card.IsCommander+YouOwn+YouCtrl`, `Card.Other`, `Card.Plains+YouCtrl`, `Card.Self`, `Card.Self+!attackedThisTurn`, `Card.Self+!IsSolved`, `Card.Self+!kicked`, `Card.Self+!ThisTurnEntered`, `Card.Self+!token`, `Card.Self+attackedThisCombat GE3`, `Card.Self+attackedThisCombat,Card.Self+blockedThisCombat`, `Card.Self+attackedThisTurn`, `Card.Self+attackedThisTurn,Card.Self+blockedThisTurn`, `Card.Self+counters_EQ0_Flying`, `Card.Self+counters_EQ0_P1P1`, `Card.Self+counters_GE100_TOWER`, `Card.Self+counters_GE10_LUCK`, `Card.Self+counters_GE1_ARROWHEAD`, `Card.Self+counters_GE1_CHARGE`, `Card.Self+counters_GE1_DELAY`, `Card.Self+counters_GE1_EGG`, `Card.Self+counters_GE1_M1M1`, `Card.Self+counters_GE1_OIL`, `Card.Self+counters_GE1_P1P1`, `Card.Self+counters_GE1_SCREAM`, `Card.Self+counters_GE1_VITALITY`, `Card.Self+counters_GE1_WRECK`, `Card.Self+counters_GE20_GROWTH`, `Card.Self+counters_GE2_KI`, `Card.Self+counters_GE2_QUEST`, `Card.Self+counters_GE3_OMEN`, `Card.Self+counters_GE3_QUEST`, `Card.Self+counters_GE4_QUEST`, `Card.Self+counters_GE5_CHARGE`, `Card.Self+counters_LE2_JUDGMENT`, `Card.Self+dealtDamageToOppThisTurn`, `Card.Self+enchanted`, `Card.Self+equipped`, `Card.Self+harnessed`, `Card.Self+HasCounters`, `Card.Self+IsSolved`, `Card.Self+startedTheTurnUntapped`, `Card.Self+ThisTurnEntered`, `Card.Self+untapped`, `Card.Self+wasDealtDamageThisTurn`, `Card.Self+YouCtrl+YouOwn`, `Card.StrictlySelf`, `Card.suspended+Self`, `Card.tapped`, `Card.untapped`, `Card.YouCtrl`, `Card.YouOwn`, `Clue.YouCtrl`, `Creature`, `Creature.AttachedBy+untapped`, `Creature.enchanted+YouCtrl`, `Creature.EnchantedBy+powerGE4`, `Creature.isDamaged`, `Creature.IsRemembered`, `Creature.OppCtrl`, `Creature.Other+Legendary+YouCtrl`, `Creature.Other+YouCtrl+powerGE4`, `Creature.Pest+token+YouCtrl`, `Creature.powerGE4+YouCtrl`, `Creature.powerGE5+YouCtrl`, `Creature.Self`, `Creature.tapped+YouCtrl`, `Creature.token+YouCtrl`, `Creature.White`, `Creature.YouCtrl`, `Creature.YouCtrl+Colorless+Other`, `Creature.YouCtrl+counters_GE1_P1P1+attackedThisTurn`, `Creature.YouCtrl+Giant`, `Creature.YouCtrl+namedBiovisionary`, `Creature.YouCtrl+namedBoo`, `Creature.YouCtrl+namedKeeper of Kookus`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+powerGE7`, `Creature.YouCtrl+powerGTbasePower`, `Creature.YouCtrl+powerLTtoughness`, `Creature.YouCtrl+tapped`, `Creature.YouCtrl+withDecayed`, `Creature.YouOwn`, `Creature.YouOwn+Above`, `Creature.YouOwn+DirectlyAbove`, `Demon.YouCtrl`, `Desert.YouCtrl`, `Detective.YouCtrl`, `Egg.YouCtrl`, `Enchantment.YouCtrl`, `Equipment.YouCtrl`, `Food.YouCtrl`, `Goblin.YouCtrl`, `Homunculus.YouCtrl+Legendary`, `Instant.YouOwn,Sorcery.YouOwn`, `Land`, `Land.nonIsland`, `Land.untapped+YouCtrl`, `Land.YouCtrl`, `Permanent.Black+YouCtrl`, `Permanent.Green+YouCtrl`, `Permanent.MultiColor+YouCtrl`, `Permanent.nonBlack+nonLand+ActivePlayerCtrl`, `Permanent.nonLand+White+YouCtrl`, `Permanent.nonLand+YouCtrl`, `Permanent.OppCtrl+counters_GE1_BOUNTY`, `Permanent.Snow+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+Black,Permanent.YouCtrl+Red`, `Permanent.YouCtrl+Blue`, `Permanent.YouCtrl+Blue,Permanent.YouCtrl+Black`, `Permanent.YouCtrl+Green,Permanent.YouCtrl+White`, `Permanent.YouCtrl+Red,Permanent.YouCtrl+Green`, `Permanent.YouCtrl+White,Permanent.YouCtrl+Blue`, `Permanent.YouDontCtrl+counters_GE1_AIM`, `Permanent.YouDontOwn+YouCtrl`, `Plains.ActivePlayerCtrl`, `Planeswalker.Ajani+YouCtrl`, `Planeswalker.Basri+YouCtrl`, `Reflection.token`, `Skeleton.YouCtrl+IsSuspected`, `Snake.YouCtrl`, `Thopter.Other+YouCtrl`, `Town.YouCtrl`, `Treasure.YouCtrl`, `Wizard.YouCtrl`, `Wolf.Other+YouCtrl,Werewolf.Other+YouCtrl`, `Zombie`
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
  Observed values: `TrigBuff`, `TrigDraw`, `TrigToken`, `TrigWarp`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.Self,Spirit.YouCtrl+Other`

## `PhaseOut`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDiscard`, `TrigMill`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.phasedOutSelf`

## `PhaseOutAll`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigPutCounter`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Permanent.phasedOutOther`

## `PlanarDice`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `RolledDie`, `TrigScry`
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
  Observed values: `Eruption`, `ExileSelf`, `OrzhovaDeal`, `TrigChangeZoneAll`, `TrigDestroy`
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Plane`, `Plane.Self`

## `PlaneswalkedTo`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `AcquireScrolls`, `Aether`, `AgyremCleanup`, `DBCleanup`, `DBPhaseIn`, `Disaster`, `DreampodsDig`, `Epiphany`, `ExileSelf`, `FluesSacrifice`, `FurnaceDiscard`, `PanopticonDraw`, `PutCounter`, `QuicksilverScry`, `TrigBolster`, `TrigChaos`, `TrigChoice`, `TrigChoose`, `TrigChooseCard`, `TrigCounter`, `TrigDig`, `TrigEffect`, `TrigExile`, `TrigInvestigate`, `TrigLife`, `TrigLoseLife`, `TrigMill`, `TrigPhaseIn`, `TrigPut`, `TrigPutCounter`, `TrigPutFromHand`, `TrigRepeatEach`, `TrigReverse`, `TrigSurveil`, `TrigToken`
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
  Observed values: `LoseGain`, `TrigChoose`, `TrigDraft`, `TrigDraw`, `TrigPerpetualBuff`, `TrigReturn`
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
  Observed values: `Card`, `Card.ActivePlayerCtrl`, `Card.IsRemembered`, `Card.IsRemembered+CastSa Spell.MayPlaySource`, `Card.nonCreature`, `Card.Self`
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
  Observed values: `Artifact`, `Artifact,Instant,Sorcery`, `Artifact.token+YouCtrl`, `Card`, `Card.!wasCastFromYourHand`, `Card.Black,Card.Red`, `Card.Blue,Card.White`, `Card.Dragon`, `Card.faceDown`, `Card.Historic`, `Card.NamedCard`, `Card.namedKarlov's Crossbow`, `Card.nonCreature`, `Card.Self`, `Card.wasCastFromExile`, `Card.wasCastFromYourGraveyard`, `Creature.Dragon`, `Creature.faceDown`, `Dragon`, `Giant`, `Instant,Sorcery`, `Instant,Sorcery,Planeswalker`, `Legendary`
- `ValidSpell$`: TODO: Describe this parameter.
  Observed values: `Activated.Equip`, `Spell.MayPlaySource`, `Static.isTurnFaceUp`

## `RingTemptsYou`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigCounters`, `TrigDigUntil`, `TrigDraw`, `TrigPutCounters`, `TrigReturn`, `TrigScry`, `TrigToken`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Creature.YouCtrl+Other`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `RolledDie`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `Pump1`, `TrigBranch`, `TrigCounter`, `TrigCounters`, `TrigDrain`, `TrigDraw`, `TrigPhaseIn`, `TrigPump`, `TrigPutCounter`, `TrigRemove`, `TrigReturn`, `TrigReveal`, `TrigToken`, `TrigTrample`, `TrigUntap`
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
  Observed values: `TrigDamage`, `TrigDamageSelf`, `TrigPump`, `TrigPut`, `TrigPutCounter`, `TrigToken`
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
  Observed values: `DBSurveil`, `TrigAlly`, `TrigAnimate`, `TrigBranch`, `TrigChange`, `TrigChoose`, `TrigChooseCard`, `TrigClone`, `TrigCopy`, `TrigCounter`, `TrigCounters`, `TrigDamage`, `TrigDealDamage`, `TrigDelay`, `TrigDelayedTrig`, `TrigDig`, `TrigDiscard`, `TrigDmg`, `TrigDraft`, `TrigDraw`, `TrigDrawCard`, `TrigDread`, `TrigEffect`, `TrigExile`, `TrigExplore`, `TrigGainLife`, `TrigLoseLife`, `TrigMana`, `TrigMill`, `TrigPoison`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigReturn`, `TrigSacrifice`, `TrigSearch`, `TrigToken`, `TrigTransform`, `TrigTreasure`, `TrigUnblockable`, `TrigVenture`
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
  Observed values: `Artifact`, `Artifact.!token+Other,Creature.!token+Other`, `Artifact.nonCreature`, `Artifact.OppCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Blood.token+YouCtrl`, `Card.Self`, `Card.Self,Artifact.YouCtrl`, `Card.Self,Clue.Other+YouCtrl`, `Card.Self,Creature`, `Card.token`, `Card.token+YouCtrl`, `Clue`, `Clue,Food`, `Clue.YouCtrl`, `Creature`, `Creature.!token`, `Creature.Black`, `Creature.Green`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+YouCtrl`, `Creature.Other,Artifact.Other`, `Creature.YouCtrl`, `Desert.YouCtrl`, `Eldrazi.Other`, `Elemental.!token`, `Enchantment.YouCtrl`, `Food`, `Food.YouCtrl`, `Food.YouCtrl,Clue.YouCtrl`, `Junk.YouCtrl`, `Land`, `Permanent`, `Permanent.!token`, `Permanent.!token+OppCtrl`, `Permanent.!token+YouCtrl`, `Permanent.Other`, `Permanent.Other+!token`, `Permanent.token+nonCreature`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl`, `Treasure.YouCtrl`
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
  Observed values: `TrigSeek`, `TrigToken`
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
  Observed values: `TrigPump`
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
  Observed values: `DBDraw`, `DBReveal`, `TrigCharm`, `TrigDmg`, `TrigDraw`, `TrigEff`, `TrigExile`, `TrigPeek`, `TrigPump`, `TrigPutCounter`, `TrigTap`, `TrigUntap`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.tapped`, `Island.YouCtrl`
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
  Observed values: `TrigGainLife`, `TrigPutCounter`, `TrigPutCounter2`, `TrigSac`
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
  Observed values: `TrigConjure`, `TrigDmg`, `TrigToken`
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
  Observed values: `Abandon`, `BloodyCombat`, `ChooseChampion`, `ChooseCreature`, `ChooseOpponent`, `ChooseTheWretch`, `ConstructDestiny`, `DarkEffect`, `DBAddMana`, `DBChoose`, `DBChoosePerms`, `DBChoosePlayer`, `DBCopyCommander`, `DBDestroy`, `DBDig`, `DBDraw`, `DBExile`, `DBGainControl`, `DBRepeat`, `DBSac`, `DBSearch`, `DBToken`, `DiscardHope`, `DmgAll`, `ExileFlying`, `GeniusLife`, `GetRealms`, `GetSaps`, `GoodTimes`, `GraveEmbrace`, `GreatMind`, `Ignite`, `LibraryDance`, `MakeUseful`, `MoltenEffect`, `MoveToBottom`, `MyWish`, `NewEvil`, `OppTutor`, `PlotEffect`, `RevealFate`, `ShowTheWeakness`, `TrigBranch`, `TrigChangeZone`, `TrigCharm`, `TrigChoose`, `TrigControl`, `TrigCopyPermanent`, `TrigDamageAll`, `TrigDigUntil`, `TrigDmg`, `TrigEffect1`, `TrigExtraTurn`, `TrigMill`, `TrigRedistribute`, `TrigRepeat`, `TrigRepeatEach`, `TrigSacEach`, `TrigToken`, `TwoPiles`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Command`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.!OnGoing`, `Card.Self`

## `Shuffled`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `ExileEffect`, `TrigChangeZone`, `TrigDamage`, `TrigDig`, `TrigPutCounter`
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
  Observed values: `TrigBoon`, `TrigChoose`, `TrigConjure`, `TrigCopy`, `TrigDestroy`, `TrigDraw`, `TrigEffect`, `TrigImmediateTrig`, `TrigPump`, `TrigRemoveCounters`, `TrigReturn`, `TrigSeek`, `TrigTap`, `TrigTargetC`, `TrigToken`, `TrigUntap`
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
  Observed values: `TrigChangeTarget`, `TrigChoose`, `TrigCopy`, `TrigCopyMain`, `TrigCopySpell`, `TrigDraw`, `TrigPutCounter`
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
  Observed values: `TrigChangeTarget`
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
  Observed values: `AddRebound`, `ApproachingSuns`, `BloodPump`, `BountysGift`, `Buybacked`, `CountCorruptedPlayers`, `CounterSpellOpp`, `DamageSomeone`, `DBAnimate`, `DBBlink`, `DBCopy`, `DBCount`, `DBCounter`, `DBDamageAll`, `DBDealDamage`, `DBDigUntil`, `DBDraw`, `DBEffect`, `DBExileSelf`, `DBGainLife`, `DBGoad`, `DBInvestigate`, `DBLoseLife`, `DBPump`, `DBPutCounter`, `DBRemoveCounters`, `DBReveal`, `DBScry`, `DBSearch`, `DBSurveil`, `DBToken`, `DBTokens`, `DelayedBuyback`, `DelayedTrigEff`, `DevourPump`, `DjinnisGift`, `DreamCounters`, `EffSpellCast`, `EffSpellCast12U`, `ExchangeControlSpell`, `ExileSelf`, `ExileTop`, `Grind`, `LifeSummer`, `NorinExile`, `PutCounter`, `RememberCaster`, `RemoveEffect`, `ReplEffAddCounter`, `SavageSummon`, `StealAbs`, `TakeOneEach`, `Trig5Damage`, `TrigAbandon`, `TrigAddCounter`, `TrigAddTurn`, `TrigAirbend`, `TrigAmass`, `TrigAnimate`, `TrigArtisanCopy`, `TrigBird`, `TrigBounce`, `TrigBranch`, `TrigCanNotBlock`, `TrigCast`, `TrigCastInstant`, `TrigCastSorcery`, `TrigCatToken`, `TrigChange`, `TrigChangePT`, `TrigChangeTarget`, `TrigChangeZone`, `TrigCharge`, `TrigCharm`, `TrigChoose`, `TrigChooseTgt`, `TrigClone`, `TrigConjure`, `TrigConnive`, `TrigControl`, `TrigControlPlayer`, `TrigConvert`, `TrigConvertLaserbeak`, `TrigConvertRavage`, `TrigCopy`, `TrigCopyMain`, `TrigCopySpell`, `TrigCopyTarget`, `TrigCounter`, `TrigCounters`, `TrigCounterSameGrave`, `TrigCounterSpell`, `TrigCurse`, `TrigDamage`, `TrigDamageAll`, `TrigDaw`, `TrigDealDamage`, `TrigDealOneDamage`, `TrigDebuff`, `TrigDestroy`, `TrigDestroyAll`, `TrigDig`, `TrigDigUntil`, `TrigDiscard`, `TrigDiscover`, `TrigDmg`, `TrigDogToken`, `TrigDouble`, `TrigDraft`, `TrigDrain`, `TrigDraw`, `TrigDraw2`, `TrigDrawCard`, `TrigDS`, `TrigEarthbend`, `TrigEffect`, `TrigEffectBis`, `TrigEnergy`, `TrigExile`, `TrigExileSpell`, `TrigExileTop`, `TrigExperience`, `TrigFight`, `TrigFind`, `TrigFirstStrike`, `TrigFlashback`, `TrigFlip`, `TrigFlipYouCast`, `TrigFlying`, `TrigFood`, `TrigForEach`, `TrigGainControl`, `TrigGainLife`, `TrigGoad`, `TrigHatchlingAnimate`, `TrigHerd`, `TrigImmediateTrig`, `TrigImpulsiveDraw`, `TrigIncubate`, `TrigInvestigate`, `TrigKnowledgeExileSpell`, `TrigLand`, `TrigLoot`, `TrigLose`, `TrigLoseLife`, `TrigLoyalty`, `TrigMana`, `TrigManifest`, `TrigMayCast`, `TrigMill`, `TrigOpenAttraction`, `TrigPerpetualP1P1`, `TrigPoison`, `TrigPowerStone`, `TrigPrepare`, `TrigProliferate`, `TrigProtect`, `TrigPump`, `TrigPump11`, `TrigPump2`, `TrigPumpAll`, `TrigPumpCurse`, `TrigPumpFear`, `TrigPumpKW`, `TrigPumpP1P1`, `TrigPut`, `TrigPutBottom`, `TrigPutCounter`, `TrigPutCounter1`, `TrigPutCounterAll`, `TrigPutCounters`, `TrigPutCountersAll1`, `TrigPutCountersAll2`, `TrigRadiation`, `TrigRebound`, `TrigRegen`, `TrigRegenerate`, `TrigRem`, `TrigRemove`, `TrigRemoveCounter`, `TrigRemoveSelf`, `TrigReturn`, `TrigReturnThis`, `TrigReveal`, `TrigRollDice`, `TrigSac`, `TrigSacrifice`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSpellweaverCopy`, `TrigSurveil`, `TrigTap`, `TrigTapOrUntap`, `TrigToken`, `TrigToken2`, `TrigTokenBis`, `TrigTokenDragon`, `TrigTokenKobold`, `TrigTransform`, `TrigTreasure`, `TrigTremor`, `TrigUnblock`, `TrigUnblockable`, `TrigUntap`, `TrigUntap2`, `TrigUntapAll`, `TrigVenture`, `TrigWolf`, `WarningGiven`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `HasXManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+attackedThisTurn`, `Card.Self+attacking`, `Card.Self+counters_EQ1_FETCH`, `Card.Self+counters_GE2_QUEST`, `Card.Self+counters_LE2_P1P1`, `Card.Self+counters_LT3_CHARGE`, `Card.Self+Creature`, `Card.Self+Enchantment`, `Card.Self+IsRenowned`, `Card.Self+IsSolved`, `Card.Self+suspended`, `Card.StrictlySelf`, `Card.suspended+Self`, `Card.tapped`, `Creature.YouCtrl`, `Creature.YouCtrl+namedKeimi`
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
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Enchantment`, `Artifact,Instant,Sorcery`, `Artifact,Lesson`, `Artifact.cmcGE4`, `Artifact.cmcGE6`, `Artifact.Creature`, `Artifact.nonColorless`, `Artificer,Artifact`, `Aura`, `Aura,Equipment`, `Aura,Equipment,Vehicle`, `Bird`, `Card`, `Card.!wasCastFromTheirHand`, `Card.!wasCastFromYourHand`, `Card.Adventure`, `Card.Adventure,Dragon`, `Card.AnyChosenColor`, `Card.Black`, `Card.Black+Green`, `Card.Black+wasCastFromYourHand`, `Card.Blue`, `Card.Blue+Red`, `Card.Blue,Card.Black`, `Card.Blue,Card.Red,Card.Black`, `Card.BorderColorBlack`, `Card.BorderColorSilver`, `Card.BorderColorWhite`, `Card.CastSa Spell.MayPlaySource`, `Card.ChosenColor`, `Card.ChosenType`, `Card.cmcEQChosen,Card.powerEQChosen,Card.toughnessEQChosen`, `Card.cmcEQCount$ChosenNumber`, `Card.cmcEQX`, `Card.cmcEQY`, `Card.cmcEven`, `Card.cmcGE4`, `Card.cmcGE5`, `Card.cmcGE6`, `Card.cmcLE3`, `Card.cmcOdd`, `Card.Colorless`, `Card.Colorless+cmcGE7`, `Card.Colorless+cmcGE7+YouCtrl`, `Card.CostsPhyrexianMana`, `Card.Creature`, `Card.Creature+!sharesCreatureTypeWith Valid Creature.YouCtrl+!sharesCreatureTypeWith ValidGraveyard Creature.YouOwn`, `Card.Creature+!sharesCreatureTypeWith ValidLibrary Creature.YouOwn`, `Card.Dragon,Card.nonCreature`, `Card.Eldrazi`, `Card.ExiledWithSourceLKI`, `Card.Green`, `Card.Green+Blue`, `Card.Green,Card.White`, `Card.hasKeywordConvoke+Other`, `Card.hasKeywordFlash+Other`, `Card.hasXCost`, `Card.Historic`, `Card.Instant,Card.Sorcery`, `Card.IsCommander+YouCtrl`, `Card.IsCommander+YouOwn`, `Card.IsImprinted+IsRemembered+wasCastFromExile`, `Card.IsRemembered`, `Card.IsRemembered+nonLand`, `Card.kicked`, `Card.kicked+YouCtrl`, `Card.Knight`, `Card.Kraken+wasCastFromYourHandByYou,Card.Leviathan+wasCastFromYourHandByYou,Card.Octopus+wasCastFromYourHandByYou,Card.Serpent+wasCastFromYourHandByYou`, `Card.Legendary`, `Card.Legendary+wasCastFromYourHandByYou`, `Card.Legendary+YouCtrl`, `Card.MultiColor`, `Card.NamedCard`, `Card.nonArtifact`, `Card.nonBlack`, `Card.nonColorless`, `Card.nonCreature`, `Card.nonCreature+cmcGE3`, `Card.nonCreature+cmcLTX`, `Card.nonCreature+ManaCostPartialBlue`, `Card.nonCreature+YouCtrl`, `Card.nonCreature,Dragon`, `Card.nonCreature,Otter`, `Card.nonRed`, `Card.numColorsEQ2`, `Card.numTypesGE2`, `Card.OppCtrl`, `Card.Outlaw`, `Card.Party`, `Card.Pirate`, `Card.Planeswalker`, `Card.Red`, `Card.Red+White`, `Card.Self`, `Card.Self+!wasCastFromExile`, `Card.Self+kicked`, `Card.Self+kicked 1`, `Card.Self+kicked 2`, `Card.Self+namedApproach of the Second Sun`, `Card.Self+wasCastFromYourHandByYou`, `Card.sharesCardTypeWith Imprinted.ExiledWithSource`, `Card.sharesCardTypeWith ValidExile Card.ExiledWithSource`, `Card.SharesCMCWith Imprinted.ExiledWithSource,Card.SharesColorWith Imprinted.ExiledWithSource`, `Card.sharesCreatureTypeWith`, `Card.sharesNameWith Imprinted+!token`, `Card.sharesNameWith Remembered`, `Card.Spirit,Card.Arcane`, `Card.ThisTurnEnteredYourHand`, `Card.Vampire+Other`, `Card.Vampire+sharesNameWith Remembered.ExiledWithSource`, `Card.wasCastFromExile`, `Card.wasCastFromExile+!token`, `Card.wasCastFromGraveyard`, `Card.wasCastFromTheirHand`, `Card.wasCastFromYourGraveyard`, `Card.wasCastFromYourGraveyardByYou`, `Card.wasCastFromYourHand`, `Card.White`, `Card.White+Black`, `Card.White,Card.Blue,Card.Black,Card.Red`, `Card.withCascade`, `Card.withConvoke`, `Card.withInfect`, `Card.YouCtrl`, `Card.YouCtrl+kicked`, `Card.YouCtrl+nonCreature`, `Card.YouDontOwn`, `Card.YouDontOwn+nonCreature`, `Cat`, `Creature`, `Creature,Planeswalker`, `Creature.AdventureCard`, `Creature.Bird,Creature.Beast`, `Creature.Black,Creature.Red,Creature.Green`, `Creature.Blue`, `Creature.ChosenType`, `Creature.cmcEQ4,Creature.cmcEQ5,Creature.cmcEQ6`, `Creature.cmcEQX`, `Creature.cmcGE4`, `Creature.cmcGE5`, `Creature.cmcGE6`, `Creature.cmcGE7`, `Creature.cmcLE3`, `Creature.Colorless`, `Creature.Dragon`, `Creature.Eldrazi+cmcGE7`, `Creature.Eldrazi+cmcGE7+YouCtrl`, `Creature.Green`, `Creature.Human`, `Creature.NamedCard`, `Creature.nonLegendary`, `Creature.nonSliver`, `Creature.OppCtrl+!SharesColorWith Valid Creature.YouCtrl`, `Creature.Pegasus,Creature.Unicorn,Creature.Horse`, `Creature.Phyrexian`, `Creature.Phyrexian,Creature.Artifact`, `Creature.powerGE4+powerLE6`, `Creature.powerGE5`, `Creature.powerGE7`, `Creature.sharesCreatureTypeWith Commander`, `Creature.Vampire`, `Creature.wasCastFromYourGraveyard`, `Creature.wasCastFromYourLibrary`, `Creature.withFlying`, `Creature.withFlying+nonLegendary`, `Creature.withMutate`, `Creature.withoutFlying`, `Dinosaur`, `Doctor,Creature.withDoctor's companion`, `Dog`, `Dragon`, `Dragon,Omen`, `Dragon.wasCastFromYourGraveyard`, `Druid`, `Elemental`, `Elf`, `Enchantment`, `Equipment`, `Giant`, `Goblin`, `Human`, `Instant`, `Instant,Sorcery`, `Instant,Sorcery,Artifact`, `Instant,Sorcery,Otter.!CastSaSource`, `Instant,Sorcery,Wizard`, `Instant.!token,Sorcery.!token`, `Instant.Adventure,Sorcery.Adventure`, `Instant.Blue,Instant.White,Sorcery.Blue,Sorcery.White`, `Instant.cmcGE3,Sorcery.cmcGE3`, `Instant.cmcGE5+wasCastFromYourHandByYou,Sorcery.cmcGE5+wasCastFromYourHandByYou`, `Instant.cmcGE5,Sorcery.cmcGE5`, `Instant.cmcGTX,Sorcery.cmcGTX`, `Instant.cmcLE3+YouCtrl,Sorcery.cmcLE3+YouCtrl`, `Instant.cmcLE3,Sorcery.cmcLE3`, `Instant.MultiColor+wasCastFromYourHandByYou,Sorcery.MultiColor+wasCastFromYourHandByYou`, `Instant.MultiColor,Sorcery.MultiColor`, `Instant.NamedCard,Sorcery.NamedCard`, `Instant.Red,Sorcery.Red`, `Instant.sharesNameWith YourGraveyard,Sorcery.sharesNameWith YourGraveyard`, `Instant.wasCastFromTheirHand,Sorcery.wasCastFromTheirHand`, `Instant.wasCastFromYourGraveyard,Sorcery.wasCastFromYourGraveyard`, `Instant.wasCastFromYourHand`, `Instant.wasCastFromYourHand,Sorcery.wasCastFromYourHand`, `Instant.wasCastFromYourHandByYou`, `Instant.wasCastFromYourHandByYou,Sorcery.wasCastFromYourHandByYou`, `Instant.wasCastFromYourLibrary,Sorcery.wasCastFromYourLibrary`, `Instant.YouCtrl+wasCastFromYourGraveyard,Sorcery.YouCtrl+wasCastFromYourGraveyard`, `Instant.YouCtrl+wasCastFromYourHandByYou,Sorcery.YouCtrl+wasCastFromYourHandByYou`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Kithkin`, `Kobold`, `Legendary`, `Lesson`, `Lesson,Saga,Shrine`, `Lizard`, `Merfolk`, `Myr`, `Omen`, `Permanent`, `Permanent.Black`, `Permanent.Blue`, `Permanent.Faerie,Permanent.Wizard`, `Permanent.Green`, `Permanent.Red`, `Permanent.White`, `Planeswalker`, `Planeswalker.Bolas`, `Snake`, `Sorcery`, `Sorcery.wasCastFromYourHandByYou`, `Sorcery.YouOwn+wasCastFromYourHand,Instant.YouOwn+wasCastFromYourHand`, `Spirit,Arcane`, `Treefolk`, `Turtle`, `Wizard`, `Zombie`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Instant.singleTarget,Sorcery.singleTarget`, `Spell.Kicked`, `Spell.ManaFromCard.StrictlySelf`, `Spell.ManaFromCreature_3`, `Spell.ManaFromTreasure`, `Spell.ManaSpent EQ0`, `Spell.ManaSpent GE4`, `Spell.ManaSpent GE7`, `Spell.ManaSpent GTX`, `Spell.MayPlaySource`, `Spell.Modal`, `Spell.numTargets GE1`, `Spell.singleTarget`, `Spell.Warp`
- `ValidSAonCard$`: TODO: Describe this parameter.
  Observed values: `Spell.Creature+sharesNameWith YourGraveyard,Spell.Planeswalker+sharesNameWith YourGraveyard`, `Spell.ManaSpent GE4`, `Spell.ManaSpent GE8`, `Spell.ManaSpent LTX`, `Spell.YouDontOwn`

## `SpellCastOrCopy`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBScry`, `LifeGain`, `TrigAnimate`, `TrigChoice`, `TrigDealDamage`, `TrigDig`, `TrigDiscard`, `TrigDrain`, `TrigDraw`, `TrigEffect`, `TrigOctify`, `TrigPower`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigReturn`, `TrigToken`, `TrigUnblockable`
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
  Observed values: `TrigDamage`, `TrigDrain`, `TrigPumpAll`, `TrigPutCounter`, `TrigTarget`
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
  Observed values: `TrigPump`
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
  Observed values: `TrigBounce`, `TrigCopy`, `TrigDamageAll`, `TrigDmg`, `TrigDraw`, `TrigPeek`, `TrigPutCounter`, `TrigReturn`
- `FirstTime$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.StrictlySelf`
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
  Observed values: `TrigToken`
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
  Observed values: `DBExileTopCard`, `ExileTwo`, `TrigBounce`, `TrigBuff`, `TrigCanNotBlock`, `TrigCharm`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDestroy1`, `TrigDig`, `TrigDiscard`, `TrigDrain`, `TrigDraw`, `TrigExile`, `TrigFight`, `TrigGain`, `TrigGainLife`, `TrigImmediateTrig`, `TrigLose`, `TrigMill`, `TrigPoison`, `TrigProliferate`, `TrigPump`, `TrigPutCounter`, `TrigRemoveCounter`, `TrigScry`, `TrigSry`, `TrigSurveil`, `TrigTap`, `TrigToken`, `TrigUntap`
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
  Observed values: `Artifact`, `Artifact.OppCtrl`, `Artifact.YouCtrl`, `Card.AttachedBy`, `Card.Self`, `Creature`, `Creature,Land`, `Creature.OppCtrl`, `Creature.YouCtrl`, `Dwarf.YouCtrl`, `Forest.OppCtrl`, `Island.OppCtrl`, `Land.ChosenType+OppCtrl`, `Land.counters_GE1_MINE`, `Land.FortifiedBy`, `Merfolk.YouCtrl`, `Mountain.OppCtrl`, `Swamp,Mountain,Permanent.Black,Permanent.Red`
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
  Observed values: `AddMana`, `DarkMana`, `DBRepeat`, `TrigBounce`, `TrigControl`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDmg`, `TrigGainLife`, `TrigMana`, `TrigPump`, `TrigPutCounter`, `TrigRemoveCounter`, `TrigTapAll`, `TrigToken`
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
  Observed values: `Artifact`, `Artifact.token`, `Card.AttachedBy`, `Card.EnchantedBy`, `Card.FortifiedBy`, `Card.Self`, `Creature`, `Forest`, `Island`, `Land`, `Land.Basic`, `Land.nonBasic`, `Land.OppCtrl`, `Land.sharesNameWith Imprinted`, `Land.Snow`, `Land.YouCtrl`, `Mountain`, `Mountain,Forest,Plains`, `Permanent`, `Permanent.nonLand`, `Swamp`

## `TokenCreated`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigCounter`, `TrigLoseLife`, `TrigTransform`
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
  Observed values: `TrigPutCounter`, `TrigToken`
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
  Observed values: `TrigExile`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`

## `Transformed`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DamageAndMoreDamage`, `Token`, `TokenAndLife`, `TrigAddTurn`, `TrigAnimate`, `TrigChange`, `TrigChangeZone`, `TrigDamageAll`, `TrigDestroy`, `TrigDig`, `TrigDraw`, `TrigExile`, `TrigFight`, `TrigMana`, `TrigMill`, `TrigPeek`, `TrigProt`, `TrigPump`, `TrigPumpAll`, `TrigPut`, `TrigPutCounter`, `TrigReturn`, `TrigReveal`, `TrigSacrifice`, `TrigToken`, `TrigTransform`
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
  Observed values: `Card.Self`, `Creature.EquippedBy`, `Creature.YouCtrl+nonHuman+inZoneBattlefield`, `Permanent.YouCtrl+inZoneBattlefield`, `Phyrexian.YouCtrl+inZoneBattlefield`

## `TurnBegin`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `ClearActivePlayer`, `DBCleanup`, `DBCleanup2`, `DBDuration`, `ResetTurnCount`, `TrigReset`
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
  Observed values: `DBWeaverofLiesSetState`, `KaronaEffect`, `TrigAttach`, `TrigBounce`, `TrigChange`, `TrigChangeTgts`, `TrigChangeZone`, `TrigChangeZoneAll`, `TrigChoice`, `TrigChoose`, `TrigChooseType`, `TrigCopy`, `TrigCounter`, `TrigCounters`, `TrigCurseNonSoldiers`, `TrigDamage`, `TrigDealDamage`, `TrigDermoplasmChangeZone`, `TrigDestroy`, `TrigDig`, `TrigDiscard`, `TrigDjinnVanishing`, `TrigDmg`, `TrigDonate`, `TrigDraw`, `TrigEffect`, `TrigEndure`, `TrigExile`, `TrigFaceUp`, `TrigFight`, `TrigGainLife`, `TrigLook`, `TrigLoseLife`, `TrigMana`, `TrigProtect`, `TrigProvoke`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigPutCounters`, `TrigRandom`, `TrigRegenerate`, `TrigRemember`, `TrigReturn`, `TrigScry`, `TrigSearch`, `TrigSeek`, `TrigSetState`, `TrigSkipUntap`, `TrigTapOrUntap`, `TrigTapUnTap`, `TrigToken`, `TrigUntap`
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
  Observed values: `Card.AttachedBy`, `Card.Self`, `Card.Self,Creature.Other+YouCtrl`, `Card.Self,Permanent`, `Card.Self,Permanent.Other+YouCtrl`, `Creature.YouCtrl`, `Detective.YouCtrl`, `Permanent`, `Permanent.Creature+YouCtrl`, `Permanent.Creature+YouCtrl+Other`, `Permanent.inZoneBattlefield`, `Permanent.YouCtrl`
- `ValidCause$`: TODO: Describe this parameter.
  Observed values: `SpellAbility.YouCtrl`

## `Unattached`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigDestroy`, `TrigSac`
- `TriggerDescription$`: TODO: Describe this parameter.
- `ValidAttachment$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidObject$`: TODO: Describe this parameter.
  Observed values: `Permanent`

## `UnlockDoor`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `DBDealDamage`, `TrigChangeZone`, `TrigConjure`, `TrigCopy`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDig`, `TrigDraw`, `TrigDread`, `TrigManifest`, `TrigMill`, `TrigPlay`, `TrigPutCounter`, `TrigReturn`, `TrigSearch`, `TrigSurveil`, `TrigTap`, `TrigToken`
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
  Observed values: `TrigPutCounter`
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
  Observed values: `Card.Self`, `Permanent.YouCtrl`
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
  Observed values: `ClearRemembered`, `DBDestroy`, `DBPhaseIn`, `DBPutCounter`, `GFGToken`, `RemoveCounters`, `SeerDig`, `TrigAddPhase`, `TrigCopy`, `TrigCounters`, `TrigDiscard`, `TrigDrain`, `TrigDraw`, `TrigDraw1`, `TrigExchangeControl`, `TrigExile`, `TrigGainLife`, `TrigMill`, `TrigPump`, `TrigPutCounter`, `TrigRemoveCounter`, `TrigReturn`, `TrigReveal`, `TrigSearch`, `TrigToken`, `TrigVenture`
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
  Observed values: `Card`, `Card.EffectSource`, `Card.Self`, `Card.Self+ActivePlayerCtrl`, `Card.Self,Creature.Other+YouCtrl+cmcGE5`, `Creature.EquippedBy`, `Permanent.YouCtrl`

## `VisitAttraction`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigAttach`, `TrigCopy`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Attraction.IsRemembered`, `Attraction.YouCtrl`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`

## `Vote`

TODO: Write documentation.

**Parameters:**
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigLoseLife`, `TrigScry`, `TrigTreasure`
- `List$`: TODO: Describe this parameter.
  Observed values: `OppVotedDiff`, `OppVotedSame`, `OppVotedSame,OppVotedDiff`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
