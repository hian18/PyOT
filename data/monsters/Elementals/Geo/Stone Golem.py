stone_golem = genMonster("Stone Golem", 67, 6005)
stone_golem.health(270)
stone_golem.type("undead")
stone_golem.defense(armor=33, fire=0.8, earth=0, energy=0.85, ice=1.1, holy=1, death=0.8, physical=0.8, drown=1)
stone_golem.experience(160)
stone_golem.speed(180)
stone_golem.behavior(summonable=590, hostile=True, illusionable=True, convinceable=590, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
stone_golem.walkAround(energy=1, fire=1, poison=0)
stone_golem.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
stone_golem.melee(110)
stone_golem.loot( (2148, 97.5, 15), ("small stone", 38.5, 4), ("power ring", 5.25), ("carlin sword", 2.5), ("sulphurous stone", 9.5), ("ancient stone", 1.25), ("iron ore", 2.5, 3), ("coal", 0.75), ("shiny stone", 0.75) )