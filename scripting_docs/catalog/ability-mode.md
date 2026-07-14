# Ability Modes

<!-- forge-doc-scope: A: -->

## `Abandon`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `TappedCreaturePower`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberAbandoned$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCopy`, `DBSetInMotionAgain`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Card>`, `PayLife<3>`, `Sac<2/Creature>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`

## `ActivateAbility`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer`
- `ManaAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDrainMana`, `DBEmptyPool`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Land`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `AddOrRemoveCounter`

TODO: Write documentation.

**Parameters:**
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Card.HasCounters`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.counters_GE1_TIME`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `1 B G`, `1`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `3`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `CHARGE`, `DEFENSE`, `DOOM`, `LORE`, `P1P1`, `PLAGUE`, `TIME`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Self`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredPlayer`
- `EachExistingCounter$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRemovedCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveConditionSVar$`: TODO: Describe this parameter.
  Observed values: `Count$Valid Card.EnchantedBy+!attackedOrBlockedSinceYourLastUpkeep`, `Targeted$Valid Battle.OppProtect`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBImmediateTrigger`, `DBSac`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Exile`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Battle`, `Permanent`, `Permanent.inZoneBattlefield+YouCtrl,Card.suspended+YouOwn`, `Permanent.inZoneBattlefield,Card.suspended`, `Saga.YouCtrl`

## `AddPhase`

TODO: Write documentation.

**Parameters:**
- `AfterPhase$`: TODO: Describe this parameter.
  Observed values: `End of Turn`, `EndCombat`, `Main2`
- `BeforeFirstPostCombatMainEnd$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `TriggeredTargetLKICopy`
- `ConditionFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self`, `Creature.attacking`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LT1`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 R G`
- `ExtraPhase$`: TODO: Describe this parameter.
  Observed values: `Beginning`, `Combat`, `End of Turn`, `Upkeep`
- `ExtraPhaseDelayedTrigger$`: TODO: Describe this parameter.
  Observed values: `DelTrigStatic`, `DelTrigUntap`
- `ExtraPhaseDelayedTriggerExcute$`: TODO: Describe this parameter.
  Observed values: `TrigEffect`, `TrigUntapAll`
- `FollowedBy$`: TODO: Describe this parameter.
  Observed values: `Main2`
- `NumPhases$`: TODO: Describe this parameter.
  Observed values: `2`, `TriggerCount$DamageAmount`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDelayedEffect`, `DBDelTrig`, `DBEffect`, `DBPumpAll`, `DBUntapAll`, `MakeVigilant`

## `AddTurn`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Blessing`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.prowled`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE7`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 U U R`, `PayEnergy<8> Exile<1/CARDNAME>`, `SubCounter<12/LOYALTY>`, `T SubCounter<3/CHARGE>`, `T SubCounter<1/EON> Return<1/CARDNAME>`, `SubCounter<All/P1P1>`, `SubCounter<10/LOYALTY>`, `SubCounter<9/LOYALTY>`, `Waterbend<20>`, `2 U U T PutCardToLibFromBattlefield<1/-1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{4}{U}{U}{R}`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `DelayTriggerRemembered`, `ImprintedController`, `Promised`, `ReplacedCardLKIController`, `You`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExtraTurnDelayedTrigger$`: TODO: Describe this parameter.
  Observed values: `DBDelTrig`
- `ExtraTurnDelayedTriggerExcute$`: TODO: Describe this parameter.
  Observed values: `TrigEffect`, `TrigEffect2`, `TrigLose`
- `GiftDescription$`: TODO: Describe this parameter.
  Observed values: `an extra turn`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Doctor.YouCtrl`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoSchemes$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumTurns$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Cleave`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ShowMessage$`: TODO: Describe this parameter.
  Observed values: `True`
- `SkipUntap$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChange`, `DBCleanup`, `DBExile`, `DBIntensify`, `DBPump`, `DBReturn`, `DBShuffle`, `DBToken`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `AdvanceCrank`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T`
- `SpellDescription$`: TODO: Describe this parameter.

## `Airbend`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredTarget`, `Valid Creature.NotDefinedTargeted`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDraw`, `DBEffect`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `MaxTgts`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Stack`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.Other`, `Creature.Other,Card.inZoneStack`, `Creature.YouCtrl`, `Permanent.nonLand`, `Permanent.nonLand+Other`, `Permanent.nonLand+Other+YouCtrl`, `Permanent.Other+nonLand+YouCtrl`

## `AlterAttribute`

TODO: Write documentation.

**Parameters:**
- `Activate$`: TODO: Describe this parameter.
  Observed values: `False`
- `Attributes$`: TODO: Describe this parameter.
  Observed values: `Commander`, `Harnessed`, `Plotted`, `Prepared`, `Saddled`, `Solved`, `Suspected`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `OppCreatures`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Remembered`, `Targeted`, `TriggeredTargetLKICopy`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.inZoneBattlefield`, `Card.IsSuspected`, `Creature.powerGE7`, `Creature.YouOwn`, `Mount`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GTYourCreatures`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T`, `6 B T Exile<1/Creature>`, `ExileFromGrave<8/Card>`, `T tapXType<2/Creature>`, `ExileFromGrave<1/Creature>`, `3 T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `EffectSource`, `Enchanted`, `Remembered`, `Self`, `Targeted`, `TriggeredCard`, `TriggeredNewCardLKICopy`, `TriggeredTargetLKICopy`, `Valid Creature.IsSuspected`, `Valid Creature.OppCtrl+IsSuspected`, `ValidAll Card.YouOwn+!IsRemembered+IsCommander`
- `IncludeAllComponentCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberAltered$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAbsolve`, `DBAnimate`, `DBCleanup`, `DBDemote`, `DBEffect`, `DBGoad`, `DBToken`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.OppCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Creature.YouOwn+YouCtrl`, `Mount.YouCtrl`, `Mount.YouCtrl,Vehicle.YouCtrl`

## `Amass`

TODO: Write documentation.

**Parameters:**
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Morbid`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Discarded`, `Sacrificed`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Creature`, `Creature.Legendary`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<2/LOYALTY>`, `X X B T`, `1`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberAmass$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBImmediateTrig`, `DBMill`, `DBPump`, `DBPumpAll`, `IgnitionDamage`, `TrigMill`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Orc`, `Sliver`, `Zombie`

## `Animate`

TODO: Write documentation.

**Parameters:**
- `Abilities$`: TODO: Describe this parameter.
  Observed values: `ABArtisanRenew`, `ABBuzz`, `ABChangeZone`, `ABDealDamage`, `ABDoodle`, `ABDraw`, `ABFight`, `ABLife`, `ABMana`, `ABPump`, `ABPutCounter`, `ABRegen`, `ABRegenerate`, `ABShuffle`, `ABToken`, `ABTurn`, `ABUntap`, `ABWhack`, `ClueSac`, `DBMana`, `FoodSac`, `Martyr`, `Pump`, `Regen`, `SetessanFight`, `ThreeG`, `TreasureSac`, `Untap`
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Solved`, `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AddAllCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `AddSVar$`: TODO: Describe this parameter.
  Observed values: `DBArtisanAnimate`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Attacking`, `BoneManCantRegenerate`, `Curse`, `EOT`, `PTByCMC`, `SetPT`, `ValuableAttackerOrBlocker`, `Worst`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Creature.untapped+YouCtrl`, `Creature.YouCtrl`, `Land.OppCtrl`
- `AITgtsStrict$`: TODO: Describe this parameter.
  Observed values: `True`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Hand`, `Sacrifice`, `SacrificeCtrl`, `YourExile`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `CountAll`, `FormidableTest`, `X`
- `Colors$`: TODO: Describe this parameter.
  Observed values: `All`, `Black`, `Black,Green`, `Black,Red`, `Blue`, `Blue,Black`, `Blue,Red`, `ChosenColor`, `Colorless`, `Green`, `Green,Blue`, `Green,White`, `Red`, `Red,Green`, `Red,White`, `White`, `White,Black`, `White,Blue`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Doodles`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `TriggeredCardLKICopy`, `TriggeredTargetLKICopy`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `W`
- `ConditionNotPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.token`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.bargained`, `Card.cmcGE4`, `Card.Creature+inZoneStack`, `Card.inZoneBattlefield`, `Card.Land`, `Card.nonCreature`, `Card.Self+Angel`, `Card.Self+Citizen`, `Card.Self+Cleric`, `Card.Self+Detective`, `Card.Self+nonCreature`, `Card.Self+Scout`, `Card.Self+Soldier`, `Card.Self+Spirit`, `Card.Self+Warrior`, `Card.withoutAt the beginning of your upkeep, destroy this creature unless you pay {1} for each music counter on it`, `Creature`, `Creature.nonAngel`, `Land`, `Permanent`, `Vehicle`
- `ConditionPresent2$`: TODO: Describe this parameter.
  Observed values: `Card.Self+IsSaddled`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 G`, `T`, `2`, `2 T`, `3 T`, `AddCounter<0/LOYALTY>`, `1`, `S S`, `4 R G`, `W`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Pay half your life, rounded up:`, `{2}, Discard a Spirit or Arcane card:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Enchanted`, `Equipped`, `Imprinted`, `ParentTarget`, `Remembered`, `ReplacedCard`, `Self`, `Targeted`, `Targeted.!Creature`, `Targeted.Creature`, `Targeted.nonCreature+nonVehicle`, `Targeted.nonVehicle`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredTargetLKICopy`, `Valid Creature.YouCtrl+Other`, `ValidCommand Effect.namedRaging River Left`, `ValidCommand Effect.namedRaging River Left+IsImprinted`, `ValidCommand Effect.namedRaging River Right`, `ValidCommand Effect.namedRaging River Right+IsImprinted`, `ValidGraveyard Card.Legendary+YouOwn`, `ValidGraveyard Creature.YouOwn`, `ValidLibrary Land.TopLibrary_Land+YouCtrl`
- `DefinedDesc$`: TODO: Describe this parameter.
  Observed values: `That creature`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `AsLongAsControl`, `AsLongAsInPlay`, `Permanent`, `Perpetual`, `UntilAnimatedFaceup`, `UntilEndOfCombat`, `UntilEndOfTurn`, `UntilHostLeavesPlay`, `UntilTheEndOfYourNextUpkeep`, `UntilUntaps`, `UntilYourNextTurn`, `UntilYourNextUpkeep`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `HiddenKeywords$`: TODO: Describe this parameter.
  Observed values: `CARDNAME can't attack or block.`, `CARDNAME can't block.`, `CARDNAME must be blocked if able.`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintCards$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `Incorporate$`: TODO: Describe this parameter.
  Observed values: `1 B`, `1 G`, `R`, `U`, `W`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+!Spirit`, `Card.Self+!withDefender`, `Creature.YouCtrl`, `Planeswalker.YouCtrl+Oko`
- `Keywords$`: TODO: Describe this parameter.
  Observed values: `At the beginning of your upkeep, destroy this creature unless you pay {1} for each music counter on it`, `Bloodthirst:3`, `Bushido:1`, `Crew:2`, `Deathtouch`, `Defender`, `Devour:5`, `Double Strike`, `Enchant:Creature`, `Enchant:Creature.IsRemembered:creature put onto the battlefield with CARDNAME`, `Equip:2`, `Equip:3`, `Fear`, `First Strike`, `Flying`, `Flying & First Strike`, `Flying & First Strike & Lifelink & Hexproof`, `Flying & Haste`, `Flying & Hexproof`, `Flying & Indestructible & Haste`, `Flying & Infect`, `Flying & Lifelink`, `Flying & Protection from red`, `Flying & Trample`, `Flying & Trample & Haste`, `Flying & Vigilance`, `Flying & Ward:1`, `Haste`, `Haste & Hexproof`, `Haste & Menace`, `Haste & Reach`, `Hexproof`, `Indestructible`, `Indestructible & Haste & Vigilance`, `Indestructible & Toxic:9`, `Lifelink`, `Menace`, `Menace & Deathtouch`, `Menace & Deathtouch & Haste`, `Protection:Player.Opponent:each of your opponents`, `Reach`, `Reach & Haste`, `Sunburst`, `Trample`, `Trample & Haste`, `Trample & Indestructible & Haste`, `Trample & Lifelink`, `Vigilance`, `Vigilance & Double team`, `Vigilance & Haste`, `Vigilance & Hexproof & Haste`, `Vigilance & Indestructible`, `Vigilance & Indestructible & Haste`, `Ward:1`, `Ward:2`, `Ward:3`, `Wither`
- `LeaveBattlefield$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `ManaCost$`: TODO: Describe this parameter.
  Observed values: `5`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `3`
- `Name$`: TODO: Describe this parameter.
  Observed values: `Everflame, Heroes' Legacy`, `Fenric`, `Mileva, the Stalwart`, `Vitu-Ghazi`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionQuestion$`: TODO: Describe this parameter.
  Observed values: `TARGETS become a legendary Equipment artifact named Everflame, Heroes' Legacy.`
- `OverwriteColors$`: TODO: Describe this parameter.
  Observed values: `True`
- `OverwriteSpells$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `Power$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `diePwr`, `DracoPwr`, `GideonPT`, `SetPwr`, `Targeted$CardToughness`, `W`, `X`, `Y`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Animate Walking Statue —`, `Death Gigas`, `Formidable —`, `Galian Beast`, `Hellmasker`, `Sokratic Dialogue`, `Solved —`, `Threshold —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberAnimated$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `RememberedCard`, `RememberedLKI`, `TriggeredCardController`
- `RemoveAllAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveEnchantmentTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveKeywords$`: TODO: Describe this parameter.
  Observed values: `Defender`, `Enchant:Creature`, `Enchant:Creature.inZoneGraveyard:creature card in a graveyard`, `First Strike`, `Flying`, `Trample`
- `RemoveLandTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveNonManaAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveThisAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Creature`, `Equipment`, `Human`, `Snow`
- `Replacements$`: TODO: Describe this parameter.
  Observed values: `DBYouCantLose,DBOppCantWin`, `Delusional`, `ETBAddCounter`, `ETBShield`, `EtherealGrasp`, `Exile`, `FungalFunk`, `PerpDamageRep`, `ReplaceDies`, `ReplaceETB`, `ReplaceLeaves`, `RPrevent`
- `RevertCost$`: TODO: Describe this parameter.
  Observed values: `1`, `B`, `G`, `R`, `U`, `W`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `staticAbilities$`: TODO: Describe this parameter.
  Observed values: `AnyType`, `AttackOwner`, `BlockRestrict`, `BoneShamanStatic`, `CanAttack`, `CantAttackOwner`, `CantBlock`, `CantBlock,NoDamageRemoval`, `CarnageMustAttack`, `CDT`, `DamageNotRemoved`, `EquipPump`, `FreeCast`, `Hunger`, `IndestructibleAspect`, `LoseFlyingStatic`, `MustAttack`, `PerpAltCost`, `PerpetualEffect`, `PerpetualMustAttack`, `PerpetualRaiseCost`, `PerpetualReduce`, `Play`, `RaiseCost`, `ReduceCost`, `SCantSac`, `SpendAnyMana`, `Static`, `STFirstStrike`, `StLandPT`, `STMayPlay`, `StPlay`, `Unblockable`, `VeiledSerpentST`, `WhipgrassCantAttack,WhipgrassCantBlock`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AniBuzz`, `AniDoodle`, `DBAddSVar`, `DBAnimate`, `DBAttach`, `DBChangeZone`, `DBChangeZone2`, `DBChoose`, `DBCleanChosen`, `DBCleanup`, `DBCleanUp`, `DBCleanup1`, `DBConjure`, `DBCounter`, `DBDamage`, `DBDamageAll`, `DBDealDamage`, `DBDelayedTrigger`, `DBDelTrig`, `DBDraw`, `DBEffect`, `DBExile`, `DBFight`, `DBGainLife`, `DBGoad`, `DBGrow`, `DBLeftPump`, `DBMakeCard`, `DBMayPlayEffect`, `DBPrevent`, `DBProtection`, `DBPump`, `DBPumpCleric`, `DBPumpPhyrexian`, `DBPutCounter`, `DBPutFromHand`, `DBRemoveTimeCounterOtherCardsInExile`, `DBReturn`, `DBRightPump`, `DBShuffle`, `DBTimeTravel`, `DBUnblockable`, `DBUntap`, `DelayedExile`, `DelTrig`, `DelTrigSlowtrip`, `DestroyPacifist`, `EffDraw`, `EOTSac`, `ExileSelf`, `GideonPrevent`, `LightformAttach`, `NecromAttach`, `NonVehicle`, `NotifyWhack`, `PumpVehicle`, `PutCounter`, `RageformAttach`, `TrigTempt`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE8`, `GE9`
- `sVars$`: TODO: Describe this parameter.
  Observed values: `AE`, `KheruMustAttack`, `MustBeBlocked`, `OdinMustBeBlocked`, `SneakAttackEOT`, `WhipMustAttack`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `MaxTargets`, `MaxTgt`, `MaxTgts`, `OneEach`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `X`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackedTarget`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Graveyard`, `Graveyard`, `Stack`, `Stack,Battlefield`
- `Toughness$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `12`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `dieTgn`, `DracoTgn`, `GideonPT`, `SetTgn`, `X`, `Y`, `Z`
- `TransferActivator$`: TODO: Describe this parameter.
  Observed values: `True`
- `Triggers$`: TODO: Describe this parameter.
  Observed values: `AbnormalEnduranceChangeZone`, `AttackTrig`, `AttackTrigger`, `BailOutTrigCZ`, `BecomesTarget`, `BiggerDies`, `CarnageDamage`, `CastSpellDrawGainLife`, `CastSpellGetPoison`, `CastSpellLoseLife`, `CastTrig`, `CastTrigger`, `CDTrigger`, `CombatTrig`, `CrashLand`, `DamageDraw`, `DamageSac`, `DamageTrig`, `DamageTrig19`, `DamageTrigger`, `DealsDamage`, `DestroyTrigger`, `Dies`, `DiesTrig`, `DiesTrigger`, `DieTrig`, `DieTrigger`, `DrawTrig`, `EndofTurnShock`, `EOTSac`, `EquippedCombatDamage`, `ETBAttach`, `ETBExile`, `ETBFight`, `ETBTrig`, `Exiled`, `FlamePhoenixChangeZone`, `GalufDeath`, `HunterProwessTrig`, `KellanCombat`, `LandEnter`, `LandETBDraw`, `LandTapDraw`, `LeavesGrave`, `LeavesTrig`, `LeaveTrigger,EndTrigger`, `ManaTap`, `OpenIntoWonderTrigger`, `PerigeeBeckonerChangeZone`, `PerpetualUpkeep`, `PhaseTrig`, `PingUpkeep`, `PseudoLifelink`, `SacTrig`, `Shackles`, `SpellCastTrig`, `SupernaturalStaminaChangeZone`, `SymbioteTrig`, `TapTrig`, `TrigAethermage`, `TrigAttack`, `TrigCDPlayer`, `TrigChangeZone`, `TrigDamage`, `TrigDamageDealtOnce`, `TrigDamageDone`, `TrigDeath`, `TrigDie`, `TrigDieExile`, `TrigDies`, `TrigETBHatchling`, `TrigGlyphUpkeep`, `TrigMusicianPay`, `TrigOlivia`, `TrigRemoveCounter,TrigCast`, `TrigRemoveEgg`, `TrigSporeUpkeep`, `TrigUpkeep`, `TrigVraska`, `TWhenLastTimeCounterRemoved`, `UpkeepCostTrigger`, `UpkeepTrig`, `VerdantRebirthChangeZone`, `WarriorLessonDmg`
- `Types$`: TODO: Describe this parameter.
  Observed values: `Angel`, `Angel,Artifact,Creature`, `Angel,Spirit,Warrior`, `Artifact`, `Artifact,Creature`, `Artifact,Creature,Angel`, `Artifact,Creature,Assembly-Worker`, `Artifact,Creature,Beast`, `Artifact,Creature,Bird`, `Artifact,Creature,Construct`, `Artifact,Creature,Crab`, `Artifact,Creature,Devil`, `Artifact,Creature,Dinosaur`, `Artifact,Creature,Dragon`, `Artifact,Creature,Elemental`, `Artifact,Creature,Giant`, `Artifact,Creature,Golem`, `Artifact,Creature,Homunculus`, `Artifact,Creature,Horror`, `Artifact,Creature,Insect`, `Artifact,Creature,Phyrexian,Construct`, `Artifact,Creature,Phyrexian,Eye`, `Artifact,Creature,Robot`, `Artifact,Creature,Robot,Villain`, `Artifact,Creature,Shapeshifter`, `Artifact,Creature,Soldier`, `Artifact,Creature,Spirit`, `Artifact,Creature,Thrull`, `Artifact,Creature,Wolf`, `Artifact,Equipment`, `Artifact,Robot`, `Artifact,Treasure`, `Assassin`, `Aura`, `Avatar`, `Basic,Island`, `Bear,Beserker`, `Bird`, `Bird,Creature`, `Bird,Giant`, `Boar,Spirit`, `Cat`, `ChosenType`, `Citizen`, `Citizen,Creature`, `Clue,Artifact`, `Coward`, `Crab`, `Creature`, `Creature,Angel`, `Creature,Ape`, `Creature,Artifact`, `Creature,Artifact,Atog`, `Creature,Artifact,Bear`, `Creature,Artifact,Beast`, `Creature,Artifact,Blinkmoth`, `Creature,Artifact,Cat`, `Creature,Artifact,Construct`, `Creature,Artifact,Dinosaur`, `Creature,Artifact,Elemental`, `Creature,Artifact,Golem`, `Creature,Artifact,Juggernaut`, `Creature,Artifact,Phyrexian,Blinkmoth`, `Creature,Artifact,Phyrexian,Horror`, `Creature,Artifact,Spirit`, `Creature,Artifact,Treefolk`, `Creature,Artifact,Turtle`, `Creature,Artifact,Wall`, `Creature,Bat`, `Creature,Bear`, `Creature,Beast`, `Creature,Beholder`, `Creature,Bird`, `Creature,Centaur`, `Creature,Citizen`, `Creature,Construct`, `Creature,Crocodile`, `Creature,Demon`, `Creature,Dinosaur`, `Creature,Dragon`, `Creature,Elemental`, `Creature,Elemental,Horror`, `Creature,Elephant`, `Creature,Elk`, `Creature,Elk,Beast`, `Creature,Faerie`, `Creature,Fractal`, `Creature,Frog`, `Creature,Fungus`, `Creature,Gargoyle`, `Creature,Giant`, `Creature,Gnome`, `Creature,Goblin`, `Creature,Horror`, `Creature,Human`, `Creature,Human,Soldier`, `Creature,Human,Soldier,Ally`, `Creature,Hydra`, `Creature,Illusion`, `Creature,Insect`, `Creature,Insect,Monk`, `Creature,Jackal`, `Creature,Knight`, `Creature,Legendary,Dragon`, `Creature,Legendary,Spirit`, `Creature,Llama`, `Creature,Monk`, `Creature,Monk,Avatar`, `Creature,Mutant`, `Creature,Nightmare`, `Creature,Octopus`, `Creature,Ox`, `Creature,Phyrexian,Horror`, `Creature,Phyrexian,Imp`, `Creature,Plant`, `Creature,Plant,Boar`, `Creature,Robot`, `Creature,Serpent`, `Creature,Shark`, `Creature,Skeleton`, `Creature,Soldier`, `Creature,Sphinx`, `Creature,Spider`, `Creature,Spirit`, `Creature,Treefolk`, `Creature,Turtle`, `Creature,Wall`, `Creature,Warrior`, `Creature,Warrior,Treefolk`, `Creature,Werewolf`, `Creature,Wizard`, `Creature,Zombie,Plant`, `Demon`, `Dinosaur`, `Dragon`, `Dragon,Illusion`, `Elemental,Creature`, `Elephant`, `Enchantment`, `Enchantment,Aura`, `Enchantment,Creature,Horror`, `Food,Artifact`, `Forest`, `Fractal`, `Frog`, `Giant`, `Goat`, `God`, `Halfling,Rogue`, `Halfling,Scout`, `Hero`, `Human`, `Human Cleric`, `Human,Cleric`, `Human,Detective`, `Human,Faerie,Detective`, `Human,Faerie,Rogue`, `Human,Warrior`, `Human,Warrior,Spirit`, `Illusion`, `Island`, `Kithkin,Avatar`, `Kithkin,Scout`, `Kithkin,Soldier`, `Kithkin,Spirit`, `Kithkin,Spirit,Warrior`, `Kithkin,Spirit,Warrior,Avatar`, `Land`, `Legendary,Artifact,Equipment`, `Legendary,Creature`, `Legendary,Creature,Elemental`, `Legendary,Creature,Horror`, `Legendary,Creature,Nightmare,God`, `Legendary,Spider,Hero`, `Lizard,Creature`, `Mutant`, `Phyrexian`, `Phyrexian,Human,Cleric`, `Pirate`, `Plains`, `Plant`, `Rabbit`, `Rat,Creature`, `Rhino`, `Rogue`, `Samurai`, `Serpent`, `Shapeshifter,Artifact,Creature`, `Skeleton`, `Snake`, `Snow`, `Spirit`, `Spirit,Warrior`, `Swamp`, `Vampire`, `Vampire,Artifact,Creature`, `Vehicle,Artifact`, `Warrior`, `Weird`, `Werewolf`, `Wolf,Creature`, `Wurm`, `Zombie,Knight`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/Creature>`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer`, `TargetedController`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Self`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact.nonCreature`, `Artifact.nonCreature+!token+YouCtrl,Land.nonCreature+!token+YouCtrl`, `Artifact.nonCreature+OppCtrl`, `Artifact.nonCreature+YouCtrl`, `Artifact.nonEquipment+YouCtrl`, `Artifact.OppCtrl,Creature.OppCtrl,Planeswalker.OppCtrl`, `Artifact.Other+!token+YouCtrl`, `Artifact.Other+YouCtrl`, `Artifact.Other,Creature.Other`, `Artifact.token+YouCtrl`, `Artifact.YouCtrl`, `Artifact.YouOwn`, `Blood.token+YouCtrl`, `Card`, `Creature`, `Creature,Vehicle`, `Creature.!token`, `Creature.Artifact`, `Creature.attacking`, `Creature.counters_GE1_P1P1`, `Creature.DefenderCtrl`, `Creature.Human+YouCtrl`, `Creature.Legendary`, `Creature.nonArtifact`, `Creature.nonGoat`, `Creature.nonWall+ActivePlayerCtrl+!firstTurnControlled`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+YouCtrl`, `Creature.Shapeshifter+YouCtrl`, `Creature.tapped`, `Creature.Vampire+YouCtrl+attacking+nonDemon`, `Creature.wasCastByYou+ThisTurnCast`, `Creature.withFlying`, `Creature.YouCtrl`, `Creature.YouOwn`, `Enchantment.nonAura+YouCtrl`, `Forest`, `Goblin.Other+YouCtrl`, `Instant,Sorcery`, `Land`, `Land.nonBasic+YouDontCtrl`, `Land.nonSnow+Basic`, `Land.OppCtrl`, `Land.Snow`, `Land.Snow+YouCtrl`, `Land.YouCtrl`, `Land.YouCtrl,Creature.YouCtrl`, `Mountain`, `Permanent`, `Permanent.nonLand`, `Permanent.nonLand+YouCtrl`, `Permanent.nonSnow`, `Permanent.Snow`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl`, `Swamp`, `Time Lord.YouCtrl`, `Vehicle`, `Vehicle.Other+YouCtrl`, `Vehicle.YouCtrl`, `Vehicle.YouCtrl+Other`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `artifact or creature`

## `AnimateAll`

TODO: Write documentation.

**Parameters:**
- `Abilities$`: TODO: Describe this parameter.
  Observed values: `ABControl`, `ABDamage`, `ABDealDamage`, `ABExplode`, `ABMana`, `ABPump`, `ABRegen`, `ABRemoveCounter`, `AnyMana`, `Counter`, `DrAbs`, `Fight`, `LVAbs`, `ShovingMatch`, `Sizzle`, `TapDestroy`, `ThrowPunch`, `TwoG`
- `AddAllCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `CreatureAdvantage`
- `CantHaveKeyword$`: TODO: Describe this parameter.
  Observed values: `Hexproof & Shroud`
- `Colors$`: TODO: Describe this parameter.
  Observed values: `Black`, `Blue`, `Green`, `Red`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE9`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `G`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Wraith+YouCtrl`, `Permanent.YouCtrl+Black`, `Permanent.YouCtrl+Blue`, `Permanent.YouCtrl+Green`, `Permanent.YouCtrl+Red`, `Permanent.YouCtrl+White`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 G G`, `1 T`, `G`, `2 R W`, `SubCounter<7/LOYALTY>`, `2 U B`, `2 G T Discard<2/Card>`, `Waterbend<X>`, `3 U U`, `1`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`, `Perpetual`, `UntilEndOfTurn`, `UntilYourNextTurn`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Keywords$`: TODO: Describe this parameter.
  Observed values: `Crew:2 & Trample & Haste`, `Deathtouch`, `Flying`, `Flying & Haste & Crew:1`, `Menace`, `Reach & Haste`, `Reach & Indestructible & Haste`, `Trample`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `OverwriteColors$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Power$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `2`, `3`, `4`, `5`, `6`, `7`, `9`, `X`
- `RemoveAllAbilities$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveKeywords$`: TODO: Describe this parameter.
  Observed values: `First Strike & Double Strike`, `Flying`, `Hexproof & Indestructible`, `Hexproof & Indestructible & Protection & Shroud & Ward`, `Hexproof & Shroud`, `Indestructible`, `Trample`
- `RemoveLandTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `Replacements$`: TODO: Describe this parameter.
  Observed values: `BrittleExile`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `staticAbilities$`: TODO: Describe this parameter.
  Observed values: `Cowardly`, `DragonReduceCost`, `DragonReduceCost,DragonAltCost`, `MinMaxBlocked`, `PerpetualRaiseCost`, `ReduceCost`, `Static`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AnimateSwamp`, `ArmDwarf`, `BlindFuryEffect`, `DBAnimateB`, `DBAnimateG`, `DBAnimateR`, `DBAnimateU`, `DBCleanup`, `DBDamage`, `DBDealDamage`, `DBDestroyAll`, `DBExileSelf`, `DBPump`, `DBPumpAll`, `DBSearch`, `UPaid`
- `Toughness$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `2`, `3`, `4`, `5`, `6`, `9`, `X`, `Y`
- `Triggers$`: TODO: Describe this parameter.
  Observed values: `AttackTrig`, `CastSpellLoseLife`, `DamageTrig`, `DiesTrig`, `DiesTrigger`, `ETBToken`, `Trig`, `Trig1`, `Trig2`, `TrigCDPlayer`, `TrigPrideDamage`, `TurnedFaceUp`
- `Types$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Construct,Assassin`, `ChosenType`, `Coward`, `Creature`, `Creature,Artifact`, `Creature,Dragon`, `Creature,Elemental`, `Creature,Elk`, `Creature,Plant`, `Creature,Treefolk`, `Dinosaur`, `Enchantment`, `Frog`, `Kindred,Elemental`, `Phyrexian`, `Shade`, `Swamp`, `Vehicle`, `Werewolf`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Angel.YouCtrl`, `Artifact.nonCreature+YouCtrl`, `Artifact.nonCreature+YouCtrl+nonVehicle`, `Artifact.Treasure+YouCtrl`, `Artifact.YouCtrl`, `Card.IsRemembered`, `Card.nonLand+cmcLE3+YouOwn`, `Card.nonLand+OwnedBy TriggeredDefendingPlayer`, `Card.nonLand+YouOwn`, `Card.Wizard+YouCtrl`, `Card.YouOwn+sharesCardTypeWith Remembered`, `Clue.Other+YouCtrl`, `Creature`, `Creature,Vehicle`, `Creature.attacking+Other`, `Creature.blockedBySource,Creature.blockingSource`, `Creature.Colorless+YouCtrl`, `Creature.ControlledBy RememberedController+!IsRemembered`, `Creature.Damaged`, `Creature.Elf+YouCtrl`, `Creature.faceDown+YouCtrl`, `Creature.modified+YouCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.Spirit+YouCtrl`, `Creature.StrictlyOther`, `Creature.StrictlyOther+YouCtrl`, `Creature.TargetedPlayerCtrl`, `Creature.unblocked`, `Creature.withFlying+attacking`, `Creature.YouCtrl`, `Creature.YouCtrl+!token+faceUp`, `Creature.YouCtrl+attacking`, `Creature.YouCtrl+Black,Creature.YouCtrl+Blue,Creature.YouCtrl+White`, `Creature.YouCtrl+ChosenType`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Outlaw`, `Creature.YouOwn`, `Dragon.YouOwn`, `Forest.YouCtrl`, `Forest.YouOwn`, `Forest.YouOwn,Treefolk.YouOwn`, `Instant.nonElemental+YouOwn,Sorcery.nonElemental+YouOwn`, `Land`, `Land.YouCtrl`, `Permanent.nonLand+OppCtrl`, `Permanent.OppCtrl`, `Permanent.YouCtrl`, `Permanent.YouOwn`, `Planeswalker.YouCtrl`, `Soldier.YouCtrl`, `Sorcery.YouOwn,Instant.YouOwn`, `Targeted.sameName`, `Thopter.YouCtrl`, `Vampire.YouCtrl`, `Vehicle.YouCtrl`, `Wraith.YouCtrl`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `XMin$`: TODO: Describe this parameter.
  Observed values: `1`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Hand`, `Graveyard,Hand,Library`, `Hand`, `Hand,Library`

## `AssembleContraption`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`, `Result`, `X`, `Y`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W Sac<1/Artifact.Other/another artifact>`, `4`, `3 W Sac<X/Contraption>`, `1`, `6 T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, sacrifice X Contraptions.`
- `DefinedAssembler$`: TODO: Describe this parameter.
  Observed values: `ReplacedCause`, `Self`
- `DefinedContraption$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `Reassemble$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Contraption.ControlledBy TriggeredTarget`, `Contraption.YouCtrl`

## `AssignGroup`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `FriendOrFoe`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `DBSearch,DBSacrifice`, `DBToHand,DBSacrifice`, `FriendRepeat,FoeBounce`, `FriendRepeat,FoeRepeat`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`
- `SpellDescription$`: TODO: Describe this parameter.

## `Attach`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Curse`, `GainControl`, `InstantReequipPowerBuff`, `MoveTgtAura`, `PowerDmg`, `Pump`, `Unenchanted`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Warrior`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.YouCtrl`, `Creature.YouCtrl,Land.YouCtrl`, `Equipment.Attached`, `Equipment.YouCtrl`, `Equipment.YouCtrl+!IsRemembered`, `Equipment.YouCtrl+IsRemembered`, `Instant`, `Land`, `Permanent`, `Permanent.sharesCardTypeWith AttachedBy Targeted`, `Permanent.sharesControllerWith AttachedBy Targeted`, `Permanent.sharesControllerWith Targeted`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a creature`, `Choose a creature you control`, `Choose a creature you control to attach Breath of Fury to`, `Choose a player to attach this Curse to`, `Choose an equipment to attach to this creature`, `Choose an equipment to attach to this token`, `Choose an Equipment you control`, `You may choose a creature you control to attach that equipment to`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`, `You`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Remembered`, `TriggeredCardLKICopy`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Aura`, `Card`, `Card.Equipment`, `Equipment`, `Warrior`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `Sac<1/Permanent.Other/another permanent>`, `B B`, `4 T`, `1 W`, `W W`, `G G`, `2 U`, `U U`, `1 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ChosenPlayer`, `DelayTriggerRememberedLKI`, `Imprinted`, `ParentTarget`, `ParentTarget.attacking`, `Remembered`, `Self`, `Targeted`, `TriggeredCardLKICopy`, `Valid Dwarf.YouCtrl`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Move$`: TODO: Describe this parameter.
  Observed values: `True`
- `Object$`: TODO: Describe this parameter.
  Observed values: `AttachedTo Targeted.Aura,Equipment`, `AttachedTo TriggeredAttackerLKICopy.Equipment`, `AttachedTo TriggeredCardLKICopy.Equipment`, `ChosenCard`, `DelayTriggerRememberedLKI`, `Imprinted`, `OriginalHost`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredCard`, `TriggeredCardLKICopy`, `Valid Aura.AttachedTo Targeted`, `Valid Aura.YouCtrl,Equipment.YouCtrl`, `Valid Equipment`, `Valid Equipment.YouCtrl`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerChoices$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `RememberAttached$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CatchBreath`, `DBAmass`, `DBCleanup`, `DBDamage`, `DBDelay`, `DBDelayTrig`, `DBDestroy`, `DBDraw`, `DBEffect`, `DBImmediateTrigger`, `DBPump`, `DBPutCounter`, `DBTapAll`, `DBUntap`, `WretchedCleanup`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MaxTargets`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Aura.AttachedTo Creature`, `Aura.AttachedTo Creature,Aura.AttachedTo Land`, `Aura.AttachedTo Permanent`, `Creature`, `Creature.!EnchantedBy`, `Creature.attacking`, `Creature.ControlledBy TriggeredTarget`, `Creature.Legendary+YouCtrl`, `Creature.nonHuman+YouCtrl`, `Creature.OppCtrl`, `Creature.Pirate+YouCtrl`, `Creature.tapped`, `Creature.YouCtrl`, `Creature.YouCtrl+Legendary`, `Equipment`, `Equipment.cmcEQ2+YouCtrl,Equipment.cmcEQ3+YouCtrl`, `Equipment.YouCtrl`, `Knight.YouCtrl`, `Permanent`, `Permanent,Player`, `Rebel.YouCtrl`

## `Balance`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BalanceCreaturesAndLands`, `BalancePermanents`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 W T Sac<1/CARDNAME>`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `BalanceCreatures`, `BalanceHands`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Land`, `Permanent`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Hand`

## `BecomeMonarch`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 R T Sac<1/NICKNAME>`, `4 T Sac<1/CARDNAME>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredTarget`, `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDamage`, `DBNoMonarch`, `DBPower`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `BecomesBlocked`

TODO: Write documentation.

**Parameters:**
- `ActivationAfterBlockers$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Blockers`, `Declare Blockers->EndCombat`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Valid Creature.attacking`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDamage`, `DelTrigSlowtrip`, `Draw`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `MaxTgt`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking`, `Creature.attacking+unblocked`

## `BidLife`

TODO: Write documentation.

**Parameters:**
- `AIBidMax$`: TODO: Describe this parameter.
  Observed values: `10`, `8`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Min`
- `BidSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBLoseLife`
- `OtherBidder$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `SpellDescription$`: TODO: Describe this parameter.
- `StartBidding$`: TODO: Describe this parameter.
  Observed values: `1`, `Any`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`

## `BlankLine`

TODO: Write documentation.

**Parameters:**
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBVote`

## `Blight`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `YourMainPhase`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `PayLife<1> Blight<2>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `Block`

TODO: Write documentation.

**Parameters:**
- `DefinedAttacker$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`
- `DefinedBlocker$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`

## `Branch`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BranchCounter`, `GrislySigil`, `TgtAttacker`
- `BranchConditionSVar$`: TODO: Describe this parameter.
  Observed values: `AltCostPaid`, `Celebration`, `CMCRememberedCard`, `Count$CardCounters.BORE`, `Count$CardCounters.TIME`, `Count$ChosenSize`, `Count$Valid Card.Self+IsSaddled`, `Count$Valid Card.Self+IsSuspected`, `Count$Valid Leech.YouCtrl`, `CountCounters`, `Ember`, `FlameTimer`, `FullyCharged`, `HasUnearth`, `HatchTimer`, `LifeCheck`, `NumImprintedCard`, `NumRememberedCard`, `NumRingTempted`, `PlayerCountOpponents$HasPropertyNotedForSilence`, `PlayerCountOpponents$HasPropertyNotedForSnitch`, `PlayerCountPropertyYou$ExploredThisTurn`, `PlayerCountPropertyYou$HasPropertyNotedForBattleBolas`, `PlayerCountPropertyYou$HasPropertyNotedForBattleUgin`, `Power`, `Remembered$CardManaCost`, `ReplicateTimer`, `Ritual`, `Soul`, `Sum`, `TargetCheck`, `TreasureCheck`, `TriggerCount$Result`, `UrzaCheck`, `WasCast`, `X`, `XMarksTheSpot`, `Y`
- `BranchConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQ3`, `EQ4`, `EQCMCImprintedCard`, `EQPlayerCountOpponents$Amount`, `GE1`, `GE10`, `GE2`, `GE3`, `GE4`, `GE5`, `GE6`, `GE7`, `GE8`, `GE9`, `GEY`, `GT0`, `GT16`, `GTCMCImprintedCard`, `GTY`, `LE0`, `LE1`, `LTX`, `LTY`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `R G`, `2 W`, `3`, `2 B`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredTarget`
- `FalseSubAbility$`: TODO: Describe this parameter.
  Observed values: `ConjurePlains`, `CounterUnless`, `Crew`, `Damage1`, `Damage12`, `DBAddCounter`, `DBBottom`, `DBBranchTwo`, `DBCastAgain`, `DBChangeZone2`, `DBChangeZoneAll2`, `DBChooseOpp`, `DBCleanup`, `DBCompareCMC2`, `DBConjure`, `DBConjureTwo`, `DBDamage`, `DBDestroyAll`, `DBDiscard`, `DBDiscard2`, `DBDraw`, `DBDraw2`, `DBDrawX`, `DBEffect`, `DBExile`, `DBFizzle`, `DBFood`, `DBGainLife`, `DBImprint`, `DBLoseLife`, `DBLoseLife2`, `DBPlant`, `DBProliferate`, `DBPump`, `DBPump2`, `DBPumpTwo`, `DBPutCounter`, `DBSac`, `DBScry`, `DBSearch`, `DBSnitchBranch`, `DBSpirit`, `DBSuspect`, `DBToken`, `DBUntap`, `DealDamage`, `Destroy`, `DestroyAttacker`, `Destruction`, `Draw`, `GainLife`, `GuidedLand`, `Mill`, `NonLegendary`, `NormalTokens`, `NotEquipped`, `Pump`, `PutCounter`, `PutCounterTwo`, `PutLand`, `Return`, `ReturnUpToTwo`, `Scry2`, `SearchLibrary`, `Seek1`, `SuspectIt`, `Tap`, `ToHand`, `Token`, `TrigFlashbackUnsaddled`, `TrigTempt`, `WasteLand`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCleanupRemembered`, `DBExile`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Stack`
- `TrueSubAbility$`: TODO: Describe this parameter.
  Observed values: `AttackingTokens`, `Blink`, `Captain`, `CastFromHand`, `Counter`, `CounterScry`, `Damage3`, `Damage4`, `Damage8`, `DBAltCostEffect`, `DBAngel`, `DBAnimate`, `DBChangeZone`, `DBChangeZone1`, `DBChangeZoneAll1`, `DBCheckImprinted`, `DBCompareCMC`, `DBConjure`, `DBConjureAll`, `DBCopy`, `DBDiscard`, `DBDiscardAll`, `DBDraw`, `DBDraw1`, `DBDuress`, `DBEffect2`, `DBExtraTurn`, `DBGenericChoice`, `DBHand`, `DBImprint`, `DBImprintForget`, `DBLoseLife1`, `DBManifestHand`, `DBPump1`, `DBPutCounter`, `DBRadiation`, `DBRemoveAll`, `DBRemoveCounter`, `DBRemoveCounters`, `DBRemoveCtrs`, `DBSac`, `DBSacrifice`, `DBSeek`, `DBTap`, `DBToken`, `DBTreasureDiscard`, `DBUntapAll`, `DBZombie`, `Draw`, `Draw4`, `Equipped`, `ExileAbility`, `ExileDemon`, `ExileHand`, `ExileIt`, `GainLife`, `Legendary`, `OppChooses`, `OppDiscard`, `OppDraw`, `OppShare`, `PutCounter`, `PutCounterOne`, `PutCreatureLand`, `PutLandCreature`, `RampantLand`, `RemoveCombat`, `ReturnAll`, `Seek2`, `ThreshDestroy`, `ThreshDestruction`, `ThreshWaste`, `ToBattlefieldTapped`, `Tokens`, `TrigFlashbackSaddled`, `TrigTheyLose`, `WinGame`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`, `Creature,Planeswalker`, `Creature.attacking`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Land`, `Opponent`, `Permanent.YouCtrl`, `Player`

## `Camouflage`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BestBlocker`
- `Defender$`: TODO: Describe this parameter.
  Observed values: `ReplacedDefendingPlayer`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ReplacedPlayer`

## `ChangeCombatants`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `WeakestOppExceptCtrl`
- `Attacking$`: TODO: Describe this parameter.
  Observed values: `.Defending & Valid Planeswalker.Defending`, `Player.OpponentOf CardController`, `RememberedPlayer`, `TargetedPlayer`, `True`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.YouCtrl`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`, `Valid Creature.attacking`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ArmorClean`, `DBCleanup`, `DBDelayTrig`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `MaxTargets`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `Player.OpponentOf ParentTarget`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking`

## `ChangeSpeed`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `TargetedController$Speed`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GTPlayerCountDefinedNonTargetedController$HighestSpeed`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `Decrease`

## `ChangeTargets`

TODO: Write documentation.

**Parameters:**
- `ChangeSingleTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `ImprintedOwner`, `Player.IsRemembered`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `Player.Chosen`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionTargetsSingleTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionTargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Creature.inZoneBattlefield`, `Permanent.YouCtrl+inRealZoneBattlefield,You`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `RevealChosen<Player>`, `Sac<1/CARDNAME>`, `U`, `X T`, `UP`, `R`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `SourceFirstSpell`, `Targeted`, `TriggeredSourceSA`, `TriggeredSpellAbility`, `ValidStack SpellAbility`
- `DefinedMagnet$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Self`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomTargetRestriction$`: TODO: Describe this parameter.
  Observed values: `Player.Other,Permanent.YouDontCtrl`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCleanupImprinted`, `DBCopy`, `DBDraw`, `DBLoseLife`
- `TargetRestriction$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.Other`, `Player`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Activated.singleTarget`, `Instant.singleTarget,Sorcery.singleTarget`, `Spell`, `Spell,Activated,Triggered`, `Spell.numTargets EQ1`, `Spell.numTargets EQ1+IsTargeting Self`, `Spell.singleTarget`, `Spell.singleTarget+IsTargeting You`, `SpellAbility.numTargets EQ1+IsTargeting Self`, `SpellAbility.singleTarget`
- `TargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `Creature.inRealZoneBattlefield`, `Player`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card,Emblem`, `Card.Arcane`, `Instant,Sorcery`, `Spell`

## `ChangeText`

TODO: Write documentation.

**Parameters:**
- `ChangeColorWord$`: TODO: Describe this parameter.
  Observed values: `Choose Choose`
- `ChangeTypeWord$`: TODO: Describe this parameter.
  Observed values: `ChooseBasicLandType ChooseBasicLandType`, `ChooseCreatureType ChooseCreatureType`, `ChooseCreatureType Vampire`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `ForbiddenNewTypes$`: TODO: Describe this parameter.
  Observed values: `Wall`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCumUpkeep`, `DBDraw`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack,Battlefield`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`, `Enchantment.YouCtrl+White+withoutCumulative upkeep`

## `ChangeX`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredSpellAbility`

## `ChangeZone`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Metalcraft`, `Solved`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Declare Attackers`, `Upkeep`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `You.NonActive`
- `AILifeThreshold$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AnyMainPhase`, `AtOppEOT`, `BeforeCombat`, `BestCard`, `BounceOnce`, `BounceOwnTrigger`, `Curse`, `DeathgorgeScavenger`, `DelayedBlink`, `ExileCombatThreat`, `ExileGraveyards`, `ExilePreference:HighestCMC`, `ExilePreference:Land`, `ExilePreference:MostProminentNonLandNonExiledOwnType`, `ExilePreference:MostProminentOppType`, `ExilePreference:MostProminentOwnType`, `ExtraplanarLens`, `Good`, `IfNotBuffed`, `Intuition`, `Main1`, `Mairsil`, `MazesEnd`, `MimicVat`, `MostProminentInComputerGraveyard`, `MostProminentOppControls`, `Necropotence`, `NeverBounceItself`, `NoSameCreatureType`, `Polymorph`, `Pongify`, `PriorityOptionalCost`, `Pump`, `ReanimateAll`, `ReturnCastable`, `SacAndRetFromGrave`, `SacAndUpgrade`, `SacAndUpgrade+SacWorst`, `SaviorOfOllenbock`, `SorinVengefulBloodlord`, `SurpriseBlock`, `SurvivalOfTheFittest`, `TheScarabGod`, `WorstCard`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `G`, `U`
- `AIMinTgts$`: TODO: Describe this parameter.
  Observed values: `3`
- `AISearchGoal$`: TODO: Describe this parameter.
  Observed values: `Creature.Green`
- `AITgtOwnCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `!Creature`, `BetterThanSource`, `Card.cmcGE3`, `Card.cmcGE3,Card.powerGE3`, `Card.cmcGE5`, `Card.Other`, `Card.SharesColorWith MostProminentColor`, `Card.YouOwn`, `Creature`, `Creature.cmcGE6`, `Creature.OppCtrl+attacking,Creature.OppCtrl+blocking`, `Creature.OppOwn`, `Creature.Other+YouOwn+cmcGE3`, `Creature.YouOwn`, `Vampire.cmcLE3+OppCtrl`
- `AIXMax$`: TODO: Describe this parameter.
  Observed values: `Y`
- `AlreadyRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `AlternateCost$`: TODO: Describe this parameter.
  Observed values: `B T`, `U T`
- `AlternativeDecider$`: TODO: Describe this parameter.
  Observed values: `RememberedOwner`, `TargetedOwner`, `ThisTargetedOwner`
- `AlternativeMessage$`: TODO: Describe this parameter.
  Observed values: `Would you like to search your library with this ability? If you do, your library will be shuffled`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `Exiled`, `X`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many white cards to exile`
- `AnnounceType$`: TODO: Describe this parameter.
  Observed values: `CreatureType`
- `AnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Hand`, `Sacrifice`, `YourSacrifice`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `AttachAfter$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `AttachedTo$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Creature`, `Creature.sharesCreatureTypeWith TriggeredCardLKICopy`, `Creature.YouCtrl`, `DelayTriggerRememberedLKI`, `Imprinted`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `TriggeredCardLKICopy`, `TriggeredSourceLKICopy`, `Valid Creature.EnchantedBy`, `Valid Creature.IsRemembered`
- `AttachedToPlayer$`: TODO: Describe this parameter.
  Observed values: `EnchantedPlayer`, `ParentTarget`, `You`
- `Attacking$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer & Valid Planeswalker.ControlledBy DefendingPlayer`, `TriggeredDefender`, `TriggeredTarget`, `True`
- `Blocking$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttacker`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChangeNum$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `2`, `3`, `4`, `5`, `7`, `Count$RememberedSize`, `Count$Valid Creature.SaddledThisTurn`, `Count$ValidHand Card.YouOwn`, `Count$YourSpeed`, `CountAuras`, `FetchCount`, `FetchX`, `GraveX`, `HandSize`, `HandX`, `JoinForcesAmount`, `MaxTgts`, `NumInHand`, `NumInLib`, `NumInYard`, `NumTotal`, `ReturnX`, `Sacrificed$CardPower`, `ShiftX`, `VoteNum`, `X`, `XFetch`, `Y`, `Z`
- `ChangeNumDesc$`: TODO: Describe this parameter.
  Observed values: `another`, `any number of`
- `ChangeType$`: TODO: Describe this parameter.
  Observed values: `Arcane`, `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment,Land`, `Artifact,Enchantment`, `Artifact,Instant,Sorcery`, `Artifact.cmcEQ2`, `Artifact.cmcEQ3`, `Artifact.cmcEQ4,Artifact.cmcEQ5`, `Artifact.cmcEQX`, `Artifact.cmcGE6`, `Artifact.cmcLE1`, `Artifact.cmcLE5`, `Artifact.cmcLEX`, `Artifact.cmcLEX+YouOwn`, `Artifact.Creature`, `Artifact.Creature+YouOwn`, `Artifact.hasManaAbility,Land.Basic`, `Artifact.IsRemembered`, `Artifact.IsRemembered+cmcEQ2,Artifact.IsRemembered+cmcEQ3`, `Artifact.IsRemembered,Creature.IsRemembered,Land.IsRemembered`, `Artifact.Legendary+YouOwn`, `Artifact.ManaCost0,Artifact.ManaCost1`, `Artifact.nonColorless+cmcLTX`, `Artifact.nonCreature`, `Artifact.nonLand+cmcLTX`, `Artifact.Other+YouCtrl`, `Artifact.OwnedBy TargetedPlayer`, `Artifact.TargetedPlayerCtrl`, `Artifact.TargetedPlayerOwn,Instant.TargetedPlayerOwn,Sorcery.TargetedPlayerOwn`, `Artifact.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouOwn`, `Artifact.YouOwn+cmcLE2`, `Artifact.YouOwn,Creature.YouOwn`, `Artifact.YouOwn,Enchantment.YouOwn`, `Aura`, `Aura,Demigod,God`, `Aura,Equipment`, `Aura,Shrine`, `Aura.CanEnchantEquippedBy`, `Aura.CanEnchantRemembered+YouCtrl`, `Aura.CanEnchantSource`, `Aura.CanEnchantSource+cmcLEX+doesNotShareNameWith Aura.YouCtrl`, `Aura.CanEnchantSource+YouCtrl+cmcLEX`, `Aura.CanEnchantSource+YouOwn`, `Aura.CanEnchantSource,Equipment.CanEnchantSource`, `Aura.Curse+NameNotEnchantingEnchantedPlayer`, `Aura.hasKeywordEnchant:Creature`, `Aura.YouCtrl+!IsRemembered`, `Aura.YouOwn`, `Aura.YouOwn,Equipment.YouOwn`, `Battle`, `Bird,Land.Basic`, `Card`, `Card.!Legendary`, `Card.!namedBurning-Rune Demon`, `Card.AdventureCard+TargetedPlayerCtrl`, `Card.Artifact,Card.Dragon`, `Card.Aura`, `Card.Aurochs`, `Card.Battle`, `Card.Black+cmcLEX`, `Card.Cave`, `Card.ChosenCard`, `Card.ChosenCtrl`, `Card.cmcEQ9`, `Card.cmcGE2+TargetedPlayerCtrl`, `Card.cmcGE3`, `Card.cmcGE4`, `Card.cmcGE6`, `Card.cmcLEX`, `Card.Colorless+cmcGE7`, `Card.Creature`, `Card.Creature+Dinosaur`, `Card.Creature+Green+nonLegendary+cmcLE3`, `Card.Creature+IsRemembered+cmcM20`, `Card.Creature+Legendary+YouOwn`, `Card.Curse`, `Card.Dinosaur`, `Card.Doctor`, `Card.Eldrazi+YouOwn`, `Card.Elemental`, `Card.Elf`, `Card.Enchantment+YouOwn`, `Card.Equipment`, `Card.Equipment+cmcLEX`, `Card.Equipment+YouOwn`, `Card.Equipment,Card.Vehicle`, `Card.ExiledWithSource`, `Card.faceUp+TargetedPlayerOwn`, `Card.Faerie`, `Card.Forest`, `Card.Giant`, `Card.Goblin`, `Card.Historic+YouOwn+IsImprinted`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.IsRemembered`, `Card.IsRemembered+ActivePlayerCtrl`, `Card.IsRemembered+Creature,Card.IsRemembered+Planeswalker`, `Card.IsRemembered+Faerie,Card.IsRemembered+Sorcery,Card.IsRemembered+Instant`, `Card.IsRemembered+hasXCost`, `Card.IsRemembered+Permanent`, `Card.IsRemembered+YouOwn`, `Card.IsRemembered+YouOwn+ExiledWithSource`, `Card.Kithkin`, `Card.Legendary`, `Card.Legendary+IsRemembered,Enchantment.IsRemembered`, `Card.Merfolk`, `Card.Merfolk,Card.Land`, `Card.MonoColor`, `Card.Mountain+YouOwn`, `Card.MultiColor`, `Card.MultiColor+YouOwn`, `Card.named1996 World Champion`, `Card.namedAlpine Watchdog,Card.namedIgneous Cur`, `Card.namedAvarax`, `Card.namedBattalion Foot Soldier`, `Card.namedBrambleweft Behemoth`, `Card.NamedCard`, `Card.namedDaru Cavalier`, `Card.namedDragonstorm Globe,Card.namedBoulderborn Dragon`, `Card.namedElvish Clancaller`, `Card.namedEmbermage Goblin`, `Card.namedEmpyrial Archangel`, `Card.namedEzio; Blade of Vengeance`, `Card.namedFestering Newt,Card.namedBubbling Cauldron`, `Card.namedForest`, `Card.namedGathering Throng`, `Card.namedGigantiform`, `Card.namedGoblin Tutor`, `Card.namedGodsire`, `Card.namedGrowth-Chamber Guardian`, `Card.namedHalvar; God of Battle,Equipment`, `Card.namedHeart-Piercer Bow,Card.namedVial of Dragonfire`, `Card.namedHellkite Overlord`, `Card.namedHowling Wolf`, `Card.namedInfectious Bloodlust`, `Card.namedJiang Yanggu`, `Card.namedLegion Conquistador`, `Card.namedLlanowar Sentinel`, `Card.namedMagitek Infantry`, `Card.namedMagnifying Glass,Card.namedThinking Cap`, `Card.namedNesting Wurm`, `Card.namedNissa; Genesis Mage`, `Card.namedNissa; Nature's Artisan`, `Card.namedOminous Traveler+YouCtrl`, `Card.namedPrince of Thralls`, `Card.namedScreaming Seahawk`, `Card.namedSkyshroud Sentinel`, `Card.namedSphinx Sovereign`, `Card.namedSpirit of the Night`, `Card.namedSquadron Hawk`, `Card.namedTempest Hawk`, `Card.namedThe Animus`, `Card.namedThe Spear of Leonidas`, `Card.namedThe Underworld Cookbook`, `Card.namedThe Unspeakable`, `Card.namedTrustworthy Scout`, `Card.namedViashivan Dragon`, `Card.namedWelkin Hawk`, `Card.namedWhisper Squad`, `Card.namedWretched Throng`, `Card.nonArtifact+nonLand`, `Card.nonCreature+nonLand`, `Card.nonCreature+nonLand+YouOwn+IsImprinted`, `Card.nonCreature+YouOwn`, `Card.nonLand`, `Card.nonLand+cmcLE3`, `Card.nonLand+Colorless`, `Card.nonLand+TargetedPlayerCtrl`, `Card.nonLand+YouCtrl`, `Card.nonLand+YouCtrl+cmcEQX`, `Card.nonLand+YouOwn`, `Card.NotedNameAetherSearcher`, `Card.OppCtrl`, `Card.Other`, `Card.OwnedBy TriggeredTarget`, `Card.Permanent`, `Card.Permanent+IsRemembered`, `Card.Permanent+YouOwn+IsRemembered`, `Card.Pirate`, `Card.Plains`, `Card.Rat`, `Card.RememberedPlayerCtrl+ChosenType`, `Card.Self`, `Card.SharesCMCWith Discarded`, `Card.SharesColorWith Valid Creature.Legendary+YouCtrl`, `Card.sharesNameWith Imprinted`, `Card.sharesNameWith Remembered`, `Card.sharesNameWith Valid Creature.YouCtrl+Other`, `Card.StrictlySelf`, `Card.targetedBy`, `Card.TargetedPlayerCtrl`, `Card.TopGraveyard+YouOwn`, `Card.Treefolk,Card.Forest`, `Card.Vampire`, `Card.withFlashback`, `Card.withFlashback+YouOwn,Card.withDisturb+YouOwn`, `Card.YouCtrl`, `Card.YouOwn`, `Card.YouOwn+cmcLE2`, `Card.YouOwn+counters_GE1_SILVER`, `Card.YouOwn+counters_GE1_STUDY`, `Card.YouOwn+namedAjani; Inspiring Leader`, `Card.YouOwn+namedAjani; Valiant Protector`, `Card.YouOwn+namedAltanak; the Thrice-Called`, `Card.YouOwn+namedAngrath; Minotaur Pirate`, `Card.YouOwn+namedArachnus Web`, `Card.YouOwn+namedAshiok; Sculptor of Fears`, `Card.YouOwn+namedBasri; Devoted Paladin`, `Card.YouOwn+namedChandra; Bold Pyromancer`, `Card.YouOwn+namedChandra; Flame's Catalyst`, `Card.YouOwn+namedChandra; Flame's Fury`, `Card.YouOwn+namedChandra; Pyrogenius`, `Card.YouOwn+namedCommand Tower`, `Card.YouOwn+namedDomri; City Smasher`, `Card.YouOwn+namedDovin; Architect of Law`, `Card.YouOwn+namedEivor; Battle-Ready`, `Card.YouOwn+namedElspeth; Undaunted Hero`, `Card.YouOwn+namedGarruk; Savage Herald`, `Card.YouOwn+namedGideon; Martial Paragon`, `Card.YouOwn+namedGideon; the Oathsworn`, `Card.YouOwn+namedGod-Pharaoh's Gift`, `Card.YouOwn+namedHuatli; Dinosaur Knight`, `Card.YouOwn+namedJace; Arcane Strategist`, `Card.YouOwn+namedJace; Ingenious Mind-Mage`, `Card.YouOwn+namedLegion Angel`, `Card.YouOwn+namedLiliana; Death Mage`, `Card.YouOwn+namedLiliana; Death Wielder`, `Card.YouOwn+namedMonk of the Open Hand`, `Card.YouOwn+namedMu Yanling`, `Card.YouOwn+namedMu Yanling; Celestial Wind`, `Card.YouOwn+namedNicol Bolas; the Deceiver`, `Card.YouOwn+namedOko; the Trickster`, `Card.YouOwn+namedRal; Caller of Storms`, `Card.YouOwn+namedRowan; Fearless Sparkmage`, `Card.YouOwn+namedScion of Darkness`, `Card.YouOwn+namedSorin; Vampire Lord`, `Card.YouOwn+namedSunlit Hoplite`, `Card.YouOwn+namedTARDIS`, `Card.YouOwn+namedTeferi; Timebender`, `Card.YouOwn+namedTeferi; Timeless Voyager`, `Card.YouOwn+namedTezzeret; Master of Metal`, `Card.YouOwn+namedVivien; Nature's Avenger`, `Card.YouOwn+namedVraska; Regal Gorgon`, `Card.YouOwn+namedVraska; Scheming Gorgon`, `Card.YouOwn+NotedNameSmugglerCaptain`, `Construct`, `Construct,Robot,Vehicle`, `Creature`, `Creature,Artifact,Enchantment,Land`, `Creature,Artifact,Land`, `Creature,Enchantment,Planeswalker`, `Creature,Land`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!token`, `Creature.!token+IsRemembered`, `Creature.!token+IsRemembered+YouOwn`, `Creature.!token+Other+YouCtrl`, `Creature.ActivePlayerCtrl`, `Creature.Ally`, `Creature.Ally+YouOwn`, `Creature.Angel+YouCtrl,Creature.Demon+YouCtrl,Creature.Dragon+YouCtrl`, `Creature.Assembly-Worker`, `Creature.Bird+YouOwn`, `Creature.Black`, `Creature.Black+YouCtrl`, `Creature.Black+YouCtrl,Creature.Blue+YouCtrl`, `Creature.Black+YouCtrl,Creature.Red+YouCtrl`, `Creature.Blue+YouCtrl`, `Creature.Blue,Creature.Black`, `Creature.Blue,Creature.Red`, `Creature.ChosenCtrl`, `Creature.ChosenType`, `Creature.ChosenType+YouOwn`, `Creature.cmcEQV`, `Creature.cmcEQX`, `Creature.cmcEQX+sharesCreatureTypeWith Sacrificed`, `Creature.cmcEQX+YouCtrl`, `Creature.cmcGE6`, `Creature.cmcLE1`, `Creature.cmcLE1,Artifact.cmcLE1,Enchantment.cmcLE1`, `Creature.cmcLE3`, `Creature.cmcLE3+YouCtrl`, `Creature.cmcLEX`, `Creature.cmcLEX+TargetedPlayerOwn`, `Creature.cmcLEX,Instant.cmcLEX,Sorcery.cmcLEX`, `Creature.cmcLTX`, `Creature.cmcLTX+YouCtrl`, `Creature.cmcLTX+YouOwn`, `Creature.cmcLTY+YouCtrl`, `Creature.Colorless`, `Creature.Colorless+cmcGE7`, `Creature.Demon`, `Creature.Dragon`, `Creature.Dragon+YouCtrl`, `Creature.Elemental+YouCtrl`, `Creature.Elf`, `Creature.ExiledWithSource`, `Creature.faceUp+YouCtrl+withDisguise`, `Creature.Goblin`, `Creature.Green`, `Creature.Green+cmcLEX`, `Creature.Green+YouCtrl`, `Creature.Green+YouOwn`, `Creature.Green,Creature.White`, `Creature.IsImprinted`, `Creature.IsRemembered`, `Creature.IsRemembered+Artifact,Vehicle.IsRemembered`, `Creature.IsRemembered,Enchantment.IsRemembered,Land.IsRemembered`, `Creature.IsRemembered,Land.IsRemembered`, `Creature.Kraken,Creature.Leviathan,Creature.Octopus,Creature.Serpent`, `Creature.Legendary`, `Creature.Minotaur`, `Creature.MultiColor`, `Creature.Myr`, `Creature.NamedCard+!sharesNameWith TriggeredCard`, `Creature.nonAngel+YouCtrl`, `Creature.nonAvatar+YouOwn,Planeswalker.YouOwn`, `Creature.nonWhite`, `Creature.NotDefinedReplacedSimultaneousETB`, `Creature.numColorsEQX`, `Creature.OppOwn`, `Creature.Other+YouCtrl`, `Creature.Other+YouOwn`, `Creature.OwnedBy Remembered`, `Creature.OwnedBy ThisTargetedPlayer,Land.OwnedBy ThisTargetedPlayer`, `Creature.powerGE6,Creature.toughnessGE6`, `Creature.powerLE2`, `Creature.Red+YouCtrl`, `Creature.Red+YouCtrl,Creature.Green+YouCtrl`, `Creature.Red,Creature.Artifact`, `Creature.RememberedPlayerCtrl`, `Creature.SaddledThisTurn`, `Creature.sharesCreatureTypeWithAll Tapped`, `Creature.sharesNameWith Sacrificed`, `Creature.sharesOwnerWith TriggeredCard`, `Creature.Soldier+YouCtrl`, `Creature.StrictlyOther+YouCtrl`, `Creature.TargetedPlayerCtrl`, `Creature.TargetedPlayerOwn`, `Creature.TopGraveyardCreature+YouCtrl`, `Creature.TopGraveyardCreature+YouOwn`, `Creature.totalPT_EQX`, `Creature.toughnessLE2`, `Creature.toughnessLEY`, `Creature.Vampire`, `Creature.Vampire+cmcLE6`, `Creature.White+YouCtrl`, `Creature.White+YouCtrl,Creature.Blue+YouCtrl`, `Creature.White+YouCtrl,Creature.Green+YouCtrl`, `Creature.withDeathtouch+YouCtrl,Creature.withHexproof+YouCtrl,Creature.withReach+YouCtrl,Creature.withTrample+YouCtrl`, `Creature.withDefender`, `Creature.withEmbalm+YouCtrl,Creature.withEternalize+YouCtrl`, `Creature.withFlying+YouCtrl`, `Creature.withMorph,Creature.withMegamorph`, `Creature.YouCtrl`, `Creature.YouCtrl+!token,Artifact.YouCtrl+!token`, `Creature.YouCtrl+cmcLEX`, `Creature.YouCtrl+nonHuman+cmcLEX`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+powerLTX`, `Creature.YouCtrl+totalPT_LE5`, `Creature.YouCtrl,Artifact.YouCtrl`, `Creature.YouCtrl,Land.YouCtrl`, `Creature.YouOwn`, `Creature.YouOwn+cmcLE2`, `Creature.YouOwn+cmcLE3`, `Creature.YouOwn+cmcLESearchX`, `Creature.YouOwn+cmcLEX`, `Creature.YouOwn+cmcLEX,Planeswalker.YouOwn+cmcLEX`, `Creature.YouOwn+cmcLTY`, `Creature.YouOwn+IsImprinted`, `Creature.YouOwn+NoAbilities`, `Creature.YouOwn+Other`, `Creature.YouOwn,Artifact.YouOwn`, `Creature.YouOwn,Land.YouOwn`, `Creature.YouOwn,Planeswalker.YouOwn`, `Creature.YouOwn,Spacecraft.YouOwn`, `Creature.YouOwn,Vehicle.YouOwn`, `Creature.Zombie+setWAR,Planeswalker.setWAR`, `Demon`, `Desert`, `Dinosaur`, `Dinosaur.YouCtrl`, `Doctor`, `Dragon`, `Dragon.!namedTiamat`, `Dwarf`, `EACH Aura & Equipment`, `EACH Card.Black & Card.Green & Card.Blue`, `EACH Card.White & Card.Blue & Card.Black & Card.Red & Card.Green`, `EACH Creature & Land`, `EACH Creature.YouOwn & Land.YouOwn`, `EACH Creature.YouOwn & Land.YouOwn & Card.nonCreature+nonLand+YouOwn`, `EACH Creature.YouOwn+IsRemembered & Land.YouOwn+IsRemembered`, `EACH Forest & Plains`, `EACH Forest.Basic & Plains.Basic`, `EACH Human.YouCtrl & Artifact.YouCtrl`, `EACH Instant & Sorcery`, `EACH Island & Swamp & Mountain`, `EACH Land.Basic & Shrine`, `EACH Plains & Island & Swamp & Mountain`, `EACH Saga.YouOwn+IsRemembered & Land.YouOwn+IsRemembered`, `EACH Zombie & Swamp`, `Eldrazi`, `Elf.IsRemembered,Land.IsRemembered`, `Elf.YouOwn,Land.YouOwn`, `Elf.YouOwn,Tyvar.YouOwn`, `Enchantment`, `Enchantment.cmcLE3`, `Enchantment.YouCtrl`, `Enchantment.YouCtrl+Red,Enchantment.YouCtrl+Green`, `Enchantment.YouOwn`, `Enchantment.YouOwn+IsRemembered`, `Equipment`, `Equipment,Vehicle`, `Equipment.cmcEQ2`, `Equipment.YouCtrl`, `Food`, `Forest`, `Forest,Island`, `Forest,Plains`, `Forest.Basic`, `Forest.Basic+YouCtrl`, `Forest.Basic,Island.Basic`, `Forest.Basic,Island.Basic,Mountain.Basic`, `Forest.Basic,Plains.Basic`, `Forest.Basic,Plains.Basic,Island.Basic`, `Gate`, `Goblin`, `God`, `Instant`, `Instant,Card.hasKeywordFlash`, `Instant,Sorcery`, `Instant.Blue`, `Instant.cmcEQ1`, `Instant.cmcEQ1,Sorcery.cmcEQ1`, `Instant.cmcEQ2`, `Instant.cmcEQ3`, `Instant.cmcEQX,Sorcery.cmcEQX`, `Instant.cmcLE2`, `Instant.cmcLE2,Sorcery.cmcLE2`, `Instant.ExiledWithSource,Sorcery.ExiledWithSource`, `Instant.IsRemembered,Sorcery.IsRemembered`, `Instant.Red,Sorcery.Red`, `Instant.SharesColorWith,Sorcery.SharesColorWith`, `Instant.sharesNameWith YourGraveyard,Sorcery.sharesNameWith YourGraveyard`, `Instant.White+cmcLE4,Instant.Red+cmcLE4`, `Instant.YouCtrl`, `Instant.YouCtrl+MultiColor,Sorcery.YouCtrl+MultiColor`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouOwn`, `Instant.YouOwn+cmcLE3,Sorcery.YouOwn+cmcLE3`, `Instant.YouOwn,Sorcery.YouOwn`, `Instant.YouOwn,Sorcery.YouOwn,Battle.YouOwn`, `Island`, `Island,Mountain`, `Island,Swamp`, `Island.Basic,Mountain.Basic,Plains.Basic`, `Island.Basic,Swamp.Basic,Mountain.Basic`, `Land`, `Land,Battle`, `Land,Creature`, `Land.Basic`, `Land.Basic+!sharesLandTypeWith Valid Land.YouCtrl`, `Land.Basic+Forest`, `Land.Basic+IsRemembered`, `Land.Basic+RememberedPlayerCtrl`, `Land.Basic+sharesNameWith ChosenCard`, `Land.Basic+YouCtrl`, `Land.Basic+YouOwn`, `Land.Basic,Card.Cave`, `Land.Basic,Card.Gate`, `Land.Basic,Cave`, `Land.Basic,Creature`, `Land.Basic,Desert`, `Land.Basic,Gate`, `Land.Basic,Land.Locus,Land.Sphere`, `Land.Basic,Town`, `Land.ControlledBy TriggeredCardController`, `Land.Forest+Basic`, `Land.hasABasicLandType`, `Land.IsRemembered`, `Land.IsRemembered+ActivePlayerCtrl`, `Land.IsRemembered,Gate.IsRemembered`, `Land.Plains`, `Land.Plains+Basic`, `Land.RememberedPlayerCtrl`, `Land.Snow`, `Land.TargetedPlayerCtrl`, `Land.TargetedPlayerOwn`, `Land.YouCtrl`, `Land.YouCtrl+tapped`, `Land.YouOwn`, `Land.YouOwn+IsImprinted`, `Legendary`, `Lesson,Noble`, `Mercenary`, `Merfolk.YouCtrl`, `Mount,Vehicle`, `Mountain`, `Mountain,Cave`, `Mountain,Forest`, `Mountain,Plains`, `Mountain.Basic`, `Mountain.Basic,Forest.Basic,Plains.Basic`, `Mountain.Basic,Plains.Basic,Swamp.Basic`, `Mountain.YouCtrl`, `Myr`, `Ninja`, `Permanent`, `Permanent.BorderColorSilver`, `Permanent.cmcLE7+YouCtrl`, `Permanent.cmcLEX`, `Permanent.cmcLEX+YouCtrl`, `Permanent.cmcLEX+YouOwn`, `Permanent.cmcOdd+YouOwn`, `Permanent.ControlledBy TriggeredTarget`, `Permanent.Dragon`, `Permanent.Elf`, `Permanent.Faerie`, `Permanent.Goblin`, `Permanent.Historic`, `Permanent.IsRemembered`, `Permanent.Legendary+cmcLTY`, `Permanent.Mercenary+cmcLE1`, `Permanent.Mercenary+cmcLE2`, `Permanent.Mercenary+cmcLE3`, `Permanent.Mercenary+cmcLE4`, `Permanent.Mercenary+cmcLE5`, `Permanent.Mercenary+cmcLE6`, `Permanent.Merfolk`, `Permanent.Minotaur`, `Permanent.namedNissa's Chosen`, `Permanent.nonLand+ChosenCtrl`, `Permanent.nonLand+cmcLE3`, `Permanent.nonLand+Other+YouOwn+YouCtrl`, `Permanent.nonLand+YouCtrl`, `Permanent.nonLand+YouOwn`, `Permanent.nonSaga`, `Permanent.Other+nonLand+YouCtrl`, `Permanent.Other+YouCtrl`, `Permanent.Rebel+cmcLE2`, `Permanent.Rebel+cmcLE3`, `Permanent.Rebel+cmcLE4`, `Permanent.Rebel+cmcLE5`, `Permanent.Rebel+cmcLE6`, `Permanent.Rebel+cmcLEX`, `Permanent.Snow,Legendary,Saga`, `Permanent.Spirit+Legendary`, `Permanent.TargetedPlayerCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+!IsRemembered`, `Permanent.YouCtrl+cmcLEX`, `Permanent.YouOwn`, `Permanent.YouOwn+cmcLE3`, `Permanent.YouOwn+IsRemembered`, `Pirate.YouCtrl`, `Plains`, `Plains,Island`, `Plains,Island,Swamp,Mountain`, `Plains,Island,Swamp,Mountain,Forest`, `Plains,Swamp`, `Plains.Basic`, `Plains.Basic,Creature.cmcLE1`, `Plains.Basic,Island.Basic,Swamp.Basic`, `Plains.Basic,Swamp.Basic,Forest.Basic`, `Plains.IsRemembered,Creature.cmcLE3+IsRemembered`, `Plains.YouCtrl`, `Planeswalker`, `Planeswalker.cmcLE6`, `Planeswalker.YouOwn`, `Praetor`, `Rat.Creature+YouOwn`, `Remembered.sameName`, `Room.doesNotShareNameWith Room.YouCtrl`, `Rune.YouOwn`, `Shrine.YouOwn`, `Sliver`, `Sorcery`, `Sorcery.YouOwn`, `Sorcery.YouOwn,Instant.YouOwn`, `Spider.Hero`, `Spirit.YouCtrl`, `Squirrel`, `Swamp`, `Swamp,Forest`, `Swamp,Mountain`, `Swamp.Basic`, `Swamp.Basic,Forest.Basic,Island.Basic`, `Swamp.Basic,Mountain.Basic,Forest.Basic`, `Swamp.YouCtrl`, `Targeted.Creature+sameName`, `Targeted.Permanent+sameName`, `Targeted.sameName`, `TargetedCard.sameName`, `Trap`, `Triggered.Other+sharesPermanentTypeWith`, `Triggered.sameName`, `Triggered.YouOwn+sameName`, `TriggeredCard.sharesNameWith`, `Vampire`, `Vampire.YouCtrl`, `Vehicle`, `Zombie.YouCtrl`, `Zombie.YouOwn`
- `ChangeTypeDesc$`: TODO: Describe this parameter.
  Observed values: `a legendary creature card`, `a multicolored instant or sorcery card from your graveyard`, `Ally creature card`, `artifact card`, `artifact card with mana value equal to 1 plus the sacrificed artifact's mana value`, `artifact creature card or vehicle card milled this way`, `artifact or enchantment they own`, `artifact they own`, `artifact, creature, and/or enchantment cards with mana value 1 or less`, `artifact, instant or sorcery`, `Aura or Shrine card`, `basic Forest`, `basic Forest or Plains`, `basic Forest, Island, or Mountain`, `basic Forest, Plains, or Island`, `basic Island, Mountain, or Plains`, `basic Island, Swamp, or Mountain`, `basic land`, `basic land card and a Shrine card`, `basic land card or a Desert card`, `basic land cards and/or Gate`, `basic land cards and/or Town cards with different names`, `basic land of Cave card`, `basic Mountain, Forest, or Plains`, `basic Mountain, Plains, or Swamp`, `basic Plains card`, `basic Plains, Island, or Swamp`, `basic Plains, Swamp, or Forest`, `basic Swamp, Forest, or Island`, `basic Swamp, Mountain, or Forest`, `basic, Sphere, or Locus land card`, `battle cards with different names`, `black card with mana value less than or equal to the number of creature cards in their graveyard`, `black creature`, `blue instant`, `card`, `card exiled with CARDNAME`, `card named Basri, Devoted Paladin`, `card they own`, `cards with flashback`, `Choose a card with mana value 2 or less`, `colorless creature`, `Creature`, `creature`, `creature and/or land card`, `creature and/or land cards they own`, `creature card that's {n:X color}`, `creature card they own`, `creature card they own and up to one land card they own`, `creature card with mana value equal to 1 plus the sacrificed creature's mana value`, `creature card with the same name as {c:Targeted}`, `creature cards milled this way`, `creature or land`, `creature or land card they own`, `creature or planeswalker card with mana value X or less`, `creature or Vehicle card`, `Dragon creature`, `Dragon permanent`, `Elf permanent`, `Goblin permanent`, `human you control and an artifact you control`, `instant and/or sorcery`, `instant card they own`, `legendary creature`, `Merfolk permanent`, `Minotaur creature`, `Mountain card they own`, `multicolored`, `multicolored card they own`, `Myr creature`, `noncreature card they own`, `nonland card`, `nonlegendary`, `permanent card with an odd mana value`, `permanent card with mana value X or less`, `permanent cards with different names`, `sorcery card they own`, `Spider Hero`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$ValidGraveyard Creature.YouOwn`, `OppDamaged`, `RaidTest`, `X`, `Z`
- `ChoiceOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `ChooseFromDefined$`: TODO: Describe this parameter.
  Observed values: `AttachedTo TriggeredCardLKICopy.Aura`, `ExiledWith.Creature`, `Remembered`, `Remembered.Black`, `Remembered.Blue`, `Remembered.Green`, `Remembered.Red`, `Remembered.White`, `ReplacedCards.Land`, `Targeted.cmcLE4`, `TopThirdOfLibrary`, `TriggeredCards`, `TriggeredSources`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `DefendingPlayer`, `ImprintedController`, `Opponent`, `Player.IsRemembered`, `Remembered`, `Targeted`, `TargetedController`, `TargetedOwner`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `Choser$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `Delirium`, `Kicked`, `Metalcraft`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CheckExiled`, `CheckHand`, `CheckName`, `CheckYard`, `Count$ActivatedThisGame`, `FetchX`, `HaveB`, `HaveG`, `HaveR`, `HaveU`, `HaveW`, `MilledCreature`, `PeerReachTotal`, `Resolved`, `SackedCMC`, `Votes`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE4`, `GE8`, `GTX`, `LE0`, `LE4`, `LTX`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Collected`, `ExiledWith`, `ExiledWithSource`, `Imprinted`, `ParentTarget`, `Remembered`, `Sacrificed`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredCard`, `TriggeredNewCardLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If an opponent has more life than you,`, `If not,`, `If that creature is a Zombie,`, `If that player or that planeswalker's controller has more life than you,`, `If you control four or fewer lands,`, `If you control three or more artifacts,`, `If you do,`
- `ConditionGameTypes$`: TODO: Describe this parameter.
  Observed values: `Draft,QuestDraft`
- `ConditionLifeAmount$`: TODO: Describe this parameter.
  Observed values: `GTX`, `LTX`
- `ConditionLifeTotal$`: TODO: Describe this parameter.
  Observed values: `TargetedOrController`, `You`
- `ConditionManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `G`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`, `G`, `U`, `U B`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.Creature`, `Aura`, `Card`, `Card.Artifact`, `Card.attackedThisTurn,Card.blockedThisTurn`, `Card.bargained`, `Card.Black`, `Card.ChosenCard`, `Card.ChosenCard+inZoneBattlefield`, `Card.ChosenCtrl`, `Card.cmcGTX`, `Card.cmcLE2`, `Card.cmcLE3`, `Card.cmcLEX`, `Card.cmcLTX`, `Card.counters_EQ0_EGG`, `Card.counters_EQ0_SCREAM`, `Card.counters_EQ0_TIME`, `Card.counters_GE5_FLAME`, `Card.Creature`, `Card.Creature+ChosenCard+inZoneBattlefield`, `Card.Creature+cmcLE2+ChosenCard`, `Card.Creature+powerLEY`, `Card.Enchantment`, `Card.Green,Card.Red`, `Card.hasXCost`, `Card.inRealZone Graveyard`, `Card.Land`, `Card.Land+ChosenCard`, `Card.NamedCard`, `Card.namedHammer of Nazahn`, `Card.nonBlack`, `Card.nonCreature+nonLand`, `Card.nonEnchantment`, `Card.Permanent`, `Card.Permanent+YouCtrl`, `Card.powerLEX`, `Card.Samurai`, `Card.Self`, `Card.Self+counters_EQ4_P1P1`, `Card.Self+PromisedGift`, `Card.sharesCardTypeWith Exiled`, `Card.sharesNameWith Battlefield`, `Card.sharesNameWith YourGraveyard`, `Card.sneaked`, `Card.ThisTurnEntered+sneaked`, `Card.wasCast`, `Card.wasCastFromGraveyard`, `Card.YouCtrl`, `Card.YouOwn`, `Creature`, `Creature,Planeswalker`, `Creature.ChosenType`, `Creature.cmcGT3`, `Creature.cmcLE3`, `Creature.Legendary+YouCtrl`, `Creature.OppCtrl`, `Creature.toughnessGE1`, `Creature.withMorph,Creature.withMegamorph`, `Creature.YouCtrl+powerGE4`, `Creature.Zombie`, `Faerie.YouCtrl`, `God`, `Instant,Sorcery`, `Land`, `Land.namedWastes+YouCtrl`, `Land.YouCtrl`, `Permanent`, `Permanent.!token+YouCtrl`, `Permanent.nonLand+cmcLEY`, `Permanent.White+YouCtrl`, `Planeswalker.Nissa+YouCtrl`, `Snow`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQ3`, `GE0`, `GE1`, `GE2`, `GE3`, `GE5`, `GE6`, `GE7`, `GEX`, `GEY`, `GT0`, `GTX`, `GTY`, `LE0`, `LE6`, `LEX`, `LEY`, `LT1`, `LT2`, `LT7`, `LTX`, `LTY`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Library`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T Exile<1/CARDNAME>`, `1 W U`, `T`, `2 B`, `ExileAnyGrave<1/Card.TriggeredNewCard>`, `1 U T`, `B R G T`, `2 U Discard<2/Card>`, `4 W`, `PayEnergy<2>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, discard X cards.`, `As an additional cost to cast this spell, sacrifice a creature.`, `As an additional cost to cast this spell, tap three untapped white creatures you control.`, `Grandeur — Discard another card named Korlash, Heir to Blackblade:`, `Grandeur — Discard another card named Linessa, Zephyr Mage:`, `Sacrifice two Eldrazi Scions:`, `Sacrifice two Treasures:`, `You may sacrifice a creature.`, `{1}, Reveal X black cards from your hand, Sacrifice CARDNAME:`, `{1}{B}{B}{G}`, `{1}{U}`, `{2}{B}, {T}, Sacrifice a blue creature, a black creature, and a red creature:`, `{2}{G}, {T}, Sacrifice a red creature, a green creature, and a white creature:`, `{2}{R}, {T}, Sacrifice a black creature, a red creature, and a green creature:`, `{2}{U}, {T}, Sacrifice a white creature, a blue creature, and a black creature:`, `{2}{W}, {T}, Sacrifice a green creature, a white creature, and a blue creature:`, `{3}{B}{B}, {T}, Sacrifice X other creatures:`, `{3}{U}`, `{G}, {T}, Sacrifice CARDNAME and another green creature:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `BottomOfLibrary`, `ChosenCard`, `CorrectedSelf`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `DirectRemembered`, `DiscardedCards`, `Enchanted`, `Enchanted & Self`, `Equipped`, `ExiledCards`, `ExiledWith`, `ExiledWithSource`, `Imprinted`, `OriginalHost`, `Parent`, `ParentTarget`, `Remembered`, `Remembered.Creature`, `Remembered.ExiledWithSource`, `RememberedCard`, `RememberedFirst`, `RememberedLKI`, `ReplacedCard`, `ReplacedTarget`, `SacrificedCards`, `Self`, `Self & ChosenCard`, `Self & ExiledWith`, `Self & Spawner>TriggeredAttackerLKICopy`, `Self.YouOwn`, `Spawner>TriggeredCard`, `Targeted`, `Targeted.!ChosenCard`, `TopOfLibrary`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredCards`, `TriggeredNewCardLKICopy`, `TriggeredSourceLKICopy`, `TriggeredSpellAbility`, `TriggeredTarget`, `TriggeredTargetLKICopy`, `Valid Creature.blockedBySource`, `ValidGraveyard Artifact.ThisTurnEnteredFrom_Battlefield,Creature.ThisTurnEnteredFrom_Battlefield,Enchantment.ThisTurnEnteredFrom_Battlefield,Land.ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Artifact.YouOwn+ThisTurnEnteredFrom_Battlefield,Creature.YouOwn+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Artifact.YouOwn+ThisTurnEnteredFrom_Battlefield,Creature.YouOwn+ThisTurnEnteredFrom_Battlefield,Land.YouOwn+ThisTurnEnteredFrom_Battlefield,Enchantment.YouOwn+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Aura.YouOwn`, `ValidGraveyard Card.YouOwn+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Creature`, `ValidGraveyard Creature.!token+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Creature.ThisTurnEntered`, `ValidGraveyard Creature.ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Creature.YouCtrl+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Creature.YouOwn+!token+ThisTurnEntered`, `ValidGraveyard Creature.YouOwn+ThisTurnEnteredFrom_Battlefield`, `ValidGraveyard Permanent.YouOwn+ThisTurnEnteredFrom_Battlefield`, `ValidHand Card.nonChosenCard`, `ValidHand Land.IsRemembered`
- `DefinedDesc$`: TODO: Describe this parameter.
  Observed values: `it`, `that card`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `CardOwner`, `ChosenPlayer`, `ImprintedController`, `Opponent`, `ParentTarget`, `Player`, `Player.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Player.Other`, `Remembered`, `RememberedController`, `RememberedOwner`, `ReplacedPlayer`, `ReplacedTarget`, `Spawner>TriggeredTarget`, `Targeted`, `TargetedController`, `TargetedOwner`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `You`
- `DestAltSVar$`: TODO: Describe this parameter.
  Observed values: `Count$ThisTurnEntered_Graveyard_from_Battlefield_Creature`, `MANDATORY Count$TimesKicked`, `MANDATORY X`, `TriggeredCard$Valid Plains`, `X`
- `DestAltSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE5`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Ante`, `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`, `Library`, `PlanarDeck`, `Sideboard`
- `DestinationAlternative$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Hand`, `Library`
- `DifferentCMC$`: TODO: Describe this parameter.
  Observed values: `True`
- `DifferentNames$`: TODO: Describe this parameter.
  Observed values: `True`
- `DifferentPower$`: TODO: Describe this parameter.
  Observed values: `True`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `UntilHostLeavesPlay`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `Exactly$`: TODO: Describe this parameter.
  Observed values: `True`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExiledWithEffectSource$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExileFaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDownPower$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `5`
- `FaceDownSetType$`: TODO: Describe this parameter.
  Observed values: `Artifact & Creature`, `Artifact & Creature & Cyberman`, `Creature`, `Land & Forest`
- `FaceDownToughness$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `5`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `Foretold$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForetoldCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `DelayTriggerRemembered`, `ParentTarget`, `Player.IsRemembered`, `Targeted`, `TriggeredCardController`, `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Hidden$`: TODO: Describe this parameter.
  Observed values: `True`
- `Imprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintLast$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Aura.Attached`, `Card.Self+tapped`, `Card.YouOwn+named1996 World Champion`, `Creature.Legendary+YouCtrl`, `Creature.YouCtrl+powerEQ1+toughnessEQ1`, `Creature.YouOwn+Above`, `Enchantment.YouOwn`, `Permanent.Snow+YouCtrl`, `Permanent.White+YouCtrl`, `Permanent.YouOwn`, `Planeswalker.Vivien+YouCtrl`, `Swamp.YouCtrl`
- `LeaveBattlefield$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `LibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`, `1`, `2`, `3`, `4`, `6`, `X`
- `LibraryPositionAlternative$`: TODO: Describe this parameter.
  Observed values: `-1`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxTotalTargetCMC$`: TODO: Describe this parameter.
  Observed values: `10`, `3`, `6`, `8`, `X`
- `MaxTotalTargetPower$`: TODO: Describe this parameter.
  Observed values: `10`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `4 G`, `5 U`
- `NoLooking$`: TODO: Describe this parameter.
  Observed values: `True`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoRegen$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoShuffle$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `1`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `True`, `You`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `OptionalPrompt$`: TODO: Describe this parameter.
  Observed values: `Do you want to put one of those creature cards with mana value 4 or less onto the battlefield instead of putting it into your hand?`, `Put that card on the bottom of your library?`, `Select any number of Aura cards that were attached to it`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Exile`, `Battlefield,Graveyard`, `Battlefield,Hand`, `Battlefield,Hand,Graveyard`, `Battlefield,Library`, `Battlefield,Stack`, `Battlefield,Stack,Graveyard`, `Command`, `Exile`, `Exile,Command`, `Graveyard`, `Graveyard,Exile`, `Graveyard,Hand`, `Graveyard,Hand,Library`, `Graveyard,Library`, `Hand`, `Hand,Command`, `Hand,Graveyard`, `Library`, `Library,Graveyard`, `Library,Hand`, `Library,Sideboard`, `PlanarDeck`, `Sideboard`, `Sideboard,Exile`, `Stack`
- `OriginAlternative$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Graveyard,Hand`, `Graveyard,Sideboard`
- `OrOtherConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`, `true`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Blizzaga`, `Blizzara`, `Blizzard`, `Channel —`, `Cleave`, `Corrupted —`, `Coven —`, `Delirium —`, `Descend 8`, `Domain —`, `Hero's Sundering —`, `I've Come Up with a New Recipe! —`, `Imprint —`, `Magical Tinkering —`, `Max speed —`, `Metalcraft —`, `Raid —`, `Rejuvenation —`, `Solved —`, `Summon —`, `The Reunion`, `Trance`, `Warp-Strike —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE2`, `GE3`, `GE4`, `GE8`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Library`
- `PrimaryPrompt$`: TODO: Describe this parameter.
  Observed values: `Choose a creature card to return to the battlefield`, `Choose a creature card with mana value X or less`, `Choose another creature card to return to your hand`, `Choose up to two lands you control`
- `RandomOrder$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberLKI$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberSearched$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reorder$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReturnAbility$`: TODO: Describe this parameter.
  Observed values: `DBReturn`
- `ReturnValid$`: TODO: Describe this parameter.
  Observed values: `Card.IsTriggerRemembered+YouCtrl`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `Searched$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SelectPrompt$`: TODO: Describe this parameter.
  Observed values: `Choose a card for the hand`, `Choose a creature card milled this way`, `Choose a creature card to return to the battlefield`, `Choose a creature card with mana value 2 or less`, `Choose a creature, enchantment, or land card from among cards milled this way`, `Choose a land to return to its owner's hand`, `Choose a Merfolk card or a land card`, `Choose an artifact card with mana value less than or equal to that damage`, `Choose an enchantment you control to return to its owner's hand`, `choose any number of artifact creatures with total mana value 6 or less.`, `Choose any number of cards with total mana value X or less from your graveyard to your hand, where X is the total of those results`, `Choose any number of creature cards with total power up to this creature's power`, `Choose any number of creatures you control`, `Choose any number of non-Angel creatures you control`, `Choose any number of nontoken artifacts and creatures you control`, `Choose any number of other nonland permanents you control`, `Choose any number of other nontoken creatures you control`, `Choose two cards for the graveyard`, `Choose two cards for the hand`, `Choose two creature cards milled this way`, `Choose up to two nonland permanents you control to return to their owner's hand`, `Exile with CARDNAME`, `Pick 1 on the top of library`, `Put an instant, sorcery, or Faerie card from among the milled cards into your hand`, `Return a card from your graveyard to your hand for each Mines of Moria vote`, `Return a creature or planeswalker card milled this way to your hand`, `Select a card exiled with CARDNAME that shares a name with the played card`, `Select a card in a graveyard`, `Select a card in your graveyard`, `Select a card in your hand to exile with a number of time counters equal to its mana value`, `Select a card in your hand to put on top of your library`, `Select a card to be put into the hand of CARDNAME's controller`, `Select a card to put into your graveyard`, `Select a card to put into your hand`, `Select a card to put onto the battlefield`, `Select a card to put onto the battlefield tapped`, `Select a card to put onto the graveyard`, `Select a commander`, `Select a commander you own`, `Select a creature card exiled with CARDNAME`, `Select a creature card in a graveyard`, `Select a creature card in the graveyard of that creature's owner`, `Select a creature card milled this way`, `Select a land card in targeted opponent's graveyard`, `Select a land to put onto the battlefield tapped under an opponent's control`, `Select a land you control to return to its owner's hand`, `Select a legendary creature card in your hand`, `Select a permanent from among the milled cards`, `Select an artifact creature card or Vehicle card milled this way`, `Select an artifact or creature card in your hand`, `Select an instant or sorcery card from your hand`, `Select another artifact you control`, `Select another creature you control`, `Select another target creature you control`, `Select any number of creature cards milled this way`, `Select any number of other nonland permanents you own and control`, `Select one or more creature cards from your graveyard`, `Select two cards for the graveyard`, `Select two cards for the hand`, `Select two cards to be put into the graveyard of CARDNAME's controller`, `Select two cards to shuffle into the library`, `Select two lands to put onto the battlefield tapped under your control`, `Select up to one creature card milled this way`, `Select up to two basic land cards and or Desert cards`, `Select up to two creature and/or land cards from your graveyard to return to your hand`, `Select up to two creature cards from your graveyard to return to your hand`, `Select up to two instant and/or sorcery cards from your graveyard to return to your hand`, `Select up to two Rat creature cards`, `Select up to two target creature cards with mana value 2 or less to return to the battlefield`, `Select up to X basic land cards`, `Select up to X creature cards from your graveyard to exile`, `You may choose a land you control to return to its owner's hand`, `You may choose a permanent card milled this way`, `You may exile a creature card from among the cards milled this way.`, `You may put a card from among them into your hand`, `You may put a card with X in its mana cost from among them into your hand`, `You may put a permanent card from among the milled cards into your hand`, `You may put an artifact card from among them into your hand`, `You may put an artifact card with mana value 2 or 3 from among the milled cards into your hand`, `You may put an artifact, creature, or land card from among the milled cards into your hand`, `You may put an Elf or land card from among the milled cards into your hand`, `You may select a creature card`, `You may select a creature card among the cards milled this way`, `You may select a creature card and/or a land card.`, `You may select a creature or land card`, `You may select a land card`, `You may select a land card milled this way`, `You may select a permanent card`, `You may select a permanent card milled this way`, `You may select a permanent milled this way`, `You may select a Plains card or a creature card with mana value 3 or less`, `You may select a Saga card and/or a land card.`, `You may select a Vampire card from your hand`, `You may select an artifact card from the cards you milled`, `You may select an instant or sorcery card`, `You may select any number of legendary and/or enchantment cards.`, `You may select up to two creature and/or land cards`, `You may select up to two creature cards`
- `ShareLandType$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `Shuffle$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `ShuffleChangedPile$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShuffleNonMandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SpeTgtPrompt$`: TODO: Describe this parameter.
  Observed values: `Select target creature you control`
- `StackDescription$`: TODO: Describe this parameter.
- `StaticEffect$`: TODO: Describe this parameter.
  Observed values: `Animate`
- `StaticEffectCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `StaticEffectSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AddCounter`, `AgyremCleanup`, `Animate`, `AttachAura`, `Aurify`, `BPaid`, `BronzeExchange`, `CantBlockEffect`, `CastFound`, `CastFromLibrary`, `CastOneExiled`, `CheckWin`, `ChooseP`, `ChooseRandom`, `ChooseZero`, `CleanupMemory`, `CloakEach`, `CloneArmy`, `ConjurerReturn`, `CopyYou`, `CostNotPaid`, `DBAdd`, `DBAddendum`, `DBAddMana`, `DBAddTrigger`, `DBAddTurn`, `DBAmass`, `DBAnimate`, `DBAnimate2`, `DBAnimatePerpetual`, `DBArtifact`, `DBAttach`, `DBBattlefield`, `DBBlight`, `DBBodySnatcherReturnCreature`, `DBBolster`, `DBBottom`, `DBBounce`, `DBBranch`, `DBCandlesDraw`, `DBCast`, `DBChange`, `DBChange2`, `DBChangeAll`, `DBChangeSorcery`, `DBChangeTwo`, `DBChangeZone`, `DBChangeZone1`, `DBChangeZone2`, `DBChangeZoneAll`, `DBChangeZoneDinosaur`, `DBChangeZoneHand`, `DBChangeZoneMerfolk`, `DBChangeZoneVampire`, `DBChoice`, `DBChoose`, `DBChooseCard`, `DBChooseCounter`, `DBChooseOpp`, `DBChoosePlayer`, `DBChooseSb`, `DBChooseSource`, `DBChooseTopLibrary`, `DBClash`, `DBCleanEff`, `DBCleanMinus`, `DBCleanup`, `DBCleanup2`, `DBCleanupAndBounce`, `DBCleanupOne`, `DBClearImprinted`, `DBClearRemembered`, `DBCloak`, `DBClone`, `DBCloneSK`, `DBConjure`, `DBConnive`, `DBCopy`, `DBCopy1`, `DBCopyCast`, `DBCopyPermanent`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDealDamageAll`, `DBDealDmg`, `DBDelayedTrigger`, `DBDelayEffect`, `DBDelayTrig`, `DBDelayTrigger`, `DBDelTrig`, `DBDermoplasmBounce`, `DBDermoplasmCleanup`, `DBDestroy`, `DBDestroyAll`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDiscard2`, `DBDiscover`, `DBDmg`, `DBDraft`, `DBDrain`, `DBDrainN`, `DBDraw`, `DBDrawYou`, `DBDread`, `DBEffect`, `DBEffect2`, `DBEmpty`, `DBEnchant`, `DBEnduringDraw`, `DBEnergy`, `DBEvokePlay`, `DBExile`, `DBExile2`, `DBExileAll`, `DBExileB`, `DBExileG`, `DBExileR`, `DBExileSelf`, `DBExileTopCard`, `DBExileU`, `DBExplore`, `DBExtraLoyaltyEffect`, `DBFlip`, `DBFog`, `DBFood`, `DBForEach`, `DBForest`, `DBGainControl`, `DBGainLife`, `DBGainLife19`, `DBGetLandsAll`, `DBGraveyard`, `DBHand`, `DBHaste`, `DBImmediateTrig`, `DBImmediateTrig1`, `DBImmediateTrig2`, `DBImmediateTrigger`, `DBIncubate`, `DBInitiative`, `DBIntensify`, `DBInvestigate`, `DBIsland`, `DBKeep`, `DBKnowledgePlaySpell`, `DBLand`, `DBLearn`, `DBLose`, `DBLoseEffect`, `DBLoseGame`, `DBLoseLife`, `DBLoseLifeYou`, `DBMakeCard`, `DBMana`, `DBManifest`, `DBMayCast`, `DBMayPlay`, `DBMesmericCleanup`, `DBMill`, `DBMonarch`, `DBMountain`, `DBMoveSb`, `DBMoveToBottom`, `DBName`, `DBNameCard`, `DBOmenPlay`, `DBOpenAttraction`, `DBOppSearch`, `DBOptionalSearch`, `DBPartyReturn`, `DBPass`, `DBPerpetual`, `DBPirateDraw`, `DBPlay`, `DBPlayerTarget`, `DBPlayExiled`, `DBPlayIt`, `DBPlaySpell`, `DBPlot`, `DBProliferate`, `DBProtection`, `DBPump`, `DBPut`, `DBPutCounter`, `DBPutCounterAll`, `DBPutCounters`, `DBPutLoyalty`, `DBRansom`, `DBRemember1`, `DBRemember2`, `DBRemember3`, `DBRemember4`, `DBRemove`, `DBReorder`, `DBRepeat`, `DBRepeatEach`, `DBRepeatPlayer`, `DBReset`, `DBResetCounter`, `DBRestOnBottom`, `DBRestRandomOrder`, `DBResurrection`, `DBReturn`, `DBReturn2`, `DBReturnAnyTwo`, `DBReturnCorrupted`, `DBReturnCreature`, `DBReturnOpp`, `DBReturnSelf`, `DBRevealUntilShare`, `DBRevive`, `DBReviveLife`, `DBRoll`, `DBRollDice`, `DBRonaLand`, `DBRonaPlay`, `DBSac`, `DBSacrifice`, `DBScry`, `DBSearch`, `DBSearch1`, `DBSearch2`, `DBSearchAgain`, `DBSearchBis`, `DBSeek`, `DBSetLife`, `DBShuffle`, `DBShuffleAll`, `DBShuffleChanged`, `DBShuffleGrave`, `DBSkipDraw`, `DBSpace`, `DBSurveil`, `DBSuspect`, `DBSwamp`, `DBSyphonLife`, `DBToGrave`, `DBToken`, `DBTransform`, `DBTreasure`, `DBTrigger`, `DBTurnFaceUp`, `DBTwoPiles`, `DBUnAnte`, `DBUnearthed`, `DBUntap`, `DBVengefulRebirthCleanup`, `DBVengefulRebirthDamage`, `DBVenture`, `DBWin`, `DBYouChoose`, `DDCopy`, `DeadeyeReturn`, `DeathrenderAttach`, `DecreaseSpeed`, `DelayedReturn`, `DelTrig`, `DelTrigEffect`, `DelTrigSlowtrip`, `Draw`, `DrawAbstainers`, `ElkinEffect`, `Enchantment`, `EqualTransmute`, `ETBExileCleanup`, `ETBExileSacrifice`, `ExchangeOwn2`, `ExileAll`, `ExileAllYard`, `ExileEffect`, `ExileGrave`, `ExileHand`, `ExileLib`, `ExileRest`, `ExileSelf`, `ExileTwo`, `ExileWithoutFly`, `ExileYard`, `FindCMC1`, `FindCMC2`, `GainControl`, `GetEnergy`, `GiveSuspend`, `HierophantChange`, `Instant`, `InvocationDBReturn`, `LibraryCheck`, `LoopTgts`, `LuckCounter`, `MoveSelf`, `MoveToBattlefield`, `MoveToYard`, `MyMagic`, `NemesisToken`, `NotPoisoned`, `ObzedatPump`, `OppDraw`, `PayForTransmute`, `Planeswalker`, `RandomHand`, `ReitoPump`, `RememberSpell`, `Replaneswalk`, `RestBottom`, `RestorationReturn`, `ReturnB`, `ReturnG`, `ReturnR`, `ReturnToHand`, `ReturnU`, `RPaid`, `SacLand`, `SacSelf`, `ScionCopy`, `ScytheAttach`, `ShuffleRest`, `SkipTurn`, `SmuggleIn`, `Sorcery`, `TabletToExile2`, `TabletToExile3`, `TabletToGraveyard`, `TakeOutTheTrash`, `TgtOpp`, `TheftEffect`, `TheyLose`, `TimeInGates`, `ToBattlefieldTapped`, `ToHand`, `Token`, `TokenPlus`, `TotemEffect`, `TrenchAnimate`, `TrigAuraReturn`, `TrigBranch`, `TrigDelay`, `TrigDraw`, `TrigExplore`, `TrigFlip`, `TrigImmediateTrig`, `TrigInvestigate`, `TrigLife`, `TrigReturn`, `TrigSearchPlay`, `TrigTempt`, `TrigToken`, `UnscytheDBToken`, `Wallflower`, `WonTwoDome`, `YouAreCommander`, `YouDraw`, `YouGetTheRest`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE111`, `GE2`, `GE3`, `GE5`, `GE6`, `GE7`, `GE8`, `GEY`, `GT0`, `GTY`, `LE1`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `TriggeredPlayer`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `6`, `MaxTargets`, `MaxTgt`, `MaxTgts`, `NrBlackAtCasting`, `OneEach`, `X`, `XKicked`, `XX`, `Y`, `Yard`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `OneEach`, `X`, `Y`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredTarget`
- `TargetsWithDifferentCMC$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDifferentControllers$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDifferentNames$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithSameController$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithSameCreatureType$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell.OppCtrl`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `You`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Exile`, `Battlefield,Graveyard`, `Battlefield,Stack`, `Battlefield,Stack,Graveyard`, `Exile`, `Graveyard`, `Stack`, `Stack,Battlefield`
- `ThisDefinedAndTgts$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Self`, `TopOfLibrary`, `TriggeredNewCardLKICopy`
- `Transformed$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `Unimprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 PayLife<3>`, `2`, `3`, `3 B`, `DamageYou<3>`, `Discard<1/Card>`, `Discard<1/Creature>`, `ExileFromGrave<4/Card.namedDragon's Approach> ExileFromStack<1/Card.Self>`, `PayEnergy<X>`, `PayLife<2>`, `PayLife<3>`, `PayLife<4>`, `PayLife<X>`, `Sac<1/Creature.Other/other creature>`, `Sac<1/Creature>`, `Sac<1/Land>`, `SubCounter<2/OIL>`, `U U U`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Remembered`, `RememberedController`, `Targeted`, `TargetedController`, `TriggeredCardController`, `TriggeredPlayer`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `another creature`, `another creature you control`, `artifact or creature card with mana value 2 or less in your graveyard`, `artifact, creature, or non-Aura enchantment card with mana value 3 or less in your graveyard`, `Aura or Equipment card in your graveyard`, `card in a graveyard`, `card in a graveyard.`, `Choose instant or sorcery card in an opponent's graveyard`, `creature card in your graveyard`, `creature card in your graveyard with mana value lessr than or equal to the amount of life you gained this turn`, `creature card with mana value 3 or less in your graveyard`, `creature with power 2 or less`, `creature you control`, `instant or sorcery card in your graveyard`, `non-Pilot creature you control`, `noncreature, nonland card in your graveyardd`, `nonland permanent`, `nonland permanent an opponent controls with mana value less than or equal to the number of colors of mana spent to cast this creature`, `nonland permanent card in your graveyard`, `nonland permanent card with mana value 3 or less in your graveyard`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Ally.YouCtrl`, `Arcane`, `Arcane.YouCtrl`, `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment`, `Artifact,Creature,Enchantment,Planeswalker`, `Artifact,Creature,Land`, `Artifact,Enchantment`, `Artifact,Enchantment,Creature.powerGE4`, `Artifact,Enchantment,Creature.withFlying`, `Artifact,Enchantment,Land`, `Artifact,Instant,Sorcery`, `Artifact,Land`, `Artifact.cmcGE1,Creature.cmcGE1`, `Artifact.cmcLE1+YouCtrl`, `Artifact.cmcLE2+YouOwn,Creature.cmcLE2+YouOwn`, `Artifact.cmcLE3+YouCtrl`, `Artifact.cmcLEX+YouOwn`, `Artifact.cmcLEX+YouOwn,Enchantment.cmcLEX+YouOwn`, `Artifact.cmcLEX+YouOwn,Enchantment.cmcLEX+YouOwn+nonAura`, `Artifact.cmcLEX,Creature.cmcLEX,Enchantment.cmcLEX`, `Artifact.cmcLTX+YouCtrl`, `Artifact.ControlledBy Spawner>TriggeredTarget,Enchantment.ControlledBy Spawner>TriggeredTarget`, `Artifact.Creature+YouCtrl`, `Artifact.Legendary,Land.Legendary`, `Artifact.nonCreature+cmcLE1+YouCtrl`, `Artifact.nonCreature+YouCtrl`, `Artifact.OppCtrl`, `Artifact.OppCtrl+!token,Creature.OppCtrl+!token,Enchantment.OppCtrl+!token`, `Artifact.OppCtrl+cmcGE3,Creature.OppCtrl+cmcGE3,Enchantment.OppCtrl+cmcGE3`, `Artifact.OppCtrl+cmcLE3,Creature.OppCtrl+cmcLE3`, `Artifact.OppCtrl,Creature.OppCtrl`, `Artifact.OppCtrl,Creature.OppCtrl,Enchantment.OppCtrl`, `Artifact.OppCtrl,Enchantment.OppCtrl`, `Artifact.OppCtrl,Enchantment.OppCtrl,Creature.OppCtrl+tapped`, `Artifact.OppOwn+ThisTurnEnteredFrom_Library,Creature.OppOwn+ThisTurnEnteredFrom_Library`, `Artifact.Other`, `Artifact.Other+YouCtrl`, `Artifact.Other,Creature.Other`, `Artifact.YouCtrl`, `Artifact.YouCtrl+cmcLE3`, `Artifact.YouCtrl+cmcLE3,Creature.YouCtrl+cmcLE3`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl,Enchantment.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouCtrl,Enchantment.YouCtrl`, `Artifact.YouOwn`, `Artifact.YouOwn+cmcLE3,Creature.YouOwn+cmcLE3,Enchantment.nonAura+YouOwn+cmcLE3`, `Artifact.YouOwn+cmcLEX`, `Artifact.YouOwn+cmcLEX,Creature.YouOwn+cmcLEX`, `Artifact.YouOwn,Creature.YouOwn`, `Artifact.YouOwn,Creature.YouOwn,Enchantment.YouOwn`, `Artifact.YouOwn,Enchantment.nonAura+YouOwn`, `Artifact.YouOwn,Enchantment.YouOwn`, `Artifact.YouOwn,Enchantment.YouOwn,Card.Legendary+YouOwn`, `Artifact.YouOwn,Enchantment.YouOwn,Planeswalker.YouOwn`, `Aura`, `Aura.AttachedTo Creature`, `Aura.CanEnchantEquippedBy+YouOwn,Equipment.CanEnchantEquippedBy+YouOwn`, `Aura.Other.YouOwn,Equipment.YouOwn`, `Aura.YouCtrl,Equipment.YouCtrl`, `Aura.YouOwn`, `Aura.YouOwn,Equipment.YouOwn`, `Bat.YouOwn,Lizard.YouOwn,Rat.YouOwn,Squirrel.YouOwn`, `Boar.YouOwn`, `Bolas`, `Card`, `Card.AdventureCard+YouDontOwn`, `Card.AdventureCard+YouOwn`, `Card.Artifact+YouOwn`, `Card.Artifact+YouOwn,Card.Enchantment+YouOwn`, `Card.Assassin+YouCtrl,Card.withFreerunning+YouCtrl`, `Card.Aura+YouCtrl+cmcLE3,Card.Equipment+YouCtrl+cmcLE3`, `Card.Aura+YouCtrl,Card.Equipment+YouCtrl`, `Card.Black+YouCtrl`, `Card.Black+YouOwn`, `Card.Blue+YouOwn`, `Card.ChosenType+YouOwn`, `Card.cmcLE4`, `Card.Creature`, `Card.Creature+cmcLE2+YouCtrl`, `Card.Creature+cmcLE2+YouOwn`, `Card.Creature+cmcLE3+YouOwn`, `Card.Creature+ThisTurnEnteredFrom_Battlefield`, `Card.Creature+ThisTurnEnteredFrom_Battlefield+YouOwn`, `Card.Creature+YouCtrl`, `Card.Creature+YouOwn,Card.Land+YouOwn,Card.Planeswalker+YouOwn`, `Card.Creature,Card.Planeswalker`, `Card.DefenderCtrl`, `Card.DiscardedThisTurn,Card.ThisTurnEnteredFrom_Library`, `Card.Enchantment+YouOwn`, `Card.Equipment+YouCtrl`, `Card.ExiledWithSource`, `Card.faceUp`, `Card.Green+YouCtrl`, `Card.Green+YouOwn`, `Card.Historic+nonAssassin+YouOwn`, `Card.Historic+YouCtrl`, `Card.Historic+YouOwn`, `Card.Instant+YouOwn`, `Card.Instant,Card.Sorcery`, `Card.inZoneStack`, `Card.inZoneStack+Creature,Card.inZoneStack+Planeswalker`, `Card.inZoneStack+Red,Card.inZoneStack+Green,Permanent.Red,Permanent.Green`, `Card.inZoneStack,Permanent.nonLand,Card.inZoneGraveyard`, `Card.IsCommander+YouOwn`, `Card.Knight+YouOwn`, `Card.Land+YouOwn`, `Card.MultiColor`, `Card.MultiColor+YouCtrl`, `Card.MultiColor+YouOwn`, `Card.Myr+YouCtrl`, `Card.namedGroffskithur`, `Card.nonBasic`, `Card.nonBasic+OppOwn`, `Card.nonCreature`, `Card.nonCreature+nonLand+cmcLTX`, `Card.nonCreature+nonLand+YouCtrl`, `Card.nonCreature+nonLand+YouOwn`, `Card.nonLand`, `Card.nonLand+ThisTurnEntered`, `Card.nonLand+YouCtrl`, `Card.nonLand+YouOwn`, `Card.nonLegendary+YouOwn`, `Card.OppOwn`, `Card.Other`, `Card.Outlaw+YouOwn`, `Card.Permanent+YouOwn`, `Card.Pirate+YouCtrl`, `Card.Planeswalker+YouOwn`, `Card.Red+YouOwn`, `Card.Skeleton,Card.Vampire,Card.Zombie`, `Card.Sorcery`, `Card.Sorcery+YouOwn`, `Card.White+YouOwn`, `Card.withFlashback+YouOwn`, `Card.withKicker+YouOwn,Card.withMultikicker+YouOwn`, `Card.withWarp`, `Card.Wizard+YouCtrl`, `Card.YouCtrl`, `Card.YouCtrl+AdventureCard`, `Card.YouCtrl+cmcGE4`, `Card.YouCtrl+withAwaken`, `Card.YouCtrl+withCycling,Card.YouCtrl+withTypeCycling`, `Card.YouDontCtrl`, `Card.YouOwn`, `Card.YouOwn+cmcGE3`, `Card.YouOwn+nonCreature+nonLand`, `Card.YouOwn+nonLand+cmcLE3`, `Card.YouOwn+Other`, `Card.YouOwn+withCycling,Card.YouOwn+withTypeCycling`, `Card.YouOwn+withFlashback`, `Card.YouOwn+withForetell`, `Card.Zombie+YouCtrl`, `Cave.YouOwn`, `Cleric.cmcLTX+YouOwn`, `Creature`, `Creature,Artifact`, `Creature,Card.inZoneStack`, `Creature,Enchantment`, `Creature,Land`, `Creature,Planeswalker`, `Creature,Spacecraft`, `Creature,Vehicle`, `Creature,Vehicle,Land.nonBasic`, `Creature.!token`, `Creature.!token+OppCtrl`, `Creature.!token+Other`, `Creature.!token+YouCtrl`, `Creature.Ally+YouCtrl`, `Creature.Angel+YouCtrl,Creature.Human+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.Assassin+YouCtrl`, `Creature.Assassin+YouOwn`, `Creature.attacking`, `Creature.attacking+nonWhite`, `Creature.attacking+OppCtrl`, `Creature.attacking+Other+YouCtrl`, `Creature.attacking+YouDontCtrl`, `Creature.attacking,Creature.blocking`, `Creature.attackingYou`, `Creature.attackingYou+withoutFlying`, `Creature.attackingYouOrYourPW`, `Creature.Black`, `Creature.Black+YouCtrl`, `Creature.Black+YouOwn`, `Creature.Black,Planeswalker.Red,Creature.Red,Planeswalker.Black`, `Creature.blockedValidThisTurn Zombie,Creature.blockedByValidThisTurn Zombie`, `Creature.blockingCreatureYouCtrl`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.Blue+YouCtrl,Creature.Green+YouCtrl`, `Creature.Blue+YouCtrl,Creature.Red+YouCtrl`, `Creature.Blue+YouOwn`, `Creature.ChosenType`, `Creature.Cleric`, `Creature.Cleric+YouOwn,Creature.Rogue+YouOwn,Creature.Warrior+YouOwn,Creature.Wizard+YouOwn`, `Creature.cmcEQ1+YouCtrl`, `Creature.cmcEQX`, `Creature.cmcEQX+YouOwn`, `Creature.cmcGE3`, `Creature.cmcLE1+YouCtrl`, `Creature.cmcLE1+YouOwn`, `Creature.cmcLE2`, `Creature.cmcLE3`, `Creature.cmcLE3+OppCtrl`, `Creature.cmcLE3+YouCtrl`, `Creature.cmcLE3+YouDontCtrl`, `Creature.cmcLE3+YouOwn`, `Creature.cmcLE4`, `Creature.cmcLE4+YouOwn`, `Creature.cmcLEX`, `Creature.cmcLEX+YouCtrl`, `Creature.cmcLEX+YouOwn`, `Creature.cmcLEX+YouOwn+nonBear+Other`, `Creature.cmcLEY+YouOwn`, `Creature.cmcLTX+YouOwn`, `Creature.cmcLTX+YouOwn+NotDefinedTriggeredCard`, `Creature.Colorless`, `Creature.ControlledBy Spawner>TriggeredDefendingPlayer+powerLTX`, `Creature.ControlledBy TriggeredTarget`, `Creature.counters_GE1_FATE`, `Creature.counters_GE1_M1M1`, `Creature.counters_GE1_STUN`, `Creature.CrewedThisTurn`, `Creature.dealtDamageToYouThisTurn`, `Creature.DefenderCtrl`, `Creature.Dragon+YouCtrl,Planeswalker.Ugin+YouCtrl`, `Creature.Eldrazi+YouOwn`, `Creature.Elemental+YouCtrl+toughnessLTX`, `Creature.ExiledWithSource`, `Creature.ExiledWithSource+cmcEQX`, `Creature.Fungus+YouOwn`, `Creature.greatestPower`, `Creature.Green`, `Creature.Green+OppCtrl,Creature.White+OppCtrl`, `Creature.Green+YouOwn`, `Creature.HasCounters`, `Creature.Human+YouOwn`, `Creature.inZoneBattlefield`, `Creature.IsRemembered+ExiledWithSource+cmcEQX`, `Creature.IsRemembered,Planeswalker.IsRemembered`, `Creature.Land`, `Creature.Legendary`, `Creature.Legendary+cmcLTX+YouOwn`, `Creature.Legendary+YouCtrl`, `Creature.milledThisTurn`, `Creature.MultiColor,Enchantment.MultiColor`, `Creature.Ninja+YouOwn,Creature.Rogue+YouOwn`, `Creature.NoAbilities+YouOwn`, `Creature.nonAngel+YouCtrl`, `Creature.nonArtifact`, `Creature.nonArtifact+YouCtrl`, `Creature.nonAssassin`, `Creature.nonBlack`, `Creature.nonDragon`, `Creature.nonFox+Other`, `Creature.nonHuman+YouOwn`, `Creature.nonLegendary`, `Creature.nonLegendary+YouCtrl`, `Creature.nonLegendary+YouOwn`, `Creature.nonOoze+OppCtrl`, `Creature.nonPilot+YouCtrl`, `Creature.nonSalamander`, `Creature.nonSpacecraft`, `Creature.nonSpirit`, `Creature.nonWarrior+YouCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl+cmcGE4`, `Creature.OppCtrl+cmcLE3`, `Creature.OppCtrl+powerGE3`, `Creature.OppCtrl+powerGTX`, `Creature.OppCtrl+powerLTTriggeredCard$CardPower`, `Creature.OppCtrl+tapped`, `Creature.OppCtrl,Enchantment.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.OppCtrl,Vehicle.OppCtrl`, `Creature.OppOwn`, `Creature.OppOwn+cmcEQX`, `Creature.OppOwn+cmcEQX,Artifact.OppOwn+cmcEQX`, `Creature.Other`, `Creature.Other+!TriggeredNewCard+toughnessLTX+YouOwn`, `Creature.Other+tapped,Vehicle.Other+tapped`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl,Artifact.Other+YouCtrl`, `Creature.Other+YouOwn`, `Creature.Other,Artifact.Other`, `Creature.Other,Planeswalker`, `Creature.OwnedBy Spawner>TriggeredTarget`, `Creature.OwnedBy TriggeredDefendingPlayer`, `Creature.powerEQ1+YouOwn+Other,Creature.toughnessEQ1+YouOwn+Other`, `Creature.powerGE3`, `Creature.powerGE4`, `Creature.powerGE5`, `Creature.powerGEX`, `Creature.powerLE1,Creature.toughnessLE1`, `Creature.powerLE2`, `Creature.powerLE2+YouCtrl`, `Creature.powerLE3`, `Creature.powerLEX+YouOwn`, `Creature.powerLEX+YouOwn+nonRogue+Other`, `Creature.powerLTX+YouOwn`, `Creature.Red`, `Creature.Red+YouCtrl,Creature.White+YouCtrl,Creature.Black+YouCtrl`, `Creature.Red+YouOwn`, `Creature.Red,Creature.Green`, `Creature.RememberedPlayerCtrl,Creature.ControlledBy Opponent.IsCorrupted`, `Creature.Spirit,Creature.withDisturb,Enchantment`, `Creature.tapped`, `Creature.tapped+OppCtrl`, `Creature.ThisTurnEntered`, `Creature.ThisTurnEnteredFrom_Battlefield+OppCtrl`, `Creature.toughnessGE3`, `Creature.toughnessGE4`, `Creature.toughnessLE2+ControlledBy TriggeredDefendingPlayer`, `Creature.toughnessLE5`, `Creature.Vampire+YouCtrl,Creature.Wizard+YouCtrl`, `Creature.White+attacking,Creature.White+blocking`, `Creature.White+YouCtrl,Creature.Black+YouCtrl`, `Creature.White+YouOwn`, `Creature.withFlying`, `Creature.withInfect+YouOwn`, `Creature.withoutFlying`, `Creature.withoutFlying+attackingYou`, `Creature.withShadow+Other`, `Creature.Wolf,Creature.Werewolf`, `Creature.YouCtrl`, `Creature.YouCtrl+Black,Creature.YouCtrl+Green`, `Creature.YouCtrl+ChosenType`, `Creature.YouCtrl+cmcEQX`, `Creature.YouCtrl+cmcLE2`, `Creature.YouCtrl+cmcLE3`, `Creature.YouCtrl+cmcLEX`, `Creature.YouCtrl+cmcLTX`, `Creature.YouCtrl+cmcLTX,Equipment.YouCtrl+cmcLTX`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other,Artifact.YouCtrl+Other`, `Creature.YouCtrl+powerLE1`, `Creature.YouCtrl+powerLE2`, `Creature.YouCtrl+powerLTZ`, `Creature.YouCtrl+tapped`, `Creature.YouCtrl+withMutate`, `Creature.YouCtrl+withoutFlying`, `Creature.YouCtrl,Artifact.YouCtrl`, `Creature.YouCtrl,Enchantment.YouCtrl`, `Creature.YouCtrl,Land.YouCtrl`, `Creature.YouCtrl,Planeswalker.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl,Enchantment.YouDontCtrl`, `Creature.YouDontCtrl,Planeswalker.YouDontCtrl`, `Creature.YouOwn`, `Creature.YouOwn+!TriggeredCard`, `Creature.YouOwn+cmcEQX`, `Creature.YouOwn+cmcLE2`, `Creature.YouOwn+cmcLE2,Vehicle.YouOwn+cmcLE2`, `Creature.YouOwn+cmcLE3`, `Creature.YouOwn+cmcLE3+Other`, `Creature.YouOwn+cmcLE3,Artifact.YouOwn+cmcLE3`, `Creature.YouOwn+cmcLE5,Spacecraft.YouOwn+cmcLE5`, `Creature.YouOwn+cmcLEX`, `Creature.YouOwn+cmcLEX+Other`, `Creature.YouOwn+Knight`, `Creature.YouOwn+nonLegendary`, `Creature.YouOwn+nonLegendary+cmcEQX`, `Creature.YouOwn+nonLegendary+ThisTurnEnteredFrom_Battlefield`, `Creature.YouOwn+Other`, `Creature.YouOwn+Outlaw`, `Creature.YouOwn+powerLE2`, `Creature.YouOwn+powerLE3`, `Creature.YouOwn+powerLTCount$CardPower`, `Creature.YouOwn+ThisTurnEnteredFrom_Battlefield`, `Creature.YouOwn+White`, `Creature.YouOwn,Battle.YouOwn`, `Creature.YouOwn,Enchantment.YouOwn`, `Creature.YouOwn,Food.YouOwn`, `Creature.YouOwn,Land.YouOwn`, `Creature.YouOwn,Planeswalker.YouOwn`, `Creature.YouOwn,Spacecraft.YouOwn`, `Creature.YouOwn,Vehicle.YouOwn`, `Creature.Zombie`, `Creature.Zombie+Other`, `Dinosaur.YouOwn`, `Elf.Other+YouOwn`, `Elf.Other+YouOwn,Tyvar.Other+YouOwn`, `Elf.YouOwn`, `Enchantment`, `Enchantment,Artifact.tapped,Creature.tapped`, `Enchantment,Creature`, `Enchantment.Creature+YouCtrl`, `Enchantment.nonAura+YouCtrl`, `Enchantment.nonCreature,Artifact.nonCreature`, `Enchantment.OppOwn+cmcLEX,Instant.OppOwn+cmcLEX,Sorcery.OppOwn+cmcLEX`, `Enchantment.YouCtrl`, `Enchantment.YouCtrl+nonGod`, `Enchantment.YouCtrl+Other`, `Enchantment.YouOwn`, `Equipment.AttachedTo ParentTarget`, `Equipment.YouCtrl`, `Equipment.YouOwn`, `Equipment.YouOwn,Vehicle.YouOwn`, `Goblin.YouCtrl`, `Goblin.YouOwn`, `Griffin.YouCtrl`, `Host.YouOwn,Card.YouOwn+withAugment`, `Human.YouCtrl`, `Instant,Sorcery`, `Instant,Sorcery,Creature`, `Instant.Blue+YouCtrl`, `Instant.cmcEQX+OwnedBy TriggeredTarget,Sorcery.cmcEQX+OwnedBy TriggeredTarget`, `Instant.cmcEQX+YouCtrl,Sorcery.cmcEQX+YouCtrl`, `Instant.cmcLE3+YouOwn,Sorcery.cmcLE3+YouOwn`, `Instant.inZoneGraveyard+YouCtrl,Sorcery.inZoneGraveyard+YouCtrl,Card.withFlashback+inZoneExile+YouCtrl`, `Instant.MonoColor+YouOwn,Sorcery.MonoColor+YouOwn`, `Instant.OppCtrl,Sorcery.OppCtrl`, `Instant.OppOwn,Sorcery.OppOwn`, `Instant.YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl,Creature.YouCtrl`, `Instant.YouOwn`, `Instant.YouOwn+cmcLE2,Sorcery.YouOwn+cmcLE2`, `Instant.YouOwn+cmcLEX,Sorcery.YouOwn+cmcLEX`, `Instant.YouOwn+withCycling,Instant.YouOwn+withTypeCycling,Sorcery.YouOwn+withCycling,Sorcery.YouOwn+withTypeCycling`, `Instant.YouOwn,Sorcery.YouOwn`, `Instant.YouOwn,Sorcery.YouOwn,Planeswalker.Tamiyo+YouOwn`, `Instant.YouOwn,Sorcery.YouOwn,Spirit.YouOwn`, `Island`, `Kavu`, `Land`, `Land.Basic`, `Land.Basic+YouCtrl`, `Land.Basic+YouOwn`, `Land.milledThisTurn`, `Land.nonBasic`, `Land.nonSnow+YouCtrl`, `Land.YouCtrl`, `Land.YouOwn`, `Mercenary`, `Mercenary.YouCtrl`, `Mount.YouOwn,Vehicle.YouOwn`, `Mountain`, `Ninja.YouCtrl`, `Opponent`, `Permanent`, `Permanent,Card.inZoneStack`, `Permanent.!enchanted`, `Permanent.!token`, `Permanent.!token+YouCtrl`, `Permanent.Bird,Permanent.Cleric`, `Permanent.Black`, `Permanent.Black+ControlledBy TriggeredTarget,Permanent.Red+ControlledBy TriggeredTarget`, `Permanent.Black,Permanent.Red`, `Permanent.cmcEQ1`, `Permanent.cmcGE1,Card.inZoneStack+cmcGE1`, `Permanent.cmcGE3`, `Permanent.cmcGE4`, `Permanent.cmcLE2`, `Permanent.cmcLE3+MultiColor+YouCtrl`, `Permanent.cmcLE3+YouCtrl`, `Permanent.ControlledBy TriggeredTarget`, `Permanent.Dragon+YouOwn`, `Permanent.enchanted`, `Permanent.ExiledWithSource+cmcEQX`, `Permanent.Historic+YouCtrl`, `Permanent.Historic+YouCtrl+Other`, `Permanent.Historic+YouOwn`, `Permanent.Legendary+!namedStaff of Eden; Vault's Key`, `Permanent.MonoColor`, `Permanent.nonBattle+YouCtrl`, `Permanent.nonColorless`, `Permanent.nonCreature`, `Permanent.nonCreature+nonLand+OppCtrl+cmcLE4`, `Permanent.nonCreature+nonLand+YouOwn`, `Permanent.nonCreature+nonLand+YouOwn+cmcLEX`, `Permanent.nonCreature+YouOwn`, `Permanent.nonEnchantment`, `Permanent.nonFaerie+nonLand+YouCtrl`, `Permanent.nonLand`, `Permanent.nonLand+!token`, `Permanent.nonLand+!token+YouCtrl`, `Permanent.nonLand+!token+YouDontCtrl+cmcLE4`, `Permanent.nonLand+cmcEQX`, `Permanent.nonLand+cmcEQX+YouCtrl`, `Permanent.nonLand+cmcLE1`, `Permanent.nonLand+cmcLE3+YouOwn`, `Permanent.nonLand+cmcLEX+YouOwn`, `Permanent.nonLand+ControlledBy TriggeredTarget`, `Permanent.nonLand+Historic`, `Permanent.nonLand+inZoneBattlefield,Card.suspended`, `Permanent.nonLand+nonEnchantment`, `Permanent.nonLand+nonSaga`, `Permanent.nonLand+OppCtrl`, `Permanent.nonLand+OppCtrl+!numColorsEQ2`, `Permanent.nonLand+OppCtrl+cmcLE2`, `Permanent.nonLand+OppCtrl+cmcLE3`, `Permanent.nonLand+OppCtrl+cmcLEX`, `Permanent.nonLand+OppCtrl,Card.inZoneStack+OppCtrl`, `Permanent.nonLand+Other`, `Permanent.nonLand+YouCtrl`, `Permanent.nonLand+YouCtrl+Other`, `Permanent.nonLand+YouDontCtrl`, `Permanent.nonLand+YouOwn`, `Permanent.nonLand+YouOwn+cmcLE3`, `Permanent.nonLand,Card.inZoneStack`, `Permanent.OppCtrl`, `Permanent.OppCtrl+cmcEven`, `Permanent.OppCtrl+cmcGE3`, `Permanent.OppOwn`, `Permanent.Other`, `Permanent.Other+nonLand`, `Permanent.Other+nonLand+!token`, `Permanent.Other+YouCtrl`, `Permanent.Other+YouOwn`, `Permanent.OwnedBy TriggeredTarget`, `Permanent.Rebel+YouCtrl+cmcLE5`, `Permanent.Snow+YouOwn`, `Permanent.ThisTurnEnteredFrom_Battlefield`, `Permanent.White`, `Permanent.YouCtrl`, `Permanent.YouCtrl+cmcLE3`, `Permanent.YouCtrl+cmcLE4`, `Permanent.YouCtrl+nonLand`, `Permanent.YouCtrl+Other`, `Permanent.YouCtrl+YouOwn`, `Permanent.YouCtrl,Permanent.YouOwn`, `Permanent.YouDontCtrl`, `Permanent.YouDontCtrl+nonLand`, `Permanent.YouOwn`, `Permanent.YouOwn+cmcLE2`, `Permanent.YouOwn+cmcLE3`, `Permanent.YouOwn+cmcLEX`, `Permanent.YouOwn+cmcLEX+NotDefinedTriggeredCard`, `Permanent.YouOwn+nonLand`, `Permanent.YouOwn+nonLand+cmcLE2`, `Permanent.YouOwn+nonLegendary`, `Permanent.YouOwn+ThisTurnEnteredFrom_Battlefield`, `Permanent.YouOwn+withCycling,Permanent.YouOwn+withTypeCycling`, `Pirate.YouOwn`, `Planeswalker.YouCtrl`, `Planeswalker.YouOwn`, `Planeswalker.YouOwn+cmcLEX`, `Plant.YouOwn,Treefolk.YouOwn,Land.YouOwn`, `Player`, `Player.Opponent`, `Player.OpponentToActive+withMoreLandsThanActive`, `Rat.YouCtrl,Card.Legendary+YouCtrl`, `Rebel.!token`, `Rebel.YouCtrl`, `Saga`, `Saga.YouCtrl,Creature.Enchantment+YouCtrl`, `Saga.YouOwn+cmcEQX`, `Skeleton,Spirit,Zombie`, `Sliver`, `Sorcery.Red+YouCtrl`, `Sorcery.YouCtrl`, `Sorcery.YouOwn`, `Spirit`, `Spirit.YouCtrl`, `Vampire.YouOwn`, `Vehicle.YouOwn`, `Villain.YouOwn`, `Zombie`, `Zombie.Creature+YouOwn`, `Zombie.YouCtrl`, `Zombie.YouOwn`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `another artifact you control`, `another creature`, `artifact card in your graveyard`, `creature card in your graveyard`, `creature with mana value 3 or less`, `creature you own`
- `WithCountersAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `Count$Valid Land.YouCtrl`, `X`, `Y`
- `WithCountersPlacer$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `WithCountersType$`: TODO: Describe this parameter.
  Observed values: `AEGIS`, `BLOOD`, `BRAIN`, `CHARGE`, `CORPSE`, `CROAK`, `DELAY`, `DREAM`, `DUTY`, `EGG`, `FETCH`, `FINALITY`, `Flying`, `Hexproof,Indestructible`, `HIT`, `ICE`, `Indestructible`, `KICK`, `Lifelink`, `M1M1`, `MANNEQUIN`, `MEMORY`, `NECRODERMIS`, `OIL`, `P1P1`, `PAGE`, `REVIVAL`, `STASH`, `STUN`, `TAKEOVER`, `TIME`, `Vigilance,Lifelink`, `VOID`
- `WithMayLook$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithNotedCounters$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithTotalCardTypes$`: TODO: Describe this parameter.
  Observed values: `4`
- `WithTotalCMC$`: TODO: Describe this parameter.
  Observed values: `4`, `6`, `X`, `Y`
- `WithTotalPower$`: TODO: Describe this parameter.
  Observed values: `Y`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `GrTo`

## `ChangeZoneAll`

TODO: Write documentation.

**Parameters:**
- `AbilityCount$`: TODO: Describe this parameter.
  Observed values: `X`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `Curse`, `DiscardAllAndRetExiled.minAdv2`, `DiscardAllAndRetExiled.noDiscard.minAdv2`, `ExileGraveyards`, `LivingDeath`, `ManifestCreatsFromGraveyard`, `RetDiscardedThisTurn`, `TimeTwister`, `Timetwister`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Sacrifice`, `YourExileUpkeep`
- `ChangeNum$`: TODO: Describe this parameter.
  Observed values: `1`, `All`
- `ChangeType$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Enchantment`, `Artifact,Land,Creature`, `Artifact.ChosenCard`, `Artifact.cmcLE2,Creature.cmcLE2`, `Artifact.cmcLE3`, `Artifact.cmcLE3,Creature.cmcLE3`, `Artifact.IsRemembered`, `Artifact.IsRemembered,Creature.IsRemembered,Land.IsRemembered`, `Artifact.IsRemembered,Creature.IsRemembered,Land.IsRemembered,Planeswalker.IsRemembered`, `Artifact.nonColorless`, `Artifact.OppCtrl`, `Artifact.TargetedPlayerOwn`, `Artifact.YouCtrl`, `Artifact.YouOwn`, `Artifact.YouOwn+cmcEQX,Creature.YouOwn+cmcEQX`, `Artifact.YouOwn,Enchantment.YouOwn`, `Artifact.YouOwn,Enchantment.YouOwn,Planeswalker.YouOwn`, `Aura.AttachedTo Targeted`, `Aura.IsRemembered`, `Card`, `Card.!IsImprinted+ExiledWithSource+YouOwn`, `Card.!IsImprinted+IsRemembered`, `Card.!IsRemembered`, `Card.Black,Card.Red`, `Card.BottomGraveyard`, `Card.BottomLibrary`, `Card.ChosenCard`, `Card.ChosenCard,Card.TargetedPlayerOwn+inZoneGraveyard`, `Card.ChosenType+YouCtrl`, `Card.ControlledBy TriggeredCardController`, `Card.counters_GE1_AEGIS`, `Card.Creature+ExiledWithSource`, `Card.Creature+IsRemembered`, `Card.Doctor`, `Card.EnchantedBy,Aura.AttachedTo Card.EnchantedBy`, `Card.Enchantment+YouCtrl+YouOwn,Card.Aura+YouOwn+AttachedTo Permanent.YouCtrl,Card.Aura+YouOwn+AttachedTo Creature.attacking+OppCtrl`, `Card.ExiledWithSource`, `Card.ExiledWithSource+!IsRemembered`, `Card.IsCommander`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.IsImprinted+!IsRemembered`, `Card.IsImprinted,Card.IsRemembered`, `Card.IsRemembered`, `Card.IsRemembered+!ChosenCard`, `Card.IsRemembered+!IsImprinted`, `Card.IsRemembered+AdventureCard`, `Card.IsRemembered+ExiledWithSource`, `Card.IsRemembered+IsImprinted`, `Card.IsRemembered+RememberedPlayerCtrl`, `Card.IsRemembered+sharesNameWith ChosenCard`, `Card.IsRemembered+YouCtrl`, `Card.IsRemembered+YouOwn`, `Card.IsRemembered,Aura.AttachedTo Targeted`, `Card.IsRemembered,Card.IsImprinted`, `Card.IsRemembered,Equipment.AttachedTo Targeted`, `Card.IsTriggerRemembered`, `Card.Knight+Creature+YouCtrl`, `Card.Land+IsRemembered`, `Card.lowestRememberedCMC`, `Card.NamedCard`, `Card.namedMyr Servitor`, `Card.nonBasic`, `Card.nonColorless+!IsRemembered`, `Card.nonCreature+nonLand+TargetedPlayerCtrl`, `Card.nonLand+YouCtrl`, `Card.NotDefinedReplacedSimultaneousETB`, `Card.OppCtrl`, `Card.OppOwn`, `Card.Other`, `Card.OwnedBy Player.NotedForStargate`, `Card.OwnedBy Player.Other`, `Card.RememberedPlayerOwn`, `Card.Self,Creature.blockedBySource`, `Card.Self,Creature.blockingSource,Creature.blockedBySource`, `Card.Self,Creature.counters_EQ0_ROPE`, `Card.Self,Creature.OppCtrl`, `Card.Self,Creature.OppCtrl,Artifact.OppCtrl`, `Card.targetedBy+ControlledBy Player.NotedForDiversion`, `Card.TargetedPlayerCtrl`, `Card.token`, `Card.TopGraveyardCreature`, `Card.TopLibrary`, `Card.TriggeredCards`, `Card.withFlashback`, `Card.YouCtrl`, `Card.YouCtrl+!IsRemembered`, `Card.YouDontOwn`, `Card.YouOwn`, `Card.YouOwn+BottomLibrary_Creature`, `Card.YouOwn+counters_GE1_INTEL`, `Card.YouOwn+DiscardedThisTurn`, `Card.YouOwn+ExiledWithSource+!IsRemembered`, `Card.YouOwn+Other`, `Card.YouOwn+Permanent`, `Creature`, `Creature,Spacecraft`, `Creature.!IsRemembered`, `Creature.!IsRemembered+!IsImprinted`, `Creature.!sharesCreatureTypeWith Convoked,Artifact,Enchantment`, `Creature.!token`, `Creature.!token+YouCtrl`, `Creature.ActivePlayerCtrl+powerGTX`, `Creature.attacking`, `Creature.Black`, `Creature.Black,Creature.Red`, `Creature.blockingRemembered,Creature.isBlockedByRemembered`, `Creature.Blue+OppCtrl`, `Creature.ChosenCard`, `Creature.ChosenColor`, `Creature.ChosenType+YouOwn`, `Creature.cmcChosenEvenOdd`, `Creature.cmcLE3+YouOwn`, `Creature.cmcLE3,Planeswalker.cmcLE3`, `Creature.cmcLEY,Planeswalker.cmcLEY`, `Creature.cmcLTX,Planeswalker.cmcLTX`, `Creature.counters_EQ0_P1P1`, `Creature.CrewedThisTurn`, `Creature.dealtDamageThisTurn`, `Creature.ExiledWithSource`, `Creature.Human+YouCtrl`, `Creature.IsNotChosenType`, `Creature.IsRemembered`, `Creature.IsRemembered+hasNonManaActivatedAbility`, `Creature.IsRemembered+ThisTurnEnteredFrom_Battlefield`, `Creature.IsRemembered,Aura.AttachedTo Creature.IsRemembered+YouCtrl`, `Creature.Legendary+YouOwn`, `Creature.nonBlue`, `Creature.nonChosenCard`, `Creature.nonDinosaur`, `Creature.nonDragon`, `Creature.nonElemental`, `Creature.nonHorror`, `Creature.nonKraken+nonLeviathan+nonMerfolk+nonOctopus+nonSerpent`, `Creature.nonKraken+nonLeviathan+nonOctopus+nonSerpent`, `Creature.nonMerfolk+nonKraken+nonLeviathan+nonOctopus+nonSerpent`, `Creature.nonPhyrexian`, `Creature.Other+YouCtrl`, `Creature.powerEven`, `Creature.powerGE4`, `Creature.powerGE5`, `Creature.powerGTX`, `Creature.powerLE2+YouCtrl`, `Creature.powerLTX`, `Creature.powerOdd`, `Creature.StrictlyOther`, `Creature.StrictlyOther+tapped`, `Creature.tapped`, `Creature.token`, `Creature.TopGraveyardCreature+DefenderCtrl`, `Creature.toughnessLEX`, `Creature.toughnessLEX+OppCtrl`, `Creature.toughnessLTX+OppCtrl`, `Creature.untapped`, `Creature.White`, `Creature.YouCtrl`, `Creature.YouOwn`, `Creature.YouOwn+cmcEQX`, `Creature.YouOwn+cmcLE2`, `Creature.YouOwn+cmcLEX`, `Creature.YouOwn+cmcLEX,Planeswalker.YouOwn+cmcLEX`, `Creature.YouOwn+namedDemigod of Revenge`, `Creature.YouOwn+TopGraveyardCreature`, `Creature.Zombie+YouCtrl`, `Effect.YouCtrl+namedCoolness Badge`, `Enchantment`, `Enchantment.Aura+YouCtrl`, `Enchantment.IsRemembered`, `Enchantment.nonAura+YouCtrl`, `Enchantment.YouOwn`, `Goblin.IsRemembered`, `Instant.IsRemembered+YouOwn,Sorcery.IsRemembered+YouOwn`, `Instant.IsRemembered,Sorcery.IsRemembered`, `Instant.YouOwn,Sorcery.YouOwn`, `Island`, `Land`, `Land.Basic`, `Land.ChosenCard`, `Land.YouCtrl`, `Land.YouOwn`, `Mount.YouOwn,Vehicle.YouOwn`, `Mountain.YouOwn`, `Nightmare`, `Nightmare.token+!IsRemembered+YouCtrl`, `Permanent`, `Permanent.!token`, `Permanent.ChosenColor`, `Permanent.ExiledWithSource`, `Permanent.ExiledWithSource+!IsImprinted`, `Permanent.Green`, `Permanent.IsCommander+TargetedPlayerCtrl`, `Permanent.IsRemembered`, `Permanent.Legendary+YouCtrl`, `Permanent.MultiColor`, `Permanent.Nightstalker+YouCtrl`, `Permanent.nonAura+ExiledWithSource`, `Permanent.nonAura+IsRemembered`, `Permanent.nonColorless+cmcLEX`, `Permanent.nonLand`, `Permanent.nonLand+!ChosenCard`, `Permanent.nonLand+!Historic`, `Permanent.nonLand+!token`, `Permanent.nonLand+cmcLE2`, `Permanent.nonLand+cmcLEX`, `Permanent.nonLand+nonCreature`, `Permanent.nonLand+nonGiant+nonWizard`, `Permanent.nonLand+nonLegendary`, `Permanent.nonLand+Other+cmcLEY`, `Permanent.nonLand+StrictlyOther`, `Permanent.nonLand+TargetedPlayerCtrl`, `Permanent.nonLand+YouDontCtrl`, `Permanent.nonLand+YouOwn+cmcLE3`, `Permanent.OppCtrl+nonLand`, `Permanent.Other`, `Permanent.Other+nonLand+ThisTurnEntered`, `Permanent.RememberedPlayerOwn`, `Permanent.YouCtrl+StrictlyOther`, `Permanent.YouOwn`, `Permanent.YouOwn+nonLand+cmcEQX`, `Planeswalker`, `Remembered`, `Remembered.Aura+White+Attached+YouOwn`, `Remembered.sameName`, `Sand.Warrior`, `Serf.token`, `Synth.YouCtrl+token`, `Targeted.sameName`, `Targeted.Self,Aura.AttachedTo Card.Self`, `Targeted.Self,Targeted.sameName`, `TargetedCard.sameName`, `TargetedCard.Self,Aura.AttachedTo Targeted`, `TargetedCard.Self,Aura.YouCtrl+AttachedTo Targeted`, `TargetedCard.Self,Card.NotDefinedTargeted+sharesNameWith Targeted`, `TargetedCard.Self,Card.NotDefinedTargeted+token+sharesNameWith Targeted+ControlledBy TargetedController`, `TargetedCard.Self,Creature.NotDefinedTargeted+sharesNameWith Targeted`, `TargetedCard.Self,Permanent.nonLand+NotDefinedTargeted+cmcEQX`, `TargetedCard.Self,Permanent.nonLand+NotDefinedTargeted+sharesNameWith Targeted+ControlledBy TargetedController`, `TargetedCard.Self,Permanent.nonLand+NotDefinedTargeted+sharesNameWith Targeted+OppCtrl`, `TargetedCard.Self,Permanent.NotDefinedTargeted+sharesNameWith Targeted`, `Triggered.sameName`, `Triggered.sameName+token`, `Warrior`, `Zombie`
- `ChangeTypeDesc$`: TODO: Describe this parameter.
  Observed values: `basic land`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `OptionalCost`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CalimNumRemembered`, `CurLife`, `MimeoNumRemembered`, `RDCoolness`, `RememberedSize`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `RememberedLKI`, `Self`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.counters_EQ0_SCREAM`, `Card.Creature`, `Card.PromisedGift`, `Creature`, `God`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `GE10`, `GE5`, `GE7`, `GEInitLife`, `GT0`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `PayEnergy<8>`, `3 G Sac<1/CARDNAME>`, `SubCounter<0/LOYALTY>`, `T PayLife<4> Sac<1/CARDNAME>`, `SubCounter<6/LOYALTY>`, `SubCounter<10/LOYALTY>`, `B`, `4 T Sac<1/CARDNAME>`, `B B B Exile<1/CARDNAME>`, `R Discard<0/Hand> Sac<1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{T}, Remove X time counters from CARDNAME and exile it:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `ParentTarget`, `Player`, `Player.IsRemembered`, `Player.NotedForExileDraw`, `Player.Opponent`, `RememberedController`, `Targeted`, `TargetedController`, `TargetedOwner`, `TriggeredCardController`, `TriggeredCardOwner`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `RememberController`, `Targeted`, `TriggeredPlayer`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Exile`, `Graveyard`, `Hand`, `Library`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `UntilHostLeavesPlay`
- `ExileFaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDownPower$`: TODO: Describe this parameter.
  Observed values: `2`
- `FaceDownSetType$`: TODO: Describe this parameter.
  Observed values: `Artifact & Creature & Cyberman`
- `FaceDownToughness$`: TODO: Describe this parameter.
  Observed values: `2`
- `ForgetChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `True`
- `Hidden$`: TODO: Describe this parameter.
  Observed values: `True`
- `Imprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Artifact+YouCtrl`, `Time Lord.YouCtrl`
- `LibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`, `6`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionQuestion$`: TODO: Describe this parameter.
  Observed values: `Put all creature cards into your hand?`, `Put all land cards into your hand?`, `Return TARGETS from graveyard to battlefield under their owners' control?`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Ante`, `Battlefield`, `Battlefield,Graveyard`, `Command`, `Command,Graveyard`, `Exile`, `Graveyard`, `Graveyard,Battlefield`, `Graveyard,Exile`, `Graveyard,Hand`, `Graveyard,Library`, `Hand`, `Hand,Battlefield`, `Hand,Graveyard`, `Hand,Graveyard,Battlefield`, `Library`, `Library,Sideboard`, `Stack`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `3`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Guardian Patrols —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomOrder$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChanged$`: TODO: Describe this parameter.
  Observed values: `Card.!token`, `True`
- `RememberLKI$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `False`
- `Shuffle$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StaticEffect$`: TODO: Describe this parameter.
  Observed values: `Animate`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChangeBack`, `ChangeEnchantment`, `ClearImprint`, `DBAnimate`, `DBAnimateAll`, `DBChange`, `DBChangeLands11M`, `DBChangeRest11M`, `DBChangeZone`, `DBChangeZone15U`, `DBChangeZone2`, `DBChangeZoneAll`, `DBChangeZoneAllBottomLibrary`, `DBChoose`, `DBChooseCard`, `DBCleanup`, `DBClearChosen`, `DBClearNoted`, `DBConjure`, `DBCounter`, `DBDamage`, `DBDamageAll`, `DBDelay`, `DBDelayTrig`, `DBDestiny`, `DBDestroy`, `DBDestroyEnchantments`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDraw`, `DBDraw10U`, `DBDrawBis`, `DBEffect`, `DBEmblem`, `DBEndTurn`, `DBExile`, `DBExileAllGraveyard`, `DBExileGraveyard`, `DBExileHand`, `DBExileSelf`, `DBFog`, `DBGainLife`, `DBGenericChoice`, `DBGetLands`, `DBGoYard`, `DBGraveShuffle`, `DBHand`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBIncubate`, `DBInvestigate`, `DBLibrary`, `DBLoseLife`, `DBMana`, `DBManifest`, `DBMask`, `DBMassReveal`, `DBMayPlay`, `DBMill`, `DBNoCombatDamage`, `DBPlay`, `DBPlayThem`, `DBPoison`, `DBPossibilityCleanup`, `DBPump`, `DBPumpAll`, `DBPutBattlefield`, `DBPutLands`, `DBRemoveRope`, `DBRepeat`, `DBRepeatChoose`, `DBRepeatDraw`, `DBRepeatEach`, `DBReturn`, `DBReveal`, `DBRollDice`, `DBSac`, `DBSacrifice`, `DBSearchLibrary`, `DBShuffle`, `DBShuffleChanged`, `DBSkipTurn`, `DBToken`, `DelayedEffect`, `DelayedReturn`, `DelTrig`, `DelTrigSlowtrip`, `Draw`, `DrawEach`, `ExileAllGrave`, `ExileAllHand`, `ExileHand`, `ExileSelf`, `GotoBottom`, `GraveShift`, `Graveyard`, `HeadChange`, `MimeoChooseCopy`, `MyVision`, `OssuaryRepeat`, `PsychoDraw`, `RepeatBis`, `ReturnOfTheHumans`, `SacAll`, `Separate`, `SetAllLife`, `Shuffle2`, `Shuffle3`, `ShuffleRest`, `TrigDelay`, `TrigImmediateTrig`, `WindDraw`, `YouDraw`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MaxTgt`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `Y`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TypeLimit$`: TODO: Describe this parameter.
  Observed values: `X`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `PayLife<5>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`
- `UseAllOriginZones$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `creatures that dealt damage this turn`, `other permanent`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.YouCtrl`, `Opponent`, `Permanent.YouCtrl+Other`, `Permanent.YouOwn`, `Player`
- `WithCountersType$`: TODO: Describe this parameter.
  Observed values: `FINALITY`, `Flying`

## `ChaosEnsues`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`

## `Charm`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`
- `AdditionalDescription$`: TODO: Describe this parameter.
  Observed values: `. Activate only as a sorcery.`, `. Activate only if there are two or more hatchling counters on CARDNAME.`, `. Each mode must target a different player.`, `. If an opponent has eight or more cards in their graveyard, you may choose both.`, `. If there are eight or more permanent cards in your graveyard as you cast this spell, choose one or more instead.`, `. If there are four or more card types among cards in your graveyard, choose both.`, `. If there are four or more card types among cards in your graveyard, choose one or more instead.`, `. If this spell was kicked, choose any number instead.`, `. If this spell's additional cost was paid, choose both instead.`, `. If you control a commander as you cast this spell, you may choose both instead.`, `. If you control a commander as you cast this spell, you may choose both.`, `. If you control a commander, you may choose both instead.`, `. If you control a Wizard as you cast this spell, you may choose two instead.`, `. If you control an artifact and an enchantment as you cast this spell, you may choose both.`, `. If you descended this turn, you may choose both instead. (You descended if a permanent card was put into your graveyard from anywhere.)`, `. If you have exactly 13 life, you may choose both.`, `. If you have max speed, choose both instead.`, `. Until end of turn, target creature you control has that base power and toughness, becomes that creature type, and gains that ability.`, `. X can't be 0.`, `and CARDNAME gets +1/+1 until end of turn.`, `and note the choice: Bolas or Ugin.`, `and you lose 2 life`, `Create a red and white creature token with those characteristics.`, `Each mode must target a different player.`, `If CARDNAME was kicked, choose both instead.`, `If you control a commander as you cast this spell, you may choose both.`, `If you control a nonland permanent you don't own as you cast this spell, you may choose two instead.`, `If you control six or more lands, choose both instead.`, `or more. Each mode must target a different player.`, `Until end of turn, target creature you control gains "When this creature dies, return it to the battlefield tapped under its owner's control" and has the chosen base power and toughness.`, `where X is the number of times you chose a mode for that spell`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `X`
- `CanRepeatModes$`: TODO: Describe this parameter.
  Observed values: `True`
- `CharmNum$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `Count$Compare B GE2.2.1`, `Count$Compare X GE1.2.1`, `Count$Compare X GE6.2.1`, `Count$Compare Y EQ13.2.1`, `Count$Compare Y GE1.2.1`, `Count$Compare Y GE8.2.1`, `Count$Compare Y GE8.3.1`, `Count$Delirium.3.1`, `Count$Kicked.2.1`, `Count$TriggerRememberAmount`, `MaxUniqueOpponents`, `W`, `X`, `Y`
- `ChoiceRestriction$`: TODO: Describe this parameter.
  Observed values: `ThisGame`, `ThisTurn`, `YourLastCombat`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `AimForTheWyvern,AimForTheCursedAmulet,FireAWarningShot`, `Animate,Connive,Return`, `Artifact,Creature`, `Artifact,Enchantment`, `Artifact,Enchantment,Proliferate`, `BardicInspiration,SongofRest`, `Bash,Buff,LoseTime`, `Bash,Token,Prevent`, `BatheInDragonfire,HordelingOutburst,SarkhansTriumph`, `BeastToken,BirdToken`, `Boil,Mash,Stew`, `BounceSaga,GraveSaga`, `BraveTheStench,SearchTheBody`, `BreakTheirChains,InterrogateThem`, `Buff,Exile,Knight`, `Buffet,SeeAShow,PlayGames,GoToSleep`, `CantBlockEffect,DBGainCtrl,DmgAll`, `CemeteryRecruitment,Duress,HumanFrailty`, `Change,Destroy`, `ChangeArtifact,ChangeCreature`, `ChangeCreature,ChangeArtifact`, `ChangeCreature,ChangeEnchantment`, `ChangeCreature,ChangeLand`, `ChangeIntoTurtle,ChangeIntoSpider,ChangeIntoElephant`, `ChangeZone,DealDmg,PumpAll`, `ChargeThem,BefriendThem`, `CharmCreature,CharmToken`, `CharmPump,CharmCurse,CharmLife`, `ChooseFreeze,ChooseThaw`, `Cleric,Phyrexian`, `ConduitCharge,ConduitP1P1`, `ControlReturn,ControlBounce`, `Copy,Exile,Pump`, `CopySpell,CopyCreature`, `Counter,Draw`, `CounterNonCreature,DBConjure`, `CounterP1P1,CounterCharge`, `CounterSorcery,DBDestroy,DBDig`, `Creature,MountVehicle,AuraEquipment`, `CreatureDBRemoveCounter,OpponentDBRemoveCounter`, `Damage,Destroy`, `DamageAll,Tuck`, `DamageFlyingCreature,DamageNonFlyingCreature,DamagePlayer`, `DBAnimate,DBDraw`, `DBAnimate,DBGangUp`, `DBAnimate7,DBAnimate1`, `DBArtifact,DBEnchantment,DBPutCounterAll`, `DBAttack,DBAbility,DBMagic,DBItem`, `DBBasicLand,DBColor`, `DBBig,DBSmall`, `DBBlink,DBToken`, `DBBlizzard,DBBlizzara,DBBlizzaga`, `DBBlock,DBToken`, `DBBounce,DBAnnul,DBCounters,DBBlessing`, `DBBounce,DBDiscard`, `DBBounceAllTokens,DBBounceAllNonTokens`, `DBBurn,DBKill,DBMaim`, `DBChange,DBDestroy`, `DBChangeZone,DBChangeZoneBis,DBExileGrave`, `DBChangeZone,DBChooseCard,DBDestroy`, `DBChangeZone,DBCounter`, `DBChangeZone,DBDestroy`, `DBChangeZone,DBDestroy,DBDestroy2`, `DBChangeZone,DBDmg,DBPump`, `DBChangeZone,DBDmg,DBPutCounter`, `DBChangeZone,DBDraw`, `DBChangeZone,DBEffect`, `DBChangeZone,DBPump,DBPumpAll`, `DBChangeZone,DBPutCounter`, `DBChangeZone,DBPutCounterAll,DBDraw`, `DBChangeZone,DBRegen,DBPump`, `DBChangeZone,DBRemoveCounter`, `DBChangeZone,DBReturn`, `DBChangeZone1,DBChangeZone2`, `DBChoose,DBMurder,DBChangeZone,DBSacrifice`, `DBCloak,DBGoad,DBDraw`, `DBCloak,DBPutCounters`, `DBCombinePowers,DBDefense,DBFight`, `DBConceal,DBReveal`, `DBConjure,DBReturn`, `DBConjureRite,DBConjureTake`, `DBControl,DBClone`, `DBCopy,DBChangeTarget`, `DBCopy,DBChangeZone,DBDestroy,DBPumpAll`, `DBCopy,DBPumpAll,DBDestroy,DBMill`, `DBCopy,DBPumpAll,DBDraw,DBTap`, `DBCopy,DBToken,DBPump,DBFight`, `DBCopy1,DBCopy2`, `DBCopySpell,DBCopyCreature`, `DBCounter,DBChangeTargets,DBCopySpellAbility`, `DBCounter,DBChangeZone`, `DBCounter,DBCopy,DBLoot`, `DBCounter,DBCounterBis`, `DBCounter,DBDealDamage,DBDraw`, `DBCounter,DBDestroy`, `DBCounter,DBDestroy,DBAnimate`, `DBCounter,DBDig`, `DBCounter,DBDraw`, `DBCounter,DBDraw,DBControl`, `DBCounter,DBDread`, `DBCounter,DBFight`, `DBCounter,DBGainLife`, `DBCounter,DBGoad,DBLoot`, `DBCounter,DBProliferate`, `DBCounter,DBPump`, `DBCounter,DBPump,DBTap,DBUntap`, `DBCounter,DBRemove`, `DBCounter,DBReturn,DBDraw`, `DBCounter,DBReturn,DBPump,DBDestroy`, `DBCounter,DBReturn,DBTapAll,DBDraw`, `DBCounter,DBSearch`, `DBCounter,DBStile`, `DBCounter,DBSurveil`, `DBCounter,DBSwitch,DBUnblockable`, `DBCounter,DBTap`, `DBCounter,DBToken`, `DBCounter,DBTreasure,DBFood`, `DBCounters,DBTrample,DBDrawTwo`, `DBCounterSpell,DBCounterAbility,DBReturn,DBCopy,DBDraw`, `DBCreateToken,DBGainLife,DBDraw`, `DBCreature,DBArtifact,DBEnchantment`, `DBCreature,DBPlaneswalker`, `DBCrossSlash,DBBladeBeam,DBOmnislash`, `DBCure,DBCura,DBCuraga`, `DBCurse,DBSwitch`, `DBDamage,DBDamageAll,DBToken`, `DBDamage,DBDestroy`, `DBDamage,DBExilePlay`, `DBDamage,DBGain`, `DBDamage,DBPump`, `DBDamage,DBPump,DBTap`, `DBDamage,DBReturn1`, `DBDamage,DBTap,DBSac`, `DBDamage,TrigPumpAll`, `DBDamageAll,DBDamage`, `DBDamageCreatures,DBDamageOpponents,DBDestroy`, `DBDamageOutlaw,DBDamageNonOutlaw`, `DBDamageP,DBDamageC,DBDestroy,DBDiscard`, `DBDateNight,DBPatrolNight`, `DBDealDamage,DBCast`, `DBDealDamage,DBChangeZone`, `DBDealDamage,DBDamageAll`, `DBDealDamage,DBDestroy,DBExileYards`, `DBDealDamage,DBDig`, `DBDealDamage,DBExile`, `DBDealDamage,DBPump`, `DBDealDamage,DBPump,DBGainLife`, `DBDealDamage,DBPumpAll,DBToken`, `DBDealDamage,DBPutCounter,DBPowerstone`, `DBDealDamage,DBReturn,DBTapAll`, `DBDealDamage,DBToken`, `DBDealDmg,DBWarrior,DBDiscard`, `DBDebuff,DBLoyalty`, `DBDebuffAll,DBChooseCard,DBDestroyAll`, `DBDecrease,DBIncrease`, `DBDestroy,CantBlockEffect`, `DBDestroy,DBAirbend`, `DBDestroy,DBBounce`, `DBDestroy,DBChange`, `DBDestroy,DBChangeTargets,DBCantBlock`, `DBDestroy,DBChangeZone`, `DBDestroy,DBChangeZone,DBCounter`, `DBDestroy,DBChangeZone,DBDraw`, `DBDestroy,DBChangeZone,DBLoseLife`, `DBDestroy,DBDamage,DBChangeZone`, `DBDestroy,DBDealDamage`, `DBDestroy,DBDealDamage,DBPump`, `DBDestroy,DBDebuff`, `DBDestroy,DBDestroy2`, `DBDestroy,DBDestroy2,DBExile,DBGainLife`, `DBDestroy,DBDestroyNonCreature`, `DBDestroy,DBDraw`, `DBDestroy,DBDraw,DBDiscard`, `DBDestroy,DBDraw,DBGainLife`, `DBDestroy,DBEarthbend`, `DBDestroy,DBExile`, `DBDestroy,DBExplore`, `DBDestroy,DBGainLife`, `DBDestroy,DBHaste`, `DBDestroy,DBProtect`, `DBDestroy,DBPump`, `DBDestroy,DBPumpAll`, `DBDestroy,DBPumpAll,DBUnblockable`, `DBDestroy,DBPutCounter`, `DBDestroy,DBSacrifice`, `DBDestroy1,DBDestroy2`, `DBDestroy1,DBDestroy2,DBDestroy3`, `DBDestroy1,DBDestroy2,DBToken`, `DBDestroyAll,DBConditionEffect`, `DBDestroyAll,DBDestroyAll2`, `DBDestroyAll,DBManifestThree`, `DBDestroyAllCreatures,DBDestroyAllArtifactsAndEnchantments`, `DBDestroyAllTokens,DBDestroyAllNonlandNontokenPermanents`, `DBDestroyArtifact,DBDestroyDefender,DBDamage`, `DBDestroyArtifact,DBDestroyEnchantment,DBDraw`, `DBDestroyArtifact,DBDestroyEnchantment,DBExile`, `DBDestroyArtifact,DBDestroyEnchantment,DBPump`, `DBDestroyArtifact,DBDestroyLand`, `DBDestroyArtifact,DBRoll`, `DBDestroyCreature,DBDestroyArtEnc,DBDraw`, `DBDestroyCreature,DBDestroyEnchantment`, `DBDestroyCreature,DBDestroyEnchantment,DBPutCounterAll`, `DBDestroyFlier,DBDestroyEnchantment,DBDraw`, `DBDestroyLand,DBChange`, `DBDig,DBCounter`, `DBDig,DBLoseLife,DBDmg`, `DBDino,DBVampire`, `DBDiscard,DBDamage`, `DBDiscard,DBDamage,DBDestroy,DBPump,DBCurse,DBToken`, `DBDiscard,DBDamageCreature,DBDamagePW,DBPump`, `DBDiscard,DBDebuff`, `DBDiscard,DBDraw`, `DBDiscard,DBEarthbend`, `DBDiscard,DBExile`, `DBDiscard,DBLoseLife,DBSac`, `DBDiscard,DBPump`, `DBDiscard,DBPump,DBDrain`, `DBDiscard,DBPump,DBPump2`, `DBDiscard,DBReturn,DBDestroy`, `DBDiscard,DBSacrifice`, `DBDiscard,YouChoose`, `DBDiscard1,DBDiscard2`, `DBDiscardColorless,DBDiscardMulticolor`, `DBDistract,DBEnthrall`, `DBDmg,DBDestroy`, `DBDmg,DBDisc`, `DBDmg,DBDmg2`, `DBDmg,DBGainLife`, `DBDmg,PumpAll,Token`, `DBDmg1,DBDestroy`, `DBDmg1,DBDmg2`, `DBDmgC,DBDmgP`, `DBDoHomework,DBFightCrime`, `DBDraw,DBChangeZone`, `DBDraw,DBCopy,DBReturn`, `DBDraw,DBDamageAll`, `DBDraw,DBDebuff`, `DBDraw,DBDestroy,DBDamage`, `DBDraw,DBDestroy,DBRemove`, `DBDraw,DBDiscard`, `DBDraw,DBDmg`, `DBDraw,DBEffect`, `DBDraw,DBExile`, `DBDraw,DBFood,DBRadAway`, `DBDraw,DBGainLife,DBDestroy`, `DBDraw,DBMill`, `DBDraw,DBPump`, `DBDraw,DBPump,DBChangeZone`, `DBDraw,DBPumpAll`, `DBDraw,DBPutCounter,DBMana,DBChangeZone`, `DBDraw,DBPutCounter,DBUntap`, `DBDraw,DBReturn`, `DBDraw,DBToken`, `DBDraw,DBToken,DBLoseLife`, `DBDraw,DBTreasure`, `DBDraw,DBTreasure,DBSibsig`, `DBEffect,DBEffect2`, `DBEffect,DBLoseGain`, `DBEffect,DBPump`, `DBEffect,DBPumpAll`, `DBEnergy,DBPutCounter,DBToken`, `DBExile,DBCounter,DBToken`, `DBExile,DBDamage`, `DBExile,DBDestroy`, `DBExile,DBDraw,DBCounters`, `DBExile,DBFlicker`, `DBExile,DBPump`, `DBExile,DBPutCounter,DBToken`, `DBExile,DBReturn,DBPutCounter`, `DBExile,DBToken`, `DBExileAll,DBSearch,DBToken,DBCounter`, `DBExileArtifact,DBExileEnchantment,DBDread`, `DBExileC,DBExileNonC`, `DBExileCreature,DBExileEnchantment`, `DBFight,DBDestroy`, `DBFight,DBRemoveCounter,DBPutCounter`, `DBFight1,DBDestroy`, `DBFightInit,DBCounter`, `DBFire,DBFira,DBFiraga`, `DBFlicker,DBReturnArtifact`, `DBFly,DBLife`, `DBFog,DBRegen,DBCounter`, `DBGain,DBChange,DBChangeAll,DBSearch`, `DBGain,DBLose`, `DBGainControl,DBSac`, `DBGainLife,DBChangeZone`, `DBGainLife,DBCounter,DBPump`, `DBGainLife,DBDestroy,DBCounter`, `DBGainLife,DBDestroy,DBExileCard`, `DBGainLife,DBDestroy,DBPutCounter`, `DBGainLife,DBDraw`, `DBGainLife,DBPrevent`, `DBGainLife,DBPreventDamage`, `DBGainLife,DBPreventDmg`, `DBGainLife,DBSurveil,DBLoseLife`, `DBGainLife,DBUntap,DBSacrifice`, `DBGalianBeast,DBDeathGigas,DBHellmasker`, `DBGoad,DBExile`, `DBHeckle,DBHeroWorship`, `DBHeist,DBExile`, `DBHeist,DBPump,DBCounter`, `DBImpulse,DBPump`, `DBIndestructible,DBDestroy`, `DBJumpKick,DBDashAttack,DBFootToss`, `DBLand,DBLand2`, `DBLandscaping,DBLeyline`, `DBLoot,DBShuffle`, `DBLoot,DBTreasure,DBToken`, `DBLose,DBChange,DBWeaken,DBSearch`, `DBLoseGame1,DBLoseGame2`, `DBLoseLife,DBGainLife`, `DBMana,DBExile`, `DBMill,DBDestroy`, `DBMill,DBDestroy,DBPump,DBLoseLife`, `DBMill,DBPutBattlefield,DBPumpAll`, `DBMove,DBRemove`, `DBMurder,DBReanimate`, `DBMurder,DBRecruit`, `DBMustBeBlocked,DBEffect`, `DBNameCard,DBPump`, `DBNoLife,DBDamage,DBLand,DBPumpAll`, `DBOpenAttraction,DBDestroy`, `DBOppLoseLife,DBGainLife`, `DBOppSac,DBExile`, `DBPermanent,DBPlayer`, `DBPhaseOut,DBDraw,DBExileGrave,DBDamage,DBDestroy`, `DBPopulate,DBProliferate`, `DBPrepare,DBUnprepare`, `DBPrevent,DBSacrifice,DBPutCounter,DBPump`, `DBProjection,DBFruition`, `DBProliferate,DBCounter`, `DBPump,DBAirbend`, `DBPump,DBChangeZone`, `DBPump,DBChooseType,DBRearrange`, `DBPump,DBCurse`, `DBPump,DBDamage`, `DBPump,DBDestroy`, `DBPump,DBDestroy,DBDraw`, `DBPump,DBDestroy,DBGainLife`, `DBPump,DBDmg`, `DBPump,DBDraw`, `DBPump,DBExile,DBScry`, `DBPump,DBFight`, `DBPump,DBGainLife,DBDestroy`, `DBPump,DBHexproof`, `DBPump,DBLoseLife`, `DBPump,DBPowerStone,DBKarnstruct,DBDraw`, `DBPump,DBProliferate`, `DBPump,DBPump2`, `DBPump,DBPump2,DBDmg`, `DBPump,DBPumpAll`, `DBPump,DBPumpKW`, `DBPump,DBPutCounter`, `DBPump,DBReturn,DBDraw,SacCreature`, `DBPump,DBToken`, `DBPump,DBToken,DBLoot`, `DBPump,DBUnsummon`, `DBPump,DBUntap`, `DBPump,DBUntapAll`, `DBPump1,DBPump2`, `DBPump1,DBPump2,DBDiscard`, `DBPumpAll,DBAnimateAll`, `DBPumpAll,DBBite`, `DBPumpAll,DBChangeZone`, `DBPumpAll,DBDamage1,DBDamage2`, `DBPumpAll,DBDiscard`, `DBPumpAll,DBDiscard,DBDealDamage`, `DBPumpAll,DBDiscard,DBLoseLife`, `DBPumpAll,DBRemoveCounters`, `DBPumpAll,DBReturn`, `DBPumpAll,DBToken`, `DBPumpOne,DBPumpTwo`, `DBPumpPower,DBPumpKW`, `DBPumpPower,DBPumpToughness`, `DBPutCounter,DBChangeZone`, `DBPutCounter,DBChangeZone1,DBChangeZone2`, `DBPutCounter,DBChoose,DBDraw`, `DBPutCounter,DBCopy,DBToken,DBSacrifice`, `DBPutCounter,DBDestroy`, `DBPutCounter,DBDmg,DBGainLife,DBGrave`, `DBPutCounter,DBDraw,DBClone`, `DBPutCounter,DBDraw,DBToken`, `DBPutCounter,DBExile,DBLoseLife`, `DBPutCounter,DBFetch`, `DBPutCounter,DBFight,DBDestroy`, `DBPutCounter,DBGainLife`, `DBPutCounter,DBGainLife,DBExile`, `DBPutCounter,DBGainLife,DBPump`, `DBPutCounter,DBProliferate`, `DBPutCounter,DBPump`, `DBPutCounter,DBPumpAll`, `DBPutCounter,DBReturn`, `DBPutCounter,DBScry,DBEarthbend`, `DBPutCounter,DBToken`, `DBPutCounter,DBToken,DBGainLife`, `DBPutCounter,DBToken,DBScry`, `DBPutCounterAll,DBDraw,DBToken,DBLoseLife`, `DBRamp,DBGiant,DBRegrow`, `DBRamp,DBPutCounterAll,DBScry`, `DBRamp,DBToken`, `DBReap,DBRevive`, `DBRearrange,DBRearrange2`, `DBRegenerate,DBDamageAll`, `DBRemoveCounter,DBPump`, `DBRepair,DBImpound`, `DBReturn,DBChangeZone`, `DBReturn,DBCounter,DBDestroy`, `DBReturn,DBDiscard,DBDestroy,DBDamage`, `DBReturn,DBDiscard,DBLook`, `DBReturn,DBDmg`, `DBReturn,DBExile`, `DBReturn,DBGainLife,DBCounter,DBDraw`, `DBReturn,DBReturn2`, `DBReturn,DBScry`, `DBReturn,DBScry,DBToken`, `DBReturnCreature,DBReturnAura`, `DBRhino,DBBird,DBPlant`, `DBRoyal,DBSorcerer,DBMonster`, `DBSac,DBChooseNumber`, `DBSac,DBExile,DBSpirit,DBGain`, `DBSac,DBExilePlay,DBExileGrave`, `DBSac,DBToken,DBDiscard`, `DBSacrifice,DBChangeZone,DBPumpAll`, `DBSacrifice,DBDiscard,DBLoseLife`, `DBSacrifice,DBDraw,DBLoseLife`, `DBSacrifice,DBPumpAll`, `DBSacrifice,DBReturn`, `DBSacrifice,DBToken`, `DBScry,DBDamage,DBGainLife`, `DBScry,DBGainLife,DBFlicker`, `DBSearch,DBChangeZone`, `DBSearch,DBDamage`, `DBSearch,DBHuman,DBFood`, `DBSearch,DBProliferate`, `DBSearch,DBPump`, `DBSearch,DBRemove`, `DBSearch,DBReturn`, `DBSearch,DBWish`, `DBSeek,DBPumpAll`, `DBSeekEngines,DBSeekNonLand`, `DBSelf,DBOthers`, `DBShock,DBLoot,DBTreasure,DBShatter`, `DBSmall,DBMedium,DBLarge`, `DBSmash,DBStrafe,DBSwoop`, `DBSomersault,DBMeteorStrikes,DBFinalHeaven`, `DBSpatialContortion,DBEldraziDisplacer,DBEldraziScion`, `DBSpirit,DBIndestructible,DBHelix,DBSacrifice`, `DBSubmerge,DBUnsummon`, `DBSurveil,DBDealDamage,DBChangeZone`, `DBTap,DBDmg`, `DBTap,DBEffect`, `DBTap,DBPump`, `DBTap,DBPump,DBBlink`, `DBTap,DBToken`, `DBTap,DBUntap`, `DBTapAll,DBTapAll2`, `DBTapOrUntap,DBScry`, `DBTapUntap,DBDamage,DBCopy,DBChangeZone`, `DBTarget,DBDelayTrig`, `DBTax,DBDetain`, `DBThunder,DBThundara,DBThundaga`, `DBToken,DBAnimateAll`, `DBToken,DBBounce,DBDraw`, `DBToken,DBChangeZone`, `DBToken,DBChangeZone,DBGainLife`, `DBToken,DBClone`, `DBToken,DBCopy`, `DBToken,DBCounter`, `DBToken,DBCounter,DBChangeZone,DBGainLife`, `DBToken,DBCounter,DBExile,DBGainLife`, `DBToken,DBDealDamage`, `DBToken,DBDestroy`, `DBToken,DBDraw,DBDamage`, `DBToken,DBDraw,DBDamage,DBTreasure`, `DBToken,DBDraw,DBExileYard`, `DBToken,DBExile,DBDamageEffect`, `DBToken,DBExile,DBReanimate`, `DBToken,DBNonToken,DBEnchantment`, `DBToken,DBPump`, `DBToken,DBPump,DBDestroy`, `DBToken,DBPump,DBReg`, `DBToken,DBPumpAll`, `DBToken,DBPutCounter,DBScry`, `DBToken,DBPutCounterAll`, `DBToken,DBPutCounterAll,DBScry`, `DBToken,DBPutCounters`, `DBToken,DBReturn,DBProliferate,DBGainLife`, `DBToken,DBScry,DBExile,DBExileGraveyard`, `DBToken,DBScry,DBPumpAll`, `DBToken,DBToken2`, `DBToken,DBUnblockable,DBExileTop`, `DBToken1,DBToken2,DBToken3`, `DBTokens,DBBuff`, `DBTokens,DBTap`, `DBTreasure,DBChoose`, `DBTreasureLose1,DBDrawLose2,DBTokenLose3`, `DBTurnFaceUp,DBChangeZoneAll`, `DBTutor,DBDraw`, `DBTutor,DBPutCounter,DBAntiquate`, `DBTutorCreature,DBPutCreature`, `DBUnsummon,DBSearch`, `DBUntap,DBAnimate`, `DBUntap,DBCantBlock,DBPutCounter`, `DBUntap,DBDestroy,DBDebuff`, `DBUntap,DBPump`, `DBUntap,DBTap`, `DBUntapAll,DBPumpAll,DBCombatTrig`, `DBWheel,DBDamage1,DBDamage2`, `DBWheel,DBFlames`, `DealDmg,PumpAll,PumpDouble`, `DelayedTrigger,DBDoubleStrike`, `DelTrigSlowDraw,Tutor`, `DelTrigSlowtrip,Pump,Phases`, `DestArt,DmgFly`, `Destroy,DigLand,GainLife`, `Destroy,Fight`, `Destroy,GainLife`, `Destroy,GainLife,Token,PutCounter`, `Destroy,Incubate`, `Destroy,Remove`, `Destroy1,Destroy2`, `DestroyAE,ExileGrave,GainLife`, `DestroyAllCreatures,DestroyAllPlaneswalkers,DestroyAllBattles,ExileAllGraveyards,RemoveAllCounters`, `DestroyArtifact,DBMill`, `DestroyArtifact,DestroyCreature,DestroyEnchantment,DestroyLand,DestroyPlaneswalker`, `DestroyArtifact,DestroyEnchantment,DestroyLand`, `DestroyArtifact,DestroyLand`, `DestroyArtifacts,DestroyEnchs,DestroyLE3,DestroyGE4`, `DestroyCtrs,DestroyPWs`, `DestroyLegend,DestroyNonLegend`, `DetroyAura,PumpSoldier,PumpVigilance`, `Disarm,Detonate`, `DiscardSeek,DamageTreasures,DamagePump`, `DiscardTwo,ReviveCreature`, `DistractTheGuard,Hide`, `DosansOldestChant,KodamasReach,TimeOfNeed`, `Drain,Battle`, `DrainPact,DiscardPact,DrawPact,DeathPact`, `Draw,Damage,PutLand`, `DrawPact,DrainPact,DamagePact,BetrayPact`, `DrawThree,DestroyAndDraw`, `EbonyDrain,EbonyExile,EbonyFear`, `Exchange,Switch`, `Exile,Return`, `Exile,Smash,CreatureDamage`, `Exile1,Exile2`, `ExileAllArtifacts,ExileAllCreatures,ExileAllEnchantments,ExileAllGraveyards`, `ExileArtifact,ExileCreature,ExileEnchant,ExilePlaneswalker`, `ExileArtifact,ExileEnchantment`, `ExileCreature,ExileEnchantment`, `ExileLandCreature,DealDmg`, `ExileTwo,CreateTreasure`, `FetchBasic,Fight`, `FightTheCurrent,FindACrossing`, `FormAParty,StartABrawl`, `Fortune,Misfortune`, `FromHand,FromGrave`, `Gelato,Pasta,Pizza`, `GrowCreature,ShrinkCreature`, `Haste,Destroy`, `Human,NonHuman`, `IdyllicTutor,RevokeExistence,Reprisal`, `Incubate,Transform,PumpAll`, `IntimidateThem,FendThemOff`, `JittePump,JitteCurse,JitteLife`, `JourneyOn,MakeCamp`, `KnightTokens,SeekCard,DestroyArtifact,DestroyEnchantment,GainLife`, `LifePact,DiscardPact,MakeZombies`, `LoseTime,GainTime`, `MakeARetreat,StandAndFight`, `Mana,Pump`, `MarathCounters,MarathDmg,MarathToken`, `MerchantScroll,MemoryLapse,Forget`, `MillOpp,ChangeType,PhaseArtifact`, `P1P1,Lore`, `P1P1,Transform`, `P2P2,M1M1,GainLife`, `Powerstone,Seek`, `PreventDamage,GainLife`, `Proliferate,PhaseOut,CounterAbility`, `Pump,Counter,Effect`, `Pump,Coward`, `Pump,Coward,Trample`, `PumpAll,Animate,Draw,Gain`, `PumpAll,DestroyEnch,RegenAll`, `PumpAll,DrawCard,ReturnCard`, `PumpAll,Tap,Prevent`, `PumpField,PumpHand,Token`, `PumpGiant,PumpHexproof,ReturnCard`, `RaiseScoundrel,HauntedHarvest`, `RampThree,SpiritLand`, `ReduceHand,ReduceBattlefield`, `RegrowCreature,RegrowEnchantment`, `Return,Curse,Goad`, `Return,Mill`, `Return,Remove`, `ReturnAll,DBDestroy,DBZombify`, `RouseTheParty,SetOffTraps`, `SacArtifact,SacCreature,SacPW`, `SacArtifact,SacEnchantment,SacFlier`, `SacCreature,DiscardCards,LoseLife`, `SacCreature,SacEnchantment`, `SacDom,DrawDom,TransDom`, `SacNontoken,SacToken,SacPW`, `SavageStomp,Naturalize`, `SearchForest,ReturnCave`, `SearchLand,Return,DoPump`, `Shock,DestroyArtifact`, `SmashIt,LiftTheCurse,StealItsEyes`, `SmashTheChest,PryItOpen`, `SplitDiscard,FocusDiscard`, `Standoff,Ghost`, `SVar1,SVar2`, `Tap,Freeze`, `Tap,Untap`, `TheGooseIsLoose,TheGooseLaidAnEgg`, `Token,Card,Counters`, `Treasure,Sacrifice,Effect`, `TrigAgeSurvivor,TrigAgeSacrifice`, `TrigDig,TrigPutCounterAll`, `TrigDrawDiscard,TrigSacrifice,TrigDmg`, `TrigTap,TrigPumpCurse`, `Wipe,Devils`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T`, `X T`, `1 T Sac<1/CARDNAME>`, `1 G T`, `T Sac<1/Artifact>`, `2 Sac<2/Artifact>`, `1 Sac<1/CARDNAME>`, `2 T`, `1 B Sac<1/Creature>`, `1 ExileFromGrave<1/Instant;Sorcery>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{1}, Exile an instant or sorcery card from your graveyard:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE2_HATCHLING`
- `MinCharmNum$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `X`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `5`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Delirium —`, `Descend 8 —`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDraft`, `DBNoop`, `NoopDesc`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `White`

## `ChooseCard`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Hand`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Ashiok`, `AtLeast1`, `AtLeast2`, `AtOppEOT`, `BestBlocker`, `BowToMyCommand`, `Clone`, `Duneblast`, `GoodCreature`, `LowestCMCCreature`, `NeedsPrevention`, `NegativePowerFirst`, `Never`, `NextTurnAttacker`, `NotSelf`, `OppPreferred`, `OrzhovAdvokist`, `OwnCard`, `Phylactery`, `RandomNonLand`, `SacOneEach`, `TangleWire`, `WorstCard`
- `AllCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `5`, `6`, `7`, `ArtifactX`, `Count$Valid Creature.Other+CanBeTargetedByTriggeredSpellAbility`, `Count$Valid Creature.RememberedPlayerCtrl`, `CreatureX`, `LandX`, `Max`, `NumCreatures`, `Random`, `ShiftX`, `TappedXTwo`, `X`, `Y`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChoiceDesc$`: TODO: Describe this parameter.
  Observed values: `creature`, `creature they control`, `instant or sorcery`, `nonland`
- `ChoiceOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature,Land`, `Artifact,Enchantment`, `Artifact.cmcEQW`, `Artifact.ControlledBy Remembered,Land.ControlledBy Remembered`, `Artifact.IsImprinted,Creature.IsImprinted`, `Artifact.IsRemembered+cmcEQ1,Creature.IsRemembered+cmcEQ1`, `Artifact.IsRemembered+cmcEQ2,Creature.IsRemembered+cmcEQ2`, `Artifact.IsRemembered+cmcEQ3,Creature.IsRemembered+cmcEQ3`, `Artifact.RememberedPlayerCtrl`, `Artifact.RememberedPlayerOwn,Creature.RememberedPlayerOwn`, `Artifact.tapped,Creature.tapped,Land.tapped`, `Artifact.TargetedPlayerCtrl`, `Artifact.untapped+ActivePlayerCtrl,Creature.untapped+ActivePlayerCtrl,Land.untapped+ActivePlayerCtrl`, `Artifact.untapped,Creature.untapped,Land.untapped`, `Artifact.YouCtrl`, `Artifact.YouCtrl+cmcEQZ`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouDontCtrl`, `Artifact.YouDontCtrl,Enchantment.YouDontCtrl`, `Artifact.YouOwn`, `Card`, `Card.ChosenType+OwnedBy TriggeredDefendingPlayer`, `Card.ChosenType+YouOwn+IsImprinted`, `Card.cmcEQX+ControlledBy TriggeredTarget`, `Card.cmcGE3+IsRemembered`, `Card.ControlledBy Remembered`, `Card.Creature`, `Card.Creature+cmcLE3+IsRemembered`, `Card.Creature+ExiledWithSource+cmcEQX`, `Card.Creature+IsRemembered`, `Card.Creature+YouOwn`, `Card.Creature+YouOwn+White`, `Card.ExiledWithSource`, `Card.Gate+IsRemembered`, `Card.inZoneHand,Permanent.CanBeSacrificedBy`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.IsRemembered`, `Card.IsRemembered+ChosenType`, `Card.IsRemembered+cmcGE4`, `Card.IsRemembered+cmcLE3+nonLand`, `Card.IsRemembered+nonLand`, `Card.IsRemembered+nonLand+nonCreature`, `Card.IsRemembered+RememberedPlayerCtrl`, `Card.IsRemembered+withoutIndestructible`, `Card.namedCalim; Djinn Emperor+YouOwn+Other`, `Card.nonBasic+TargetedPlayerCtrl+inZoneHand`, `Card.nonLand`, `Card.nonLand+IsRemembered`, `Card.nonLand+OwnedBy TriggeredTarget`, `Card.nonLand+RememberedPlayerCtrl+inZoneHand`, `Card.nonLand+YouOwn`, `Card.OppOwn+counters_GE1_VOID`, `Card.Permanent+YouOwn`, `Card.RememberedPlayerCtrl`, `Card.RememberedPlayerCtrl+Black`, `Card.RememberedPlayerCtrl+Blue`, `Card.RememberedPlayerCtrl+Green`, `Card.RememberedPlayerCtrl+nonLand`, `Card.RememberedPlayerCtrl+Red`, `Card.RememberedPlayerCtrl+White`, `Card.TargetedPlayerOwn`, `Card.TargetedPlayerOwn+!IsImprinted+sharesNameWith Remembered`, `Card.TopLibrary+YouOwn,Card.YouOwn+inZoneHand`, `Card.TriggeredCards`, `Card.White+YouOwn`, `Card.YouCtrl+cmcEQX`, `Card.YouOwn`, `Card.YouOwn+!IsImprinted+sharesNameWith Remembered`, `Card.YouOwn+!IsRemembered`, `Card.YouOwn+ChosenType`, `Card.YouOwn+DrawnThisTurn`, `Card.YouOwn+faceUp`, `Card.YouOwn+nonLand`, `Card.YouOwn+NotedForVolatileChimera`, `Cave.YouCtrl`, `Creature`, `Creature,Land`, `Creature,Planeswalker`, `Creature.!token+nonVehicle+RememberedPlayerCtrl`, `Creature.attackedThisTurn`, `Creature.attacking`, `Creature.attacking+NotDefinedTargeted+powerLTX`, `Creature.CanBeEnchantedBy`, `Creature.cmcEQX+ExiledWithSource`, `Creature.cmcEQY`, `Creature.ControlledBy ChosenPlayer`, `Creature.ControlledBy TargetedPlayer,Planeswalker.ControlledBy TargetedPlayer`, `Creature.EquippedBy,Creature.YouCtrl+namedVecna`, `Creature.ExiledWithSource`, `Creature.faceDown+attacking,Creature.faceDown+blocking`, `Creature.Giant+YouCtrl`, `Creature.greatestCMC_CreatureControlledByRemembered`, `Creature.greatestPowerControlledByRemembered`, `Creature.Green+IsRemembered,Creature.White+IsRemembered`, `Creature.IsRemembered`, `Creature.IsRemembered,Land.IsRemembered`, `Creature.leastPower+withoutIndestructible`, `Creature.leastToughness`, `Creature.leastToughnessControlledByOpponent`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+CanBeTargetedByTriggeredSpellAbility`, `Creature.Other+YouCtrl`, `Creature.OwnedBy Player.Active`, `Creature.Party+YouOwn`, `Creature.powerLEX`, `Creature.RememberedPlayerCtrl`, `Creature.RememberedPlayerCtrl+cmcEQX,Planeswalker.RememberedPlayerCtrl+cmcEQX`, `Creature.RememberedPlayerCtrl+powerLE2`, `Creature.RememberedPlayerCtrl,Planeswalker.RememberedPlayerCtrl`, `Creature.SaddledThisTurn`, `Creature.Samurai+YouCtrl`, `Creature.tapped+Blue`, `Creature.tapped+nonGreen`, `Creature.tapped+withoutFlying`, `Creature.targetedBy`, `Creature.TargetedPlayerCtrl`, `Creature.TargetedPlayerCtrl+!IsRemembered`, `Creature.TargetedPlayerCtrl+cmcEQX,Planeswalker.TargetedPlayerCtrl+cmcEQX`, `Creature.TargetedPlayerOwn`, `Creature.unblocked`, `Creature.untapped`, `Creature.untapped+RememberedPlayerCtrl`, `Creature.untapped+YouCtrl`, `Creature.withoutBlitz+YouOwn`, `Creature.withShadow`, `Creature.yardGreatestPower+YouOwn`, `Creature.YouCtrl`, `Creature.YouCtrl+cmcEQX`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+Other`, `Creature.YouCtrl,Planeswalker.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl+leastToughnessControlledByOpponent`, `Creature.YouOwn`, `Creature.YouOwn+!IsRemembered`, `Creature.YouOwn+cmcEQ1`, `Creature.YouOwn+cmcEQ2`, `Creature.YouOwn+cmcEQ3`, `Creature.YouOwn+cmcEQX`, `Creature.YouOwn+nonLegendary`, `Creature.YouOwn+NotDefinedReplacedSimultaneousETB`, `Creature.YouOwn+Other+NotDefinedReplacedSimultaneousETB`, `Creature.YouOwn,Planeswalker.YouOwn`, `Curse.AttachedTo You`, `Doctor`, `Elf.YouOwn`, `Enchantment.YouDontCtrl`, `Equipment.AttachedTo Creature.IsRemembered`, `Equipment.AttachedTo Targeted`, `Equipment.YouOwn`, `Instant.IsRemembered,Sorcery.IsRemembered`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouOwn+cmcGE3,Sorcery.YouOwn+cmcGE3`, `Instant.YouOwn,Sorcery.YouOwn`, `Land`, `Land.IsRemembered,Artifact.IsRemembered`, `Land.nonBasic+RememberedPlayerCtrl`, `Land.RememberedPlayerCtrl`, `Land.TargetedPlayerCtrl`, `Land.YouCtrl`, `Land.YouDontCtrl`, `Land.YouOwn`, `Permanent`, `Permanent.!enchanted`, `Permanent.cmcGE3+OppCtrl`, `Permanent.greatestCMC_NonLandPermanentControlledByRemembered`, `Permanent.nonFood+YouOwn`, `Permanent.nonLand`, `Permanent.nonLand+!RememberedPlayerCtrl+!IsRemembered`, `Permanent.nonLand+!token`, `Permanent.nonLand+cmcLEX+IsRemembered`, `Permanent.nonLand+ControlledBy Remembered`, `Permanent.nonLand+RememberedPlayerCtrl`, `Permanent.nonLand+YouDontCtrl`, `Permanent.nonLand+YouOwn`, `Permanent.nonSaga+HasCounters`, `Permanent.RememberedPlayerCtrl`, `Permanent.RememberedPlayerCtrl+HasCounters`, `Permanent.RememberedPlayerOwn`, `Permanent.TargetedPlayerCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+Other`, `Permanent.YouDontCtrl`, `Permanent.YouDontCtrl+counters_GE1_AIM+withoutIndestructible`, `Permanent.YouOwn`, `Plains`, `Planeswalker.ControlledBy TriggeredPlayer`, `Planeswalker.YouCtrl`, `Soldier.YouOwn`, `Sorcery.YouOwn,Instant.YouOwn`, `Vehicle`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a artifact that player controls`, `Choose a card exiled with Muse Vessel`, `Choose a card exiled with Valki with mana value X`, `Choose a card in your hand`, `Choose a card or permanent`, `Choose a card revealed this way or a card in their graveyard`, `Choose a card that was revealed in targeted player's hand`, `Choose a card to be put into the hand of CARDNAME's controller`, `Choose a card to put into hand. If it's a land, you may put it onto the battlefield tapped instead.`, `Choose a card to put on your opponent's battlefield`, `Choose a card with mana value 4 or greater`, `Choose a Cave you control`, `Choose a commander you own`, `Choose a creature`, `Choose a creature card in this player's graveyard`, `Choose a creature card in your graveyard`, `Choose a creature card in your hand`, `Choose a creature card in your hand or a creature you control`, `Choose a creature card in your hand without blitz`, `Choose a creature card to reveal`, `Choose a creature card with power 2 or less`, `Choose a creature controlled by the player to your left`, `Choose a creature or planeswalker`, `Choose a creature or planeswalker card in this player's graveyard`, `Choose a creature or planeswalker to keep`, `Choose a creature or planeswalker with the greatest mana value among creatures and planeswalkers you control`, `Choose a creature or planeswalker with the highest mana value among creatures and planeswalkers you control`, `Choose a creature or planeswalker with the highest mana value to sacrifice`, `Choose a creature that player controls`, `Choose a creature this player controls`, `Choose a creature to be stolen`, `Choose a creature to destroy`, `Choose a creature to exchange text boxes with`, `Choose a creature to keep`, `Choose a creature with the highest mana value`, `Choose a creature with the least toughness among creatures your opponents control`, `Choose a creature you control`, `Choose a creature you control to attach an Equipment to`, `Choose a creature you control to attach the Equipment to`, `Choose a creature you control with equal or lesser power`, `Choose a creature you control with the greatest power`, `Choose a creature you want to control`, `Choose a Curse attached to you`, `Choose a Gate card to put onto the battlefield`, `Choose a Giant creature you control`, `Choose a land for CARDNAME's controller to sacrifice`, `Choose a land that player controls`, `Choose a land to exile`, `Choose a noncreature, nonland card`, `Choose a nonland card among the cards exiled (that can't be played)`, `Choose a nonland card exiled this way`, `Choose a nonland card in your hand`, `Choose a nonland card with mana value 3 or less`, `Choose a nonland permanent in your hand`, `Choose a nonland permanent to put on the battlefield under your control`, `Choose a nonland permanent with the highest mana value`, `Choose a nonland permanent you control`, `Choose a nonland permanent.`, `Choose a party creature card in your hand`, `Choose a permanent to untap`, `Choose a permanent you control`, `Choose a Soldier card in your hand`, `Choose a Sorcery`, `Choose a spell with mana value equal to Jarsyl, Dark Age Scion's intensity`, `Choose a token`, `Choose a Vehicle you control`, `Choose a white creature card in your hand`, `Choose an artifact or creature card`, `Choose an artifact or enchantment`, `Choose an attacker to block`, `Choose an Equipment attached to the targeted creature`, `Choose an equipment card in your hand`, `Choose an equipped creature you control`, `Choose an exiled card an opponent owns with a void counter on it`, `Choose an exiled card exiled with NICKNAME`, `Choose an face-down attacking or blocking creature`, `Choose an instant or sorcery card in your hand`, `Choose an instant or sorcery card in your hand or graveyard`, `Choose an instant or sorcery card in your hand with mana value 3 or greater`, `Choose another attacking creature with lesser power`, `Choose any number of creatures`, `Choose any number of creatures you control`, `Choose any number of non-Saga permanents with counters`, `Choose any number of other creatures that spell could target`, `Choose any number of Planeswalkers you control`, `Choose any number of tapped blue creatures you control`, `Choose any number of tapped creatures without flying you control`, `Choose any number of tapped nongreen creatures you control`, `Choose any number of untapped creatures you control`, `Choose creature to copy`, `Choose creature to exile`, `Choose creature to put on the battlefield under your control`, `Choose creatures to put on the battlefield`, `Choose five lands to keep`, `Choose five permanents you control`, `Choose half the creatures (rounded up) target player controls`, `Choose one creature to keep untapped`, `Choose one of the cards that entered the battlefield`, `Choose one of the exiled cards`, `Choose one or two creatures you control`, `Choose one to exile`, `Choose one to sacrifice`, `Choose one to take 5 damage`, `Choose six lands to keep`, `Choose six lands you control`, `Choose three lands to keep`, `Choose three nonland permanents you control`, `Choose three permanents to keep`, `Choose two cards not to exile`, `Choose two cards to shuffle into opponent's library`, `Choose two nontoken, non-Vehicle creatures you control`, `Choose two other cards named Calim, Djinn Emperor from your graveyard`, `Choose up to five permanents you control`, `Choose up to one nonbasic land this player controls`, `Choose up to one permanent with mana value 3 or greater`, `Choose up to one untapped creature you control to tap`, `Choose up to three Doctors`, `Choose up to three nonland permanents you don't control.`, `Choose up to two creature and/or land cards to reveal`, `Choose up to two creature and/or planeswalker cards in your hand`, `Choose up to two creature cards to reveal`, `Choose up to two creatures`, `Choose up to two creatures to keep`, `Choose up to two Plains for each creature tapped`, `Choose up to X creatures and/or planeswalkers you control`, `Exile any number of creature cards from your graveyard`, `Exile with Volatile Chimera`, `Reveal a card from your hand or the top of your library`, `Sacrifice any number of creatures with total power 12 or greater.`, `Secretly choose a creature`, `Secretly choose a creature in your graveyard`, `Secretly choose a creature or planeswalker targeted player controls`, `Select a nonland card`, `Select another creature you control`, `You may choose a card of this type from defending player's graveyard to exile`, `You may choose a card of this type to put into your hand`, `You may choose a card of this type to put onto the battlefield`, `You may choose a card with mana value 3 or greater`, `You may choose a card with the same name from target opponent's library`, `You may choose a card with the same name from your library`, `You may choose a card with this name from your library`, `You may choose a creature`, `You may choose a creature card in your hand`, `You may choose a nonland card`, `You may choose a nonland card in your hand`, `You may choose a nonland permanent`, `You may choose an artifact or creature card with mana value 1 you discarded this way`, `You may choose an artifact or creature card with mana value 2 you discarded this way`, `You may choose an artifact or creature card with mana value 3 you discarded this way`, `You may choose an Equipment to unattach from that creature`, `You may choose an instant or sorcery card in your hand`, `You may exile a nonland card from it`, `You may select a creature card`
- `ChoiceTitleAppend$`: TODO: Describe this parameter.
  Observed values: `ChosenType`, `Defined Player.IsRemembered`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command,Battlefield`, `Exile`, `Graveyard`, `Graveyard,Exile`, `Hand`, `Hand,Battlefield`, `Hand,Graveyard`, `Hand,Library`, `Library`, `None`, `Sideboard`
- `ChooseEach$`: TODO: Describe this parameter.
  Observed values: `Artifact & Battle & Creature & Enchantment & Land & Planeswalker`, `Artifact & Creature & Enchantment & Land`, `Artifact & Creature & Enchantment & Planeswalker`, `Artifact & Creature & Land`, `Party`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackingPlayer`
- `ChosenMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CheckYard`, `CountExiled`, `MimeoInYard`, `MimeoNumRemembered`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`, `LE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionGameTypes$`: TODO: Describe this parameter.
  Observed values: `Draft,QuestDraft`
- `ConditionManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `B R`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Equipment`, `Swamp`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `EQ3`, `GE2`, `GEX`
- `ControlAndNot$`: TODO: Describe this parameter.
  Observed values: `True`
- `ControlledByPlayer$`: TODO: Describe this parameter.
  Observed values: `Chooser`, `Left`, `Remembered`, `Right`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/CARDNAME>`, `SubCounter<4/LOYALTY>`, `W`, `SubCounter<X/LOYALTY>`, `Discard<1/Card>`, `T PayLife<1>`, `3 Sac<1/CARDNAME>`, `1`, `1 B T`, `T Sac<1/CARDNAME>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `ParentTarget`, `Player`, `Player.Chosen`, `Player.IsRemembered`, `Remembered`, `RememberedPlayer`, `TargetedAndYou`, `TargetedController`, `TargetedOrController`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredDefendingPlayer & You`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `DefinedCards$`: TODO: Describe this parameter.
  Observed values: `ExiledWith`, `ParentTargeted`, `Remembered`, `RememberedLKI.ControlledBy ChosenPlayer`, `Targeted`, `TargetedCard`, `TriggeredAttackers`, `TriggeredBlockers`, `TriggeredCards`, `TriggeredCards.Artifact,Creature`, `TriggeredSources`
- `EachBasicType$`: TODO: Describe this parameter.
  Observed values: `True`
- `EachDifferentPower$`: TODO: Describe this parameter.
  Observed values: `True`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `FromDesc$`: TODO: Describe this parameter.
  Observed values: `it`
- `Guess$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `IncludeSpellsOnStack$`: TODO: Describe this parameter.
  Observed values: `True`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `MinAmount$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `3`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `NoReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OrString$`: TODO: Describe this parameter.
  Observed values: `{p:You} conjures a duplicate of a random card from their library into your hand.`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `QuasiLibrarySearch$`: TODO: Describe this parameter.
  Observed values: `TargetedPlayer`, `You`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `RevealTitle$`: TODO: Describe this parameter.
  Observed values: `Chosen creatures. They will be destroyed.`, `Creatures chosen by opponent.`, `Randomly chosen permanent to be destroyed`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StartingWith$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Block`, `BounceArtifact`, `BounceCreature`, `BounceEnchant`, `BounceLand`, `CalimExile`, `ChooseYou`, `ChosenToHand`, `CopySpell`, `DBAdditionalCounter`, `DBAllOthers`, `DBAnimate`, `DBAnimate18`, `DBAnimateB`, `DBAnimateG`, `DBAnimateR`, `DBAnimateU`, `DBAnimateW`, `DBAttach`, `DBAttachEquip`, `DBBottom`, `DBBounce`, `DBBranch`, `DBChange`, `DBChangeOne`, `DBChangeZone`, `DBChangeZone1`, `DBChangeZone16`, `DBChangeZone19`, `DBChangeZone3`, `DBChangeZoneAll`, `DBChangeZoneBattlefield`, `DBChoose2`, `DBChoose3`, `DBChooseArtifactOpp`, `DBChooseB`, `DBChooseCard`, `DBChooseCardThree`, `DBChooseCardTwo`, `DBChooseCreatureYou`, `DBChooseEquip`, `DBChooseFromGraveyard`, `DBChooseG`, `DBChoosePlayer`, `DBChooseR`, `DBChooseU`, `DBChooseYou`, `DBCleanup`, `DBClone`, `DBConjure`, `DBControl`, `DBCopyPerm`, `DBCounter`, `DBDamage`, `DBDamageChosen`, `DBDamagePlayer`, `DBDealDamage`, `DBDelayedTrigger`, `DBDelayTrig`, `DBDestroy`, `DBDestroy12`, `DBDestroy8`, `DBDestroy9`, `DBDestroyAll`, `DBDestroyChosen`, `DBDig`, `DBDiscard`, `DBDmg`, `DBDraw`, `DBEffect`, `DBExchange`, `DBExchangeArtifact`, `DBExchangeCreature`, `DBExchangeText`, `DBExile`, `DBExileBoth`, `DBExileOpp`, `DBExileYou`, `DBFaceUp`, `DBGainControl`, `DBGenericChoice`, `DBGive`, `DBGuess`, `DBImprint`, `DBLook`, `DBManaLandOnlyEffect`, `DBMDamage`, `DBMoveHand`, `DBNoRegen`, `DBOneCounter`, `DBOppChooseCard`, `DBOpponentGainControl`, `DBOracleEffect`, `DBPayOrReturn`, `DBPhase`, `DBPlay`, `DBPlayEffect`, `DBPrevent`, `DBPump`, `DBPump1`, `DBPump10`, `DBPump14`, `DBPump15`, `DBPump3`, `DBPump8`, `DBPump9`, `DBPumpAll`, `DBPutArtifact`, `DBPutBattlefield`, `DBPutCounter`, `DBPutCounter20`, `DBPutX`, `DBRandom`, `DBRemoveCounter`, `DBRepeat`, `DBRepeatEach`, `DBRepeatEach17`, `DBReturn`, `DBReturnAll`, `DBSac`, `DBSac1`, `DBSacLand`, `DBSacrifice`, `DBSacrificeAll`, `DBSetVarBefore`, `DBShuffle`, `DBStoreSVar`, `DBTap`, `DBTap5`, `DBTapAll`, `DBTapOrUntap2`, `DBToken`, `DBUnattach`, `DBUntap`, `DBUntap4`, `DestroyAll`, `ExileChoice`, `ExileChosen`, `ExileCreatures`, `ExileYard`, `MakeItDance`, `MimeoAddCounters`, `MimeoExile`, `MoveChosen`, `MoveNotChosen`, `PhasesArtifact`, `PhasesCreature`, `PhasesLand`, `Pump4Tgt`, `ReturnCreature`, `SacAllOthers`, `SacRest`, `SacrificeSelf`, `StealChosen`, `SuspectOther`, `TapChosenCards`
- `TargetControls$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`, `4`, `NumCreatPW`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `2`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `3`, `B`, `Discard<1/Card>`, `G`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.Creature+YouCtrl+Other`, `Creature`, `Creature,Planeswalker`, `Creature.HasCounters`, `Creature.White+YouCtrl`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Opponent`, `Permanent.YouOwn`, `Player`
- `WithDifferentPowers$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithTotalPower$`: TODO: Describe this parameter.
  Observed values: `4`

## `ChooseColor`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `MostExcessOpponentControls`, `MostProminentAttackers`, `MostProminentComputerControls`, `MostProminentDualInComputerDeck`, `MostProminentHumanControls`, `MostProminentHumanCreatures`, `MostProminentInActivePlayerHand`, `MostProminentInComputerDeck`, `MostProminentInComputerDeckButGreen`, `MostProminentInGame`, `MostProminentInHumanDeck`, `MostProminentKeywordInComputerDeck`, `MostProminentPermanent`
- `AINoRecursiveCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `black,red`
- `ColorsFrom$`: TODO: Describe this parameter.
  Observed values: `ValidHand Card.YouOwn`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T`, `1 W`, `5 W W`, `1 U`, `G`, `2 B`, `2 R`, `T`, `0`, `2 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `TriggeredPlayer`, `You`
- `Exclude$`: TODO: Describe this parameter.
  Observed values: `black`, `blue`, `green`, `red`, `white`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `InstantSpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `OrColors$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Coven —`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Animate`, `ChooseCT`, `ChooseOpp`, `ChooseP`, `DBAnimate`, `DBDmg`, `DBDmgEach`, `DBEffect`, `DBEffect2`, `DBExile`, `DBGainLife`, `DBMana`, `DBProtection`, `DBPump`, `DBPutCounter`, `DBRevealDiscard`, `DBRevealHand`, `DBScryingGlassRevealHand`, `DBSwayAnimate`, `DBToken`, `DBWash`, `DestroyAll`, `FilterForExile`, `SehtsProtection`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `TwoColors$`: TODO: Describe this parameter.
  Observed values: `True`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`

## `ChooseDirection`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Aminatou`, `GainControl`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<6/LOYALTY>`, `SubCounter<2/LOYALTY>`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBControl`, `DBEffect`, `DBGainControl`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`

## `ChooseEvenOdd`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `CMCInHand`, `CMCOppControlsByPower`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `ListTitle$`: TODO: Describe this parameter.
  Observed values: `Choose ODD or EVEN`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDestroyAll`, `DBExile`

## `ChooseNumber`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Damnation`, `DigACard`, `HighestGetCounter`, `HighestLoseLife`, `LoseLife`, `LowestLoseLife`, `Max`, `MaxForAnyController`, `Min`, `OptionalDraw`, `PowerLeakMaxMana.2`, `Random`, `RepeatDraw`, `SweepCreatures`, `Vermin`
- `ChooseAnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChooseNumberSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBLoseLife`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Resolved`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GT2`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<1/LOYALTY>`, `3 B Discard<1/Card>`, `AddCounter<0/LOYALTY>`, `3 T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `Player`, `Player.IsRemembered`, `Remembered`, `Targeted`, `TargetedAndYou`, `You`
- `GuessCorrect$`: TODO: Describe this parameter.
  Observed values: `DBSac`
- `Guesser$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `GuessWrong$`: TODO: Describe this parameter.
  Observed values: `DBLoseLife`
- `Highest$`: TODO: Describe this parameter.
  Observed values: `DBLoseLife`
- `KeepSecret$`: TODO: Describe this parameter.
  Observed values: `True`
- `ListTitle$`: TODO: Describe this parameter.
  Observed values: `amount of damage to be dealt`, `amount of energy to pay`, `amount of life to pay`, `amount of mana to pay`, `Choose amount of energy to pay`, `Discard how many cards?`, `How many times do you want repeat this process?`, `number of cards in your graveyard to exile`
- `Lowest$`: TODO: Describe this parameter.
  Observed values: `DBLoseHalfLife`
- `MatchedAbility$`: TODO: Describe this parameter.
  Observed values: `DBSacrifice`
- `Max$`: TODO: Describe this parameter.
  Observed values: `10`, `13`, `20`, `3`, `4`, `5`, `6`, `7`, `Count$YourCountersEnergy`, `LifeAmountX`, `LifeTotal`, `Max`, `MaxChoice`, `X`, `Y`
- `Min$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`
- `Notify$`: TODO: Describe this parameter.
  Observed values: `True`
- `NotLowest$`: TODO: Describe this parameter.
  Observed values: `DBDiscard`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberHighest$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveChoices$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCheckPaid`, `DBChoice`, `DBChoose`, `DBChooseCard`, `DBDealDamage`, `DBDestroyAll`, `DBDig`, `DBDiscard`, `DBDmg`, `DBDraw`, `DBImmediateTrig`, `DBMill`, `DBPay`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBRepeat`, `DBReveal`, `DBSac`, `DBScryingGlassChooseColor`, `DBShuffle`, `DBStore`, `DBStun`, `DBToken`, `DBVoidDestroyAll`, `FlipCoin`, `Pay`, `RepeatFlip`
- `UnmatchedAbility$`: TODO: Describe this parameter.
  Observed values: `DBFillSafe`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `ChoosePlayer`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BestAllyBoardPosition`, `Curse`, `LeastCreatures`, `MostCardsInHand`, `Pump`, `Random`
- `CantChooseSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBTap`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `ChosenCardController`, `NonChosenPlayer`, `Opponent`, `Player`, `Player.!IsRemembered`, `Player.IsRemembered`, `Player.Opponent`, `Player.Opponent+!EnchantedBy`, `Player.Opponent+!IsRemembered`, `Player.Opponent+lifeEQX`, `Player.Opponent+withMoreLandsThanYou`, `Player.OpponentOf Remembered`, `Player.OpponentOf ReplacedPlayer`, `Player.Other`, `Player.withLowestLife`, `Player.withMostLife`, `ThisTargetedPlayer`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a player`, `Choose a player to create two Treasure tokens`, `Choose a player to draw a card`, `Choose a player to put two +1/+1 counters on a creature they control`, `Choose a player with the most life or tied for most life`, `Choose an opponent`, `Choose an opponent to create treasure tokens and scry 2`, `Choose an opponent to draw a card`, `Choose an opponent to give control to`, `Choose an opponent to look at their hand`, `Choose an opponent whose top library card to exile`, `Choose an player with lowest life total`, `Choose another player`
- `ChooseSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBPump`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `LE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`
- `ConditionNotPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Swamp`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `GE3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 W`, `T`, `2 T Sac<1/Artifact>`, `1 B T`, `T Sac<1/Forest>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `ReplacedPlayer`, `TriggeredCardOwner`, `You`
- `DontNotify$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OrOtherConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Grenades! —`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CantAttackEffect`, `Card`, `ChoosePTwo`, `Counters`, `DBAttach`, `DBChangeZone`, `DBChangeZone1`, `DBChoice`, `DBChoose`, `DBChooseCard2`, `DBChooseCreature`, `DBChooseLand`, `DBChoosePlayer2`, `DBChooseSpell`, `DBChooseType`, `DBConjure`, `DBControlPlayer1`, `DBCounters`, `DBDamage`, `DBDealDamage`, `DBDelayTrig`, `DBDig`, `DBDiscard`, `DBDiscard18`, `DBDmg`, `DBDonate`, `DBDraw`, `DBDraw7`, `DBEffect`, `DBExile`, `DBFlip`, `DBGainControl`, `DBGainLife10`, `DBGainLifeYou`, `DBGiveControl`, `DBHorseDonate`, `DBImmediateTrig`, `DBLook`, `DBLoseLife`, `DBMana`, `DBMill13`, `DBOppChoose`, `DBPump`, `DBReturnYou`, `DBSac`, `DBToken`, `DBToken2`, `DBTwoPiles`, `DBUntap`, `DelTrigSlowtrip`, `DonateTheVale`, `LoseControl`, `MoveToPlay`, `NameOpp`, `OppPickOne`, `OppPickTwo`, `OppTreasure`, `PrepChamps`, `Tokens`, `TrigChoice`, `TrigSearchHand`, `YouChoice`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature,Player,Planeswalker`, `Opponent`, `Player`

## `ChooseSector`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Destroy`, `Pump`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<1/LOYALTY>`, `SubCounter<5/LOYALTY>`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDestroyAll`, `DBPutCounterAll`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`

## `ChooseSource`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `NeedsPrevention`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Card,Emblem`, `Card.Artifact`, `Card.BlackSource`, `Card.BlackSource,Card.RedSource`, `Card.BlueSource`, `Card.ChosenColorSource`, `Card.GreenSource`, `Card.RedSource`, `Card.RedSource,Card.BlackSource`, `Card.SharesColorWith ActivationColor`, `Card.SharesColorWith Imprinted`, `Card.WhiteSource`, `Card.YouCtrl,Emblem.YouCtrl`, `Land`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a source`, `Choose a source that shares a color with the exiled card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `W Sac<1/CARDNAME>`, `T`, `2 T`, `Sac<1/CARDNAME>`, `W T Discard<1/Card>`, `1 W W T Discard<1/Card>`, `1 Sac<1/Creature>`, `2`, `1`, `PayEnergy<2>`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CoinFlip`, `DBEffect`, `DBEffectSB`, `DBStoreSVar`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`

## `ChooseType`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `ChosenLandwalk`, `MostNeededType`, `MostProminentComputerControls`, `MostProminentComputerControlsOrOwns`, `MostProminentInComputerDeck`, `MostProminentInComputerDeckNonToken`, `MostProminentInComputerGraveyard`, `MostProminentOppControls`, `ProtectionFromType`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChooseNoted$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChooseType2$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 R T`, `T`, `Sac<1/CARDNAME>`, `X`, `1`, `1 U`, `2 U U T`, `2 Return<1/Land>`, `1 T`, `SubCounter<6/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player.Chosen`, `Player.IsRemembered`, `You`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `InvalidTypes$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature,Land`, `Instant,Sorcery,Kindred`, `Mountain,Forest,Plains`, `Wall`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `MostPrevalentInDefinedZone$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer_Library`
- `Note$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ApplyPressure`, `ChooseType2`, `DBAnimate`, `DBAnimateAll`, `DBBranch`, `DBChangeZoneAll`, `DBChooseBis`, `DBCleanup`, `DBCleanupChosen`, `DBClone`, `DBCloneAll`, `DBCounters`, `DBDamage`, `DBDealDamage`, `DBDestroyAll`, `DBDestroyOther`, `DBDig`, `DBDigUntil`, `DBDraw`, `DBEffect`, `DBGainLife`, `DBPump`, `DBPumpAll`, `DBPumpOther`, `DBPutCounterAll`, `DBRemember`, `DBReturn`, `DBReturnAll`, `DBReveal`, `DBSeek`, `DBTap`, `DBTapOrUntapAll`, `DBUntapAll`, `EffChangeType`, `ShamanDig`, `ShuffleInto`, `TribalPump`, `TrigSac`, `TsabosDiscard`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Basic Land`, `Card`, `Creature`, `CreatureInTargetedDeck`, `Land`, `Nonbasic Land`, `Planeswalker`, `Shared`
- `TypesFromDefined$`: TODO: Describe this parameter.
  Observed values: `ExiledWith`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `ValidTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature,Enchantment,Instant,Sorcery`, `Artifact,Creature,Land`, `Artifact,Enchantment,Instant,Sorcery,Planeswalker`, `Creature,Land`, `Elemental,Elf,Faerie,Giant,Goblin,Kithkin,Merfolk,Treefolk`, `Human,Merfolk,Goblin`, `Land,Nonland`

## `ClaimThePrize`

TODO: Write documentation.

**Parameters:**
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE6_LUCK`

## `Clash`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredDefendingPlayer`
- `OtherwiseSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDiscardOne`, `DBReset`, `OppControl`
- `RememberClasher$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDeclined`, `DBExile`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Player`
- `WinSubAbility$`: TODO: Describe this parameter.
  Observed values: `AdditionalPump`, `DBDamage`, `DBDamageController`, `DBDelTrig`, `DBDestroyAll`, `DBDiscardTwo`, `DBEffect`, `DBGain`, `DBLibrary`, `DBMill`, `DBPump`, `DBPutCounter`, `DBReturn`, `DBStoreSVar`, `DBUntap`, `RecrossReturn`, `YouControl`

## `Cleanup`

TODO: Write documentation.

**Parameters:**
- `ClearChosenCard$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearChosenColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearChosenPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearChosenType$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearCoinFlips$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearImprinted$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearNamedCard$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearRemembered$`: TODO: Describe this parameter.
  Observed values: `True`, `true`
- `ClearTriggered$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `TriggeredNewCardLKICopy`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.inRealZone Graveyard`
- `ForgetDefined$`: TODO: Describe this parameter.
  Observed values: `ActivePlayer`, `TriggeredCard`, `TriggeredTargetHostCard`
- `Log$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChangePermanent`, `DBAddEOT`, `DBAnimate`, `DBBounceMe`, `DBChange`, `DBChangeZone`, `DBChoose`, `DBChooseA2C3`, `DBChooseA2L3`, `DBChooseA3`, `DBChooseArtifactYou`, `DBChooseC2A3`, `DBChooseC2L3`, `DBChooseC3`, `DBChooseL2A3`, `DBChooseL2C3`, `DBChooseL3`, `DBCleanup2`, `DBClearNotes`, `DBClearSVar`, `DBDigUntil`, `DBDraft`, `DBDraw`, `DBEffect`, `DBEmblem`, `DBExile`, `DBExile1`, `DBExileSelf`, `DBExileTop`, `DBFlip`, `DBGrind`, `DBImprint`, `DBInvestigate`, `DBLoseLife`, `DBMana`, `DBMassShuffle`, `DBMill`, `DBMonarchEffect`, `DBPerpetual`, `DBPlayEffect`, `DBRem`, `DBReset`, `DBReveal`, `DBSac`, `DBSacrificeE`, `DBSacrificeP`, `DBScry`, `DBSearch`, `DBSeek`, `DBShuffle`, `DBSpace`, `DBStore`, `DBToken`, `DeathrendersCall`, `FakeScry`, `FindHighestCMC`, `FlickerformAttach`, `GoToBottom`, `MaybeRepeat`, `PWAway`, `RememberTargets`, `SearchLibrary`, `TrigChoose`, `TrigRemember`, `TrigTempt`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `RememberedController`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`

## `Cloak`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Card.YouCtrl`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `TopOfLibrary`, `ValidLibrary Card.TopLibrary+OwnedBy TriggeredTarget`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `RememberedController`
- `RememberCloaked$`: TODO: Describe this parameter.
  Observed values: `True`
- `Shuffle$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBAttach`, `DBCleanup`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`

## `Clone`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Delirium`
- `AddAbilities$`: TODO: Describe this parameter.
  Observed values: `ABMana`, `EvilTwin`, `Gigantoplasm`, `MercurialBounce`, `ReturnSakashima`
- `AddColors$`: TODO: Describe this parameter.
  Observed values: `Black`, `Blue & Black`
- `AddKeywords$`: TODO: Describe this parameter.
  Observed values: `Changeling`, `Crew:3`, `Defender`, `Flying`, `Haste`, `Haste & Dethrone`, `Hexproof`, `IfNew Vanishing:3`, `Myriad`, `Partner`, `Vigilance`
- `AddStaticAbilities$`: TODO: Describe this parameter.
  Observed values: `FamilyTease`, `NoLegendRule`, `Unblockable`
- `AddSVars$`: TODO: Describe this parameter.
  Observed values: `CryptoplasmCopy`, `InvocationDBReturn,InvocationTrigExile,InvocationExileUpkeep`, `IrmaCopy,IrmaPutCounter`, `LazavCopy`, `PhantasmalImageSac,Targeting`, `ProgenitorCopy,ProgenitorTrig`, `RonsoCounter,RonsoTap,RonsoClone`, `TrigArtisanCopy`, `TrigCloneCopy`, `TrigConnive`, `TrigDamage,TrigDraw`, `TrigDamage,TrigEnergy`, `TrigDestroy`, `TrigDraw`, `TrigProteanCopy`, `TrigReturnSak`, `VesDopCopy`, `VesDopCopy,VesDopUpkeepTrig`, `VesShapeTurn,VesShapeUpkeepTrig`, `X`
- `AddTriggers$`: TODO: Describe this parameter.
  Observed values: `AttackTrig`, `DrawTrig`, `ETBDestroy`, `InvocationExileUpkeep`, `PhantasmalImageTgtTrig`, `ProgenitorTrig`, `TrigDamage`, `VesDopUpkeepTrig`, `VesShapeUpkeepTrig`
- `AddTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact & Creature`, `Artifact & Creature & Synth`, `Bird`, `Cave`, `Creature & Dinosaur`, `Dragon`, `Enchantment`, `Faerie & Shapeshifter`, `Illusion`, `Land`, `Legendary`, `Legendary & Snow`, `Legendary & Zombie`, `Ninja`, `Phyrexian`, `Pirate`, `Shapeshifter & Rogue`, `Spider & Human & Hero`, `Spirit`, `Vehicle & Artifact`, `Wall`, `Zombie`
- `AiChoiceLogic$`: TODO: Describe this parameter.
  Observed values: `BestOppCtrl`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtLeast1`, `CloneBestCreature`, `IfDefinedCreatureIsBetter`
- `ChoiceOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact.Other`, `Artifact.Other,Enchantment.Other`, `Artifact.YouCtrl+Other,Creature.YouCtrl+Other`, `Card.Creature+ExiledWithSource`, `Card.token+YouCtrl`, `Card.TriggeredCards+Creature`, `Creature`, `Creature.Ally+Other`, `Creature.counters_GE1_TAKEOVER`, `Creature.ExiledWithSource`, `Creature.nonLegendary`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+cmcLEY`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl,Planeswalker.Other+YouCtrl`, `Creature.Other,Artifact.Other`, `Creature.ThisTurnEnteredFrom_Battlefield`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+powerGE4`, `Doctor.YouOwn+ThisTurnEnteredFrom_Library`, `Enchantment.Other`, `Enchantment.Other+YouCtrl`, `Equipment.Other`, `Land.Other`, `Permanent`, `Permanent.nonLand+Other`, `Permanent.Other+YouCtrl`, `Permanent.ThisTurnEntered+Other`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a card exiled with Reflection Net`, `Choose a creature card among the exiled cards to copy`, `Choose a creature on the battlefield to copy`, `Choose a creature to copy`, `Choose a creature you control`, `Choose a nonlegendary creature to copy`, `Select another target creature you control`, `You may choose a token you control`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`
- `CloneTarget$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Enchanted`, `Equipped`, `Imprinted`, `ParentTarget`, `Remembered`, `ReplacedCard`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredTarget`, `TriggeredTargetLKICopy`, `Valid Artifact.YouCtrl+NotDefinedTargeted`, `Valid Card.token+YouCtrl`, `Valid Creature.!token+YouCtrl+!IsRemembered`, `Valid Creature.NotDefinedTargeted`, `Valid Creature.YouCtrl`, `Valid Creature.YouCtrl+NotDefinedTargeted`, `Valid Land.YouCtrl+ChosenType`, `Valid Permanent.nonLand+YouCtrl`, `Valid Shapeshifter.YouCtrl`, `Valid Shard.YouCtrl`
- `CloneZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `MimeoNumRemembered`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `ParentTarget`, `Remembered`, `TopOfLibrary`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `LT1`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `CopyFromChosenName$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 U Exile<1/Artifact.!token+Other+Creature/select another target artifact creature>`, `tapXType<2/Creature>`, `X`, `3`, `2`, `1 U R`, `AddCounter<0/LOYALTY>`, `2 U`, `2 G G`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Sacrifice another creature:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Enchanted`, `Exiled`, `ExiledWith`, `Imprinted`, `ParentTarget`, `Remembered`, `Remembered.Creature`, `RememberedLKI`, `ReplacedCard`, `Sacrificed`, `Self`, `Targeted`, `TopOfLibrary`, `TriggeredCardLKICopy`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `UntilEndOfTurn`, `UntilFacedown`, `UntilNextEndStep`, `UntilTargetedUntaps`, `UntilUnattached`, `UntilYourNextTurn`
- `Embalm$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExcludeChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `GainThisAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ImprintRememberedNoCleanup$`: TODO: Describe this parameter.
  Observed values: `True`
- `IntoPlayTapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `KeepName$`: TODO: Describe this parameter.
  Observed values: `True`
- `NewName$`: TODO: Describe this parameter.
  Observed values: `Chameleon, Master of Disguise`, `Gogo, Mysterious Mime`, `Irma, Part-Time Mutant`, `Kimahri, Valiant Guardian`, `Lazav, Dimir Mastermind`, `Lazav, the Multifarious`, `Olag, Ludevic's Hubris`, `Sakashima the Impostor`, `Sarkhan, Soul Aflame`, `Sunfrill Imitator`, `Superior Spider-Man`
- `NonLegendary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Delirium —`
- `PumpDuration$`: TODO: Describe this parameter.
  Observed values: `EOT`
- `PumpKeywords$`: TODO: Describe this parameter.
  Observed values: `Haste`
- `RememberCloneOrigin$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveSubTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `SetColor$`: TODO: Describe this parameter.
  Observed values: `Blue`, `White`
- `SetPower$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `4`, `5`, `7`, `X`
- `SetToughness$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `12`, `2`, `3`, `4`, `5`, `6`, `7`, `Y`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddCounter`, `DBAnimate`, `DBCleanup`, `DBClearChosen`, `DBConditionEffect`, `DBCopy`, `DBImmediateTrig`, `DBImprint`, `DBPrevent`, `DBPump`, `DBPutCounter`, `DBTrigger`, `DelTrig`, `IrmaPutCounter`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `nonlegendary creature you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment,Land`, `Artifact.Other,Enchantment.Other`, `Artifact.YouCtrl`, `Artifact.YouCtrl+cmcEQX+!token`, `Artifact.YouCtrl,Creature.YouCtrl`, `Creature`, `Creature.ChosenType+YouCtrl`, `Creature.Dinosaur+Other+YouCtrl`, `Creature.ExiledWithSource`, `Creature.HasCounters`, `Creature.Legendary+YouCtrl`, `Creature.nonLegendary`, `Creature.nonLegendary+Other+attacking`, `Creature.nonLegendary+YouCtrl`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+YouCtrl`, `Creature.TriggeredCrew+nonLegendary`, `Creature.YouCtrl`, `Creature.YouCtrl+!TriggeredTarget`, `Creature.YouOwn+cmcEQX`, `Land`, `Permanent.nonAura`, `Permanent.Other`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl+Other`, `Permanent.YouOwn`

## `Connive`

TODO: Write documentation.

**Parameters:**
- `ConniveNum$`: TODO: Describe this parameter.
  Observed values: `X`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3`, `B T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Convoked`, `Equipped`, `Targeted`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChooseCard`, `DBConvert`, `DBImmediateTrigger`, `DBPhase`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.attacking`, `Creature.YouCtrl`

## `ControlPlayer`

TODO: Write documentation.

**Parameters:**
- `Combat$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `OptionalCost`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `Controller$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Player.Chosen`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T Sac<1/CARDNAME>`, `SubCounter<7/LOYALTY>`, `15 Exile<1/OriginalHost/The Dominion Bracelet>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player.Chosen`, `Targeted`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `DominionBraceletX`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ControlTurn`, `DBChange`, `DBControlPlayer2`, `DBDelTrig`, `DBExile`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `ControlSpell`

TODO: Write documentation.

**Parameters:**
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `TriggeredSpellAbility`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `Exchange`, `Gain`
- `NewController$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`
- `Remember$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChooseTargets`, `DBCopy`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`, `Spell.numTargets EQ1`
- `TargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `Permanent.inRealZoneBattlefield,Player`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.nonCreature`

## `CopyPermanent`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AddAbilities$`: TODO: Describe this parameter.
  Observed values: `FoodSac`
- `AddColors$`: TODO: Describe this parameter.
  Observed values: `Black`, `Green`, `Red`
- `AddKeywords$`: TODO: Describe this parameter.
  Observed values: `Double Strike & Haste`, `Flying`, `Flying & Haste`, `Haste`, `Menace`, `Menace & Haste`, `Toxic:1`, `Trample`, `Trample & Haste`, `Vigilance & Menace`
- `AddStaticAbilities$`: TODO: Describe this parameter.
  Observed values: `ConstructBuff`, `EquipReduce`
- `AddSVars$`: TODO: Describe this parameter.
  Observed values: `DelinaTrigExile`, `HofriTrigReturn`, `NorinExile`, `TrigFight,TrigChange`, `TrigFight,TrigFightBis`
- `AddTriggers$`: TODO: Describe this parameter.
  Observed values: `Norin1,Norin2`, `TrigChange`, `TrigFight`, `TrigLeavesBattlefield`, `TrigPhase`
- `AddTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact & Creature`, `Artifact & Creature & Synth`, `Artifact & Creature & Thopter`, `Artifact & Food`, `Construct & Artifact`, `Coward`, `Creature`, `Creature & Balloon`, `Creature & Construct`, `Creature & Dinosaur`, `Creature & Eldrazi`, `Creature & Fractal`, `Creature & Soldier`, `Creature & Spirit`, `Creature & Squirrel`, `Creature & Zombie`, `Dragon & Creature`, `Enchantment`, `Enchantment & Creature`, `Food & Golem & Artifact & Creature`, `Golem & Artifact & Creature`, `Hero`, `Illusion`, `Legendary`, `Mutant`, `Nightmare`, `Reflection`, `Spirit`, `Tyranid`, `Zombie`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtEOT`, `AtOppEOT`, `Different`, `DuplicatePerms`, `MimicVat`, `MomirAvatar`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Kraken.Other+attacking,Leviathan.Other+attacking,Octopus.Other+attacking,Serpent.Other+attacking`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Exile`, `ExileCombat`, `Sacrifice`, `SacrificeCombat`, `SacrificeUpkeep`, `YourSacrifice`
- `AtEOTCondition$`: TODO: Describe this parameter.
  Observed values: `Y`
- `AtEOTDesc$`: TODO: Describe this parameter.
  Observed values: `At the beginning of the next end step, exile that token unless NICKNAME is your Ring-bearer.`
- `AtEOTTrig$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Sacrifice`, `You_Sacrifice`
- `AttachAfter$`: TODO: Describe this parameter.
  Observed values: `True`
- `AttachedTo$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Imprinted`, `Remembered`, `Self`, `TriggeredAttackerLKICopy`, `TriggeredCardLKICopy`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact.token+YouCtrl,Creature.token+YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Card`, `Card.IsCommander+YouOwn`, `Card.token+nonSaga+YouCtrl`, `Card.TriggeredCards`, `Creature.IsImprinted`, `Creature.nonLegendary+SaddledThisTurn`, `Creature.RememberedPlayerCtrl`, `Enchantment.nonLegendary+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+Other`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a commander you own`, `Choose a non-Saga token you control`, `Choose a nonlegendary enchantment you control`, `Choose a permanent you control to copy`, `Choose one of those creatures to copy`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ChosenMapIndex$`: TODO: Describe this parameter.
  Observed values: `0`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Blessing`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `RememberedSize`, `Result`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Imprinted`, `Remembered`, `RememberedLKI`, `TriggeredSpellAbility`
- `ConditionManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `R G`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `R G`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.IsImprinted+inZoneExile`, `Card.nonAura`, `Card.nonLegendary`, `Card.Self+AttachedTo Creature.YouCtrl`, `Creature`, `Permanent`, `Spell.IsTargeting Valid Permanent.YouCtrl~Other`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ20`, `GE1`, `GE5`
- `Controller$`: TODO: Describe this parameter.
  Observed values: `NonRememberedController`, `Opponent`, `Player.IsRemembered`, `Remembered`, `RememberedController`, `Targeted`, `TargetedController`, `TargetedPlayer`, `TriggeredCardController`, `You`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W T`, `ExileFromGrave<1/Creature> Mana<0\Exiled>`, `1 G`, `1`, `RevealFromExile<1/Creature.YouOwn+NotedForCallerOfTheUntamed> X T`, `AddCounter<1/LOYALTY>`, `5`, `3 T Sac<1/Zombie.Other/another zombie>`, `7`, `1 U`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Exile a creature card from your graveyard and pay its mana cost:`, `{X}, {T}`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ChosenMap`, `CounterPutCards`, `DelayTriggerRememberedLKI`, `DirectRemembered`, `Enchanted`, `Equipped`, `Exiled`, `ExiledWith`, `Imprinted`, `Imprinted.ExiledWithSource`, `ParentTarget`, `Remembered`, `RememberedLKI`, `Revealed`, `Sacrificed`, `Self`, `Spawner>Sacrificed`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredCards`, `TriggeredSourceLKICopy`, `TriggeredSpellAbilityTargets`, `Valid Artifact.YouCtrl`, `Valid Card.token+YouCtrl+ThisTurnEntered`, `Valid Creature.ChosenType+YouCtrl`, `Valid Creature.nonLegendary+YouCtrl`, `Valid Creature.TargetedPlayerCtrl`, `Valid Creature.token+YouCtrl`, `Valid Creature.token+YouCtrl+ThisTurnEntered`, `Valid Equipment.Attached,Aura.Attached`, `Valid Permanent.!token+AttachedTo TriggeredAttackerLKICopy`, `Valid Permanent.Other+YouCtrl+nonLand`, `Valid Permanent.token+YouCtrl`, `Valid Permanent.token+YouCtrl+ChosenType+ThisTurnEntered`, `ValidAll Card.IsCommander+YouOwn`, `ValidExile Card.Creature+YouOwn+counters_GE1_MEMORY`, `ValidExile Card.ExiledWithSource`, `ValidGraveyard Creature.YouOwn`
- `DefinedName$`: TODO: Describe this parameter.
  Observed values: `Arrest`, `Forest`, `Mutavault`, `Pacifism`, `Spellgorger Weird`, `Tarmogoyf`, `Wastes`
- `DoesntHaveThisAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintTokens$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `3`
- `NewName$`: TODO: Describe this parameter.
  Observed values: `Mishra's Warform`, `Prisoner Zero`
- `NonLegendary$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCopies$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `5`, `Wins`, `X`, `Y`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `2`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `Populate$`: TODO: Describe this parameter.
  Observed values: `True`
- `PumpDuration$`: TODO: Describe this parameter.
  Observed values: `EOT`, `UntilYourNextTurn`
- `PumpKeywords$`: TODO: Describe this parameter.
  Observed values: `Haste`
- `RandomCopied$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomNum$`: TODO: Describe this parameter.
  Observed values: `1`
- `RememberTokens$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveCardTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveKeywords$`: TODO: Describe this parameter.
  Observed values: `Soulbond`
- `RemoveSubTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `SetColor$`: TODO: Describe this parameter.
  Observed values: `Black`, `Black,Green`, `Colorless`, `Green`, `White`
- `SetCreatureTypes$`: TODO: Describe this parameter.
  Observed values: `Alien`, `Demon`, `Frog`, `Illusion`, `Insect`, `Wraith`, `Zombie`
- `SetLoyalty$`: TODO: Describe this parameter.
  Observed values: `1`
- `SetPower$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `dX`, `Imprinted$CardPower`
- `SetToughness$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `dY`, `Imprinted$CardToughness`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ClearImprinted`, `CopyFight`, `DBAnimate`, `DBCastSp`, `DBChangeZoneAll`, `DBCleanup`, `DBClearNamed`, `DBCount`, `DBCounter`, `DBDraw`, `DBEnergy`, `DBGoad`, `DBMill`, `DBNotRepeat`, `DBPlaneswalk`, `DBProlif`, `DBPumpAll`, `DBPutCounter`, `DBPutCountersAll`, `DBRepeat`, `DBReset`, `DBSac`, `DBScry`, `DBToken`, `DBUntap`, `DBWin`, `DelTrig`, `ExileTokens`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `TargetingPlayerControls$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `MaxTargets`, `OneEach`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Graveyard`, `Exile`, `Graveyard`
- `TokenAttacking$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedPlayer`, `TriggeredAttackedTarget`, `True`
- `TokenBlocking$`: TODO: Describe this parameter.
  Observed values: `Imprinted`
- `TokenOwner$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`
- `TokenRemembered$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `TokenTapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1 G`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidSupportedCopy$`: TODO: Describe this parameter.
  Observed values: `Creature.cmcEQX`, `Creature.Sliver+nonShapeshifter+cmcEQX`, `Equipment.cmcLTX`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `creature you control`, `non-Aura permanent you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature,Land`, `Artifact.ControlledBy TriggeredTarget`, `Artifact.Creature+YouCtrl`, `Artifact.nonCreature+YouCtrl`, `Artifact.Other+YouCtrl`, `Artifact.token+YouCtrl`, `Artifact.YouCtrl`, `Artifact.YouCtrl+token`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouCtrl,Enchantment.YouCtrl`, `Artifact.YouDontCtrl`, `Card.Elemental+YouCtrl`, `Card.token+nonSaga+YouCtrl`, `Card.token+YouCtrl`, `Creature`, `Creature,Artifact`, `Creature.!token`, `Creature.!token+attacking TriggeredAttackedTarget`, `Creature.!token+doesNotShareNameWith Card.token+YouCtrl`, `Creature.!token+YouCtrl+Other`, `Creature.attacking+Other`, `Creature.attacking+Other+Legendary+YouCtrl`, `Creature.cmcLEX`, `Creature.IsImprinted+ExiledWithSource`, `Creature.IsTriggerRemembered`, `Creature.nonArtifact+YouCtrl`, `Creature.nonFrog`, `Creature.nonLegendary+YouCtrl`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+attacking`, `Creature.Other+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+nonLegendary+Other`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other,Artifact.YouCtrl+Other`, `Creature.YouCtrl,Artifact.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouOwn`, `Elf.YouCtrl`, `Enchantment.nonLegendary+YouCtrl`, `Enchantment.YouCtrl+doesNotShareNameWith OtherYourBattlefield`, `Goblin.YouCtrl`, `Kithkin.YouCtrl`, `Land`, `Merfolk.YouCtrl`, `Opponent`, `Permanent`, `Permanent.Creature+token+ThisTurnEntered`, `Permanent.nonAura+YouCtrl`, `Permanent.nonCreature`, `Permanent.nonLand+YouCtrl+Other`, `Permanent.OppCtrl`, `Permanent.token+ThisTurnEntered`, `Permanent.token+YouCtrl`, `Permanent.token+YouCtrl+!namedDutiful Replicator`, `Permanent.token+YouCtrl+ThisTurnEntered`, `Permanent.YouCtrl`, `Player`, `Player.!TriggeredCardController`
- `WithCountersAmount$`: TODO: Describe this parameter.
  Observed values: `Y`
- `WithCountersType$`: TODO: Describe this parameter.
  Observed values: `P1P1`
- `WithDifferentNames$`: TODO: Describe this parameter.
  Observed values: `True`

## `CopySpellAbility`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `AddTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Spirit`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AlwaysCopyActivatedAbilities`, `ChainOfAcid`, `ChainOfSmog`, `Once`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `OwnedOnly`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `X`, `Y`
- `CantCopy$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$ThisTurnCast_Card.YouCtrl`
- `ChooseOnlyOne$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Self`, `Targeted`, `TriggeredSpellAbility`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Card`, `Card.counters_EQ0_DELAY`, `Card.Self+counters_GE4_QUEST`, `Card.sharesCardTypeWith TriggeredCardLKICopy`, `Card.wasCastFromGraveyard`, `Enchantment.YouCtrl`, `Instant.YouOwn,Sorcery.YouOwn`, `Permanent`, `Planeswalker.YouCtrl,Cleric.YouCtrl,Druid.YouCtrl,Shaman.YouCtrl,Warlock.YouCtrl,Wizard.YouCtrl`, `Spell.IsTargeting Valid Permanent,Spell.IsTargeting Player`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Controller$`: TODO: Describe this parameter.
  Observed values: `NextOpponentToYourLeft`, `NonTriggeredCardController`, `Remembered`, `Targeted`, `TargetedController`, `TargetedOrController`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredSpellAbilityController`, `You`
- `CopyForEachCanTarget$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.ControlledBy TriggeredActivator`, `Creature.YouCtrl`, `Golem.inZoneBattlefield`, `Permanent.inRealZoneBattlefield,Player`, `Permanent.IsRemembered`, `Permanent.nonLand+OppCtrl+!ControlledBy TriggeredSpellAbilityTargetsOrController`, `Spell,Permanent,Card,Player`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 T`, `2 U T`, `1 RW`, `1`, `3 T`, `R T`, `U U T`, `1 U T`, `2 U ExileFromGrave<1/CARDNAME>`, `XMin1 X X T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Parent`, `Remembered`, `Spawner>TriggeredSpellAbility`, `Targeted`, `TriggeredSourceSA`, `TriggeredSpellAbility`, `ValidStack Ability.YouCtrl+otherAbility`, `ValidStack Spell.YouCtrl`
- `DefinedTarget$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `OppNonTriggeredSpellAbilityTargetsOrController`, `Self`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IgnoreFreeze$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.powerGE3+Self`
- `MayChooseTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `NonLegendary$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Max speed —`
- `RememberCopies$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberNewCard$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SetColor$`: TODO: Describe this parameter.
  Observed values: `Red`
- `SetPower$`: TODO: Describe this parameter.
  Observed values: `1`
- `SetToughness$`: TODO: Describe this parameter.
  Observed values: `1`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBChangeTargets`, `DBCleanup`, `DBCopy`, `DBDraw`, `DBDrawAll`, `DBExile`, `DBPump`, `DBPutCounter`, `DBReturn`, `TrigCopyAbilities`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Activated,Triggered,Instant,Sorcery`, `Activated.YouCtrl,Triggered.YouCtrl`, `Spell`, `Spell.numTargets EQ1`, `SpellAbility.numTargets EQ1`, `Triggered.YouCtrl`
- `TargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `Permanent.inRealZoneBattlefield,Player`, `You`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `ChainOfVapor`, `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `2 U`, `CopyCost`, `Discard<1/Card>`, `R R`, `Sac<1/Land>`, `U U`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `TargetedController`, `TargetedOrController`, `TriggeredActivator`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `UseOriginalHost$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `creature spell you control`, `instant or sorcery spell you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.YouCtrl`, `Card`, `Card,Emblem`, `Card.Colorless,Emblem`, `Card.Instant+cmcLE4,Card.Sorcery+cmcLE4`, `Card.Legendary+Other+!IsCommander+YouCtrl`, `Card.YouCtrl`, `Card.YouCtrl+!wasCast`, `Creature.YouCtrl`, `Enchantment`, `Instant,Sorcery`, `Instant.YouCtrl+cmcEQX,Sorcery.YouCtrl+cmcEQX`, `Instant.YouCtrl+cmcLE2`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Permanent.YouCtrl`, `Sorcery.YouCtrl+cmcLE2`

## `Counter`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `MinCMC.3`, `MinCMC.4`, `Never`, `NullBrooch`
- `AIPhyrexianPayment$`: TODO: Describe this parameter.
  Observed values: `Never`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `!Creature`, `Card.Blue`, `Card.cmcGE2`, `Card.Red`, `Card.SharesColorWith Valid Creature.YouCtrl`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `SharesNameBattlefield`, `SharesNameGrave`, `T`, `TotalPresence`, `X`, `Y`, `YourPeerGroup`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`, `TriggeredCard`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `U`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.cmcEQX`, `Card.NamedCard`, `Card.sharesCardTypeWith TriggeredCard`, `Creature.YouCtrl+powerGE4`, `Spell.Blue`, `Spell.kicked`, `Spell.ManaSpent EQ0`, `Spell.Red`, `Spell.SharesColorWith Valid Creature.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQX`, `EQY`, `GE1`, `GTY`, `LEX`, `LEY`
- `ConditionWouldDestroy$`: TODO: Describe this parameter.
  Observed values: `Land.YouCtrl`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `U Sac<1/Permanent.Blue/blue permanent>`, `1 U Sac<1/NICKNAME>`, `3 U U`, `T`, `2 U`, `1 U U Sac<1/Creature>`, `1 G T`, `SubCounter<1/KI>`, `Sac<1/CARDNAME>`, `T Sac<1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{1}{U}{U}`, `{2}, Reveal X blue cards from your hand, Sacrifice CARDNAME:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`, `TriggeredSourceSA`, `TriggeredSpellAbility`, `ValidStack Activated,Triggered`, `ValidStack Activated.OppCtrl,Triggered.OppCtrl`, `ValidStack Spell.OppCtrl,Activated.OppCtrl,Triggered.OppCtrl`, `ValidStack Spell.Other`, `ValidStack Spell.sharesNameWith ExiledWithSource`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `BottomOfLibrary`, `Exile`, `Graveyard`, `Hand`, `TopOfLibrary`
- `DestinationChoice$`: TODO: Describe this parameter.
  Observed values: `BottomOfLibrary,TopOfLibrary`
- `DestroyPermanent$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.Snow+YouCtrl`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 U`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Cleave`, `Ultimate Sacrifice —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `RememberCountered$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberCounteredCMC$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberCounteredSA$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberForCounter$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberSplicedOntoCounteredSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAmass`, `DBAnimate`, `DBAssemble`, `DBBurn`, `DBCast`, `DBChange`, `DBChangeZone`, `DBClash`, `DBCleanup`, `DBCopy`, `DBCounter`, `DBCounterSamePermanent`, `DBDamage`, `DBDealDamage`, `DBDelTrig`, `DBDestroy`, `DBDig`, `DBDiscard`, `DBDisCard`, `DBDiscover`, `DBDraft`, `DBDrain`, `DBDraw`, `DBDread`, `DBEffect`, `DBEnergy`, `DBGainLife`, `DBIncubate`, `DBInvestigate`, `DBMill`, `DBPlay`, `DBProliferate`, `DBPutCounter`, `DBRandom`, `DBRearrange`, `DBReturn`, `DBReveal`, `DBSacrifice`, `DBScentOfBrineCleanup`, `DBScry`, `DBSeek`, `DBSurveil`, `DBSuspect`, `DBToken`, `DBTreasure`, `DBTreasureTokens`, `DBUntap`, `DBVenture`, `DelTrigSlowtrip`, `ExileYard`, `TapLands`, `TrigSurveil`, `TrigTempt`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `4`, `X`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`, `Y`
- `TargetsWithControllerProperty$`: TODO: Describe this parameter.
  Observed values: `cmcLECardsInGraveyard`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated,Triggered`, `Activated,Triggered,Spell.Legendary`, `Activated,Triggered,Spell.nonCreature`, `Activated.YouDontCtrl,Triggered.YouDontCtrl`, `Instant,Sorcery,Triggered`, `Spell`, `Spell,Activated,Triggered`, `Spell.Colorless,Triggered`, `Spell.Instant,Spell.Sorcery,Activated,Triggered`
- `TargetValidTargeting$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl+inRealZoneBattlefield,Creature.YouCtrl+inRealZoneBattlefield`, `Card.StrictlySelf`, `Creature.inRealZoneBattlefield`, `Creature.YouCtrl+inRealZoneBattlefield`, `Enchantment.inRealZoneBattlefield`, `Land.YouCtrl+inRealZoneBattlefield`, `Permanent.YouCtrl+inRealZoneBattlefield`, `Permanent.YouCtrl+inRealZoneBattlefield,You`, `Player`, `You`, `You,Creature.YouCtrl+inRealZoneBattlefield`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 PayLife<1>`, `2`, `3`, `4`, `6`, `B`, `DamageYou<4>`, `DefinedSACost_TriggeredSpellAbility`, `Discard<1/Card>`, `Discard<1/Hand>`, `Discard<3/Card>`, `ExileFromGrave<1/All>`, `LifeTotalHalfUp`, `N`, `PayLife<4>`, `PayLife<5>`, `Sac<1/Creature>`, `Sac<1/Land>`, `ScentOfBrineX`, `W`, `X`, `XX`, `Y`, `Z`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `NonTriggeredCardController`, `Player`, `RememberedController`, `TargetedController`, `ThisTargetedController`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredSourceSAController`, `TriggeredSpellAbilityController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `spell`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment,Land`, `Artifact,Creature,Planeswalker`, `Artifact,Enchantment`, `Card`, `Card,Emblem`, `Card.!wasCastFromTheirHand`, `Card.Black`, `Card.Blue`, `Card.cmcEQ1`, `Card.cmcEQ2`, `Card.cmcEQX`, `Card.cmcGE4`, `Card.cmcLE1`, `Card.cmcLE2`, `Card.cmcLE3`, `Card.cmcLE4`, `Card.cmcLE6+Red,Card.cmcLE6+Green`, `Card.cmcLEX`, `Card.Colorless`, `Card.Creature`, `Card.Green`, `Card.Green,Card.Red`, `Card.hasXCost`, `Card.MultiColor`, `Card.NamedCard`, `Card.nonArtifact`, `Card.nonBlue`, `Card.nonCreature`, `Card.nonCreature,Emblem`, `Card.nonFaerie`, `Card.OppCtrl`, `Card.Red`, `Card.Red,Card.Green`, `Card.SecondSpellCastThisTurn`, `Card.sharesNameWith ValidExile Card.ExiledWithSource`, `Card.Sorcery`, `Card.wasCastFromGraveyard`, `Card.White`, `Card.YouDontCtrl`, `Creature`, `Creature,Artifact`, `Creature,Artifact,Planeswalker`, `Creature,Aura`, `Creature,Battle`, `Creature,Enchantment`, `Creature,Planeswalker`, `Creature,Sorcery`, `Creature.cmcLE4`, `Creature.powerLE2,Creature.toughnessLE2`, `Enchantment`, `Enchantment,Instant,Sorcery`, `Instant`, `Instant,Aura`, `Instant,Sorcery`, `Instant.Blue`, `Instant.Red,Sorcery.Red`, `Permanent`, `Planeswalker`, `Sorcery`, `Spirit,Arcane`

## `DamageAll`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `X`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Attackers`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DmgAllCreaturesAndPlayers`
- `AIPhyrexianPayment$`: TODO: Describe this parameter.
  Observed values: `Never`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `X`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `AshlingNum`, `LandfallAmount`, `Resolved`, `TriggeredSpellAbility$CardPower`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `G`, `R`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Artifact`, `Creature`, `Creature.Demon`, `Creature.powerGE4+YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `EQ3`, `GE6`, `GE7`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Hand> Draw<2/You>`, `X G G Discard<1/NICKNAME>`, `1 R`, `2`, `1 R Sac<1/CARDNAME>`, `R Sac<1/CARDNAME>`, `R Sac<1/Card.AttachedBy/enchanted creature>`, `T`, `SubCounter<3/LOYALTY>`, `SubCounter<7/LOYALTY>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{2}, Reveal X red cards from your hand, Sacrifice CARDNAME:`
- `DamageSource$`: TODO: Describe this parameter.
  Observed values: `EffectSource`, `ParentTarget`, `Remembered`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredCard`, `TriggeredSource`, `TriggeredTargetLKICopy`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `5`
- `NumDmg$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `13`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `Count$TriggerRememberAmount`, `KeraliaX`, `Remembered$CardPower`, `SVar$Votes/Times.2`, `WasKicked`, `X`, `XX`, `Y`, `Z`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Fira`, `Firaga`, `Fire`, `Threshold —`
- `RememberDamaged$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceDyingDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddMana`, `DBAnimate`, `DBChoose`, `DBCleanup`, `DBDamage`, `DBDamageAll`, `DBDamageCreature`, `DBDamageResolve`, `DBDamageResolve6U`, `DBDestroyAll`, `DBDiscard`, `DBDraw`, `DBEffect`, `DBExile`, `DBForget`, `DBGainLife`, `DBGainOneLife`, `DBNoRegen`, `DBPump`, `DBPumpAll`, `DBRadiation`, `DBRepeat`, `DBReturn`, `DBSacLand`, `DBScry`, `DBSearch`, `DBTapAllDamaged`, `DBToken`, `DBTreasure`, `GPaid`, `OppCantBlock`, `ResetFlips`, `SucksToBeAlpha`, `ThunderTap`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Battle.OppProtect`, `Card.IsRemembered+withFlying`, `Creature`, `Creature,Planeswalker`, `Creature,Planeswalker,Battle`, `Creature,Planeswalker.nonBolas`, `Creature.!IsCommander+OppCtrl`, `Creature.!IsRemembered`, `Creature.!IsRemembered+ControlledBy TargetedController`, `Creature.!Outlaw`, `Creature.!ThisTurnEntered`, `Creature.!token`, `Creature.!TriggeredTarget+ControlledBy TriggeredTargetController`, `Creature.attacking`, `Creature.attacking+withoutFlying`, `Creature.attacking,Creature.blocking`, `Creature.blocked,Creature.blocking`, `Creature.blocking`, `Creature.blockingEquipped`, `Creature.blockingSource`, `Creature.Blue`, `Creature.ChosenColor`, `Creature.ControlledBy Spawner>TriggeredTarget,Planeswalker.ControlledBy Spawner>TriggeredTarget`, `Creature.ControlledBy TargetedOrController`, `Creature.ControlledBy TargetedPlayer`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.ControlledBy TriggeredTarget`, `Creature.DefenderCtrl`, `Creature.Goblin`, `Creature.Green`, `Creature.Human`, `Creature.IsRemembered`, `Creature.nonArmy`, `Creature.nonArtifact`, `Creature.nonBlack`, `Creature.nonBlue+withoutFlying`, `Creature.nonChosenCard`, `Creature.nonDragon`, `Creature.nonElemental`, `Creature.nonGiant`, `Creature.nonGiant,Planeswalker`, `Creature.nonLegendary`, `Creature.nonPirate`, `Creature.nonVampire`, `Creature.nonWall`, `Creature.nonWhite`, `Creature.NotDefinedTargeted`, `Creature.NotDefinedTargeted+ControlledBy TargetedController`, `Creature.NotDefinedTargeted+sharesCreatureTypeWith Targeted`, `Creature.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.Other`, `Creature.Other+withoutFlying`, `Creature.Outlaw`, `Creature.RememberedPlayerCtrl`, `Creature.StrictlyOther`, `Creature.tapped`, `Creature.TargetedPlayerCtrl`, `Creature.untapped`, `Creature.wasDealtDamageThisTurn`, `Creature.White`, `Creature.White+TargetedPlayerCtrl,Creature.Blue+TargetedPlayerCtrl`, `Creature.White,Creature.Blue`, `Creature.withFlying`, `Creature.withFlying+OppCtrl`, `Creature.withFlying+StrictlyOther`, `Creature.withHorsemanship`, `Creature.withoutFirst Strike+withoutDouble Strike+withoutVigilance+withoutHaste`, `Creature.withoutFlying`, `Creature.withoutFlying+ControlledBy TriggeredDefendingPlayer`, `Creature.withoutFlying+DefenderCtrl`, `Creature.withoutFlying+StrictlyOther`, `Creature.withoutFlying,Planeswalker`, `Creature.withoutHorsemanship`, `Creature.withShadow`, `Creature.YouCtrl`, `Creature.YouCtrl+StrictlyOther`, `Creature.YouCtrl+withoutFlying,Creature.YouDontCtrl`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl,Planeswalker.YouDontCtrl`, `Planeswalker`, `Planeswalker.OppCtrl`, `Planeswalker.wasDealtDamageByThisGame`, `Planeswalker.YouDontCtrl`, `Targeted.sameName+Other`, `Targeted.Self`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `each attacking creature.`, `each attacking or blocking creature target player controls.`, `each blocked and blocking creature.`, `each blocking creature`, `each creature`, `each creature and each opponent.`, `each creature and each planeswalker.`, `each creature and each player.`, `each creature and planeswalker.`, `each creature and with flying.`, `each creature and without flying.`, `each creature dealt damage this turn.`, `each creature defending player controls.`, `each creature except for creatures you control with flying.`, `each creature it blocked this combat.`, `each creature of the chosen color.`, `each creature target player controls`, `each creature target player controls.`, `each creature that doesn't have first strike, double strike, vigilance, or haste.`, `each creature that's white or blue that player controls.`, `each creature that's white or blue.`, `each creature the opponent controls.`, `each creature touched.`, `each creature with flying and each player.`, `each creature with flying if {R} was spent to cast it. (Do both if {R}{G} was spent.)`, `each creature with flying.`, `each creature with horsemanship and each player.`, `each creature with shadow.`, `each creature without flying`, `each creature without flying and each player.`, `each creature without flying if {R} was spent to cast it.`, `each creature without flying that player controls.`, `each creature without flying.`, `Each creature without flying.`, `each creature you control.`, `each creature you don't control.`, `each creature your opponents control`, `each creature your opponents control.`, `each creature.`, `each green creature.`, `each Human creature`, `each non-Army creature.`, `each non-Giant creature and each planeswalker.`, `each non-Giant creature.`, `each non-Pirate creature.`, `each non-Vampire creature.`, `each non-Wall creature.`, `each nonartifact creature and each player`, `each nonartifact creature target opponent controls.`, `each nonartifact creature.`, `each nonblack creature.`, `each noncommander creature your opponents control.`, `each nonlegendary creature.`, `each opponent and each creature and planeswalker they control.`, `each opponent and each creature they control`, `each opponent and each creature they control.`, `each opponent.`, `each other creature and each opponent.`, `each other creature and each player.`, `each other creature with flying.`, `each other creature with the same name as that creature.`, `each other creature without flying.`, `each other creature.`, `each player.`, `each tapped creature and each player.`, `each tapped creature target player controls.`, `each untapped creature.`, `target opponent and each creature they control.`, `target player and each creature and planeswalker they control.`, `target player and each creature that player controls.`
- `ValidPlayers$`: TODO: Describe this parameter.
  Observed values: `FlippedTails`, `OppNonTriggeredTarget`, `Opponent`, `Opponent.IsRemembered`, `Player`, `Player.controlsCreature.White_GE1`, `Player.Opponent`, `Player.Opponent+wasDealtDamageThisGameBy Self`, `Remembered`, `Targeted`, `TargetedController`, `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `Black`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `GrTo`

## `DamageResolve`

TODO: Write documentation.

**Parameters:**
- `RememberDamaged$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceDyingDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DB2`, `DBCleanup`, `DBDraw`, `DBMana`, `DBPump`

## `DayTime`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDiscard`, `DBPump`, `DBTransform`
- `Value$`: TODO: Describe this parameter.
  Observed values: `Day`, `Night`, `Switch`

## `DealDamage`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Desert`, `Hellbent`, `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Attackers`, `EndCombat`, `Upkeep`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AIExpectAmount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AssumeAtLeastOneTarget`, `Burn`, `BurnCreatures`, `DiscardCMCX`, `DiscardLands`, `Good`, `MadSarkhanDigDmg`, `NinThePainArtist`, `OppAtTenLife`, `OpponentGainLife`, `PingAfterAttack`, `Polukranos`, `PowerAtLeast.4`, `PowerDmg`, `ProcRaid.6`, `SelfDamage`, `Triskelion`, `WildHunt`, `XLifeDrain`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `R`
- `AIPhyrexianPayment$`: TODO: Describe this parameter.
  Observed values: `OnFatalDamage.1`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `BetterThanSource`, `Creature.White,Creature.Blue`, `Creature.White,Creature.Blue,Planeswalker.White,Planeswalker.Blue`, `Spirit.OppCtrl`
- `AlternateCost$`: TODO: Describe this parameter.
  Observed values: `R T`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `Exiled`, `Tapped`, `X`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many black cards to exile`, `how many creatures to tap`
- `AnnounceType$`: TODO: Describe this parameter.
  Observed values: `ChooseNumber`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CardChoices$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Morbid`, `X`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`, `Kicked 1`, `Threshold`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `AntagonismX`, `Bargain`, `ClockworkX`, `Count$Presence_Dragon.1.0`, `ElectrostaticCheck`, `FoundMountain`, `IsDestroyed`, `RaidTest`, `Result`, `TrigCount`, `TriggeredSpellAbility$CardManaCostLKI`, `Win`, `Wins`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQY`, `GE1`, `GE2`, `GE3`, `GE5`, `LT2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `Remembered`, `RememberedLKI`, `ReplacedSource`, `Sacrificed`, `Self`, `Targeted`, `TriggeredCardLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If CARDNAME was kicked,`, `If it was kicked,`, `If that land is nonbasic,`, `If that land was a snow land,`, `If this spell was kicked,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `R`
- `ConditionOpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.YouCtrl`, `Card`, `Card.Creature`, `Card.EnchantedBy+!attackedThisTurn`, `Card.Island`, `Card.NamedCard`, `Card.namedStomping Slabs`, `Card.nonCreature`, `Card.nonLand`, `Card.Red`, `Card.RedSource`, `Card.Self+!firstTurnControlled`, `Card.Self+PromisedGift`, `Card.sharesCardTypeWith ValidExile Card.ExiledWithSource`, `Creature`, `Creature.nonWizard`, `Creature.targetedBy+attacking`, `Creature.White`, `Creature.withInfect`, `Creature.Wizard`, `Creature.YouCtrl+modified`, `Dragon.YouCtrl`, `Enchantment`, `Equipment.YouCtrl`, `Forest`, `Giant`, `Instant.YouOwn,Sorcery.YouOwn`, `Island`, `Land`, `Land.Basic`, `Land.Basic+ControlledBy TriggeredPlayer`, `Land.Snow`, `Mountain.YouCtrl+!TriggeredCard`, `Ogre.YouCtrl`, `Permanent.Black+YouCtrl`, `Permanent.IsCommander+ControlledBy TriggeredPlayer`, `Permanent.Red+YouCtrl+Other`, `Spirit`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ10`, `EQ2`, `EQY`, `GE1`, `GE10`, `GE2`, `GE3`, `GE4`, `GE5`, `GE7`, `GE8`, `GT0`, `GT4`, `LE0`, `LT1`, `LT2`, `LT3`, `LT7`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 R Discard<1/Random>`, `2 Sac<1/CARDNAME>`, `1 T`, `1 T Sac<1/CARDNAME>`, `Sac<1/CARDNAME>`, `PayLife<50>`, `T PayEnergy<2>`, `T PayEnergy<8>`, `1 R Sac<1/Creature.Goblin/Goblin creature>`, `SubCounter<2/LOYALTY>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, choose a number between 0 and 5.`, `As an additional cost to cast this spell, exile a creature card from your graveyard.`, `As an additional cost to cast this spell, sacrifice all creatures you control.`, `As an additional cost to cast this spell, tap any number of untapped creatures you control.`, `Grandeur — Discard another card named Skoa, Embermage, Sacrifice two Mountains:`, `Sacrifice CARDNAME and any number of creatures you control:`, `Tap enchanted creature:`, `{1}{B}{B}`, `{3}, {T}, Sacrifice a creature of the chosen type:`, `{X}{R}{W}`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `4`
- `DamageMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `DamageSource$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `EffectSource`, `Enchanted`, `Imprinted`, `OriginalHost`, `ParentTarget`, `Remembered`, `Self`, `Spawner>TriggeredCardLKICopy`, `Targeted`, `ThisTargetedCard`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredSource`, `TriggeredTarget`, `TriggeredTargetLKICopy`, `Valid Artifact.Creature+YouCtrl`, `Valid Aura.AttachedTo Creature`, `Valid Card.IsCommander+YouCtrl`, `Valid Enchantment`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttackingPlayer`, `CardController`, `ChoosingPlayer`, `ChosenCard`, `ChosenCardController`, `ChosenPlayer`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `Enchanted`, `EnchantedController`, `EnchantedOwner`, `EnchantedPlayer`, `ImprintedController`, `OppNonParentTarget`, `Opponent`, `Opponent.NotedForSilence`, `ParentTarget`, `ParentTargetedController`, `Player`, `Player.!MaxSpeed`, `Player.attackedBySourceThisCombat`, `Player.Chosen`, `Player.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Player.Opponent+IsRemembered`, `Player.Other`, `Remembered`, `RememberedController`, `ReplacedCard`, `ReplacedSource`, `ReplacedSourceController`, `Self`, `ShieldEffectTarget`, `Targeted`, `TargetedController`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredAttackedTarget`, `TriggeredAttackerController`, `TriggeredAttackerLKICopy`, `TriggeredAttackers`, `TriggeredAttackingPlayer`, `TriggeredBlockerController`, `TriggeredBlockerLKICopy`, `TriggeredBlockers`, `TriggeredCardController`, `TriggeredCardLKICopy`, `TriggeredCardOwner`, `TriggeredDefender`, `TriggeredDefender.Opponent & Valid Planeswalker.TriggeredDefender`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredSourceLKICopy`, `TriggeredSourceSAController`, `TriggeredTarget`, `TriggeredTargetController`, `Valid Card.EnchantedBy`, `You`, `You.CardsInHandAtBeginningOfTurn`
- `Description$`: TODO: Describe this parameter.
- `DividedAsYouChoose$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `CoreStrength`, `Count$CardPower`, `DistroDmg`, `FirePower`, `MonstrosityX`, `NumCreatures`, `OrigMountains`, `OrigPower`, `TriggerObjectsAttackers$Amount`, `X`, `Y`, `Z`
- `DivideEvenly$`: TODO: Describe this parameter.
  Observed values: `RoundedDown`
- `DividerOnResolution$`: TODO: Describe this parameter.
  Observed values: `ParentTargetedController`
- `ExcessDamage$`: TODO: Describe this parameter.
  Observed values: `TargetedController`, `ThisTargetedController`
- `ExcessDamageCondition$`: TODO: Describe this parameter.
  Observed values: `Card.withTrample`
- `ExcessSVar$`: TODO: Describe this parameter.
  Observed values: `Excess`, `X`
- `ExcessSVarCondition$`: TODO: Describe this parameter.
  Observed values: `Card.targetedBy`, `Creature`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.powerGE4+Self`, `Card.Self`, `Card.Self+!firstTurnControlled`, `Card.Self+attacking`, `Card.Self+attacking,Card.Self+blocking`, `Card.Self+counters_GE1_P1P1`
- `Max$`: TODO: Describe this parameter.
  Observed values: `5`
- `Min$`: TODO: Describe this parameter.
  Observed values: `0`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `2`, `3`, `5 R`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoPrevention$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoRedirection$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumDmg$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `100`, `12`, `13`, `15`, `2`, `20`, `3`, `4`, `5`, `50`, `6`, `7`, `8`, `9`, `AngelDamage`, `ArcheryX`, `ArlinnX`, `Backlash`, `BlazeSize`, `BrawlX`, `BurningAngerDmg`, `CommandoRaidX`, `CoreStrength`, `Count$CardCounters.TIME`, `Count$CardPower`, `Count$CastSinceBeginningOfYourLastTurn_Card.nonCreature+YouCtrl`, `Count$ChosenNumber`, `Count$TriggerRememberAmount`, `Count$Valid Creature.YouCtrl`, `Count$Valid Swamp.YouCtrl`, `D`, `Damage`, `DistroDmg`, `DmgX`, `DoubleX`, `FarrelX`, `FirePower`, `FlameX`, `FleshReaverX`, `GruesomeX`, `GuerrillasX`, `HalfXDown`, `HalfXUp`, `HankyuX`, `HeartlessX`, `HereticX`, `Imprinted$Amount`, `MangaraX`, `MonstrosityX`, `MountainsYouControl`, `MyX`, `NumAllies`, `NumCreatures`, `NumDragons`, `OrigMountains`, `OrigPower`, `ParentTargeted$CardPower`, `PredatoryX`, `PredatoryY`, `PreventedDamage`, `R`, `Remembered$Amount`, `Remembered$CardManaCost`, `Result`, `RigX`, `ScentOfCinderX`, `SearingX`, `SinstrikerCount`, `SpitefulX`, `SurestrikeTridentX`, `TheirX`, `TriggerCount$Amount`, `TriggeredAttacker$CardPower`, `TriggerObjectsAttackers$Amount`, `VengefulRebirthX`, `WasKicked`, `X`, `XPlus`, `XPower`, `XX`, `Y`, `Z`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `ParentTargetedController`, `TargetedController`, `You`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`, `true`
- `PlayerChoices$`: TODO: Describe this parameter.
  Observed values: `Player`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Blow Up —`, `Channel —`, `Chroma —`, `Cleave`, `Cohort —`, `Hadoken —`, `Hellbent —`, `Radiance —`, `Rope Dart —`, `Scorching Ray —`, `The Most Important Punch in History —`, `Threshold —`, `Throw . . . —`, `Thundaga`, `Thundara`, `Thunder`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RelativeTarget$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDamaged$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRandomChoice$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRedirectedExcess$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `Remove$`: TODO: Describe this parameter.
  Observed values: `All`
- `ReplaceDyingCondition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ReplaceDyingDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Remembered.Creature`, `Targeted`, `ThisTargetedCard.Creature`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Imprinted`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Animate`, `BombGainCtrl`, `BoomerangCatch`, `CantBlockEffect`, `ChandraDamage`, `ChompEquip`, `Clean`, `ControlFlip`, `CowedByAurelia`, `CreatureDmg`, `DamageEffectPlayer`, `DamageNonCreature`, `DamageOpponents`, `DamageSame`, `DamageThis`, `DB1`, `DBAmass`, `DBAnimate`, `DBAnimateAll`, `DBAttach`, `DBAuraDmg`, `DBBlood`, `DBBoon`, `DBBottom`, `DBBounce`, `DBBranch`, `DBCantBlock`, `DBChandraCleanup`, `DBChange`, `DBChangeZone`, `DBChoose`, `DBChooseCard`, `DBCinderCleanup`, `DBClash`, `DBCleanup`, `DBCleanup2`, `DBCleanupBis`, `DBClockworkCleanup`, `DBColor`, `DBColorlessMana`, `DBConvert`, `DBCopy1`, `DBCounter`, `DBCurseArtifactCleanup`, `DBDamage`, `DBDamage2`, `DBDamageAll`, `DBDamageAtk`, `DBDamageBlk`, `DBDamageChosen`, `DBDamageController`, `DBDamageCreature`, `DBDamagePlayer`, `DBDamageResolve`, `DBDamageSelf`, `DBDamageThree`, `DBDamageTwo`, `DBDamageYou`, `DBDealDamage`, `DBDealDamage2`, `DBDealDamageSelf`, `DBDebuff`, `DBDelayedTrigger`, `DBDelayTrig`, `DBDelayTrigger`, `DBDes`, `DBDestroy`, `DBDestroyAll`, `DBDig`, `DBDiscard`, `DBDiscard1U`, `DBDiscardDraw`, `DBDiscardOpp`, `DBDiscover`, `DBDmg`, `DBDmgAll`, `DBDoubleBelch`, `DBDrain`, `DBDraw`, `DBDrawSeven`, `DBEffect`, `DBElderSpawnCleanup`, `DBExile`, `DBFood`, `DBGain`, `DBGain1Life`, `DBGain3Life`, `DBGainFourLife`, `DBGainLife`, `DBGainLife2`, `DBGainLife3M`, `DBGainLifeC`, `DBGiantDamage`, `DBGoad`, `DBHereticCleanup`, `DBImmediateTrigger`, `DBIntensify`, `DBInvestigate`, `DBLearn`, `DBLoseFlying`, `DBMana`, `DBNoBlock`, `DBNoCombatDamage`, `DBNoRegen`, `DBPlay`, `DBPoison`, `DBProliferate`, `DBPump`, `DBPumpAll`, `DBPumpCurse`, `DBPutCounter`, `DBRemoveCounters`, `DBRepeat`, `DBReset`, `DBRoll`, `DBRollDice`, `DBSac`, `DBScentOfCinderCleanup`, `DBScry`, `DBSearch`, `DBShuffle`, `DBStayTapped`, `DBSurveil`, `DBTap`, `DBTapLand`, `DBToken`, `DBTokenForest`, `DBTransform`, `DBTreasure`, `DBUltimateEmblem`, `DBUntapAll`, `DBVengefulRebirthExile`, `DBWandDmg`, `DBYouGainLife`, `DelTrigSlowtrip`, `DmgAll`, `DmgAll6U`, `DmgController`, `DmgResolve`, `DmgYou`, `DrawNine`, `DrawYou`, `EffDraw`, `ExileEffect`, `ExileYard`, `GainLife`, `GigantotheriumFight`, `HammerCatch`, `Justice`, `Kicked`, `KickingLava`, `LavabellyGainLife`, `MoreDamage`, `PathwayTapAll`, `PreventHealing`, `QuicksilverDraw`, `ReheatTheForge`, `Retribution`, `ReturnDmg`, `SearingDamage`, `ShurikenGainCtrl`, `SquirrelToken`, `TapWolves`, `TrigDamage2`, `TrigDamage3`, `TrigDraw`, `TrigTempt`, `Unpoison`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.Opponent`, `TriggeredCardController`, `TriggeredPlayer`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `6`, `8`, `CoreStrength`, `Count$CardPower`, `FirePower`, `MaxTargets`, `MaxTgts`, `NumCreatures`, `OneEach`, `OrigMountains`, `OrigPower`, `TargetsNum`, `TriggerObjectsAttackers$Amount`, `X`, `Y`, `Z`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `TargetsNum`, `X`, `Y`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `ParentTargetedController`, `TriggeredDefendingPlayer`, `TriggeredTarget`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `AddCounter<1/M1M1/Creature.YouCtrl/a creature you control>`, `B`, `B B`, `DamageYou<2>`, `DamageYou<4>`, `DamageYou<5>`, `DamageYou<X>`, `Discard<1/Card>`, `ExileFromGrave<1/Card>`, `G G G G`, `PayEnergy<X>`, `Sac<1/CARDNAME>`, `Sac<1/Creature.!EnchantedBy>`, `Sac<1/Creature.!token/a nontoken creature>`, `Sac<1/Creature.Other/a creature other than CARDNAME>`, `Sac<1/Creature>`, `Sac<1/Permanent.nonLand+targetedBy/targeted nonland permanent>`, `Sac<1/Permanent.nonLand>`, `Sac<1/Permanent>`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `EnchantedController`, `ImprintedController`, `Remembered`, `Targeted`, `TargetedController`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredPlayer`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Ability.IsTargeting Player.hasMoreLife`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `creature an opponent controls`, `creature or planeswalker`, `creature with flying.`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`, `Any.!Dinosaur`, `Any.!Dragon`, `Any.!IsCommander`, `Any.NotDefinedParentTarget,Player`, `Battle.Other,Opponent`, `Creature`, `Creature,Planeswalker`, `Creature,Planeswalker,Battle`, `Creature,Player`, `Creature.!EnchantedBy,Player,Planeswalker.!EnchantedBy,Battle.!EnchantedBy`, `Creature.!TriggeredAttacker`, `Creature.!TriggeredTarget,Player,Planeswalker.!TriggeredTarget`, `Creature.Artifact`, `Creature.attacking`, `Creature.attacking+OppCtrl,Creature.blocking+OppCtrl`, `Creature.attacking+withFlying`, `Creature.attacking+withFlying,Creature.blocking+withFlying`, `Creature.attacking+withoutFlying`, `Creature.attacking+withoutFlying,Creature.blocking+withoutFlying`, `Creature.attacking,Creature.blocking`, `Creature.attacking,Creature.blocking,Creature.tapped`, `Creature.blockedBySource`, `Creature.blockedBySourceLKI`, `Creature.blockedThisTurn`, `Creature.blocking`, `Creature.blockingSelf`, `Creature.blockingSource`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.Blue`, `Creature.Blue,Creature.White`, `Creature.ControlledBy ParentTargetedController,Creature.ControlledBy ParentTarget`, `Creature.ControlledBy TargetedOrController`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.ControlledBy TriggeredTarget`, `Creature.DefenderCtrl`, `Creature.Human`, `Creature.nonBlack`, `Creature.nonDragon+OppCtrl`, `Creature.nonElemental`, `Creature.nonRed`, `Creature.nonSpirit`, `Creature.nonWhite`, `Creature.OppCtrl`, `Creature.OppCtrl+wasDealtDamageThisTurn`, `Creature.OppCtrl+withFlying`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl,Opponent`, `Creature.Other`, `Creature.Other,Planeswalker.Other`, `Creature.Other,Player,Planeswalker.Other,Battle.Other`, `Creature.Red,Planeswalker.Red`, `Creature.Spirit`, `Creature.tapped`, `Creature.tapped+OppCtrl`, `Creature.token`, `Creature.token,Player,Planeswalker`, `Creature.Treefolk`, `Creature.wasDealtDamageThisTurn`, `Creature.wasDealtDamageThisTurn,Player.wasDealtDamageThisTurn`, `Creature.Werewolf`, `Creature.White`, `Creature.White,Creature.Blue`, `Creature.White,Planeswalker.White,Creature.Blue,Planeswalker.Blue`, `Creature.withFlying`, `Creature.withoutFlying`, `Creature.withoutFlying+attackingYou`, `Creature.withoutFlying+YouDontCtrl`, `Creature.Wizard`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl,Planeswalker.YouDontCtrl`, `Opponent`, `Opponent,Battle`, `Opponent,Creature.OppCtrl,Planeswalker.OppCtrl`, `Opponent,Planeswalker`, `Opponent,Planeswalker,Battle`, `Opponent.wasDealtDamageThisGameBy Self`, `Planeswalker`, `Planeswalker,Player`, `Planeswalker.ControlledBy TriggeredTarget`, `Planeswalker.ControlledBy TriggeredTarget,Battle.ProtectedBy TriggeredTarget`, `Player`, `Player, Planeswalker`, `Player,Battle`, `Player,Planeswalker`, `Player.!TriggeredActivator`, `Player.attackedWithCreaturesThisTurn`, `Player.Opponent`, `Player.Opponent,Card.Planeswalker`, `Player.Opponent,Planeswalker`, `Player.OpponentToActive+hasMoreLifeThanActive`, `Spirit.attacking,Spirit.blocking`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `attacking or blocking creature`, `creature an opponent controls`
- `XAnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `mana value of Equipment to unattach`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `Black`, `Red`

## `Debuff`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AllSuffixKeywords$`: TODO: Describe this parameter.
  Observed values: `walk`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 S`, `Sac<1/CARDNAME>`, `G`, `3`, `2`, `4`, `T`, `1`, `0`, `2 T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered.Creature`, `Self`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`, `UntilYourNextTurn`
- `Keywords$`: TODO: Describe this parameter.
  Observed values: `Banding & Bands with other`, `Bands with other`, `Defender`, `First Strike`, `Flanking`, `Flying`, `Hexproof`, `Indestructible`, `Landwalk:Forest`, `Landwalk:Swamp`, `Prevent all damage that would be dealt to CARDNAME.`, `Protection from black`, `Shadow`, `Trample`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBCleanup`, `DBDamage`, `DBDraw`, `DBFlight`, `DBGainFly`, `DBGainFs`, `DBGainShdw`, `DBGainTrpl`, `DBPump`, `Flight`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.withFirst Strike`, `Creature.withFlying`, `Creature.withShadow`, `Creature.withTrample`

## `DelayedTrigger`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `NarsetRebound`, `SaveCreature`, `SpellCopy`
- `AttackingPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `RaidTest`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedLKI`, `Targeted`, `TriggeredCardLKICopy`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self+PromisedGift`, `Creature`, `Vehicle`, `Wizard.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<3/CHARGE>`, `T`, `SubCounter<2/LOYALTY>`, `2`, `G Sac<1/CARDNAME>`, `5`, `AddCounter<2/LOYALTY>`, `Exile<1/NICKNAME>`, `SubCounter<2/OIL>`, `U T`
- `DelayedTriggerDefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `You`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Any`, `Battlefield`, `Graveyard`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `Abandon`, `AddMana`, `AddRebound`, `BounceCritter`, `ChooseB`, `ChooseOpp`, `DBAddTurn`, `DBChange`, `DBChangeZone`, `DBDig`, `DBDiscard`, `DBDraw`, `DBDread`, `DBEffect`, `DBLoseLife`, `DBMassReveal`, `DBPutCounter`, `DBPutCounters`, `DBReturn`, `DBSurveil`, `DBToken`, `DBUntapAll`, `DestroySource`, `Discard`, `DiscardEach`, `DrawSlowThree`, `DrawSlowtrip`, `DrawTwo`, `EffTrigCopy`, `EffTrigCopy1`, `EffTrigCopy2`, `EndlessReturn`, `GBReturn`, `GrantHaste`, `MischiefReturn`, `MoveBack`, `MoveToPlay`, `MoveToYard`, `ObzedatReturn`, `ReturnAll`, `RuneswordSac`, `TrigAddAPI`, `TrigAddCounter`, `TrigAddMana`, `TrigAnimate`, `TrigBack`, `TrigBounce`, `TrigBranch`, `TrigChange`, `TrigChangeAll`, `TrigChangeZone`, `TrigChoose`, `TrigChooseLand`, `TrigConditionEffect`, `TrigConjure`, `TrigConvert`, `TrigCopy`, `TrigDamage`, `TrigDealDamage`, `TrigDestroy`, `TrigDestroy1`, `TrigDestroyAll`, `TrigDestroyBlocked`, `TrigDestroyBlocker`, `TrigDestroySimic`, `TrigDiscard`, `TrigDiscardExiled`, `TrigDmg`, `TrigDraw`, `TrigEarthbend`, `TrigEffect`, `TrigExile`, `TrigExileAll`, `TrigFight`, `TrigFlip`, `TrigGainControl`, `TrigGainLife`, `TrigGhostReturn`, `TrigGrave`, `TrigGrowth`, `TrigLifelineReturn`, `TrigLoseGame`, `TrigPhase`, `TrigPoison`, `TrigPopulate`, `TrigPump`, `TrigPureReturn`, `TrigPutCounter`, `TrigRem`, `TrigRemember`, `TrigRemoveCounter`, `TrigReturn`, `TrigReturnSak`, `TrigSac`, `TrigSacBlocker`, `TrigSacrifice`, `TrigTap`, `TrigToken`, `TrigTokens`, `TrigTransform`, `TrigUnattach`, `TrigUntap`, `VenomousBreathTrigDestroy`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.IsTriggerRemembered`, `Card.IsTriggerRemembered+AttachedTo Creature.YouCtrl`, `Card.StrictlySelf`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `AbilityCast`, `AttackersDeclared`, `ChangesController`, `ChangesZone`, `DamageDone`, `Phase`, `SpellAbilityCast`, `SpellCast`
- `NextTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Any`, `Battlefield`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `BeginCombat`, `Cleanup`, `Declare Attackers`, `End of Turn`, `End Of Turn`, `EndCombat`, `Main1`, `Main1,Main2`, `Main2`, `Upkeep`, `Upkeep->`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Hand`
- `RememberNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ChosenPlayer`, `Imprinted`, `ImprintedLKI`, `ParentTarget`, `Remembered`, `Remembered & ExiledCards`, `RememberedController`, `RememberedLKI`, `ReplacedCard`, `Self`, `Self & Targeted`, `Spawner>TriggeredAttacker`, `Spawner>TriggeredBlocker`, `Targeted`, `Targeted & SacrificedCards`, `Targeted.Creature`, `Targeted.YouDontCtrl`, `TargetedOwner & ChosenPlayer`, `TargetedOwner & RememberedLKI`, `TargetedPlayer & Self`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredFighterLKICopy`, `TriggeredNewCardLKICopy`, `TriggeredNewCardLKICopy & TriggeredCardOwner`, `TriggeredTargetLKICopy`, `Valid Creature.ActivePlayerCtrl+nonWall`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `Stackable$`: TODO: Describe this parameter.
  Observed values: `False`
- `StackDescription$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCleanup1`, `DBCleanup2`, `DBClone`, `DBDamageAll`, `DBDraw`, `DBEffect`, `DBExile`, `DBFight`, `DelTrigDrawTwo`, `ExileSelf`, `RuneswordEffect`, `TrigDelay2`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ThisTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `TriggerDescription$`: TODO: Describe this parameter.
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `UpcomingTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidActivatingPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.IsTriggerRemembered`, `Card.IsTriggerRemembered+counters_GE1_EGG`, `Card.IsTriggerRemembered+YouCtrl`, `Card.Self`, `Card.StrictlySelf`, `Creature`, `Instant,Sorcery`, `Instant.cmcLE2,Sorcery.cmcLE2`, `Instant.cmcLE3,Sorcery.cmcLE3`, `Instant.cmcLE4,Sorcery.cmcLE4`, `Instant.wasCastFromYourHand,Sorcery.wasCastFromYourHand`, `Lesson`, `Wolf,Werewolf`
- `ValidOriginalController$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.CardOwner`, `Player.controlsCard.IsTriggerRemembered`, `Player.IsTriggerRemembered`, `You`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Activated.Exhaust+!ManaAbility`, `Activated.Loyalty`, `Spell.Instant,Spell.Sorcery,Activated.Loyalty`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Card.IsTriggerRemembered`
- `ValidTarget$`: TODO: Describe this parameter.
  Observed values: `Player`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other,Artifact.Other`, `Creature.YouOwn`, `Opponent`, `Player`

## `Destroy`

TODO: Write documentation.

**Parameters:**
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Attackers`, `Upkeep`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.Opponent`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AssumeAtLeastOneTarget`, `AtEOTIfNotAttacking`, `AtOpponentsCombatOrAfter`, `GhostQuarter`, `LandForLand`, `MinLoyalty.4`, `OppDestroyYours`, `Pactivator`, `Polymorph`, `Pongify`, `WillSkipTurn`
- `AIMaxTgtsCount$`: TODO: Describe this parameter.
  Observed values: `Valid Creature.YouCtrl+cmcLE2`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.cmcLEX`, `BetterThanEvalRating.130`, `BetterThanSource`, `Card.Blue`, `Card.cmcGE4`, `Card.cmcLTX`, `Card.leastPower`, `Card.Red`, `Card.toughnessLTY`, `Card.White`, `Creature.cmcLEX`, `Creature.OppCtrl+powerLE0`, `Creature.SharesColorWith MostProminentColor`, `Land.nonBasic`, `Permanent.nonLand,Land.nonBasic`
- `AlwaysRemember$`: TODO: Describe this parameter.
  Observed values: `True`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `AdditionalCostPayTimesR,AdditionalCostPayTimesG`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many times to pay the additional cost`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Hellbent`, `Threshold`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `RememberedCMC`, `TgtPow`, `WinnowCheck`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `DelayTriggerRemembered`, `OriginalHost`, `ParentTarget`, `Remembered`, `Self`, `Targeted`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If this spell was bargained,`, `If you control a black permanent,`
- `ConditionManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `G W`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `G W`
- `ConditionNoDifferentColors$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Card`, `Card.attackedThisTurn`, `Card.Black,Card.Red`, `Card.Blue`, `Card.counters_EQ0_TASK`, `Card.counters_GE5_HUNGER`, `Card.Land`, `Card.Red`, `Creature`, `Creature.!attackedThisTurn`, `Creature.cmcLEX`, `Creature.greatestPower`, `Creature.leastPower`, `Creature.tapped`, `Creature.Werewolf`, `Creature.White`, `Cyclops`, `Permanent.Black+YouCtrl`, `Swamp.YouCtrl`
- `ConditionPresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQX`, `GE2`, `GE3`, `GEX`, `LEX`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T Sac<1/CARDNAME>`, `PayLife<4>`, `7 T`, `Sac<1/CARDNAME>`, `W Sac<1/Enchantment>`, `3 T Sac<1/CARDNAME>`, `T Sac<1/Land>`, `B T tapXType<X/Knight>`, `G G T`, `B Sac<1/Creature>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, discard X land cards.`, `As an additional cost to cast this spell, sacrifice X creatures.`, `This spell costs 3 life more to cast for each target.`, `{2}{G}, Pay 3 life for each velocity counter on CARDNAME:`, `{5}{W}`, `{B}{B}, Pay half your life, rounded up:`, `{T}, Exile two cards from your graveyard and CARDNAME:`, `{T}, Tap three untapped white creatures you control:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttachedBy TriggeredCardLKICopy`, `ChosenCard`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `Enchanted`, `Imprinted`, `OriginalHost`, `ParentTarget`, `Remembered`, `RememberedLKI`, `ReplacedTarget`, `Self`, `Spawner>TriggeredAttackerLKICopy`, `Spawner>TriggeredBlockerLKICopy`, `Targeted`, `Targeted.powerLE0`, `ThisTargetedCard`, `TriggeredAttackerLKICopy`, `TriggeredAttackerLKICopy & Self`, `TriggeredBlockerLKICopy`, `TriggeredCardLKICopy`, `TriggeredObjectLKICopy`, `TriggeredSourceLKICopy`, `TriggeredTargetLKICopy`, `Valid Card.EquippedByEnchanted`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ForgetOtherTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Artifact+YouCtrl`, `Vampire.YouCtrl`
- `MaxTotalTargetCMC$`: TODO: Describe this parameter.
  Observed values: `X`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `2 B`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoRegen$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Blade Beam`, `Channel —`, `Cleave`, `Cross-Slash`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberDestroyed$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberLKI$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `BeserkParoxysm`, `CantBlockEffect`, `ChooserDraws`, `DBAddLoyalty`, `DBAssemble`, `DBAttach`, `DBBolster`, `DBBoon`, `DBChange`, `DBChangeZone`, `DBChangeZoneAll`, `DBChangeZoneAll11U`, `DBChoose`, `DBClash`, `DBCleanup`, `DBCleanUp`, `DBConjure`, `DBConnive`, `DBCopy`, `DBCounter`, `DBDamage`, `DBDamageAll`, `DBDamageController`, `DBDealDamage`, `DBDealDamageYou`, `DBDealTwoDamage`, `DBDebuff`, `DBDelTrig`, `DBDelTrigAttacker`, `DBDelTrigBlocker`, `DBDestroy`, `DBDestroy2`, `DBDestroy3`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDmg`, `DBDrain`, `DBDraw`, `DBDread`, `DBEffect`, `DBExile`, `DBExileHand`, `DBFood`, `DBGainLife`, `DBGainLife4M`, `DBGainLife8`, `DBGainLifeBlocked`, `DBGainLifeBlocker`, `DBGiveFood`, `DBGoblin`, `DBIncubate`, `DBInvestigate`, `DBLifeGain`, `DBLoseLife`, `DBMana`, `DBMill`, `DBNoCombatDamage`, `DBPain`, `DBPoison`, `DBProliferate`, `DBPump`, `DBPutCounter`, `DBPutLoyalty`, `DBRancidDamage`, `DBRepeat`, `DBReturn`, `DBSacrifice`, `DBScry`, `DBSearch`, `DBSkipTurn`, `DBSpirit`, `DBSurveil`, `DBTapAttacker`, `DBTapBlocker`, `DBToken`, `DBTransform`, `DBTreasure`, `DBUntap`, `DBUntapSelf`, `DelTrigSlowtrip`, `DestroyArtifact`, `DestroyOtherAll`, `ExileEffect`, `GetForests`, `GhostToken`, `MakeToken`, `MakeTokens`, `NaturalLife`, `OxToken`, `PumpAll`, `ShadowRevealCards`, `StealEquip`, `TrigControl`, `TrigPutCounter`, `TrigTempt`, `TrigToken`, `TuktukDamage`, `Velocity`, `WeakenOther`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`, `TriggeredPlayer`, `TriggeredTarget`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `6`, `AdditionalCostPayTimesG`, `AdditionalCostPayTimesR`, `AmountToChoose`, `Count$Valid Creature`, `MaxPayLifeLimit`, `MaxTargets`, `MaxTgt`, `MaxTgts`, `OneEach`, `X`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `6`, `AdditionalCostPayTimesG`, `AdditionalCostPayTimesR`, `X`, `Y`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithControllerProperty$`: TODO: Describe this parameter.
  Observed values: `cmcLECardsInGraveyard`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `TriggeredCauser`, `TriggeredDefendingPlayer`, `TriggeredSourceController`, `TriggeredTarget`
- `TargetsWithDifferentCMC$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDifferentControllers$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithEqualToughness$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `3 B B B`, `DamageYou<2>`, `DamageYou<5>`, `DamageYou<6>`, `DamageYou<X>`, `MusicX`, `PayLife<1>`, `PayLife<2>`, `PayLife<X>`, `Sac<1/Artifact>`, `Sac<2/Island>`, `Sac<2/Permanent.Land/two lands>`, `U`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `Remembered`, `RememberedController`, `TargetedController`, `TriggeredPlayer`, `TriggeredTargetController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `artifact or enchantment`, `artifact or enchantment with mana value X or less`, `creature or planeswalker`, `creature with power 3 or greater`, `nonbasic land`, `nonland permanent`, `nonland permanent with mana value 2 or less`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Angel`, `Artifact`, `Artifact,Battle,Enchantment,Creature.withFlying`, `Artifact,Creature`, `Artifact,Creature,Enchantment`, `Artifact,Creature,Land`, `Artifact,Creature,Planeswalker`, `Artifact,Creature.tapped`, `Artifact,Enchantment`, `Artifact,Enchantment,Creature.tapped`, `Artifact,Enchantment,Creature.withFlying`, `Artifact,Enchantment,Land`, `Artifact,Enchantment,Planeswalker`, `Artifact,Land`, `Artifact,Planeswalker`, `Artifact.!hasManaAbility`, `Artifact.cmcEQX`, `Artifact.cmcEQX,Creature.cmcEQX`, `Artifact.cmcEQX,Enchantment.cmcEQX`, `Artifact.cmcLE3`, `Artifact.cmcLE3,Enchantment.cmcLE3`, `Artifact.cmcLE4,Enchantment.cmcLE4`, `Artifact.cmcLEX,Enchantment.cmcLEX`, `Artifact.ControlledBy Spawner>TriggeredTarget,Enchantment.ControlledBy Spawner>TriggeredTarget`, `Artifact.ControlledBy TriggeredDefendingPlayer`, `Artifact.ControlledBy TriggeredDefendingPlayer,Enchantment.ControlledBy TriggeredDefendingPlayer`, `Artifact.ControlledBy TriggeredTarget`, `Artifact.ControlledBy TriggeredTarget,Enchantment.ControlledBy TriggeredTarget`, `Artifact.nonCreature`, `Artifact.nonCreature+cmcEQX`, `Artifact.nonCreature+cmcLE3`, `Artifact.OppCtrl`, `Artifact.OppCtrl+!token,Enchantment.OppCtrl+!token`, `Artifact.OppCtrl+cmcLEX,Enchantment.OppCtrl+cmcLEX`, `Artifact.OppCtrl,Creature.OppCtrl`, `Artifact.OppCtrl,Enchantment.OppCtrl`, `Artifact.OppCtrl,Enchantment.OppCtrl,Land.nonBasic+OppCtrl`, `Artifact.OppCtrl,Land.OppCtrl`, `Artifact.Other`, `Artifact.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouDontCtrl`, `Artifact.YouDontCtrl,Creature.YouDontCtrl`, `Attraction.TargetedPlayerCtrl`, `Aura`, `Aura.AttachedTo Creature`, `Aura.AttachedTo Creature.YouCtrl`, `Aura.AttachedTo Land`, `Card.Attraction`, `Creature`, `Creature,Enchantment`, `Creature,Enchantment,Planeswalker`, `Creature,Land`, `Creature,Planeswalker`, `Creature,Planeswalker,Vehicle`, `Creature,Planeswalker.Other`, `Creature,Spacecraft`, `Creature,Vehicle`, `Creature.!enchanted`, `Creature.!HasCounters`, `Creature.!Outlaw`, `Creature.Artifact`, `Creature.Artifact,Creature.Black`, `Creature.attacking`, `Creature.attacking+nonArtifact`, `Creature.attacking+powerLE2,Creature.blocking+powerLE2`, `Creature.attacking+withFlying`, `Creature.attacking+withFlying,Creature.blocking+withFlying`, `Creature.attacking+withoutFlying`, `Creature.attacking,Creature.blocking`, `Creature.Black`, `Creature.Black+attacking,Creature.Black+blocking,Creature.Red+attacking,Creature.Red+blocking`, `Creature.Black,Planeswalker.Black`, `Creature.blocked`, `Creature.blockedBySourceLKI`, `Creature.blockedValidThisTurn Creature.Legendary,Creature.blockedByValidThisTurn Creature.Legendary`, `Creature.blocking`, `Creature.blockingSource`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.Blue`, `Creature.Blue+withFlying,Creature.Black+withFlying`, `Creature.ChosenType`, `Creature.Cleric`, `Creature.cmcEQX`, `Creature.cmcGE3`, `Creature.cmcLE2`, `Creature.cmcLE2,Planeswalker.cmcLE2`, `Creature.cmcLE3`, `Creature.cmcLE3+YouDontCtrl`, `Creature.cmcLE3,Planeswalker.cmcLE3`, `Creature.cmcLEX`, `Creature.ControlledBy ChoosingPlayer`, `Creature.ControlledBy Spawner>TriggeredTarget,Planeswalker.ControlledBy Spawner>TriggeredTarget`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.ControlledBy TriggeredTarget`, `Creature.counters_GE1_BOUNTY`, `Creature.counters_GE1_M1M1`, `Creature.dealtDamageThisTurn`, `Creature.dealtDamageToYouThisTurn`, `Creature.enchanted`, `Creature.enchanted,Creature.Enchantment`, `Creature.Enchantment+OppCtrl`, `Creature.faceDown`, `Creature.Green`, `Creature.Green,Creature.White`, `Creature.HasCounters`, `Creature.hasKeywordLandwalk:Island`, `Creature.Human`, `Creature.Knight`, `Creature.Land,Land.nonBasic`, `Creature.Legendary`, `Creature.Legendary,Artifact.Legendary,Enchantment.Legendary`, `Creature.MonoColor`, `Creature.nonAngel+nonDemon+nonDevil+nonDragon`, `Creature.nonArtifact`, `Creature.nonArtifact+ActivePlayerCtrl`, `Creature.nonArtifact+ControlledBy TriggeredPlayer`, `Creature.nonArtifact+nonBlack`, `Creature.nonBlack`, `Creature.nonBlack+attacking`, `Creature.nonBlack+cmcEQX`, `Creature.nonBlack+ControlledBy TriggeredTarget`, `Creature.nonBlack+EnteredSinceYourLastTurn`, `Creature.nonBlack+nonArtifact`, `Creature.nonBlack+tapped`, `Creature.nonBlack+TargetedPlayerCtrl`, `Creature.nonBlack+ThisTurnEntered`, `Creature.nonColorless`, `Creature.nonDemon`, `Creature.nonElf`, `Creature.nonElf+!equalPT`, `Creature.nonElf+OppCtrl+powerLEX`, `Creature.nonGorgon+OppCtrl`, `Creature.nonGreen`, `Creature.nonLegendary`, `Creature.nonMerfolk`, `Creature.nonSnow`, `Creature.nonSpirit`, `Creature.nonVampire+nonWerewolf+nonZombie`, `Creature.nonWhite+nonBlack`, `Creature.nonZombie`, `Creature.NotedColor`, `Creature.OppCtrl`, `Creature.OppCtrl+cmcGE3`, `Creature.OppCtrl+cmcLE2`, `Creature.OppCtrl+powerLE2`, `Creature.OppCtrl+tapped`, `Creature.OppCtrl+wasDealtDamageThisTurn`, `Creature.OppCtrl+wasDealtDamageThisTurn,Planeswalker.OppCtrl+wasDealtDamageThisTurn`, `Creature.OppCtrl+withFlying`, `Creature.OppCtrl,Enchantment.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.Other`, `Creature.Other+sameName`, `Creature.Other,Planeswalker.Other`, `Creature.powerGE3`, `Creature.powerGE4`, `Creature.powerGE4+OppCtrl`, `Creature.powerGE4,Artifact,Enchantment`, `Creature.powerGE4,Creature.toughnessGE4`, `Creature.powerLE1`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.powerLE3+attacking`, `Creature.powerLE3+attacking,Creature.powerLE3+blocking`, `Creature.powerLE3+OppCtrl`, `Creature.powerLE4`, `Creature.powerLEX`, `Creature.powerLTX`, `Creature.Red`, `Creature.sameName`, `Creature.Spirit`, `Creature.tapped`, `Creature.tapped+nonBlack`, `Creature.tapped+OppCtrl`, `Creature.tapped,Creature.blocking`, `Creature.token`, `Creature.totalPT_LE5`, `Creature.toughnessGE4`, `Creature.toughnessLE2`, `Creature.toughnessLE3`, `Creature.toughnessLEX`, `Creature.untapped`, `Creature.Vampire,Creature.Werewolf,Creature.Zombie`, `Creature.wasDealtDamageThisTurn`, `Creature.wasDealtDamageThisTurn+OppCtrl`, `Creature.White`, `Creature.White,Planeswalker.White,Creature.Green,Planeswalker.Green`, `Creature.withDefender`, `Creature.withFlying`, `Creature.withHorsemanship`, `Creature.withoutFlying`, `Creature.withShadow`, `Creature.YouDontCtrl+wasDealtDamageThisTurn`, `Creature.YouDontCtrl,Planeswalker.YouDontCtrl`, `Djinn,Efreet`, `Dragon.attacking,Dragon.blocking`, `Enchantment`, `Enchantment,Artifact`, `Enchantment,Creature`, `Enchantment,Land`, `Enchantment.ControlledBy TriggeredTarget`, `Enchantment.nonAura`, `Enchantment.OppCtrl`, `Equipment`, `Equipment.Attached`, `Equipment.ControlledBy TriggeredTarget`, `Forest,Enchantment.Green,Planeswalker.Green`, `Goblin`, `Land`, `Land,Creature`, `Land,Creature.nonBlack`, `Land.ControlledBy ParentTarget`, `Land.hasNonManaActivatedAbility`, `Land.Island+OppCtrl,Land.Swamp+OppCtrl`, `Land.nonBasic`, `Land.nonBasic+ControlledBy Spawner>TriggeredDefendingPlayer`, `Land.nonBasic+OppCtrl`, `Land.nonSwamp`, `Land.Snow`, `Land.Snow,Land.canProduceManaColor Colorless`, `Mountain`, `Ninja`, `Permanent`, `Permanent.Black`, `Permanent.Blue`, `Permanent.BorderColorSilver`, `Permanent.ChosenColor`, `Permanent.Creature+OppCtrl`, `Permanent.enchanted`, `Permanent.Legendary`, `Permanent.MultiColor`, `Permanent.nonColorless`, `Permanent.nonCreature`, `Permanent.nonCreature+Blue,Permanent.nonCreature+Black`, `Permanent.nonCreature+nonLand+cmcLE1`, `Permanent.nonCreature+nonLand+cmcLE2`, `Permanent.nonCreature+OppCtrl`, `Permanent.nonland`, `Permanent.nonLand`, `Permanent.nonLand+cmcEQX`, `Permanent.nonLand+cmcLE2`, `Permanent.nonLand+cmcLE3`, `Permanent.nonLand+cmcLEX+OppCtrl`, `Permanent.nonLand+Colorless`, `Permanent.nonLand+lowestCMC`, `Permanent.nonLand+OppCtrl`, `Permanent.nonLand+OppCtrl+cmcLE4`, `Permanent.nonWhite`, `Permanent.OppCtrl`, `Permanent.OppCtrl+nonland`, `Permanent.OppCtrl+nonland+!token`, `Permanent.Red`, `Permanent.token+OppCtrl`, `Permanent.YouOwn`, `Plains,Island`, `Planeswalker`, `Planeswalker.activated,Creature.tapped`, `Planeswalker.Other`, `Reflection`, `Room`, `Scarecrow,Plains`, `Spirit,Enchantment`, `Treefolk,Forest`, `Vampire`, `Vehicle`, `Wall`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `artifact or creature`, `noncreature artifact`

## `DestroyAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `FellTheMighty`, `RaidingParty`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If you control an untapped land,`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.!kicked`, `Card.kicked`, `Creature.powerEQ20`, `Land.untapped+YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`, `GE5`, `GE6`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<7/LOYALTY>`, `SubCounter<11/LOYALTY>`, `2 T Sac<1/CARDNAME>`, `5`, `3 T Sac<1/CARDNAME>`, `Sac<1/CARDNAME>`, `X X W Sac<1/CARDNAME>`, `SubCounter<3/LOYALTY>`, `SubCounter<5/LOYALTY>`, `3 B Sac<1/Creature>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{4}{W}{B}`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `Hidden$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `3 W`, `3 W W`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoRegen$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoRegenValid$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Cleave`, `Omnislash`
- `RememberAllObjects$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDestroyed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddMana`, `DBChoose`, `DBChooseCard`, `DBCleanImp`, `DBCleanup`, `DBCleanUp`, `DBClearUgin`, `DBDamageAll`, `DBDealDamage`, `DBDestroyAll`, `DBDestroyChaosOrb`, `DBDig`, `DBDraw`, `DBDrawCard`, `DBEffect`, `DBEndTurn`, `DBExile`, `DBFood`, `DBGainControl`, `DBGainLife`, `DBLoseLife`, `DBNoUntap`, `DBPay`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBRemove`, `DBRepeat`, `DBReturn`, `DBSacrifice`, `DBScry`, `DBSearch`, `DBTapAll`, `DBToken`, `DBTokenInfestation`, `DBTransform`, `DBTreasure`, `DBVoidRevealDiscard`, `PWAway`, `ThreshReturn`, `ThreshToken`, `TrigKicker`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `DamageYou<6>`, `PayEnergy<Y>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment`, `Artifact,Creature,Land`, `Artifact,Enchantment`, `Artifact.cmcEQX`, `Artifact.cmcEQX,Creature.cmcEQX`, `Artifact.cmcEQX,Creature.cmcEQX,Enchantment.cmcEQX`, `Artifact.cmcLE3`, `Artifact.cmcLEX`, `Artifact.cmcLEX,Creature.cmcLEX`, `Artifact.cmcLEX,Creature.cmcLEX,Enchantment.cmcLEX`, `Artifact.cmcLEY,Creature.cmcLEY,Enchantment.cmcLEY`, `Artifact.nonLand+cmcLE4`, `Artifact.YouDontCtrl`, `Aura`, `Aura,Equipment`, `Aura.AttachedTo Card.IsRemembered`, `Battle`, `Card.AttachedTo Targeted`, `Card.Aura+AttachedTo Card.Self`, `Card.Aura+AttachedTo Targeted`, `Card.ChosenCard`, `Card.Enchantment+YouCtrl,Card.Aura+AttachedTo Permanent.YouCtrl,Card.Aura+AttachedTo Creature.attacking+OppCtrl`, `Card.IsImprinted`, `Card.IsRemembered`, `Card.IsRemembered+!token`, `Card.Self,Card.blockedBySourceThisTurn`, `Card.token`, `Creature`, `Creature,Enchantment`, `Creature,Land`, `Creature,Permanent.AttachedTo Creature`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!AllColors`, `Creature.!ChosenCard`, `Creature.!enchanted`, `Creature.!HasCounters`, `Creature.!IsCommander,Planeswalker.!IsCommander`, `Creature.!IsImprinted`, `Creature.!IsRemembered`, `Creature.!token`, `Creature.ActivePlayerCtrl+!attackedThisTurn+nonWall+!firstTurnControlled`, `Creature.Black`, `Creature.blocked,Creature.blocking`, `Creature.blockedByRemembered`, `Creature.blockedByThisTurn,Creature.blockedThisTurn`, `Creature.blockedByValidThisTurn ParentTarget`, `Creature.blockedRemembered,Creature.blockedByRemembered`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.ChosenCard`, `Creature.ChosenCardStrict+!attackedThisTurn`, `Creature.ChosenSector`, `Creature.ChosenType`, `Creature.ChosenType+TargetedPlayerCtrl`, `Creature.cmcChosenEvenOdd`, `Creature.cmcEQX`, `Creature.cmcGE4`, `Creature.cmcLE2`, `Creature.cmcLE3`, `Creature.cmcLEX`, `Creature.Dalek`, `Creature.dealtDamageToYouThisTurn`, `Creature.Dragon`, `Creature.Goblin`, `Creature.Green`, `Creature.IsNotChosenType`, `Creature.IsRemembered`, `Creature.IsTriggerRemembered+!attackedThisTurn`, `Creature.Legendary`, `Creature.nonArtifact`, `Creature.nonArtifact+nonBlack`, `Creature.nonBlack`, `Creature.nonChosenCard`, `Creature.nonChosenCard,Planeswalker.nonChosenCard`, `Creature.nonDalek`, `Creature.nonDinosaur`, `Creature.nonDragon`, `Creature.nonEnchantment`, `Creature.nonGiant`, `Creature.nonGorgon`, `Creature.nonLand`, `Creature.nonLegendary`, `Creature.nonVehicle`, `Creature.nonWall+!firstTurnControlled+untapped+ActivePlayerCtrl+!attacking`, `Creature.nonWall+blockingEnchanted`, `Creature.nonWhite`, `Creature.nonZombie`, `Creature.OppCtrl`, `Creature.OppCtrl+counters_GE1_PREY`, `Creature.Other`, `Creature.Other,Artifact`, `Creature.powerGE3`, `Creature.powerGE4`, `Creature.powerGEX`, `Creature.powerGTX`, `Creature.powerLE2`, `Creature.powerLTX`, `Creature.sharesCreatureTypeWith Sacrificed`, `Creature.StrictlyOther`, `Creature.StrictlyOther+YouCtrl`, `Creature.tapped`, `Creature.ThisTurnEntered`, `Creature.totalPT_GE5+totalPT_LE8`, `Creature.totalPT_GE9`, `Creature.totalPT_LE4`, `Creature.toughnessGE4`, `Creature.toughnessLEX`, `Creature.untapped`, `Creature.untapped+IsRemembered`, `Creature.Wall`, `Creature.wasDealtDamageThisTurn+StrictlyOther`, `Creature.White`, `Creature.withFlying`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl+wasDealtDamageThisTurn`, `Creature.YouDontCtrl,Planeswalker.YouDontCtrl`, `Curse.AttachedTo You`, `Djinn,Efreet`, `Enchantment`, `Enchantment.ChosenColor`, `Enchantment.nonAura`, `Enchantment.nonWhite`, `Enchantment.OppCtrl`, `Enchantment.StrictlyOther`, `Enchantment.YouCtrl`, `Enchantment.YouDontCtrl`, `Forest`, `Goblin`, `Human`, `Island`, `Land`, `Land.IsRemembered`, `Land.nonBasic`, `Land.YouCtrl`, `Merfolk.IsRemembered`, `Permanent`, `Permanent.!ChosenCard`, `Permanent.!token+setHML`, `Permanent.!TriggeredCard+sharesNameWith TriggeredCard`, `Permanent.cmcEQX`, `Permanent.counters_GE1_DOOM`, `Permanent.IsRemembered`, `Permanent.namedWirefly`, `Permanent.nonArtifact`, `Permanent.nonArtifact+nonLand`, `Permanent.nonArtifact+nonLand+nonPhyrexian+StrictlyOther`, `Permanent.nonCreature+nonLand`, `Permanent.nonLand`, `Permanent.nonLand+!IsRemembered`, `Permanent.nonLand+!token`, `Permanent.nonLand+!token+StrictlyOther`, `Permanent.nonLand+cmcEQX`, `Permanent.nonLand+cmcEQX+controllerWasDealtCombatDamageByThisTurn`, `Permanent.nonLand+cmcEQY`, `Permanent.nonLand+cmcLE1`, `Permanent.nonLand+cmcLE2`, `Permanent.nonLand+cmcLEX`, `Permanent.nonLand+counters_LT1_FATE`, `Permanent.nonLand+OppCtrl`, `Permanent.Other`, `Permanent.White`, `Permanent.YouDontCtrl+sharesNameWith Remembered`, `Plains`, `Plains.!IsImprinted`, `Planeswalker`, `Reflection`, `Remembered.Equipment+Attached`, `Skeleton.token`, `Swamp.YouCtrl`, `Targeted.Equipment+Attached`, `Targeted.sameName+Other`, `Targeted.Self,Card.Equipment+Attached`, `TargetedCard.Self,Artifact.NotDefinedTargeted+sharesNameWith Targeted`, `TargetedCard.Self,Enchantment.NotDefinedTargeted+sharesNameWith Targeted`, `TargetedCard.Self,Land.NotDefinedTargeted+sharesNameWith Targeted`, `TargetedCard.Self,Permanent.NotDefinedTargeted+sharesNameWith Targeted`, `Triggered.SharesColorWith+Creature+Other`, `Wall.IsRemembered`, `Wall.OppCtrl`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `all creatures targeted opponent controls`, `all creatures targeted player controls`, `all nonland permanents`, `artifacts you don't control`, `each equipment equipped to target creature`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Land`, `Opponent`, `Player`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `Detain`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Valid Permanent.OppCtrl+nonLand+cmcLE4`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDraw`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`, `Permanent.nonLand+OppCtrl`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `creature an opponent controls`, `creature your opponent controls`, `nonland permanent an opponent controls`, `nonland permanent your opponent controls`

## `Dig`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `AdditionalDesc$`: TODO: Describe this parameter.
  Observed values: `This spell costs {2} less to cast for each card exiled this way.`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AlwaysConfirm`, `AtOppEOT`, `BestCard`, `DigForCreature`, `ExileAndPlayOrDealDamage`, `ExileAndPlayUntilEOT`, `MadSarkhanDigDmg`, `PayX`, `PayXButSaveMana.3`, `SacAndUpgrade`, `TimmerianFiends`, `WorstCard`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `Exiled`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many red cards to exile`
- `Attacking$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer`, `DefendingPlayer & Valid Planeswalker.ControlledBy DefendingPlayer`, `True`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChangeNum$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `4`, `All`, `Any`, `X`, `Y`
- `ChangeType$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ChangeValid$`: TODO: Describe this parameter.
  Observed values: `Ally`, `Ally,Equipment,Lesson`, `Artifact`, `Artifact,Creature,Enchantment,Land`, `Artifact,Creature,Enchantment,Land,Planeswalker`, `Artifact,Creature,Land`, `Artifact,Enchantment`, `Artifact.cmcLEX`, `Artifact.cmcLEY`, `Artifact.nonCreature+YouOwn`, `Assassin,Pirate,Vehicle`, `Aura`, `Aura,Creature,Planeswalker`, `Aura,Equipment`, `Aura.cmcLEX`, `Bat,Bird,Mouse,Rabbit`, `Card`, `Card.Artifact`, `Card.Black`, `Card.Blue,Card.Artifact`, `Card.ChosenType`, `Card.Cleric,Card.Rogue,Card.Warrior,Card.Wizard,Card.Ally`, `Card.cmcLEX`, `Card.Colorless`, `Card.Creature`, `Card.Creature+!sharesCreatureTypeWith Valid Creature.YouCtrl`, `Card.Creature,Card.Land`, `Card.Dragon`, `Card.Green`, `Card.Historic`, `Card.Human`, `Card.Instant,Card.Sorcery`, `Card.Knight,Aura,Equipment,Artifact.Legendary`, `Card.Land`, `Card.Legendary`, `Card.NamedByRememberedPlayer`, `Card.NamedCard`, `Card.nonCreature+nonLand`, `Card.nonLand`, `Card.numColorsEQ2`, `Card.Permanent+nonLand`, `Card.Permanent+nonLand+cmcLE3`, `Card.Red`, `Card.sharesCardTypeWith TriggeredCard`, `Card.Shrine`, `Card.Snow`, `Card.Warrior,Card.Equipment`, `Card.White`, `Card.withKicker,Card.withMultikicker`, `Creature`, `Creature,Enchantment`, `Creature,Land`, `Creature,Land,Planeswalker`, `Creature,Planeswalker`, `Creature,Planeswalker.Garruk`, `Creature,Vehicle`, `Creature.ChosenType`, `Creature.cmcLE3`, `Creature.cmcLE3,Artifact.cmcLE3`, `Creature.cmcLE4`, `Creature.cmcLEX`, `Creature.Dinosaur`, `Creature.Dragon`, `Creature.Goblin+cmcLE5`, `Creature.Human`, `Creature.IsRemembered`, `Creature.Kraken,Creature.Leviathan,Creature.Octopus,Creature.Serpent`, `Creature.Legendary`, `Creature.Mount,Plains`, `Creature.nonHuman`, `Creature.powerGE5`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.sharesCreatureTypeWith Enchanted`, `Creature.sharesCreatureTypeWith Self`, `Creature.sharesCreatureTypeWith TriggeredAttacker`, `Creature.YouCtrl+cmcLE3`, `Dinosaur,Land`, `Doctor`, `Dragon`, `Dwarf`, `Dwarf,Vehicle`, `Elemental,Island,Mountain`, `Elf`, `Elf,Swamp,Forest`, `Elf,Warrior,Tyvar`, `Enchantment`, `Enchantment,Land`, `Equipment`, `Equipment,Vehicle`, `Goblin`, `Goblin,Swamp,Mountain`, `Human,Artifact`, `Instant,Sorcery`, `Instant,Sorcery,Dragon`, `Instant.cmcLEX,Sorcery.cmcLEX`, `Island`, `Kavu`, `Kithkin,Forest,Plains`, `Land`, `Land,Card.DoubleFaced`, `Land,Card.hasXCost`, `Land,Creature.cmcLEY`, `Land,Permanent.Legendary+cmcLEX`, `Land,Turtle.Legendary`, `Land.Basic`, `Land.Basic+IsRemembered`, `Lesson,Saga,Shrine`, `Merfolk`, `Merfolk,Plains,Island`, `Mutant,Ninja,Turtle,Land`, `Permanent`, `Permanent.cmcLE3`, `Permanent.cmcLE5`, `Permanent.cmcLEX`, `Permanent.Goblin`, `Permanent.Green+cmcLEX`, `Permanent.nonCreature+nonLand+cmcLE3`, `Permanent.nonLand`, `Permanent.nonLand+cmcLE3`, `Permanent.nonLand+cmcLEX`, `Permanent.nonSaga`, `Permanent.sharesNameWith Battlefield`, `Permanent.Snow`, `Pirate,Artifact`, `Plane,Phenomenon`, `Planeswalker`, `Planeswalker.IsRemembered`, `Rat`, `Soldier`, `Spacecraft`, `Zombie`
- `ChangeValidDesc$`: TODO: Describe this parameter.
  Observed values: `creature card with mana value 3 or less`, `creature or land`, `noncreature, nonland`, `nonland`, `permanent card with mana value 3 or less`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `You`
- `Choser$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `Player.Opponent`, `Targeted`, `TriggeredPlayer`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `Delirium`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`
- `ConditionNotPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Bison`, `Card`, `Card.nonLand`, `Card.Outlaw+YouCtrl`, `Card.Self`, `Creature`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE5`, `GTY`, `LEY`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 U U`, `AddCounter<1/LOYALTY>`, `SubCounter<8/LOYALTY>`, `AddCounter<2/LOYALTY>`, `T Sac<1/CARDNAME>`, `PutCardToLibFromGrave<1/-1/Sorcery;Instant>`, `SubCounter<7/LOYALTY>`, `3 T`, `4 G`, `T tapXType<X/Creature>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ActivePlayer`, `ChosenPlayer`, `ImprintedController`, `Opponent`, `Opponent.IsCorrupted`, `Player`, `Player.Chosen`, `Player.IsRemembered`, `Player.Opponent`, `Remembered`, `ReplacedPlayer`, `ReplacedTarget`, `Targeted`, `TargetedOwner`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredAttackingPlayer`, `TriggeredCardController`, `TriggeredCardOwner`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredTarget`, `TriggeredTargetController`, `TriggeredTargets`, `You`
- `DefinedExiler$`: TODO: Describe this parameter.
  Observed values: `ReplacedPlayer`, `TriggeredSourceController`
- `DestinationZone$`: TODO: Describe this parameter.
  Observed values: `Ante`, `Battlefield`, `Exile`, `Graveyard`, `Hand`, `Library`, `PlanarDeck`
- `DestinationZone2$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Hand`, `Library`, `PlanarDeck`
- `DestZone2Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `DigNum$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `13`, `14`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `Count$ChosenNumber`, `Excess`, `LifePaidOnNewGame`, `VoteNum`, `X`, `Y`, `Z`
- `ExileFaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExileWithCounters$`: TODO: Describe this parameter.
  Observed values: `COLLECTION`, `FETCH`, `HATCHING`, `INTEL`, `SILVER`
- `FaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDownPower$`: TODO: Describe this parameter.
  Observed values: `2`
- `FaceDownSetType$`: TODO: Describe this parameter.
  Observed values: `Artifact & Creature & Cyberman`
- `FaceDownToughness$`: TODO: Describe this parameter.
  Observed values: `2`
- `ForceReveal$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceController`
- `ForceRevealToController$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForEachColorPair$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `FromBottom$`: TODO: Describe this parameter.
  Observed values: `True`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `True`
- `Imprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+IsSolved`, `Permanent.Blue+YouCtrl`
- `LibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`
- `LibraryPosition2$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoLooking$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalAbilityPrompt$`: TODO: Describe this parameter.
  Observed values: `Would you like to put the land onto the battlefield tapped?`, `Would you like to put the permanent onto the battlefield?`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `2`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Cohort —`, `Draw Arcanum`, `Master of Machines —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `PrimaryPrompt$`: TODO: Describe this parameter.
  Observed values: `Choose a card to Manifest`, `You may choose a creature card to put on the battlefield`, `You may choose a permanent card with mana value 3 or less to put on the battlefield`, `You may choose up to two land cards`
- `PromptToSkipOptionalAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomChange$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberMovedToZone$`: TODO: Describe this parameter.
  Observed values: `2`
- `RememberRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `RestRandomOrder$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `RevealOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `SelectPrompt$`: TODO: Describe this parameter.
  Observed values: `Select a permanent to put into your hand`
- `SetChosenPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `SkipReorder$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SourceZone$`: TODO: Describe this parameter.
  Observed values: `PlanarDeck`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StaticEffect$`: TODO: Describe this parameter.
  Observed values: `Enchantment`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `20Life`, `CastCard`, `ClearImprint`, `DamageOpponent`, `DBAnimate`, `DBAperture`, `DBBottom`, `DBBounce`, `DBBranch`, `DBCast`, `DBChange`, `DBChangeLibrary`, `DBChangeZone`, `DBChangeZone2`, `DBChangeZone3`, `DBChangeZoneAll`, `DBChoice`, `DBChoose`, `DBCleanup`, `DBCleanupChosen`, `DBCloak`, `DBConjure`, `DBConvert`, `DBCopy`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDelay`, `DBDelayedTrigger`, `DBDig`, `DBDig1`, `DBDig2`, `DBDigBis`, `DBDigUntil`, `DBDraw`, `DBEffect`, `DBEffect1`, `DBEffect2`, `DBEffectYou`, `DBElf`, `DBEnergy`, `DBExile2`, `DBExile3`, `DBFlip`, `DBGain`, `DBGainLife`, `DBImmediateTrigger`, `DBImmediateTriggerCheck`, `DBLand`, `DBLifeGain`, `DBLookAgain`, `DBLose`, `DBLoseLife`, `DBManifest`, `DBMayPlay`, `DBMayPlayLand`, `DBMoveToBottom`, `DBOmenLand`, `DBOppDigOne`, `DBOppDigTwo`, `DBPain`, `DBPlaneswalk`, `DBPlay`, `DBPlayThem`, `DBPlot`, `DBProliferate`, `DBPump`, `DBPumpTrample`, `DBPutCounter`, `DBPutHand`, `DBPutLand`, `DBRemoveCombat`, `DBRepeat`, `DBReplace`, `DBReturn`, `DBReturnToHand`, `DBRollDice`, `DBSacrifice`, `DBShuffle`, `DBSower`, `DBStackDesc`, `DBToken`, `DBTreasure`, `DBTrig`, `DBTwoPiles`, `DBUntap`, `DBWin`, `DBYouDigTwo`, `Dig2`, `EachLose`, `ExchangeOwn1`, `ExileAll`, `FindHighestCMCFirst`, `GainLife`, `MillTargeted`, `OpponentChooses`, `PickOne`, `PicksFight`, `RandomGraveyard`, `SeersCost`, `TheyChoose`, `YouChoose`, `YouPick`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Mandatory PayEnergy<X>`, `PayLife<2>`, `PayLife<Y>`, `Sac<1/CARDNAME> 2 G G`, `X`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `NonReplacedPlayer`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `You`
- `WithCounters$`: TODO: Describe this parameter.
  Observed values: `MANIFESTATION`, `Shield`
- `WithDifferentPowers$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithMayLook$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithTotalCMC$`: TODO: Describe this parameter.
  Observed values: `4`, `6`, `X`

## `DigMultiple`

TODO: Write documentation.

**Parameters:**
- `ChangeLater$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChangeValid$`: TODO: Describe this parameter.
  Observed values: `Card.Angel,Card.Demon,Card.Dragon`, `Card.Cleric,Card.Rogue,Card.Warrior,Card.Wizard`, `Card.Warrior,Card.Equipment`, `Card.withFlying,Card.withFirst Strike,Card.withDeathtouch,Card.withHaste,Card.withHexproof,Card.withIndestructible,Card.withLifelink,Card.withMenace,Card.withReach,Card.withTrample,Card.withVigilance`, `Creature,Enchantment`, `Creature,Land`, `Land,Spell.!Aura`
- `ChooseAmount$`: TODO: Describe this parameter.
  Observed values: `1`
- `ChosenZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<2/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`
- `DestinationZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Hand`
- `DestinationZone2$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Library`
- `DigNum$`: TODO: Describe this parameter.
  Observed values: `4`, `5`, `6`, `7`, `SVar$X/Plus.1`, `X`
- `ForceRevealToController$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintRest$`: TODO: Describe this parameter.
  Observed values: `True`
- `LibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `RestRandomOrder$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `SourceZone$`: TODO: Describe this parameter.
  Observed values: `Library`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChangeZone`, `DBGainLife`

## `DigUntil`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DontMillSelf`, `OathOfDruids`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `MassX`, `VoteNum`, `X`, `Y`
- `AttachedTo$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardLKICopy`
- `Attacking$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Y`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `MassX`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedLKI`, `TriggeredCard`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.wasCastFromYourHandByYou`, `Creature`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `GE6`, `GT0`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `AddCounter<1/LOYALTY>`, `Mandatory Sac<1/CARDNAME>`, `T Sac<1/Artifact>`, `4 T`, `Sac<1/Card.TriggeredSources>`, `2 R Sac<1/Permanent.nonLand/nonland permanent>`, `G Sac<1/Creature>`, `1`, `ExileAnyGrave<1/Card.TriggeredNewCard>`, `3 T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Eminence — {X}, Discard a card:`, `Grandeur — Discard another card named Page, Loose Leaf:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ImprintedController`, `Opponent`, `Player`, `Player.EnchantedBy`, `Player.Opponent`, `Remembered`, `RememberedController`, `RememberedOwner`, `TargetedController`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `DigZone$`: TODO: Describe this parameter.
  Observed values: `PlanarDeck`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `FoundDestination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`, `Hand`, `Library`, `PlanarDeck`
- `FoundLibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`
- `GainControl$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintFound$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxRevealed$`: TODO: Describe this parameter.
  Observed values: `X`
- `MinTotalCMC$`: TODO: Describe this parameter.
  Observed values: `20`, `4`, `5`
- `NoMoveFound$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoMoveRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoneFoundDestination$`: TODO: Describe this parameter.
  Observed values: `Library`
- `NoneFoundLibraryPosition$`: TODO: Describe this parameter.
  Observed values: `0`
- `NoPutDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalFoundMove$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalNoDestination$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Sketch and Lore`
- `RememberFound$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealedDestination$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Hand`, `Library`, `PlanarDeck`
- `RevealedLibraryPosition$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`
- `RevealRandomOrder$`: TODO: Describe this parameter.
  Observed values: `True`
- `Shuffle$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShuffleCondition$`: TODO: Describe this parameter.
  Observed values: `NoneFound`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CascadeCast`, `Damage`, `DBAnimate`, `DBBelch`, `DBCast`, `DBChange`, `DBChaosEnsues`, `DBChoose`, `DBChoosePlayer`, `DBClean`, `DBCleanup`, `DBClone`, `DBDamage`, `DBDealDamage`, `DBDmg`, `DBEffect`, `DBExileW`, `DBForget`, `DBImmediateTrigger`, `DBLoseLife`, `DBMassCleanup`, `DBMassShuffle`, `DBPlaneswalk`, `DBPlay`, `DBPlay1`, `DBPlay2`, `DBPump`, `DBPutCounter`, `DBPutOnTop`, `DBPWTo`, `DBShuffle`, `DBToHand`, `DBToPlay`, `MakeItChoose`, `MutantPump`, `RecrossClash`, `SacThought`, `ShadowReattach`, `TrigPump`, `UndyingDamage`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Aura`, `Card`, `Card.Artifact`, `Card.cmcEQX`, `Card.Creature`, `Card.Creature+nonLegendary+cmcLTX`, `Card.Historic`, `Card.Instant+cmcLEZ,Card.Sorcery+cmcLEZ,Card.Enchantment+cmcLEZ`, `Card.Land`, `Card.Legendary`, `Card.NamedCard`, `Card.namedMirror-Mad Phantasm`, `Card.nonLand`, `Card.nonLand+cmcGE3`, `Card.nonLand+cmcLE3`, `Card.nonLand+cmcLE4`, `Card.nonLand+doesNotShareNameWith Remembered`, `Card.nonLand+Legendary+cmcLTY`, `Card.nonLand+nonLegendary+cmcLE3`, `Card.nonLand+YouOwn`, `Card.sharesCardTypeWith RememberedLKI`, `Card.sharesCardTypeWith ReplacedSource`, `Card.sharesCardTypeWith TriggeredCardLKICopy`, `Card.White`, `Creature`, `Creature,Planeswalker`, `Creature.ChosenType`, `Creature.ChosenType+YouOwn`, `Creature.cmcEQX`, `Creature.cmcGEX`, `Creature.cmcLEX`, `Creature.nonLegendary`, `Creature.sharesCreatureTypeWith Sacrificed`, `Creature.sharesCreatureTypeWith TriggeredCardLKICopy`, `Creature.Time Lord`, `Creature.YouOwn`, `Creature.Zombie`, `Elf,Elemental`, `Equipment`, `Instant,Sorcery`, `Instant,Sorcery,Creature`, `Instant.cmcLTX,Sorcery.cmcLTX`, `Land`, `Land.Basic`, `Permanent`, `Permanent.Land`, `Permanent.nonLand`, `Permanent.nonland`, `Permanent.sharesCardTypeWith RememberedLKI`, `Plane`, `Saga`, `Shrine`, `Vehicle,Doctor,Card.withDoctor's companion`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `artifact`, `artifact or creature`, `basic land`, `creature`, `Creature`, `creature card`, `creature card of chosen type`, `creature card with higher mana value`, `creature or planeswalker`, `creature that shares a creature type`, `creature with chosen type`, `elf or elemental`, `historic card`, `instant or sorcery`, `instant, sorcery, or creature`, `land`, `land card`, `Mirror-Mad Phantasm`, `named card`, `nonland`, `nonland card`, `nonland permanent`, `nonland permanent with mana value 3 or greater`, `nonlegendary creature`, `permanent`, `permanent card that shares a card type with the destroyed permanent`, `permanent card that shares a card type with the sacrificed permanent`, `shares a card type with exiled card`, `the named`, `white`
- `ValidPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `Y`

## `Discard`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AnyPhaseIfFavored`, `AtLeast2`, `DiscardUncastableAndExcess`, `UnlessAtLife.6`, `VolrathsShapeshifter`
- `AnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Condition`, `Excess`, `Morbid`, `RaidTest`, `Resolved`, `X`, `Y`, `YourCruelty`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Imprinted`, `Remembered`, `RememberedLKI`, `Returned`, `Self`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If you do,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Card`, `Card.!kicked`, `Card.Green,Card.White`, `Card.Land`, `Card.nonLand`, `Card.spectacle`, `Card.ThisTurnEntered`, `Creature`, `Creature.Blue+YouCtrl`, `Creature.Other+YouCtrl+powerLE2`, `Creature.YouCtrl`, `Creature.YouCtrl+powerGE4`, `Land.hasANonBasicLandType`, `Ogre.YouCtrl`, `Planeswalker.Liliana+YouCtrl`, `Player`, `Zombie.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `GEOppsCruelty`, `LE4`, `LE6`, `LT3`, `LT5`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `X 1 B Discard<X/Card/card>`, `Draw<1/You>`, `T tapXType<1/Ally>`, `AddCounter<1/LOYALTY>`, `Sac<1/CARDNAME>`, `Sac<1/Creature>`, `1 B T ExileFromGrave<2/Card>`, `X B T`, `T`, `2 B T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `You may blight 1.`, `You may sacrifice a creature.`, `{2}{B}`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `NonRememberedController`, `OppNonParentTarget`, `OppNonRememberedController`, `Opponent`, `ParentTarget`, `ParentTargetedController`, `Player`, `Player.IsRemembered`, `Player.NotedForDiscard`, `Player.Opponent`, `Player.Other`, `Remembered`, `RememberedController`, `RememberedOwner`, `ReplacedPlayer`, `Targeted`, `TargetedController`, `TargetedOrController`, `TargetedOwner`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredAttackedTarget & You`, `TriggeredAttackingPlayer`, `TriggeredCardController`, `TriggeredCardOwner`, `TriggeredDefendingPlayer`, `TriggeredDefendingPlayer & You`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `DefinedCards$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRemembered`, `Imprinted`, `Remembered`, `ValidHand Card.!ChosenCard+OwnedBy Targeted`, `ValidHand Card.!IsRemembered+nonLand+RememberedPlayerCtrl`, `ValidHand Card.!IsRemembered+OwnedBy Targeted`, `ValidHand Card.IsRemembered+NamedCard`, `ValidHand Card.nonLand+IsRemembered`, `ValidHand Card.sharesNameWith Imprinted+RememberedPlayerCtrl+!IsImprinted`
- `DiscardValid$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Card`, `Card.ChosenCard`, `Card.ChosenColor`, `Card.cmcEQX`, `Card.Creature,Card.Planeswalker`, `Card.IsRemembered`, `Card.MultiColor`, `Card.NamedCard`, `Card.NamedCard+IsRemembered`, `Card.nonCreature`, `Card.nonCreature+nonLand`, `Card.nonLand`, `Card.nonLand+cmcEQX`, `Card.nonLand+cmcLE2`, `Card.nonLand+cmcLE3`, `Card.nonLand+cmcLEX`, `Card.nonLand+Colorless`, `Card.nonLand+nonCreature`, `Card.nonLand+nonLegendary`, `Card.Permanent+nonLand`, `Card.SharesColorWith Sacrificed`, `Card.sharesNameWith Remembered`, `Card.Trap`, `Creature`, `Creature,Battle`, `Creature,Enchantment,Planeswalker`, `Creature,Planeswalker`, `Creature.ChosenType`, `Creature.Spirit,Instant.Arcane,Sorcery.Arcane`, `Instant,Sorcery`, `Land`, `Land.nonBasic`, `Permanent.nonLand`
- `DiscardValidDesc$`: TODO: Describe this parameter.
  Observed values: `artifact or creature`, `card`, `card of that color`, `creature or battle`, `creature or planeswalker`, `creature, enchantment, or planeswalker`, `instant or sorcery`, `nonbasic land`, `noncreature`, `noncreature, nonland`, `nonland`, `nonland card`, `nonland card from it with mana value 2 or less`, `nonland card from it with mana value 3 or less`, `nonland card with mana value X or less`, `nonlegendary, nonland`, `Select up to one nonland card in your hand to discard`, `Spirit or Arcane`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `Defined`, `Hand`, `LookYouChoose`, `Random`, `RevealDiscardAll`, `RevealTgtChoose`, `RevealYouChoose`, `TgtChoose`, `YouChoose`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `7`, `BB`, `BreakthroughZ`, `C`, `ChosenInitiation`, `Count$CommittedCrimeThisTurn.1.2`, `IslandsYouControl`, `NantukoX`, `ThisTargetedPlayer$CardsInHand/HalfUp`, `VoteNum`, `WasKicked`, `X`, `Y`, `Z`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Cleave`, `Cohort —`, `Threshold —`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberDiscarded$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDiscardingPlayers$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealNumber$`: TODO: Describe this parameter.
  Observed values: `3`, `X`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ApathyUntap`, `BetThat`, `DBAirbend`, `DBAmass`, `DBAnte`, `DBCast`, `DBChandraDealDamage`, `DBChandraDraw`, `DBChangeZone`, `DBChangeZoneAll`, `DBChooseCard`, `DBCleanup`, `DBCopy`, `DBCoralSacrifice`, `DBCounter`, `DBCreature`, `DBDamage`, `DBDealDamage`, `DBDestroy`, `DBDig`, `DBDiscard`, `DBDiscard2`, `DBDiscardTarget`, `DBDmg`, `DBDmgAll`, `DBDraw`, `DBDraw2`, `DBDrawOne`, `DBDrawOpp`, `DBDrawSeven`, `DBDrawThree`, `DBEachDraw`, `DBExile`, `DBExileGraveyard`, `DBExileHand`, `DBExileSix`, `DBExperience`, `DBFlip`, `DBFluxDraw`, `DBGainLife`, `DBGainLife1`, `DBHeist`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBImmediateTriggerCheck`, `DBImprint`, `DBIncendiaryDraw`, `DBIncubate`, `DBInvestigate`, `DBLastRitesDiscard`, `DBLibrary`, `DBLose`, `DBLoseLife`, `DBLoseLifeOpp`, `DBLoseLifeThree`, `DBLosesGame`, `DBMana`, `DBMill`, `DBNantukoPutCounter`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBPutCounters`, `DBRaiseDead`, `DBRepeat`, `DBRepeatLoseLife`, `DBReturn`, `DBSac`, `DBSac1U`, `DBSacCreature`, `DBSacPermanent`, `DBSacrifice`, `DBScry`, `DBSearch`, `DBSeek`, `DBShuffle`, `DBSurveil`, `DBToken`, `DBTransform`, `DBTreasure`, `DBUnspeakable`, `DBUntap`, `DBUntapAll`, `DBWheelDraw`, `DelTrigSlowtrip`, `DemonBlight`, `DiscardRandom`, `ExileEffect`, `GainLife`, `MakeToken`, `MindMaggotsPutCounter`, `MorbidDiscard`, `MoveToGraveyard`, `ReturnAll`, `ReturnDross`, `TrigImmediateTrig`, `TrigMill`, `TrigReturn`, `TsabosDestroy`, `WindfallDraw`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `MaxTgt`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `DamageYou<4>`, `Draw<1/You>`, `ExileFromGrave<1/Card.Historic>`, `PayEnergy<2>`, `PayLife<1>`, `PayLife<3>`, `PayLife<4>`, `PayLife<7>`, `PayLife<X>`, `PutCardToLibFromHand<1/0/Card>`, `Return<1/Land>`, `Reveal<2/Card.Black>`, `Sac<1/Permanent>`, `Waterbend<2>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `RememberedController`, `ReplacedPlayer`, `Targeted`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessType$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Card.nonLand`, `Creature`, `Creature.withFlying,Instant,Sorcery`, `Enchantment`, `Instant,Sorcery`, `Land`, `Land.Basic`, `Pirate`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Opponent`

## `Discover`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Excess`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `5 ExileFromGrave<1/CARDNAME>`, `tapXType<2/Artifact;Creature/artifacts and/or creatures>`, `4`, `T ExileFromGrave<1/Creature>`, `4 U T Sac<1/CARDNAME>`, `4 W T Sac<1/CARDNAME>`, `4 B T Sac<1/CARDNAME>`, `4 G T Sac<1/CARDNAME>`, `4 R T Sac<1/CARDNAME>`, `1 SubCounter<2/CHARGE>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedOwner`
- `Num$`: TODO: Describe this parameter.
  Observed values: `10`, `3`, `4`, `5`, `Excess`, `TriggeredSpellAbility$CardManaCostLKI`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDiscovered$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBTreasure`

## `Draft`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$ValidGraveyard Card.YouOwn$DifferentCardManaCost`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE5`
- `Conjure$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Sac<2/Artifact>`, `Sac<1/Land>`, `W T`, `U Discard<2/Card>`, `SubCounter<1/LOYALTY>`, `1 BG ExileFromGrave<2/Card>`, `U Sac<1/Food>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `You`
- `DraftNum$`: TODO: Describe this parameter.
  Observed values: `2`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDrafted$`: TODO: Describe this parameter.
  Observed values: `True`
- `Spellbook$`: TODO: Describe this parameter.
  Observed values: `Abrade,Cleansing Wildfire,Terror of the Peaks,Explosive Singularity,Guttersnipe,Seasoned Pyromancer,Unexpected Windfall,Banefire,Lightning Bolt,Dualcaster Mage,Electrodominance,Crackle with Power,Volcanic Fallout,Young Pyromancer,Siege-Gang Commander`, `Accorder Paladin,Ardent Recruit,Auriok Sunchaser,Blade-Tribe Berserkers,Goblin Gaveleer,Hero of Bladehold,Hero of Oxid Ridge,Mirran Crusader,Oxidda Scrapmelter,Sunspear Shikari,Oxidda Finisher,Barbed Batterfist,Bladehold War-Whip,Dragonwing Glider,Jor Kadeen; the Prevailer`, `Acquisitions Expert,Asylum Visitor,Blade Juggler,Bloodthirsty Aerialist,Boneclad Necromancer,Hoard Robber,Malakir Blood-Priest,Malakir Cullblade,Morbid Opportunist,Slaughter Specialist,Tavern Swindler,Thieves' Guild Enforcer,Tithebearer Giant,Vengeful Warchief,Yuan-Ti Fang-Blade`, `Adagia; Windswept Bastion,Blast Zone,Cascading Cataracts,Contested War Zone,Deserted Temple,Dust Bowl,Kavaron; Memorial World,Mutavault,Nesting Grounds,Plaza of Heroes,Sunken Citadel,Susur Secundi; Void Altar,Terrain Generator,Uthros; Titanic Godcore`, `Adagia; Windswept Bastion,Evendo; Waking Haven,Kavaron; Memorial World,Susur Secundi; Void Altar,Uthros; Titanic Godcore`, `Air Response Unit,Skysovereign; Consul Flagship,Sky Skiff,High-Speed Hoverbike,Heart of Kiran,Aethersphere Harvester,Hulldrifter,Smuggler's Copter`, `Almighty Brushwagg,Frilled Sandwalla,Moss Viper,Brushstrider,Highland Game,Ironshell Beetle,Lotus Cobra,Kazandu Nectarpot,Gilded Goose,Nessian Hornbeetle,Scurrid Colony,Territorial Boar,Deathbonnet Sprout,Spore Crawler,Moldgraf Millipede`, `Amorphous Axe,Citizen's Crowbar,Cloudsteel Kirin,Conqueror's Flail,Fireshrieker,Fishing Pole,Krovod Haunch,Leech Gauntlet,Lion Sash,Mace of the Valiant,Maul of the Skyclaves,Shield of the Realm,Sigiled Sword of Valeron,Thran Power Suit,Thunder Lasso`, `Ancient Imperiosaur,Burning Sun's Avatar,Carnage Tyrant,Charging Monstrosaur,Etali; Primal Conqueror,Ghalta; Primal Hunger,Gishath; Sun's Avatar,Quartzwood Crasher,Regisaur Alpha,Ripjaw Raptor,Shifting Ceratops,Territorial Allosaurus,Tranquil Frillback,Verdant Sun's Avatar,Zacama; Primal Calamity`, `Ancient Imperiosaur,Conclave Tribunal,Knight-Errant of Eos,Loxodon Restorer,March of the Multitudes,Nissa's Expedition,Overwhelm,Triplicate Spirits,Venerated Loxodon`, `Angel of Destiny,Resplendent Angel,Angel of Vitality,Righteous Valkyrie,Angel of Invention,Angel of Sanctions,Valkyrie Harbinger,Emancipation Angel,Youthful Valkyrie,Resplendent Marshal,Enduring Angel,Sigardian Savior,Serra Angel,Stalwart Valkyrie,Segovian Angel`, `Angel of Suffering,Aphemia; the Cacophony,Balemurk Leech,Chitinous Crawler,Defiler of Flesh,Gravebreaker Lamia,Mindwrack Harpy,Puppet Raiser,Starving Revenant`, `Angelfire Ignition,Barge In,Become Brutes,Boon of Safety,Cheeky House-Mouse,Crumb and Get It,Defiant Strike,Embercleave,Feather of Flight,Mabel's Mettle,Might of the Meek,Moment of Heroism,Unleash Fury,War Squeak`, `Anointed Procession,Cathars' Crusade,Authority of the Consuls,Sigil of the Empty Throne,All That Glitters,Banishing Light,Divine Visitation,Duelist's Heritage,Glorious Anthem,Gauntlets of Light,Teleportation Circle,Angelic Gift,Spectral Steel,Cleric Class,Angelic Exaltation`, `Approach of the Second Sun,Day of Judgment,Time Warp,Counterspell,Demonic Tutor,Doom Blade,Lightning Bolt,Claim the Firstborn,Krosan Grip,Regrowth,Despark,Electrolyze,Growth Spiral,Lightning Helix,Putrefy`, `Arcane Encyclopedia,Daredevil Dragster,Diamond Mare,Filigree Familiar,Fountain of Renewal,Gilded Lotus,Golden Egg,Guild Globe,Heraldic Banner,Honored Heirloom,Key to the City,Prophetic Prism,Stuffed Bear,Treasure Vault,Zephyr Boots`, `Archipelagore,Junk Winder,Moat Piranhas,Mystic Skyfish,Nadir Kraken,Nezahal; Primal Tide,Pouncing Shoreshark,Pursued Whale,Riptide Turtle,Ruin Crab,Sea-Dasher Octopus,Sigiled Starfish,Spined Megalodon,Stinging Lionfish,Voracious Greatshark`, `Azorius Signet,Boros Signet,Dimir Signet,Golgari Signet,Gruul Signet,Izzet Signet,Orzhov Signet,Rakdos Signet`, `Bitterblossom,Brazen Borrower,Faebloom Trick,Faerie Fencing,Faerie Mastermind,Flitterwing Nuisance,Glen Elendra Guardian,High Fae Prankster,Hypnotic Sprite,Likeness Looter,Pestermite,Picklock Prankster,Spell Stutter,Vendillion Clique,Voracious Tome-Skimmer`, `Bloom Hulk,Contagion Engine,Contagion Clasp,Evolution Sage,Contentious Plan,Flux Channeler,Inexorable Tide,Merfolk Skydiver,Pollenbright Druid,Roalesk; Apex Hybrid,Sword of Truth and Justice,Thrummingbird,Smell Fear,Cankerbloom,Tezzeret's Gambit`, `Boltwing Marauder,Caldera Pyremaw,Magmatic Hellkite,Neriv; Heart of the Storm,Stormscale Scion,Thunderbreak Regent,Thundermane Dragon`, `Boots of Speed,Cliffhaven Kitesail,Colossus Hammer,Dueling Rapier,Spare Dagger,Tormentor's Helm,Goldvein Pick,Jousting Lance,Mask of Immolation,Mirror Shield,Relic Axe,Rogue's Gloves,Scavenged Blade,Shield of the Realm,Ceremonial Knife`, `Bounty Agent,Outflank,Bound in Gold,Bring to Trial,Glass Casket,Reprobation,Collar the Culprit,Compulsory Rest,Expel,Fairgrounds Warden,Iron Verdict,Luminous Bonds,Raise the Alarm,Seal Away,Summary Judgment`, `Bristling Boar,Enraged Ceratok,Exuberant Wolfbear,Gaea's Protector,Master Symmetrist,Ornery Dilophosaur,Overgrown Armasaur,Predatory Wurm,Prized Unicorn,Sabertooth Mauler,Spike-Tailed Ceratops,Spore Crawler,Thrashing Brontodon,Wardscale Crocodile,World Shaper`, `Chained Brute,Charmbreaker Devils,Festival Crasher,Forge Devil,Frenzied Devils,Havoc Jester,Hellrider,Hobblefiend,Pitchburn Devils,Sin Prodder,Spiteful Prankster,Tibalt's Rager,Torch Fiend,Brimstone Vandal,Devil's Play`, `Champion's Helm,Lightning Greaves,Sword of Body and Mind,Sword of Feast and Famine,Sword of Fire and Ice,Sword of Light and Shadow,Sword of War and Peace`, `Colossal Plow,Millstone,Whirlermaker,Magistrate's Scepter,Replicating Ring,Raiders' Karve,Weapon Rack,Relic Amulet,Orazca Relic,Fifty Feet of Rope,Pyre of Heroes,Treasure Chest,Leather Armor,Spiked Pit Trap,Gingerbrute`, `Corpse Churn,Corpse Hauler,Courier Bat,Durable Coilbug,Fear of Death,Gorging Vulture,Locked in the Cemetery,Naga Oracle,Necrotic Wound,Obsessive Stitcher,Reassembling Skeleton,Strategic Planning,Unmarked Grave,Wonder`, `Cultivator's Caravan,Bomat Bazaar Barge,Raiders' Karve,Demolition Stomper,Futurist Sentinel,Mechtitan Core,Reckoner Bankbuster,High-Speed Hoverbike,Mindlink Mech,Silent Submersible,Mobile Garrison,Untethered Express,Ovalchase Dragster,Daredevil Dragster,Thundering Chariot`, `Deathbloom Thallid,Deathbonnet Sprout,Rhizome Lurcher,Spore Crawler,Sporecrown Thallid,Sporemound,Swarm Shambler,Thallid Omnivore,Thallid Soothsayer,Yavimaya Sapherd,Fungal Plots,Verdant Force,Verdant Embrace,Spore Swarm,Saproling Migration`, `Demonic Bargain,Ever After,Demonic Pact`, `Dominating Vampire,Vampire Socialite,Stromkirk Bloodthief,Falkenrath Pit Fighter,Wolfkin Outcast,Howlpack Piper,Tovolar; Dire Overlord,Patrician Geist,Shipwreck Sifters,Steelclad Spirit,Heron-Blessed Geist,Archghoul of Thraben,Champion of the Perished,Headless Rider,Bladestitched Skaab`, `Eiganjo Exemplar,Imperial Subduer,Ancestral Katana,Selfless Samurai,Norika Yamazaki; the Poet,Akki Ronin,Peerless Samurai,Heiko Yamazaki; the General,Asari Captain,Eiganjo Uprising,Eater of Virtue,Sunblade Samurai,Reinforced Ronin,Adamant Will,Tempered in Solitude`, `Emergence Zone,Radiant Fountain,Scavenger Grounds,Boseiju; Who Endures,Gingerbread Cabin,Khalni Garden,Memorial to Unity,Thriving Grove,Hall of Oracles,Secluded Courtyard,Treasure Vault,Mobilized District,Bonders' Enclave,Roadside Reliquary,Field of Ruin`, `Entomber Exarch,Phyrexian Fleshgorger,Phyrexian Gargantua,Phyrexian Obliterator,Phyrexian Rager,Phyrexian Revoker,Toxic Abomination,Vault Skirge,Scrapwork Rager,Bilious Skulldweller,Archfiend of the Dross,Myr Convert,Zenith Chronicler,Soulless Jailer,Diminished Returner`, `Fleet Swallower,Moat Piranhas,Mystic Skyfish,Nadir Kraken,Pouncing Shoreshark,Sea-Dasher Octopus,Spined Megalodon,Stinging Lionfish,Voracious Greatshark,Archipelagore,Serpent of Yawning Depths,Wormhole Serpent,Sigiled Starfish,Riptide Turtle,Ruin Crab`, `Hag of Syphoned Breath,Hag of Dark Duress,Hag of Ceaseless Torment,Hag of Inner Weakness,Hag of Death's Legion,Hag of Scoured Thoughts,Hag of Twisted Visions,Hag of Mage's Doom,Hag of Noxious Nightmares`, `Midnight Reaper,Guardian of Faith,Knight of the Ebon Legion,Cavalier of Dawn,Benalish Marshal,Cavalier of Night,Murderous Rider,Order of Midnight,Acclaimed Contender,Dauntless Bodyguard,Valiant Knight,Smitten Swordmaster,Blacklance Paragon,History of Benalia,The Circle of Loyalty`, `Mosscoat Goriak,Sylvan Brushstrider,Murasa Rootgrazer,Dire Wolf Prowler,Ferocious Pup,Pestilent Wolf,Garruk's Uprising,Dawntreader Elk,Nessian Hornbeetle,Territorial Scythecat,Trufflesnout,Wary Okapi,Scurrid Colony,Barkhide Troll,Underdark Basilisk`, `Serra Angel,Resplendent Angel,Steel-Plume Marshal,Duelcraft Trainer,Falconer Adept,Seraph of Dawn,Star-Crowned Stag,Benalish Marshal,Blade Historian,Captivating Crew,Manaform Hellkite,Serra Paragon,Moonveil Regent,Skyship Stalker,Ogre Battledriver`, `Twin-Silk Spider,Drider,Brood Weaver,Glowstone Recluse,Gnottvold Recluse,Hatchery Spider,Mammoth Spider,Netcaster Spider,Sentinel Spider,Snarespinner,Sporecap Spider,Spidery Grasp,Spider Spawning,Prey Upon,Arachnoform`, `Witch's Cauldron,Witch's Vengeance,Witch's Oven,Witch's Cottage,Witch's Familiar,Curse of Leeches,Cauldron Familiar,Black Cat,Sorcerer's Broom,Bloodhunter Bat,Unwilling Ingredient,Expanded Anatomy,Cruel Reality,Torment of Scarabs,Trespasser's Curse`
- `SpellbookName$`: TODO: Describe this parameter.
  Observed values: `Planets`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBChangeZone`, `DBDiscard`, `DBExile`, `DBPlay`, `DBPut`, `DBReveal`, `TrigImmediateTrig`
- `TriggerZones$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `DrainMana`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer`, `Player`, `Targeted`, `TargetedController`
- `DrainMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDrainedMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBNoCombatDamage`

## `Draw`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Blessing`, `Delirium`, `Hellbent`, `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationGameTypes$`: TODO: Describe this parameter.
  Observed values: `Commander,Brawl,TinyLeaders,Oathbreaker`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Draw`, `End of Turn`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.Opponent`
- `AILifeThreshold$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `ConsiderPrimary`, `DoSacrifice`, `GainLife`, `Good`, `LifeLessThan.5`, `Main2`, `OptionalDraw`, `RespondToOwnActivation`, `VeilOfSummer`, `YawgmothsBargain`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `B`, `U`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`
- `AnnounceType$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `CastTest`, `Count$CountersRemovedThisTurn ENERGY You`, `RaidTest`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Blessing`, `Kicked`, `Kicked 2`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CardsThem`, `CheckRemoved`, `CreatureETBAmount`, `DiceResult`, `DiedThisTurn`, `Excess`, `FatefulHour`, `Loss`, `MilledSharesType`, `NumInHand`, `NumRingTempted`, `Opp`, `OtherLost`, `PlayerCountDefinedTriggeredAttackedTarget$HasPropertylifeGTX`, `RDCoolness`, `Resolved`, `ScryingGlassX`, `TriggeredAttacker$CardPower`, `TriggeredSpellAbility$CardPower`, `Win`, `X`, `XCards`, `Y`, `YourFerocity`, `YourTough`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE3`, `GE8`, `GTY`, `LT3`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `Imprinted`, `Remembered`, `RememberedLKI`, `Sacrificed`, `Self`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredSourceLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `a permanent you controlled or a token,`, `If CARDNAME was kicked,`, `If it was kicked,`, `If that permanent was blue or black,`, `If they do,`, `If this spell was kicked`, `If you control a blue creature,`, `If you control a Faerie,`, `If you control a Fish, Octopus, Otter, Seal, Serpent, or Whale,`, `If you control a Giant,`, `If you control a Kithkin,`, `If you control a Merfolk,`, `If you control a Treefolk,`, `If you control a Wizard,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `U`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Bird,Frog,Otter,Rat`, `Card`, `Card.!wasDealtDamageThisTurn`, `Card.AllColors`, `Card.Black`, `Card.ChosenCtrl`, `Card.counters_GE1_P1P1`, `Card.Creature`, `Card.IsCommander`, `Card.Legendary`, `Card.modified`, `Card.NamedCard`, `Card.nonCreature`, `Card.OwnedBy Opponent`, `Card.powerGE4`, `Card.PromisedGift`, `Card.prowled`, `Card.Self+counters_GE7_PHYRESIS`, `Card.Self+enchanted`, `Card.Self+IsRingbearer`, `Card.Self+Phyrexian`, `Card.Self+PromisedGift`, `Card.sharesNameWith YourGraveyard`, `Card.spectacle`, `Card.token`, `Card.wasCast`, `Card.wasCastFromGraveyard`, `Card.withToxic`, `Card.YouCtrl`, `Card.YouOwn`, `Card.Zombie`, `Creature`, `Creature,Land`, `Creature.attacking+YouCtrl`, `Creature.attackingYou`, `Creature.Blue+YouCtrl`, `Creature.counters_GE1_P1P1`, `Creature.enchanted+YouCtrl`, `Creature.greatestPower`, `Creature.greatestPower+YouCtrl`, `Creature.powerLE2`, `Creature.YouCtrl`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+modified`, `Creature.YouCtrl+powerGE3`, `Creature.YouCtrl+powerGE4`, `Creature.YouDontCtrl`, `Enchantment.YouCtrl`, `Faerie.YouCtrl`, `Fish.YouCtrl,Octopus.YouCtrl,Otter.YouCtrl,Seal.YouCtrl,Serpent.YouCtrl,Whale.YouCtrl`, `Giant.YouCtrl`, `Hamster`, `Kithkin.YouCtrl`, `Land`, `Land,Card.DoubleFaced`, `Land.YouCtrl`, `Legendary`, `Merfolk.YouCtrl`, `Permanent.Blue+YouCtrl+Other`, `Permanent.Blue,Permanent.Black`, `Permanent.YouCtrl+counters_GE1_OIL`, `Permanent.YouCtrl,Card.token`, `Pirate`, `Planeswalker.Chandra`, `Planeswalker.Nissa`, `Raccoon.YouCtrl`, `Spell`, `Treefolk.YouCtrl`, `Vehicle`, `Villain`, `Wizard.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQ5`, `EQScryingGlassY`, `EQY`, `GE1`, `GE10`, `GE2`, `GE3`, `GE4`, `GE5`, `GE6`, `GE7`, `GENotedLife`, `GEOppsFerocity`, `GEOppsTough`, `GEZ`, `GT0`, `GTCardsYou`, `GTMe`, `GTMostInHand`, `GTY`, `GTYCards`, `LE1`, `LE5`, `LT1`, `LT2`, `LT3`, `LTY`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Hand`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `W B G T Sac<1/CARDNAME>`, `2 U SubCounter<1/P1P1>`, `Discard<1/Card>`, `T PayEnergy<50>`, `1 Sac<1/CARDNAME>`, `2 T`, `2 B Sac<1/Creature.Other/another creature>`, `2 Sac<1/CARDNAME>`, `Sac<1/Land>`, `2 U T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, discard a card.`, `As an additional cost to cast this spell, discard a land card.`, `As an additional cost to cast this spell, discard two cards.`, `As an additional cost to cast this spell, discard X cards.`, `Discard two nonland cards with the same name`, `{3}, {T}, Pay life equal to the number of colors in your commanders' color identity:`, `{3}{U}{U}`, `{4}{G}{U}`, `{T}, Discard a black card:`, `{T}, Discard a non-black card:`, `{T}, Exile two cards from your graveyard:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `.Chosen,You`, `AttackingPlayer`, `CardController & ReplacedTarget`, `CardOwner`, `ChoosingPlayer`, `ChosenPlayer`, `DelayTriggerRemembered`, `NonTriggeredCardController`, `OppNonRememberedOwner`, `Opponent`, `OriginalHostController`, `ParentTarget`, `Player`, `Player.Chosen`, `Player.controlsCreature.MultiColor`, `Player.controlsCreature.powerGE4_GE1`, `Player.controlsPermanent.namedBonder's Ornament`, `Player.IsRemembered`, `Player.NotedForExileDraw`, `Player.NotedForStargate`, `Player.Opponent`, `Player.Opponent+IsRemembered`, `Player.OpponentOf TriggeredCardController`, `Player.Other`, `Promised`, `Remembered`, `RememberedController`, `RememberedOwner`, `ReplacedPlayer`, `ReplacedSourceController`, `SourceController`, `Targeted`, `TargetedAndYou`, `TargetedController`, `TargetedOwner`, `TargetedPlayer`, `ThisTargetedPlayer`, `TriggeredActivator`, `TriggeredAttackedTarget & You`, `TriggeredAttackingPlayer`, `TriggeredAttackingPlayer & You`, `TriggeredAttackingPlayer.Opponent+controlsCreature.attacking Player.EnchantedBy`, `TriggeredBlockerController`, `TriggeredCardController`, `TriggeredCardOpponent`, `TriggeredCardOwner`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredPlayer & You`, `TriggeredSourceController`, `TriggeredSourcesController & You`, `TriggeredTarget`, `You`, `You & ReplacedPlayer`, `You & TriggeredDefendingPlayer`, `You & TriggeredTarget`, `You.!CardsInHandAtBeginningOfTurn`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `GiftDescription$`: TODO: Describe this parameter.
  Observed values: `a card`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+attacking`, `Card.Self+Blue`, `Card.Self+counters_GE5_OIL`, `Card.YouOwn`, `Creature.YouCtrl+powerGE4`, `Land.YouCtrl`
- `ManaRestriction$`: TODO: Describe this parameter.
  Observed values: `ChosenColor`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `TgtChoose`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `B B`
- `NonBasicSpell$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `20`, `3`, `4`, `5`, `7`, `8`, `9`, `AffectedX`, `B`, `CardsToDraw`, `Count$CardBasePower`, `Count$DifferentCounterKinds_Card.Self`, `Count$RememberedSize`, `Count$RememberedSize/Plus.1`, `Count$Valid Artifact.YouCtrl`, `Count$Valid Permanent.YouCtrl+YouDontOwn`, `Count$YourSpeed`, `DecreeX`, `Difference`, `Disgorge`, `DrawNum`, `DrawX`, `HalfXDown`, `HunterProwessY`, `IslandsYouControl`, `JoinForcesAmount`, `Lands`, `NantukoY`, `NumCreats`, `NumScrolls`, `PlayerCountRegisteredOpponents$HasPropertyLostLifeThisTurn`, `PrivateResearchX`, `Remembered$Amount`, `Remembered$Amount/Plus.1`, `RemTossed`, `ReplaceCount$Number/Plus.1`, `Result`, `Sacrificed$CardPower`, `SVar$X/Plus.1`, `UU`, `VoteNum`, `Votes`, `Wins`, `X`, `XLKI`, `XPower`, `Y`, `Z`
- `NumCardsDesc$`: TODO: Describe this parameter.
  Observed values: `cards equal to that card's mana value`, `two cards for each opponent who controls fewer creatures than you`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `TargetedController`, `TriggeredCardController`, `True`, `You`
- `OrOtherConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `OrString$`: TODO: Describe this parameter.
  Observed values: `Draw a card.`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Atomic Transmutation —`, `Channel —`, `Cleave`, `Cohort —`, `Corrupted —`, `Delirium —`, `Ferocious —`, `Field Reprogramming —`, `GOOOOAAAALLL! —`, `Hellbent —`, `Max speed —`, `Sleight of Hand —`, `Threshold —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ7`, `GE5`, `GE7`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `RaiseCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberDrawn$`: TODO: Describe this parameter.
  Observed values: `AllReplaced`, `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `All`, `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `BlessedLife`, `CalimChooseTwo`, `ChangeZoneDB`, `CheatBattlefield`, `CleanDrawn`, `CleanIncendiary`, `CleanTheFlux`, `CleanTheWind`, `DB1`, `DBAbandon`, `DBAddendum`, `DBAmass`, `DBAnimate`, `DBBlight`, `DBBottom`, `DBBounce`, `DBBranch`, `DBBreakthroughDiscard`, `DBCandlesCleanup`, `DBCast`, `DBChange`, `DBChangeZone`, `DBChangeZone2`, `DBChangeZone20U`, `DBChangeZone7M`, `DBChangeZoneAllOpponents`, `DBChangeZoneBis`, `DBChaos`, `DBChoose`, `DBChooseCardOne`, `DBChooseColor`, `DBChooseNumber`, `DBChoosePlayer`, `DBClash`, `DBCleanC`, `DBCleanE`, `DBCleanP`, `DBCleanup`, `DBClearNoted`, `DBClearRemembered`, `DBColor`, `DBConnive`, `DBConvert`, `DBCopy`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDestroy`, `DBDiscard`, `DBDiscard20`, `DBDiscard20M`, `DBDiscard3`, `DBDiscardJustAsMany`, `DBDiscardOrFreeCast`, `DBDiscardYou`, `DBDmg`, `DBDoubleCounters`, `DBDraw`, `DBDraw2`, `DBDrawMore`, `DBDrawX`, `DBDrawYou`, `DBEffect`, `DBEmblem`, `DBEnd`, `DBEnduringCleanup`, `DBEnergy`, `DBExile`, `DBExileForEach`, `DBExtraTurn`, `DBFlip`, `DBFood`, `DBGain`, `DBGainControl`, `DBGainGontrol`, `DBGainLife`, `DBGainLifeYou`, `DBGetMana`, `DBGreen`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBIntensify`, `DBInvestigate`, `DBKhorne`, `DBLand`, `DBLearn`, `DBLife`, `DBLLoseLife`, `DBLook`, `DBLoseLife`, `DBLoseLife1`, `DBLoseLife2`, `DBLoseLifeSeven`, `DBLoseLifeYou`, `DBMana`, `DBMana14`, `DBMill`, `DBMLoseLife`, `DBNantukoCleanup`, `DBNoCombatDamage`, `DBPain`, `DBPass`, `DBPlaneswalk`, `DBPlay`, `DBProlif`, `DBProliferate`, `DBPump`, `DBPumpAll`, `DBPut`, `DBPutCounter`, `DBPutCounter1`, `DBPutCounterAll`, `DBRadiation`, `DBRegenerate`, `DBRemoveCounter`, `DBRemoveCounters`, `DBRepeat`, `DBRepeatCreature`, `DBReset`, `DBReveal`, `DBSac`, `DBSacrifice`, `DBScry`, `DBScryingGlassCleanup`, `DBSeek`, `DBSetLife`, `DBShuffle`, `DBSkip`, `DBSkipTurn`, `DBSLoseLife`, `DBSpace`, `DBSubDraw`, `DBTap`, `DBToken`, `DBToken1`, `DBToken2`, `DBToken3`, `DBTop`, `DBTransform`, `DBTreasure`, `DBTrigger`, `DBUnblockable`, `DBUntap`, `DBUntapAll`, `DBVillainousChoice`, `DBWar`, `DelayedDiscard`, `DelayedReturn`, `DelTrig`, `DelTrigSlowtrip`, `DelTrigUntap`, `Discard`, `Discard3`, `DiscardTwo`, `EachPlayLand`, `Effect`, `ExileEffect`, `HardCoverDiscard`, `MathasPayoffLife`, `MillOne`, `MindFlame`, `NoteNum`, `OppExile`, `OppTreasureScry`, `PitifulDraw`, `PumpAll`, `PWAway`, `ResetCoolness`, `SetAllLife`, `SetLife`, `Switch`, `TrigAddDraw`, `TrigChoosePlayer3`, `TrigDamageOpp`, `TrigDiscard`, `TrigDraft`, `TrigDrain`, `TrigReveal`, `TrigSteal`, `TrigTempt`, `TrigToken`, `Unfathomable`, `UntapLands`, `WindfallCleanup`, `WinGame`, `WitEmblem`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ5`, `GE2`, `GE3`, `GE4`, `GE8`
- `TapCreaturesForMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`, `MaxTgt`, `MaxTgts`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `2`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `LowPriority`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `4`, `DamageYou<4>`, `DamageYou<5>`, `Discard<1/Card>`, `Discard<1/Creature>`, `Discard<1/Random>`, `Discard<2/Card>`, `Draw<3/Player.targetedBy>`, `PayLife<1>`, `PayLife<3>`, `PayLife<5>`, `Sac<1/Artifact>`, `Sac<1/Creature>`, `Sac<1/Land>`, `Sac<1/Permanent>`, `Sac<2/Permanent.nonLand+!token/nonland nontoken permanents>`, `tapXType<1/Artifact>`, `tapXType<2/Creature;Treasure/creatures and/or Treasures>`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.IsRemembered`, `Targeted`, `TriggeredActivator`, `TriggeredAttackingPlayer`, `TriggeredSourceController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `Upto$`: TODO: Describe this parameter.
  Observed values: `True`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Ability.IsTargeting Player.HasCardsInHand_Card_GEY`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.!EnchantedBy`, `Player.Other`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `LifeGained`

## `EachDamage`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `MadSarkhanUltimate`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<7/LOYALTY>`, `SubCounter<4/LOYALTY>`
- `DamageDesc$`: TODO: Describe this parameter.
  Observed values: `damage equal to its power`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `TriggeredAttackerLKICopy`, `Valid Creature,Planeswalker`
- `DefinedDamagers$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Remembered`, `Targeted`, `Targeted.YouCtrl`, `Valid Bird.Other+YouCtrl`, `Valid Creature.modified+YouCtrl`, `Valid Creature.Wolf+YouCtrl,Creature.Werewolf+YouCtrl`, `Valid Creature.YouCtrl`, `Valid Creature.YouCtrl+powerGE4`
- `EachToItself$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumDmg$`: TODO: Describe this parameter.
  Observed values: `1`, `Count$CardPower`, `Count$CardToughness`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ToEachOther$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.!IsRemembered+ControlledBy TargetedController`, `Creature.tapped`, `Creature.YouCtrl+counters_GE1_P1P1`, `Dragon.Creature+YouCtrl`, `Dragon.YouCtrl`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `Dragon creature you control`, `modified creature you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature,Planeswalker,Battle`, `Creature.OppCtrl`, `Creature.YouDontCtrl`, `Player,Planeswalker`

## `Earthbend`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 G T`, `4`, `2 W U B R G`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `8`, `X`, `Y`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBEarthbend`, `DBGainLife`, `DBImmediateTrig`, `DBPumpAll`, `DBPutCounter`, `DBSearch`, `DBUntap`

## `Effect`

TODO: Write documentation.

**Parameters:**
- `Abilities$`: TODO: Describe this parameter.
  Observed values: `ABMana`, `ABProtect`, `ABRiseToTop`, `DiscordCast`, `KarnPing`, `ObGainLife`, `PayUp`
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->Declare Attackers`, `BeginCombat->EndCombat`, `Declare Attackers`, `Upkeep`, `Upkeep->BeginCombat`, `Upkeep->Declare Attackers`, `Upkeep->Main1`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.Opponent`, `Player.Owner`
- `AddSVar$`: TODO: Describe this parameter.
  Observed values: `AE`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `BeginningOfOppTurn`, `Bribe`, `Burn`, `CantRegenerate`, `ChainVeil`, `Evasion`, `Fog`, `KeepOppCreatsLandsTapped`, `Main1`, `Main2`, `MakeUnblockable`, `NeedCreatures:3`, `Never`, `NoGain`, `NonCastCreature`, `PeaceTalks`, `Prevent`, `Pump`, `RedirectSpellDamageFromPlayer`, `RestrictBlocking`, `SecretTunnel`, `WillCastCreature`, `YawgmothsWill`
- `AINoRecursiveCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Permanent.withPhasing+YouCtrl`, `Snake`, `Vampire`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Sacrifice`
- `Boon$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`, `X`, `Y`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`, `OptionalCost`, `Threshold`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Excess`, `FatefulHour`, `TriggeredAttacker$Valid Card.powerLE2`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Imprinted`, `ParentTarget`, `Remembered`, `RememberedCard`, `Self`, `Targeted`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If CARDNAME was kicked,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `R`, `W`, `W U`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.inZoneBattlefield,Creature.inZoneBattlefield,Planeswalker.inZoneBattlefield`, `Card`, `Card,Emblem`, `Card.inZoneBattlefield`, `Card.inZoneExile`, `Card.inZoneStack`, `Card.Land`, `Card.nonLand`, `Card.powerLE2`, `Card.Red`, `Card.Self`, `Card.Self+PromisedGift`, `Card.SharesColorWith ChosenCard`, `Card.StrictlySelf`, `Card.wasCastFromGraveyard`, `Creature`, `Creature.attacking`, `Creature.Goblin`, `Creature.YouCtrl+powerGE4`, `Instant,Sorcery`, `Land`, `Player`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQ2`, `EQ5`, `GE1`, `GE10`, `GE7`, `LE5`, `M20`, `M21`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T`, `4 T`, `1`, `U`, `2 U`, `SubCounter<7/LOYALTY>`, `SubCounter<6/LOYALTY>`, `XMin1 X T`, `G U T`, `T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Exile a card from your hand:`, `Exile a face-down permanent you control face up:`, `Exile any number of historic cards from your graveyard with total mana value 30 or greater:`, `Grandeur — Discard another card named Oriss, Samite Guardian:`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `3`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `P1P1`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self`, `Targeted`, `You`
- `Description$`: TODO: Describe this parameter.
- `Duration$`: TODO: Describe this parameter.
  Observed values: `AsLongAsControl`, `AsLongAsInPlay`, `End of Turn`, `EndOfTurn`, `Permanent`, `ThisTurnAndNextTurn`, `UntilEndOfCombat`, `UntilEndOfCombatYourNextTurn`, `UntilEndOfTurn`, `UntilHostLeavesPlay`, `UntilHostLeavesPlayOrEndOfCombat`, `UntilHostLeavesPlayOrEOT`, `UntilStateBasedActionChecked`, `UntilTargetedUntaps`, `UntilTheEndOfYourNextTurn`, `UntilTheEndOfYourNextUntap`, `UntilUntaps`, `UntilYourNextEndStep`, `UntilYourNextTurn`, `UntilYourNextUpkeep`
- `EffectOwner$`: TODO: Describe this parameter.
  Observed values: `CardOwner`, `ImprintedOwner`, `Opponent`, `Player.IsRemembered`, `Player.Opponent`, `Remembered`, `RememberedController`, `RememberedOwner`, `RememberedOwner.Opponent`, `Targeted`, `TargetedController`, `TargetedOwner`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `You`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `TrigRemoveSelf`
- `ExileOnLost$`: TODO: Describe this parameter.
  Observed values: `True`
- `ExileOnMoved$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Exile,Stack`, `Graveyard`, `Graveyard,Exile`, `Graveyard,Stack`, `Stack`
- `FogetOnMoved$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetCounter$`: TODO: Describe this parameter.
  Observed values: `AWAKENING`, `BLAZE`, `BLIGHT`, `BOUNTY`, `DUTY`, `FEATHER`, `FLOOD`, `MANNEQUIN`, `MIRE`, `PARALYZATION`, `Shadow`, `SHIELD`, `VOW`
- `ForgetOnCast$`: TODO: Describe this parameter.
  Observed values: `Card.ChosenType+YouCtrl`, `Card.IsRemembered`, `Card.nonCreature+YouCtrl`, `Card.YouCtrl`, `Creature.Dragon+YouCtrl`, `Creature.faceDown+YouCtrl`, `Creature.Red+YouCtrl,Creature.Green+YouCtrl`, `Creature.YouCtrl`, `Dragon.YouCtrl`, `False`, `Giant.YouCtrl`, `Instant.YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Sorcery.YouCtrl`
- `ForgetOnMoved$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`, `Graveyard,Exile`, `Graveyard,Stack`, `Hand`, `Stack`, `True`
- `ForgetOnPhasedIn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `Image$`: TODO: Describe this parameter.
  Observed values: `emblem_1996_world_champion`, `emblem_ajani_adversary_of_tyrants`, `emblem_ajani_sleeper_agent`, `emblem_ajani_steadfast`, `emblem_arlinn_embraced_by_the_moon`, `emblem_basri_ket`, `emblem_chandra_roaring_flame`, `emblem_chandra_spark_hunter`, `emblem_chandra_torch_of_defiance`, `Emblem_daretti_scrap_savant`, `emblem_domri_chaos_bringer`, `emblem_domri_rade`, `Emblem_dovin_baan`, `emblem_ellywick_tumblestrum`, `emblem_elspeth_knight_errant`, `emblem_elspeth_suns_champion`, `emblem_garruk_apex_predator`, `emblem_garruk_caller_of_beasts`, `emblem_garruk_cursed_huntsman`, `emblem_garruk_unleashed`, `emblem_huatli_radiant_champion`, `emblem_jace_telepath_unbound`, `emblem_jace_unraveler_of_secrets`, `emblem_jaya_ballard`, `emblem_jaya_fiery_negotiator`, `emblem_kaito_bane_of_nightmares`, `emblem_kaito_cunning_infiltrator`, `emblem_kaito_shizuki`, `emblem_karn_living_legacy`, `emblem_kaya_the_inexorable`, `emblem_kiora_master_of_the_depths`, `emblem_koth_of_the_hammer`, `emblem_liliana_defiant_necromancer`, `emblem_liliana_of_the_dark_realms`, `emblem_liliana_the_last_hope`, `emblem_liliana_waker_of_the_dead`, `emblem_lukka_wayward_bonder`, `emblem_mordenkainen`, `emblem_mu_yanling_sky_dancer`, `emblem_narset_of_the_ancient_way`, `emblem_nissa_vital_force`, `emblem_nissa_who_shakes_the_world`, `emblem_ob_nixilis_of_the_black_oath`, `emblem_ob_nixilis_reignited`, `emblem_oko_shadowmoor_scion`, `emblem_professor_dellian_fel`, `emblem_ral`, `emblem_ral_crackling_wit`, `emblem_rowan_kenrith`, `emblem_sephiroth_one_winged_angel`, `emblem_serra_the_benevolent`, `emblem_sorin_lord_of_innistrad`, `emblem_tamiyo_field_researcher`, `emblem_tamiyo_seasoned_scholar`, `emblem_tamiyo_the_moon_sage`, `emblem_teferi_akosa_of_zhalfir`, `emblem_teferi_hero_of_dominaria`, `emblem_teferi_temporal_archmage`, `emblem_teferi_who_slows_the_sunset`, `emblem_teferis_talent`, `emblem_tezzeret_artifice_master`, `emblem_tezzeret_betrayer_of_flesh`, `emblem_tezzeret_cruel_captain`, `emblem_the_capitoline_triad`, `emblem_tibalt_cosmic_impostor`, `emblem_tyvar_kell`, `emblem_venser_the_sojourner`, `emblem_vivien_reid`, `emblem_vraska_golgari_queen`, `emblem_will_kenrith`, `emblem_wrenn_and_one`, `emblem_wrenn_and_realmbreaker`, `emblem_wrenn_and_seven`, `emblem_wrenn_and_six`, `emblem_zariel_archduke_of_avernus`
- `ImprintCards$`: TODO: Describe this parameter.
  Observed values: `AttachedBy Sacrificed`, `Enchanted`, `Imprinted`, `OriginalHost`, `OriginalHost.inZoneBattlefield`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredAttacker`, `Valid Creature.Horror+YouCtrl`
- `ImprintOnHost$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.YouOwn`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `R`
- `Name$`: TODO: Describe this parameter.
  Observed values: `Agyrem's Effect — None Can Attack You`, `Agyrem's Effect — Nonwhite Creatures Rebirthed`, `Agyrem's Effect — White Creatures Feign Death`, `Aladdin's Wish`, `Alora, Cheerful Scout's Perpetual Effect`, `Alora, Cheerful Thief's Perpetual Effect`, `ApproachingSuns`, `Avacyn, Guardian Angel Effect — Protect Creature`, `Avacyn, Guardian Angel's Effect — Protect Player`, `Awe Struck`, `Chandra, Dressed to Kill's Effect — +1 May Play`, `Chandra, Dressed to Kill's Effect — Ultimate May Play`, `Chandra, Heart of Fire's Effect — +1 May Play`, `Chandra, Heart of Fire's Effect — Ultimate May Cast`, `Coolness Badge`, `Damaged by Gollum, Obsessed Stalker`, `Dark Power Scheme`, `Davriel, Soul Broker's Effect — +1 Attack Tax`, `Desperate Gambit's Effect — Lost The Flip`, `Desperate Gambit's Effect — Won The Flip`, `Elite Guard Escort`, `Emblem — 1996 World Champion`, `Emblem — Ajani Steadfast`, `Emblem — Ajani, Adversary of Tyrants`, `Emblem — Ajani, Sleeper Agent`, `Emblem — Arlinn, Embraced by the Moon`, `Emblem — Basri Ket`, `Emblem — Chandra, Awakened Inferno`, `Emblem — Chandra, Dressed to Kill`, `Emblem — Chandra, Roaring Flame`, `Emblem — Chandra, Spark Hunter`, `Emblem — Chandra, Torch of Defiance`, `Emblem — Dack Fayden`, `Emblem — Daretti, Scrap Savant`, `Emblem — Davriel, Soul Broker (Condition 5)`, `Emblem — Davriel, Soul Broker (Condition 6)`, `Emblem — Davriel, Soul Broker (Condition 7)`, `Emblem — Davriel, Soul Broker (Condition 8)`, `Emblem — Davriel, Soul Broker (Offer 5)`, `Emblem — Davriel, Soul Broker (Offer 6)`, `Emblem — Davriel, Soul Broker (Offer 7)`, `Emblem — Davriel, Soul Broker (Offer 8)`, `Emblem — Domri Rade`, `Emblem — Domri, Chaos Bringer`, `Emblem — Dovin Baan`, `Emblem — Ellywick Tumblestrum`, `Emblem — Elspeth, Knight-Errant`, `Emblem — Elspeth, Sun's Champion`, `Emblem — Ersta, Friend to All`, `Emblem — Garruk, Apex Predator`, `Emblem — Garruk, Caller of Beasts`, `Emblem — Garruk, Cursed Huntsman`, `Emblem — Garruk, Unleashed`, `Emblem — Gideon of the Trials`, `Emblem — Gideon, Ally of Zendikar`, `Emblem — Huatli, Radiant Champion`, `Emblem — Inzerva, Master of Insights`, `Emblem — Jace, Telepath Unbound`, `Emblem — Jace, Unraveler of Secrets`, `Emblem — Jaya Ballard`, `Emblem — Jaya, Fiery Negotiator`, `Emblem — Kaito Shizuki`, `Emblem — Kaito, Bane of Nightmares`, `Emblem — Kaito, Cunning Infiltrator`, `Emblem — Karlov's Crossbow`, `Emblem — Karn, Living Legacy`, `Emblem — Kaya the Inexorable`, `Emblem — Kiora, Master of the Depths`, `Emblem — Kiora, the Crashing Wave`, `Emblem — Koth of the Hammer`, `Emblem — Koth, Fire of Resistance`, `Emblem — Liliana Of The Dark Realms`, `Emblem — Liliana, Defiant Necromancer`, `Emblem — Liliana, the Last Hope`, `Emblem — Liliana, Waker of the Dead`, `Emblem — Lolth, Spider Queen`, `Emblem — Lukka, Wayward Bonder`, `Emblem — Mordenkainen`, `Emblem — Mu Yanling, Sky Dancer`, `Emblem — Narset of the Ancient Way`, `Emblem — Narset Transcendent`, `Emblem — Nissa, Vital Force`, `Emblem — Nissa, Who Shakes the World`, `Emblem — Ob Nixilis of the Black Oath`, `Emblem — Ob Nixilis Reignited`, `Emblem — Oko, Shadowmoor Scion`, `Emblem — Professor Dellian Fel`, `Emblem — Puresteel Angel`, `Emblem — Ral`, `Emblem — Ral, Crackling Wit`, `Emblem — Rowan Kenrith`, `Emblem — Rowan, Scholar of Sparks`, `Emblem — Saheeli, Filigree Master`, `Emblem — Sarkhan, the Dragonspeaker`, `Emblem — Sephiroth, One-Winged Angel`, `Emblem — Serra the Benevolent`, `Emblem — Sorin, Lord of Innistrad`, `Emblem — Sorin, Solemn Visitor`, `Emblem — Tamiyo, Field Researcher`, `Emblem — Tamiyo, Seasoned Scholar`, `Emblem — Tamiyo, the Moon Sage`, `Emblem — Teferi Akosa of Zhalfir`, `Emblem — Teferi, Hero of Dominaria`, `Emblem — Teferi, Temporal Archmage`, `Emblem — Teferi, Who Slows the Sunset`, `Emblem — Teyo, Aegis Adept`, `Emblem — Tezzeret the Schemer`, `Emblem — Tezzeret, Artifice Master`, `Emblem — Tezzeret, Betrayer of Flesh`, `Emblem — Tezzeret, Cruel Captain`, `Emblem — The Capitoline Triad`, `Emblem — Tibalt, Cosmic Impostor`, `Emblem — Tyvar Kell`, `Emblem — Urza, Academy Headmaster (12U)`, `Emblem — Urza, Academy Headmaster (13U)`, `Emblem — Urza, Academy Headmaster (2U)`, `Emblem — Urza, Academy Headmaster (5M)`, `Emblem — Urza, Academy Headmaster (7U)`, `Emblem — Urza, Academy Headmaster (8U)`, `Emblem — Venser, the Sojourner`, `Emblem — Vivien Reid`, `Emblem — Vraska, Golgari Queen`, `Emblem — Will Kenrith`, `Emblem — Wrenn and One`, `Emblem — Wrenn and Realmbreaker`, `Emblem — Wrenn and Seven`, `Emblem — Wrenn and Six`, `Emblem — Zariel, Archduke of Avernus`, `en-Kor Redirection`, `Enter the Unknown's Effect — Exploration`, `Escape to the Wilds's Effect — Exploration`, `Escape to the Wilds's Effect — May Play`, `Gale, Storm Conduit's Perpetual Effect`, `Havengul Lich's Delayed Trigger`, `Imaginary Threats's Effect — Must Attack`, `Imaginary Threats's Effect — Stunned`, `Imoen, Wise Trickster's Effect — Exploration`, `Impulsive Maneuvers's Effect — Lost The Flip`, `Impulsive Maneuvers's Effect — Won The Flip`, `Intet, the Dreamer's Effect — May Look`, `Intet, the Dreamer's Effect — May Play`, `Kiora, the Crashing Wave's Effect — Exploration`, `Know Evil's Effect — No Attacking`, `Know Evil's Effect — No Creatures`, `Know Evil's Effect — No Spells`, `Moonhold's Effect — No Creatures`, `Moonhold's Effect — No Lands`, `Orim's Chant's Effect — No Attacking`, `Orim's Chant's Effect — No Spells`, `Personal Incarnation Redirection`, `Pieces Coming Together`, `Plant Beans's Effect — Exploration`, `Plots Scheme`, `Raging River Left`, `Raging River Right`, `Rasaad, Radiant Monk's Perpetual Effect`, `Redirection Ward`, `Rowan Kenrith's Effect — Taunting`, `Shriveling Rot's Effect — Deadly Toxin`, `Shriveling Rot's Effect — Stench of Death`, `Silent Assassin's Effect — Tracking...`, `Sword of Forge and Frontier's Effect — Exploration`, `Tamiyo, Field Researcher's Effect — Curiosity`, `This World Belongs to Me's Effect — Exploration`, `Urban Evolution's Effect — Exploration`, `Viconia, Disciple of Arcana's Perpetual Effect`, `Viconia, Disciple of Blood's Perpetual Effect`, `Viconia, Disciple of Rebirth's Perpetual Effect`, `Viconia, Disciple of Strength's Perpetual Effect`, `Viconia, Disciple of Violence's Perpetual Effect`, `Wandering Effect`, `Wilson, Ardent Bear's Perpetual Effect`, `Wilson, Fearsome Bear's Perpetual Effect`, `Wilson, Majestic Bear's Perpetual Effect`, `Wilson, Subtle Bear's Perpetual Effect`, `Wilson, Urbane Bear's Perpetual Effect`, `Zhalfirin Redirection`
- `NoteCounterDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `OneOff$`: TODO: Describe this parameter.
  Observed values: `True`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `3`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Affirmative —`, `Cunning Action —`, `Formidable —`, `Gift of Chaos —`, `Jolly Gutpipes —`, `Play Arcanum`, `Threshold —`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `PumpZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberLKI$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `Caster & Valid Permanent.OppCtrl`, `ChosenCard`, `ChosenCardController`, `ChosenPlayer & Targeted`, `ChosenPlayer & You`, `DefendingPlayer`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `DelayTriggerRememberedLKI & Self`, `Enchanted`, `Equipped`, `ExiledCards`, `ExiledCards.Other`, `Imprinted`, `ParentTarget`, `ParentTarget & Targeted`, `Player.IsRemembered`, `Player.Opponent+IsRemembered`, `Remembered`, `Remembered.Creature`, `Remembered.YouOwn`, `RememberedCard`, `RememberedFirst`, `RememberedLKI`, `RememberedLKI & RememberedOwner`, `ReplacedCard`, `Self`, `Self & Targeted`, `ShieldEffectTarget`, `Targeted`, `Targeted & Self`, `Targeted & TargetedController`, `TargetedController`, `TargetedOrController`, `TargetedPlayer`, `TargetedPlayer & RememberedCard`, `TargetedPlayer & ThisTargetedCard`, `TargetedSource`, `ThisTargetedCard`, `ThisTargetedCard & ThisTargetedPlayer`, `ThisTargetedPlayer`, `TriggeredActivator`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `TriggeredAttackers`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredDefendingPlayer`, `TriggeredObjectLKICopy`, `TriggeredPlayer`, `TriggeredTarget`, `TriggeredTargetLKICopy`, `Valid Artifact.Other`, `Valid Aura.AttachedTo Targeted`, `Valid Creature.ActivePlayerCtrl+nonWall`, `Valid Creature.blockedBySource,Creature.blockingSource`, `Valid Creature.OppCtrl`, `Valid Land.YouCtrl`, `Valid Permanent.YouCtrl+HasCounters`, `ValidExile Card.ExiledWithSource`, `ValidExile Card.ExiledWithSource+nonLand`, `You`, `You & Targeted`
- `RememberSpell$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ReplacementEffects$`: TODO: Describe this parameter.
  Observed values: `AntiMagic`, `AntiMagic,ETBCounters`, `BlankIsChaos`, `BraceReplace`, `Bribe`, `CantBeCountered`, `CantTap`, `CaromDamage`, `ChannelHarmRep`, `CountersAdded`, `Curse`, `Damage`, `DamageEvent`, `DamageShielded`, `Dazzle`, `DBBoostLoyalty`, `DBCantLose,DBCantWin`, `DBPrevent`, `DBRemove`, `DBYouCantLose,DBOppCantWin`, `DBYouCantLose,DBOppCantWin,SelflessDamage`, `DeathRep`, `DmgEvent`, `DMPrevent`, `DontUntap`, `DoubleDamageEvent`, `DrawReplace`, `EffRMoved`, `EnKor`, `EntersAsCreature`, `EqualEvent`, `ETBAddCounter`, `ETBAddCounterTapped`, `ETBCounters`, `ETBCreat`, `ETBCreatPlans`, `ETBPrevent`, `EventDamageDone`, `EventDraw`, `EventGuerrillasDamageDone`, `EventLossDamageDone`, `EventWinDamageDone`, `ExtraETBCounter`, `FDRep`, `FlameOfKeldDamageEvent`, `FuryCombatEvent`, `GainLifeEvent`, `GeneralDamage`, `GraceDamage`, `GraveExileToLibrary`, `GraveToExile`, `HarvestReplacement`, `HazduhrDamage`, `InsultDamageEvent`, `JayaReplace`, `LandETB`, `LandsTapped`, `LoseReplace`, `ManeuverDamage`, `MartyrDamage`, `MoltenRealm`, `MoreDamage`, `MoveToExileReplace`, `MoveToHandReplace`, `OppCreatEnters`, `OverblazeEvent`, `PlotPower`, `PreventArtifact`, `PreventColorless`, `PreventDamage`, `PreventDmg`, `PreventDogDamage`, `Protect`, `QuarumReplacement`, `RaziaDamage`, `RDeclareBlocker`, `RDoubleDamage`, `REBosiumStrip`, `ReDamage`, `RedirectDamage`, `REExileOnResolve`, `ReMoved`, `RepCurse`, `RepDamage`, `RepDmg`, `RepETB`, `ReplaceChosen`, `ReplaceColorless`, `ReplaceEnter`, `ReplaceETB`, `ReplaceExile`, `ReplaceGrave`, `ReplaceGraveyard`, `ReplacePlaneswalk`, `ReplaceU`, `REQuintorius`, `RGideon`, `RigRoll`, `RPrevent`, `RPrevent1`, `RPrevent1,RPrevent2`, `RPrevent2`, `RPreventCreature`, `RPreventDamage`, `RPreventNextFromCreature`, `RPreventNextFromSource`, `RPreventNextFromSourceSB`, `RPreventPlayer`, `RuneswordRep`, `RUntap`, `SavingGraceDamage`, `SelfDamage`, `SelflessDamage`, `Stagger`, `Static`, `StaticReplace`, `StrikeWithAwe`, `STWorship`, `TapLockETBTapped`, `TokenReplace`, `TripleCombatDamage`, `WardDamage`, `ZealotDamage`, `Zealous`, `Zhalfirin`
- `SetChosenNumber$`: TODO: Describe this parameter.
  Observed values: `Count$ValidExile Card.YouOwn+IsRemembered$CardManaCost`, `Excess`, `NotedPower`, `X`, `Y`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `Stackable$`: TODO: Describe this parameter.
  Observed values: `False`
- `StackDescription$`: TODO: Describe this parameter.
- `StaticAbilities$`: TODO: Describe this parameter.
  Observed values: `AddAttackStatic`, `AddP2Ab`, `AllUnblockable`, `Animate`, `AttackChosen`, `AttackEach,AttackOther`, `AttackTax`, `AttackThisTurn`, `BlightStatic`, `BlockRestrict`, `BloomingLand`, `CadenceStaticAb`, `CanAttack`, `CanAttack,CombatDamageToughness`, `CantActivate`, `CantAttack`, `CantBeBlockedPow`, `CantBeCast`, `CantBeCast,CantAttack`, `CantBeCast,KWShow`, `CantBeCastCreats`, `CantBeCastNonCreats`, `CantBlock`, `CantBlockBy`, `CantBlockEven`, `CantBlockOdd`, `CantCast`, `CantGainLife`, `CantPhaseIn`, `CantPhaseOut`, `CantSac`, `CantSac,CantAttack`, `CantTarget`, `CascadeInstant`, `CascadeSorcery`, `CFReduceCost`, `ChangeLandType`, `CheapParts`, `CombatDamageToughness`, `Convert`, `CostBLess`, `CostBMore`, `CRPlay`, `DBCantAttack,DBCantBlockBy`, `DBCantAttackBlock`, `DBCantBeActivated`, `DBCantBlock`, `DBCantPutCounterCreature`, `DBCantPutCounterPlayer`, `DBCantStatic`, `DBLimitMana`, `DBPlay`, `DeclareCombatants`, `DontUntap`, `EffModeCantBlockBy`, `EffPlay`, `EffSModeContinuous`, `ElkinPlay`, `EmblemArtifactPump,ReduceCost`, `Enchant`, `Energybend`, `Exploration`, `FasterThanLime`, `FDManaConvertion`, `ForbidAttack`, `ForceAttack,ForbidAttack`, `FountainStatic`, `FreeCast`, `GainControl`, `GiveFlash`, `GrantAffinity`, `GrantCascade`, `GrantConvoke`, `GrantImprovise`, `GrantStorm`, `HBReduceCost`, `InstantPlaneswalkers`, `IsGoaded`, `IslandRetreat`, `JourneyOfDis`, `KWAnimateAll`, `KWPump`, `KWPump2`, `Land,MayPlay`, `LandPlay`, `LoyaltyAbs`, `MannequinStatic`, `MathasStatic`, `MayCast`, `MayCastForetell`, `MayCastGrave`, `MayLook`, `MayLookAndPlay`, `MayLookFaceDown`, `MayPlay`, `MayPlay,CostsMore`, `MayPlay,ManaConvert`, `MayPlay,RaiseCost`, `MimeomancerStatic`, `MinMaxBlocked`, `MischiefPlay`, `MustAttack`, `MustAttack,DBCantBeActivated`, `MustAttack,MustBlock`, `MustAttack1,MustAttack2`, `MustBlock`, `MustBlock,KWPump`, `NoCombat`, `NoMorePoison`, `NoRegen`, `NoRegen,NoPrevent`, `NoRegenST`, `ObsidianStatic`, `Omniscience`, `OppCantBlock`, `OppCantCast`, `OppPerms`, `OwnerMayPlay`, `PermanentRecycle`, `PerpetualAbility`, `PerpetualDebuff`, `PerpetualDoubleStrike`, `PerpetualLifelink`, `PerpetualLoss`, `PerpetualMenace`, `PerpetualP1P1`, `PerpetualPump`, `PerpetualStatic`, `PerpetualUnblockable`, `Play`, `Play1`, `Play2`, `PlayCr,PlayPl,PlayAr,PlayEn,PlayIn,PlaySo,PlayKi,PlayBa`, `PlayExile`, `PlayMoreLand`, `PlayOpp`, `PlaySideboard`, `PreventDmg`, `Pump`, `PumpStatic`, `PWTwice`, `QuickenStA`, `QuickSpell`, `RaiseCost`, `RalReduceCost`, `ReduceCost`, `ReduceCost,STPlay`, `ReduceHand`, `ReduceSPCost`, `RestrictAttackers,RestrictCasting`, `ScoutFlash`, `SectorBlock`, `ShadowStatic`, `SMayPlay,SReduceCost`, `SMayPlayLand`, `SNoCombatDamage`, `SReduceCost`, `ST7U`, `STArlinn`, `Static`, `Static,StaticTwo,StaticThree`, `StaticAllowAdapt`, `StaticBlock`, `StaticCantAttack`, `StaticMayLookAndPlay`, `StaticMayPlay`, `StaticPlay`, `StaticReduce`, `STaticReduce`, `STBlock`, `STBlock,DeclareCombatants`, `STBosiumStrip`, `STCanLookAtMayPlay`, `STCantAttack`, `STCantAttack,STCantTarget,STCantTargetPlayer`, `STCantAttack,STMustAttack`, `STCantBeActivated`, `STCantBeCast`, `STCantBeCast,STCanPeek,STCanPlay`, `STCantBeCast,STCantBeActivated`, `STCantBeCast,STCantBeActivated,STHandRevealed,STCanPlay`, `STCantBeTarget`, `STCantBlockBy,STCantBlockByFrog`, `STCantCast`, `STCantCast,STCantPlayLand`, `STCantChange`, `STCantGain`, `STCantGain,STCantPrevent`, `STCantMonarch`, `STCantPlayCreats`, `STCantPlayLand`, `STCantPlayLand,STCantCastSpell,STTrance`, `STCantPrevent`, `STCantSearch`, `STCantTarget`, `STCommuned`, `STCoolness`, `STCurse`, `STDamage`, `STDomri`, `STDovin`, `STDraw`, `STFlash`, `STFlying`, `STGrinning`, `STHandSize`, `STIndestructible`, `STIndestructible8U`, `STJaya`, `STKeepLife`, `STLimitBlock`, `STLook`, `STLook,STPlay`, `STLookPlay`, `STLoseAB`, `STMayLookAt`, `STMayPlay`, `STNarset`, `STNinjaBoost`, `STNoDmg`, `StolenGoodsPlay`, `STOverrun`, `STPiracy`, `STPlay`, `StPlay`, `STPlay,NoLand,NoCast`, `STPlay,STAffinity`, `STPlay,STPlay2`, `STPlay2`, `STPlayWithoutCost`, `STPump`, `STPump5M`, `STReveal`, `STRevealHand`, `STSetPT`, `STSteal`, `STThieving`, `STTrample`, `STUnblockable`, `STVigilance`, `STVivien`, `STVoter`, `STWit`, `STWrenn`, `STYardCast`, `SusPlay`, `SwampBoost`, `TangleStatic`, `TempoCantAttack`, `TombStatic`, `Unblockable`, `UnlimitedHand`, `Unspent`, `UntapOppStep`, `VowStatic`, `WillReduceCost`, `WithFlash`, `YojimboCantAttack`, `YoursM1Pow`, `YoursP2Pow`, `ZombieCast`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CantAttackWhenKicked`, `CleanupName`, `CloakofConfusionDiscard`, `DBAnimate`, `DBBargained`, `DBBranch`, `DBCantAttackBlock`, `DBChange`, `DBChangeZone`, `DBCleanup`, `DBCleanupSB`, `DBClearChosen`, `DBClearRemembered`, `DBConnive`, `DBConvert`, `DBCopy`, `DBDamage`, `DBDealDamage`, `DBDefLeftRight`, `DBDefRightEffect`, `DBDelayedTrigger`, `DBDelayTrig`, `DBDelTrig`, `DBDmg`, `DBDraft`, `DBDraw`, `DBEffect`, `DBEffect2`, `DBEffect3`, `DBEffectBis`, `DBEndCombatPhase`, `DBExile`, `DBExileSelf`, `DBForget`, `DBGainLife`, `DBGoad`, `DBImmediateTrigger`, `DBLearn`, `DBLose`, `DBLoseLife`, `DBMana`, `DBNoCombatDamage`, `DBPlaneswalk`, `DBPlay`, `DBProliferate`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBResetSVar`, `DBRestRandomOrder`, `DBReturn`, `DBScry`, `DBSorceryEffect`, `DBTap`, `DBToken`, `DBToken13U`, `DBTreasure`, `DBUntap`, `DBUnTapAll`, `DBVenture`, `DelTrig`, `DelTrigBoth`, `DelTrigFriend`, `DelTrigReturn`, `DelTrigSlowtrip`, `DestroyPacifist`, `ExileSelf`, `PutCounter`, `PWAway`, `TrigEffect2`, `TrigEffect3`, `WPaid`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE8`
- `SVars$`: TODO: Describe this parameter.
  Observed values: `LukkaDmg`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `NHand`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `2`, `X`
- `TargetsWithSameCreatureType$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`, `Stack`
- `Triggers$`: TODO: Describe this parameter.
  Observed values: `ActivateTrig`, `ArtifactDraw`, `Attack`, `AttackerBlocked,Blocks`, `AttackTrig`, `AttackTrigger`, `BODTrig,EOTTrig`, `Boon`, `BOTTrig`, `Cast`, `CastSpell`, `CastTrig`, `CastTrigger`, `ChangesZone`, `ChangeZoneTrig`, `CombatTrig`, `ComeBack`, `CopyAbility`, `CopySpell`, `CopySpellCast`, `CreatureEnchantmentETB`, `CreatureEntered`, `CreatureETB`, `CreatureSpell`, `DalkovanAttack`, `Damage`, `DamageDraw`, `DamageTrig`, `DamageTrigger`, `DarkPower`, `DealCombatDamagePlayer`, `DelTrig`, `DiesTrig`, `DieTrigger`, `DrawGainTrig`, `DrawOppStep`, `DrawTrig`, `DrawTrig,DrawTrigLand`, `DTCast`, `DuskmantleCardToGrave`, `EffPhase`, `EffT`, `EndLose`, `EndStepTrig`, `EOTTrig`, `ExileEff`, `ExileEffect`, `ExileMe`, `ExileSelf`, `FlameTrigger`, `GainLife`, `HatchlingCast`, `HuatliCreatureETB`, `InstantSorceryCast`, `IslandTrigger`, `LeavesBattlefield`, `LeavesPlay,Untap`, `LifeGainTrigger`, `LostTheGuarded`, `LostTheMount,LostTheTarget`, `LukkaCreatureETB`, `MerfolkETB`, `MogCopy`, `MoongloveTrigger`, `MustAttackTrig`, `NamedCardCast`, `NextSpell`, `OutOfSight`, `PlaneswalkTrig`, `Play1,Play2`, `PoisonTrig`, `PureDiscarded`, `RemoveEffect`, `RestoreSight`, `Sacrifice`, `SacTrig`, `SpellCast`, `SpellCastTrig`, `SpellCastTrig,LandPlayedTrig`, `StaticCast`, `StaticRem`, `STDamage`, `StillTopCheck,ShuffleCheck`, `STShip`, `STZariel`, `SwampTrigger`, `TamiyoCardToGrave`, `TargetMoved`, `TAttack`, `TPWAway`, `TRCast`, `Trig`, `Trig1`, `Trig2`, `TrigAbandoned`, `TrigAbilityActivated`, `TrigAttack`, `TrigAttack10`, `TrigAttackerUnblocked`, `TrigAttacks`, `TrigAttackYou`, `TrigBlock`, `TrigBlocked`, `TrigBlocking`, `TrigBounce`, `TrigCastSpell`, `TrigChangeController`, `TrigChangesZone`, `TrigComeBack`, `TrigCounter`, `TrigCounters`, `TrigCradle`, `TrigDam,TrigLeave`, `TrigDamage`, `TrigDamageDone`, `TrigDealtDmg`, `TrigDelay,TrigExile`, `TrigDestroy`, `TrigDie`, `TrigDies`, `TrigDrain`, `TrigDraw`, `TrigDraw,TrigUntap,TrigZone`, `TrigDrawDiscard`, `TrigEOT`, `TrigEOT2`, `TrigExile`, `TrigExile,TrigDie`, `TrigExile,TrigSac`, `TrigFight`, `TrigFight13U`, `TrigForget`, `TriggerAttack`, `TriggerAttacks`, `TriggerCastDoM`, `TriggerCastDoM,TriggerLandPlayed`, `TriggerClearAdapt`, `TriggerDamage`, `TrigHostLeaves`, `TrigLandPlayed,TrigCast`, `TrigLeavePlay`, `TrigLeavesBattlefield`, `TrigLoseLife`, `TrigMana`, `TrigMill`, `TrigOpenScry`, `TrigPhageCreature`, `TrigPhageDestroy`, `TrigPhase`, `TrigPlaneswalk`, `TrigRamp`, `TrigRemove`, `TrigReturn,TrigDuration`, `TrigSacGuard`, `TrigSearch`, `TrigSetLife`, `TrigSpellCast`, `TrigSpellCast12U`, `TrigTapForMana`, `TrigTaps`, `TrigToken`, `TrigUntaps,TrigChangesZone`, `TrigUpkeep`, `TrigVisit,RemoveEffect`, `TrigWin`, `TRSpellCast`, `Upkeep`, `UpkeepLoseTrig`, `UpkeepRemove`, `UpkeepTrig`, `VizkopaMageTrig`, `WayPump`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `Unique$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `WillAttack`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `4`, `Draw<1/Player.TriggeredPlayer>`, `ExileFromGrave<1/Card>`, `ExileFromGrave<3/Card>`, `R`, `X`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `EnchantedPlayer`, `Player`, `TriggeredActivator`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`, `Artifact.YouOwn`, `Beeble`, `Card`, `Card.Artifact+OppCtrl`, `Card.Detective`, `Creature`, `Creature,Planeswalker,Player`, `Creature,Player`, `Creature,Player,Planeswalker`, `Creature.Artifact`, `Creature.attacking`, `Creature.attacking+Other`, `Creature.attacking+powerLE3`, `Creature.attacking+unblocked`, `Creature.attacking+withFlying`, `Creature.attacking,Creature.blocking`, `Creature.blocked`, `Creature.blocking`, `Creature.ControlledBy TriggeredPlayer`, `Creature.IsRemembered+ExiledWithSource`, `Creature.Legendary`, `Creature.Legendary+Other`, `Creature.Legendary+YouCtrl`, `Creature.Merfolk`, `Creature.Merfolk+tapped,Creature.Kithkin+tapped`, `Creature.MultiColor`, `Creature.Ninja`, `Creature.nonHuman+Other+attacking`, `Creature.nonLegendary`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Other+attacking`, `Creature.Other+counters_GE1_P1P1`, `Creature.Other+powerLE2`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl+powerLE2`, `Creature.powerGE5`, `Creature.powerLE2`, `Creature.powerLE2+YouCtrl`, `Creature.powerLE3`, `Creature.powerLEX`, `Creature.tapped`, `Creature.token`, `Creature.Wall`, `Creature.White`, `Creature.withDefender`, `Creature.withoutFirst Strike+withoutDouble Strike+withoutVigilance`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Creature.YouOwn`, `Creature.Zombie+YouOwn`, `Enchantment.YouCtrl`, `Enchantment.YouOwn`, `Frog.YouCtrl`, `Goblin,Orc,Pirate`, `Instant,Sorcery`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouOwn,Sorcery.YouOwn`, `Land`, `Merfolk`, `Ninja`, `Ninja,Turtle`, `Opponent`, `Opponent,Planeswalker`, `Permanent`, `Permanent.nonLand`, `Permanent.nonLand+OppCtrl`, `Permanent.Snow+YouCtrl`, `Plains`, `Player`, `Player,Planeswalker`, `Player.wasDealtCombatDamageThisTurnBySource`, `Sorcery`

## `EndCombatPhase`

TODO: Write documentation.

**Parameters:**
- `SpellDescription$`: TODO: Describe this parameter.

## `EndTurn`

TODO: Write documentation.

**Parameters:**
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `1 T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ActivePlayer`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DelayedLoss`

## `Endure`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 W`, `X B T PayLife<X>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardLKICopy`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `X`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.

## `ExchangeControl`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep->Main1,Main2->Cleanup`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `PowerStruggle`, `TrigTwoTargets`
- `CantFizzle$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `5`, `T`, `5 U`, `2 U U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Remembered`, `Self`, `TriggeredCard`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberExchanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanCreature`, `DBCleanup`, `DBDestroyAll`, `DBDraw`, `DBSacSelf`, `Energy`, `TrigImmediateTrig`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `2`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `NonTriggeredCardController`, `Player.OpponentOf TriggeredPlayer`
- `TargetsWithDifferentControllers$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithRelatedProperty$`: TODO: Describe this parameter.
  Observed values: `LECMC`, `LEPower`
- `TargetsWithSameCardType$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithSharedCardType$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `TriggeredCard`
- `TargetsWithSharedTypes$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature`, `Artifact,Creature,Land`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature,Land`, `Artifact.OppCtrl,Creature.OppCtrl`, `Artifact.Other`, `Artifact.YouDontCtrl,Creature.YouDontCtrl`, `Creature`, `Creature.ControlledBy Player.wasDealtCombatDamageThisCombatBy ParentTarget`, `Creature.nonLegendary`, `Creature.OppCtrl`, `Creature.OppCtrl+powerLE3`, `Creature.Other`, `Creature.YouDontCtrl`, `Enchantment`, `Land`, `Land.OppCtrl`, `Permanent`, `Permanent.nonBasic+nonCreature`, `Permanent.nonLand`, `Permanent.OppCtrl`, `Permanent.OppCtrl+nonLand`, `Permanent.YouDontCtrl+YouDontOwn`

## `ExchangeControlVariant`

TODO: Write documentation.

**Parameters:**
- `SpellDescription$`: TODO: Describe this parameter.
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `ExchangeLife`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE5`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T Sac<1/CARDNAME>`, `6 T`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberDifference$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberOwnLoss$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDraw`, `DBToken`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `ExchangeLifeVariant`

TODO: Write documentation.

**Parameters:**
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.StrictlySelf`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4`, `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `Power`, `Toughness`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `ExchangePower`

TODO: Write documentation.

**Parameters:**
- `BasePower$`: TODO: Describe this parameter.
  Observed values: `True`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Perpetual`, `UntilEndOfCombat`
- `SpellDescription$`: TODO: Describe this parameter.
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.blockedBySource`

## `ExchangeTextBox`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self & ChosenCard`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `AsLongAsInPlay`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`

## `ExchangeZone`

TODO: Write documentation.

**Parameters:**
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `Object$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`
- `StackDescription$`: TODO: Describe this parameter.
- `ValidExchange$`: TODO: Describe this parameter.
  Observed values: `Card.TopLibrary`
- `Zone1$`: TODO: Describe this parameter.
  Observed values: `Ante`
- `Zone2$`: TODO: Describe this parameter.
  Observed values: `Library`

## `Explore`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Aristocrat`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 Sac<1/Creature.Other/another creature>`, `1 T`, `2 G`, `1 Discard<1/Card>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `ReplacedCard`, `Targeted`, `TriggeredCardLKICopy`, `Valid Creature.Merfolk+YouCtrl`
- `Num$`: TODO: Describe this parameter.
  Observed values: `2`, `X`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBClone`, `DBDestroyAll`, `TrigEffect`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.CrewedThisTurn`, `Creature.Merfolk+YouCtrl`, `Creature.YouCtrl`

## `Fight`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `ChosenAsTgt`, `FightSub`, `Grothama`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `NumFighters`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2`, `2 R T`, `R T`, `1 Sac<1/Aura.Attached>`, `1 B G`, `T`, `1`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `DelayTriggerRemembered`, `Enchanted`, `Imprinted & Remembered`, `ParentTarget`, `Remembered`, `Remembered & Self`, `Self`, `Self & TriggeredTarget`, `Targeted`, `TriggeredAttackerLKICopy & OriginalHost`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredTargetLKICopy`
- `ExcessSVar$`: TODO: Describe this parameter.
  Observed values: `Excess`
- `ExcessSVarCondition$`: TODO: Describe this parameter.
  Observed values: `Creature.targetedBy+OppCtrl`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceDyingDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `ThisTargetedCard`
- `ReplaceDyingExiledWith$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCopy`, `DBDelayedTrigger`, `DBEffect`, `DBImmediateTrig`, `DBMana`, `DBPump`, `DBToken`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `2`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithoutSameCreatureType$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `creature an opponent controls`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.blocking`, `Creature.ControlledBy NextOpponentToYourLeft`, `Creature.ControlledBy Spawner>TriggeredDefendingPlayer`, `Creature.DefenderCtrl`, `Creature.namedFenric`, `Creature.nonWerewolf+YouDontCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl+Green`, `Creature.Other`, `Creature.Other+ControlledBy DelayTriggerRemembered`, `Creature.token`, `Creature.withFlying+YouDontCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Creature.YouDontCtrl`, `Creature.YouDontCtrl+SharesCMCWith TriggeredCard`, `Zombie.OppCtrl`

## `FlipCoin`

TODO: Write documentation.

**Parameters:**
- `ActivationAfterBlockers$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Blockers->EndCombat`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `Bangchuckers`, `KillOrcs`, `Never`, `PhaseOut`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `5`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `1 Sac<1/CARDNAME>`, `Sac<1/Artifact>`, `0`, `R T`, `Sac<1/CARDNAME>`, `{T} Sac<1/CARDNAME/this artifact>`, `1`, `PayEnergy<2>`, `SubCounter<7/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `Flipper$`: TODO: Describe this parameter.
  Observed values: `Player`, `Remembered`, `TriggeredActivator`
- `FlipUntilYouLose$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `HeadsSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddTurn`, `DBAddTurn19U`, `DBAttacker`, `DBCopyPermanent`, `DBCopyPermanent17`, `DBHeadsPump`, `DBSkipTurn`, `OddCounter`
- `InstantSpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `LoseSubAbility$`: TODO: Describe this parameter.
  Observed values: `ChaoticStrikeDraw`, `ChooseOpp`, `CounterIt`, `CreateEffect`, `CreateLossEffect`, `DamageIt`, `DBBounce`, `DBChange`, `DBControl`, `DBCounter`, `DBDamage`, `DBDamageSelf`, `DBDamageYou`, `DBDealDamage`, `DBDestroyAll`, `DBDestroyBig`, `DBDraw`, `DBGiveControl`, `DBImmediateTrigDamage`, `DBPumpMinus`, `DBRemoveCounter`, `DBRemoveFromCombat`, `DBSacrifice`, `DBSacSelf`, `DelTrigSlowtrip`, `DestroyImprinted`, `DestroyYours`, `DmgSelf`, `GainLifeOpp`, `IncrementLoss`, `SacAttackers`, `YouLoseGame`
- `NoCall$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberLoser$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberNumber$`: TODO: Describe this parameter.
  Observed values: `Wins`
- `RememberResult$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Assassination`, `DBAdd0`, `DBCleanup`, `DBEffect`, `DoubleLifeStake`
- `TailsSubAbility$`: TODO: Describe this parameter.
  Observed values: `ClashTails`, `DBDefender`, `DBRememberCreature`, `DBTailsPump`, `OddCopy`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`, `Artifact`, `Artifact.YouCtrl+IsRemembered`, `Card`, `Creature`, `Creature.blockingEquipped`, `Creature.Orc`, `Instant,Sorcery`, `Opponent`, `Opponent,Planeswalker`
- `WinSubAbility$`: TODO: Describe this parameter.
  Observed values: `AleatoryPump`, `ChaoticStrikePump`, `CreateWinEffect`, `DBAddCounter`, `DBAddTurn`, `DBCopies`, `DBCopy`, `DBDamage`, `DBDamageAll`, `DBDamageOpp`, `DBDamageTarget`, `DBDestroy`, `DBDestroyAll`, `DBDestroySmall`, `DBDraw`, `DBExile`, `DBImmediateTrigDamageCopy`, `DBMana`, `DBPhase`, `DBPreventDmg`, `DBPump`, `DBPumpPlus`, `DBPutCounter`, `DBReturn`, `DBSac`, `DBToken`, `DBTransform`, `DestroyOpp`, `DestroyRemembered`, `ExileIt`, `GainControl`, `GainLifeYou`, `IncrementFlips`, `IncrementWins`, `OppLoseGame`, `PWAway`, `SacBlockers`, `TSGainLife`

## `FlipOntoBattlefield`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DamageCreatures`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 T`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDamageTouched`, `DBDestroyTouched`

## `Fog`

TODO: Write documentation.

**Parameters:**
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep->Declare Blockers`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `SeriousDamage`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `OptionalCost`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `W`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `False`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `G W U T`, `G T Discard<1/Card>`, `Sac<1/Mountain.Snow/snow Mountain>`, `Sac<1/CARDNAME>`, `W Sac<1/Soldier>`, `1 SubCounter<1/P1P1>`, `SubCounter<3/SPORE>`, `2 Sac<1/Land.Snow/snow land>`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `BatwingRepeat`, `DBClash`, `DBEffect`, `DBGainLife`, `DBPumpAll`, `DBRepeatLook`, `DBTapAll`

## `GainControl`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Main2->Cleanup`
- `AddKWs$`: TODO: Describe this parameter.
  Observed values: `Haste`, `Haste & Flying`, `Haste & Menace`, `Haste & Myriad`, `Haste & Trample & Annihilator:2`, `Lifelink & Haste`, `Trample & Haste & Annihilator:1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DonateTargetPerm`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Creature.enchanted`
- `AITgtsStrict$`: TODO: Describe this parameter.
  Observed values: `True`
- `AllValid$`: TODO: Describe this parameter.
  Observed values: `Artifact.ControlledBy Targeted,Creature.ControlledBy Targeted`, `Artifact.ControlledBy TriggeredTarget`, `Artifact.OppCtrl`, `Card.blockingSource`, `Card.IsCommander`, `Card.Self,Creature.YouCtrl+namedKobolds of Kher Keep`, `Creature`, `Creature.!IsCommander+cmcLE3`, `Creature.!IsRemembered+YouCtrl`, `Creature.ChosenType`, `Creature.IsGoaded,Creature.IsSuspected`, `Creature.powerGE4`, `Creature.powerLE3`, `Creature.TargetedPlayerCtrl`, `Dragon`, `Enchantment`, `Land.ControlledBy Targeted`, `Permanent.ChosenCard`, `Permanent.counters_GE1_CORRUPTION`, `Permanent.nonLand`, `Permanent.OppCtrl+nonLand`, `Permanent.StrictlyOther+YouCtrl`, `Permanent.YouOwn`, `Rat.token`, `Survivor`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Creature.RememberedPlayerCtrl`, `Land.ControlledBy TriggeredTarget+counters_GE1_CONTESTED`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a creature that player controls`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceController`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `M12Complete`, `X`, `Y`, `YourPeerGroup`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Ninja`, `Swamp`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GTY`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 R R T`, `SubCounter<3/LOYALTY>`, `SubCounter<11/LOYALTY>`, `T`, `3 R`, `tapXType<5/Vampire>`, `T Discard<1/Card>`, `2`, `SubCounter<1/KI>`, `U T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Tap seven untapped Druids you control:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttachedTo Targeted.Aura,Equipment`, `AttachedTo Targeted.Equipment`, `ChosenCard`, `CorrectedSelf`, `DelayTriggerRememberedLKI`, `Enchanted`, `Equipped`, `Imprinted`, `OriginalHost`, `Remembered`, `Remembered.Creature`, `ReplacedCard`, `Self`, `Targeted`, `TriggeredCardLKICopy`, `TriggeredSpellAbilityTargets`, `TriggeredTarget`, `TriggeredTargetLKICopy`
- `LoseControl$`: TODO: Describe this parameter.
  Observed values: `EndOfCombat`, `EOT`, `LeavesPlay`, `LeavesPlay,LoseControl`, `LoseControl,LeavesPlay`, `StaticCommandCheck`, `Untap,LeavesPlay`, `Untap,LeavesPlay,LoseControl`, `Untap,LeavesPlay,LoseControl,StaticCommandCheck`, `UntilSourceUnattached`, `UntilTheEndOfYourNextTurn`
- `NewController$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `ImprintedController`, `NextPlayerToYourRight`, `Opponent`, `ParentTarget`, `Player.Chosen`, `Player.withMostCardsInHand`, `Player.withMostLife`, `Player.withMostTypeCreatureOnly`, `Player.withMostTypeWizardOnly`, `Remembered`, `RememberedController`, `Targeted`, `TargetedController`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredAttackingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `You`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberControlled$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StaticCommandCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `StaticCommandSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GTX`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AddMana`, `Animate`, `ChompEquip`, `DBAnimate`, `DBAttach`, `DBAttack`, `DBCast`, `DBChangeText`, `DBChangeZone`, `DBCleanup`, `DBClearChosen`, `DBControlSpell`, `DBCopy`, `DBDamage`, `DBDelay`, `DBDelayTrig`, `DBDestroyAll`, `DBDraw`, `DBEffect`, `DBGainCtrlOpp`, `DBGoad`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBNoCombatDamage`, `DBNoUntap`, `DBPlaneswalk`, `DBPump`, `DBPutCounter`, `DBPutCounters`, `DBRepeatEach`, `DBReset`, `DBRoll`, `DBScry`, `DBSuspect`, `DBTap`, `DBToken`, `DBUntap`, `DBUntapAll`, `DelTrig`, `PutCounter`, `ReEnchant`, `RemCombat`, `TrigCounter`, `TrigTempt`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `TargetingPlayerControls$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `3`, `MaxTargets`, `OneEach`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `OneEach`, `X`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithControllerProperty$`: TODO: Describe this parameter.
  Observed values: `powerLECardsInGraveyard`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `PayEnergy<X>`, `PayLife<2>`, `R R`, `Sac<1/Land>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `TriggeredPlayer`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `Untap$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Enchantment`, `Artifact.cmcLEX`, `Artifact.ControlledBy TriggeredDefendingPlayer`, `Artifact.nonCreature`, `Artifact.OppCtrl`, `Artifact.OppCtrl+cmcLE4,Creature.OppCtrl+cmcLE4`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Aura.AttachedTo Permanent`, `Creature`, `Creature,Artifact`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!attacking`, `Creature.cmcEQX`, `Creature.cmcLE3`, `Creature.cmcLEX`, `Creature.ControlledBy TriggeredTarget`, `Creature.ControllerControlsIsland`, `Creature.counters_GE1_P1P1`, `Creature.IsNotChosenType`, `Creature.Legendary`, `Creature.MonoColor`, `Creature.nonBlack+nonArtifact`, `Creature.nonBlack+nonArtifact+attackedYouThisTurn`, `Creature.nonLegendary+OppCtrl`, `Creature.nonLegendary+powerLEX+OppCtrl`, `Creature.nonMutant`, `Creature.OppCtrl`, `Creature.OppCtrl+cmcLE3,Planeswalker.OppCtrl+cmcLE3`, `Creature.OppCtrl+powerLE2`, `Creature.OppCtrl+powerLTX`, `Creature.Other`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.powerLE4`, `Creature.powerLEX`, `Creature.powerLEX+ControlledBy DelayTriggerRemembered`, `Creature.powerLTY`, `Creature.powerLTZ`, `Creature.Sliver`, `Creature.Vampire`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouOwn`, `Dragon`, `Equipment`, `Equipment.OppCtrl`, `Horse.YouCtrl`, `Human.OppCtrl,Artifact.OppCtrl`, `Land.ControlledBy TriggeredTarget`, `Land.DefenderCtrl`, `Opponent`, `Permanent`, `Permanent.Legendary`, `Permanent.nonLand`, `Permanent.nonLand+cmcLE1`, `Permanent.nonLand+ControlledBy Player.wasDealtCombatDamageThisTurnBy Creature.Pirate GE3`, `Permanent.OppCtrl`, `Permanent.Other+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouOwn+YouDontCtrl`, `Player`, `Player.!CardOwner`, `Thrull`, `Treasure.YouCtrl`

## `GainControlVariant`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `GainControlOwns`
- `AllValid$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Land.YouCtrl`, `Permanent`, `Permanent.!token`, `Permanent.nonLand`, `Permanent.nonLand+Other`
- `ChangeController$`: TODO: Describe this parameter.
  Observed values: `CardOwner`, `ChooseFromPlayerToTheirRight`, `ChooseNextPlayerInChosenDirection`, `NextPlayerInChosenDirection`, `Random`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBUntap`

## `GainLife`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Blessing`, `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`, `Upkeep->BeginCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `CriticalOnly`, `PlayForSub`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `PseudoKicker`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `CastTest`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`, `OptionalCost`, `Revolt`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$Presence_Dragon.1.0`, `Count$RememberedSize/Plus.DinoControlled`, `IsHuman`, `IsLegendary`, `LandfallAmount`, `LifeThem`, `NumLife`, `PiousCheckName`, `Resolved`, `X`, `XLife`, `Y`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Sacrificed`, `Self`, `Targeted`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If it was kicked,`, `If that land was a snow land,`, `If you control an Angel,`
- `ConditionLifeAmount$`: TODO: Describe this parameter.
  Observed values: `LTX`
- `ConditionLifeTotal$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Angel`, `Angel.YouCtrl`, `Artifact`, `Bat.YouCtrl`, `Card`, `Card.Cave`, `Card.cmcLE3`, `Card.counters_EQ0_HOPE`, `Card.Creature`, `Card.Land`, `Card.nonLand+nonCreature`, `Card.Saproling`, `Card.Self`, `Card.tapped`, `Card.Town`, `Card.wasCast`, `Creature`, `Creature,Land`, `Creature.toughnessGE4`, `Creature.YouCtrl+powerGE10`, `Creature.YouCtrl+powerGE4`, `Demon.YouCtrl,Devil.YouCtrl`, `Eldrazi.YouCtrl`, `God.YouCtrl,Demigod.YouCtrl,Enchantment.YouCtrl+Legendary`, `Instant,Sorcery`, `Instant.YouOwn,Sorcery.YouOwn`, `Land`, `Land.Snow`, `Lesson`, `Planeswalker.Gideon`, `Planeswalker.Nissa+YouCtrl`, `Spider`, `Vampire.YouCtrl`, `Zombie`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE3`, `GE5`, `GTLifeYou`, `GTMostLife`, `GTYLife`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `AddCounter<1/LOYALTY>`, `AddCounter<2/LOYALTY>`, `SubCounter<8/LOYALTY>`, `tapXType<5/Cleric>`, `2 T Sac<1/CARDNAME/this artifact>`, `2 T SubCounter<4/CHARGE>`, `T Sac<1/Creature>`, `1`, `Sac<1/CARDNAME>`, `T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{1}, Reveal X white cards from your hand, Sacrifice CARDNAME:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `ParentTarget`, `Player`, `Player.IsRemembered`, `Player.Opponent`, `Player.OpponentOf TriggeredCardController`, `Remembered`, `RememberedController`, `ReplacedTarget`, `ShieldEffectTarget`, `Targeted`, `TargetedController`, `TargetedOwner`, `TriggeredActivator`, `TriggeredAttackerController`, `TriggeredAttackingPlayer.Opponent+controlsCreature.attacking Player.EnchantedBy`, `TriggeredCardController`, `TriggeredPlayer`, `TriggeredSourceController`, `You`, `You & TriggeredTarget`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.Green+YouCtrl`, `Planeswalker.Yanggu+YouCtrl`
- `LifeAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `100`, `13`, `15`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `AdditionalCostPayTimesG`, `AFLifeLost`, `AnimalBoneyardX`, `C`, `Count$Valid Permanent.Colorless+YouCtrl`, `Count$YourSpeed`, `DelifX`, `DomainX`, `DrainedLifeCard`, `Excess`, `GainLifeX`, `GenjuX`, `GreatestPow`, `HalfXDown`, `JaddiLifestriderZ`, `JasmineX`, `KithkinZealot`, `L`, `Lands`, `Life`, `LifePaidOnETB`, `LifeX`, `NumCreatures`, `NumLife`, `NumScrolls`, `PlainsYouControl`, `PrahvX`, `PreventedDamage`, `Remembered$Amount`, `Remembered$CardManaCost`, `Result`, `ScentOfJasmineX`, `ScoutsHonor`, `SVar$VoteNum/Times.3`, `SVar$X/Times.3`, `Targeted$CardToughness`, `TgtPower`, `Toughness`, `TriggeredCard$CardNumColors`, `VolverX`, `X`, `X19`, `X4M`, `X8`, `XLife`, `XPower`, `XToughness`, `XX`, `Y`, `Z`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Cohort —`, `Nosh —`, `Summary Execution —`, `Threshold —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBBlood`, `DBBolster`, `DBChange`, `DBCleanup`, `DBCleanupN`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDelayedTrigger`, `DBDestroy`, `DBDig`, `DBDiscard`, `DBDrain`, `DBDraw`, `DBDraw18U`, `DBDraw20U`, `DBDrawCardIsland`, `DBDrawCards`, `DBDrawThree`, `DBEffect`, `DBEnergy`, `DBExile`, `DBFight`, `DBFog`, `DBGainLife`, `DBGainLifeOpp`, `DBIncubate`, `DBIntensify`, `DBJaddiLifestriderCleanup`, `DBJasmineCleanup`, `DBLearn`, `DBLifeCurse`, `DBLose`, `DBLoseLife`, `DBMana`, `DBMill`, `DBNoCombatDamage`, `DBPump`, `DBPumpAll`, `DBPumpPlus`, `DBPutCounter`, `DBPutOnBottom`, `DBReturn`, `DBReturnKicked`, `DBScentOfJasmineCleanup`, `DBScry`, `DBSearch`, `DBSeek`, `DBShuffle`, `DBShuffleElixir`, `DBSurveil`, `DBSuspect`, `DBToken`, `DBTransform`, `DBTreasure`, `DBTrigDraw`, `DBUntap`, `DBUntapAll`, `DBWinGame`, `DelayReturn`, `DelTrigSlowtrip`, `Dmg`, `DoDraw`, `ExileEff`, `ExileEffect`, `GeniusCards`, `LoseLifeOpp`, `LoseLifeYou`, `Meld`, `Reapproach`, `Token`, `TrigDraw`, `TrigExile`, `TrigReturn`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `MaxTgt`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `Reveal<1/Creature.Dinosaur>`, `Sac<1/Permanent.Other>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredTargetController`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `GainOwnership`

TODO: Write documentation.

**Parameters:**
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `CorrectedSelf`, `Imprinted`, `Remembered`, `Targeted`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`, `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ExchangeAnte`, `TabletToExile1`, `TargetToExile1`, `ToGrave`, `ToGrave1`, `ToHand`
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Ante`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card`

## `GameDrawn`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `NumHighestLife`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_EQ0_INTERVENTION`, `Card.Self+counters_EQ0_OMEN`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`

## `GenericChoice`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `BestOption`, `Brotherhood`, `CombustibleGearhulk`, `CreativitySpark`, `Dragons`, `Fatespinner`, `FoodOrTreasure`, `Khans`, `Legion`, `Mirran`, `PayUnlessCost`, `Phasing`, `Random`, `SelfOthers`, `SinProdder`, `SoulEcho`, `Timetwister`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`, `Urza`
- `ChangeZoneTable$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChoicePrompt$`: TODO: Describe this parameter.
  Observed values: `Choose a condition`, `Choose an offer`, `Have them put the card in their hand?`, `Have them put the card into their graveyard?`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `ABPump1,ABPump2`, `Abzan,Mardu`, `Ambitious,Expedient`, `Angel,Demon`, `Animate41,Animate14`, `Animate51,Animate15`, `AniWhack,OppDoodle`, `Believe,Doubt`, `Berserk,Twiddle,BloodLust,Green,White,Red,Damage3,Flying,P3P3,Banding,Black,Blue,NoRegen,LilSneak,M2M0,ToHand,Damage1,Nerf,Exile,Orcish`, `BigTough,BigPower`, `Blood,Clue,Food`, `Brotherhood,Enclave`, `Cat,Dog`, `ChangeColor,ChangeType`, `ChangePower,ChangeToughness`, `ChooseC1L2A3,ChooseL1C2A3,ChooseA1L2C3,ChooseA1C2L3,ChooseC1A2L3,ChooseL1A2C3`, `ChooseCounters,ChooseFlying,ChooseFirstStrike,ChooseTrample`, `ChooseCreature,ChooseArtifact,ChooseLand,ChooseEnchant`, `Clue,Food,Treasure`, `CombustDraw,CombustDamage`, `Cosplay,Science`, `CovenantPutIntoHand,CovenantMillDraw`, `DamageAll1M,GainControl2M,DealDamage3M,Destroy4M,Effect5M,ChangeZone6M,Draw7M,Mill8M,Dig9M,Exile10M,Reveal11M,Tutor12M,Sacrifice13M,Token14M,Token15M,SetLife16M,Destroy17M,Return18M,Token19M,Draw20M`, `DBBlink,DBFight`, `DBBottomLibChoice,DBTopLibChoice`, `DBCheckHand,DBNoChange`, `DBDiscardOne,DBChallenge`, `DBDiscardToDraw,DBSacToDraw`, `DBDmgAttackers,DBDmgBlockers`, `DBDoNotKeep,DBIncrease`, `DBDrawCard,DBCheatCreature`, `DBExileAll,DBCleanupBis`, `DBExileSelf,DBExileTarget`, `DBFrog,DBOctopus`, `DBGraveAndDamage,DoNothing`, `DBHandChoice,DBTopLibChoice`, `DBKillAllEnch,DBKillNonWEnch`, `DBKillArtifacts,DBKillEnchantments`, `DBKillLand,DBKillCreatures`, `DBLoseLife,DBSac`, `DBPayLife,DBDiscard`, `DBPayLife,DBSacCreature`, `DBPutCounter,DBBanding,DBFirstStrike,DBTrample`, `DBPutCounter,DBTurnFaceUp`, `DBRepeat,Play`, `DBReturn,DBUnlock`, `DBSacToDraw,DBDiscardToDraw`, `DBScry,DBUntap`, `DBToHand,DoNothing`, `DBTop,DBBottom`, `DBTopLibChoice,DBHandChoice`, `DealDamage1U,Effect2U,DestroyAll3U,Token4U,LifeGain5U,Damage6U,Effect7U,Effect8U,Token9U,Shuffle10U,Destroy11U,Effect12U,Effect13U,ControlPlayer14U,ExileLibrary15U,Token16U,Raise17U,LifeDraw18U,FlipTurns19U`, `DebuffFS,DebuffSW`, `DestroyWhite,DestroyGreen`, `DigLand,DigNonland`, `Discard,No`, `Discard,Sacrifice`, `Diversion,Intelligence`, `Draw3,Conjure,Return2,ReturnBig,EmblemBuff,EmblemReduceCost,EmblemDavrielPW,EmblemDrawGain`, `ExchangeOwnership,Concede`, `ExileDraw,No`, `Fame,Fortune`, `FatespinnerSkipDraw,FatespinnerSkipMain,FatespinnerSkipCombat`, `Flyer,VigilancePump,Wall`, `Food,Treasure`, `FSVig,VigLif,FSLif`, `GreenAnchor,RedWaterfall`, `GroundMold,AirMold,WallMold`, `GroundPlasma,AirPlasma,WallPlasma`, `GuessGreaterArtifacts,GuessNotGreaterArtifacts`, `GuessGreaterThanFour,GuessNotGreaterThanFour`, `GuessInHand,GuessNotInHand`, `Jeskai,Temur`, `Khans,Dragons`, `Land,Nonland`, `LandOne,NonlandOne`, `Lose6,Exile2,Sac2,PerpetualBuffTheirs,EmblemDebuff,EmblemRaiseCost,EmblemDrawExile,EmblemUpkeepLose`, `Mardu,Jeskai`, `Mirran,Phyrexian`, `Money,Friends,Secrets`, `NCR,Legion`, `Odd,Even`, `OppRock,OppPape,OppScis`, `P1P1Counter,ChargeCounters`, `Pay1,Pay1Life`, `Pay2,Pay1`, `PayB,Pay3`, `PayDiscard,Pay2`, `PayG,PayW,PayU`, `PayLife,ExchangeOwnership,Concede`, `PayLife,RevealCard`, `PayRR,Pay2Life`, `PaySac,PayDiscard`, `PayW,PaySacFood`, `Pump1,PutCounter2,Destroy3,Token4,Token5,Token6,Dig7,MustAttack8,PutCounter9,Effect10,Exile11,Dig12,Animate13,Draw14,Animate15,PumpAll16,Dig17,DealDamage18,Animate19,Mana20`, `PumpAtt,PumpDef`, `RemoveCounters,DealDamage`, `ReturnPetals,DrawCards`, `RevealCard`, `SacNonland,Discard`, `SacTwoLands,DealDmg`, `SeekNonLand,ConjurePlains`, `Self,Others`, `Silence,Snitch`, `SparkDamage,SparkPlay`, `SpongeFly,SpongeStrike,SpongeTramp`, `Stargate,Homebody`, `Sultai,Abzan`, `SVar1,SVar2`, `Temur,Sultai`, `TerrapactToken,TerrapactPutCounter`, `ToHand,Untap,Tap,Damage,Draw3,DestroyGain,DestroyAE,Gain3,Anoint,DestroyCL,Mill2,Wasp,Nevinyrral,Suleiman,Pandora,Discard,Fog,Sindbad`, `TrigPump1,TrigPump2`, `WarChoice,PeaceChoice`, `Wolf,Antelope,Cat,Rhino`, `YouDoodle`, `YouPape`, `YouRock`, `YouRock,YouPape,YouScis`, `YouScis`, `YouWhack`, `YouWhack,YouDoodle`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `YouChose`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self+counters_GT0_ECHO`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE10`, `LT10`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `AddCounter<2/LOYALTY>`, `SubCounter<2/LOYALTY>`, `1 G G`, `2 Discard<1/Card>`, `2 G`, `PayEnergy<1>`, `G W Discard<1/Card>`, `AddCounter<3/LOYALTY>`, `2 T CollectEvidence<3>`
- `DamageMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `ParentTarget`, `Player`, `Player.Chosen`, `Player.IsRemembered`, `Remembered`, `RememberedController`, `RememberedOwner`, `Targeted`, `TargetedController`, `TargetedOwner`, `TargetedPlayer`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `FallbackAbility$`: TODO: Describe this parameter.
  Observed values: `DrawFallback`, `LoseLifeFallback`
- `Guess$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumRandomChoices$`: TODO: Describe this parameter.
  Observed values: `3`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `2`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `SetChosenMode$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowChoice$`: TODO: Describe this parameter.
  Observed values: `Description`, `ExceptSelf`, `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Choice2`, `DBCleanup`, `DBCondition`, `DBDelayTrigger`, `DBDiscard`, `DBDraw`, `DBFame`, `DBGrandWheel`, `DBMoney`, `DBPutIntoHand`, `DBSilenceBranch`, `DBTimetwister`, `Exile`, `NotifyDoodle`, `NotifyPape`, `NotifyScis`, `OppChoice`, `ScoreWin`, `StoreYou`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TempRemember$`: TODO: Describe this parameter.
  Observed values: `Chooser`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`, `Stack,Battlefield`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.Other`, `Card`, `Card.Black`, `Creature`, `Opponent`, `Permanent`

## `Goad`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 R Sac<1/Artifact;Creature/artifact or creature>`, `T Sac<1/Treasure>`, `3 T`, `2 Sac<1/Artifact;Creature/artifact or creature>`, `2 U`, `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `TriggeredObjectLKICopy`, `Valid Creature.attacking`, `Valid Creature.ControlledBy Player.TriggeredTarget`, `Valid Creature.ControlledBy TargetedPlayer`, `Valid Creature.IsSuspected`, `Valid Creature.NamedCard`, `Valid Creature.OppCtrl`, `Valid Creature.OppCtrl+EnchantedBy Aura.YouCtrl`, `Valid Creature.YouCtrl`, `Valid Creature.YouDontCtrl`
- `DefinedDesc$`: TODO: Describe this parameter.
  Observed values: `each creature that had a double strike counter put on it this way`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `AsLongAsControl`, `AsLongAsInPlay`, `Permanent`
- `NoLonger$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Alluring Eyes —`, `Crown of Madness —`
- `RememberGoaded$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddCombat`, `DBCleanup`, `DBDisableSacing`, `DBDraw`, `DBEffect`, `DBNoBlock`, `DBPump`, `DBPutCounter`, `DelTrig`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MonstrosityX`, `OneEach`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackedTarget`, `TriggeredTarget`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.ControlledBy NextPlayerToYourLeft`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.OppCtrl`, `Creature.YouDontCtrl`, `Player`

## `Heist`

TODO: Write documentation.

**Parameters:**
- `Num$`: TODO: Describe this parameter.
  Observed values: `2`
- `SpellDescription$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `ImmediateTrigger`

TODO: Write documentation.

**Parameters:**
- `AfterReplacement$`: TODO: Describe this parameter.
  Observed values: `True`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `SacForDamage`, `SacForDamage.cmc`, `SacForDamage.GiantX2`, `WeakerCreature`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `NumTimes`
- `AnnounceMax$`: TODO: Describe this parameter.
  Observed values: `3`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CalimNumRemembered`, `Count$RememberedSize`, `Excess`, `LifeAmount`, `NumTimes`, `Resolved`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `EQ3`, `EQ4`, `GE1`, `GE2`, `GE4`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Discarded`, `Imprinted`, `Remembered`, `RememberedCard`, `RememberedLKI`, `Sacrificed`, `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Aura`, `Card`, `Card.ControlledBy ParentTarget`, `Card.Creature`, `Card.Creature+YouCtrl`, `Card.Equipment`, `Card.Land+YouCtrl`, `Card.nonLand`, `Card.nonLand+YouCtrl`, `Card.Self`, `Card.Self+counters_GE4_QUEST`, `Creature`, `Creature.YouOwn`, `Equipment`, `Instant,Sorcery`, `Land.Basic+YouCtrl`, `Permanent.Red+YouCtrl+Other`, `Zombie`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `EQ20`, `EQ3`, `GT2`, `LE10`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `CopyTriggeringObjects$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/Artifact>`, `PayLife<2>`, `1`, `3`, `SubCounter<1/OIL>`, `PayEnergy<2>`, `SubCounter<1/Menace>`, `Mana<2 R\NumTimes>`, `Sac<1/Creature.Other;Enchantment.Other/another creature or enchantment>`, `Sac<1/Creature>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `You may pay {2} and sacrifice an Aura attached to CARDNAME.`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `Execute$`: TODO: Describe this parameter.
  Observed values: `ChooseName`, `DBAddMana`, `DBChangeZone`, `DBDamage`, `DBDamageAll`, `DBDealDamage`, `DBDealDmg`, `DBDmg`, `DBDraw`, `DBFight`, `DBPlay`, `DBPump`, `DBReanimate`, `DBRepeatCopy`, `DBReturn`, `DBSac`, `DBTap`, `DBToken`, `GainLifeYou`, `NameCard`, `TrigABDealDamage`, `TrigAttach`, `TrigBounce`, `TrigBounceAll`, `TrigCast`, `TrigChange`, `TrigChangeZone`, `TrigCharm`, `TrigChoose`, `TrigClone`, `TrigConjure`, `TrigCopy`, `TrigCounter`, `TrigDamage`, `TrigDamageAll`, `TrigDamageBis`, `TrigDamageCreature`, `TrigDealDamage`, `TrigDealDmg`, `TrigDebuff`, `TrigDestroy`, `TrigDig`, `TrigDiscard`, `TrigDmg`, `TrigDoubleDamage`, `TrigDraw`, `TrigEachOpp`, `TrigEffect`, `TrigExile`, `TrigExileAll`, `TrigExtraTurn`, `TrigFight`, `TrigFirstStrike`, `TrigFlashback`, `TrigGainControl`, `TrigLoseGame`, `TrigMakeCard`, `TrigMill`, `TrigMoveCounter`, `TrigMultiplyCounter`, `TrigPlay`, `TrigPowerDamage`, `TrigPump`, `TrigPumpAll`, `TrigPutCounter`, `TrigPutCounterAll`, `TrigPutCounterP1P1`, `TrigPutCounters`, `TrigRemoveCounter`, `TrigReturn`, `TrigReveal`, `TrigSac`, `TrigSacrifice`, `TrigTap`, `TrigTapOrUntap`, `TrigToken`, `TrigUnblockable`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE4_QUEST`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `RememberDiscarded$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberEach$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `ChosenCard & Player.IsRemembered`, `ChosenPlayer`, `Discarded`, `Remembered`, `Remembered.nonLand`, `RememberedCard`, `RememberedLKI`, `ReplacedSource`, `Sacrificed`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredCardLKICopy`
- `RememberSVarAmount$`: TODO: Describe this parameter.
  Observed values: `Excess`, `NumTimes`, `Result`, `X`, `Y`, `Z`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `Static$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCleanup2`, `DBTriggerNonLand`, `ExileEffect`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TrigDescReminderDefined$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`
- `TriggerAmount$`: TODO: Describe this parameter.
  Observed values: `Count$RememberedNumber`, `Count$RememberedNumber/DivideEvenlyDown.2`, `Remembered$Amount`, `Remembered$Amount/DivideEvenlyDown.2`, `Remembered$Amount/DivideEvenlyDown.4`, `Remembered$Amount/DivideEvenlyDown.5`
- `TriggerDescription$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `2 W`, `CollectEvidence<9>`, `Discard<1/Card.nonLand/nonland card>`, `Discard<1/Card>`, `Discard<2/Card>`, `Exile<1/Creature.!token>`, `ExileAnyGrave<1/Card.TriggeredNewCard>`, `Mandatory PayEnergy<X>`, `PayEnergy<8>`, `PayEnergy<X>`, `Reveal<1/Giant>`, `Sac<1/Artifact>`, `Sac<1/Creature>`, `Sac<1/Food>`, `W U B R G`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Permanent.nonLand`
- `XAnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `any amount of red mana to pay`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `R`

## `Incubate`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `Count$Valid Land.YouCtrl`, `TriggeredSpellAbility$CardManaCostLKI`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 T Sac<1/Creature.Other;Artifact.Other/another creature or artifact>`, `B ExileFromGrave<1/CARDNAME>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedController`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`, `DBTransform`
- `Times$`: TODO: Describe this parameter.
  Observed values: `2`, `5`, `X`

## `Intensify`

TODO: Write documentation.

**Parameters:**
- `AllDefined$`: TODO: Describe this parameter.
  Observed values: `Card.namedAwestruck Cygnet+YouOwn`, `Card.Self,Card.inZoneGraveyard+namedArek; False Goldwarden+YouOwn,Card.inZoneHand+namedArek; False Goldwarden+YouOwn,Card.inZoneLibrary+namedArek; False Goldwarden+YouOwn`, `Card.Self,Card.inZoneGraveyard+namedMinthara of the Absolute+YouOwn,Card.inZoneHand+namedMinthara of the Absolute+YouOwn,Card.inZoneLibrary+namedMinthara of the Absolute+YouOwn`, `Card.Self,Card.inZoneGraveyard+namedPiece It Together+YouOwn,Card.inZoneHand+namedPiece It Together+YouOwn,Card.inZoneLibrary+namedPiece It Together+YouOwn`, `Card.YouOwn+Chorus`, `Card.YouOwn+namedChittering Skullspeaker`, `Card.YouOwn+namedStatic Discharge`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `DefinedDesc$`: TODO: Describe this parameter.
  Observed values: `all cards they own named Chittering Skullspeaker`, `all cards they own named Static Discharge`, `all Chorus cards you own`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`

## `Investigate`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Excess`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedLKI`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.YouCtrl`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T`, `3 T`, `ExiledMoveToGrave<1/Card.ExiledWithSource/card exiled with CARDNAME>`, `1 G ExileFromGrave<1/Creature>`, `Discard<1/Card>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player.withMostTypeCreature`, `RememberedController`, `TargetedController`, `TargetedOwner`, `You`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `Count$Valid Creature.IsGoaded+YouCtrl`, `PlayerCountRegisteredOpponents$HasPropertyLostLifeThisTurn`, `Remembered$Amount/Times.2`, `VoteNum`, `X`, `Y`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberInvestigatingPlayers$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDebuff`, `DBDelTrig`, `DBDestroyAll`, `DBDraw`, `DBEffect`, `DBGainLife`, `DBLoseLife`, `DBNoGoad`, `DBPump`, `DBRegen`, `DBToken`

## `Learn`

TODO: Write documentation.

**Parameters:**
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.cmcLE4`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 Sac<1/CARDNAME>`
- `SpellDescription$`: TODO: Describe this parameter.

## `LookAt`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 W`, `1 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Valid Creature.faceDown+TargetedPlayerCtrl`, `ValidAll Card.TopLibrary+TargetedPlayerCtrl`, `ValidHand Card.TargetedPlayerCtrl`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBFaceDown`, `DBRearrange`, `DBTopLibrary`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.faceDown`

## `LoseLife`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILifeThreshold$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AnyPhase`
- `AnnounceType$`: TODO: Describe this parameter.
  Observed values: `ChooseNumber`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `LoseLifeCheck`, `OpponentSmallest`, `RaidTest`, `Resolved`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE3`, `GE5`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ExiledWith`, `Remembered`, `RememberedLKI`, `Self`, `Targeted`, `TriggeredCardLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `an enchantment,`, `If you control a Demon,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Card`, `Card.Creature`, `Card.IsSaddled`, `Card.Self+Phyrexian`, `Card.Self+PromisedGift`, `Card.sharesCardTypeWith Imprinted+OppOwn`, `Card.tapped`, `Card.YouDontCtrl`, `Creature`, `Creature.Cleric`, `Creature.YouCtrl+Colorless+Other`, `Demon.YouCtrl`, `Enchantment`, `Human.YouCtrl`, `Instant,Card.withFlash`, `Instant,Sorcery`, `Land`, `Legendary`, `Ninja.YouCtrl`, `Ogre.YouCtrl`, `Pirate.StrictlyOther+YouCtrl`, `Planeswalker.Liliana`, `Vampire.YouCtrl`, `Villain.YouCtrl`, `Warrior.YouCtrl`, `Zombie`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `GE1`, `GE11`, `GE3`, `GE8`, `LT1`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T Sac<1/Creature.Other;Artifact.Other/another creature or artifact>`, `1 B T`, `2 Sac<1/Creature.Other;Blood.token/another creature or a Blood token>`, `3 W B T Sac<1/NICKNAME>`, `T Sac<X/Permanent>`, `5 T`, `Draw<X/You>`, `Sac<1/CARDNAME>`, `T`, `7 B T Sac<1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, sacrifice all permanents you control and discard your hand.`, `{B}{B}, {T}, Sacrifice CARDNAME and thirteen Blood tokens:`, `{T}, Sacrifice up to three permanents:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttackingPlayer`, `CardController`, `ChosenPlayer`, `ImprintedController`, `NonRememberedOwner`, `NonTriggeredCardOwner`, `OppNonRememberedController`, `Opponent`, `Opponent.!IsRemembered`, `Opponent.HasCardsInCommand_Effect.namedDamaged by Gollum; Obsessed Stalker_GE1`, `Opponent.IsCorrupted`, `ParentTarget`, `Player`, `Player.Chosen`, `Player.controlsPermanent.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Player.Opponent+controlsElf_EQ0`, `Player.Opponent+HasCardsInHand_Card_EQ0`, `Player.Opponent+IsCorrupted`, `Player.Other`, `Remembered`, `RememberedController`, `RememberedPlayer`, `ReplacedCardController`, `ReplacedPlayer`, `Targeted`, `TargetedController`, `TargetedOwner`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredAttackerController`, `TriggeredAttackerOwner`, `TriggeredAttackingPlayer`, `TriggeredAttackingPlayer & You`, `TriggeredBlockerController`, `TriggeredCardController`, `TriggeredCardOwner`, `TriggeredCauseController`, `TriggeredDefender`, `TriggeredDefendingPlayer`, `TriggeredOpponentVotedDiff`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredSourceSAController`, `TriggeredTarget`, `TriggeredTargetController`, `You`
- `ForgetOtherTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.YouOwn`, `Permanent.Black+YouCtrl`, `Planeswalker.Liliana+YouCtrl`
- `LifeAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `1000`, `13`, `15`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `A`, `C`, `CntLife`, `Count$ChosenNumber`, `Count$Valid Creature.YouCtrl`, `Count$YourSpeed`, `DiffX`, `EbonXOpp`, `EbonXYou`, `ExiledWith$CardManaCost`, `HalfUp`, `HavocX`, `L`, `LichLeech`, `LifePaidOnETB`, `LifeTotal`, `MortisX`, `NumAllies`, `NumLife`, `Ouch`, `PainX`, `PlayerCountRemembered$LifeTotal/HalfUp`, `QuietusX`, `RavingXOpp`, `Remembered$CardPower`, `Result`, `SVar$Y/Minus.Z`, `SwampsYouControl`, `ThisTargetedPlayer$LifeTotal/HalfUp`, `TriggeredCard$CardNumColors`, `VizkopaMageX`, `X`, `Y`, `Z`
- `Max$`: TODO: Describe this parameter.
  Observed values: `3`
- `Min$`: TODO: Describe this parameter.
  Observed values: `0`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `3`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `3`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Cohort —`, `Relentless Mind —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GE4`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ReduceAmount$`: TODO: Describe this parameter.
  Observed values: `X`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `4 B`, `X`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DB1`, `DBAmass`, `DBAnimate`, `DBChange`, `DBChangeZone`, `DBClean`, `DBCleanup`, `DBControl`, `DBConvert`, `DBCounter`, `DBDamage`, `DBDamageMountain`, `DBDestroyAll`, `DBDig`, `DBDiscard`, `DBDraft`, `DBDraw`, `DBDrawC`, `DBDrawE`, `DBDrawP`, `DBEffect`, `DBEndure`, `DBEnergy`, `DBExile`, `DBExileTop`, `DBGain`, `DBGain2`, `DBGainLife`, `DBGainLife1`, `DBGainLife2`, `DBGainLifeEmblem`, `DBGainLifeN`, `DBGainOneLife`, `DBGainThree`, `DBGainTrea`, `DBInvestigate`, `DBLoseLifeOpp`, `DBLoseLifeOpponents`, `DBLoseLifeYou`, `DBMana`, `DBMill`, `DBPlay`, `DBPoison`, `DBPoisoned`, `DBProliferate`, `DBPutCounter`, `DBResurrectYou`, `DBReveal`, `DBSac`, `DBSacArtifact`, `DBSacrifice`, `DBSacrificeThree`, `DBSacSelf`, `DBScry`, `DBSearch`, `DBTap`, `DBToken`, `DBTreasure`, `DBTreasureTokens`, `DBTutor`, `DBUntap`, `DBVoidDraw`, `EbonyGain`, `Gain`, `GainLife`, `RememberOpp`, `RememberYou`, `TargetToExile2`, `TrigMill`, `TrigToken`, `YouLose`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `MaxTgts`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 W`, `2`, `3`, `Blight<2>`, `Discard<1/Card>`, `Discard<2/Card>`, `Discard<Y/Card>`, `Draw<1/You>`, `ExileFromGrave<1/Elf>`, `Sac<1/CARDNAME>`, `Sac<1/Creature.!token/a nontoken creature>`, `Sac<1/Creature;Planeswalker/creature or planeswalker>`, `Sac<1/Creature>`, `Sac<1/Permanent.!IsRemembered+nonLand/another nonland permanent>`, `Sac<1/Permanent.nonLand/nonland permanent>`, `Sac<1/Permanent.nonland/nonland permanent>`, `Sac<1/Permanent.nonLand>`, `Sac<1/Permanent>`, `Sac<X/Permanent>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `ParentTarget`, `Player.IsRemembered`, `Remembered`, `Targeted`, `TargetedController`, `TriggeredCardController`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `TriggeredTargetController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.LostLifeThisTurn`, `Player.Opponent`, `Player.wasDealtDamageThisTurnBySource`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `3`

## `LosePerpetual`

TODO: Write documentation.

**Parameters:**
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`

## `LosesGame`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CardsInGrave`, `CheckExile`, `CheckGraveyard`, `PermanentsToSac`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `NE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.counters_EQ0_OIL`, `Card.Self+counters_GE3_JUDGMENT`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE15`, `GE3`, `GE6`, `GTY`, `LTX`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `W W U U B B R R G G T Sac<1/CARDNAME>`, `SubCounter<8/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `EnchantedPlayer`, `Player.attackedBySourceThisTurn`, `Player.lifeEQ13`, `Player.Opponent+controlsLegendary.Creature_EQ0+controlsPlaneswalker_LE0`, `RememberedOwner`, `SourceController`, `Spawner>TriggeredTarget`, `Targeted`, `TargetedOwner`, `TriggeredTarget`, `You`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBExile`, `DBGainLife`, `DBLoseLife`, `DBSacrificePerm`, `DBShuffle`, `ForbiddenPractice`, `TargetToExile3`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1 W W`, `2 B`, `2 G G`, `3 U U`, `4 R`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `MakeCard`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `AdditionalActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `7`, `X`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `AttachedTo$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl`
- `Booster$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Ionize,Electrolyze`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.!token`, `Card.Self`, `Creature.cmcLE2`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE5`
- `Conjure$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `tapXType<1/Bird> Sac<1/Artifact>`, `Sac<1/CARDNAME>`, `SubCounter<6/LOYALTY>`, `T`, `Discard<1/Land/land>`, `2 G Discard<1/CARDNAME>`, `AddCounter<1/LOYALTY>`, `ExileFromGrave<1/CARDNAME>`, `1 G ExileFromGrave<1/CARDNAME/this card>`, `1 T Discard<1/Card>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player`, `Promised`, `TargetedPlayer`, `TriggeredCardController`
- `DefinedName$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ChosenMap`, `DelayTriggerRemembered`, `Remembered`, `Targeted`, `Targeted.!token`, `TargetedSource`, `ThisTargetedCard`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredCards`, `TriggeredEnlisted`, `TriggeredSource`, `ValidLibrary Card.TopLibrary+TargetedPlayerOwn`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `FaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `Filter$`: TODO: Describe this parameter.
  Observed values: `Card.cmcEQCount$CardCounters.P1P1`, `Card.cmcEQX`
- `GiftDescription$`: TODO: Describe this parameter.
  Observed values: `a Rhystic Study`
- `ImprintMade$`: TODO: Describe this parameter.
  Observed values: `True`
- `LibraryPosition$`: TODO: Describe this parameter.
  Observed values: `0`, `Count$Random.0.10`, `Count$Random.0.15`, `Count$Random.0.4`, `Count$Random.0.6`, `Count$Random.0.8`, `Z`
- `Name$`: TODO: Describe this parameter.
  Observed values: `A-Blood Artist`, `Admiral Beckett Brass`, `Ambush Viper`, `Arguel's Blood Fast`, `Ball Lightning`, `Calim, Djinn Emperor`, `Cantor of the Refrain`, `Chitterspitter`, `ChosenName`, `Colossal Dreadmaw`, `Demonic Pact`, `Dig Up the Body`, `Dragonfly Suit`, `Fblthp, the Lost`, `Flamebraider`, `Flametongue Kavu`, `Flooded Strand`, `Food Fight`, `Forest`, `Gilded Goose`, `Gixian Recycler`, `Goatnap`, `Goblin Gaveleer`, `Golden Egg`, `Hangarback Walker`, `Hollowhenge Beast`, `Inspiring Statuary`, `Juggernaut`, `Kraken Hatchling`, `Leeches`, `Lightning Bolt`, `Llanowar Elves`, `Lumbering Lightshield`, `Manor Guardian`, `Marwyn, the Nurturer`, `Mephidross Slime`, `Midnight Clock`, `Might of the Meek`, `Mishra's Foundry`, `Mitotic Slime`, `Monastery Mentor`, `Mothlight Processionist`, `Mox Emerald`, `Mox Jet`, `Mox Opal`, `Mox Pearl`, `Mox Ruby`, `Mox Sapphire`, `Muraganda Petroglyphs`, `Naturalize`, `Nettlecyst`, `Ornithopter`, `Phyrexian Scrapyard`, `Plains`, `Plummet`, `Ponder`, `Predatory Sludge`, `Propagator Primordium`, `Ragavan, Nimble Pilferer`, `Reassembling Skeleton`, `Regal Force`, `Rhystic Study`, `Rite of Flame`, `Sanguine Bond`, `Savage Stomp`, `Seven Dwarves`, `Shivan Dragon`, `Siege Rhino`, `Sigardian Evangel`, `Slimy Dualleech`, `Soldiers of the Watch`, `Soul of New Phyrexia`, `Spotlight Falcon`, `Stab Wound`, `Starfighter Pilot`, `Stonybrook Schoolmaster`, `Stormfront Pegasus`, `Sunscorched Desert`, `Suntail Hawk`, `Take Inventory`, `Tempered Steel`, `Thieving Magpie`, `Think Twice`, `Time Walk`, `Training Grounds`, `Tropical Island`, `Utility Knife`, `Verdant Dread`, `Virus Beetle`, `Volcanic Geyser`, `Wastes`
- `Names$`: TODO: Describe this parameter.
  Observed values: `Ancestral Recall,Black Lotus,Mox Emerald,Mox Jet,Mox Pearl,Mox Ruby,Mox Sapphire,Time Walk,Timetwister`, `Darksteel Ingot,Darksteel Plate`, `Disruptive Stormbrood,Purging Stormbrood,Runescale Stormbrood,Twinmaw Stormbrood,Whirlwing Stormbrood`, `First Little Pig,Second Little Pig,Third Little Pig`, `Steelclaw Lance,Brawler's Plate`, `Urza's Mine,Urza's Tower,Urza's Power Plant`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionPrompt$`: TODO: Describe this parameter.
  Observed values: `Would you like to conjure a duplicate of the targeted card into the top five cards of your library ?`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Corrupted —`, `Renew —`
- `RememberMade$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Spellbook$`: TODO: Describe this parameter.
  Observed values: `Adagia; Windswept Bastion,Evendo; Waking Haven,Kavaron; Memorial World,Susur Secundi; Void Altar,Uthros; Titanic Godcore`, `Aether Tunnel,All That Glitters,Celestial Mantle,Curator's Ward,Curiosity,Ethereal Armor,Face of Divinity,Knightly Valor,Metamorphic Alteration,On Serra's Wings,Rousing Read,Staggering Insight,Take Flight`, `Aurelia; the Law Above,Boros Recruit,Skyknight Legionnaire,Spark Trooper,Swiftblade Vindicator`, `Belligerent Sliver,Bladeback Sliver,Blur Sliver,Bonescythe Sliver,Cleaving Sliver,Cloudshredder Sliver,Diffusion Sliver,Dregscape Sliver,Enduring Sliver,First Sliver's Chosen,Hollowhead Sliver,Lancer Sliver,Lavabelly Sliver,Leeching Sliver,Manaweft Sliver,Predatory Sliver,Scuttling Sliver,Sentinel Sliver,Sliver Hivelord,Spiteful Sliver,Steelform Sliver,Striking Sliver,Tempered Sliver,The First Sliver`, `Blade Juggler,Body Count,Dead Revels,Drill Bit,Hackrobat,Light Up the Stage,Rafter Demon,Rix Maadi Reveler,Skewer the Critics,Spawn of Mayhem,Spikewheel Acrobat`, `Brainstorm,Consider,Obsessive Search,Opt,Peek,Piece It Together,Ponder,Preordain,Quicken,Serum Visions,Sleight of Hand,Thought Scour`, `Empty the Warrens,Galvanic Relay,Grapeshot`, `Faith's Fetters,Ritual of Rejuvenation,Invoke the Divine,Inspiring Cleric`, `First Little Pig,Second Little Pig,Third Little Pig`, `Gate of the Black Dragon,Gate to Manorborn,Gate to Seatower,Gate to the Citadel,Gate to Tumbledown`, `Goblin Warchief,Goblin Chieftain,Skirk Prospector,Brash Taunter,Wily Goblin,Goblin Trashmaster,Ember Hauler,Relic Robber,Fanatical Firebrand,Goblin Arsonist,Reckless Ringleader,Battle Cry Goblin,Beetleback Chief,Goblin Instigator,Legion Warboss`, `Hard Evidence,Stifle,Contentious Plan,Suit Up,Befuddle,Majestic Metamorphosis,Hampering Snare,Ghostform,See the Truth,Keep Safe,Teferi's Time Twist,Startle,Flood of Recollection,Choking Tethers,Bury in Books`, `Light of Hope,Swords to Plowshares,Force Spike,Ponder,Dark Ritual,Duress,Assault Strobe,Lightning Bolt,Fog,Giant Growth`, `Shivan Dragon,Moonveil Regent,Terror of the Peaks,Leyline Tyrant,Immersturm Predator,Manaform Hellkite,Bone Dragon,Demanding Dragon,Skarrgan Hellkite,Thunderbreak Regent,Black Dragon,Skyship Stalker,Red Dragon`, `Spyglass Siren,Staunch Crewmate,Corsair Captain`
- `SpellbookAmount$`: TODO: Describe this parameter.
  Observed values: `2`, `X`
- `SpellbookName$`: TODO: Describe this parameter.
  Observed values: `Planets`, `Slivers`, `the Three Pigs`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ArmorSetAtt`, `DBAnimate`, `DBAttach`, `DBCleanup`, `DBClearChosen`, `DBClearNamed`, `DBCloak`, `DBConjure`, `DBCopyPerm`, `DBDelayTrig`, `DBDiscard`, `DBDraw`, `DBEffect`, `DBImmediateTrigger`, `DBIntensify`, `DBManifest`, `DBPerpetual`, `DBPump`, `DBPumpTurn`, `DBPutBattlefield`, `DBPutCounter`, `DBRemember`, `DBReorder`, `DBRepeat`, `DBSetAttacking`, `DBToken`, `DBTransform`, `WeftwinderDraw`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GE3`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `X`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`, `Y`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Stack`
- `TokenCard$`: TODO: Describe this parameter.
  Observed values: `True`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Card>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card.inZoneStack`, `Card.OppOwn`, `Creature.!token`, `Creature.attacking+Other+!token`, `Creature.ExiledWithSource`, `Creature.OppOwn+inZoneGraveyard`, `Creature.Other+YouOwn`, `Creature.YouCtrl+Other+!token,Artifact.YouCtrl+Other+!token`, `Creature.YouOwn`, `Instant.ExiledWithSource,Sorcery.ExiledWithSource`, `Permanent.!token`
- `WithCounter$`: TODO: Describe this parameter.
  Observed values: `CHARGE`, `EGG`
- `WithCounterNum$`: TODO: Describe this parameter.
  Observed values: `3`, `8`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`, `Hand`, `Library`, `None`

## `Mana`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Metalcraft`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`, `3`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep->Main2`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AddsCounters$`: TODO: Describe this parameter.
  Observed values: `Card.Creature+MultiColor_P1P1_1`, `Card.Creature_P1P1_1`, `Card.YouOwn+IsCommander_P1P1_ManaAddsCounterNum`, `Creature.nonHuman_P1P1_1`
- `AddsKeywords$`: TODO: Describe this parameter.
  Observed values: `Haste`, `Riot`
- `AddsKeywordsUntil$`: TODO: Describe this parameter.
  Observed values: `UntilEOT`
- `AddsKeywordsValid$`: TODO: Describe this parameter.
  Observed values: `Spell.Creature`, `Spell.Dragon+Creature`
- `AddsNoCounter$`: TODO: Describe this parameter.
  Observed values: `!Permanent`, `True`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AtOppEOT`, `BlackLotus`, `ManaRitual`, `ManaRitualBattery`, `ManaRitualBattery.1`, `MostProminentInComputerHand`
- `AINoRecursiveCheck$`: TODO: Describe this parameter.
  Observed values: `True`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `10`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `Count$Valid Goblin.YouCtrl`, `Excess`, `ManaX`, `MetalWorkerX`, `NumManaMax`, `NumRemoved`, `Sacrificed$CardPower`, `SakuraX`, `UrzaAmount`, `X`, `X20`, `Y`, `Z`
- `AmountDesc$`: TODO: Describe this parameter.
  Observed values: `for each counter removed`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$YourTurns`, `FormidableTest`, `X`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `You`
- `CombatMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Add one mana of any color chosen as you drafted cards named CARDNAME.`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CheckCounter`, `LandfallAmount`, `RDCoolness`, `Resolved`, `SoulbrightNum`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`, `TriggeredCard`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Green`, `Card.wasCastFromYourHand`, `Instant.YouOwn,Sorcery.YouOwn`, `Land`, `Land.Snow`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `EQ3`, `GE1`, `GE5`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `T Sac<1/CARDNAME>`, `1 T`, `1`, `T PayEnergy<1>`, `R`, `T Sac<1/CARDNAME/this artifact>`, `2 T`, `U T`, `R T Exert<1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{1}, Remove X storage counters from CARDNAME:`, `{T}, Remove X storage counters from CARDNAME:`, `{T}, Sacrifice X Goats:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player`, `Targeted`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredPlayer`, `You`
- `Each$`: TODO: Describe this parameter.
  Observed values: `2`, `X`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `InstantSpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Card.Self+counters_GE2_OIL`, `Card.Self+ThisTurnEntered`, `Creature.Self`, `Creature.YouCtrl+powerGE4`, `Dragon.YouCtrl`, `Forest.YouCtrl,Island.YouCtrl`, `Forest.YouCtrl,Plains.YouCtrl`, `Island.YouCtrl`, `Island.YouCtrl,Mountain.YouCtrl`, `Island.YouCtrl,Swamp.YouCtrl`, `Land.YouCtrl`, `Mountain.YouCtrl,Forest.YouCtrl`, `Mountain.YouCtrl,Plains.YouCtrl`, `Plains.YouCtrl`, `Plains.YouCtrl,Island.YouCtrl`, `Plains.YouCtrl,Swamp.YouCtrl`, `Swamp.YouCtrl`, `Swamp.YouCtrl,Forest.YouCtrl`, `Swamp.YouCtrl,Mountain.YouCtrl`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PersistentMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `A Thousand Souls Die Every Day —`, `Corrupted —`, `Devouring Monster —`, `Domain —`, `Ferocious —`, `Formidable —`, `Genomic Enhancement —`, `Grand Summon —`, `Max speed —`, `Metalcraft —`, `Psychic Stimulus —`, `Secrets of the Soul —`, `Sonic Rainboom —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE5`, `GE7`
- `Produced$`: TODO: Describe this parameter.
  Observed values: `Any`, `B`, `B G`, `B R`, `B R G`, `C`, `C B`, `C C`, `C C R`, `C G`, `C G U`, `C R`, `C U`, `C W`, `Chosen`, `Combo Any`, `Combo AnyDifferent`, `Combo B Chosen`, `Combo B G`, `Combo B G U`, `Combo B R`, `Combo B R G`, `Combo Chosen`, `Combo ColorID`, `Combo ColorIdentity`, `Combo G B`, `Combo G Chosen`, `Combo G U`, `Combo G U R`, `Combo G W`, `Combo G W U`, `Combo NotedColors`, `Combo R Chosen`, `Combo R G`, `Combo R G W`, `Combo R W`, `Combo R W B`, `Combo U B`, `Combo U B R`, `Combo U Chosen`, `Combo U G`, `Combo U R`, `Combo U R W`, `Combo W B`, `Combo W B G`, `Combo W B G C`, `Combo W Chosen`, `Combo W G`, `Combo W U`, `Combo W U B`, `Combo W U G`, `G`, `G G`, `G U`, `G U R`, `G W`, `G W U`, `R`, `R G`, `R G W`, `R G W U`, `R R`, `R R R G G G`, `R R R R R R R R`, `R W`, `R W B`, `Special DoubleManaInPool`, `Special EachColorAmong_ExiledWith`, `Special EachColorAmong_Valid Permanent.YouCtrl`, `Special EachColorAmong_Valid Permanent.YouCtrl+MonoColor`, `Special EachColoredManaSymbol_Milled`, `Special EnchantedManaCost`, `Special LastNotedType`, `U`, `U B`, `U B R`, `U R`, `U R W`, `U U`, `U U R R R`, `W`, `W B`, `W U`, `W U B`, `W U B R G`, `W W U U B B R R G G`, `W W W`
- `RestrictValid$`: TODO: Describe this parameter.
  Observed values: `Activated`, `Activated.Artifact`, `Activated.Artifact+inZoneBattlefield`, `Activated.Land`, `CantCastNonArtifactSpells`, `CantCastSpellFromHand`, `CantPayGenericCosts`, `CostContainsX`, `CumulativeUpkeep`, `nonSpell`, `Spell`, `Spell.!wasCastFromYourHand`, `Spell.Ally`, `Spell.Ally,Activated.Ally`, `Spell.Angel`, `Spell.Artifact`, `Spell.Artifact,Activated`, `Spell.Artifact,Activated.Artifact`, `Spell.Artifact,Activated.Artifact+inZoneBattlefield`, `Spell.Artifact,Spell.Creature`, `Spell.Assassin,Spell.withFreerunning,Activated.Assassin`, `Spell.Aura,Spell.Equipment`, `Spell.ChosenColor+MonoColor`, `Spell.ChosenType`, `Spell.ChosenType,Activated.ChosenType`, `Spell.Cleric,Spell.Rogue,Spell.Warrior,Spell.Wizard,Activated.Cleric+inZoneBattlefield,Activated.Rogue+inZoneBattlefield,Activated.Warrior+inZoneBattlefield,Activated.Wizard+inZoneBattlefield`, `Spell.cmcGE4`, `Spell.Colorless`, `Spell.Colorless,Activated`, `Spell.Colorless,Activated.Permanent+Colorless+inZoneBattlefield,CostContainsC`, `Spell.Creature`, `Spell.Creature+Blue`, `Spell.Creature+ChosenType`, `Spell.Creature+ChosenType,Activated.Creature+ChosenType`, `Spell.Creature+ChosenType,Spell.Creature+Legendary`, `Spell.Creature+cmcGE4,Spell.Creature+hasXCost`, `Spell.Creature+Dragon`, `Spell.Creature+Elf`, `Spell.Creature+NoAbilities`, `Spell.Creature+Phyrexian`, `Spell.Creature,Activated.Creature`, `Spell.Creature,Activated.Creature+inZoneBattlefield`, `Spell.Creature,Spell.Enchantment`, `Spell.Demon,Spell.Cleric,Spell.Vampire`, `Spell.Dinosaur,Activated.Dinosaur`, `Spell.Disturb,Spell.Instant,Spell.Sorcery`, `Spell.Dragon`, `Spell.Dragon,Activated.Dragon+inZoneBattlefield`, `Spell.Dragon,Spell.Omen`, `Spell.Eldrazi+Colorless,Activated.Eldrazi+Colorless+inZoneBattlefield`, `Spell.Elemental,Activated.Elemental`, `Spell.Elemental,Activated.Elemental+inZoneBattlefield`, `Spell.Elemental,Spell.Planeswalker+Chandra`, `Spell.Enchantment,Static.Unlock,Static.isTurnFaceUp`, `Spell.Equipment,Activated.Equip`, `Spell.hasXCost,Spell.cmcGE5`, `Spell.Instant,Spell.Sorcery`, `Spell.Instant,Spell.Sorcery,Activated.ClassLevelUp`, `Spell.Instant,Spell.Sorcery,Spell.Demon,Spell.Spirit`, `Spell.isCastFaceDown+Creature,Static.ManifestUp+Creature,Static.MorphUp`, `Spell.isCastFaceDown,Static.isTurnFaceUp+Creature`, `Spell.IsCommander+YouOwn`, `Spell.IsRemembered`, `Spell.Kicked`, `Spell.Kicked,Spell.Instant,Spell.Sorcery`, `Spell.Knight,Spell.Equipment`, `Spell.Legendary`, `Spell.Lesson`, `Spell.Lesson,Spell.Shrine`, `Spell.Mount`, `Spell.Mount,Spell.Vehicle`, `Spell.MultiColor`, `Spell.Myr,Activated.Myr+inZoneBattlefield`, `Spell.Ninja,Spell.Turtle`, `Spell.nonColorless+!hasXCost`, `Spell.nonCreature`, `Spell.numColorsEQ3`, `Spell.Outlaw,Activated.Outlaw`, `Spell.Planeswalker`, `Spell.Sliver`, `Spell.Time Lord,Spell.Alien,Activated.Time Lord+inZoneBattlefield,Activated.Alien+inZoneBattlefield`, `Spell.Vampire`, `Spell.Vehicle,Spell.Pilot`, `Spell.wasCastFromExile`, `Spell.wasCastFromGraveyard+withFlashback`, `Spell.wasCastFromYourGraveyard`, `Spell.withDevoid`, `Spell.YouDontOwn`, `Static.Foretelling,Spell.Instant,Spell.Sorcery`, `Static.Foretelling,Spell.withForetell`, `Static.isTurnFaceUp`, `Static.Unlock,Spell.Room`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AddCounter`, `ChangeControl`, `CheckPlus`, `ChooseColor`, `DBAnimate`, `DBAnimateAll`, `DBChange`, `DBCleanup`, `DBConvert`, `DBCounter`, `DBDamageAll`, `DBDealDamage`, `DBDraft`, `DBDraw`, `DBEffect`, `DBEffectAddCounter`, `DBExile`, `DBExileSelf`, `DBGainLife`, `DBImmediateTrig`, `DBIntensify`, `DBLife`, `DBLoseLife`, `DBMana`, `DBMetalWorkerCleanup`, `DBPain`, `DBPlay`, `DBPump`, `DBPutCounter`, `DBRadiation`, `DBReturn`, `DBRollDice`, `DBSac`, `DBScry`, `DBStayTapped`, `DBSubCounter`, `DBTearUpAndRemove`, `DBTrigger`, `DelTrigSlowtrip`, `ManaB`, `RevealUntil`, `SubMana`, `TrigRemove`, `ValeTrig`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE6`, `GE8`
- `TriggersWhenSpent$`: TODO: Describe this parameter.
  Observed values: `TrigChange`, `TrigCopy`, `TrigScry`, `TrigSpent`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `AddCounter<1/P1P1/CARDNAME>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `TriggeredPlayer`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `XMin$`: TODO: Describe this parameter.
  Observed values: `1`

## `ManaReflected`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `3`, `IncubationAmount`
- `ColorOrType$`: TODO: Describe this parameter.
  Observed values: `Color`, `Type`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T untapYType<1/Land.OppCtrl/land>`, `T`, `T PayLife<1>`, `Sac<1/Land>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TriggeredActivator`, `TriggeredCardController`, `You`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+hasAbility Activated.otherAbility`
- `Produced$`: TODO: Describe this parameter.
  Observed values: `Combo`
- `ReflectProperty$`: TODO: Describe this parameter.
  Observed values: `Is`, `Produce`, `Produced`
- `RestrictValid$`: TODO: Describe this parameter.
  Observed values: `Activated.Creature+inZoneBattlefield`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDealDamage`, `DBMove`, `DBPump`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Basic.YouCtrl`, `Creature.Legendary+YouCtrl,Planeswalker.Legendary+YouCtrl`, `Defined.ExiledWith`, `Defined.Imprinted`, `Defined.Sacrificed`, `Defined.Self`, `Defined.Untapped`, `Defined.ValidGraveyard Card.YouOwn`, `Defined.ValidGraveyard Creature.Legendary+YouOwn`, `Gate.YouCtrl`, `Land.OppCtrl`, `Land.YouCtrl`, `Permanent.Legendary+YouCtrl`, `Permanent.YouCtrl`

## `Manifest`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `X`, `Y`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Card.TargetedPlayerOwn`, `Card.YouCtrl`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W`, `1 B T Sac<1/Creature.Other/another creature>`, `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `ValidHand Card.YouOwn`, `ValidLibrary Card.TopLibrary+ActivePlayerCtrl`, `ValidLibrary Card.TopLibrary+ControlledBy TriggeredTarget`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `TargetedController`, `You`
- `RememberManifested$`: TODO: Describe this parameter.
  Observed values: `True`
- `Shuffle$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Aurify`, `DBCleanup`, `DBClearBolas`, `DBDigRemaining`, `DBDraw`, `DBDrawSeven`, `TrigPutCounter`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `ManifestDread`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `DefinedPlayer$`: TODO: Describe this parameter.
  Observed values: `RememberedOwner`, `TargetedController`
- `RememberManifested$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBAttach`, `DBChangeZone`, `DBCleanup`, `DBPutCounter`, `DBPutCounters`, `DBTurnFaceUp`

## `Meld`

TODO: Write documentation.

**Parameters:**
- `Attacking$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+YouCtrl+YouOwn`, `Card.Self+YouCtrl+YouOwn+attacking`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 R R T`, `7`, `3 B G`
- `Name$`: TODO: Describe this parameter.
  Observed values: `Brisela, Voice of Nightmares`, `Chittering Host`, `Hanweir, the Writhing Township`, `Mishra, Lost to Phyrexia`, `Ragnarok, Divine Deliverance`, `Titania, Gaea Incarnate`, `Urza, Planeswalker`
- `Primary$`: TODO: Describe this parameter.
  Observed values: `Gisela, the Broken Blade`, `Graf Rats`, `Hanweir Battlements`, `Mishra, Claimed by Gix`, `Titania, Voice of Gaea`, `Urza, Lord Protector`, `Vanille, Cheerful l'Cie`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `Argoth, Sanctum of Nature`, `Bruna, the Fading Light`, `Fang, Fearless l'Cie`, `Hanweir Garrison`, `Midnight Scavengers`, `Phyrexian Dragon Engine`, `The Mightstone and Weakstone`
- `SecondaryType$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Land`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`

## `Mill`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `LilianaMill`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `B`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.kicked`, `Card.Land`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/Creature>`, `3`, `SubCounter<1/LOYALTY>`, `B`, `Sac<1/Food>`, `T`, `3 T`, `1 U T`, `1 U B`, `2 U T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `ParentTarget`, `Player`, `Player.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Remembered`, `ReplacedPlayer`, `ReplacedTarget`, `SourceController`, `Targeted`, `TargetedController`, `TargetedOwner`, `TriggeredActivator`, `TriggeredAttackerController`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `You`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `Imprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `TgtChoose`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `2`
- `NoReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `12`, `13`, `14`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `JoinForcesAmount`, `PhenaxToughness`, `Result`, `VoteNum`, `X`, `Y`, `Z`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Translocation Protocols —`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `Count$Valid Creature.Legendary+YouCtrl`
- `RememberMilled$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowMilledCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DamageOpponent`, `DBAccumulateX`, `DBAmass`, `DBBranch`, `DBCast`, `DBChange`, `DBChangeZone`, `DBChangeZone1`, `DBChangeZone2`, `DBChangeZoneAll`, `DBChoose`, `DBCleanup`, `DBConjure`, `DBCounter`, `DBDamage`, `DBDestroy`, `DBDig`, `DBDiscard`, `DBDraw`, `DBEffect`, `DBEnergy`, `DBExile`, `DBExileGrave`, `DBExileSK`, `DBForEach`, `DBGainLife`, `DBHereticDamage`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBIncubate`, `DBInvestigate`, `DBLifeDrain`, `DBLifeGain`, `DBLoseLife`, `DBMillKicked`, `DBPlay`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBPutCounter1`, `DBRandom`, `DBRepeatEach`, `DBReset`, `DBReturn`, `DBReturnAura`, `DBSacrifice`, `DBScry`, `DBSelfSac`, `DBToken`, `DBTransform`, `DBUnblockable`, `DBUntap`, `DBYouGainLife`, `DelTrig`, `DelTrigSlowtrip`, `FishyCast`, `Treasure`, `TrigDraw`, `TrigImmediateTrig`, `TrigToken`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MaxTgt`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `DamageYou<6>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `MoveCounter`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `FromValid`, `ToValid`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `X T`, `1 U T`, `T`, `2`, `1 BG BG`, `U T`, `U Q`, `4 W`, `1 G`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `All`, `Any`, `X`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `All`, `Any`, `EachNotOn`, `LOYALTY`, `P1P1`, `SHIELD`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self`, `Targeted`, `TriggeredCardLKICopy`
- `NonZero$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberPut$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Source$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Self`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDraw`, `DBGainLife`, `DBPump`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetsWithSameController$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidDefined$`: TODO: Describe this parameter.
  Observed values: `Creature.Other`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.YouCtrl`, `Permanent.YouCtrl+Other+counters_GE1_P1P1`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `another creature`, `nonland permanent you control (move counters)`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.Other`, `Creature`, `Creature.Other`, `Creature.YouCtrl`, `Permanent`, `Permanent.nonLand+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+Other`

## `MultiplePiles`

TODO: Write documentation.

**Parameters:**
- `ChosenPile$`: TODO: Describe this parameter.
  Observed values: `DBSacrifice`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`
- `Piles$`: TODO: Describe this parameter.
  Observed values: `3`
- `RandomChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`

## `MultiplyCounter`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`, `GE1`, `GE10`, `GE6`, `GTY`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T Sac<1/Permanent.token/token>`, `3 G G`, `4 G G`, `2 G U`, `T`, `2 GU Q`, `2 T`, `G U T`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `GROWTH`, `P1P1`, `TIME`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Remembered`, `Self`, `Targeted`, `Targeted.Mutant,Targeted.Ninja,Targeted.Turtle`, `TriggeredAttackerLKICopy`, `TriggeredSourceLKICopy`, `Valid Creature.YouCtrl`, `Valid Spider.YouCtrl,Creature.Legendary+YouCtrl`, `You`
- `Multiplier$`: TODO: Describe this parameter.
  Observed values: `2`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCopyPermanents`, `DBDraw`, `DBEffect`, `DBToken`, `ScrollsOfLife`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`, `MaxTargets`, `MaxTgt`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `another creature`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature,Land`, `Creature`, `Creature.Other`, `Creature.YouCtrl`, `Creature.YouCtrl,Artifact.YouCtrl`, `Permanent`, `Permanent.YouCtrl`

## `MustBlock`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AllowNonLethal`
- `BlockAllDefined$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Creature.untapped+DefenderCtrl`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `TriggeredDefendingPlayer`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1`, `2 G`, `Sac<1/Food>`, `G`, `R`, `1 G`, `3 U U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Valid Creature.counters_GE1_MAGNET`
- `DefinedAttacker$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `Valid Card.attacking`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `UntilEndOfCombat`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Formidable —`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.Artifact`, `Creature.DefenderCtrl`, `Creature.OppCtrl`

## `NameCard`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `BestCreatureInComputerDeck`, `CursedScroll`, `MostProminentInComputerDeck`, `MostProminentInComputerDeckNonToken`, `MostProminentInHumanDeck`, `PhyrexianRevoker`, `PithingNeedle`, `RandomInComputerDeck`, `SorcerousSpyglass`
- `AtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChooseFromDefinedCards$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ChooseFromList$`: TODO: Describe this parameter.
  Observed values: `Arcades Sabboth,Chromium,Nicol Bolas,Palladia-Mors,Vaevictis Asmadi`, `Disenchant,Braingeyser,Terror,Shivan Dragon,Regrowth,Black Lotus`, `Emrakul; the Promised End`, `Enlightened Tutor,Mystical Tutor,Booster Tutor,Imperial Recruiter,Worldly Tutor`, `Piracy Charm,Sapphire Charm,Trickery Charm,Vision Charm`, `Righteous Confluence,Mystic Confluence,Wretched Confluence,Fiery Confluence,Verdant Confluence,Brokers Confluence,Cabaretti Confluence,Maestros Confluence,Obscura Confluence,Riveteers Confluence`, `Thoughtseize,Lightning Bolt,Abrupt Decay`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T`, `T`, `1 T`, `1 B T Discard<1/Card>`, `SubCounter<3/LOYALTY>`, `2 T`, `X T`, `X`, `AddCounter<1/LOYALTY>`, `2 T Exile<1/CARDNAME>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player`, `TriggeredTarget`, `You`
- `ExcludeChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `SelectPrompt$`: TODO: Describe this parameter.
  Observed values: `Choose a card other than a basic land card to ban`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChooseCT`, `ChooseP`, `CreateAbility`, `DBCast`, `DBChangeZone`, `DBChooseNumber`, `DBCleanup`, `DBClear`, `DBConjure`, `DBCopy`, `DBDementiaReveal`, `DBDig`, `DBDigEach`, `DBDigUntil`, `DBDiscard`, `DBEffect`, `DBExile`, `DBGoad`, `DBGuess`, `DBMake`, `DBMill`, `DBRemove`, `DBReveal`, `DBRevealHand`, `DBSearch`, `DBTarget`, `ExileHand`, `ExileYard`, `FindThePrecious`, `RevealHand`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Card.Artifact`, `Card.Creature`, `Card.Land+nonBasic`, `Card.ManaCost=Imprinted`, `Card.nonBasic`, `Card.nonLand`, `Card.nonLand+nonArtifact`, `Card.nonLand+nonCreature`, `Creature`, `Creature.cmcEQM`, `Creature.cmcEQX`, `Creature.ManaCost=Equipped`, `Land`
- `ValidDescription$`: TODO: Describe this parameter.
  Observed values: `a card name other than a basic land card name`, `artifact`, `card other than a basic land`, `Choose a noncreature, nonland card name.`, `creature`, `creature card`, `land card`, `nonartifact, nonland`, `nonbasic land`, `nonland`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `OpenAttraction`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`
- `SpellDescription$`: TODO: Describe this parameter.

## `PeekAndReveal`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `InstantOrSorcery`, `Main2`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `ColorAmount`, `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`, `GE3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T PayEnergy<6>`, `1 U`, `1 T`, `1`, `2`, `3 T`, `4 T`, `U T`, `2 U U SubCounter<1/WISH>`, `AddCounter<1/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Remembered`, `RememberedPlayer`, `ReplacedPlayer`, `Targeted`, `TargetedAndYou`, `TriggeredPlayer`, `You`
- `ImprintRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoPeek$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoReveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `PeekAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `2`, `20`, `3`, `4`, `5`, `6`, `7`, `9`, `ShiftX`, `WarpX`, `X`, `Y`
- `PeekNum$`: TODO: Describe this parameter.
  Observed values: `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Parley —`
- `RememberPeeked$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Reveal$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealValid$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature`, `Card`, `Card.ChosenType`, `Card.Instant,Card.Sorcery`, `Card.Mount`, `Card.nonCreature+nonLand`, `Card.sharesCreatureTypeWith`, `Creature`, `Creature,Planeswalker`, `Creature.ChosenType`, `Land`, `Snow`, `Zombie`
- `SourceZone$`: TODO: Describe this parameter.
  Observed values: `PlanarDeck`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CastCard`, `ChooseNonLand`, `CloneArmy`, `DBAnimate`, `DBBottom`, `DBCandlesChangeZone`, `DBChangeCreatures11M`, `DBChangeZone`, `DBChangeZone1`, `DBCheckLibrary`, `DBChoice`, `DBChoose`, `DBCleanImprint`, `DBClone`, `DBCopyCast`, `DBCounter`, `DBCreature`, `DBDamage`, `DBDamageAll`, `DBDiscard`, `DBDraw`, `DBEnduringGraveyard`, `DBExile`, `DBGainLife`, `DBInvestigate`, `DBLife`, `DBLoseLife`, `DBMana`, `DBMayCast`, `DBMill`, `DBPetalChoose`, `DBPlay`, `DBProd`, `DBPump`, `DBPutCounter`, `DBPutRevealed`, `DBRepeat`, `DBRepeatEach`, `DBRepeatTypes`, `DBReveal`, `DBRevealHand`, `DBRunChaos`, `DBSac`, `DBSacrifice`, `DBShuffle`, `DBToHand`, `DBToken`, `DBTransform`, `DBTwoPile`, `DBTwoPiles`, `DBTwoPiles9M`, `DBUntap`, `DelTrigSlowtrip`, `DestructiveParoxysm`, `ExileDown`, `GoToBattlefield`, `PickOne`, `Separate`, `TelepathCast`, `TrigPlay`, `TrigRepeatTypes`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `PermanentCreature`

TODO: Write documentation.

**Parameters:**
- `AdditionalDesc$`: TODO: Describe this parameter.
  Observed values: `This spell costs {1} less to cast for each permanent sacrificed this way.`, `This spell costs {2} less to cast for each card exiled this way.`, `This spell costs {2} less to cast for each counter removed this way.`, `This spell costs {2} less to cast for each creature sacrificed this way.`, `This spell costs {2} less to cast for each permanent sacrificed this way and {2} less to cast for each other artifact or creature you've sacrificed this turn.`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `MostProminentOnBattlefield`, `SacToReduceCost`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 U ExileFromGrave<6/Card>`, `4 B B Sac<1/Creature>`, `2 G ChooseCreatureType<1>`, `U ExileFromGrave<1/Creature>`, `6 R Sac<X/Artifact;Creature/any number of artifacts and/or creatures>`, `2 B B Sac<1/Creature>`, `4 W W Exile<1/Creature>`, `2 G tapXType<2/Creature;Land/creatures and/or lands>`, `1 U Return<1/Permanent/permanent>`, `6 B B ExileFromGrave<X/Creature/creature cards>`
- `ManaRestriction$`: TODO: Describe this parameter.
  Observed values: `Creature.inZoneBattlefield`, `Land.Basic`, `None`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Frenzied Metabolism —`
- `SpellDescription$`: TODO: Describe this parameter.

## `PermanentNoncreature`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Never`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `B B B`

## `Phases`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DontPhaseOut`
- `AllValid$`: TODO: Describe this parameter.
  Observed values: `Artifact.!token`, `Creature`, `Creature.!token`, `Creature.hasKeywordPhasing,Card.phasedOutCreature`, `Creature.TargetedPlayerCtrl`, `Enchantment.nonAura+!token`, `Land.!token`, `Permanent.Other+!IsRemembered`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `Exiled`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many blue cards to exile`
- `AnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Black`, `Card.Self`, `Card.Self+PromisedGift`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W`, `2 T`, `4`, `3 U U`, `U U`, `1 W`, `SubCounter<3/LOYALTY>`, `SubCounter<8/LOYALTY>`, `U U T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `Enchanted`, `Equipped`, `Remembered`, `Self`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `TriggeredTargetLKICopy`, `Valid Land.YouCtrl`, `Valid Permanent.IsRemembered+YouCtrl`, `Valid Permanent.YouCtrl`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `PhaseInOrOut$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Astral Projection —`, `Teleport —`
- `RememberAffected$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberValids$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChooseArtifact`, `ChooseCreature`, `DBChange`, `DBCleanup`, `DBDamageAll`, `DBEffect`, `DBExile`, `DBExileSelf`, `DBPhaseOutAll`, `DBPhaseSelf`
- `Tapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MaxTgts`, `X`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`, `Y`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2 G U`, `U U`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature,Land`, `Creature`, `Creature.!IsRemembered`, `Creature.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.Other+YouCtrl`, `Creature.Other,Artifact.Other,Enchantment.Other`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Opponent`, `Permanent`, `Permanent.nonLand+Other`, `Permanent.nonLand+YouCtrl`, `Player`
- `WontPhaseInNormal$`: TODO: Describe this parameter.
  Observed values: `True`

## `Planeswalk`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `IdolX`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `DontPlaneswalkAway$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ClearImprinted`, `DBCleanup`

## `Play`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `NeedsChosenCard`, `ReplaySpell`, `WithTotalCMC`
- `AllowRepeats$`: TODO: Describe this parameter.
  Observed values: `True`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `All`, `ChandraX`, `X`
- `AnySupportedCard$`: TODO: Describe this parameter.
  Observed values: `Instant`, `Names:Hellion Eruption,Insurrection,Warp World`, `Names:Ignorant Bliss,Crack the Earth,Blazing Volley`, `Names:Seething Song,Dance with Devils,Flamebreak`, `Sorcery`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CastFaceDown$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChoiceNum$`: TODO: Describe this parameter.
  Observed values: `1`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `HandSize`, `X`, `Y`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE10`, `GE20`, `GE9`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Remembered`, `TopOfLibrary`, `TriggeredCard`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.cmcGT4+nonLand`, `Card.cmcGTX+nonLand`, `Card.cmcLE4+nonLand`, `Card.cmcLEX+nonLand`, `Card.cmcOdd`, `Card.IsImprinted+sharesNameWith TriggeredCard`, `Card.IsRemembered`, `Card.nonLand`, `Card.Self+counters_GE4_CHORUS`, `Card.sharesCardTypeWith TriggeredCard`, `Card.YouOwn`, `Creature.sharesCreatureTypeWith Valid Creature.YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+powerGE7`, `Instant,Sorcery`, `Permanent`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ4`, `GE10`, `GE11`, `GE3`, `GE4`, `GE6`, `GE7`, `GTY`, `LE13`, `LE20`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Hand`
- `ControlledByPlayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `Controller$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `RememberedController`, `RememberedOwner`, `Targeted`, `TargetedController`, `TargetedPlayer`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredPlayer`, `You`
- `CopyCard$`: TODO: Describe this parameter.
  Observed values: `True`
- `CopyFromChosenName$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<7/LOYALTY>`, `ExileFromGrave<1+/Card.Black+withTotalManaSymbols_Black_GE15>`, `SubCounter<2/LOYALTY>`, `ExileFromGrave<1/Permanent>`, `2 T`, `T`, `X T`, `3 U U T`, `W U B R G`, `B T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Exile any number of black cards from your graveyard with fifteen or more black mana symbols among their mana costs:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRemembered`, `Enchanted`, `ExiledCards`, `ExiledWith`, `ExiledWithSource`, `Imprinted`, `Remembered`, `Remembered.!ChosenCard`, `Remembered.ExiledWithSource`, `Remembered.nonLand+sharesCardTypeWith ReplacedSource`, `RememberedLKI`, `Self`, `Targeted`, `TopOfLibrary`, `TriggeredCard`, `ValidExile Card.IsImprinted`, `ValidExile Card.IsImprinted+!sharesNameWith TriggeredCard`
- `DefinedDesc$`: TODO: Describe this parameter.
  Observed values: `it`, `that card`, `the exiled card`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Battlefield`
- `ExileOnMoved$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ForgetPlayed$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `if it's an instant spell with mana value 2 or less`, `if there are four or more chorus counters on NICKNAME`
- `ImprintPlayed$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouOwn`
- `ManaConversion$`: TODO: Describe this parameter.
  Observed values: `AnyType->AnyType`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayCost$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `Discard<1/Card>`, `PayEnergy<ConvertedManaCost>`, `PayLife<ConvertedManaCost>`, `SuspendCost`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayRaiseCost$`: TODO: Describe this parameter.
  Observed values: `R R`
- `PlayReduceCost$`: TODO: Describe this parameter.
  Observed values: `2`, `4`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Descend 8`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `RandomCopied$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomNum$`: TODO: Describe this parameter.
  Observed values: `3`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `RememberPlayed$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceGraveyard$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `ReplaceGraveyardValid$`: TODO: Describe this parameter.
  Observed values: `Instant,Sorcery`
- `ReplaceIlluMask$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCards$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`
- `ShowCardToActivator$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CascadeMoveToLib`, `DBBottom`, `DBChange`, `DBChangeZone`, `DBChangeZone2`, `DBCleanup`, `DBCleanup1`, `DBCleanup2`, `DBConvert`, `DBCopy`, `DBDamage`, `DBDraw`, `DBEffect`, `DBExile`, `DBExileEffect`, `DBExileIfNotPlayed`, `DBExileSelf`, `DBGiveHaste`, `DBGrave`, `DBHand`, `DBHellCleanup`, `DBIncrease`, `DBInvestigate`, `DBKnowledgeCleanup`, `DBLibrary`, `DBLoseLife`, `DBLosePerpAbility`, `DBNoUntap`, `DBOmenCleanup`, `DBPump`, `DBPutHand`, `DBRepeatTwo`, `DBRestRandomOrder`, `DBReturn`, `DBReturnHand`, `DBRonaCleanup`, `DBScry`, `DBShuffle`, `DBToken`, `DBTokenIfNotPlayed`, `ExileMe`, `ExileSelf`, `MoveLand`, `PlayLandIfNotCast`, `PutRestBackBottomLibrary`, `Shuffle`, `TrigDT`, `TrigSpellweaverCopySame`, `YouShuffle`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `OneEach`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `W U B R G`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `Valid$`: TODO: Describe this parameter.
  Observed values: `Ally.YouOwn+ExiledWithSource`, `Artifact.ExiledWithSource,Instant.ExiledWithSource,Sorcery.ExiledWithSource`, `Artifact.YouOwn`, `Aura.IsRemembered`, `Card`, `Card.ChosenCard`, `Card.ControlledBy TriggeredTarget`, `Card.counters_GE1_PAGE`, `Card.Creature+YouOwn+CanPayManaCost`, `Card.Eldrazi+YouOwn`, `Card.ExiledWithSource`, `Card.faceUp+OwnedBy Player.Opponent`, `Card.IsCommander+YouOwn`, `Card.IsImprinted`, `Card.IsImprinted+!IsRemembered+nonLand`, `Card.IsImprinted+ExiledWithSource`, `Card.IsImprinted+YouOwn`, `Card.IsRemembered`, `Card.IsRemembered+ExiledWithSource`, `Card.IsRemembered+nonLand`, `Card.IsRemembered+YouOwn`, `Card.Legendary+YouOwn`, `Card.nonCreature+nonLand+IsRemembered`, `Card.nonLand+ExiledWithSource`, `Card.nonLand+IsRemembered`, `Card.nonLand+IsRemembered+cmcLEX`, `Card.nonLand+IsRemembered+YouOwn+cmcLE10`, `Card.nonLand+IsRemembered+YouOwn+cmcLE5`, `Card.nonLand+OwnedBy TriggeredTarget`, `Card.nonLand+sharesNameWith ThisTurnCast`, `Card.nonLand+YouOwn`, `Card.nonLand+YouOwn+sharesCardTypeWith TriggeredCard`, `Card.Self`, `Card.TargetedPlayerCtrl`, `Card.withSuspend`, `Card.YouCtrl`, `Card.YouCtrl+cmcEQX`, `Card.YouCtrl+nonLand`, `Card.YouOwn`, `Card.YouOwn+counters_GE1_DREAM`, `Card.YouOwn+counters_GE1_KICK`, `Card.YouOwn+nonLand`, `Card.YouOwn+NotedForArcaneSavant`, `Creature.YouCtrl+cmcLEX,Instant.YouCtrl+cmcLEX,Sorcery.YouCtrl+cmcLEX,Planeswalker.YouCtrl+cmcLEX`, `Creature.YouOwn+counters_GE1_HATCHING`, `Instant.ExiledWithSource,Sorcery.ExiledWithSource`, `Instant.IsRemembered,Sorcery.IsRemembered`, `Instant.Red+YouCtrl,Sorcery.Red+YouCtrl`, `Instant.TargetedPlayerCtrl,Sorcery.TargetedPlayerCtrl`, `Instant.YouCtrl+cmcLEX,Sorcery.YouCtrl+cmcLEX`, `Instant.YouOwn+cmcLE4,Sorcery.YouOwn+cmcLE4`, `Permanent.YouOwn`, `Permanent.YouOwn+cmcLEX`, `Sorcery.cmcLE3+IsRemembered+YouOwn`, `Sorcery.TargetedPlayerCtrl,Instant.TargetedPlayerCtrl`, `Sorcery.YouOwn+cmcLEX`, `Targeted.sharesCardTypeWith+YouCtrl`, `Vehicle.IsRemembered,Artifact.Creature+IsRemembered`
- `ValidSA$`: TODO: Describe this parameter.
  Observed values: `Instant,Sorcery`, `Instant.cmcEQ1,Instant.cmcEQ2,Sorcery.cmcEQ1,Sorcery.cmcEQ2`, `Instant.cmcEQY,Sorcery.cmcEQY`, `Instant.cmcLE2`, `Instant.cmcLE2,Sorcery.cmcLE2`, `Instant.cmcLEX,Sorcery.cmcLEX`, `Instant.cmcLEY,Sorcery.cmcLEY`, `Instant.cmcLEZ,Sorcery.cmcLEZ`, `Instant.YouOwn,Sorcery.YouOwn`, `Spell`, `Spell.cmcEQX`, `Spell.cmcLE2`, `Spell.cmcLE3`, `Spell.cmcLE4`, `Spell.cmcLE5`, `Spell.cmcLE8`, `Spell.cmcLEX`, `Spell.cmcLTX`, `Spell.Creature`, `Spell.Instant+cmcLEX,Spell.Sorcery+cmcLEX`, `Spell.Instant,Spell.Sorcery`, `Spell.nonCreature+YouOwn`, `SpellAbility.Land,Spell.cmcLEX`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `instant or sorcery card in your graveyard`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Card.namedPass the Torch+YouOwn`, `Card.nonCreature+cmcLE3+YouOwn`, `Card.nonLand+OwnedBy Spawner>TriggeredDefendingPlayer`, `Elemental.YouCtrl`, `Instant,Sorcery`, `Instant.cmcEQX,Sorcery.cmcEQX`, `Instant.OppCtrl,Sorcery.OppCtrl`, `Instant.OppOwn,Sorcery.OppOwn`, `Instant.OwnedBy Player.TriggeredTarget,Sorcery.OwnedBy Player.TriggeredTarget`, `Instant.OwnedBy TriggeredTarget,Sorcery.OwnedBy TriggeredTarget`, `Instant.Red+YouOwn,Sorcery.Red+YouOwn`, `Instant.YouCtrl`, `Instant.YouCtrl+cmcEQX,Sorcery.YouCtrl+cmcEQX`, `Instant.YouCtrl+cmcLE3,Sorcery.YouCtrl+cmcLE3`, `Instant.YouCtrl+cmcLE4,Sorcery.YouCtrl+cmcLE4`, `Instant.YouCtrl+cmcLEX,Sorcery.YouCtrl+cmcLEX`, `Instant.YouOwn`, `Instant.YouOwn+cmcLE3,Sorcery.YouOwn+cmcLE3`, `Instant.YouOwn,Sorcery.YouOwn`, `Instant.YouOwn,Sorcery.YouOwn,Artifact.YouOwn`, `Opponent`, `Permanent.nonLand+ControlledBy TriggeredTarget`, `Permanent.nonLand+YouOwn`, `Sorcery.YouOwn`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Exile`, `Graveyard`, `Graveyard,Exile`, `Graveyard,Hand`, `Hand`, `Hand,Graveyard`, `Hand,Graveyard,Exile`, `Library`, `Sideboard`
- `WithoutManaCost$`: TODO: Describe this parameter.
  Observed values: `True`
- `WithTotalCMC$`: TODO: Describe this parameter.
  Observed values: `10`, `6`, `X`
- `ZoneRegardless$`: TODO: Describe this parameter.
  Observed values: `True`

## `Poison`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LT9`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<9/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `ParentTarget`, `Player`, `Player.Opponent`, `Remembered`, `Targeted`, `TargetedController`, `TriggeredAttackingPlayer`, `TriggeredBlockerController`, `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `You`
- `Num$`: TODO: Describe this parameter.
  Observed values: `-X`, `1`, `2`, `3`, `Difference`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `CobraEffect`, `DBDraw`, `DBMill`, `RepeatPlayers`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `PreventDamage`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AlternateCost$`: TODO: Describe this parameter.
  Observed values: `W T`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `X`
- `CardChoices$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `CombatDamage$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `1 ExileFromGrave<1/Card.TopGraveyard>`, `2 T`, `W Sac<1/CARDNAME>`, `SubCounter<1/P1P0>`, `W Sac<1/Creature>`, `1 Sac<1/CARDNAME>`, `1 W`, `3 T`, `SubCounter<1/FADE>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `{1}, Exile the top card of your graveyard:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Remembered`, `Self`, `Valid Creature & Player`, `Valid Creature.YouCtrl`, `You`
- `DividedAsYouChoose$`: TODO: Describe this parameter.
  Observed values: `4`, `5`, `X`
- `InstantSpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerChoices$`: TODO: Describe this parameter.
  Observed values: `Player`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Domain —`, `Radiance —`, `Threshold —`
- `PreventionSubAbility$`: TODO: Describe this parameter.
  Observed values: `AcolytesRetribution`, `ArchonsVengeance`, `BoonEffect`, `EvenTemper`, `FaithsReward`, `GlowOfLife`, `ScarEffect`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShieldEffectTarget$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `Targeted`, `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`, `DBReturn`, `DBTap`, `DelTrigSlowtrip`, `GuardianEffect`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GTY`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `4`, `5`, `MaxTgts`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`, `Cleric,Wizard`, `Creature`, `Creature.Artifact`, `Creature.Legendary`, `Creature.Sliver,Player,Planeswalker`, `Creature.YouCtrl`, `Player,Planeswalker`

## `Proliferate`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `Number$2/Minus.Y`, `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.cmcLE3`, `Permanent.cmcLE3`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/CARDNAME>`, `4 T`, `1 G Sac<1/CARDNAME>`, `3`, `1 T Sac<1/Artifact.Other/other artifact>`, `tapXType<1/Card.Self/CARDNAME>`, `tapXType<3/Elf>`, `AddCounter<0/LOYALTY>`, `3 U`, `3 G U`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberPut$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`, `DBInvestigate`, `DBPhaseOut`, `DBPump`, `TrigProliferate2`

## `Protection`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `MostProminentHumanCreatures`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `AnyColor`, `AnyColor,Artifact`, `AnyColor,colorless`, `CardType`
- `Choser$`: TODO: Describe this parameter.
  Observed values: `Controller`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `FatefulHour`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GT5`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 Sac<1/CARDNAME>`, `1 W W`, `Sac<1/CARDNAME>`, `Sac<1/Creature.Other/another creature>`, `W`, `1 W`, `T`, `R`, `Discard<1/Random>`, `Sac<2/Land>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self`, `Targeted`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`
- `Gains$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `black`, `black,red`, `Choice`, `ChosenColor`, `Defined TriggeredCard`, `green,white`, `red`, `white`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBClash`, `DBCounter`, `DBDraw`, `DBGain`, `DBProtection`, `DBScry`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `X`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.Green`, `Creature.Other+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Creature.YouCtrl,Artifact.YouCtrl`, `Creature.YouCtrl,Enchantment.YouCtrl`, `Creature.YouCtrl,Planeswalker.YouCtrl`, `Merfolk.YouCtrl`, `Permanent.Goblin`, `Permanent.YouCtrl`

## `ProtectionAll`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `AnyColor`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `FatefulHour`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE5`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 W`, `T`
- `Gains$`: TODO: Describe this parameter.
  Observed values: `Choice`, `ChosenColor`, `TargetedCardColor`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Card.Ally+YouCtrl`, `Creature`, `Creature.White+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+Legendary`, `Permanent.YouCtrl`
- `ValidPlayers$`: TODO: Describe this parameter.
  Observed values: `You`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Permanent.YouCtrl`

## `Pump`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Threshold`
- `ActivationFirstCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->Combat Damage`, `BeginCombat->Declare Attackers`, `BeginCombat->EndCombat`, `Declare Attackers`, `Declare Blockers`, `Main2->Cleanup`, `Upkeep`, `Upkeep->BeginCombat`, `Upkeep->Declare Attackers`, `Upkeep->Declare Blockers`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AlwaysOnDiscard`, `AnyPhase`, `Aristocrat`, `AristocratCounters.Human`, `Berserk`, `BetterCreatureThanSource`, `ContinuousBonus`, `Curse`, `Damage`, `Destroy`, `DonateTargetPerm`, `DonateTargetPlayer`, `Fight`, `GideonBlackblade`, `HighestPower`, `InfernoOfTheStarMounts`, `Main1IfAble`, `Never`, `PowerDmg`, `PowerStruggle`, `Pummeler`, `Pump`, `ReplaySpell`, `SacOneEach`, `SameName`, `SwitchPT`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `Treasure`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Artifact.YouCtrl+cmcLE1`, `Card.IsCommander+YourTeamCtrl`, `Creature.OppCtrl+toughnessLE5`, `Creature.Other`, `Creature.YouCtrl+powerEQ2`, `Equipment.YouCtrl+!equipping`, `Human.YouOwn`
- `AlternateCost$`: TODO: Describe this parameter.
  Observed values: `G T`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `Exiled`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `how many green cards to exile`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Destroy`, `Exile`, `Library`, `Sacrifice`, `SacrificeCtrl`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CanBlockAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `CanBlockAny$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`, `X`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Player`
- `ClearNotedCardsFor$`: TODO: Describe this parameter.
  Observed values: `BattleBolas`, `BattleUgin`, `Discard`, `Diversion,Intelligence`, `ExileDraw`, `GreenAnchor,RedWaterfall`, `MaelstromArchangelAvatar`, `Money,Friends,Secrets`, `Silence,Snitch`, `Stargate`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `Delirium`, `Kicked`
- `ConditionActivationLimit$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `BogbrewWitchPresent`, `Doubles`, `MyPower`, `S`, `TreasureCheck`, `X`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE2`, `GE3`, `GT0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Remembered`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If a Dinosaur is dealt damage this way, CARDNAME gets +2/+0 until end of turn.`, `If CARDNAME was kicked,`, `If it was kicked,`, `If that card is a land card,`, `If you control a creature with power 4 or greater.`, `If you control a Mouse.`, `If {S} was spent to cast this spell,`, `Otherwise,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`, `G`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Ally`, `Artifact`, `Artifact.YouCtrl`, `Assassin`, `Card`, `Card.!Mount`, `Card.CastSa Spell.Warp`, `Card.Creature`, `Card.exploited`, `Card.Goblin+IsRemembered`, `Card.HasCounters`, `Card.Land`, `Card.nonLand`, `Card.Red`, `Card.Self`, `Card.Self+Aura`, `Card.Self+nonAura`, `Card.Self+PromisedGift`, `Card.wasCast`, `Card.White`, `Card.withoutSuspend`, `Cat`, `Contraption`, `Creature`, `Creature.Artifact`, `Creature.ControllerControlsIsland`, `Creature.Dinosaur`, `Creature.enchanted,Creature.Enchantment`, `Creature.IsImprinted+inZoneBattlefield`, `Creature.nonAngel`, `Creature.powerEQ2`, `Creature.powerGE1`, `Creature.powerGE4`, `Creature.withoutRampage`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+withDeathtouch`, `Creature.YouCtrl+withDouble Strike`, `Creature.YouCtrl+withFirst Strike`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withIndestructible`, `Creature.YouCtrl+withLifelink`, `Creature.YouCtrl+withMenace`, `Creature.YouCtrl+withTrample`, `Dwarf.YouCtrl`, `Elf.YouCtrl`, `Equipment`, `Forest.Snow`, `Goat`, `Human`, `Instant.YouOwn,Sorcery.YouOwn`, `Island`, `Knight`, `Land`, `Legendary`, `Mouse.YouCtrl`, `Orc,Goblin`, `Permanent.Snow+YouCtrl`, `Permanent.token`, `Rat.attacking`, `Spell.Creature`, `Spirit`, `Vampire`, `Vehicle,Creature`
- `ConditionPresent2$`: TODO: Describe this parameter.
  Observed values: `Enchantment.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE3`, `GE4`, `GE5`, `GT9`, `LE0`, `LT5`, `LT7`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `W T`, `1 B`, `PayLife<4>`, `1`, `W`, `U`, `1 T`, `Discard<1/Card>`, `R`, `PayEnergy<1>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `As an additional cost to cast this spell, discard a red or green card.`, `Exile the top creature card of your graveyard:`, `Grandeur — Discard another card named Tarox Bladewing:`, `Remove all +1/+1 counters from NICKNAME:`, `Remove two carrion counters from CARDNAME:`, `Tap an untapped snow land you control:`, `Tap any number of untapped creatures you control other than CARDNAME with total power 10 or greater:`, `Tap enchanted creature:`, `Tap enchanted land:`, `{1}, Exile the top card of your graveyard:`, `{1}, Reveal X green cards from your hand, Sacrifice CARDNAME:`, `{B}, {T}, Exile X cards from your graveyard:`, `{T}, Exile any number of cards from your graveyard:`, `{T}, Exile cards from your graveyard equal to the number of opponents you have:`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttachedBy Sacrificed & Valid Creature.sharesCreatureTypeWith AttachedBy Sacrificed`, `ChosenCard`, `DelayTriggerRememberedLKI`, `Enchanted`, `Equipped`, `ExiledCards.withoutSuspend`, `Imprinted`, `ParentTarget`, `Player`, `Player.!IsRemembered`, `Remembered`, `Remembered & Self`, `Remembered.!ChosenCard`, `Remembered.Creature`, `Remembered.withoutSuspend`, `RememberedLKI`, `ReplacedCard`, `RevealedCards.!Self`, `Self`, `Self & TriggeredCardLKICopy`, `Self & ValidLibrary Creature.YouOwn+TopLibrary_Creature.withoutFlying`, `Targeted`, `Targeted & Self`, `Targeted.ChosenType`, `Targeted.Creature`, `Targeted.RememberedPlayerCtrl`, `Targeted.Snake`, `Targeted.Vampire`, `TargetedCard`, `TargetedSource`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `TriggeredAttackers`, `TriggeredBlocker`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredCard & Remembered`, `TriggeredCardController`, `TriggeredCardLKICopy`, `TriggeredNewCardLKICopy`, `TriggeredObjectLKICopy`, `TriggeredSourceController`, `TriggeredSourceLKICopy`, `TriggeredSpellAbilityTargets`, `TriggeredTarget`, `TriggeredTargetLKICopy`, `Valid Ally.YouCtrl`, `Valid Card.ChosenCardStrict`, `Valid Creature.blockingRemembered`, `Valid Creature.StrictlyOther+YouCtrl`, `Valid Creature.TriggeredCrew`, `Valid Creature.YouCtrl`, `Valid Creature.YouCtrl+StrictlyOther`, `Valid Dragon.YouCtrl`, `Valid Planeswalker.YouCtrl`, `ValidLibrary Creature.TopLibrary_Creature+YouCtrl`, `You`, `You & Valid Permanent.YouCtrl`
- `DefinedKW$`: TODO: Describe this parameter.
  Observed values: `ChosenColor`, `ChosenPlayer`, `ChosenType`, `Opponent`, `RememberedController.Opponent`, `TargetedPlayer`, `You`
- `DefinedLandwalk$`: TODO: Describe this parameter.
  Observed values: `Sacrificed`
- `Description$`: TODO: Describe this parameter.
- `Duration$`: TODO: Describe this parameter.
  Observed values: `AsLongAsControl`, `Permanent`, `Perpetual`, `UntilEndOfCombat`, `UntilUntaps`, `UntilYourNextTurn`, `UntilYourNextUpkeep`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetImprinted$`: TODO: Describe this parameter.
  Observed values: `TriggeredCard`
- `ForgetObjects$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Imprinted`, `TriggeredCard`, `Valid Creature.RememberedPlayerCtrl`, `ValidHand Card.nonCreature+IsRemembered`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `Imprint$`: TODO: Describe this parameter.
  Observed values: `True`
- `ImprintCards$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Enchanted`, `Remembered`, `ReplacedCard`, `Targeted`, `TargetedSource`, `ThisTargetedCard`, `TriggeredCard`, `TriggeredSource`, `Valid Creature.!IsRemembered+ControlledBy RememberedController+!sharesCreatureTypeWith Remembered`, `Valid Creature.attacking`, `Valid Permanent.sharesNameWith Remembered+!IsRemembered`, `ValidAll Card.greatestRememberedCMC`, `ValidAll Card.IsRemembered+YouCtrl`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.powerGE4+Self`, `Card.Self+blocked`, `Card.Self+Creature`, `Card.Self+toughnessGE2`, `Creature.blockingSource`, `Creature.withFlying+OppCtrl`, `Creature.YouCtrl+withFlying`, `Demon.YouCtrl`, `Land.Snow+DefenderCtrl`, `Mountain.Snow+YouCtrl`
- `KW$`: TODO: Describe this parameter.
  Observed values: `"Left" pile`, `"Right" pile`, `Banding`, `Battle cry`, `Blitz:CardManaCost:Spell.Creature`, `CARDNAME can't attack.`, `CARDNAME can't block.`, `Casualty:2`, `Cumulative upkeep:1`, `Cumulative upkeep:2`, `Deathtouch`, `Deathtouch & HIDDEN CARDNAME must be blocked if able.`, `Deathtouch & Indestructible`, `Deathtouch & Lifelink`, `Decayed`, `Defender`, `Double Strike`, `Double Strike & Haste`, `Double Strike & Lifelink`, `Double Strike & Trample`, `Double team`, `Embalm:CardManaCost`, `Encore:CardManaCost`, `Equip:1`, `Escape:CardManaCost ExileFromGrave<2/Card.Other/other>`, `Escape:CardManaCost ExileFromGrave<3/Card.Other/other>`, `Fear`, `Fear & Vigilance`, `Firebending:2`, `Firebending:4`, `First Strike`, `First Strike & Deathtouch`, `First Strike & Double team`, `First Strike & Flying & Deathtouch & Double Strike & Haste & Hexproof & Indestructible & Lifelink & Menace & Protection & Reach & Trample & Vigilance`, `First Strike & Flying & Deathtouch & Double Strike & Haste & Hexproof & Indestructible & Lifelink & Menace & Reach & Trample & Vigilance`, `First Strike & Haste`, `First Strike & HIDDEN CARDNAME must be blocked if able.`, `First Strike & Lifelink`, `First Strike & Menace`, `First Strike & Reach`, `First Strike & Trample`, `First Strike & Vigilance`, `First Strike & Vigilance & Lifelink`, `Flanking`, `Flash`, `Flashback`, `Flashback:0`, `Flashback:2 R G`, `Flying`, `Flying & Double Strike`, `Flying & Double Strike & Haste`, `Flying & Double Strike & Vigilance`, `Flying & First Strike`, `Flying & First Strike & Lifelink`, `Flying & First Strike & Trample`, `Flying & First Strike & Trample & Haste & Protection from black & Protection from red & Vigilance`, `Flying & Indestructible`, `Flying & Lifelink`, `Flying & Menace`, `Flying & Prevent all combat damage that would be dealt to CARDNAME.`, `Flying & Prevent all damage that would be dealt to CARDNAME.`, `Flying & Shroud`, `Flying & Toxic:1`, `Flying & Vigilance`, `Harmonize`, `Haste`, `Haste & Menace`, `Haste & Myriad`, `Haste & Trample`, `Hexproof`, `Hexproof & Indestructible`, `Hexproof & Indestructible & Trample & Reach`, `Hexproof:Card.Black:black & Hexproof:Card.Blue:blue`, `Hexproof:ChosenColor`, `Hexproof:ChosenColor & Toxic:1`, `HIDDEN All creatures able to block CARDNAME do so.`, `HIDDEN CARDNAME can't attack or block.`, `HIDDEN CARDNAME can't attack.`, `HIDDEN CARDNAME can't block.`, `HIDDEN CARDNAME must be blocked if able.`, `HIDDEN CARDNAME's power and toughness are switched`, `HIDDEN Damage that would be dealt to CARDNAME can't be redirected.`, `HIDDEN During your next untap step, as you untap your permanents, return CARDNAME to its owner's hand.`, `HIDDEN This card doesn't untap during your next untap step.`, `Horsemanship`, `Indestructible`, `Indestructible & Deathtouch`, `Indestructible & HIDDEN All creatures able to block CARDNAME do so.`, `Infect`, `Intimidate`, `Intimidate & Haste`, `Jump-start`, `Landwalk:ChosenType`, `Landwalk:ChosenType.Snow:Snow ChosenType`, `Landwalk:Forest`, `Landwalk:Island`, `Landwalk:Mountain`, `Landwalk:Swamp`, `Lifelink`, `Lifelink & Deathtouch`, `Lifelink & Hexproof`, `Lifelink & Indestructible`, `Lifelink & Vigilance`, `Melee`, `Menace`, `Menace & Deathtouch`, `Menace & Haste`, `Menace & Lifelink`, `Mobilize:1`, `Myriad`, `Offspring:1`, `Persist`, `Prevent all combat damage that would be dealt by CARDNAME.`, `Prevent all combat damage that would be dealt to and dealt by CARDNAME.`, `Prevent all combat damage that would be dealt to CARDNAME.`, `Prevent all damage that would be dealt by CARDNAME.`, `Prevent all damage that would be dealt to and dealt by CARDNAME.`, `Prevent all damage that would be dealt to CARDNAME.`, `Protection from black`, `Protection from black & Protection from red`, `Protection from blue`, `Protection from each color`, `Protection from everything`, `Protection from green`, `Protection from red`, `Protection from red & Protection from blue & Protection from black & Protection from white & Protection from green`, `Protection:Creature`, `Protection:Creature.OppCtrl:creatures your opponents control`, `Protection:Player.OpponentOf PlayerUID_ChosenPlayerUID:all opponents of ChosenPlayerName`, `Protection:Player.PlayerUID_ChosenPlayerUID:ChosenPlayerName`, `Protection:Spell.Instant,Spell.Sorcery:instant spells and from sorcery spells`, `Rampage:2`, `Reach`, `Reach & Deathtouch`, `Reach & Trample`, `Reach & Trample & Indestructible`, `Rebound`, `Shadow`, `Shroud`, `Skulk`, `Storm`, `Suspend`, `Trample`, `Trample & Haste`, `Trample & Hexproof & Indestructible`, `Trample & HIDDEN All creatures able to block CARDNAME do so.`, `Trample & HIDDEN CARDNAME must be blocked if able.`, `Trample & Indestructible`, `Trample & Lifelink`, `Trample & Lifelink & Indestructible`, `Trample & Wither`, `Undying`, `Unearth:1 R`, `Unearth:CardManaCost`, `Vanishing`, `Vigilance`, `Vigilance & Haste`, `Vigilance & Indestructible & Haste`, `Vigilance & Lifelink`, `Vigilance & Lifelink & Indestructible`, `Vigilance & Menace`, `Vigilance & Reach`, `Vigilance & Trample`, `Vigilance & Trample & Lifelink & Indestructible & Haste`, `Wither`
- `KWChoice$`: TODO: Describe this parameter.
  Observed values: `Deathtouch,Lifelink`, `Double Strike,Lifelink`, `Double Strike,Protection from red,Vigilance,Shadow`, `Double Strike,Trample`, `First Strike,Lifelink`, `First Strike,Vigilance`, `First Strike,Vigilance,Lifelink`, `First Strike,Vigilance,Trample`, `Flying,Banding,First Strike,Trample`, `Flying,Deathtouch,Lifelink`, `Flying,First Strike,Haste`, `Flying,First Strike,Trample,Rampage:3`, `Flying,Lifelink`, `Flying,Menace,Haste`, `Flying,Trample,Haste`, `Flying,Vigilance,Deathtouch,Haste`, `Flying,Vigilance,Deathtouch,Lifelink`, `Flying,Vigilance,Lifelink`, `Haste,Prowess`, `Hexproof,Indestructible`, `Indestructible,Lifelink`, `Menace,Deathtouch,Lifelink`, `Menace,Lifelink`, `Menace,Lifelink,Haste`, `Reach,Trample,Haste`, `Vigilance,Lifelink,Haste`, `Vigilance,Lifelink,Hexproof`, `Vigilance,Lifelink,Indestructible`
- `LeaveBattlefield$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `6 G`
- `NoRepetition$`: TODO: Describe this parameter.
  Observed values: `True`
- `NoteCards$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`, `TriggeredSource`
- `NoteCardsFor$`: TODO: Describe this parameter.
  Observed values: `ArcaneSavant`, `BattleBolas`, `BattleUgin`, `CallerOfTheUntamed`, `Discard`, `Diversion`, `ExileDraw`, `Fame`, `Fortune`, `Friends`, `GreenAnchor`, `Intelligence`, `MaelstromArchangelAvatar`, `Money`, `Peace`, `RedWaterfall`, `Secrets`, `Silence`, `Snitch`, `Stargate`, `VolatileChimera`, `War`
- `NoteNumber$`: TODO: Describe this parameter.
  Observed values: `X`
- `NumAtt$`: TODO: Describe this parameter.
  Observed values: `+1`, `+10`, `+2`, `+20`, `+3`, `+4`, `+5`, `+6`, `+7`, `+9`, `+9999`, `+ArmamentsX`, `+BarrelingX`, `+Count$ChosenNumber`, `+Count$ValidGraveyard Creature.YouOwn`, `+Excess`, `+IvyX`, `+JoinForcesAmount`, `+P`, `+RCX`, `+RR`, `+ScentOfIvyX`, `+SliversOnFieldX`, `+Spawner>TriggerCount$LifeAmount`, `+TreasureX`, `+WasKicked`, `+X`, `+X1`, `+X2`, `+Y`, `+Z`, `-1`, `-11`, `-13`, `-2`, `-3`, `-4`, `-5`, `-6`, `-7`, `-NightshadeX`, `-ScentOfNightshadeX`, `-X`, `-XPlus`, `-Y`, `Double`, `Triple`
- `NumDef$`: TODO: Describe this parameter.
  Observed values: `+1`, `+10`, `+2`, `+20`, `+3`, `+4`, `+5`, `+6`, `+7`, `+9`, `+ArmamentsX`, `+BarrelingX`, `+Count$ValidGraveyard Creature.YouOwn`, `+Excess`, `+IvyX`, `+P`, `+ScentOfIvyX`, `+Spawner>TriggerCount$LifeAmount`, `+WasKicked`, `+X`, `+X1`, `+X2`, `+Y`, `+Z`, `-1`, `-11`, `-13`, `-2`, `-3`, `-4`, `-5`, `-6`, `-9999`, `-NightshadeX`, `-ScentOfNightshadeX`, `-X`, `-X3`, `-XPlus`, `-Y`, `Double`, `Triple`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionQuestion$`: TODO: Describe this parameter.
  Observed values: `Do you want TARGETS to gain reach?`, `Do you want TARGETS to get +3/+3?`, `Do you want TARGETS to get -3/-3?`
- `Origin$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Blind Betrayal —`, `Bloodrush —`, `Channel —`, `Climb Over —`, `Corrupted —`, `Coven —`, `Cura`, `Cure`, `Delirium —`, `Dinosaur Formula —`, `Domain —`, `Endurant —`, `Final Heaven`, `Formidable —`, `Mantle of Inspiration —`, `Max speed —`, `Meteor Strikes`, `Mine Vibranium —`, `Renew —`, `Smear Campaign —`, `Somersault`, `Steal —`, `Threshold —`, `Tie Up —`, `Wind Walk —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `PumpZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Exile`, `Battlefield,Graveyard`, `Battlefield,Hand`, `Battlefield,Library`, `Exile`, `Graveyard`, `Hand`, `Hand,Battlefield`, `Library`, `Stack`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomKeyword$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomKWNum$`: TODO: Describe this parameter.
  Observed values: `2`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `Imprinted`, `ImprintedOwner`, `Opponent.IsCorrupted`, `Player.NotedForRedWaterfall`, `RememberedController`, `Targeted`, `TargetedController`, `ThisTargetedCard`, `TriggeredAttacker`, `TriggeredBlocker`, `TriggeredCard`, `TriggeredCardController`, `TriggeredCardLKICopy`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredSourceLKICopy`, `TriggeredSpellAbility>TappedCards`, `TriggeredTargetLKICopy`, `Valid Card.AttachedBy`, `Valid Creature.blockedBySource`, `Valid Permanent.RememberedPlayerCtrl+MonoColor+ChosenColor`, `You`
- `RememberPumped$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReplaceDyingDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SharedKeywordsZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Hand,Graveyard,Exile,Library,Command`, `Library`
- `SharedRestrictions$`: TODO: Describe this parameter.
  Observed values: `Card.IsRemembered`, `Card.TriggeredCard`, `Creature.YouCtrl`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `staticAbilities$`: TODO: Describe this parameter.
  Observed values: `MustAttack`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ABChoice`, `AcolytesPrevention`, `AllNoBlock`, `AlphaAttack`, `ArchonPrevention`, `BloodDamage`, `Blue`, `BoonEffect`, `BrassSquireAttach`, `BruenorAttach`, `Burn`, `Burninate`, `ChangeColor`, `ChaoticStrikeDraw`, `Choice`, `Choice1`, `ChompEquip`, `Choose`, `ChooseArtifact`, `ChooseCreature`, `ChooseEnchant`, `ChooseLand`, `ChooseNumber`, `CrabExchange`, `Creature`, `CrimsonCascade`, `DBAddCombat`, `DBAddendum`, `DBAirbend`, `DBAmass`, `DBAnimate`, `DBAnte`, `DBAttach`, `DBBoon`, `DBBounce`, `DBBranch`, `DBChange`, `DBChangePower`, `DBChangeZone`, `DBChangeZoneAll`, `DBChangeZoneHand`, `DBChargeCounter`, `DBCheat`, `DBChoice`, `DBChoose`, `DBChooseAttackers`, `DBChooseCard`, `DBChooseCreature`, `DBChooseExiled`, `DBChooseLand`, `DBChoosePlayer`, `DBChooseRandom`, `DBChooseSac`, `DBChooseSource`, `DBClash`, `DBCleanup`, `DBCleanUp`, `DBCleanup2`, `DBClearChosen`, `DBClone`, `DBCombatDamageEffect`, `DBConjure`, `DBConnive`, `DBConvert`, `DBCopy`, `DBCounter`, `DBCreature`, `DBCurse`, `DBDamage`, `DBDealDamage`, `DBDeathtouch`, `DBDebuff`, `DBDefaultAction`, `DBDelay`, `DBDelayedTrigger`, `DBDelayedTrigger1`, `DBDelayTrig`, `DBDelTrig`, `DBDestroy`, `DBDestroyAll`, `DBDestroyBlue`, `DBDestroyLand`, `DBDestroyWhite`, `DBDig`, `DBDiscard`, `DBDiscover`, `DBDmg`, `DBDmgEach`, `DBDmgOpp`, `DBDonate`, `DBDouble`, `DBDoubleStrike`, `DBDraft`, `DBDraw`, `DBDraw1`, `DBEachDamage`, `DBEffect`, `DBEnchantment`, `DBEnergy`, `DBExchange`, `DBExchangeControl`, `DBExile`, `DBExileAll`, `DBExileTargets`, `DBExileTop`, `DBExileTopCard`, `DBExplore`, `DBFerocious`, `DBFight`, `DBFight2`, `DBFightBis`, `DBFirstStrike`, `DBFlip`, `DBFood`, `DBForget`, `DBGain`, `DBGainControl`, `DBGainLife`, `DBGainLife1`, `DBGiveControl`, `DBGoad`, `DBHand`, `DBHit`, `DBImmediateTrigger`, `DBIncubate`, `DBIndestructible`, `DBInvestigate`, `DBIvyCleanup`, `DBLand`, `DBLearn`, `DBLifelink`, `DBLoseLife`, `DBMana`, `DBMarkGraveyard`, `DBMenace`, `DBMill`, `DBMoonglove`, `DBMount`, `DBMove`, `DBMoveAura`, `DBMustBlock`, `DBNightshadeCleanup`, `DBNonLand`, `DBNoteBolas`, `DBNoteUgin`, `DBPeekAndReveal`, `DBPhases`, `DBPing`, `DBPitFight`, `DBPlay`, `DBProliferate`, `DBProtect`, `DBPump`, `DBPump1`, `DBPump2`, `DBPump3`, `DBPumpAll`, `DBPumpBis`, `DBPumpCombat`, `DBPumpHexproof`, `DBPumpMinus`, `DBPumpNeg`, `DBPumpOpp`, `DBPumpOther`, `DBPumpWalkers`, `DBPumpZ`, `DBPutCounter`, `DBPutCounterAll`, `DBRat`, `DBReanimate`, `DBRegen`, `DBRem`, `DBRemAura`, `DBRemember`, `DBRememberPlayer`, `DBRememberSorcery`, `DBRemoveCounter`, `DBRepeat`, `DBRepeatPlayer`, `DBReset`, `DBReturn`, `DBReturnToHand`, `DBReveal`, `DBRevealHand`, `DBRoll`, `DBRollDice`, `DBSac`, `DBSacMe`, `DBSacrificeAll`, `DBSaproling`, `DBScentOfIvyCleanup`, `DBScentOfNightshadeCleanup`, `DBScry`, `DBSearch`, `DBShuffle`, `DBSkipPhase`, `DBSkipTurn`, `DBStayTapped`, `DBSurveil`, `DBSwiftKick`, `DBTap`, `DBTargetYard`, `DBToken`, `DBTrample`, `DBTransform`, `DBTreasure`, `DBUnblockable`, `DBUnsuspect`, `DBUntap`, `DBUntapAll`, `DBVanilla`, `DBVehicle`, `DBWakeofDestructionDestroyThemAll`, `DeadKeepersDestroy`, `DealDamage`, `DelayedTrig`, `DelTrig`, `DelTrigSlowtrip`, `DestroyAll`, `DestroyCreature`, `DestroyEnch`, `DestroyLand`, `DestroyOpp`, `DestroyPacifist`, `DomriFight`, `Draw`, `EliteGuardEffect`, `Enchantment`, `ExileAll`, `ExileSelf`, `ExileYard`, `FeintPumpAll`, `FightForTheCliffs`, `FindOne`, `FinesseAttach`, `GoingDownInStyle`, `GPaid`, `GraveReap`, `GreenToRed`, `IgnitionDamage`, `JitterClean`, `KazuulAttach`, `Kicked`, `KickerPump`, `KjeldoranGuardEffect`, `KorOutfitting`, `Land`, `LifeTough`, `LightKeepersLife`, `MagneticTheft`, `MakeChoice`, `MirriPutCounter`, `MoveToPlay`, `MutinyDamage`, `NoDamage`, `OkoExchange`, `PhantasmalMountEffect`, `Planeswalker`, `Pump2`, `Pump3`, `PumpBargain`, `PumpEquipped`, `PumpKicked`, `PumpOthers`, `PutCounter`, `PutCounterSelf`, `RakdosBurn`, `ReanimateSelf`, `RebukeDamage`, `RedToGreen`, `RepeatFlip`, `ResetWin`, `ReturnTwo`, `RollD20`, `RuneDelay`, `SaheeliCopy`, `ShapesharerCopy`, `SkipTurn`, `Smolder`, `SnakeBite`, `SoulbrightMana`, `SoulsDamage`, `TailDamage`, `TrackerFight`, `TrigDamage`, `TrigDestroy`, `TrigEffect`, `TrigGenericChoice`, `TrigGorgonDestroy`, `TrigLose`, `TrigMill`, `TrigPlay`, `TrigRemoveCounter`, `TrigSac`, `TrigTap`, `TrigTempt`, `TypeChoice`, `VampiricUrge`, `VigorousPumping`, `WindwalkerAttach`, `WolfStrike`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE8`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `ParentTargetedController`, `Player.Opponent`, `TriggeredCardController`, `TriggeredPlayer`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `100`, `2`, `3`, `4`, `5`, `DBSize`, `MaxPlayers`, `MaxTargets`, `MaxTgt`, `MaxTgts`, `OneEach`, `PlayerCountOpponents$Amount`, `X`, `Y`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `3`, `OneEach`, `X`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `ParentTargetedController`, `TriggeredCardOpponent`, `TriggeredPlayer`
- `TargetsWithSameController$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`, `SpellAbility.numTargets GE1`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`, `Stack`
- `ThisDefinedAndTgts$`: TODO: Describe this parameter.
  Observed values: `Self`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 G`, `2`, `2 R`, `DamageYou<4>`, `Mandatory PayEnergy<2>`, `Mandatory PayEnergy<N>`, `Mandatory PayEnergy<X>`, `PayEnergy<X>`, `PayLife<Y>`, `Sac<1/Balloon>`, `U`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `ImprintedController`, `Player`, `Remembered`, `RememberedController`, `TriggeredDefendingPlayer`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Ability.IsTargeting Player.HasCardsInGraveyard_Creature_LEY`, `Ability.IsTargeting Player.hasMoreLife`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `artifact you control`, `attacking creature`, `creature (+1/+1)`, `creature (-1/-1)`, `creature an opponent controls`, `creature you control`, `instant or sorcery card in your graveyard`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Ally.Other+YouCtrl`, `Any`, `Artifact`, `Artifact,Creature`, `Artifact,Creature,Land`, `Artifact,Creature,Planeswalker`, `Artifact.Creature+YouCtrl`, `Artifact.OppCtrl,Enchantment.OppCtrl`, `Artifact.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouOwn`, `Assassin.Other+YouCtrl`, `Aura.YouCtrl`, `Aura.YouCtrl,Equipment.YouCtrl`, `Bear.YouCtrl`, `Card`, `Card,Emblem`, `Card.CrewedThisTurn`, `Card.ExiledWithSource`, `Card.IsCommander`, `Card.IsCommander+ThisTurnEntered`, `Card.nonBasic`, `Card.nonCreature`, `Card.OppCtrl`, `Card.YouCtrl`, `Card.YouOwn`, `Cleric.Other`, `Creature`, `Creature NumAtt$ +3`, `Creature,Planeswalker`, `Creature,Player`, `Creature,Vehicle`, `Creature.!attacking`, `Creature.!attacking+!blocking`, `Creature.!EnchantedBy`, `Creature.!token`, `Creature.!token+YouOwn`, `Creature.ActivePlayerCtrl`, `Creature.Artifact`, `Creature.Artifact+YouCtrl`, `Creature.Artifact+YouCtrl,Creature.cmcLE3+YouCtrl`, `Creature.Assembly-Worker`, `Creature.Assembly-Worker+attacking`, `Creature.attacking`, `Creature.attacking TriggeredAttackedTarget`, `Creature.attacking+Cleric,Creature.attacking+Rogue,Creature.attacking+Warrior,Creature.attacking+Wizard`, `Creature.attacking+counters_GE1_P1P1`, `Creature.attacking+equipped`, `Creature.attacking+Other`, `Creature.attacking+withoutFlying`, `Creature.attacking,Creature.blocking`, `Creature.Barbarian+Other`, `Creature.Beast`, `Creature.Beast+YouCtrl`, `Creature.Bird`, `Creature.Black`, `Creature.Black+Other+YouCtrl`, `Creature.Black,Creature.Green`, `Creature.Black,Creature.Red`, `Creature.Blinkmoth`, `Creature.blocked+YouCtrl`, `Creature.blockedBySource`, `Creature.blockedBySource,Creature.blockingSource`, `Creature.blocking`, `Creature.blocking+YouCtrl`, `Creature.blocking+YouCtrl,Creature.blocked+YouCtrl`, `Creature.Blue`, `Creature.Blue+Other+YouCtrl`, `Creature.Blue,Creature.Red`, `Creature.Cat+YouCtrl+Other`, `Creature.cmcLTX`, `Creature.Colorless`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.ControllerControlsIsland+attacking,Creature.ControllerControlsIsland+blocking`, `Creature.counters_GE1_P1P1`, `Creature.counters_GE1_REJECTION+OppCtrl`, `Creature.dealtDamageThisTurn`, `Creature.DefenderCtrl`, `Creature.DefenderCtrl+powerLEX`, `Creature.DefenderCtrl+powerLTX`, `Creature.DefendingPlayerCtrl`, `Creature.Dinosaur`, `Creature.Dinosaur+YouCtrl`, `Creature.Dwarf`, `Creature.Elf`, `Creature.Elf,Creature.Soldier`, `Creature.enchanted+YouCtrl,Creature.Enchantment+YouCtrl`, `Creature.ExiledWithSource`, `Creature.Giant`, `Creature.Goblin`, `Creature.greatestPowerControlledByYou`, `Creature.Green`, `Creature.Green+blockingSource`, `Creature.Green+Other+YouCtrl`, `Creature.Green,Creature.Blue`, `Creature.Historic+attacking`, `Creature.Human+attacking`, `Creature.Human+YouCtrl`, `Creature.Kavu`, `Creature.Knight`, `Creature.Legendary`, `Creature.Legendary+counters_GE1_MEMORY`, `Creature.Legendary+YouCtrl`, `Creature.Minotaur+Other`, `Creature.modified+YouCtrl`, `Creature.MultiColor`, `Creature.Mutant`, `Creature.nonBlack`, `Creature.nonBrushwagg`, `Creature.nonHuman+YouCtrl`, `Creature.nonSpirit+YouCtrl`, `Creature.nonWall+ActivePlayerCtrl+!firstTurnControlled`, `Creature.nonWall+OppCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl+cmcLE2`, `Creature.OppCtrl+powerLEX`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.OppCtrl,Vehicle.OppCtrl`, `Creature.Other`, `Creature.Other+!token+YouCtrl`, `Creature.Other+Artifact+YouCtrl`, `Creature.Other+attacking`, `Creature.Other+attacking+withoutFlying`, `Creature.Other+attackingSame`, `Creature.Other+Legendary+YouCtrl`, `Creature.Other+YouCtrl`, `Creature.Other,Planeswalker.Other`, `Creature.powerEQ1+toughnessEQ1`, `Creature.powerGE5`, `Creature.powerLE2`, `Creature.powerLE2+YouCtrl`, `Creature.powerLE3`, `Creature.powerLEX`, `Creature.Red`, `Creature.Red+Other+YouCtrl`, `Creature.Red+YouCtrl,Creature.Green+YouCtrl,Creature.White+YouCtrl`, `Creature.Red,Creature.Green`, `Creature.Red,Creature.White`, `Creature.Shapeshifter`, `Creature.Sliver`, `Creature.Snow`, `Creature.Soldier`, `Creature.token+attacking`, `Creature.token+YouCtrl`, `Creature.Vampire+attacking`, `Creature.Wall`, `Creature.Wall+blocking`, `Creature.Warrior+YouCtrl+Other`, `Creature.White`, `Creature.White+Other+YouCtrl`, `Creature.White,Creature.Black`, `Creature.withDefender`, `Creature.withFlying`, `Creature.withoutFlying`, `Creature.withoutFlying+YouCtrl`, `Creature.Wizard`, `Creature.Wolf`, `Creature.YouCtrl`, `Creature.YouCtrl+!EnchantedBy`, `Creature.YouCtrl+!token`, `Creature.YouCtrl+!token+Other`, `Creature.YouCtrl+attacking`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+dealtCombatDamageThisCombat`, `Creature.YouCtrl+Elf+attacking`, `Creature.YouCtrl+enchanted`, `Creature.YouCtrl+Green`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+nonLegendary`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other+attacking`, `Creature.YouCtrl+Other,Vehicle.YouCtrl+Other`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+powerLE2`, `Creature.YouCtrl+toughnessLE2`, `Creature.YouCtrl+toughnessLTX`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withoutUnearth`, `Creature.YouCtrl+withToxic`, `Creature.YouCtrl+withToxic+Other`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouOwn`, `Creature.YouOwn+NoAbilities`, `Creature.YourTeamCtrl`, `Creature.Zombie`, `Dalek.YouCtrl`, `Detective.YouCtrl`, `Dinosaur.YouCtrl`, `Elemental.Other+YouCtrl`, `Elf.Other+YouCtrl`, `Elf.YouCtrl`, `Enchantment`, `Enchantment.nonAura+YouOwn`, `Equipment`, `Equipment.AttachedTo Creature.YouCtrl,Aura.AttachedTo Creature.YouCtrl`, `Equipment.YouCtrl`, `Faerie,Elf`, `Giant.YouCtrl`, `Goblin.attacking+YouCtrl`, `Goblin.YouCtrl`, `Human`, `Human.YouCtrl`, `Human.YouCtrl+Other`, `Insect`, `Instant.YouCtrl+sharesNameWith TriggeredCard,Sorcery.YouCtrl+sharesNameWith TriggeredCard`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Instant.YouOwn+cmcLEX`, `Instant.YouOwn,Sorcery.YouOwn`, `Island`, `Knight`, `Knight.Other+attacking`, `Knight.Other+YouCtrl`, `Knight.YouCtrl`, `Knight.YouCtrl+attacking+Other`, `Knight.YouCtrl+Other`, `Land`, `Land.nonBasic`, `Land.nonBasic+YouDontCtrl`, `Land.YouCtrl`, `Land.YouDontCtrl`, `Land.YouOwn`, `Lizard.YouCtrl,Mouse.YouCtrl,Otter.YouCtrl,Raccoon.YouCtrl`, `Merfolk`, `Merfolk.Other+YouCtrl`, `Merfolk.YouCtrl`, `Mount.YouOwn`, `Mouse.YouCtrl`, `Opponent`, `Permanent`, `Permanent.!token+OppOwn`, `Permanent.Dinosaur+Other+YouCtrl`, `Permanent.Legendary+Other+YouCtrl`, `Permanent.namedVolo's Journal+YouCtrl`, `Permanent.nonEnchantment`, `Permanent.nonLand`, `Permanent.nonland`, `Permanent.nonLand+!namedDetention Sphere`, `Permanent.nonLand+OppCtrl`, `Permanent.nonland+OppCtrl`, `Permanent.nonLand+YouCtrl`, `Permanent.nonLand+YouDontCtrl`, `Permanent.OppCtrl`, `Permanent.Other`, `Permanent.YouCtrl`, `Permanent.YouCtrl+nonLand`, `Phoenix.YouCtrl`, `Pirate`, `Pirate.attacking+YouCtrl`, `Plains`, `Planeswalker`, `Planeswalker.YouCtrl+Other`, `Player`, `Player,Planeswalker`, `Player.Opponent`, `Player.Opponent+Active`, `Player.OpponentToActive+hasFewerCreaturesInYardThanActive`, `Player.OpponentToActive+hasMoreCardsInHandThanActive`, `Player.OpponentToActive+withMoreCreaturesThanActive`, `Rat.attacking`, `Robot`, `Shark`, `Sliver`, `Soldier`, `Sorcery.YouOwn`, `Sorcery.YouOwn+cmcLEX`, `Spider.YouCtrl`, `Spirit`, `Squirrel`, `Vampire`, `Vampire.YouCtrl`, `Vehicle.YouOwn`, `Villain.YouCtrl`, `Wall`, `Wall.blockedThisTurn`, `Warrior`, `Wolf.attacking,Werewolf.attacking`, `Wolf.Other+YouCtrl,Werewolf.Other+YouCtrl`, `Wolf.YouCtrl,Werewolf.YouCtrl`, `Zombie`, `Zombie.attacking`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `another creature you control`, `attacking creature token`, `creature to get +3/+3`, `creature to get -3/-3`, `creature without flying`, `creature you control`

## `PumpAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->Declare Attackers`, `Declare Attackers`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `Never`, `PumpForTrample`, `UntapCombatTrick`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Sacrifice`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`, `Metalcraft`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CreatureETBAmount`, `FatefulHour`, `Food`, `InnerFlameStrength`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`, `GE2`, `GE5`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`, `Targeted`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If CARDNAME was kicked,`, `If it was kicked,`, `If you control a Plains,`, `If you control an Forest,`, `If you control an Island,`, `If you control an Mountain,`, `If you control an Swamp,`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B`, `R`, `U`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.!CastSa Spell.Mayhem`, `Card.CastSa Spell.Mayhem`, `Card.Self+PromisedGift`, `Card.sharesCreatureTypeWith`, `Card.wasCast`, `Creature.blocking`, `Forest.YouCtrl`, `Instant.YouOwn,Sorcery.YouOwn`, `Island.YouCtrl`, `Mountain.YouCtrl`, `Plains.YouCtrl`, `Rat.YouCtrl`, `Swamp.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQ3`, `GE10`, `LE5`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 G U`, `4 R G`, `Sac<1/CARDNAME/this creature>`, `SubCounter<10/LOYALTY>`, `SubCounter<3/LOYALTY>`, `3 U R W`, `R T`, `2 R`, `8`, `Discard<1/Hand> Draw<2/You>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Sacrifice enchanted creature:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `TargetedOrController`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `Permanent`, `Perpetual`, `UntilEndOfCombat`, `UntilUntaps`, `UntilYourNextTurn`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `KW$`: TODO: Describe this parameter.
  Observed values: `Afterlife:1`, `Annihilator:1 & Indestructible`, `Deathtouch`, `Deathtouch & Lifelink`, `Decayed`, `Double Strike`, `Double Strike & Vigilance`, `Double team`, `Escape:3 B ExileFromGrave<4/Card.Other/other>`, `Exalted`, `Fear`, `Firebending:2`, `Firebending:5`, `First Strike`, `First Strike & Deathtouch`, `First Strike & Flying & Deathtouch & Double Strike & Haste & Hexproof & Indestructible & Lifelink & Menace & Reach & Skulk & Trample & Vigilance`, `First Strike & Flying & Deathtouch & Double Strike & Haste & Hexproof & Indestructible & Lifelink & Menace & Reach & Trample & Vigilance`, `First Strike & Lifelink`, `First Strike & Trample`, `First Strike & Trample & Lifelink`, `First Strike & Vigilance`, `Flashback`, `Flying`, `Flying & Double Strike`, `Flying & Fear & First Strike & Double Strike & Landwalk & Protection & Trample & Vigilance`, `Flying & First Strike & Trample & Lifelink & Haste`, `Flying & Lifelink`, `Flying & Vigilance`, `Flying & Vigilance & Double Strike`, `Haste`, `Haste & Double Strike`, `Hexproof`, `Hexproof & Indestructible`, `HIDDEN CARDNAME can't block.`, `HIDDEN CARDNAME must be blocked if able.`, `HIDDEN CARDNAME's power and toughness are switched`, `HIDDEN This card doesn't untap during your next untap step.`, `Horsemanship`, `Indestructible`, `Indestructible & Haste`, `Indestructible & Hexproof`, `Intimidate`, `Landwalk:Forest`, `Landwalk:Land`, `Lifelink`, `Lifelink & Indestructible & Protection from each color`, `Menace`, `Menace & Haste`, `Menace & Lifelink & Haste`, `Menace & Trample`, `Menace & Trample & Lifelink`, `Persist`, `Prevent all combat damage that would be dealt to and dealt by CARDNAME.`, `Protection from black`, `Protection from blue`, `Protection from green`, `Protection from red`, `Protection from white`, `Protection:Creature.nonHuman:non-Human creatures.`, `Provoke`, `Reach`, `Shroud`, `Suspend`, `Toxic:1`, `Trample`, `Trample & Double Strike`, `Trample & Haste`, `Trample & Infect`, `Trample & Lifelink`, `Trample & Lifelink & Haste`, `Undying`, `Unearth:3`, `Vigilance`, `Vigilance & Haste`, `Vigilance & Lifelink`, `Vigilance & Menace`, `Vigilance & Menace & Lifelink`, `Vigilance & Trample`, `Vigilance & Trample & Indestructible`, `Vigilance & Trample & Melee`, `Ward:1`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3 W`
- `NumAtt$`: TODO: Describe this parameter.
  Observed values: `+1`, `+10`, `+2`, `+3`, `+4`, `+5`, `+7`, `+Excess`, `+ThroneTarkirX`, `+WasKicked`, `+X`, `+Y`, `+Z`, `-1`, `-2`, `-3`, `-4`, `-5`, `-X`, `-Y`
- `NumDef$`: TODO: Describe this parameter.
  Observed values: `+1`, `+10`, `+2`, `+3`, `+4`, `+5`, `+7`, `+ThroneTarkirX`, `+WasKicked`, `+X`, `+Y`, `+Z`, `-1`, `-2`, `-3`, `-4`, `-5`, `-X`, `-Y`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Curaga`, `Formidable —`, `Max speed —`, `Shieldwall —`
- `PumpZone$`: TODO: Describe this parameter.
  Observed values: `All`, `Battlefield`, `Battlefield,Graveyard,Hand,Library`, `Battlefield,Hand`, `Battlefield,Hand,Library`, `Battlefield,Hand,Library,Graveyard`, `Exile`, `Graveyard`, `Hand`, `Library`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberAllPumped$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberPumped$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SharedKeywordsZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Graveyard`, `Hand,Battlefield`
- `SharedRestrictions$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChooseColor`, `DBAddCombat`, `DBAddendum`, `DBAddTurn`, `DBAlterAttribute`, `DBAnimate`, `DBAnimateAll`, `DBBlack`, `DBBlue`, `DBBoon`, `DBChange`, `DBChangeZoneAll`, `DBChoose`, `DBCleanup`, `DBCleanUp`, `DBConvert`, `DBDeathtouch`, `DBDebuff`, `DBDelTrig`, `DBDestroy`, `DBDestroyAll`, `DBDoubleStrike`, `DBDraw`, `DBEffect`, `DBEffect2`, `DBExile`, `DBFirstStrike`, `DBGainLife`, `DBGainLife2`, `DBGreen`, `DBHaste`, `DBHexproof`, `DBIndestructible`, `DBInvestigate`, `DBLifelink`, `DBLoseLife`, `DBMenace`, `DBMonarch`, `DBPartner`, `DBPlay`, `DBPrevent`, `DBProtection`, `DBPump`, `DBPumpAll`, `DBPumpCitizens`, `DBPumpRed`, `DBPumpWhite`, `DBPumpYourZombies`, `DBPutCounter`, `DBPutCounterAll`, `DBPutCounters`, `DBRadiation`, `DBReach`, `DBRed`, `DBReturn`, `DBRollDice`, `DBScry`, `DBSeek`, `DBSurveil`, `DBTapAll`, `DBTimeTravel`, `DBTrample`, `DBTurnFaceUp`, `DBUntapAll`, `DBUnTapAll`, `DBVigilance`, `DelTrigSlowtrip`, `ExileSomeCreatures`, `FatefulHourPump`, `GSEffect`, `InnerHeatStrike`, `Kicked`, `LoseTwo`, `OppBlock`, `RPaid`, `TrigEffect`, `TrigTempt`, `TrigUntapAll`
- `SubABility$`: TODO: Describe this parameter.
  Observed values: `DBChangeZone`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `Mandatory PayEnergy<X>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player`, `RememberedController`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Advisor.YouCtrl,Artificer.YouCtrl,Monk.YouCtrl`, `Ally.YouCtrl`, `Angel.YouCtrl`, `Artifact.Creature+YouCtrl`, `Artifact.Creature+YouOwn+!token,Spacecraft.YouOwn+!token`, `Artifact.YouCtrl,Planeswalker.YouCtrl`, `Aura.YouCtrl,Equipment.YouCtrl,Creature.modified+YouCtrl`, `Bat.YouCtrl`, `Bird.YouCtrl`, `Bird.YouCtrl,Frog.YouCtrl,Otter.YouCtrl,Rat.YouCtrl`, `Card.Cat`, `Card.Creature+YouCtrl`, `Card.Creature+YouDontCtrl`, `Card.IsImprinted,Aura.AttachedTo Creature.IsImprinted`, `Card.IsRemembered`, `Card.IsRemembered+withoutSuspend`, `Card.IsRemembered+withoutSuspend,Card.IsImprinted+withoutSuspend`, `Card.Self`, `Card.Self,Drake.YouCtrl`, `Card.sharesCreatureTypeWith+YouCtrl`, `Card.TargetedPlayerOwn`, `Card.token+YouCtrl`, `Card.TopGraveyard2+YouCtrl`, `Card.Vampire+YouCtrl`, `Cat.YouCtrl`, `Creature`, `Creature.!HasCounters`, `Creature.!IsRemembered`, `Creature.!TriggeredAttacker+attacking Opponent`, `Creature.ActivePlayerCtrl`, `Creature.Ally+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.attackersBandedWith`, `Creature.attacking`, `Creature.attacking Opponent,Creature.attacking Valid Planeswalker.OppCtrl`, `Creature.attacking+Other`, `Creature.attacking+Other+YouCtrl`, `Creature.attacking+Red`, `Creature.attacking+Red+Other+YouCtrl`, `Creature.attacking+unblocked`, `Creature.attacking+White`, `Creature.attacking+withFlanking`, `Creature.attacking+withFlying`, `Creature.attacking+withFlying+Other+YouCtrl`, `Creature.attacking+YouCtrl`, `Creature.attacking,Creature.blocking`, `Creature.basePowerEQ1+baseToughnessEQ1+Other+YouCtrl`, `Creature.Beast+YouCtrl`, `Creature.Black`, `Creature.blocked`, `Creature.blockedByRemembered`, `Creature.blockedThisTurn`, `Creature.blockedValidThisTurn Card.StrictlySelf`, `Creature.blocking`, `Creature.blocking+Other`, `Creature.blocking+withFlying`, `Creature.blockingRemembered+YouCtrl`, `Creature.blockingSource`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.ChosenType`, `Creature.Citizen+YouCtrl`, `Creature.cmcLEX`, `Creature.Colorless+YouCtrl`, `Creature.ControlledBy RememberedController+!IsRemembered`, `Creature.couldAttackButNotAttacking`, `Creature.counters_GE1_P1P1`, `Creature.Dinosaur+YouCtrl`, `Creature.Dragon`, `Creature.Elf`, `Creature.Elf+StrictlyOther+YouCtrl`, `Creature.Elf+YouCtrl`, `Creature.EquippedByTargeted`, `Creature.Faerie+StrictlyOther+YouCtrl`, `Creature.Goblin`, `Creature.Goblin+YouCtrl`, `Creature.Green`, `Creature.Green+YouCtrl`, `Creature.Human+StrictlyOther+YouCtrl`, `Creature.Human+YouCtrl`, `Creature.Human+YouCtrl,Creature.Artifact+YouCtrl`, `Creature.IsNotChosenType`, `Creature.IsRemembered`, `Creature.Kithkin+YouCtrl`, `Creature.Land+YouCtrl`, `Creature.Legendary+YouCtrl`, `Creature.Mercenary+StrictlyOther`, `Creature.modified+YouCtrl+StrictlyOther`, `Creature.nonAngel+YouCtrl`, `Creature.nonArtifact`, `Creature.nonArtifact+Other`, `Creature.nonBlack`, `Creature.nonBlue`, `Creature.nonChosenCard+TargetedPlayerCtrl`, `Creature.nonDemon`, `Creature.nonDragon`, `Creature.nonElf`, `Creature.nonGreen+YouCtrl`, `Creature.nonHuman+attacking`, `Creature.nonInsect+nonRat+nonSpider+nonSquirrel`, `Creature.nonSnow`, `Creature.nonVampire`, `Creature.nonWhite`, `Creature.nonZombie`, `Creature.nonZombie+YouCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl+!IsRemembered`, `Creature.Orc+StrictlyOther`, `Creature.Other`, `Creature.Other+!ChosenCardStrict`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl+withDeathtouch`, `Creature.Other+YouCtrl+withDouble Strike`, `Creature.Other+YouCtrl+withFirst Strike`, `Creature.Other+YouCtrl+withFlying`, `Creature.Other+YouCtrl+withFlying+attacking`, `Creature.Other+YouCtrl+withHaste`, `Creature.Other+YouCtrl+withHexproof`, `Creature.Other+YouCtrl+withIndestructible`, `Creature.Other+YouCtrl+withLifelink`, `Creature.Other+YouCtrl+withMenace`, `Creature.Other+YouCtrl+withPartner`, `Creature.Other+YouCtrl+withProtection`, `Creature.Other+YouCtrl+withReach`, `Creature.Other+YouCtrl+withTrample`, `Creature.Other+YouCtrl+withVigilance`, `Creature.Otter+YouCtrl,Creature.Enchantment+YouCtrl`, `Creature.powerGE5+YouCtrl`, `Creature.powerLE2+YouCtrl`, `Creature.Red`, `Creature.Red+YouCtrl,Creature.White+YouCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.sameName`, `Creature.Samurai+YouCtrl`, `Creature.Saproling`, `Creature.Snow+YouCtrl`, `Creature.Soldier`, `Creature.Squirrel`, `Creature.StrictlyOther`, `Creature.StrictlyOther+Human+YouCtrl`, `Creature.StrictlyOther+Legendary+YouCtrl`, `Creature.StrictlyOther+YouCtrl`, `Creature.StrictlyOther+YouCtrl+powerGE4`, `Creature.token`, `Creature.token+YouCtrl`, `Creature.Vampire+YouCtrl`, `Creature.Warrior+YouCtrl`, `Creature.White`, `Creature.White+YouCtrl`, `Creature.White,Creature.Green`, `Creature.withDefender+YouCtrl`, `Creature.withFlying+attacking`, `Creature.withFlying+StrictlyOther+YouCtrl`, `Creature.withFlying+YouCtrl`, `Creature.withoutFlanking+blockingSource`, `Creature.withoutShadow`, `Creature.withShadow`, `Creature.withToxic+StrictlyOther+YouCtrl`, `Creature.Wolf+StrictlyOther+YouCtrl,Creature.Werewolf+StrictlyOther+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+!token`, `Creature.YouCtrl+attacking`, `Creature.YouCtrl+ChosenType`, `Creature.YouCtrl+cmcLE2`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+equipped`, `Creature.YouCtrl+equipped,Equipment.YouCtrl`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+namedGary Clone`, `Creature.YouCtrl+namedGenasi Enforcers`, `Creature.YouCtrl+namedGenasi Rabble-Rouser`, `Creature.YouCtrl+namedPack Mastiff`, `Creature.YouCtrl+nonHuman`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other+ChosenType`, `Creature.YouCtrl+Outlaw`, `Creature.YouCtrl+powerEQ1+toughnessEQ1`, `Creature.YouCtrl+powerEQX`, `Creature.YouCtrl+powerGE4`, `Creature.YouCtrl+powerLEX`, `Creature.YouCtrl+powerLTY`, `Creature.YouCtrl+StrictlyOther`, `Creature.YouCtrl+toughnessGE4`, `Creature.YouCtrl+Warrior`, `Creature.YouCtrl+White`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withFlying,Creature.YouCtrl+withLifelink,Creature.YouCtrl+withDeathtouch`, `Creature.YouCtrl+withMenace`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YouOwn`, `Creature.YouOwn+!token+cmcLE2`, `Creature.YouOwn,Planeswalker.YouOwn`, `Creature.YourTeamCtrl`, `Creature.YourTeamCtrl+attacking`, `Creature.Zombie+YouCtrl`, `Dinosaur.StrictlyOther+YouCtrl`, `Dinosaur.YouCtrl`, `Dinosaur.YouCtrl+Other`, `Dragon.Elder+YouCtrl`, `Dragon.YouCtrl`, `Elemental.YouCtrl`, `Elf.YouCtrl`, `Employee.YouCtrl,Dog.YouCtrl`, `Fungus.Creature+YouCtrl,Saproling.Creature+YouCtrl`, `Giant.Other+YouCtrl,Wizard.Other+YouCtrl`, `Goblin.IsRemembered`, `Goblin.YouCtrl,Orc.YouCtrl`, `Gremlin.YouCtrl`, `Human.attacking`, `Human.StrictlyOther+YouCtrl`, `Human.YouCtrl`, `Insect.YouCtrl`, `Instant.YouCtrl,Sorcery.YouCtrl`, `Knight.YouCtrl`, `Knight.YouCtrl+StrictlyOther`, `Land`, `Minotaur.YouCtrl`, `Mouse.YouCtrl`, `Ninja.YouCtrl,Rogue.YouCtrl`, `Permanent.token+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+HasCounters`, `Permanent.YouCtrl+Other+ChosenType`, `Phyrexian.YouCtrl`, `Pirate.YouCtrl`, `Raccoon.YouCtrl`, `Rat.StrictlyOther+YouCtrl`, `Rat.YouCtrl`, `Remembered.sameName+Other+Creature`, `Scion.YouCtrl,Spawn.YouCtrl`, `Sliver.YouCtrl`, `Soldier.YouCtrl`, `Soldier.YouCtrl,Hero.YouCtrl`, `Spider.Other+YouCtrl`, `Spirit.attacking`, `Spirit.YouCtrl`, `Squirrel.YouCtrl`, `Targeted.Creature+Other+sameName`, `Targeted.Other+YouCtrl+Creature`, `Targeted.PairedWith`, `Targeted.sameName+Other`, `TargetedCard.Self,Creature.blockedByValidThisTurn Targeted`, `Treefolk.YouCtrl,Forest.YouCtrl`, `TriggeredAttacker.Creature+ControlledBy TriggeredDefendingPlayer`, `Vampire.!token+YouCtrl`, `Villain.YouCtrl+StrictlyOther`, `Warrior.attacking`, `Warrior.attacking+YouCtrl`, `Wizard`, `Wizard.YouCtrl`, `Zombie`, `Zombie.YouCtrl`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `PutCounter`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Metalcraft`, `Solved`, `Threshold`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Attackers`, `Declare Blockers`, `Upkeep`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`, `Graveyard`, `Hand`, `Stack`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `Adapt$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`
- `AIActivateLast$`: TODO: Describe this parameter.
  Observed values: `True`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AlwaysWithNoTgt`, `AristocratCounters`, `AtOppEOT`, `BoonCounterOnOppCreature`, `ChargeToBestCMC`, `ChargeToBestOppControlledCMC`, `CheckDFC`, `CrawlingBarrens`, `Curse`, `ExiledCreatureFromGraveCMC`, `Fight`, `FromDiceRoll`, `Good`, `MarkOppCreature`, `MoveCounter`, `MoveCounter.IsCounterUser`, `Never`, `NoCounterOfType`, `PayEnergy`, `PayEnergyConservatively`, `Polukranos`, `PowerDmg`, `TheOneRing`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `G`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Card.inZoneBattlefield+YouCtrl,Card.suspended+YouDontCtrl`, `Creature.!token`, `Creature.!token+YouCtrl`, `Creature.nonHorror+OppCtrl+counters_LT1_SLIME`, `Creature.OppCtrl+!namedThe Flood of Mars,Land.OppCtrl+nonIsland`, `Creature.token+attacking+ChosenType`, `Land.Basic+YouCtrl+!canProduceManaColor Colorless`, `Permanent.counters_GE1_TIME+inZoneBattlefield+YouCtrl,Card.suspended+YouDontCtrl`
- `AltChoiceForEach$`: TODO: Describe this parameter.
  Observed values: `P1P1`
- `AnnounceType$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `Bolster$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `X`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`
- `ChoiceAmount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `4`, `X`, `Y`
- `ChoiceOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChoicePrompt$`: TODO: Describe this parameter.
  Observed values: `Select target attraction you control that doesn't have a midway counter on it`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Attraction.YouCtrl+counters_EQ0_MIDWAY`, `Card.IsRingbearer+YouCtrl`, `Card.Self,Card.IsCommander`, `Card.targetedBy`, `Creature`, `Creature.ControlledBy ChosenPlayer`, `Creature.ControlledBy Player.IsRemembered`, `Creature.ControlledBy TargetedPlayer`, `Creature.ControlledBy ThisTargetedPlayer`, `Creature.ControlledBy TriggeredPlayer`, `Creature.IsRemembered`, `Creature.tapped+OppCtrl`, `Creature.targetedBy`, `Creature.TargetedPlayerCtrl,Vehicle.TargetedPlayerCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+IsCommander`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Dragon.ChosenColor+YouCtrl`, `Permanent.nonLand`, `Permanent.YouCtrl+HasCounters`, `Permanent.YouDontCtrl+nonEnchantment`, `Planeswalker.Liliana+YouCtrl`, `Planeswalker.YouCtrl`, `Snail.YouCtrl`, `Soldier.YouCtrl`
- `ChoicesDesc$`: TODO: Describe this parameter.
  Observed values: `creature they control`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose a creature`, `Choose a creature or Vehicle you control`, `Choose a creature targeted by this spell`, `Choose a creature to put a deathtouch counter on`, `Choose a creature to put a menace counter on`, `Choose a creature you control`, `Choose a Dragon for chosenColor`, `Choose any number of creatures and/or Vehicles target player controls to distribute counters to`, `Choose any number of creatures you control to distribute counters to`, `Choose any number of tapped creatures your opponents control to distribute counters to`, `Choose one, two, or three creatures you control to distribute counters to`, `Choose this card and/or any number of commanders to distribute counters to`, `Choose up to that many creatures tapped this way`, `Choose up to two Soldiers you control`
- `ChooseDifferent$`: TODO: Describe this parameter.
  Observed values: `2`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player.IsRemembered`, `Remembered`, `TargetedPlayer`, `ThisTargetedPlayer`, `TriggeredPlayer`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CurseY`, `DragonPresence`, `IsInstantOrSorcery`, `MimeoNumRemembered`, `Morbid`, `PlayerCountDefinedTriggeredAttackedTarget$HasPropertylifeGTX`, `Resolved`, `SameType`, `TriggeredSpellAbility$CardManaCostLKI`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GTX`, `LT1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `CastSA>Collected`, `Equipped`, `Imprinted`, `ParentTarget`, `Remembered`, `RememberedLKI`, `Sacrificed`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredSourceLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If it was a permanent card,`, `Then, if you control an artifact and an enchantment,`
- `ConditionNotPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Angel`, `Artifact`, `Artifact.YouCtrl`, `Card`, `Card.Black`, `Card.cmcGE4`, `Card.Creature`, `Card.greatestRememberedCMC+YouOwn`, `Card.HasCounters`, `Card.Insect`, `Card.Mount`, `Card.nonLand`, `Card.Permanent`, `Card.powerEQ1+toughnessEQ1`, `Card.PromisedGift`, `Card.Self+Angel`, `Card.Self+blockedOrBeenBlockedSinceYourLastUpkeep`, `Card.Self+Cleric`, `Card.Self+counters_EQ0_Indestructible`, `Card.Self+Phyrexian`, `Card.Self+PromisedGift`, `Card.Self+Spirit`, `Card.Self+Warrior`, `Card.StrictlySelf`, `Card.Vampire`, `Card.wasCast`, `Card.wasCast+!wasCastFromYourHand`, `Card.wasCastFromGraveyard`, `Card.YouCtrl+ThisTurnEntered`, `Creature`, `Creature.Black`, `Creature.Blue`, `Creature.counters_EQ0_P1P1`, `Creature.counters_GE1_OIL`, `Creature.Elemental`, `Creature.Green`, `Creature.nonArtifact`, `Creature.OppCtrl`, `Creature.powerGE1`, `Creature.powerGE4`, `Creature.powerLE2`, `Creature.Red`, `Creature.tapped`, `Creature.ThisTurnEntered`, `Creature.token`, `Creature.White`, `Creature.YouCtrl`, `Dragon`, `Human`, `Knight.YouCtrl+StrictlyOther`, `Land`, `Legendary`, `Lesson`, `Locus,Sphere`, `Permanent`, `Permanent.White+YouCtrl+Other+NotDefinedTargeted`, `Planeswalker`, `Soldier`, `Thrull`
- `ConditionPresent2$`: TODO: Describe this parameter.
  Observed values: `Enchantment.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE3`, `GE5`, `GT0`, `GTY`, `LE0`, `LE10`, `LTY`, `NE2`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `tapXType<2/Artifact;Creature/artifacts and/or creatures>`, `B ExileFromGrave<1/CARDNAME>`, `ExileFromGrave<2/Card>`, `2 G U`, `PayEnergy<2>`, `T`, `2 G G`, `3 U ExileFromGrave<1/CARDNAME>`, `AddCounter<1/LOYALTY>`, `SubCounter<3/LOYALTY>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `({3}{R}, Exile this card from your graveyard:`, `Exile an instant or sorcery spell you control:`, `Exile any number of tokens put onto the battlefield with CARDNAME.`, `{2}, Exile a nonland card from your hand:`, `{B}, Reveal CARDNAME from your hand:`, `{T}, Exile an instant or sorcery card from your graveyard:`, `{U}, Tap an untapped blue creature you control, Remove a polyp counter from CARDNAME:`
- `CounterMapValues$`: TODO: Describe this parameter.
  Observed values: `1`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `13`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `AFLifeLost`, `CardTriggeredTarget$ExcessDamageReceivedThisTurn`, `Count$CardPower`, `Count$ChosenNumber`, `Count$Valid Land.YouCtrl`, `Count$ValidGraveyard,Exile Ooze.YouOwn,Card.YouOwn+namedSlime Against Humanity/Plus.2`, `Devour2X`, `DiceResult`, `EvenResults`, `ExiledWith$CardManaCost`, `GateX`, `KickedPet`, `LifeX`, `LightOfPromiseAmount`, `MimeoX`, `NantukoY`, `NumDamage`, `OldThoughts`, `OssuaryX`, `PlayerCountRegisteredOpponents$HasPropertyLostLifeThisTurn`, `PreventedDamage`, `Result`, `ScavengeX`, `SunbondTriggerAmount`, `SVar$VoteNum/Times.2`, `Treasure`, `TriggerCount$DamageAmount`, `TriggeredSpellAbility$CardManaCostLKI`, `VoteNum`, `Votes`, `WarElementalY`, `Wins`, `WW`, `X`, `X20`, `X9`, `Y`, `Z`
- `CounterNumPerDefined$`: TODO: Describe this parameter.
  Observed values: `X`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `ACORN`, `AGE`, `AIM`, `ARROW`, `AWAKENING`, `BAIT`, `BLAZE`, `BLESSING`, `BLIGHT`, `BLOOD`, `BLOODLINE`, `BLOODSTAIN`, `BOOK`, `BORE`, `BOUNTY`, `BRIBERY`, `BRICK`, `BURDEN`, `CAGE`, `CARRION`, `CELL`, `CHARGE`, `CHORUS`, `COIN`, `COLLECTION`, `COMPONENT`, `CONQUEROR`, `CONTESTED`, `CORPSE`, `CORRUPTION`, `CREDIT`, `CUBE`, `CURRENCY`, `DEATH`, `Deathtouch`, `Deathtouch,Lifelink`, `Decayed`, `DELAY`, `DEPLETION`, `DESCENT`, `DESPAIR`, `DEVOTION`, `DISCOVERY`, `DIVINITY`, `DOOM`, `Double Strike`, `DREAD`, `DREAM`, `EachFromSource`, `EGG`, `ELIXIR`, `EMBER`, `ENERGY`, `ENLIGHTENED`, `EON`, `ERUPTION`, `EVERYTHING`, `Exalted`, `ExistingCounter`, `Experience`, `EXPOSURE`, `EYEBALL`, `FATE`, `FEATHER`, `FEEDING`, `FELLOWSHIP`, `FILIBUSTER`, `FINALITY`, `FIRE`, `First Strike`, `First Strike,Vigilance,Deathtouch,Lifelink`, `First Strike,Vigilance,Lifelink`, `FLAME`, `FLOOD`, `Flying`, `Flying,First Strike`, `Flying,First Strike,Deathtouch,Hexproof,Lifelink,Menace,Reach,Trample,Vigilance,P1P1`, `Flying,Hexproof`, `Flying,Lifelink,P1P1`, `FORESHADOW`, `FUNGUS`, `FUNK`, `FURY`, `FUSE`, `GHOSTFORM`, `GLYPH`, `GOLD`, `GROWTH`, `HARMONY`, `HATCHLING`, `HEALING`, `Hexproof`, `HIT`, `HONE`, `HOOFPRINT`, `HOUR`, `HOURGLASS`, `HUNGER`, `HUSK`, `ICE`, `INCARNATION`, `INCUBATION`, `Indestructible`, `INFECTION`, `INFLUENCE`, `INGENUITY`, `INGREDIENT`, `INVITATION`, `JUDGMENT`, `KI`, `KNOWLEDGE`, `LANDMARK`, `Lifelink`, `LOOT`, `LORE`, `LOYALTY`, `LUCK`, `M0M1`, `M0M2`, `M1M0`, `M1M1`, `M2M1`, `M2M2`, `MAGNET`, `MATRIX`, `Menace`, `Menace,Deathtouch,Lifelink`, `Menace,Trample,Lifelink`, `Menace,Trample,Reach,Haste`, `MIDWAY`, `MINE`, `MIRE`, `MUSIC`, `MUSTER`, `NEST`, `NIGHT`, `OIL`, `OMEN`, `P0P1`, `P1P0`, `P1P1`, `P1P1,CHARGE`, `P1P1,Double Strike`, `P1P1,First Strike,Trample`, `P1P1,First Strike,Vigilance`, `P1P1,First Strike,Vigilance,Menace`, `P1P1,Flying`, `P1P1,Flying,Lifelink`, `P1P1,LOYALTY`, `P1P2`, `P2P2`, `PAGE`, `PAIN`, `PALLIATION`, `PETAL`, `PETRIFICATION`, `PHYLACTERY`, `PHYRESIS`, `PIN`, `PLAGUE`, `PLAN`, `PLOT`, `POINT`, `POLYP`, `POSSESSION`, `PRESSURE`, `PREY`, `PUPA`, `QUEST`, `Quest`, `RALLY`, `Reach`, `RELEASE`, `REV`, `RIBBON`, `RITUAL`, `ROPE`, `SCREAM`, `SCROLL`, `Shadow`, `SHIELD`, `SHOE`, `SHRED`, `SKEWER`, `SLEEP`, `SLEIGHT`, `SLIME`, `SLUMBER`, `SOOT`, `SOUL`, `SPITE`, `SPORE`, `STASH`, `STORAGE`, `STORY`, `STRIFE`, `STUDY`, `Stun`, `STUN`, `SUPPLY`, `THEFT`, `TICKET`, `TIDE`, `TIME`, `TOWER`, `TRAINING`, `Trample`, `Trample,Menace`, `TRAP`, `TREASURE`, `UNITY`, `UNLOCK`, `VALOR`, `VELOCITY`, `VERSE`, `Verse`, `Vigilance`, `Vigilance,Menace,Trample`, `Vigilance,Reach`, `Vigilance,Reach,Trample`, `VITALITY`, `VORTEX`, `VOW`, `VOYAGE`, `WAGE`, `WINCH`, `WIND`, `WRECK`
- `CounterTypePerDefined$`: TODO: Describe this parameter.
  Observed values: `True`
- `CounterTypes$`: TODO: Describe this parameter.
  Observed values: `Deathtouch,Lifelink`, `EachType_Creature.YouCtrl`, `EachType_Permanent.YouCtrl`, `Flying,Deathtouch,Lifelink`, `Flying,First Strike,Lifelink`, `Lifelink`, `Lifelink,P1P1`, `P1P1`, `P1P1,ChosenFromList`, `P1P1,Deathtouch`, `P1P1,Lifelink`, `P1P1,P1P1,P1P1,P1P1,Flying,Vigilance,Trample,Lifelink`, `P1P1,Reach,Deathtouch`, `P1P1,Reach,Trample`, `P1P1,Trample`, `P1P1,Trample,Vigilance`, `P2P0,P1P1,P0P2`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttachedBy Returned`, `ChosenCard`, `ChosenPlayer`, `Convoked`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `EffectSource`, `Enchanted`, `Equipped`, `ExiledCards`, `Imprinted`, `OriginalHost`, `ParentTarget`, `Remembered`, `Remembered.Saga`, `RememberedCard`, `RememberedLKI`, `ReplacedCard`, `ReplacedNewCard.Creature`, `ReplacedNewCard.Planeswalker`, `ReplacedTarget`, `Self`, `Self & Targeted`, `ShieldEffectTarget`, `Tapped`, `Targeted`, `Targeted.!ChosenCard`, `Targeted.Artifact+Creature`, `Targeted.ChosenType`, `Targeted.Spacecraft`, `Targeted.YouDontCtrl`, `TargetedCard`, `TriggeredAttackerLKICopy`, `TriggeredAttackers`, `TriggeredBlockerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredCardLKICopy & Self`, `TriggeredCardLKICopy.Spider`, `TriggeredObjectLKICopy`, `TriggeredSourceLKICopy`, `TriggeredSources`, `TriggeredTargetLKICopy`, `Valid Card.Self`, `Valid Creature.Other+YouCtrl`, `Valid Creature.YouCtrl+Other`, `Valid Creature.YouCtrl+powerGTbasePower`, `You`
- `Description$`: TODO: Describe this parameter.
- `DividedAsYouChoose$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `4`, `5`, `7`, `8`, `OssuaryX`, `X`, `Y`
- `DividedRandomly$`: TODO: Describe this parameter.
  Observed values: `True`
- `DividedUpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `EachExistingCounter$`: TODO: Describe this parameter.
  Observed values: `True`
- `EachFromSource$`: TODO: Describe this parameter.
  Observed values: `Self`, `TriggeredCardLKICopy`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForColor$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IfDesc$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.canReceiveCounters P1P1`, `Card.Self+attackingYou`, `Card.Self+ThisTurnEntered`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxFromEffect$`: TODO: Describe this parameter.
  Observed values: `4`, `7`
- `MinChoiceAmount$`: TODO: Describe this parameter.
  Observed values: `0`, `1`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `Monstrosity$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `2`, `3`, `4`, `5`, `X`
- `OnlyNewKind$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `1`
- `Placer$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player.IsRemembered`, `TargetedPlayer`, `ThisTargetedPlayer`, `TriggeredPlayer`, `TriggeredSource`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PowerUp$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Camouflage —`, `Channel —`, `Come Fly With Me —`, `Find New Host —`, `Max speed —`, `Metalcraft —`, `Mold Harvest —`, `Oil Scavenge {3}{R}`, `Renew —`, `Share —`, `Solved —`, `Threshold —`, `Web Support —`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceLKICopy`
- `PutOnDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `PutOnEachOther$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`
- `RandomNumTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `RandomType$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberCostMana$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberPut$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemovePhase$`: TODO: Describe this parameter.
  Observed values: `Cleanup`, `End of Turn`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SharedKeywords$`: TODO: Describe this parameter.
  Observed values: `Flying & First Strike & Double Strike & Deathtouch & Hexproof & Haste & Indestructible & Lifelink & Menace & Reach & Trample & Vigilance`, `Flying & First Strike & Double Strike & Deathtouch & Hexproof & Indestructible & Lifelink & Menace & Reach & Trample & Vigilance`
- `SharedKeywordsDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SharedKeywordsZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `SharedRestrictions$`: TODO: Describe this parameter.
  Observed values: `Creature.YouOwn`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpecifyCounter$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SplitAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AddFungalEffects`, `AddTrigger`, `ChooseColor`, `ChooseX`, `CostNotPaid`, `DBAddMana`, `DBAddTriggers`, `DBAlter`, `DBAnimate`, `DBAnimateAll`, `DBArtisanAnimate`, `DBAssemble`, `DBAttach`, `DBBranch`, `DBCast`, `DBChange`, `DBChangeTarget`, `DBChangeZone`, `DBChooseCard`, `DBChooseNumber`, `DBChoosePlayer`, `DBCleanImprinted`, `DBCleanup`, `DBClone`, `DBConjure`, `DBConvert`, `DBCopy`, `DBCounter`, `DBCounterBis`, `DBCounters`, `DBCurseCleanup`, `DBDamage`, `DBDealDamage`, `DBDelayedTrigger`, `DBDelayTrig`, `DBDelTrig`, `DBDestroy`, `DBDestroyHunger`, `DBDig`, `DBDigUntil`, `DBDmg`, `DBDouble`, `DBDraw`, `DBDraw1`, `DBDraw2`, `DBEachDamage`, `DBEarthbend`, `DBEffect`, `DBEnergy`, `DBExile`, `DBExileSelf`, `DBExileTop`, `DBFight`, `DBFood`, `DBGainControl`, `DBGainLife`, `DBGainLifeBis`, `DBGenericChoice`, `DBGetFood`, `DBGoad`, `DBHand`, `DBHaste`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBImprint`, `DBInvestigate`, `DBJunk`, `DBLearn`, `DBLose`, `DBLoseLife`, `DBMana`, `DBMaySac`, `DBMill`, `DBMonarch`, `DBMultiplyCounter`, `DBMustBlock`, `DBNantukoDraw`, `DBPhase`, `DBPhases`, `DBPlay`, `DBPrepare`, `DBProliferate`, `DBProtection`, `DBPump`, `DBPumpAll`, `DBPumpOne`, `DBPutCounter`, `DBPutCounter2`, `DBPutCounterAll`, `DBPutCounterCommander`, `DBPutLOYALTY`, `DBPutThree`, `DBPutTwo`, `DBRegenerate`, `DBRemoveCounter`, `DBRemoveCounters`, `DBRemoveSelf`, `DBRepeat`, `DBReselect`, `DBReturn`, `DBSac`, `DBSacrifice`, `DBScry`, `DBSearch`, `DBSeek`, `DBSkipTurn`, `DBSubCounter`, `DBSurveil`, `DBTap`, `DBTapOrUntap`, `DBToken`, `DBTokenFood`, `DBTrample`, `DBTransform`, `DBTreasure`, `DBTrigger`, `DBUnblockable`, `DBUntap`, `DBUntapAll`, `DBUpdate`, `DBWin`, `DealToCreature`, `DelayedTrigger`, `Delude`, `DevourCleanup`, `DivineCharacter`, `Dustwalk`, `ETBTapped`, `ExileFromHand`, `GiveSuspend`, `GorgeOnThoughts`, `LifelinkCounter`, `Mill`, `MimeoCopyChosen`, `MoveAllCounter`, `PayThePiper`, `PounceAmbush`, `PutCounters`, `PutOneMore`, `RemCounter`, `RemoveSelf`, `RonsoTap`, `SacAllOthers`, `Sacrifice`, `SacSelf`, `ScrollsOfKnowledge`, `ScrollsOfLife`, `SelectOpponent`, `SquadronLaunch`, `Survivor`, `TrigAnimate`, `TrigChoosePlayer2`, `TrigDoubleCounters`, `TrigDraw`, `TrigImmediate`, `TrigImmediateTrig`, `TrigLife`, `TrigPump`, `TrigRemoveSelf`, `TurnToStone`, `VolverLaunch`, `VolverLife`, `VolverResilience`, `VolverSpeed`, `VolverStomp`, `WinGame`
- `Support$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `6`, `X`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredPlayer`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `7`, `8`, `MaxTargets`, `MaxTgts`, `OneEach`, `TargetsNum`, `TriggerCount$Amount`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `OneEach`, `TargetsNum`, `X`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `TriggeredCardController`, `TriggeredDefendingPlayer`, `TriggeredPlayer`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Exile`, `Exile`, `Graveyard`
- `TriggeredCounterMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `TypeList$`: TODO: Describe this parameter.
  Observed values: `Flying,First Strike,Lifelink,Vigilance`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UniqueType$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `AddCounter<1/Stun/Card.targetedBy/stun counter on targeted creature>`, `G`, `PayEnergy<X>`, `PayEnergy<Y>`, `Return<1/Permanent.nonLand/nonland permanent>`, `Sac<1/Artifact;Creature/artifact or creature>`, `U`, `W`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredPlayer`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Self`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `another creature you control`, `attacking creature`, `creature you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Angel`, `Artifact`, `Artifact.!token+YouCtrl+Other,Creature.YouCtrl+Other+!token`, `Artifact.nonCreature`, `Artifact.nonCreature+YouCtrl`, `Artifact.Other,Creature.Other`, `Artifact.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl,Land.YouCtrl`, `Artifact.YouOwn,Creature.YouOwn`, `Assembly-Worker.YouCtrl`, `Bear`, `Bird,Cat,Dog,Goat,Ox,Snake`, `Creature`, `Creature,Artifact`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!IsCommander+YouDontCtrl`, `Creature.!token`, `Creature.Artifact`, `Creature.attacking`, `Creature.attacking+Other`, `Creature.attacking+Other+YouCtrl`, `Creature.attacking+YouCtrl,Creature.blocking+YouCtrl`, `Creature.attackingYou`, `Creature.Beast+YouCtrl`, `Creature.blockedBySource,Creature.blockingSource`, `Creature.blockedByValidThisTurn ParentTarget`, `Creature.Chimera`, `Creature.ChosenType+YouCtrl`, `Creature.Colorless+ThisTurnEntered`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.counters_GE1_P1P1`, `Creature.counters_LTX_P1P1`, `Creature.CrewedThisTurn`, `Creature.Dinosaur+YouCtrl`, `Creature.greatestPowerControlledByYou`, `Creature.Green,Creature.White,Creature.Blue`, `Creature.Halfling,Creature.Treefolk`, `Creature.HasCounters`, `Creature.IsCommander+YouCtrl`, `Creature.IsSuspected+YouCtrl`, `Creature.Legendary+Other`, `Creature.modified+YouCtrl`, `Creature.nonArtifact`, `Creature.nonBlack`, `Creature.nonCat+YouCtrl`, `Creature.nonHuman+ThisTurnEntered`, `Creature.nonHuman+YouCtrl`, `Creature.nonLegendary+YouCtrl`, `Creature.OppCtrl`, `Creature.OppCtrl,Planeswalker.OppCtrl`, `Creature.Other`, `Creature.Other+counters_EQ0_EGG`, `Creature.Other+withFlying`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl,Vehicle.Other+YouCtrl`, `Creature.Other,Land.Other`, `Creature.powerEQX`, `Creature.powerLE2+YouCtrl`, `Creature.SaddledThisTurn`, `Creature.Soldier`, `Creature.tapped`, `Creature.tapped+Other+YouCtrl`, `Creature.ThisTurnEntered`, `Creature.token+attacking`, `Creature.token+YouCtrl`, `Creature.withFlying`, `Creature.withoutFlying+YouCtrl`, `Creature.withTrample,Creature.withHaste`, `Creature.YouCtrl`, `Creature.YouCtrl+attackedThisTurn`, `Creature.YouCtrl+counters_EQ0_P1P1`, `Creature.YouCtrl+NotDefinedTriggeredTarget`, `Creature.YouCtrl+Other`, `Creature.YouCtrl+Other,Vehicle.YouCtrl+Other`, `Creature.YouCtrl+withoutFlying`, `Creature.YouCtrl,Artifact.YouCtrl`, `Creature.YouCtrl,Enchantment.YouCtrl`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Creature.YouDontCtrl`, `Dinosaur`, `Elemental.Other+YouCtrl`, `Elemental.YouCtrl`, `Elf`, `Enchantment.Creature`, `Faerie.YouCtrl`, `Food.nonCreature+YouCtrl`, `Fungus`, `Goblin.YouCtrl`, `God`, `Human`, `Knight.YouCtrl`, `Land`, `Land.ActivePlayerCtrl+nonIsland`, `Land.counters_EQ0_BLAZE`, `Land.nonCreature+YouCtrl`, `Land.nonSwamp`, `Land.YouCtrl`, `Merfolk`, `Merfolk.Other+YouCtrl`, `Merfolk.YouCtrl`, `Mount,Vehicle`, `Opponent`, `Permanent`, `Permanent,Player`, `Permanent.counters_GE1_TIME+inZoneBattlefield,Card.suspended`, `Permanent.nonLand`, `Permanent.nonLand+YouCtrl`, `Permanent.Other`, `Permanent.Vampire+Other+YouCtrl`, `Permanent.YouCtrl`, `Pirate.YouCtrl`, `Planeswalker.Gideon`, `Planeswalker.Jace`, `Planeswalker.Other+YouCtrl`, `Plant.YouCtrl`, `Player`, `Saga.YouCtrl`, `Shrine`, `Soldier.Other+YouCtrl`, `Spacecraft.YouCtrl,Planet.YouCtrl`, `Spider`, `Symbiote`, `Vampire.Other+YouCtrl`, `Vampire.YouCtrl`, `Zombie.YouCtrl`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `another artifact or creature`

## `PutCounterAll`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AtEOTOrBlock`, `AtOppEOT`, `OwnCreatsAndOtherPWs`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `W`
- `AmountByChosenMap$`: TODO: Describe this parameter.
  Observed values: `Count$CardPower INDEX 1`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.nonLand`, `Card.wasCast`, `Card.wasCast+!wasCastFromYourHand`, `Creature.YouCtrl+powerGE5`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GT11`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 W T`, `6 Discard<1/CARDNAME/this card>`, `SubCounter<1/LOYALTY>`, `AddCounter<2/LOYALTY>`, `SubCounter<2/LOYALTY>`, `SubCounter<9/LOYALTY>`, `W B T Sac<1/Creature.Other/another creature>`, `2 Forage`, `B SubCounter<1/M1M1>`, `AddCounter<0/LOYALTY>`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `Aid`, `VoteNum`, `X`
- `CounterNum2$`: TODO: Describe this parameter.
  Observed values: `1`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `ACORN`, `Deathtouch`, `FADE`, `Flying`, `FUSE`, `HOUR`, `IMPOSTOR`, `LEVEL`, `LORE`, `LOYALTY`, `M0M2`, `M1M1`, `MANABOND`, `P1P1`, `PARALYZATION`, `REJECTION`, `RUST`, `SLIME`, `SPORE`, `TIME`
- `CounterType2$`: TODO: Describe this parameter.
  Observed values: `CHARGE`, `Flying`, `LOYALTY`, `Reach`, `Trample`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `Placer$`: TODO: Describe this parameter.
  Observed values: `Controller`, `Owner`, `TargetedPlayer`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Cohort —`
- `RememberPut$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBCleanup`, `DBCopy`, `DBCount`, `DBDamage`, `DBDestroyAllRusted`, `DBDrain`, `DBDraw`, `DBEffect`, `DBGainLife`, `DBGoad`, `DBPlaneswalk`, `DBPump`, `DBPumpAll`, `DBPumpAll1`, `DBPumpAll2`, `DBRepeat`, `DBReset`, `DBSearch`, `DBSeek`, `DBShuffle`, `DBTap`, `DBUntap`, `DBUntapAll`, `SlowTime`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Advisor.YouCtrl`, `Ally.YouCtrl`, `Artifact`, `Artifact.Creature+YouCtrl`, `Artifact.Creature+YouCtrl,Vehicle.YouCtrl`, `Bird`, `Bird.YouCtrl`, `Card.IsRemembered`, `Card.IsRemembered+withSuspend`, `Card.Self,Golem.YouCtrl`, `Card.suspended`, `Cat.YouCtrl`, `Cleric.YouCtrl`, `Creature`, `Creature.Ally+Other+YouCtrl`, `Creature.Artifact+StrictlyOther+YouCtrl`, `Creature.Artifact+YouCtrl`, `Creature.Artifact+YouCtrl,Vehicle.YouCtrl`, `Creature.attackedThisTurn`, `Creature.attacking`, `Creature.attacking+counters_GE1_P1P1`, `Creature.attacking+YouCtrl`, `Creature.blockedBySource,Creature.blockingSource`, `Creature.blockingSource,Creature.blockedBySource`, `Creature.ChosenCard`, `Creature.ChosenSector`, `Creature.ChosenType+YouCtrl`, `Creature.Colorless+YouCtrl`, `Creature.ControlledBy ChoosingPlayer`, `Creature.counters_GE1_FUSE`, `Creature.counters_GE1_M1M1`, `Creature.Dragon+YouCtrl+StrictlyOther`, `Creature.Elf+YouCtrl`, `Creature.faceDown+YouCtrl`, `Creature.Green+ThisTurnEntered`, `Creature.Human+YouCtrl`, `Creature.IsRemembered`, `Creature.Land+YouCtrl`, `Creature.Legendary+YouCtrl`, `Creature.Merfolk+YouCtrl`, `Creature.Monkey+YouCtrl,Creature.Ape+YouCtrl`, `Creature.namedCharmed Stray+StrictlyOther`, `Creature.nonBlack`, `Creature.nonGideon+YouCtrl+attacking`, `Creature.OppCtrl`, `Creature.Other`, `Creature.Plant+YouCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.Shaman+StrictlyOther+YouCtrl`, `Creature.StrictlyOther`, `Creature.StrictlyOther+namedBaloth Packhunter`, `Creature.StrictlyOther+YouCtrl`, `Creature.StrictlyOther+YouCtrl+counters_GE1_P1P1`, `Creature.StrictlyOther+YouCtrl+sharesCreatureTypeWith Remembered`, `Creature.tapped+YouCtrl`, `Creature.targetedBy`, `Creature.TargetedPlayerCtrl`, `Creature.ThisTurnEntered`, `Creature.ThisTurnEntered+EnteredUnder You`, `Creature.token+YouCtrl`, `Creature.TriggeredAttacker,Creature.YouCtrl+sharesCreatureTypeWith TriggeredAttackerLKICopy`, `Creature.Vampire+YouCtrl`, `Creature.Warrior`, `Creature.White+YouCtrl`, `Creature.Wraith+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+!ThisTurnEntered+!attackedThisTurn`, `Creature.YouCtrl+attacking`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+counters_GE1_P1P1+StrictlyOther`, `Creature.YouCtrl+modified`, `Creature.YouCtrl+namedGruff_Triplets`, `Creature.YouCtrl+StrictlyOther`, `Creature.YouCtrl+StrictlyOther+token,Creature.YouCtrl+StrictlyOther+Rabbit`, `Creature.YouCtrl+tapped`, `Creature.YouCtrl+ThisTurnEntered`, `Creature.YouCtrl+toughnessLTX`, `Creature.YouCtrl+withFlash,Creature.YouCtrl+withHaste`, `Creature.YouCtrl+withFlying`, `Creature.YouCtrl+withLevel up`, `Creature.YouCtrl+withLifelink`, `Creature.YouCtrl+withMenace`, `Creature.YouCtrl+withModular`, `Creature.YouCtrl+withoutFlying`, `Creature.YouCtrl+withTrample`, `Creature.YouCtrl+withVigilance`, `Creature.YouCtrl,Vehicle.YouCtrl`, `Creature.YouDontCtrl`, `Creature.Zombie+YouCtrl`, `Dog.YouCtrl`, `Fractal.YouCtrl`, `Frog.ThisTurnEntered+YouCtrl,Rabbit.ThisTurnEntered+YouCtrl,Raccoon.ThisTurnEntered+YouCtrl,Squirrel.ThisTurnEntered+YouCtrl`, `Fungus`, `Fungus.YouCtrl`, `Goblin.YouCtrl`, `Human.YouCtrl+StrictlyOther`, `Knight.YouCtrl+StrictlyOther,Merfolk.YouCtrl+StrictlyOther`, `Leech.YouCtrl`, `Merfolk.YouCtrl`, `Moogle.Other+YouCtrl`, `Moogle.YouCtrl`, `Myr.YouCtrl`, `Ooze.YouCtrl`, `Permanent.counters_GE1_TIME`, `Permanent.withFading+YouCtrl`, `Permanent.YouCtrl+namedChitterspitter`, `Permanent.YouCtrl+namedMidnight Clock`, `Pest.YouCtrl,Bat.YouCtrl,Insect.YouCtrl,Snake.YouCtrl,Spider.YouCtrl`, `Planeswalker.YouCtrl`, `Planeswalker.YouCtrl+Red`, `Plant.YouCtrl`, `Saga.YouCtrl`, `Scout.YouCtrl,Pirate.YouCtrl,Rogue.YouCtrl`, `Soldier.YouCtrl`, `Soldier.YouCtrl+StrictlyOther`, `Spirit.YouCtrl`, `Squirrel.StrictlyOther+YouCtrl`, `Vampire.YouCtrl`, `Vampire.YouCtrl+StrictlyOther`, `Zombie.YouCtrl,Mutant.YouCtrl`
- `ValidCards2$`: TODO: Describe this parameter.
  Observed values: `Artifact.IsImprinted`, `Planeswalker.YouCtrl`, `Planeswalker.YouCtrl+StrictlyOther`
- `ValidCardsDesc$`: TODO: Describe this parameter.
  Observed values: `artifact creature and/or Vehicle you control`, `creature you control`, `creature you control with a +1/+1 counter on it.`, `other creature you control`, `Saga you control`, `Vampire you control`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Exile`

## `Radiation`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `TriggeredAttackingPlayer`, `TriggeredDefendingPlayer`, `TriggeredTarget`, `You`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `HalfXUp`, `TriggeredCard$CardPower`, `X`, `Z`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBP1P1`, `DBToken`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `RearrangeTopOfLibrary`

TODO: Write documentation.

**Parameters:**
- `AIRespondsToOwnAbility$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 U`, `1 U`, `3`, `G T`, `T`, `1`, `X`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `MayShuffle$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `X`
- `RearrangePlayer$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChoosePlayer`, `DBDraw`, `DBLoseLife`, `DBRearrange`, `DelTrigSlowtrip`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `Regenerate`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Instant.YouOwn,Sorcery.YouOwn`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T`, `1 G`, `PayLife<3>`, `G`, `2 B`, `1 B`, `T`, `1 C`, `0`, `Return<1/CARDNAME>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Exile the top creature card of your graveyard:`, `Pay {1} for each +1/+1 counter on CARDNAME:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Equipped`, `ParentTarget`, `Remembered`, `Self`, `Targeted`, `Targeted.Other+YouCtrl+Creature`, `Valid Creature.Werewolf+YouCtrl`, `Valid Creature.YouCtrl`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+blockedValidThisTurn Creature.Blue,Card.Self+blockedByValidThisTurn Creature.Blue`, `Creature.Colorless+YouCtrl+Other`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Formidable —`, `Threshold —`
- `RegenerationAbility$`: TODO: Describe this parameter.
  Observed values: `DBImmediateTrigger`, `TrigGainControl`
- `RememberObjects$`: TODO: Describe this parameter.
  Observed values: `TargetedPlayer`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`, `DBGainLife`, `DBLoseLife`, `TrigGorgonEffect`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Beast`, `Creature`, `Creature.Artifact`, `Creature.Black`, `Creature.Black,Creature.Green`, `Creature.counters_GE1_P1P1`, `Creature.Green`, `Creature.powerGE5`, `Creature.Vampire+Other`, `Creature.YouCtrl`, `Elephant`, `Elf.Other`, `Fungus`, `Goblin.Other`, `Golem.YouCtrl`, `Insect,Rat,Spider,Squirrel`, `Opponent`, `Permanent`, `Samurai`, `Shade,Skeleton,Specter,Spirit,Vampire,Wraith,Zombie`, `Sliver`, `Treefolk`, `Zombie`

## `Regeneration`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ReplacedCard`

## `RemoveCounter`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.EnchantedController`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AtOppEOT`, `Never`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Card.counters_GE1_TIME+inZoneBattlefield+YouDontCtrl,Card.suspended+YouCtrl`, `Creature.counters_GE1_M1M1`, `Permanent.counters_GE1_TIME+inZoneBattlefield+YouDontCtrl,Card.suspended+YouCtrl`, `Permanent.counters_GE1_TIME+YouDontCtrl,Card.suspended+YouCtrl`, `Saga.counters_GE1_LORE`
- `ChoiceNum$`: TODO: Describe this parameter.
  Observed values: `2`
- `ChoiceOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Artifact.HasCounters,Creature.HasCounters,Enchantment.HasCounters`, `Card.counters_GE1_HIT+OwnedBy TriggeredTarget`, `Card.suspended+YouOwn`, `Creature.YouCtrl+counters_GE1_P1P1`, `Permanent`, `Permanent.counters_GE1_STUN`, `Permanent.YouCtrl`, `Saga.YouCtrl`
- `ChoiceZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `AshlingNum`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.counters_GE3_RIBBON`, `Card.Self+blockedOrBeenBlockedSinceYourLastUpkeep`, `Card.Self+counters_GE3_BLOODLINE`, `Creature`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `X T`, `4`, `U B`, `3 T`, `AddCounter<0/LOYALTY>`, `3`, `Sac<1/Creature>`, `Sac<1/Artifact;Creature;Land/artifact, creature or land>`, `1 T Sac<1/CARDNAME>`, `T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Pay enchanted creature's mana cost:`, `Sacrifice an artifact, creature, or land:`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `2`, `3`, `4`, `5`, `All`, `Any`, `NumDmg`, `Result`, `SekkiX`, `X`, `Y`
- `CounterNumShared$`: TODO: Describe this parameter.
  Observed values: `True`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `All`, `Any`, `BAIT`, `BLOOD`, `BLOODLINE`, `BORE`, `CHARGE`, `DELAY`, `DEPLETION`, `DOOM`, `ECHO`, `EGG`, `EMBER`, `EYESTALK`, `FILIBUSTER`, `FLAME`, `FLOOD`, `FUNGUS`, `FUNK`, `FUSE`, `GLYPH`, `HATCHLING`, `HIT`, `HONE`, `HOPE`, `HOUR`, `ICE`, `Indestructible`, `INTERVENTION`, `LANDMARK`, `LORE`, `LOYALTY`, `M1M1`, `M2M2`, `MIRE`, `NET`, `NIGHT`, `OIL`, `OMEN`, `ORE`, `P1P0`, `P1P1`, `PARALYZATION`, `POINT`, `POISON`, `PUPA`, `RAD`, `RIBBON`, `RITUAL`, `SCREAM`, `SHELL`, `SHIELD`, `SLEEP`, `SLUMBER`, `SOUL`, `STUDY`, `STUN`, `TASK`, `TIDE`, `TIME`, `VORTEX`, `WAGE`, `WIND`, `WRECK`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `EffectSource`, `Enchanted`, `Imprinted`, `Opponent`, `OriginalHost`, `Remembered`, `RememberedLKI`, `ReplacedCard`, `ReplacedTarget`, `Self`, `Targeted`, `TriggeredBlockerLKICopy`, `Valid Permanent`, `You`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+suspended`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `RememberAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRemoved$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChangeZone`, `DBChangeZoneAll`, `DBChooseOpp`, `DBCleanup`, `DBClockworkDamage`, `DBConjure`, `DBCopy`, `DBDealDamage`, `DBDestroy`, `DBDig`, `DBDmg`, `DBDraw`, `DBEffect`, `DBExile`, `DBForget`, `DBGainLife`, `DBHeliodsPunishment`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBLosesGame`, `DBMoveToGraveyard`, `DBPump`, `DBPumpCreature`, `DBPumpOpponent`, `DBPutCounter`, `DBPutCounters`, `DBPutOntoStack`, `DBRadiation`, `DBReturn`, `DBSac`, `DBSacrifice`, `DBSacSelf`, `DBSeek`, `DBSekkiToken`, `DBTap`, `DBToken`, `DBTransform`, `DBUntap`, `ExileEffect`, `GameIsADraw`, `LoseGame`, `RepeatOnUpkeep`, `Sac`, `TrigGetMana`, `TrigPutCounter`, `Untap`, `WinnerDecided`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield,Exile`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `nonland permanent you control (remove counters)`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature,Planeswalker,Opponent`, `Artifact.nonCreature`, `Creature`, `Creature.OppCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Opponent`, `Permanent`, `Permanent,Opponent`, `Permanent.inZoneBattlefield,Card.suspended`, `Permanent.nonLand`, `Permanent.nonLand+YouCtrl`, `Permanent.Other,Opponent`, `Planeswalker`, `Planeswalker.OppCtrl`, `Player`, `Saga.YouCtrl`

## `RemoveCounterAll`

TODO: Write documentation.

**Parameters:**
- `AllCounters$`: TODO: Describe this parameter.
  Observed values: `True`
- `AllCounterTypes$`: TODO: Describe this parameter.
  Observed values: `True`
- `CounterNum$`: TODO: Describe this parameter.
  Observed values: `1`, `2`
- `CounterType$`: TODO: Describe this parameter.
  Observed values: `FATE`, `FLOOD`, `FUNGUS`, `GOLD`, `HOURGLASS`, `LOYALTY`, `M1M1`, `MINE`, `P1P1`, `ROPE`, `RUST`, `TIME`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanUp`, `DBRemove`, `QuickenTime`, `TrigCounters`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Card.Self`, `Card.suspended`, `Card.suspended+YouOwn`, `Card.YouOwn+!IsRemembered`, `Creature`, `Creature.YouCtrl`, `Land`, `Permanent`, `Permanent.ActivePlayerCtrl`, `Planeswalker`
- `ValidZone$`: TODO: Describe this parameter.
  Observed values: `Exile`

## `RemoveFromCombat`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Blockers`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `RemoveBestAttacker`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `IsForest`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `4 T`, `0`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`, `Self`, `Targeted`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `Valid Creature.attacking`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRemovedFromCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChooseAttacker`, `DBCantBlock`, `DBCleanup`, `DBDraw`, `DBTap`, `DBTreasureTree`, `DBUntap`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnblockCreaturesBlockedOnlyBy$`: TODO: Describe this parameter.
  Observed values: `Self`, `Targeted`, `TriggeredBlocker`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking+YouCtrl`, `Creature.attacking,Creature.blocking`, `Creature.blocking`, `Creature.DefendingPlayerCtrl`

## `RemoveFromGame`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `StackDescription$`: TODO: Describe this parameter.

## `RemoveFromMatch`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Self`
- `IncludeSideboard$`: TODO: Describe this parameter.
  Observed values: `True`
- `LogMessage$`: TODO: Describe this parameter.
  Observed values: `Torn to pieces and removed`
- `RemoveFromInventory$`: TODO: Describe this parameter.
  Observed values: `True`
- `RemoveType$`: TODO: Describe this parameter.
  Observed values: `Card.NamedCard`
- `StackDescription$`: TODO: Describe this parameter.

## `ReorderZone`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChoosePlayer`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`

## `Repeat`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `CopyBestCreature.IgnoreLegendary`, `MaxX`, `MaxXAtOppEOT`, `MaxY`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `ChoiceNum`, `TimesToFlip`, `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GT0`, `LTY`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T`, `AddCounter<1/LOYALTY>`, `XMin1 X T`, `XMin1 X G U`, `SubCounter<8/LOYALTY>`, `T Sac<1/Creature.Other/another creature>`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxRepeat$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `7`, `MaxRepeats`, `NumRemoved`, `X`, `Y`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RepeatCheckSVar$`: TODO: Describe this parameter.
  Observed values: `AccumulatedMilled`, `CheckNotPaid`, `CheckRepeat`, `FlipsDone`, `Left`, `LifePaid`, `Loss`, `MilledInsect`, `MilledSharesColor`, `MilledSharesType`, `NumPlayerGiveup`, `PlayerCountRemembered$HasPropertyYou`, `RepeatCheck`, `TaintedCheck`, `Total`, `X`
- `RepeatCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE8`
- `RepeatDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`
- `RepeatOptional$`: TODO: Describe this parameter.
  Observed values: `True`
- `RepeatOptionalDecider$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `RepeatPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.cmcGE4`, `Card.sharesNameWith Remembered`, `Land`, `Land.YouCtrl`, `Permanent`, `Permanent.nonland`
- `RepeatSubAbility$`: TODO: Describe this parameter.
  Observed values: `CheckLifePaid`, `CleanupBegin`, `DBChange`, `DBChangeZone`, `DBChoose`, `DBChooseAgain`, `DBCleanAndGrind`, `DBCleanBeforeRepeat`, `DBCleanLoop`, `DBCleanup`, `DBClear`, `DBConjure`, `DBDig`, `DBDiscard`, `DBDraw`, `DBExileCleanup`, `DBExileThree`, `DBFlip`, `DBGenericChoice`, `DBLoseLife`, `DBMakeCard`, `DBNameCard`, `DBOppChoose`, `DBPopulate`, `DBPump`, `DBRepeat`, `DBRepeatDraw`, `DBReset`, `DBResetCheck`, `DBRollDice`, `DBSac`, `DBSacrifice`, `DBToken`, `FlipAgain`, `Play`, `RepeatTorment`, `ResetCheck`, `Roll`, `TrigDiscard`, `TrigToken`
- `RepeatSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE2`, `GT0`, `LT2`, `LT7`, `LTTimesToFlip`, `LTTotalPlayer`, `LTX`, `LTY`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DamageCreature`, `DamageTarget`, `DBAddTurn`, `DBCleanup`, `DBDealDamage`, `DBMoveChosen`, `DBRepeatToken`, `DBRestore`, `DBReturn`, `DBSacHelm`, `DBShuffle`, `DBToken`, `DrawIfWin`, `FinalReset`, `Play`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.YouCtrl`, `Opponent`, `Player`

## `RepeatEach`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->Declare Attackers`, `Declare Blockers`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILifeThreshold$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AllPlayerLoseLife`, `BalanceLands`, `CloneAllTokens`, `EquipAll`, `Never`, `PriceOfProgress`
- `AmountFromVotes$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChangeZoneTable$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `FormidableTest`
- `ChooseOrder$`: TODO: Describe this parameter.
  Observed values: `RememberedPlayer`, `True`
- `ClearRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `ClearRememberedBeforeLoop$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Collected`, `Remembered`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `B R`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Creature`, `Instant.YouOwn,Sorcery.YouOwn`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE40`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<8/LOYALTY>`, `1 W`, `2 U T`, `1 U`, `T`, `Sac<1/Creature.White/White Creature>`, `SubCounter<2/LOYALTY>`, `AddCounter<1/LOYALTY>`, `4 T Sac<1/CARDNAME>`, `3`
- `DamageMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `DefinedCards$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DirectRemembered`, `DirectRemembered.Land`, `ImprintedLKI.RememberedPlayerCtrl`, `Remembered`, `Remembered.Plains`, `RememberedCard`, `RememberedLKI`, `Targeted`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `LoseLifeMap$`: TODO: Describe this parameter.
  Observed values: `True`
- `NextTurnForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionPrompt$`: TODO: Describe this parameter.
  Observed values: `Clone your other creatures with revealed?`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Formidable —`
- `RepeatCards$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Aura.CanEnchantSource+!Attached`, `Aura.IsRemembered`, `Aura.YouCtrl,Equipment.YouCtrl`, `Card.ChosenCard`, `Card.greatestRememberedCMC`, `Card.IsImprinted`, `Card.IsImprinted+RememberedPlayerOwn`, `Card.IsRemembered`, `Card.IsRemembered+Instant+Blue`, `Card.IsRemembered+nonLand`, `Card.NotedForMaelstromArchangelAvatar`, `Creature`, `Creature.attacking`, `Creature.attacking Player`, `Creature.attacking+modified+YouCtrl`, `Creature.attacking+Other+YouCtrl`, `Creature.attacking+Red`, `Creature.attacking+withoutFlying`, `Creature.attackingYouOrYourPW`, `Creature.blocking`, `Creature.counters_GE4_FUSE`, `Creature.Damaged`, `Creature.IsRemembered`, `Creature.nonDemon+nonDevil+nonImp`, `Creature.OppCtrl`, `Creature.Rat+YouCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.Spirit`, `Creature.TargetedPlayerCtrl`, `Creature.token`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Equipment.YouCtrl`, `Equipment.YouCtrl+namedHelm of Kaldra,Equipment.YouCtrl+namedSword of Kaldra,Equipment.YouCtrl+namedShield of Kaldra`, `Land`, `Land.YouCtrl+!TriggeredCard+sharesNameWith TriggeredCard`, `Permanent.nonBasic`, `Permanent.nonLand+TargetedPlayerCtrl+tapped`
- `RepeatOptionalForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `RepeatOptionalMessage$`: TODO: Describe this parameter.
  Observed values: `Do you want to copy the targeted spell?`, `Do you want to create a token that's a copy of that creature?`, `Do you want to create a Treasure token?`, `Do you want to create X 1/1 red Elemental creature tokens with haste?`, `Do you want to draw a card and create a 1/1 white Rabbit creature token?`, `Do you want to put a +1/+1 counter on each creature you control?`
- `RepeatPlayers$`: TODO: Describe this parameter.
  Observed values: `.Chosen,You`, `ImprintedController`, `ImprintedOwner`, `NonOpponent`, `NonTargetedController`, `OppNonRememberedController`, `OppNonTriggeredDefender`, `Opponent`, `Opponent.LostLifeThisTurn`, `Player`, `Player.Allies`, `Player.HasCardsInHand_Card_LTX`, `Player.NotedForDiscard`, `Player.NotedForFame`, `Player.NotedForFortune`, `Player.NotedForFriends`, `Player.NotedForMoney`, `Player.NotedForSecrets`, `Player.Opponent`, `Player.YourTeam`, `Remembered`, `RememberedController`, `Targeted`, `TargetedAndYou`, `TargetedController`, `TriggeredAttackedTarget`, `You`
- `RepeatSpellAbilities$`: TODO: Describe this parameter.
  Observed values: `Spell.OppCtrl,Activated.OppCtrl,Triggered.OppCtrl`
- `RepeatSubAbility$`: TODO: Describe this parameter.
  Observed values: `ArmToken`, `ArrestEach`, `BalanceLands`, `BatwingLoseLife`, `BrunaAttach`, `ChooseA1`, `ChooseA2`, `ChooseA3`, `ChooseArtf`, `ChooseC1`, `ChooseC2`, `ChooseC3`, `ChooseCard`, `ChooseCardsToTap`, `ChooseL1`, `ChooseL2`, `ChooseL3`, `ChooseThreePermanents`, `ChooseTwoGrave`, `DBAllAuraAttach`, `DBAnimate`, `DBAttach`, `DBAurora`, `DBBounce`, `DBChangeZone`, `DBChoice`, `DBChoose`, `DBChooseCard`, `DBChooseColor`, `DBChooseCounter`, `DBChooseKeep`, `DBChooseLT`, `DBChooseNum`, `DBChoosePermanent`, `DBChoosePlayer`, `DBChooseReturn`, `DBChooseType`, `DBChooseVictim`, `DBCleanup`, `DBClone`, `DBCloneAndBlock`, `DBConjure`, `DBCopy`, `DBCopyPermanent`, `DBCopyRandom`, `DBCounterUnless`, `DBDamage`, `DBDealDamage`, `DBDebuff`, `DBDefLeftEffect`, `DBDelayedTrigger`, `DBDestroy`, `DBDestroyRusted`, `DBDig`, `DBDigExile`, `DBDigUntil`, `DBDiscard`, `DBDiscardToDraw`, `DBDmg`, `DBDrain`, `DBDraw`, `DBDraw1`, `DBEffect`, `DBExile`, `DBFlip`, `DBFlip17`, `DBFluxDiscard`, `DBFriendsPump`, `DBGainLife`, `DBGetLandsOne`, `DBIncendiaryDiscard`, `DBLibrary`, `DBLoseLife`, `DBLoseLife2`, `DBManaReflect`, `DBMaySac`, `DBMill`, `DBMoneyPump`, `DBOppToken`, `DBPay`, `DBPlay`, `DBPump`, `DBPutCounter`, `DBRem`, `DBRemove`, `DBRepeatCard`, `DBRepeatCreature`, `DBReplace`, `DBReturn`, `DBReturnCreature`, `DBReturnLand`, `DBReveal`, `DBRevealCard`, `DBSac`, `DBSacEach`, `DBSacrifice`, `DBSearch`, `DBSecretsPump`, `DBSetLife`, `DBShuffle`, `DBTally`, `DBTap`, `DBToken`, `DBTokenOpp`, `DBTwoPiles`, `DBWheelDiscard`, `DmgEach`, `DmgOpp`, `Dream`, `EachDig`, `ExileYard`, `FlipClash`, `GainControl`, `GiveLifeEach`, `OpponentsChoose`, `OssuaryTokens`, `ParadePump`, `PumpOthers`, `Reveal`, `ShapeTgt`, `ShuffleHand`, `ShuffleSearched`, `TemptingChange`, `TokenBoar`, `TokenDragon`, `TrigChooseReturn`, `TrigDraw`, `TrigLoseAgain`, `TrigLoseLife`, `TrigSac`, `TyphoonDmg`, `UntapEach`, `WolfStrike`, `YouChoose`
- `RepeatTargeted$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `TargetedPlayer`, `True`
- `RepeatTypesFrom$`: TODO: Describe this parameter.
  Observed values: `ThisTurnCast_Card.nonCreature+YouCtrl+sharesCardTypeWith Remembered`, `Valid Permanent.OppCtrl`, `ValidGraveyard Card.OwnedBy TriggeredDefendingPlayer`, `ValidLibrary Card.IsImprinted`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StartingWith$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AllChoose`, `Battlefield`, `ChangePermanent`, `ClashDamage`, `CopyAgain`, `DBAtkLeftRight`, `DBBidding`, `DBChangeTargets`, `DBChangeZone`, `DBChangeZoneAll`, `DBChoose`, `DBChooseRandom`, `DBCleanRemembered`, `DBCleanup`, `DBCleanupBis`, `DBClearNotes`, `DBCopy`, `DBCopySelf`, `DBDestroy`, `DBDestroyAll`, `DBDraw`, `DBDraw2`, `DBEffect`, `DBExile`, `DBFinalReset`, `DBFortune`, `DBFriends`, `DBGainLife`, `DBIncendiaryDraw`, `DBMill`, `DBOnlyBlock`, `DBPhaseOut`, `DBPlayAll`, `DBPoison`, `DBPump`, `DBPutCounter`, `DBPutOnBattlefield`, `DBRepeatCard`, `DBRepeatEach`, `DBRepeatLand`, `DBRepeatPay`, `DBRepeatPut`, `DBRepeatToken`, `DBRepeatYou`, `DBReturn`, `DBReveal`, `DBSac`, `DBSacAll`, `DBScry`, `DBSearch`, `DBSecrets`, `DBShuffle`, `DBToken`, `DBTreasure`, `DBYouDraw`, `DelTrig`, `DestroyAll`, `ExileAll`, `ExileAllOthers`, `ExileAurora`, `ExileChosen`, `FilterCreature`, `HuntedDamage`, `Nightmare`, `PutCounterAgain`, `PutIntoHand`, `PWAway`, `RepeatLands`, `SacA1C2L3`, `SacA1L2C3`, `SacA2C3`, `SacA2L3`, `SacA3`, `SacAllOthers`, `SacC1A2L3`, `SacC1L2A3`, `SacC2A3`, `SacC2L3`, `SacC3`, `SacL1A2C3`, `SacL1C2A3`, `SacL2A3`, `SacL2C3`, `SacL3`, `ShipToBottom`, `WalkAway`, `ZoneAuras`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`, `MaxTargets`, `MaxTgt`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `X`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UseImprinted$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`, `Creature`, `Creature.attacking`, `Creature.YouCtrl`, `Creature.YouCtrl+!token`, `Instant,Sorcery`, `Opponent`, `Player`, `Player,Planeswalker`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `Snow`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Battlefield,Graveyard,Exile,Library,Hand`, `Exile`, `Hand`, `Library`

## `ReplaceCounter`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `ReplaceCount$CounterNum/Plus.1`, `ReplaceCount$CounterNum/Twice`, `X`, `Y`, `Z`
- `ChooseCounter$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBImmediateTrigger`
- `ValidCounterType$`: TODO: Describe this parameter.
  Observed values: `ENERGY`, `M1M1`, `P1P1`, `POISON`
- `ValidSource$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `You`

## `ReplaceDamage`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `AlchemicX`, `PaidAmount`, `ShieldAmount`, `X`, `Z`
- `DivideShield$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDealDamage`, `ExileEffect`, `RemoveCtrsRepl`

## `ReplaceEffect`

TODO: Write documentation.

**Parameters:**
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBExileEffect`, `ExileEffect`, `EyeForEye`, `IgnoreLowest`, `IgnoreRoll`
- `VarKey$`: TODO: Describe this parameter.
  Observed values: `You`
- `VarName$`: TODO: Describe this parameter.
  Observed values: `Affected`, `Amount`, `DamageAmount`, `DicePTExchanges`, `Ignore`, `IgnoreChosen`, `LifeGained`, `Num`, `Number`, `Result`
- `VarType$`: TODO: Describe this parameter.
  Observed values: `Card`, `CardSet`, `GameEntity`, `Map`, `PlanarDice`, `Player`
- `VarValue$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `Chaos`, `EffectSource`, `Enchanted`, `Equipped`, `MoltenX`, `Remembered`, `ReplaceCount$Amount/Twice`, `ReplaceCount$DamageAmount/Plus.1`, `ReplaceCount$DamageAmount/Plus.2`, `ReplaceCount$DamageAmount/Plus.Y`, `ReplaceCount$DamageAmount/Twice`, `ReplaceCount$Ignore/Plus.1`, `ReplaceCount$Num/Twice`, `ReplaceCount$Number/Plus.1`, `ReplacedSourceController`, `ReplacedTargetController`, `Self`, `StaggerX`, `WinX`, `X`, `Y`, `You`, `Z`

## `ReplaceMana`

TODO: Write documentation.

**Parameters:**
- `ReplaceAmount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `ReplaceColor$`: TODO: Describe this parameter.
  Observed values: `C`, `Chosen`, `White`
- `ReplaceMana$`: TODO: Describe this parameter.
  Observed values: `Any`, `B`, `C`
- `ReplaceOnly$`: TODO: Describe this parameter.
  Observed values: `W`
- `ReplaceType$`: TODO: Describe this parameter.
  Observed values: `Any`, `B`, `Black`, `C`, `G`, `R`, `Red`, `U`, `W`

## `ReplaceSplitDamage`

TODO: Write documentation.

**Parameters:**
- `DamageTarget$`: TODO: Describe this parameter.
  Observed values: `EffectSource`, `Imprinted`, `Remembered`, `You`
- `DivideShield$`: TODO: Describe this parameter.
  Observed values: `True`
- `VarName$`: TODO: Describe this parameter.
  Observed values: `ShieldAmount`, `X`, `Y`

## `ReplaceToken`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `HalfDown`, `Thrice`
- `NewController$`: TODO: Describe this parameter.
  Observed values: `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `TokenScript$`: TODO: Describe this parameter.
  Observed values: `c_1_1_a_thopter_flying`, `c_a_blood_draw`, `c_a_clue_draw`, `c_a_clue_draw,c_a_food_sac,c_a_treasure_sac`, `c_a_food_sac`, `c_a_map_sac_explore`, `c_a_mutagen_sac`, `c_a_treasure_sac`, `Chosen`, `g_1_1_frog`, `g_1_1_squirrel`, `g_2_2_cat_haste`, `g_3_1_dog_vigilance`, `u_3_3_shark`, `u_8_8_octopus`, `w_1_1_soldier`, `w_4_4_angel_flying_vigilance`
- `Type$`: TODO: Describe this parameter.
  Observed values: `AddToken`, `Amount`, `ReplaceController`, `ReplaceToken`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`
- `ValidChoices$`: TODO: Describe this parameter.
  Observed values: `Card.EnchantedBy`, `Card.EquippedBy`, `Creature.Other`

## `RestartGame`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<14/LOYALTY>`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RestrictFromValid$`: TODO: Describe this parameter.
  Observed values: `Card.!ExiledWithSource,Spell,Card.Aura`
- `RestrictFromZone$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ReturnFromExile`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`

## `Reveal`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Kefnet`
- `AnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `BecomeStartingPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T`, `2 U T`, `2 R T`, `2 G T`, `2 W T`, `T`, `2 B T`, `3 G`, `3 R`, `3 W`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player.Chosen`, `Player.IsRemembered`, `ReplacedPlayer`, `Targeted`, `TargetedController`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `NumCards$`: TODO: Describe this parameter.
  Observed values: `2`, `5`, `X`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OptionalDecider$`: TODO: Describe this parameter.
  Observed values: `You`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealAllValid$`: TODO: Describe this parameter.
  Observed values: `Card.cmcGE2+TargetedPlayerCtrl`, `Card.nonLand+nonCreature+TargetedPlayerCtrl`, `Card.nonLand+TargetedPlayerCtrl`, `Card.nonLand+TargetedPlayerOwn`, `Card.nonLand+TargetedPlayerOwn+cmcLE4`, `Creature.TargetedPlayerOwn,Land.TargetedPlayerOwn`
- `RevealDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `ReplacedCard`, `Self`, `TriggeredCard`, `ValidHand Card.IsRemembered+RememberedPlayerCtrl`
- `RevealTitle$`: TODO: Describe this parameter.
  Observed values: `Cards created by Maelstrom Archangel Avatar`
- `RevealToAll$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealValid$`: TODO: Describe this parameter.
  Observed values: `Card.Artifact+YouCtrl`, `Card.Black`, `Card.Blue`, `Card.Dragon+YouOwn`, `Card.Green`, `Card.Green+YouCtrl`, `Card.hasXCost+YouCtrl`, `Card.IsRemembered`, `Card.nonLand`, `Card.nonLand+YouOwn`, `Card.Red`, `Card.White`, `Creature`, `Creature.powerGE5+YouCtrl`, `Dinosaur`, `Dragon`, `Soldier`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBChangeZone`, `DBChoose`, `DBChooseCard`, `DBCinderDamage`, `DBCleanup`, `DBCounter`, `DBDamage`, `DBDementiaDiscard`, `DBDiscard`, `DBDiscard1`, `DBDmg`, `DBEffect`, `DBEvokeLand`, `DBExile`, `DBGain`, `DBGainLife`, `DBImmediateTrig`, `DBIvyPump`, `DBJasmineLife`, `DBLose`, `DBMana`, `DBMetalWorkerMana`, `DBNightshadePump`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBPutCounters`, `DBRepeat`, `DBScentOfBrineCounter`, `DBScentOfCinderDamage`, `DBScentOfIvyPump`, `DBScentOfJasmineLife`, `DBScentOfNightshadePump`, `DBSpeakerMana`, `DBTap`, `DBTrigger`, `DBTriggerLand`, `DelTrigSlowtrip`, `DrainOnUpkeep`, `ExchangeOwn1`, `ManaOnMain`, `PickOne`, `PlayChosen`, `ScryOnUpkeep`, `SetLifeOnUpkeep`, `TokenOnUpkeep`, `TrigEffect`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `RevealHand`

TODO: Write documentation.

**Parameters:**
- `AIPhyrexianPayment$`: TODO: Describe this parameter.
  Observed values: `Never`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `B B B T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Player.IsRemembered`, `Player.Opponent`, `Spawner>TriggeredTarget`, `Targeted`, `TargetedController`, `TriggeredDefendingPlayer`, `TriggeredTarget`, `You`
- `ImprintRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Look$`: TODO: Describe this parameter.
  Observed values: `True`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRevealed$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberRevealedPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealType$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `ChooseCard`, `Damage`, `DBChangeZone`, `DBChoose`, `DBChooseCard`, `DBChooseCardType`, `DBChooseW`, `DBCounter`, `DBDamage`, `DBDiscard`, `DBDraw`, `DBExile`, `DBGainLife`, `DBInHandDraw`, `DBLoseGame`, `DBNameCard`, `DBNotInHandDraw`, `DBPlay`, `DBRepeat`, `DBRepeatChoose`, `DBRepeatDiscard`, `DBRepeatEach`, `DBRevealTopLibrary`, `DBScryingGlassDraw`, `DBToken`, `DelTrigSlowtrip`, `ExileCard`, `MyPleasure`, `ShuffleCardToLib`, `TrigPlay`, `WinGame`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `ReverseTurnOrder`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T Exile<1/CARDNAME>`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBPlaneswalk`, `PWAway`

## `RingTemptsYou`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Resolved`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Spell.Legendary`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ2`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 B ExileFromGrave<1/CARDNAME>`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDigUntil`, `DBDraw`, `DBMill`, `DBPutCounter`, `TrigSearch`

## `RollDice`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Upkeep->Declare Attackers`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `Combat`, `CombatEarly`, `Main2`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `5`, `Count$TotalManaSpent Treasure/Plus.1`, `NbAttackedPlayers`, `X`
- `ChosenSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `5 U`, `2 G`, `3 T Sac<1/CARDNAME>`, `4 G T`, `1 T`, `tapXType<1/Bird>`, `AddCounter<0/LOYALTY>`, `T`, `AddCounter<1/LOYALTY>`, `4`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`, `You`
- `DifferentResults$`: TODO: Describe this parameter.
  Observed values: `True`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `EvenOddResults$`: TODO: Describe this parameter.
  Observed values: `True`
- `IgnoreLower$`: TODO: Describe this parameter.
  Observed values: `1`
- `InstantSpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `MaxRollsResults$`: TODO: Describe this parameter.
  Observed values: `True`
- `Modifier$`: TODO: Describe this parameter.
  Observed values: `CardsInHand`, `X`, `Y`
- `NoteDoubles$`: TODO: Describe this parameter.
  Observed values: `True`
- `OtherSVar$`: TODO: Describe this parameter.
  Observed values: `Y`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Circle of Death —`, `Search the Room —`
- `RememberHighestPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `RerollResults$`: TODO: Describe this parameter.
  Observed values: `True`
- `ResultSubAbilities$`: TODO: Describe this parameter.
  Observed values: `1-14:ChooseNew,Else:ChooseAndCopy`, `1-14:ChooseOne,Else:ChooseTwo`, `1-14:DBCopy,15-20:DBCopyRepeat`, `1-14:DBDraw,Else:DBScry`, `1-14:DBMayPlay,Else:DBMayPlayWithoutCost`, `1-14:DBToHand,Else:DBToField`, `1-14:MustBlock,15-20:ChooseBlock`, `1-14:ToHand,Else:HandAndLife`, `1-2:Token,3:Unearth,4-5:Damage,6:CometGo`, `1-3:AddC,Else:AddAny`, `1-3:DBLoseLife`, `1-3:DBScry`, `1-4:DBDamage`, `1-6:DBMana1,7-14:DBMana2,15-20:DBMana3`, `1-6:DBToken`, `1-9:DamageAll,10-20:DamageOpp`, `1-9:DBDamage,10-20:DBDamageAndTreasure`, `1-9:DBDamageToController,10-19:DBDamageToDefending,20:DBDamageToOpponents`, `1-9:DBDesc,10-20:DBReturn`, `1-9:DBDraw,10-20:DBDig`, `1-9:DBDraw2,10-19:DBScry2,20:DBScry3`, `1-9:DBHand,10-19:DBLibrary,20:DBControl`, `1-9:DBLibrary,10-20:DBHand`, `1-9:DBPump,10-19:DBPutCounter,20:DBMaxCounter`, `1-9:DBPutLand,10-19:DBToken,20:DBPutAll`, `1-9:DBSDamage,10-19:DBChooseCard,20:DBLDamage`, `1-9:DBSDraw,10-19:DBMDraw,20:DBLDraw`, `1-9:DBSToken,10-19:DBKToken,20:DBTokens`, `1-9:DBTap,10-20:DBReallyTap`, `1-9:DBTapAll,10-19:TapAndLock,20:TapLockETBEffect`, `1-9:DBToken,10-20:DBTokenAttach`, `1-9:DBX1,10-19:DBX2,20:DBX3`, `1-9:EachDraw,10-19:YouDraw,20:Copy`, `1-9:Exile1,10-19:Exile2,20:Exile3`, `1-9:Gain1,10-19:Gain2,20:Gain5`, `1-9:GreenOx,10-19:GreenBoar,20:WhiteGoat`, `1-9:LoseTwo,10-19:LoseGain,20:LoseTrea`, `1-9:OneOppSac,10-19:EachOppSac,20:SacTopPower`, `1-9:PlayCopy,10-19:PlayCost1,20:PlayAny`, `1-9:Pump1,10-19:Pump2,20:Pump3`, `1-9:PutOne,10-20:PutTwo`, `1-9:Sac1,10-19:SacOpp,20:SacOpp2`, `1-9:Scry1,10-19:Scry2,20:Scry3`, `1-9:Token1,10-19:Token2,20:Token3`, `1-9:ToLib,10-19:ToHand,20:ToField`, `1-9:TutuDaDome,10-19:WonTwoField,Else:ToFourField`, `1:DBChangeZone`, `1:DBCurse,2:DBCounter,3:DBDrain,4:DBCurseBis,5:DBDestroy,6:DBExile`, `1:DBNothing,2:DBArtif,3:DBLand,4:DBDamage,5:DBWheel,6:DBTwoMore`, `1:DBSac`, `1:DBSac,2:AddW,3:AddU,4:AddB,5:AddR,6:AddG`, `1:DBSac,Else:DBCounter`, `1:DBSkipTurn,12-20:DBDraw`, `1:M2,2:Fog,3:Vig,4:FS,5:Fly,6:P2`, `1:PumpPT,2:PumpMe,3:PumpVi,4:PumpLi,5:PumpFl,6:PumpIn`, `1:Trapped,2-9:DBToken,10-19:DBGainLife,20:DBChangeZone`, `2-3:DBSac,12:DBSac,7:DBSafe,11:DBSafe,Else:DBNote`, `20:Win,Else:Lose`, `2:GetGobTut,3:GetEnch,4:GetArtif,5:GetCreat,6:GetSpell`, `3-4:DBOne,5-6:DBTwo,1:DBRemove`, `5-6:DBUntap`, `6:DBSac`, `7:DBSac`, `Else:DBDiscard,1-9:DBReturn,10-19:DBDrawTwo,20:DBReanimate`
- `ResultSVar$`: TODO: Describe this parameter.
  Observed values: `diePwr`, `dieTgn`, `Result`, `SetPwr`, `SetTgn`, `X`, `Y`
- `Sides$`: TODO: Describe this parameter.
  Observed values: `10`, `12`, `20`, `4`, `6`, `8`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StoreResults$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Add0`, `Crash`, `DBAnimate`, `DBAssemble`, `DBChange`, `DBChangeZone`, `DBCheck`, `DBCounters`, `DBCountersEnd`, `DBCountersETB`, `DBCountersUpkeep`, `DBCreateTreasure`, `DBDamage`, `DBDamageAll`, `DBDecr`, `DBDestroy`, `DBDouble`, `DBDraw`, `DBEffect`, `DBGainLife`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBImmediateTrigPutCounter`, `DBLife`, `DBLoyalty`, `DBMill`, `DBPump`, `DBPutCounter`, `DBReturn`, `DBReveal`, `DBScry`, `DBToken`, `DBTreasure`, `DmgPlus`, `PumpDS`, `RollTough`, `Tokens`, `TrigDraw`, `Tuck`
- `SubsForEach$`: TODO: Describe this parameter.
  Observed values: `True`
- `ToVisitYourAttractions$`: TODO: Describe this parameter.
  Observed values: `True`
- `UseDifferenceBetweenRolls$`: TODO: Describe this parameter.
  Observed values: `True`
- `UseHighestRoll$`: TODO: Describe this parameter.
  Observed values: `True`

## `RollPlanarDice`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.

## `RunChaos`

TODO: Write documentation.

**Parameters:**
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChangeZone`

## `Sacrifice`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `DesecrationDemon`, `ExceptSelf`, `Lethal`, `OpponentOnly`, `SacToReduceCost`, `WorstCard`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `13`, `2`, `3`, `4`, `5`, `6`, `7`, `Amt`, `Count$Valid Permanent.YouCtrl`, `CurseX`, `DevourSacX`, `E`, `EdictX`, `G`, `OppX`, `PermanentsToSac`, `SacX`, `ThisTargetedPlayer$Valid Creature.YouCtrl/HalfUp`, `VoteNum`, `X`, `Y`, `Z`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ChangeNum$`: TODO: Describe this parameter.
  Observed values: `1`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `DecreeX`, `FadingCheckSVar`, `Found`, `MilledCreature`, `MilledSharesAllTypes`, `PermanentsToSac`, `Result`, `SacX`, `StillLooking`, `TotalPower`, `WarElementalX`, `X`, `XDelirium`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ13`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Collected`, `Remembered`, `RememberedLKI`, `Self`, `TriggeredAttackerLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If that land was legendary,`
- `ConditionManaNotSpent$`: TODO: Describe this parameter.
  Observed values: `U`
- `ConditionNotPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+escaped`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.counters_EQ0_HOPE`, `Card.counters_EQ0_OIL`, `Card.counters_GE3_P1P1`, `Card.Creature`, `Card.NamedCard`, `Card.nonRed`, `Card.Self+!attackedThisTurn`, `Card.Self+counters_EQ0_DEPLETION`, `Card.Self+counters_EQ0_ECHO`, `Card.Self+counters_EQ0_MINING`, `Card.Self+counters_EQ0_TIME`, `Card.Self+counters_GE13_RELEASE`, `Card.Self+counters_GE2_VELOCITY`, `Card.Self+counters_GE3_COLLECTION`, `Card.Self+counters_GE3_DOOM`, `Card.Self+counters_GE5_BLOODSTAIN`, `Card.Self+counters_GE5_POINT`, `Card.YouCtrl`, `Forest`, `Island`, `Land.Legendary`, `Land.YouCtrl`, `Ogre.YouCtrl`, `Permanent.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQY`, `GE1`, `GE2`, `GE8`, `GT0`, `LE0`, `LEY`, `LT1`, `LT12`, `LT3`, `LTX`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Waterbend<3>`, `1 C`, `4 B T Sac<1/CARDNAME>`, `SubCounter<2/LOYALTY>`, `R R Discard<X/Random>`, `1 B Sac<1/Creature>`, `6 B R Sac<X/Creature/any number of creatures>`, `B R Sac<1/Permanent.nonLand/nonland permanent>`, `1 R`, `2 W`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `.Chosen,You`, `Card.Self`, `ChosenPlayer`, `FlippedTails`, `OppNonParentTarget`, `Opponent`, `ParentTarget`, `Player`, `Player.controlsPermanent.EnchantedBy`, `Player.IsRemembered`, `Player.Opponent`, `Player.Other`, `Player.TappedLandForManaThisTurn`, `Player.withMostTypeLand`, `Remembered`, `RememberedController`, `ReplacedCardController`, `Self`, `Targeted`, `TargetedController`, `TargetedOrController`, `TriggeredActivator`, `TriggeredAttackingPlayer`, `TriggeredCardController`, `TriggeredCardOpponent`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `TriggeredTargetController`, `You`
- `Destroy$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `TgtChoose`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OrString$`: TODO: Describe this parameter.
  Observed values: `Sacrifice it.`, `Sacrifice {c:Self}.`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `1`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE6`
- `Random$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberSacrificed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SacEachValid$`: TODO: Describe this parameter.
  Observed values: `True`
- `SacMessage$`: TODO: Describe this parameter.
  Observed values: `a creature with the least toughness among creatures you control`, `Another target creature`, `any number of creatures and/or planeswalkers`, `any number of creatures each with base power or toughness 1 or less`, `attached Equipment`, `Attacking Creature`, `attacking creature`, `attacking or blocking Creature`, `Creature`, `creature or planeswalker`, `creature or planeswalker they control with the highest mana value among creatures and planeswalkers they control`, `creature other than enchanted creature`, `Creature that attacked or blocked this turn`, `creature token`, `creature with flying`, `creature with mana value 3 or less`, `Egg you control`, `enchanted creature`, `Food token`, `Green or White Creature`, `Island or a blue permanent`, `land`, `monocolored creature`, `non-Demon creature`, `non-Demon Permanent`, `non-Zombie Creature`, `nonbasic land`, `noncreature artifact`, `noncreature, nonland permanent`, `nonland permanent`, `nontoken artifact`, `nontoken creature`, `nontoken creature or planeswalker`, `nontoken enchantment`, `nontoken permanent`, `other creature or artifact`, `permanent`, `permanent that shares a card type with the chosen card`, `permanent that shares a type with the sacrificed permanent`, `permanent that shares type with it`, `Swamp or a black permanent`, `the creature with the greatest power`, `the creature with the highest mana value`, `this land`, `three creatures`, `Zombies`
- `SacValid$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact & Creature & Enchantment & Land & Planeswalker`, `Artifact & Land`, `Artifact,Creature`, `Artifact,Creature,Enchantment,Land,Planeswalker`, `Artifact,Creature,Land`, `Artifact,Enchantment`, `Artifact.!token`, `Artifact.EnchantedBy`, `Artifact.nonCreature`, `Artifact.Other`, `Artifact.Other,Creature.Other`, `Beeble`, `Card.AttachedBy`, `Card.ChosenCard`, `Card.Self`, `Creature`, `Creature & Planeswalker`, `Creature,Artifact`, `Creature,Artifact,Land`, `Creature,Enchantment`, `Creature,Land`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!EnchantedBy`, `Creature.!firstTurnControlled`, `Creature.!token`, `Creature.!token,Planeswalker.!token`, `Creature.Artifact & Creature.nonArtifact`, `Creature.attackedThisTurn,Creature.blockedThisTurn`, `Creature.attacking`, `Creature.attacking,Creature.blocking`, `Creature.basePowerLE1,Creature.baseToughnessLE1`, `Creature.blockingTriggeredAttacker`, `Creature.cmcEQX,Planeswalker.cmcEQX`, `Creature.cmcLE3`, `Creature.dealtCombatDamageThisTurn You`, `Creature.greatestPowerControlledByTargeted`, `Creature.Human`, `Creature.leastPowerControlledByTriggeredDefendingPlayer`, `Creature.leastToughnessControlledByTriggeredPlayer`, `Creature.MonoColor`, `Creature.nonArtifact`, `Creature.nonBlack`, `Creature.nonDemon`, `Creature.nonElf`, `Creature.nonGod`, `Creature.nonGorgon`, `Creature.nonVampire`, `Creature.nonZombie`, `Creature.NotDefinedTargeted`, `Creature.Other`, `Creature.Other,Land.Other`, `Creature.Other,Planeswalker`, `Creature.Other,Planeswalker.Other`, `Creature.token`, `Creature.White,Creature.Green`, `Creature.withFlying`, `Egg.YouCtrl`, `Enchantment`, `Enchantment,Artifact,Card.token`, `Enchantment.!token`, `Equipment.AttachedTo Card.Self`, `Food`, `Food.token`, `Forest`, `Forest.untapped`, `Homunculus`, `Island`, `Island,Card.Blue`, `Island.untapped`, `Kindred`, `Kraken`, `Land`, `Land,Creature`, `Land.nonBasic`, `Land.untapped`, `Land.withoutIndestructible`, `Merfolk`, `Mountain`, `Mountain.untapped`, `Permanent`, `Permanent.!token`, `Permanent.ChosenCard`, `Permanent.ChosenType`, `Permanent.Green,Permanent.White`, `Permanent.MultiColor`, `Permanent.nonColorless`, `Permanent.nonCreature+nonLand`, `Permanent.nonDemon`, `Permanent.nonLand`, `Permanent.nonLand+!token`, `Permanent.Other`, `Permanent.sharesCardTypeWith RememberedCard`, `Permanent.sharesCardTypeWith Sacrificed`, `Permanent.sharesCardTypeWith Targeted`, `Permanent.YouCtrl`, `Plains`, `Plains,Permanent.White`, `Planeswalker`, `Powerstone`, `Self`, `Snake`, `Swamp`, `Swamp,Card.Black`, `TargetedCard.Self`, `Treasure`, `TriggeredAttacker`, `TriggeredCard.sharesCardTypeWith`, `Vampire`, `Zombie`
- `ShowSacrificedCards$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StrictAmount$`: TODO: Describe this parameter.
  Observed values: `True`
- `SuAbility$`: TODO: Describe this parameter.
  Observed values: `DBLoseLife`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AllFoundCelebration`, `CrashDamage`, `DBAddTurn`, `DBAnimate`, `DBBolster`, `DBBranch`, `DBChange`, `DBChangeZone`, `DBChangeZoneAll`, `DBCleanup`, `DBCleanup2`, `DBCleanupChosen`, `DBCoin`, `DBConjure`, `DBCopy`, `DBCoralCleanup`, `DBCurseArtifactDamage`, `DBCursePutCounter`, `DBDamage`, `DBDamageAll`, `DBDealDamage`, `DBDestroy`, `DBDestroyAll`, `DBDig`, `DBDigUntil`, `DBDiscard`, `DBDiscardOpp`, `DBDmg`, `DBDrain`, `DBDraw`, `DBEdict`, `DBEffect`, `DBElderSpawnDamage`, `DBElderSpawnSacrificeMe`, `DBExile`, `DBFood`, `DBGainLife`, `DBGenericChoice`, `DBGraveyard`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBIntensify`, `DBInvestigate`, `DBLand`, `DBLoseLife`, `DBLoseLife2`, `DBLoseLifeC`, `DBLoseLifeE`, `DBLoseLifeOpp`, `DBLoseLifeP`, `DBMana`, `DBNameCard`, `DBOpen`, `DBOpenSafe`, `DBPlaneswalk`, `DBPoison`, `DBPump`, `DBPutCounter`, `DBRageDamage`, `DBRepeat`, `DBRepeatEach`, `DBReturn`, `DBReturnChoose`, `DBReveal`, `DBSac`, `DBSac2`, `DBSacCreature`, `DBSacEnchantment`, `DBSacKindred`, `DBSacLand`, `DBSacPlaneswalker`, `DBSacrifice`, `DBSacrificeBoth`, `DBSacSelf`, `DBScry`, `DBSearch`, `DBShift`, `DBStealCreature`, `DBTap`, `DBToken`, `DBTransform`, `DBTreasure`, `DBTrigger`, `DevourCounters`, `Discard`, `DiscardIf`, `Dmg`, `EvidenceCollected`, `FetchLands`, `FluesDig`, `GainLife`, `GrabDmg`, `HalfHeartDBDamage`, `IdolWalk`, `LetEmHaveIt`, `MakeToken`, `MoveToGraveyard`, `NettlevineAttach`, `ResetFlips`, `ReturnGrave`, `Rise`, `RollD20`, `RuptureDmg`, `SacrificeCreatures`, `StoreCanSearch`, `TrigChoose`, `TrigConjure`, `TrigDamage`, `TrigImmediate`, `TrigImmediateTrig`, `TrigPayCost`, `TrigTempt`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessColor$`: TODO: Describe this parameter.
  Observed values: `G`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `1 U`, `1 W`, `2`, `2 B B`, `3`, `B`, `B B`, `B B B B`, `B R G`, `DamageYou<4>`, `DamageYou<5>`, `DefinedCost_ChosenCard`, `DefinedCost_Self`, `Discard<1/Card.nonCreature>`, `Discard<1/Card>`, `Discard<1/Creature>`, `Discard<1/Land>`, `Discard<1/Random>`, `Discard<2/Card>`, `ExileFromGrave<1/Card.TopGraveyardCreature>`, `ExileFromGrave<1/Card>`, `G`, `G G`, `G W U`, `Mandatory ExileFromGrave<2/Card>`, `Mill<2>`, `PayEnergy<1>`, `PayEnergy<2>`, `PayLife<1>`, `PayLife<2>`, `PutCardToLibFromGrave<1/-1/Card>`, `PutCardToLibFromGrave<2/-1/Card>`, `R G W`, `R R R R`, `R W B`, `RemoveAnyCounter<1/Any/Permanent>`, `Return<1/Artifact>`, `Return<1/Creature.Other/other creature>`, `Return<1/Forest.untapped/untapped Forest>`, `Return<1/Island.untapped+YouCtrl/untapped Island you control>`, `Return<1/Island.untapped/untapped Island>`, `Return<1/Land.nonLair/non-Lair land>`, `Return<1/Land>`, `Return<1/Mountain.untapped/untapped Mountain>`, `Return<1/Plains.untapped/untapped Plains>`, `Return<1/Swamp.untapped/untapped Swamp>`, `Return<2/Forest>`, `Return<3/Land.Basic>`, `Sac<1/Artifact>`, `Sac<1/Creature>`, `Sac<1/Enchantment>`, `Sac<1/Forest>`, `Sac<1/Island>`, `Sac<1/Land>`, `Sac<1/Mountain>`, `Sac<1/Pegasus>`, `Sac<2/Creature>`, `Sac<2/Land>`, `Sac<2/Mountain>`, `Sac<2/Swamp>`, `Sac<3/Forest>`, `Sac<4/Creature>`, `Sac<5/Land>`, `SubCounter<1/P1P1>`, `tapXType<1/Artifact;Land/artifact or land>`, `tapXType<1/Creature>`, `tapXType<1/Permanent>`, `U`, `U B R`, `U U`, `UpkeepX`, `W U`, `W U B`, `W U B R G`, `W W`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.IsRemembered`, `Remembered`, `TriggeredActivator`, `TriggeredCardController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCard$`: TODO: Describe this parameter.
  Observed values: `Card.Self`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`, `Player.Opponent`

## `SacrificeAll`

TODO: Write documentation.

**Parameters:**
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `HellionEruption`, `MadSarkhanDragon`, `ShapeAnew`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `TotalPower`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `DelayTriggerRememberedLKI`, `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.cmcLE3`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE12`
- `Controller$`: TODO: Describe this parameter.
  Observed values: `OriginalHostController`, `TriggeredPlayer`, `You`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`, `1 T`, `7`, `0`, `SubCounter<2/LOYALTY>`, `Discard<2/Card>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `AttachedBy TriggeredCardLKICopy`, `ChosenCard`, `DelayTriggerRememberedLKI`, `DirectRemembered`, `EffectSource`, `Enchanted`, `Equipped`, `OriginalHost`, `Remembered`, `RememberedLKI`, `Self`, `Targeted`, `TriggeredAttackers`, `TriggeredBlockers`, `TriggeredCardLKICopy`, `TriggeredObjectLKICopy`
- `ImprintSacrificed$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberSacrificed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBBounce`, `DBChange`, `DBCleanA1C2L3`, `DBCleanA1L2C3`, `DBCleanA3`, `DBCleanC1A2L3`, `DBCleanC1L2A3`, `DBCleanC3`, `DBCleanL1A2C3`, `DBCleanL1C2A3`, `DBCleanL3`, `DBCleanup`, `DBCleanup2`, `DBConjure`, `DBDamage`, `DBDamageAll`, `DBDig`, `DBDigUntil`, `DBDiscardHand`, `DBDmg`, `DBDrain`, `DBDraw`, `DBEffect`, `DBGainControl`, `DBGainLife`, `DBLifeGain`, `DBPutCounter`, `DBRepeat`, `DBRepeatEach`, `DBReturn`, `DBReturnAll`, `DBToken`, `MoveToBattlefield`, `ReturnAll`, `StillFurious`, `TrigImmediateTrig`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `DefinedCost_Remembered_Minus2`, `PayEnergy<N>`, `PayEnergy<X>`, `W U B R G`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `You`
- `UnlessUpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Enchantment,Land.nonBasic`, `Artifact.IsRemembered`, `Card.ChosenCardStrict`, `Card.EnchantedBy`, `Card.IsImprinted`, `Card.IsRemembered`, `Creature`, `Creature.!ChosenCard`, `Creature.!IsImprinted`, `Creature.!IsRemembered`, `Creature.!IsRemembered+ControlledBy Player.IsRemembered`, `Creature.ChosenCard`, `Creature.IsImprinted`, `Creature.IsRemembered`, `Creature.nonChosenCard`, `Creature.nonChosenCard+OppCtrl`, `Creature.nonChosenCard,Planeswalker.nonChosenCard`, `Creature.nonOgre+YouCtrl`, `Creature.Other+YouCtrl`, `Creature.StrictlyOther`, `Creature.YouCtrl`, `Dragon.YouCtrl`, `Land`, `Land.IsRemembered`, `Land.nonChosenCard`, `Land.YouCtrl`, `Permanent.!token+setARN+Other`, `Permanent.!token+setATQ`, `Permanent.IsRemembered`, `Permanent.nonChosenCard`, `Permanent.nonChosenCard+OppCtrl`, `Permanent.nonColorless`, `Permanent.nonLand+!IsRemembered`, `Permanent.nonLand+nonChosenCard`, `Permanent.nonLand+OppCtrl+nonChosenCard`, `Permanent.YouCtrl+namedSheltered Valley`, `Permanent.YouCtrl+StrictlyOther`, `Reflection.YouCtrl`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Creature`, `Creature.Artifact`, `Creature.ControlledBy TriggeredTarget`, `Permanent`

## `Scry`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtOppEOT`, `BestOpportunity`, `BrainJar`, `MultipleChoice`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Bargain`, `Foretold`, `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CreatureETBAmount`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GE2`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Self`, `Targeted`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Ally`, `Card`, `Card.Aura`, `Card.cmcLE2`, `Card.cmcLE3`, `Card.Self+counters_LE6_PHYRESIS`, `Card.wasCast`, `Enchantment.YouCtrl`, `Instant.YouOwn,Sorcery.YouOwn`, `Player`, `Rabbit.YouCtrl`, `Spell.Jace+Planeswalker`, `Wolf.YouCtrl,Werewolf.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE3`, `GE4`, `NE2`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T PayEnergy<1>`, `4 G U`, `1`, `1 B Sac<1/Creature.Other/another creature>`, `3 T SubCounter<X/CHARGE>`, `2 U U T`, `1 T`, `2 U Sac<1/CARDNAME>`, `T SubCounter<1/OIL/CARDNAME>`, `1 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `Player`, `TriggeredCardController`, `TriggeredOpponentVotedSame & You`, `You`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Creature.Legendary+YouCtrl`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `OrOtherConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `ScryNum$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `Result`, `X`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChoice`, `DBCleanup`, `DBCounter`, `DBDamageAll`, `DBDealDamage`, `DBDig`, `DBDraw`, `DBDraw2`, `DBDraw3`, `DBEffect`, `DBEnergy`, `DBExile`, `DBExplore`, `DBLandmark`, `DBLoseLife`, `DBPeekAndReveal`, `DBPutCounter`, `DBReveal`, `DBScry`, `DBScry2`, `DBScry3`, `DBToken`, `Draw`, `Draw2`, `OraclesInsightDraw`, `TrigGainLife`, `TrigPutCounter`, `TrigTempt`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GEY`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `Sac<1/Creature.Other/another creature>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `Seek`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `SacAndUpgrade`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `TriggeredCard`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.Self+PromisedGift`, `Creature`, `Creature.cmcGE4`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Discard<1/Card>`, `2 G`, `ExileCtrlOrGrave<1/Artifact.Other>`, `4 T`, `1 Sac<1/Clue>`, `SubCounter<1/LOYALTY>`, `3 B T`, `3 G T`, `3 U T`, `3 W T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ImprintedController`, `ParentTarget`, `Player`, `RememberedOwner`, `TargetedController`, `You`
- `DefinedCards$`: TODO: Describe this parameter.
  Observed values: `Top_10_OfLibrary`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ImprintFound$`: TODO: Describe this parameter.
  Observed values: `True`
- `Num$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `X`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Domain —`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberFound$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAnimate`, `DBAnimateW`, `DBBattlefield`, `DBBottomCard`, `DBChangeZone`, `DBChangeZone1`, `DBChooseCard`, `DBCleanup`, `DBCloak`, `DBDelay`, `DBDelayTrig`, `DBDiscard`, `DBEffect`, `DBExile`, `DBManifest`, `DBPump`, `DBPump2`, `DBPut`, `DBRemoveCounter`, `DBShuffle`, `Shuffle`, `TrigImmediateTrig`
- `Type$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.nonLand+cmcLEX`, `Card.!sharesCardTypeWith Remembered`, `Card.ChosenType`, `Card.cmcEQX`, `Card.cmcEQX+YouOwn`, `Card.cmcEQY`, `Card.cmcGTX`, `Card.cmcLTX`, `Card.Creature`, `Card.Creature+cmcLEX`, `Card.Creature+MostProminentCreatureTypeInLibrary`, `Card.Dragon`, `Card.Elf`, `Card.Historic`, `Card.Instant+cmcEQ3,Card.Sorcery+cmcEQ3`, `Card.Instant,Card.Sorcery`, `Card.Land`, `Card.Land+Basic`, `Card.Land+Urza's`, `Card.namedAudacious Knuckleblade`, `Card.nonCreature+nonLand`, `Card.nonLand`, `Card.nonLand+cmcEQX`, `Card.nonLand+cmcLE2`, `Card.nonShark`, `Card.Permanent+ChosenType`, `Card.Permanent+cmcEQX`, `Card.Permanent+nonLand`, `Card.Permanent+nonLand+cmcLE3`, `Card.sharesCardTypeWith Remembered`, `Card.sharesCardTypeWith TriggeredCards`, `Card.SharesColorWith Valid Permanent.YouCtrl`, `Card.Survivor+cmcLEX`, `Card.withStart your engines`, `Creature`, `Creature.cmcEQX`, `Creature.cmcLE2`, `Creature.cmcLE3+YouOwn`, `Creature.cmcLTX`, `Creature.nonElephant+cmcLE3`, `Creature.YouOwn+cmcLE3`, `Dragon`, `Forest`, `Instant,Sorcery`, `Instant.cmcLE3,Sorcery.cmcLE3`, `Kithkin`, `Land`, `Land.hasABasicLandType`, `Land.nonBasic`, `Merfolk`, `Permanent.nonLand+cmcLEX`, `Pirate`, `Rat`, `Spacecraft`, `Vampire`
- `Types$`: TODO: Describe this parameter.
  Observed values: `Card.Land,Card.nonLand`, `Card.YouOwn+cmcLE2,Card.YouOwn+cmcGE3`, `Mountain,Forest,Land.nonMountain+nonForest`

## `SetInMotion`

TODO: Write documentation.

**Parameters:**
- `Again$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `RepeatNum$`: TODO: Describe this parameter.
  Observed values: `3`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `ExilePlot`

## `SetLife`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `ChoiceAmount$`: TODO: Describe this parameter.
  Observed values: `Any`
- `ChoicePrompt$`: TODO: Describe this parameter.
  Observed values: `Choose any number of players`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 W W ExileFromGrave<1/CARDNAME>`, `SubCounter<3/LOYALTY>`, `SubCounter<10/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`, `Player.IsRemembered`, `Player.Opponent`, `RememberedOwner`, `TriggeredDefender`, `TriggeredSourceController`, `You`
- `LifeAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `15`, `20`, `26`, `3`, `4`, `5`, `7`, `HalfLife`, `X`, `Y`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerChoices$`: TODO: Describe this parameter.
  Observed values: `Player`
- `Redistribute$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBEffect`, `DBExile`, `DBLoseGame`, `DBLoseHalf`, `DBNoCombatDamage`, `DBNoUntap`, `DBShuffle`, `ExileEffect`, `ExileSelf`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `SetState`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Delirium`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `Never`, `PowerDmg`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `NumHumanWerewolves`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Creature.faceDown+YouCtrl`, `Human.Werewolf+YouCtrl+CanTransform`, `Incubator.token+YouCtrl`, `Permanent.faceDown+YouCtrl`
- `ChoiceTitle$`: TODO: Describe this parameter.
  Observed values: `Choose an Incubator token you control`, `Choose any number of Human Werewolves you control`, `Select a face-down creature you control`, `Select a face-down permanent you control`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `A`, `AFLifeLost`, `CheckHandLand`, `Count$RememberedNumber`, `Discharged`, `FormidableTest`, `HandSize`, `NumTreasure`, `TrigAmount`, `X`, `Y`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE10`, `GE3`, `GE4`, `GE7`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Self`, `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact.YouCtrl`, `Card`, `Card.counters_GE3_INVITATION`, `Card.Creature`, `Card.ExiledWithSource`, `Card.Instant,Card.Sorcery`, `Card.inZoneHand`, `Card.Self+counters_EQ0_ICE`, `Card.Self+counters_EQ0_OMEN`, `Card.Self+counters_EQ0_P1P1`, `Card.Self+counters_GE3_DREAD`, `Card.Self+powerGE5`, `Card.Wizard+YouCtrl`, `Card.YouOwn`, `Creature.cmcGE6`, `Creature.counters_GE3_P1P1`, `Creature.toughnessGE6`, `Creature.YouOwn`, `Land.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ2`, `EQ4`, `GE1`, `GE10`, `GE3`, `GE5`, `GE7`, `GE8`, `GE9`, `GEY`, `GT1`, `LEY`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Exile`, `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `Waterbend<8>`, `2 B T`, `4 UP`, `1 W W`, `U`, `R`, `5 RP`, `5 G U T`, `3 GP`, `B`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `ExiledWith`, `ExiledWithSource`, `Remembered`, `Self`, `TriggeredCard`, `TriggeredSourceLKICopy`, `Valid Creature.!token+Other+faceUp`, `Valid Creature.Human`, `Valid Incubator.token+YouCtrl`, `ValidExile Card.ExiledWithSource`
- `FaceDownPower$`: TODO: Describe this parameter.
  Observed values: `2`
- `FaceDownSetType$`: TODO: Describe this parameter.
  Observed values: `Artifact & Creature & Cyberman`, `Horror & Creature`
- `FaceDownToughness$`: TODO: Describe this parameter.
  Observed values: `2`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.canBeTurnedFaceUp+faceDown`, `Card.Self+counters_EQ0_TIME`, `Card.Vampire+YouCtrl`, `Permanent.YouCtrl`
- `Mandatory$`: TODO: Describe this parameter.
  Observed values: `True`
- `MinAmount$`: TODO: Describe this parameter.
  Observed values: `0`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `Flip`, `Transform`, `TurnFaceDown`, `TurnFaceUp`, `Unspecialize`
- `NewState$`: TODO: Describe this parameter.
  Observed values: `FaceDown`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Coven —`, `Delirium —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`, `GE5`
- `PresentDefined$`: TODO: Describe this parameter.
  Observed values: `TriggeredSourceLKICopy`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberChanged$`: TODO: Describe this parameter.
  Observed values: `True`
- `RevealFirst$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAdapt`, `DBAttach`, `DBChangeZone`, `DBCleanup`, `DBCounter`, `DBCurseNonWolves`, `DBDouble`, `DBGainLife`, `DBImmediateTrig`, `DBLoseLife`, `DBMana`, `DBPump`, `DBPumpAll`, `DBReturn`, `DBSetLife`, `DBToken`, `DBTokenLaserbeak`, `DBTokenRavage`, `DBTreasureTokens`, `DBUntap`, `ExileSelf`, `ExtraBeginningPhase`, `IgnitionDamage`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`, `GE4`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `WeaverofLiesX`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `4 U U`, `Sac<1/Creature>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`, `You`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidNewFace$`: TODO: Describe this parameter.
  Observed values: `Creature`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact.Other+DoubleFaced+YouCtrl`, `Card.faceDown`, `Card.Werewolf+YouCtrl`, `Creature`, `Creature.faceDown`, `Creature.faceDown+attacking+YouCtrl`, `Creature.faceDown+OppCtrl`, `Creature.tapped+!token`, `Creature.withMorph+Other,Creature.withMegamorph+Other`, `Creature.withMorph,Creature.withMegamorph`, `Creature.YouCtrl`, `Creature.YouCtrl+faceDown`, `Incubator.token+YouCtrl`

## `Shuffle`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `OwnMain2`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `MassX`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`, `GT0`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `R Sac<1/CARDNAME>`, `T Sac<1/CARDNAME>`, `R T`, `U T Sac<1/CARDNAME>`, `2 T`, `3 U U`, `5 T`, `5`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ParentTarget`, `ParentTargetedController`, `Player.IsRemembered`, `Remembered`, `RememberedController`, `RememberedOwner`, `Targeted`, `TargetedController`, `TriggeredTarget`, `You`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Permanent.Red+YouCtrl`
- `Optional$`: TODO: Describe this parameter.
  Observed values: `True`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChoose`, `DBCleanRemembered`, `DBCleanup`, `DBDigUntil`, `DBEffect`, `DBExile`, `DBMassCleanup`, `DBMill`, `DBReveal`, `DelTrigSlowtrip`, `RevealCard`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `SkipPhase`

TODO: Write documentation.

**Parameters:**
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `W`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`, `TargetedPlayer`, `TriggeredCardController`, `TriggeredPlayer`, `TriggeredTarget`, `You`
- `Duration$`: TODO: Describe this parameter.
  Observed values: `EndOfTurn`, `NextThisTurn`, `UntilTheEndOfTargetedNextTurn`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `Phase$`: TODO: Describe this parameter.
  Observed values: `BeginCombat`, `Main`
- `SpellDescription$`: TODO: Describe this parameter.
- `Start$`: TODO: Describe this parameter.
  Observed values: `FromNext`
- `Step$`: TODO: Describe this parameter.
  Observed values: `Draw`, `Untap`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `TrigDelay`, `TrigTap`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `SkipTurn`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `You`
- `NumTurns$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `X`

## `StoreSVar`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `CheckHand`, `GameMod`, `Loyalty`, `MilledCard`, `MilledCreature`, `TargetedLibrary`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `Targeted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`, `Card.!IsImprinted+SharesCMCWith Imprinted`, `Card.Creature`, `Card.Creature,Card.Planeswalker`, `Card.Planeswalker`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `GE1`, `GTExiledCMC`, `LTLimit`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `PayLife<X>`, `Mandatory PayLife<X>`
- `Expression$`: TODO: Describe this parameter.
  Observed values: `-1`, `0`, `1`, `2`, `3`, `AccumulatedMilled/Plus.1`, `Aid/Plus.1`, `CardCounters.LOYALTY`, `CardManaCost`, `CardToughness`, `Delirium.1.0`, `Doodles`, `Doodles/Plus.1`, `FlipsDone/Plus.1`, `Hits/Plus.1`, `JoinForcesAmount/Plus.Y`, `Left/Minus.1`, `Left/Plus.2`, `LifeAllButOne`, `Loss/Plus.1`, `Losses/Plus.1`, `M/Plus.1`, `NumLife/Times.2`, `NumPlayerGiveup/Plus.1`, `RepeatCheck/Plus.1`, `Result`, `Result/Minus.Noted`, `SetTrap/Plus.1`, `TargetedPlayer$LifeTotal`, `TimesToFlip`, `TreasureNum/Plus.1`, `Win/Plus.1`, `Wins/Plus.1`, `X`, `X/Plus.1`, `Y`, `Y/Plus.1`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AniBuzz`, `DBChoose`, `DBCleanup`, `DBClear`, `DBDamage`, `DBDmg`, `DBEffect`, `DBEmptyLibrary`, `DBExile`, `DBGiveUp`, `DBLoseLife`, `DBMilledCreature`, `DBRepeat`, `DBRepeatChoice`, `DBResetEach`, `DBResetRem`, `DBSacrifice`, `DBStore`, `NotifyRock`, `OppChoice`, `RepeatClash`, `RepeatPlay`, `ResetLoss`, `ResetSVars2`, `ResetSVars3`, `ResetWins`, `ScoreLoss`, `SetFlipsDone`, `StoreCMC`, `StoreTgtP`, `StoreTgtPW`
- `SVar$`: TODO: Describe this parameter.
  Observed values: `AccumulatedMilled`, `Aid`, `CarpetX`, `CheckNotPaid`, `CheckRepeat`, `CurrPower`, `Doodles`, `EachPlayer`, `ElkinSVar`, `ExiledCMC`, `FlipsDone`, `Hits`, `JoinForcesAmount`, `LandsPlayedFromExile`, `LandsPlayedFromNotHand`, `Left`, `LifePaid`, `LifePaidOnETB`, `LifePaidOnNewGame`, `Limit`, `Loss`, `Losses`, `M`, `ModsThisTurn`, `Noted`, `NotedLife`, `NotedPower`, `NumLife`, `NumPlayerGiveup`, `OppChose`, `PaidAmount`, `RepeatCheck`, `RhysticPaid`, `SackedCMC`, `Safe`, `SetTrap`, `ShieldAmount`, `TaintedCheck`, `TreasureNum`, `VarFSLif`, `VarFSVig`, `VarVigLif`, `Win`, `Wins`, `X`, `XDelirium`, `Y`, `YouChose`
- `Type$`: TODO: Describe this parameter.
  Observed values: `AdditiveForEach`, `Calculate`, `Count`, `CountSVar`, `Number`, `Targeted`, `Triggered`
- `UnlessAI$`: TODO: Describe this parameter.
  Observed values: `Never`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `PayLife<1>`, `PayLife<X>`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `EnchantedController`, `Player.IsRemembered`, `Remembered`, `TargetedOrController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Any`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `Black`, `Black,Red`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `Limit`

## `Subgame`

TODO: Write documentation.

**Parameters:**
- `RememberPlayers$`: TODO: Describe this parameter.
  Observed values: `NotWin`, `Win`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StartingLife$`: TODO: Describe this parameter.
  Observed values: `1`, `5`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBEffect`, `DBRepeatEachPlayer`

## `Surveil`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Once`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `X`, `Z`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `OptionalCost`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Resolved`, `X`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `GE1`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `RememberedLKI`, `Targeted`
- `ConditionOptionalPaid$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.cmcLE3`, `Desert.Other`, `Desert.YouCtrl`, `Rat.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 U`, `2 T`, `Sac<1/CARDNAME>`, `AddCounter<1/LOYALTY>`, `T Blight<1>`, `PayLife<2>`, `2 U`, `2 Sac<1/CARDNAME>`, `T`, `2 B T Sac<1/CARDNAME/this artifact>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE5_UNLOCK`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberKept$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCastFromYard`, `DBChangeZone`, `DBChooseCard`, `DBCleanup`, `DBCopy`, `DBCounter`, `DBDiscard`, `DBDraw`, `DBExile`, `DBGainLife`, `DBInvestigate`, `DBPrepare`, `DBRemoveCounter`, `DBReturn`, `DBTransform`, `DBUntap`, `DBWin`, `TrigImmediate`

## `SwitchBlock`

TODO: Write documentation.

**Parameters:**
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `Declare Blockers`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `T`
- `DefinedAttacker$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `Valid Creature.blockedByValidThisTurn Targeted`
- `DefinedBlocker$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `Valid Creature.blockingTargeted`
- `RemoveFromCombat$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `2`
- `TargetsWithSameController$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking+blocked`, `Creature.blocking+OppCtrl`

## `TakeInitiative`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `2 T Sac<1/CARDNAME>`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBGainLife`, `DBTreasure`

## `Tap`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Metalcraft`, `Threshold`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`, `Hand`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Arena`, `Curse`, `GoblinPolkaBand`
- `AIPhyrexianPayment$`: TODO: Describe this parameter.
  Observed values: `Never`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Creature.OppCtrl+equipped`
- `AlwaysRemember$`: TODO: Describe this parameter.
  Observed values: `True`
- `Announce$`: TODO: Describe this parameter.
  Observed values: `TgtNum`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `any number of creatures to target`
- `AnyNumber$`: TODO: Describe this parameter.
  Observed values: `True`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CardChoices$`: TODO: Describe this parameter.
  Observed values: `Creature.untapped+White+RememberedPlayerCtrl`, `Creature.YouCtrl+untapped`, `Gate.YouCtrl+untapped`, `Human.YouCtrl+untapped`, `Vampire.YouCtrl+untapped`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ChoiceAmount$`: TODO: Describe this parameter.
  Observed values: `Count$Valid Creature.untapped+White+RememberedPlayerCtrl`, `Count$Valid Creature.YouCtrl+untapped`, `Count$Valid Gate.YouCtrl+untapped`, `Count$Valid Human.YouCtrl+untapped`, `Count$Valid Vampire.YouCtrl+untapped`
- `ChoicePrompt$`: TODO: Describe this parameter.
  Observed values: `Tap any number of untapped creatures you control`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `DragonPresence`, `ETBCheckSVar2`, `M12Complete`, `SoldierPresence`, `TappedCreaturePower`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE1`, `GE2`, `GT1`, `GT2`, `LE1`, `LT2`, `LT3`, `LT8`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Remembered`, `Self`, `Targeted`
- `ConditionPhases$`: TODO: Describe this parameter.
  Observed values: `Main1,Main2`
- `ConditionPlayerContains$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionPlayerDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `False`, `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Card.wasCast`, `Card.YouCtrl`, `Creature.Legendary+YouCtrl`, `Creature.Legendary+YouCtrl+Green`, `Creature.nonArtifact`, `Creature.untapped`, `Equipment`, `Forest.YouCtrl`, `Forest.YouCtrl+Other`, `Forest.YouCtrl,Island.YouCtrl`, `Forest.YouCtrl,Plains.YouCtrl`, `Island.YouCtrl`, `Island.YouCtrl+Other`, `Island.YouCtrl,Mountain.YouCtrl`, `Island.YouCtrl,Swamp.YouCtrl`, `Land.Basic+YouCtrl`, `Land.OppCtrl`, `Land.YouCtrl`, `Mount.YouCtrl,Vehicle.YouCtrl`, `Mountain.YouCtrl`, `Mountain.YouCtrl+Other`, `Mountain.YouCtrl,Forest.YouCtrl`, `Mountain.YouCtrl,Plains.YouCtrl`, `Permanent.White+YouCtrl,Permanent.Blue+YouCtrl,Permanent.Black+YouCtrl`, `Plains.YouCtrl`, `Plains.YouCtrl+Other`, `Plains.YouCtrl,Island.YouCtrl`, `Plains.YouCtrl,Swamp.YouCtrl`, `Swamp`, `Swamp.YouCtrl`, `Swamp.YouCtrl+Other`, `Swamp.YouCtrl,Forest.YouCtrl`, `Swamp.YouCtrl,Mountain.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `GE8`, `GT13`, `GT3`, `LE0`, `LE2`, `LT1`, `LT2`, `LT3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `tapXType<1/Octopus>`, `B T`, `2 U`, `2 W T`, `W T`, `R`, `4 T`, `tapXType<2/Wizard>`, `3 T`, `1 T`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Sacrifice an Eldrazi Scion:`, `{2}, {T}:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRemembered`, `DelayTriggerRememberedLKI`, `Enchanted`, `Imprinted`, `Remembered`, `ReplacedCard`, `Self`, `Targeted`, `Targeted.YouDontCtrl`, `TriggeredAttackerLKICopy`, `TriggeredBlockerLKICopy`, `TriggeredObjectLKICopy`, `TriggeredTargetLKICopy`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+attacking`, `Creature.YouCtrl+withFlying`, `Land.YouCtrl`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Body-print —`, `Channel —`, `Cohort —`, `Corrupted —`, `Hunt for Heresy —`, `Metalcraft —`, `Renew —`, `Stunning Strike —`, `Threshold —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE8`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberTapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AbandonSelf`, `ChoosePlainsToSave`, `DBAddCounter`, `DBAnimate`, `DBBounce`, `DBChangeZone`, `DBChooseOpponent`, `DBCleanup`, `DBConstrict`, `DBControl`, `DBCounter`, `DBDamage`, `DBDealDamage`, `DBDestroyAll`, `DBDmg`, `DBDraw`, `DBEachDamage`, `DBEffect`, `DBElderSpawnDamage`, `DBExile`, `DBExileSelf`, `DBFight`, `DBGainLife`, `DBGoad`, `DBImmediateTrig`, `DBImmediateTrigger`, `DBInvestigate`, `DBJaddiLifestriderGainLife`, `DBLearn`, `DBLoseLife`, `DBMana`, `DBMill`, `DBMonarch`, `DBNekoTe`, `DBNoUntap`, `DBProliferate`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBRadiation`, `DBRemoveAttacker`, `DBRemoveBlocker`, `DBRemoveCounter`, `DBScry`, `DBSeek`, `DBSetAttacking`, `DBStayTapped`, `DBStun`, `DBTap`, `DBToken`, `DBTransform`, `DBTransform1`, `DBTransform2`, `DBUnattach`, `DBUntap`, `DelTrigSlowtrip`, `DovinPump`, `Drain`, `GoblinHangover`, `RemCombat`, `RemoveSelf`, `RonsoClone`, `SpiritDmg`, `TamiyoPump`, `TrigDraw`, `TrigPump`, `TrigTapW2`, `VampiricFeed`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE3`
- `Tapper$`: TODO: Describe this parameter.
  Observed values: `RememberedPlayer`, `TriggeredPlayer`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`
- `TargetingPlayerControls$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `8`, `OneEach`, `TgtNum`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `TgtNum`, `X`
- `TargetsAtRandom$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetsWithDefinedController$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackedTarget`, `TriggeredDefendingPlayer`, `TriggeredTarget`
- `TgtPrompt$`: TODO: Describe this parameter.
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `1`, `3`, `B B B`, `PayEnergy<1>`, `PayLife<1>`, `PayLife<2>`, `PayLife<3>`, `Reveal<1/Elemental>`, `Reveal<1/Elf>`, `Reveal<1/Faerie>`, `Reveal<1/Forest;Island/Forest or Island>`, `Reveal<1/Forest;Plains/Forest or Plains>`, `Reveal<1/Giant>`, `Reveal<1/Goblin>`, `Reveal<1/Island;Mountain/Island or Mountain>`, `Reveal<1/Island;Swamp/Island or Swamp>`, `Reveal<1/Kithkin>`, `Reveal<1/Merfolk>`, `Reveal<1/Mountain;Forest/Mountain or Forest>`, `Reveal<1/Mountain;Plains/Mountain or Plains>`, `Reveal<1/Plains;Island/Plains or Island>`, `Reveal<1/Plains;Swamp/Plains or Swamp>`, `Reveal<1/Swamp;Forest/Swamp or Forest>`, `Reveal<1/Swamp;Mountain/Swamp or Mountain>`, `Reveal<1/Treefolk>`, `Sac<1/Card.token;Artifact;Enchantment/artifact, enchantment, or token>`, `Sac<1/Creature.Other/another creature>`, `Sac<1/Creature>`, `tapXType<1/Creature>`, `X`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player.Opponent`, `TargetedController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`, `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Land`, `Artifact.nonCreature`, `Artifact.OppCtrl,Creature.OppCtrl`, `Artifact.YouDontCtrl`, `Card.nonLand+OppCtrl`, `Creature`, `Creature,Artifact`, `Creature,Planeswalker`, `Creature,Vehicle`, `Creature.!token+OppCtrl`, `Creature.ActivePlayerCtrl`, `Creature.blockingSource`, `Creature.cmcGE2`, `Creature.cmcLE3`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.DefenderCtrl`, `Creature.DefendingPlayerCtrl`, `Creature.Green`, `Creature.nonEnchantment`, `Creature.nonHuman`, `Creature.nonMount`, `Creature.OppCtrl`, `Creature.Other`, `Creature.powerGE4`, `Creature.powerLE2`, `Creature.powerLE3`, `Creature.powerLE8`, `Creature.powerLEX`, `Creature.Red+OppCtrl,Creature.Green+OppCtrl`, `Creature.toughnessLE2`, `Creature.untapped`, `Creature.untapped+YouCtrl`, `Creature.withFlying`, `Creature.withFlying+blockedBySource`, `Creature.withoutFlying`, `Creature.withoutFlying+attackingYou`, `Creature.withoutHorsemanship`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Land`, `Land.OppCtrl`, `Permanent`, `Permanent.ControlledBy ParentTarget`, `Permanent.nonLand`, `Permanent.nonland`, `Permanent.nonLand+OppCtrl`, `Permanent.OppCtrl`, `Permanent.OppCtrl+nonLand`, `Permanent.Other+nonLand`, `Permanent.YouDontCtrl`, `Spirit`, `Wall`
- `XColor$`: TODO: Describe this parameter.
  Observed values: `R`

## `TapAll`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `AtLeast3`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `FatefulHour`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `LE5`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `U U U`, `0`, `8`, `SubCounter<9/LOYALTY>`, `2 T`, `5`, `SubCounter<10/LOYALTY>`, `3 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedController`, `TriggeredActivator`, `TriggeredCardController`, `TriggeredPlayer`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBAddTurn`, `DBAnimate`, `DBChooseNumber`, `DBChooseP`, `DBCleanup`, `DBDamage`, `DBDmg`, `DBEffect`, `DBExileSelf`, `DBGoad`, `DBNoUntap`, `DBPump`, `DBPumpAll`, `DBStun`, `DBUnTap`, `DBUntapAll`, `DrainMana`, `FeintPump`, `ManaLose`, `NoUntap`, `PathwayCleanup`, `SpellLimitations`, `TrigPump2`, `WildHuntDamage`
- `TapperController$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `R R R`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.StrictlyOther`, `Artifact.untapped+!IsRemembered,Creature.untapped+!IsRemembered,Land.untapped+!IsRemembered`, `Card.Self,Creature.YouCtrl+namedKobolds of Kher Keep`, `Creature`, `Creature.attacking`, `Creature.blockedByRemembered`, `Creature.blockedBySource,Creature.blockingSource`, `Creature.blockedValidThisTurn Card.StrictlySelf`, `Creature.blocking`, `Creature.blockingRemembered`, `Creature.Blue`, `Creature.ChosenCard`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.IsRemembered`, `Creature.IsRemembered+Colorless`, `Creature.IsRemembered+DamagedBy`, `Creature.Legendary`, `Creature.nonBlue`, `Creature.nonChosenCard+RememberedPlayerCtrl`, `Creature.nonSpirit`, `Creature.nonWhite`, `Creature.OppCtrl`, `Creature.OppCtrl+toughnessLE2`, `Creature.Red`, `Creature.StrictlyOther`, `Creature.toughnessLE2`, `Creature.untapped+!attackedThisTurn+ActivePlayerCtrl`, `Creature.untapped+!IsRemembered`, `Creature.withFlying+OppCtrl`, `Creature.withoutFlying`, `Creature.Wolf+YouCtrl+untapped`, `Creature.YouCtrl+StrictlyOther`, `Creature.YouDontCtrl`, `Island`, `Island.ActivePlayerCtrl+untapped`, `Land`, `Land.ControlledBy TriggeredDefendingPlayer`, `Land.ControlledBy TriggeredTarget`, `Land.hasManaAbility`, `Land.IsRemembered`, `Land.OppCtrl`, `Land.YouCtrl`, `Permanent`, `Permanent.nonLand`, `Spirit`, `TriggeredCard.canProduceSameManaTypeWith+Land`, `TriggeredCard.sharesControllerWith+Land`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature.attacking`, `Opponent`, `Player`

## `TapOrUntap`

TODO: Write documentation.

**Parameters:**
- `Cost$`: TODO: Describe this parameter.
  Observed values: `1 U T`, `3 G T`, `T`, `T PayEnergy<2>`, `Discard<1/Card>`, `U T`, `2 T`, `1 T`, `3`, `Sac<1/CARDNAME>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Equipped`, `Targeted`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.EquippedBy`, `Permanent.Snow+YouCtrl`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCopy`, `DBDraw`, `DBTapOrUntap`, `DelTrigSlowtrip`
- `Tapper$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackingPlayer`
- `TargetingPlayer$`: TODO: Describe this parameter.
  Observed values: `TriggeredAttackingPlayer`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact,Creature`, `Artifact,Creature,Land`, `Artifact.OppCtrl`, `Creature`, `Creature.Other`, `Permanent`, `Permanent.nonLand`, `Permanent.Other`

## `TaporUntapAll`

TODO: Write documentation.

**Parameters:**
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `TriggeredCard.sharesCreatureTypeWith`
- `ValidMessage$`: TODO: Describe this parameter.
  Observed values: `creatures that share a creature type with the triggered creature`

## `TapOrUntapAll`

TODO: Write documentation.

**Parameters:**
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Card.ChosenType`
- `ValidMessage$`: TODO: Describe this parameter.
  Observed values: `permanents of the chosen type target player controls`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Player`

## `TimeTravel`

TODO: Write documentation.

**Parameters:**
- `Amount$`: TODO: Describe this parameter.
  Observed values: `2`, `3`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T`, `7`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Timey-Wimey —`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBDraw`

## `Token`

TODO: Write documentation.

**Parameters:**
- `ActivationAfterBlockers$`: TODO: Describe this parameter.
  Observed values: `True`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Declare Blockers->EndCombat`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Command`, `Graveyard`, `Hand`
- `Activator$`: TODO: Describe this parameter.
  Observed values: `Player`
- `AddTriggersFrom$`: TODO: Describe this parameter.
  Observed values: `ExiledCards`
- `AICheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AlwaysOnDiscard`, `Curse`, `Never`, `OnlyOnAlliedAttack`, `RandomPT`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `W`
- `AISVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE4`
- `AITgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`
- `AnnounceTitle$`: TODO: Describe this parameter.
  Observed values: `number of creatures to sacrifice`
- `AtEOT$`: TODO: Describe this parameter.
  Observed values: `Destroy`, `Exile`, `ExileCombat`, `Sacrifice`, `SacrificeCombat`, `YourExile`, `YourSacrifice`, `YourSacrificeUpkeep`
- `AtEOTCondition$`: TODO: Describe this parameter.
  Observed values: `Y`
- `AtEOTDesc$`: TODO: Describe this parameter.
  Observed values: `At the beginning of the next end step, exile those tokens unless you have the city's blessing.`
- `AttachedTo$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Remembered`, `Self`, `Targeted`, `ThisTargetedCard`, `TriggeredCardLKICopy`, `TriggeredDefendingPlayer`, `TriggeredNewCardLKICopy`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `ArtifactSacrificed`, `Count$ThisTurnEntered_Battlefield_Card.Self+YouCtrl,Artifact.YouCtrl+Other`, `CountCountersRemoved`, `FormidableTest`, `Morbid`, `X`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Delirium`, `Foretold`, `Kicked`, `Surge`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `AllThree`, `CounterX`, `CreaturesThem`, `CreatureYouControl`, `Excess`, `Morbid`, `NumLands`, `RaidTest`, `Resolved`, `Result`, `TriggeredSpellAbility$CardManaCostLKI`, `X`, `XCreatures`, `XLands`, `Z`
- `ConditionChosenColor$`: TODO: Describe this parameter.
  Observed values: `black`, `blue`, `green`, `red`, `white`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `GE1`, `GE10`, `GE3`, `GT0`, `LT10`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `RememberedLKI`, `Sacrificed`, `Self`, `Targeted`, `TriggeredCard`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If CARDNAME was kicked, create a 1/1 red Goblin creature token.`, `If you control an Equipment,`
- `ConditionLifeAmount$`: TODO: Describe this parameter.
  Observed values: `GTX`
- `ConditionLifeTotal$`: TODO: Describe this parameter.
  Observed values: `You`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `G`, `W`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.YouCtrl`, `Card`, `Card.AllColors`, `Card.attacking`, `Card.Blue,Card.Black`, `Card.cmcLE1`, `Card.cmcLE2`, `Card.cmcLE4`, `Card.cmcLT10`, `Card.counters_EQ0_CHARGE`, `Card.Creature`, `Card.ExiledWithSource`, `Card.Goblin`, `Card.inRealZoneGraveyard`, `Card.inZoneBattlefield`, `Card.inZoneHand`, `Card.Legendary`, `Card.nonCreature+nonLand`, `Card.nonLand`, `Card.Outlaw`, `Card.Self`, `Card.SharesColorWith TriggeredProduced`, `Card.tapped`, `Card.wasCastFromYourHand`, `Card.YouCtrl`, `Creature`, `Creature.counters_GE1_P1P1`, `Creature.equipped+YouCtrl`, `Creature.powerGE4+YouCtrl`, `Creature.powerGE7`, `Creature.wasDealtDamageThisTurn`, `Creature.YouCtrl+namedMowu`, `Creature.YouCtrl+namedThe Hollow Sentinel`, `Creature.YouCtrl+powerGE4`, `Desert.YouCtrl`, `Elf`, `Equipment.YouCtrl`, `Food`, `Land`, `Land.YouCtrl`, `Merfolk.YouCtrl`, `You`
- `ConditionPresent2$`: TODO: Describe this parameter.
  Observed values: `Enchantment.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ1`, `EQ2`, `EQ3`, `GE1`, `GE10`, `GE3`, `GE5`, `GE7`, `GE8`, `GT0`, `GTCreaturesYou`, `GTMostLands`, `GTYCreatures`, `GTYLands`, `LE2`, `LEX`, `LTCreatureOppControl`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `6 T`, `1 W B G T Sac<1/CARDNAME>`, `2 U`, `PayEnergy<2>`, `Sac<1/CARDNAME>`, `SubCounter<8/LOYALTY>`, `SubCounter<6/LOYALTY>`, `AddCounter<0/LOYALTY>`, `AddCounter<1/LOYALTY>`, `SubCounter<2/LOYALTY>`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Grandeur — Discard another card named Baru, Fist of Krosa:`, `Morbid — {T}, Tap two untapped creatures you control:`, `{2}{B}{B}, {T}, Sacrifice all lands you control:`, `{3}{G}{W}, {T}, Tap two untapped creatures you control, Sacrifice CARDNAME:`, `{5}, Exile CARDNAME and four other artifact creatures and/or Vehicles you control:`, `{6}, {T}, Remove all charge counters from CARDNAME:`, `{B}, Exile two creature cards from your graveyard:`, `{T}, Exile CARDNAME and artifacts you control named Eye of Vecna and Hand of Vecna:`, `{T}, Sacrifice CARDNAME and any number of other non-Eldrazi creatures:`, `{W}{U}, {T}, Exile a creature card from your graveyard:`
- `Destination$`: TODO: Describe this parameter.
  Observed values: `Exile`
- `EffectZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `Exhaust$`: TODO: Describe this parameter.
  Observed values: `True`
- `Forecast$`: TODO: Describe this parameter.
  Observed values: `True`
- `ForgetOtherRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `GiftDescription$`: TODO: Describe this parameter.
  Observed values: `a Food`, `a tapped Fish`, `a Treasure`, `an Octopus`
- `ImprintTokens$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_GE4_QUEST`, `Creature.attackingYou`, `Creature.YouCtrl`, `Creature.YouCtrl+attacking+modified`, `Creature.YouCtrl+FoughtThisTurn`, `Enchantment.YouCtrl`, `Sliver.YouCtrl`
- `LockInText$`: TODO: Describe this parameter.
  Observed values: `True`
- `LockTokenScript$`: TODO: Describe this parameter.
  Observed values: `True`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`, `3`
- `Pawprint$`: TODO: Describe this parameter.
  Observed values: `1`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Channel —`, `Chapter Master —`, `Cohort —`, `Formidable —`, `Max speed —`, `Ultima Founding —`
- `PresentCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `LTX`
- `PumpDuration$`: TODO: Describe this parameter.
  Observed values: `EndOfTurn`, `EOT`
- `PumpKeywords$`: TODO: Describe this parameter.
  Observed values: `Haste`, `Lifelink & Haste`, `Menace & Haste`
- `ReduceCost$`: TODO: Describe this parameter.
  Observed values: `X`
- `RememberOriginalTokens$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberSource$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTokens$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secondary$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `AdditionalPump`, `Blood`, `BlotDestroy`, `ChoseBlack`, `ChoseBlue`, `ChoseGreen`, `ChoseRed`, `CleanupFinal`, `Clear`, `CoupDestroy`, `CreateCopy`, `DBAbandon`, `DBAddTurn`, `DBAmass`, `DBAngels`, `DBAnimate`, `DBAnimateAll`, `DBAttach`, `DBAttachEach`, `DBBounce`, `DBCentaurToken`, `DBChange`, `DBChangeZone`, `DBChoose`, `DBChooseToken`, `DBChooseType`, `DBChooseX`, `DBClaim`, `DBClash`, `DBCleanup`, `DBClearRemember`, `DBCleric`, `DBClone`, `DBCopy`, `DBCount`, `DBCounter`, `DBCounters`, `DBCurseNonSpiders`, `DBDamage`, `DBDamageYou`, `DBDealDamage`, `DBDelayedTrigger`, `DBDelayTrig`, `DBDelTrig`, `DBDestroy`, `DBDig`, `DBDiscount`, `DBDrain`, `DBDraw`, `DBEarthbend`, `DBEff`, `DBEffect`, `DBEnergy`, `DBExile`, `DBFight`, `DBFirstStrike`, `DBFlip`, `DBGainLife`, `DBGainLifePlains`, `DBGoad`, `DBImmediateTrig`, `DBImmediateTrig1`, `DBImmediateTrigger`, `DBIntensify`, `DBInvestigate`, `DBLearn`, `DBLoot`, `DBLoseLife`, `DBLoseLife1`, `DBLoseLife14M`, `DBLoseLife3`, `DBLosePerpAbility`, `DBMakeCard`, `DBManifest`, `DBMassTokens`, `DBMill`, `DBMove`, `DBNoUntap`, `DBPass`, `DBPhases`, `DBPlay`, `DBPrepare`, `DBPrevent`, `DBPump`, `DBPumpAll`, `DBPutCounter`, `DBPutCounterAll`, `DBPutCounters`, `DBReach`, `DBRepeat`, `DBReset`, `DBReturn`, `DBRhinoToken`, `DBRogue`, `DBRoll`, `DBSac`, `DBSac1`, `DBSack`, `DBSacrifice`, `DBScry`, `DBSetLife`, `DBShuffle`, `DBSpace`, `DBStoreSVar`, `DBStoreSVarT`, `DBSurveil`, `DBSuspect`, `DBTakeTurn`, `DBToken`, `DBToken2`, `DBTokenBis`, `DBTokenOpp`, `DBTokenTrice`, `DBTransform`, `DBTreasure`, `DBTrigger`, `DBUnimprint`, `DBUntap`, `DBVehicle`, `DBVenture`, `DBWinGame`, `DBWizard`, `DBWrath`, `DelTrig`, `ExileEffect`, `Insect`, `KickerPump`, `Life`, `MatureEvil`, `MoltenFlip`, `OppScry`, `RememberPlayer`, `RollDie`, `TrigDealDamage`, `TrigExile`, `TrigLoseLife`, `TrigPump`, `TrigTempt`, `UnscytheDBCleanup`, `UPaid`, `VillainousChoice`
- `SVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE2`, `GE8`, `GEY`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `MaxTargets`, `MaxTgt`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `TokenAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `10`, `13`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `Amt`, `BasriX`, `Count$CrewSize`, `Count$ThisTurnEntered_Battlefield_Mount.YouCtrl,Vehicle.YouCtrl`, `Count$Valid Creature.ControlledBy TargetedPlayer$CardCounters.ALL`, `Count$ValidGraveyard Creature.YouCtrl`, `CountForest`, `Difference`, `DifferentResults`, `ElementalMasteryCount`, `Excess`, `ForestsYouControl`, `HalfXUp`, `JoinForcesAmount`, `L`, `Lands`, `LifePaidAmount`, `MonstrosityX`, `N`, `OddResults`, `OneEach`, `OsX`, `PlayerCountOpponents$HasPropertycontrolsArtifact/Plus.1`, `PlayerCountOpponents$HasPropertycontrolsCreature.powerGE4`, `Remembered$Amount`, `Remembered$CardManaCost/NMinus.10`, `Result`, `SekkiX`, `SVar$VoteNum/Times.2`, `SVar$X/Twice`, `TokenX`, `TreasureNum`, `TriggerCount$Amount`, `VoteNum`, `WasKicked`, `Wins`, `X`, `X4U`, `Y`, `Z`
- `TokenAttacking$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedPlayer`, `RememberedPlayer & Valid Planeswalker.ControlledBy Remembered`, `TriggeredAttackedTarget`, `TriggeredDefender`, `True`
- `TokenBlocking$`: TODO: Describe this parameter.
  Observed values: `Targeted`, `TriggeredAttacker`
- `TokenColors$`: TODO: Describe this parameter.
  Observed values: `ChosenColor`
- `TokenController$`: TODO: Describe this parameter.
  Observed values: `You`
- `TokenOwner$`: TODO: Describe this parameter.
  Observed values: `.Chosen,You`, `ChosenPlayer`, `DelayTriggerRememberedController`, `EnchantedPlayer`, `ImprintedController`, `NonTargeted`, `Opponent`, `ParentTarget`, `Player`, `Player.controlsCreature_EQX`, `Player.controlsEnchantment,controlsArtifact`, `Player.IsRemembered`, `Player.Opponent`, `Player.Other`, `Promised`, `Remembered`, `RememberedController`, `RememberedOwner`, `Targeted`, `TargetedAndYou`, `TargetedController`, `TargetedOrController`, `TargetedPlayer`, `ThisTargetedPlayer`, `TriggeredActivator`, `TriggeredAttackerController`, `TriggeredAttackingPlayer`, `TriggeredAttackingPlayer.Opponent+controlsCreature.attacking Player.EnchantedBy`, `TriggeredCardController`, `TriggeredCardOwner`, `TriggeredOpponentVotedSame`, `TriggeredPlayer`, `TriggeredSourceController`, `TriggeredTarget`, `TriggeredTargetController`, `You`
- `TokenPower$`: TODO: Describe this parameter.
  Observed values: `dX`, `L`, `LifePaidOnETB`, `MonstrosityX`, `X`, `XLKI`, `Y`, `Z`
- `TokenRemembered$`: TODO: Describe this parameter.
  Observed values: `ExiledCards`
- `TokenScript$`: TODO: Describe this parameter.
  Observed values: `ajanis_pridemate`, `all_1_1_a_stained_glass`, `all_1_1_human_wizard`, `all_2_2_citizen`, `all_2_2_elemental`, `all_3_3_kavu_trample`, `angelo`, `ashaya_the_awoken_world`, `avacyn`, `b_0_0_phyrexian_germ`, `b_0_1_cleric`, `b_0_1_insect`, `b_0_1_serf`, `b_0_1_thrull`, `b_0_1_wizard_snipe`, `b_1_1_assassin_deathtouch_haste`, `b_1_1_assassin_deathtouch_pwdestroy`, `b_1_1_assassin_lose_con`, `b_1_1_assassin_menace`, `b_1_1_bat_flying`, `b_1_1_bird_flying_noblock`, `b_1_1_cat`, `b_1_1_faerie_rogue_flying`, `b_1_1_fungus_noblock`, `b_1_1_goblin_rogue`, `b_1_1_harpy_flying`, `b_1_1_horror`, `b_1_1_insect`, `b_1_1_insect_flying`, `b_1_1_insect_warrior_flying`, `b_1_1_minion`, `b_1_1_nightmare_exile_counter`, `b_1_1_ninja`, `b_1_1_rat`, `b_1_1_rat_deathtouch`, `b_1_1_rat_lifelink`, `b_1_1_rat_noblock`, `b_1_1_rat_relentless`, `b_1_1_rat_rogue`, `b_1_1_skeleton`, `b_1_1_skeleton_opp_life`, `b_1_1_skeleton_regenerate`, `b_1_1_slug`, `b_1_1_snail`, `b_1_1_snake_deathtouch`, `b_1_1_thrull`, `b_1_1_vampire`, `b_1_1_vampire_knight_lifelink`, `b_1_1_vampire_lifelink`, `b_1_1_vampire_rogue_lifelink`, `b_1_1_wolf_deathtouch`, `b_1_2_a_phyrexian_wurm_deathtouch,b_2_1_a_phyrexian_wurm_lifelink`, `b_1_2_bat_flying_nosferatu`, `b_2_1_bat_flying`, `b_2_1_cat`, `b_2_1_skeleton`, `b_2_1_spider_menace_reach`, `b_2_1_warrior`, `b_2_2_a_alien_angel_firststrike_vigilance`, `b_2_2_a_necron_warrior`, `b_2_2_astartes_warrior_menace`, `b_2_2_bird_flying`, `b_2_2_e_horror`, `b_2_2_e_zombie`, `b_2_2_horror`, `b_2_2_knight_flanking_pro_white_haste`, `b_2_2_phyrexian`, `b_2_2_phyrexian_zombie`, `b_2_2_pirate_menace`, `b_2_2_rogue`, `b_2_2_rogue_hexproof`, `b_2_2_rogue_menace`, `b_2_2_skeleton_pirate`, `b_2_2_vampire_flying`, `b_2_2_zombie`, `b_2_2_zombie_berserker`, `b_2_2_zombie_decayed`, `b_2_2_zombie_druid`, `b_2_2_zombie_employee`, `b_2_2_zombie_knight_menace`, `b_2_2_zombie_mutant`, `b_2_3_vampire_flying_lifelink`, `b_2_4_spider_reach`, `b_3_3_a_dalek_menace`, `b_3_3_angel_flying`, `b_3_3_beast_deathtouch`, `b_3_3_demon`, `b_3_3_horror`, `b_3_3_kavu`, `b_3_3_wraith_menace`, `b_4_1_skeleton_menace`, `b_4_3_ogre_warrior`, `b_4_4_horror`, `b_4_4_zombie_warrior_vigilance`, `b_5_5_demon_flying`, `b_5_5_zombie_giant`, `b_6_6_demon_flying`, `b_6_6_demon_flying_trample_aristocrat`, `b_6_6_wurm_trample`, `b_aura_curse_life`, `b_x_x_aetherborn`, `b_x_x_demon_flying`, `b_x_x_horror`, `b_x_x_nightmare_horror`, `b_x_x_phyrexian_minion`, `b_x_x_spirit`, `b_x_x_vampire`, `b_x_x_zombie`, `b_x_x_zombie_horror`, `ballistic_boulder`, `banana`, `bear_force_one`, `beau`, `bg_1_1_e_snake_deathtouch`, `bg_1_1_insect`, `bg_1_1_insect_flying`, `bg_1_1_pest_attack_lifegain`, `bg_1_1_pest_lifegain`, `bg_1_1_worm`, `bg_2_1_spider_menace_reach`, `bg_2_2_elf`, `bg_2_2_wolf_garruk`, `bg_x_x_hydra`, `bg_x_x_spirit_warrior`, `bling`, `blue_horror`, `boo`, `br_1_1_goblin`, `br_3_1_graveborn_haste`, `br_3_1_vampire_trample_lifelink_haste`, `br_3_6_avatar_haste_bolt`, `br_5_5_elemental`, `br_6_6_dragon_flying_menace_steal`, `br_7_7_demon`, `brg_3_3_cat_dragon_flying`, `butterfly`, `c_0_0_a_construct_total_artifacts`, `c_0_0_a_thopter_flying`, `c_0_1_a_egg`, `c_0_1_a_goblin_construct_noblock_ping`, `c_0_1_a_pest`, `c_0_1_a_prism`, `c_0_1_eldrazi_spawn_sac`, `c_0_2_a_wall_defender`, `c_0_3_wall_defender_reach`, `c_0_4_a_wall_defender`, `c_0_4_wall_defender`, `c_10_10_eldrazi`, `c_1_1_a_construct`, `c_1_1_a_construct_defender`, `c_1_1_a_drone_flying_blockflying`, `c_1_1_a_gnome`, `c_1_1_a_insect_flying`, `c_1_1_a_myr`, `c_1_1_a_pentavite_flying`, `c_1_1_a_phyrexian_mite_toxic_noblock`, `c_1_1_a_phyrexian_myr`, `c_1_1_a_robot`, `c_1_1_a_robot_flying`, `c_1_1_a_servo`, `c_1_1_a_snake_poison`, `c_1_1_a_soldier`, `c_1_1_a_tetravite_flying_noenchant`, `c_1_1_a_thopter_flying`, `c_1_1_a_triskelavite_flying_ammo`, `c_1_1_e_shrine`, `c_1_1_eldrazi_scion_sac`, `c_1_1_eldrazi_sliver_sac`, `c_1_1_hero`, `c_1_1_pilot_crewbuff`, `c_1_1_pilot_crewsaddlebuff`, `c_1_1_sand`, `c_1_1_shapeshifter_changeling`, `c_1_1_sliver`, `c_1_1_spirit`, `c_1_1_spirit_lifelink_haste`, `c_1_1_spirit_spiritshadow`, `c_2_2_a_assembly_worker`, `c_2_2_a_construct`, `c_2_2_a_drone_deathtouch_leavedrain`, `c_2_2_a_robot`, `c_2_2_a_spawn`, `c_2_2_pincher`, `c_2_2_scarecrow`, `c_2_2_shapeshifter_changeling`, `c_2_2_spirit`, `c_3_2_a_vehicle_crew_1`, `c_3_2_eldrazi_horror`, `c_3_2_shapeshifter_changeling`, `c_3_3_a_golem`, `c_3_3_a_golem_flying,c_3_3_a_golem_vigilance,c_3_3_a_golem_trample`, `c_3_3_a_phyrexian_golem`, `c_3_3_a_phyrexian_wurm_deathtouch,c_3_3_a_phyrexian_wurm_lifelink`, `c_3_3_a_robot`, `c_3_3_a_robot,c_a_treasure_sac`, `c_3_3_a_zombie`, `c_3_3_e_a_golem`, `c_3_4_a_gargoyle_flying`, `c_4_4_a_construct`, `c_4_4_a_golem`, `c_4_4_a_robot_noblock`, `c_4_4_a_scarecrow_vigilance`, `c_4_4_dragon_flying`, `c_4_4_eldrazi_angel_flying_vigilance`, `c_4_6_a_golem`, `c_5_5_a_djinn_flying`, `c_6_12_a_construct_trample`, `c_6_6_a_beast`, `c_7_7_eldrazi_annihilator`, `c_9_9_a_golem`, `c_a_blood_draw`, `c_a_clue_draw`, `c_a_clue_draw,c_a_food_sac,c_a_junk_sac_exileplay`, `c_a_clue_draw,c_a_food_sac,c_a_treasure_sac`, `c_a_food_sac`, `c_a_food_sac,b_2_2_human_rogue`, `c_a_food_sac,c_a_clue_draw`, `c_a_food_sac,w_1_1_human_doctor_reduce`, `c_a_food_sac,w_1_1_human_soldier`, `c_a_gold_sac`, `c_a_junk_sac_exileplay`, `c_a_lander_sac_search`, `c_a_map_sac_explore`, `c_a_mutagen_sac`, `c_a_powerstone`, `c_a_treasure_sac`, `c_a_treasure_sac,c_1_1_pilot_crewbuff`, `c_a_treasure_sac,u_2_2_bird_flying`, `c_a_treasure_sac,w_2_2_alien`, `c_a_vibranium`, `c_e_shard_draw`, `c_x_x_a_construct`, `c_x_x_a_golem`, `c_x_x_a_golem_haste`, `c_x_x_a_horror`, `c_x_x_a_phyrexian_horror`, `c_x_x_a_sculpture_total_sculptures`, `c_x_x_shapeshifter_changeling_deathtouch`, `carnivore`, `cherubael`, `cloud_sprite`, `colossal_dreadmaw`, `contract`, `cordyceps_infected`, `cragflame`, `darkstar`, `doombot`, `etherium_cell`, `everywhere`, `feather`, `festering_goblin`, `first_mate_ragavan`, `g_0_0_hydra`, `g_0_0_ooze_trample`, `g_0_1_dinosaur_egg`, `g_0_1_egg_defender`, `g_0_1_plant`, `g_0_1_sheep`, `g_0_2_plant_defender`, `g_1_1_ape`, `g_1_1_boar_food`, `g_1_1_cat`, `g_1_1_dog`, `g_1_1_elf_druid_g`, `g_1_1_elf_g`, `g_1_1_elf_warrior`, `g_1_1_forest_dryad`, `g_1_1_forest_dryad_squirrel`, `g_1_1_hippo`, `g_1_1_human_monk_g`, `g_1_1_insect`, `g_1_1_insect_flying_deathtouch`, `g_1_1_phyrexian_insect_infect`, `g_1_1_phyrexian_saproling`, `g_1_1_plant`, `g_1_1_saproling`, `g_1_1_snake`, `g_1_1_snake,g_2_2_wolf,g_3_3_elephant`, `g_1_1_snake_deathtouch`, `g_1_1_spike`, `g_1_1_splinter_flying_cum`, `g_1_1_squirrel`, `g_1_1_squirrel,u_0_3_crab`, `g_1_1_tyranid`, `g_1_1_wolf_sound_the_call`, `g_1_2_spider_reach`, `g_1_3_e_spider_reach`, `g_2_1_spider_reach`, `g_2_1_varmint`, `g_2_2_alien_salamander_islandwalk`, `g_2_2_bear`, `g_2_2_beast`, `g_2_2_bird_landfall`, `g_2_2_boar`, `g_2_2_cat`, `g_2_2_cat_warrior_forestwalk`, `g_2_2_elemental`, `g_2_2_gorilla`, `g_2_2_lizard`, `g_2_2_monkey`, `g_2_2_ooze`, `g_2_2_ooze_mitotic`, `g_2_2_spider_reach`, `g_2_2_wolf`, `g_2_2_wolf,g_3_3_beast,g_4_4_beast`, `g_2_3_antelope_forestwalk`, `g_2_5_treefolk_shaman`, `g_3_1_boar`, `g_3_2_cat_shroud`, `g_3_3_ape`, `g_3_3_badger`, `g_3_3_beast`, `g_3_3_boar`, `g_3_3_centaur`, `g_3_3_centaur_pro_black`, `g_3_3_dinosaur`, `g_3_3_dinosaur_trample`, `g_3_3_e_centaur`, `g_3_3_elemental`, `g_3_3_elephant`, `g_3_3_elk`, `g_3_3_frog_lizard`, `g_3_3_hippo`, `g_3_3_insect`, `g_3_3_mutant_deathtouch`, `g_3_3_ooze`, `g_3_3_phyrexian_beast_toxic`, `g_3_3_raccoon`, `g_3_3_tyranid_warrior_trample`, `g_3_4_treefolk_reach`, `g_4_2_beast`, `g_4_2_plant_warrior_reach`, `g_4_4_bear`, `g_4_4_beast`, `g_4_4_elemental`, `g_4_4_fungus_beast_trample`, `g_4_4_ox`, `g_4_4_phyrexian_beast`, `g_4_4_rhino_trample`, `g_4_4_rhino_warrior`, `g_4_4_troll_warrior_trample`, `g_4_4_wurm`, `g_4_5_spirit`, `g_5_3_elemental`, `g_5_4_snake`, `g_5_5_beast`, `g_5_5_beast_trample`, `g_5_5_elephant`, `g_5_5_tyranid`, `g_5_5_wurm`, `g_5_5_wurm_trample`, `g_6_1_insect_shroud`, `g_6_6_wurm`, `g_7_7_elemental_trample`, `g_7_7_giant`, `g_x_x_dinosaur_beast_trample`, `g_x_x_dinosaur_trample`, `g_x_x_elemental`, `g_x_x_elephant_resurgence`, `g_x_x_fungus_dinosaur`, `g_x_x_hydra`, `g_x_x_ooze`, `g_x_x_ooze_gutter_grime`, `g_x_x_phyrexian_horror`, `g_x_x_phyrexian_wurm_trample_toxic`, `g_x_x_saproling_burst`, `g_x_x_spirit`, `g_x_x_treefolk`, `g_x_x_treefolk_reach_total_lands`, `g_x_x_treefolk_warrior_total_forests`, `g_x_x_wurm`, `g_x_y_ooze_types_graveyard`, `galactus`, `goldmeadow_harrier`, `gu_0_0_fractal`, `gu_1_1_snake`, `gu_2_2_drake_flying`, `guenhwyvar`, `gw_1_1_alien_insect_flying`, `gw_1_1_citizen`, `gw_1_1_elf_warrior`, `gw_1_1_human_citizen`, `gw_1_1_human_soldier_training`, `gw_1_1_kithkin`, `gw_2_2_elf_knight_vigilance`, `gw_3_3_phyrexian_hydra_reach,gw_3_3_phyrexian_hydra_lifelink`, `gw_8_8_elemental_vigilance`, `gw_x_x_elemental_total_creatures`, `hornet`, `icingdeath_frost_tongue`, `icy_manalith`, `incubator_dark_confidant`, `jumblebones`, `kaldra`, `karox_bladewing`, `keimi`, `kelp`, `kobolds_of_kher_keep`, `komas_coil`, `land_mine`, `laserbeak`, `lightning_rager`, `llanowar_elves`, `marit_lage`, `mark_of_the_rani`, `mask`, `mechtitan`, `metallic_sliver`, `meteorite`, `minor_demon`, `mowu`, `munitions`, `nalaar_aetherjet`, `ornithopter`, `phobos`, `plaguebearer_of_nurgle`, `primo_the_indivisible`, `r_0_0_a_gremlin`, `r_0_1_elemental_rekindling_phoenix`, `r_0_2_dragon_egg_defender_hatches_dragon`, `r_1_1_balloon_flying`, `r_1_1_devil_burn`, `r_1_1_dinosaur_haste,w_1_1_human_soldier`, `r_1_1_dwarf`, `r_1_1_elemental`, `r_1_1_elemental_cat_haste`, `r_1_1_elemental_haste`, `r_1_1_elemental_ping`, `r_1_1_employee`, `r_1_1_goblin`, `r_1_1_goblin_all_attack`, `r_1_1_goblin_haste`, `r_1_1_goblin_noblock`, `r_1_1_goblin_scout_mountainwalk`, `r_1_1_goblin_wizard_prowess`, `r_1_1_gremlin`, `r_1_1_hamster`, `r_1_1_human`, `r_1_1_human_haste`, `r_1_1_mercenary_tappump`, `r_1_1_monk_prowess`, `r_1_1_phyrexian_goblin`, `r_1_1_phyrexian_goblin_haste`, `r_1_1_pirate_menace_haste`, `r_1_1_pirate_noblock_all_attack`, `r_1_1_satyr_noblock`, `r_1_1_soldier_haste`, `r_1_1_survivor`, `r_1_1_warrior`, `r_1_1_wizard_mana_restrict`, `r_2_1_dwarf_berserker`, `r_2_1_elemental_trample_haste`, `r_2_1_goblin_haste`, `r_2_1_human_wizard`, `r_2_2_alien_warrior`, `r_2_2_dragon_flying_firebreathing`, `r_2_2_goblin_shaman_treasure`, `r_2_2_gremlin`, `r_2_2_human_knight_trample_haste`, `r_2_2_imp_burn_opp`, `r_2_2_mutant`, `r_2_2_rebel`, `r_2_2_soldier`, `r_2_2_soldier_firebending_1`, `r_2_2_spirit_menace`, `r_2_3_demon_berserker_menace`, `r_2_3_minotaur`, `r_2_3_minotaur_haste`, `r_3_1_a_construct_haste`, `r_3_1_dinosaur`, `r_3_1_e_elemental_haste`, `r_3_1_elemental`, `r_3_1_elemental_haste`, `r_3_1_elemental_shaman`, `r_3_1_elemental_shaman_haste`, `r_3_1_elemental_trample_haste`, `r_3_1_knight`, `r_3_2_wolf`, `r_3_3_elemental`, `r_3_3_fighter_first_strike`, `r_3_3_ogre`, `r_3_3_spawn`, `r_4_2_pirate_noblock`, `r_4_4_bird_flying`, `r_4_4_devil_haste_treasure`, `r_4_4_dinosaur_dragon_flying`, `r_4_4_dragon_elemental_flying_prowess`, `r_4_4_dragon_flying`, `r_4_4_dragon_flying_firebending_4`, `r_4_4_giant`, `r_4_4_giant_bird`, `r_4_4_hellion`, `r_4_4_hellion_haste`, `r_4_4_ogre`, `r_4_4_scorpion_dragon_flying_haste`, `r_5_5_dragon_flying`, `r_5_5_dragon_spirit_flying`, `r_6_6_dragon_flying`, `r_7_1_elemental_trample_haste`, `r_8_8_lizard`, `r_x_1_elemental_trample_haste`, `r_x_1_phyrexian_horror_trample_haste`, `r_x_x_dragon_illusion_flying_haste`, `r_x_x_elemental`, `r_x_x_elemental_trample_grave_exile`, `rabid_sheep`, `ragavan`, `ravage`, `reliquary_dragon`, `replicated_ring`, `rg_1_1_dragon_flying_devour`, `rg_1_1_goblin_warrior`, `rg_2_2_satyr_haste`, `rg_4_4_beast_trample`, `rg_4_4_giant_warrior_haste`, `rg_5_4_dragon_spirit_damagesac`, `rg_5_5_elemental`, `rgw_1_1_sand_warrior`, `rgw_8_8_beast`, `riptide_replicator`, `rock`, `role_cursed`, `role_huntsman`, `role_monster`, `role_questing`, `role_royal`, `role_sorcerer`, `role_virtuous`, `role_wicked`, `role_young_hero`, `rw_1_1_goblin_soldier`, `rw_1_1_soldier_haste`, `rw_1_2_human_rogue_haste_damage`, `rw_2_1_human_cleric_lifelink_haste`, `rw_2_2_dinosaur_cat`, `rw_2_2_dinosaur_flying_haste`, `rw_2_2_spirit`, `rw_3_1_human_warrior_trample_haste`, `rw_3_2_spirit`, `rw_3_2_warrior_symbiotic_attack`, `rw_4_4_a_golem`, `scion_of_the_deep`, `scrap`, `settlement`, `smaug`, `smoke_blessing`, `spark_elemental`, `spawn_of_azar`, `stangg_twin`, `stoneforged_blade`, `storm_crow`, `sword`, `syr_acha`, `tamiyos_notebook`, `the_blackjack`, `the_hollow_sentinel`, `the_void`, `tiny`, `tombspawn`, `toskis_coil`, `tuktuk_the_returned`, `twin`, `u_0_0_alien`, `u_0_0_elemental`, `u_0_1_a_homunculus`, `u_0_1_starfish`, `u_0_2_illusion_mesmerize`, `u_0_3_crab`, `u_1_0_elemental`, `u_1_1_a_thopter_flying`, `u_1_1_beeble`, `u_1_1_bird_flying`, `u_1_1_bird_flying_blockflying`, `u_1_1_bird_flying_vigilance`, `u_1_1_bird_illusion_flying`, `u_1_1_camarid`, `u_1_1_faerie_dragon_flying`, `u_1_1_faerie_flying`, `u_1_1_faerie_flying_blockflying`, `u_1_1_faerie_spy_flying_haste_draw`, `u_1_1_fish`, `u_1_1_fish_unblockable`, `u_1_1_human_wizard`, `u_1_1_illusion_flying`, `u_1_1_illusion_other_illusions`, `u_1_1_jellyfish_flying`, `u_1_1_kraken_trample`, `u_1_1_merfolk`, `u_1_1_merfolk_hexproof`, `u_1_1_merfolk_wizard`, `u_1_1_ninja_unblockable`, `u_1_1_spirit_flying`, `u_1_1_squid_islandwalk`, `u_1_1_tentacle`, `u_1_1_tyranid_gargoyle_flying`, `u_1_1_wizard_countersac`, `u_1_1_wizard_flying`, `u_1_2_moonfolk_flying`, `u_2_1_a_phyrexian_myr`, `u_2_1_ninja`, `u_2_2_bird_flying`, `u_2_2_djinn_monk_flying`, `u_2_2_drake_flying`, `u_2_2_e_bird_flying`, `u_2_2_elemental_flying`, `u_2_2_homunculus`, `u_2_2_illusion`, `u_2_2_illusion_illusory`, `u_2_2_shapeshifter_changeling`, `u_2_2_spirit_vigilance_drawcounter`, `u_2_2_wizard`, `u_3_2_reflection`, `u_3_3_a_robot_warrior`, `u_3_3_fish_hatches_whale`, `u_3_3_illusion_villain`, `u_3_3_weird_defender_flying`, `u_4_3_salamander_warrior`, `u_4_4_elemental_bird_flying`, `u_4_4_giant_wizard`, `u_4_4_sphinx_flying`, `u_5_5_dragon_spirit_flying`, `u_5_5_wall_defender`, `u_8_8_kraken`, `u_8_8_kraken_hexproof`, `u_8_8_octopus`, `u_9_9_kraken`, `u_m1_m1_squid`, `u_x_x_dog_illusion_cardsinhand`, `u_x_x_illusion`, `u_x_x_orb_flying`, `u_x_x_shark_flying`, `u_x_x_spirit_flying`, `u_x_x_zombie`, `ub_1_1_faerie_flying`, `ub_1_1_faerie_rogue_flying`, `ub_1_1_horror_flying`, `ub_1_1_zombie_wizard`, `ub_2_2_zombie_rogue`, `ub_2_3_nightmare_mill`, `ub_x_x_zombie_menace`, `ur_1_1_elemental`, `ur_1_1_insect_flying_haste`, `ur_1_1_otter_prowess`, `ur_3_3_elemental_flying`, `ur_4_4_elemental`, `ur_5_5_elemental_flying`, `ur_x_x_elemental_flying_haste`, `ur_x_x_weird`, `urami`, `vecna`, `voja`, `voja_fenstalker`, `voja_friend_to_elves`, `volos_journal`, `volraths_laboratory`, `w_0_0_spirit_flying`, `w_0_1_caribou`, `w_0_1_deserter`, `w_0_1_goat`, `w_0_3_wall_defender`, `w_0_4_wall_defender`, `w_0_4_wall_defender_flying`, `w_1_1_a_clown_robot`, `w_1_1_a_toy`, `w_1_1_ally`, `w_1_1_bird_flying`, `w_1_1_bird_soldier_flying`, `w_1_1_cat`, `w_1_1_cat_bird_flying`, `w_1_1_cat_lifelink`, `w_1_1_cat_lifelink,w_1_1_bird_flying,w_2_4_ox`, `w_1_1_cat_soldier_vigilance`, `w_1_1_citizen`, `w_1_1_cleric_lifelink`, `w_1_1_dog`, `w_1_1_e_glimmer`, `w_1_1_e_soldier`, `w_1_1_halfling`, `w_1_1_halfling,c_a_food_sac`, `w_1_1_human`, `w_1_1_human,c_a_food_sac`, `w_1_1_human,u_1_1_merfolk,r_1_1_goblin`, `w_1_1_human_noble_vanishing_prevention`, `w_1_1_human_rogue`, `w_1_1_human_soldier`, `w_1_1_human_ward,w_4_4_alien_rhino`, `w_1_1_human_warrior`, `w_1_1_kithkin_soldier`, `w_1_1_knight_banding`, `w_1_1_kor_ally`, `w_1_1_kor_soldier`, `w_1_1_kor_warrior`, `w_1_1_monk_prowess`, `w_1_1_mouse`, `w_1_1_ninja_turtle_spirit`, `w_1_1_pegasus_flying`, `w_1_1_rabbit`, `w_1_1_sheep`, `w_1_1_soldier`, `w_1_1_soldier_ally`, `w_1_1_soldier_lifelink`, `w_1_1_spirit`, `w_1_1_spirit_flying`, `w_1_1_vampire_lifelink`, `w_1_1_warrior`, `w_1_1_warrior_vigilance`, `w_1_1_zombie`, `w_1_2_moogle_lifelink`, `w_1_2_soldier_defender`, `w_1_3_wall_defender`, `w_2_1_cat_warrior`, `w_2_1_e_cleric`, `w_2_1_insect_flying`, `w_2_2_alien`, `w_2_2_astartes_warrior_vigilance`, `w_2_2_cat`, `w_2_2_cat_beast`, `w_2_2_dinosaur_soldier`, `w_2_2_e_nymph`, `w_2_2_fox_vigilance`, `w_2_2_griffin_flying`, `w_2_2_horse_horsemanship`, `w_2_2_human_knight_artifact_pump`, `w_2_2_knight`, `w_2_2_knight_ally`, `w_2_2_knight_first_strike`, `w_2_2_knight_pro_red`, `w_2_2_knight_vigilance`, `w_2_2_ox`, `w_2_2_pegasus_flying`, `w_2_2_performer`, `w_2_2_reflection`, `w_2_2_samurai_double_strike`, `w_2_2_samurai_vigilance`, `w_2_2_soldier`, `w_2_2_soldier_vigilance`, `w_2_2_spirit_flying`, `w_2_2_unicorn`, `w_2_4_ox`, `w_3_1_spirit_flying`, `w_3_3_angel_flying`, `w_3_3_bird_flying`, `w_3_3_bird_flying_attacks`, `w_3_3_knight`, `w_3_3_spirit_flying`, `w_3_4_bird_flying`, `w_4_4_angel_flying`, `w_4_4_angel_flying_vigilance`, `w_4_4_angel_warrior_flying`, `w_4_4_angel_warrior_flying_vigilance`, `w_4_4_avatar_flying`, `w_4_4_beast_lonely`, `w_4_4_elemental_flying`, `w_4_4_spirit_flying`, `w_5_5_giant_warrior`, `w_5_5_horse`, `w_x_x_a_gnome_soldier_total_artifacts_creatures`, `w_x_x_avatar`, `w_x_x_avatar_life_total`, `w_x_x_reflection`, `w_x_x_spirit`, `w_x_x_spirit_cleric_total_spirits`, `walker`, `wasp`, `wasteland_survival_guide`, `wb_1_1_cleric_deathpact`, `wb_1_1_human_cleric`, `wb_1_1_inkling_flying`, `wb_1_1_spirit_flying`, `wb_1_1_vampire_lifelink`, `wb_2_1_inkling_flying`, `wb_2_1_inkling_flying,rw_3_2_spirit,ur_4_4_elemental`, `wb_4_3_vampire_demon_flying`, `wb_x_x_e_spirit_experience`, `wirefly`, `wolves_of_the_hunt`, `wood`, `wu_1_1_bird_flying`, `wu_1_1_merfolk`, `wu_2_2_detective`, `wu_2_2_knight_vigilance`, `wu_4_4_a_golem`, `wu_4_4_elemental`, `wu_4_4_sphinx_flying_vigilance`, `yellow_hat`, `zeppelin`
- `TokenTapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `TokenToughness$`: TODO: Describe this parameter.
  Observed values: `dY`, `L`, `LifePaidOnETB`, `MonstrosityX`, `X`, `XLKI`, `Y`, `Z`
- `TokenTypes$`: TODO: Describe this parameter.
  Observed values: `ChosenType`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `3`, `Draw<1/Player.Activator>`, `ExileFromGrave<1/Creature;Enchantment/creature or enchantment card>`, `ExileFromGrave<3/Card>`, `Mandatory PayEnergy<X>`, `Sac<1/Creature>`, `tapXType<1/Card.TriggeredCard/that card>`, `Y`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `Player.IsRemembered`, `Player.Opponent`, `TriggeredAttackerController`, `TriggeredCardController`, `TriggeredCardLKIController`, `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenNotPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidAfterStack$`: TODO: Describe this parameter.
  Observed values: `Ability.IsTargeting Player.withMoreCreaturesThanYou`
- `ValidTgtDesc$`: TODO: Describe this parameter.
  Observed values: `creature an opponent controls`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.attacking`, `Creature.attackingYou`, `Creature.OppCtrl`, `Creature.Other`, `Creature.YouCtrl`, `Creature.YouCtrl+Other`, `Land.YouCtrl`, `Opponent`, `Permanent.Other`, `Player`
- `WithCountersAmount$`: TODO: Describe this parameter.
  Observed values: `1`, `X`
- `WithCountersType$`: TODO: Describe this parameter.
  Observed values: `P1P1`
- `XMax$`: TODO: Describe this parameter.
  Observed values: `LifeLost`
- `XMin$`: TODO: Describe this parameter.
  Observed values: `1`

## `TwoPiles`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Best`, `Random`, `Worst`
- `Chooser$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `TriggeredDefendingPlayer`, `TriggeredPlayer`, `You`
- `ChosenPile$`: TODO: Describe this parameter.
  Observed values: `DBAtkLeftPile`, `DBBattlefield`, `DBBreak`, `DBDefLeftPile`, `DBDestroy`, `DBEffect`, `DBExile`, `DBHand`, `DBHand9M`, `DBPlay`, `DBSacAll`, `ToGrave`, `ToHand`, `TurnFaceUp`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE10`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `SubCounter<6/LOYALTY>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `TriggeredPlayer`, `You`
- `DefinedCards$`: TODO: Describe this parameter.
  Observed values: `Imprinted`, `Remembered`, `Targeted`, `Top_4_OfLibrary`
- `DefinedPiles$`: TODO: Describe this parameter.
  Observed values: `Imprinted,Remembered`, `Remembered,Imprinted`
- `FaceDown$`: TODO: Describe this parameter.
  Observed values: `One`, `True`
- `KeepRemembered$`: TODO: Describe this parameter.
  Observed values: `True`
- `LeftRightPile$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberChosen$`: TODO: Describe this parameter.
  Observed values: `True`
- `Separator$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Remembered`, `Targeted`, `TargetedPlayer`, `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `DBCleanupChosen`, `DBClearImprinted`, `DBLoseLife`, `TheyChoose`, `TrigTempt`
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnchosenPile$`: TODO: Describe this parameter.
  Observed values: `DBAtkRightPile`, `DBBend`, `DBDefRightPile`, `DBExile`, `DBGrave`, `DBGraveyard`, `DBLibraryBottom`, `DBLibraryBottom9M`, `DBPlay`, `DBReturn`, `ToGrave`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.attacking+YouCtrl`, `Creature.RememberedPlayerCtrl`, `Creature.withoutFlying+RememberedPlayerCtrl`, `Land.!token+RememberedPlayerCtrl`, `Permanent`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Battlefield`, `Exile`, `Graveyard`, `Library`

## `Unattach`

TODO: Write documentation.

**Parameters:**
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Enchanted`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Equipment`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `DelayTriggerRememberedLKI`, `Enchanted`, `Remembered`, `Valid Equipment.AttachedTo Card.targetedBy`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBTap`, `ExileSelf`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Creature`

## `UnlockDoor`

TODO: Write documentation.

**Parameters:**
- `Choices$`: TODO: Describe this parameter.
  Observed values: `Room.YouCtrl+!FullyUnlocked`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 T Sac<1/CARDNAME>`, `T`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Room.YouCtrl+!FullyUnlocked`
- `Mode$`: TODO: Describe this parameter.
  Observed values: `LockOrUnlock`, `Unlock`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`
- `TgtPrompt$`: TODO: Describe this parameter.
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Room.YouCtrl`

## `Untap`

TODO: Write documentation.

**Parameters:**
- `Activation$`: TODO: Describe this parameter.
  Observed values: `Threshold`
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->Declare Attackers`, `BeginCombat->EndCombat`, `Upkeep`
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Command`
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `AtOppEOT`, `Never`, `PoolExtraMana`, `PreventCombatDamage`
- `AIManaPref$`: TODO: Describe this parameter.
  Observed values: `NotSameCard`
- `Amount$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `X`
- `Boast$`: TODO: Describe this parameter.
  Observed values: `True`
- `Condition$`: TODO: Describe this parameter.
  Observed values: `Kicked`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `X`, `Y`, `Z`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE1`, `GE2`, `GE4`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`, `RememberedLKI`, `Targeted`, `TriggeredTargetLKICopy`
- `ConditionDescription$`: TODO: Describe this parameter.
  Observed values: `If it was kicked,`, `If you control four or more lands, untap that land.`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Artifact`, `Card.Aura`, `Card.Creature`, `Card.IsRenowned`, `Card.Land`, `Creature`, `Creature.attacking`, `Instant.YouOwn,Sorcery.YouOwn`, `Land.nonBasic`, `Land.YouCtrl`, `Wolf,Werewolf`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ1`, `GE10`, `GE5`, `LEY`
- `ConditionZone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `tapXType<5/Creature>`, `T`, `1 tapXType<1/Creature>`, `1 W`, `AddCounter<1/M1M1>`, `3`, `tapXType<2/Merfolk>`, `Sac<1/Creature>`, `3 U`, `1`
- `CostDesc$`: TODO: Describe this parameter.
  Observed values: `Tap enchanted creature:`, `{1}, Tap an untapped creature you control:`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenCard`, `Enchanted`, `Equipped`, `ParentTarget`, `Remembered`, `ReplacedCard`, `Self`, `Targeted`, `Targeted.YouCtrl`, `TriggeredAttacker`, `TriggeredAttackerLKICopy`, `TriggeredCard`, `TriggeredCardLKICopy`, `TriggeredPlayer`, `TriggeredSpellAbilityTargets`, `You`
- `ETB$`: TODO: Describe this parameter.
  Observed values: `True`
- `GameActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `IsCurse$`: TODO: Describe this parameter.
  Observed values: `True`
- `IsPresent$`: TODO: Describe this parameter.
  Observed values: `Planeswalker.Gideon+YouCtrl`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`, `true`
- `PlayerTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Bigby's Hand —`, `Conjure Elemental —`, `Mage Hand —`, `Threshold —`
- `Radiance$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberTargets$`: TODO: Describe this parameter.
  Observed values: `True`
- `ShowCurrentCard$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Animate`, `DBAddCombat`, `DBAddPhase`, `DBAnimate`, `DBChange`, `DBCleanup`, `DBClone`, `DBControl`, `DBDelTrig`, `DBDesc`, `DBDiscard`, `DBDraw`, `DBEffect`, `DBGainControl`, `DBGainLife`, `DBInvestigate`, `DBPhase`, `DBProtection`, `DBPump`, `DBPutCounter`, `DBRandom`, `DBRemoveCombat`, `DBScry`, `DBStunCounter`, `DBTap`, `DBTransform`, `DBUntap`, `DelTrigSlowtrip`, `GainShroud`, `Reconsider`, `RemCombat`, `TrigDraw`
- `TargetMax$`: TODO: Describe this parameter.
  Observed values: `1`, `2`, `3`, `4`, `6`, `MaxTgts`, `OneEach`, `X`
- `TargetMin$`: TODO: Describe this parameter.
  Observed values: `0`, `1`, `2`, `X`
- `TargetsForEachPlayer$`: TODO: Describe this parameter.
  Observed values: `True`
- `TargetUnique$`: TODO: Describe this parameter.
  Observed values: `True`
- `TgtPrompt$`: TODO: Describe this parameter.
- `Ultimate$`: TODO: Describe this parameter.
  Observed values: `True`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `2`, `4`, `Draw<1/Player.Activator>`, `U`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `DefendingPlayer`, `EnchantedController`, `RememberedController`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `UntapExactly$`: TODO: Describe this parameter.
  Observed values: `True`
- `UntapType$`: TODO: Describe this parameter.
  Observed values: `Creature.YouCtrl`, `Land`, `Land.ActivePlayerCtrl`, `Land.YouCtrl`
- `UntapUpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact,Creature`, `Artifact,Creature,Land`, `Artifact.nonCreature`, `Artifact.Other`, `Artifact.Other+YouCtrl,Creature.Other+YouCtrl`, `Artifact.YouCtrl,Creature.YouCtrl`, `Creature`, `Creature,Land`, `Creature.Artifact`, `Creature.attacking`, `Creature.attacking+OppCtrl`, `Creature.attacking+Other`, `Creature.attacking+withShadow`, `Creature.attacking+YouCtrl`, `Creature.attacking+youCtrl`, `Creature.Blue`, `Creature.counters_GE1_P1P1`, `Creature.hasAbility Activated.hasTapCost`, `Creature.Legendary+Other`, `Creature.Legendary+YouCtrl`, `Creature.nonLegendary`, `Creature.OppCtrl`, `Creature.OppCtrl+tapped`, `Creature.Other`, `Creature.Other+YouCtrl`, `Creature.Other+YouCtrl,Land.Other+YouCtrl`, `Creature.powerLTX`, `Creature.YouCtrl`, `Creature.YouDontCtrl`, `Creature.YourTeamCtrl`, `Elf`, `Forest`, `Gate`, `Goat`, `Griffin`, `Kraken`, `Land`, `Land.Basic`, `Land.Snow`, `Land.YouCtrl`, `Merfolk.YouCtrl`, `Mountain`, `Permanent`, `Permanent.Legendary`, `Permanent.nonLand`, `Permanent.nonLand+OppCtrl`, `Permanent.Other`, `Permanent.Other+!namedClever Conjurer`, `Permanent.Other+nonLand`, `Permanent.Other+Snow`, `Permanent.Other+YouCtrl`, `Permanent.YouCtrl`
- `ValidTgtsDesc$`: TODO: Describe this parameter.
  Observed values: `another creature`

## `UntapAll`

TODO: Write documentation.

**Parameters:**
- `ActivationLimit$`: TODO: Describe this parameter.
  Observed values: `1`
- `ActivationPhases$`: TODO: Describe this parameter.
  Observed values: `BeginCombat->EndCombat`, `Declare Attackers`
- `CheckSVar$`: TODO: Describe this parameter.
  Observed values: `Count$FinishedUpkeepsThisTurn`, `X`
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Food`, `Win`, `X`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Remembered`
- `ConditionManaSpent$`: TODO: Describe this parameter.
  Observed values: `W`
- `ConditionPlayerTurn$`: TODO: Describe this parameter.
  Observed values: `False`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `GE20`, `GE3`
- `ControllerUntaps$`: TODO: Describe this parameter.
  Observed values: `True`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `3 R R`, `PayLife<10>`, `AddCounter<2/LOYALTY>`, `5 R R`, `AddCounter<1/LOYALTY>`, `T Sac<1/CARDNAME>`, `1 T`, `W U B R G`, `T`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `TargetedAndYou`, `TriggeredAttackingPlayer.Opponent+controlsCreature.attacking Player.EnchantedBy`, `TriggeredPlayer`, `You`
- `ModeCost$`: TODO: Describe this parameter.
  Observed values: `1`, `2 R`
- `OpponentTurn$`: TODO: Describe this parameter.
  Observed values: `True`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberUntapped$`: TODO: Describe this parameter.
  Observed values: `True`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `Battlecry`, `DBAddCombat`, `DBAddPhase`, `DBCleanup`, `DBDraw`, `DBEffect`, `DBGainControl`, `DBGainCtrl`, `DBGoad`, `DBPhase`, `DBPhaseOut`, `DBPump`, `DBPumpAll`, `DBPumpYourSamurai`, `DBTap`, `DBUntap`, `RepeatLoseLife`, `TheFuryContinues`
- `UnlessCost$`: TODO: Describe this parameter.
  Observed values: `PayEnergy<8>`
- `UnlessPayer$`: TODO: Describe this parameter.
  Observed values: `You`
- `UnlessResolveSubs$`: TODO: Describe this parameter.
  Observed values: `WhenPaid`
- `UnlessSwitched$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidCards$`: TODO: Describe this parameter.
  Observed values: `Artifact`, `Artifact.Creature+YouCtrl+Other`, `Artifact.tapped,Creature.tapped,Land.tapped`, `Bird.YouCtrl,Frog.YouCtrl,Otter.YouCtrl,Rat.YouCtrl`, `Card.Self,Samurai.YouCtrl`, `Creature`, `Creature,Land`, `Creature.attackedThisTurn`, `Creature.attacking`, `Creature.attacking+White+Other+YouCtrl`, `Creature.ChosenType`, `Creature.ControlledBy TriggeredDefendingPlayer`, `Creature.IsRemembered`, `Creature.modified+YouCtrl`, `Creature.Other+YouCtrl`, `Creature.tapped`, `Creature.tapped+YouCtrl`, `Creature.TargetedPlayerCtrl`, `Creature.White+YouCtrl`, `Creature.YouCtrl`, `Creature.YouCtrl+!ThisTurnEntered+!attackedThisTurn`, `Creature.YouCtrl+attackedThisTurn`, `Creature.YouCtrl+counters_GE1_P1P1`, `Creature.YouCtrl+HasCounters`, `Creature.YouCtrl+StrictlyOther`, `Forest`, `Forest,Creature.Green`, `Forest.YouCtrl`, `Land.Basic`, `Land.YouCtrl`, `Merfolk.Other+YouCtrl`, `Merfolk.YouCtrl`, `Myr.StrictlyOther+YouCtrl`, `Myr.YouCtrl`, `Permanent.ChosenCard`, `Permanent.enchanted+YouCtrl`, `Permanent.nonLand`, `Permanent.nonLand+YouCtrl`, `Permanent.nonLand+YouCtrl,Permanent.nonLand+ChosenCtrl`, `Permanent.Snow+YouCtrl`, `Permanent.YouCtrl`, `Permanent.YouCtrl+HasCounters`, `Permanent.YouCtrl+nonLand`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`, `Player`

## `Venture`

TODO: Write documentation.

**Parameters:**
- `ActivationZone$`: TODO: Describe this parameter.
  Observed values: `Hand`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `4 T tapXType<1/Creature.Legendary/legendary creature>`, `3 T`, `AddCounter<1/LOYALTY>`, `4 T`, `W Discard<1/CARDNAME>`, `3 T tapXType<1/Creature.Other>`, `1 T tapXType<1/Creature.Legendary/legendary creature>`, `4 U`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `You`
- `Planeswalker$`: TODO: Describe this parameter.
  Observed values: `True`
- `PrecostDesc$`: TODO: Describe this parameter.
  Observed values: `Rappel Down —`
- `SorcerySpeed$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBGainLife`

## `VillainousChoice`

TODO: Write documentation.

**Parameters:**
- `Choices$`: TODO: Describe this parameter.
  Observed values: `DBAnimate,DBCopy`, `DBDamage,DBDraw`, `DBDestroyDalek,DBDestroyNonDalek`, `DBDig,DBDamage`, `DBDiscard,DBChangeZone`, `DBDiscard,DBDamage`, `DBLoseLife,DBCopy`, `DBLoseLife,DBShuffleAnother`, `DBSacrifice,DBGainControl`, `DBSacrifice,DBToken`, `Discard,FreeCast`, `Draw,Discard`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `ChosenPlayer`, `Opponent`, `Opponent.LostLifeThisTurn GE3`, `RememberedController`, `TargetedOwner`, `TriggeredDefendingPlayer`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Opponent`

## `Vote`

TODO: Write documentation.

**Parameters:**
- `AILogic$`: TODO: Describe this parameter.
  Observed values: `Always`, `CarnageOrHomage`, `DeathOrTaxes`, `FeatherOrQuill`, `GraceOrCondemnation`, `Judgment`, `Protection`, `SproutOrHarvest`, `StrengthOrNumbers`, `Torture`
- `Choices$`: TODO: Describe this parameter.
  Observed values: `DBAddTurn,DBDrawThree`, `DBChangeZone,DBWheel`, `DBDenial,DBDuplication`, `DBDestroyAll,DBDraw`, `DBDraw,DBChoose`, `DBEvidence,DBBribery`, `DBInnocent,DBGuilty`, `DBPlaneswalk,DBChaos`, `DBPumpAll,DBDiscard`, `DBTempt,DBDraw`, `DBTime,DBMoney`, `DBVoteDeath,DBVoteTaxes`, `DBVoteFeather,DBVoteQuill`, `DBVotePast,DBVotePresent`, `DBVoteProfit,DBVoteSecurity`, `DBVoteSprout,DBVoteHarvest`, `DBVoteStrength,DBVoteNumbers`, `DBVoteWild,DBVoteFree`, `DBZombify,DBDestroy`, `Fellowship,AidPlus`, `PumpU,PumpB,PumpR,PumpG`, `TyrantsChoiceSac,TyrantsChoiceLoseLife`, `VoteRedhornPass,VoteMinesofMoria`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player`
- `EachVote$`: TODO: Describe this parameter.
  Observed values: `True`
- `RememberVotedObjects$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secret$`: TODO: Describe this parameter.
  Observed values: `True`
- `Secretly$`: TODO: Describe this parameter.
  Observed values: `True`
- `SpellDescription$`: TODO: Describe this parameter.
- `StackDescription$`: TODO: Describe this parameter.
- `StoreVoteNum$`: TODO: Describe this parameter.
  Observed values: `True`
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBChange`, `DBExile`, `DBGainControl`, `DBRepeatDraw`, `DBRepeatOpp`, `DBRepeatStun`
- `TargetType$`: TODO: Describe this parameter.
  Observed values: `Spell`
- `TgtZone$`: TODO: Describe this parameter.
  Observed values: `Stack`
- `UpTo$`: TODO: Describe this parameter.
  Observed values: `True`
- `ValidTgts$`: TODO: Describe this parameter.
  Observed values: `Instant,Sorcery`
- `VoteCard$`: TODO: Describe this parameter.
  Observed values: `Creature`, `Creature.YouDontCtrl`, `Creature.YouOwn,Enchantment.YouOwn,Artifact.YouOwn`, `Permanent.nonLand+YouDontCtrl`
- `VoteMessage$`: TODO: Describe this parameter.
  Observed values: `for a creature`, `for a creature you don't control`, `for a nonland permanent you don't control`, `for an artifact, creature, or enchantment card in your graveyard`
- `VotePlayer$`: TODO: Describe this parameter.
  Observed values: `Other`, `Player`
- `VoteSubAbility$`: TODO: Describe this parameter.
  Observed values: `DBDestroyAll`, `DBExile`, `DBReturn`
- `VoteTiedAbility$`: TODO: Describe this parameter.
  Observed values: `DBChaos`, `DBDestroy`, `DBDiscard`, `DBDraw`, `DBDrawThree`, `DBDuplication`, `DBInnocent`, `DBWheel`, `TyrantsChoiceLoseLife`
- `Zone$`: TODO: Describe this parameter.
  Observed values: `Graveyard`

## `WinsGame`

TODO: Write documentation.

**Parameters:**
- `ConditionCheckSVar$`: TODO: Describe this parameter.
  Observed values: `Contractors`, `MaxRolls`, `MazeGate`, `NumHighestLife`, `RoomsUnlocked`, `TalkedEnough`, `Win`, `X`, `Y`
- `ConditionCompare$`: TODO: Describe this parameter.
  Observed values: `EQ6`, `GE13`
- `ConditionDefined$`: TODO: Describe this parameter.
  Observed values: `Tapped`
- `ConditionPresent$`: TODO: Describe this parameter.
  Observed values: `Card.Self+counters_EQ0_OMEN`, `Card.Self+counters_GE100_LUCK`, `Creature.Legendary`, `Creature.YouCtrl+powerGE20`, `Doctor.YouCtrl`
- `ConditionSVarCompare$`: TODO: Describe this parameter.
  Observed values: `EQ0`, `EQ10`, `EQ4`, `EQ5`, `EQ7`, `GE10`, `GE20`, `GE4`, `GE5`, `GE8`, `LEX`, `LT2`
- `Cost$`: TODO: Describe this parameter.
  Observed values: `W W W W W T untapYType<15/Creature.YouCtrl/creatures>`
- `Defined$`: TODO: Describe this parameter.
  Observed values: `Player.lifeEQX`, `You`
- `SpellDescription$`: TODO: Describe this parameter.
- `SubAbility$`: TODO: Describe this parameter.
  Observed values: `DBCleanup`, `GameIsADraw`
