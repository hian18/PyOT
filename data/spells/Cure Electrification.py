instant = spell.Spell("Cure Electrification", "exana vis", icon=146, target=TARGET_SELF, group=HEALING_GROUP)
instant.require(mana=30, level=22, maglevel=0, learned=0, vocations=(2, 6))
instant.cooldowns(6, 1)
instant.targetEffect(callback=spell.cure(ENERGY))
instant.effects(caster=EFFECT_MAGIC_BLUE)