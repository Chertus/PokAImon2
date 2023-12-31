# move_list.py

move_list_dict = {
    "Absorb": {"Type": "Grass", "Power": 20, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "User recovers half of damage inflicted on opponent."},
    "Acid": {"Type": "Poison", "Power": 40, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "10% chance of lowering opponent's defense by 1."},
    "Acid Armor": {"Type": "Poison", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Raises user's defense by 2."},
    "Agility": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "TM33", "Description": "Raises user's speed by 2."},
    "Amnesia": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Raises user's special by 2."},
    "Aurora Beam": {"Type": "Ice", "Power": 65, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "10% chance of lowering opponent's attack by 1."},
    "Barrage": {"Type": "Normal", "Power": 15, "Accuracy": 85, "PP": 20, "TM/HM": "", "Description": "Attacks opponent repeatedly."},
    "Barrier": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Raises user's defense by 2."},
    "Bide": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM34", "Description": "User doesn't attack for 2-3 turns, then attacks with double the damage received from the opponent."},
    "Bind": {"Type": "Normal", "Power": 15, "Accuracy": 75, "PP": 10, "TM/HM": "", "Description": "Attacks for 2-5 turns; opponent cannot attack until Bind finishes."},
    "Bite": {"Type": "Normal", "Power": 60, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "30% chance the opponent flinches afterward."},
    "Blizzard": {"Type": "Ice", "Power": 120, "Accuracy": 90, "PP": 5, "TM/HM": "TM14", "Description": "10% chance of freezing the opponent."},
    "Body Slam": {"Type": "Normal", "Power": 85, "Accuracy": 100, "PP": 15, "TM/HM": "TM08", "Description": "30% chance of paralyzing the opponent."},
    "Bone Club": {"Type": "Ground", "Power": 65, "Accuracy": 85, "PP": 20, "TM/HM": "", "Description": "10% chance the opponent flinches afterward."},
    "Bonemerang": {"Type": "Ground", "Power": 50, "Accuracy": 90, "PP": 10, "TM/HM": "", "Description": "Attacks opponent twice in succession."},
    "Bubble": {"Type": "Water", "Power": 20, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "10% chance of lowering opponent's speed by 1."},
    "Bubblebeam": {"Type": "Water", "Power": 60, "Accuracy": 100, "PP": 20, "TM/HM": "TM11", "Description": "10% chance of lowering opponent's speed by 1."},
    "Clamp": {"Type": "Water", "Power": 35, "Accuracy": 75, "PP": 10, "TM/HM": "", "Description": "Attacks for 2-5 turns; opponent cannot attack until Clamp finishes."},
    "Comet Punch": {"Type": "Normal", "Power": 18, "Accuracy": 85, "PP": 15, "TM/HM": "", "Description": "Attacks opponent 2-5 times in succession."},
    "Confuse Ray": {"Type": "Ghost", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "Confuses opponent."},
    "Confusion": {"Type": "Psychic", "Power": 50, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "10% chance of confusing the opponent."},
    "Constrict": {"Type": "Normal", "Power": 10, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "10% chance of lowering opponent's speed by 1."},
    "Conversion": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "User's type becomes the type of one of its moves at random."},
    "Counter": {"Type": "Fighting", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "TM18", "Description": "Inflicts double the damage the user received from the last physical hit."},
    "Crabhammer": {"Type": "Water", "Power": 90, "Accuracy": 85, "PP": 10, "TM/HM": "", "Description": "High critical hit ratio."},
    "Cut": {"Type": "Normal", "Power": 50, "Accuracy": 95, "PP": 30, "TM/HM": "HM01", "Description": "Cuts down thin trees outside of battle."},
    "Defense Curl": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Raises user's defense by 1."},
    "Dig": {"Type": "Ground", "Power": 80, "Accuracy": 100, "PP": 10, "TM/HM": "TM28", "Description": "Digs underground on first turn, attacks on second. Can also escape from caves."},
    "Disable": {"Type": "Normal", "Power": 0, "Accuracy": 55, "PP": 20, "TM/HM": "", "Description": "Randomly disables one of the opponent's moves."},
    "Dizzy Punch": {"Type": "Normal", "Power": 70, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "20% chance of confusing the opponent."},
    "Double Kick": {"Type": "Fighting", "Power": 30, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Hits opponent twice in one turn."},
    "Double Team": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 15, "TM/HM": "TM32", "Description": "Raises user's evasiveness by 1."},
    "Double-Edge": {"Type": "Normal", "Power": 100, "Accuracy": 100, "PP": 15, "TM/HM": "TM10", "Description": "User receives recoil damage equal to 1/3 of damage inflicted on opponent."},
    "DoubleSlap": {"Type": "Normal", "Power": 15, "Accuracy": 85, "PP": 10, "TM/HM": "", "Description": "Attacks opponent 2-5 times in succession."},
    "Dragon Rage": {"Type": "Dragon", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "Always inflicts 40 HP."},
    "Dream Eater": {"Type": "Psychic", "Power": 100, "Accuracy": 100, "PP": 15, "TM/HM": "TM42", "Description": "User recovers half of damage inflicted on a sleeping opponent."},
    "Drill Peck": {"Type": "Flying", "Power": 80, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "No additional effect."},
    "Earthquake": {"Type": "Ground", "Power": 100, "Accuracy": 100, "PP": 10, "TM/HM": "TM26", "Description": "Power is doubled if opponent is underground from using Dig."},
    "Egg Bomb": {"Type": "Normal", "Power": 100, "Accuracy": 75, "PP": 10, "TM/HM": "", "Description": "No additional effect."},
    "Ember": {"Type": "Fire", "Power": 40, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "10% chance of burning the opponent."},
    "Explosion": {"Type": "Normal", "Power": 170, "Accuracy": 100, "PP": 5, "TM/HM": "TM47", "Description": "User faints."},
    "Fire Blast": {"Type": "Fire", "Power": 110, "Accuracy": 85, "PP": 5, "TM/HM": "TM38", "Description": "10% chance of burning the opponent."},
    "Fire Punch": {"Type": "Fire", "Power": 75, "Accuracy": 100, "PP": 15, "TM/HM": "TM48", "Description": "10% chance of burning the opponent."},
    "Fire Spin": {"Type": "Fire", "Power": 15, "Accuracy": 70, "PP": 15, "TM/HM": "", "Description": "Attacks for 2-5 turns; opponent cannot attack until Fire Spin finishes."},
    "Fissure": {"Type": "Ground", "Power": 0, "Accuracy": 30, "PP": 5, "TM/HM": "TM27", "Description": "Causes a one-hit KO, if it hits."},
    "Flamethrower": {"Type": "Fire", "Power": 90, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "10% chance of burning the opponent."},
    "Flash": {"Type": "Normal", "Power": 0, "Accuracy": 70, "PP": 20, "TM/HM": "HM05", "Description": "Lowers opponent's accuracy by 1. Can also light up dark areas."},
    "Fly": {"Type": "Flying", "Power": 70, "Accuracy": 95, "PP": 15, "TM/HM": "HM02", "Description": "Flies up on first turn, attacks on second turn. Can also fly to any known town."},
    "Focus Energy": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Increases critical hit ratio."},
    "Fury Attack": {"Type": "Normal", "Power": 15, "Accuracy": 85, "PP": 20, "TM/HM": "", "Description": "Attacks opponent 2-5 times in succession."},
    "Fury Swipes": {"Type": "Normal", "Power": 18, "Accuracy": 80, "PP": 15, "TM/HM": "", "Description": "Attacks opponent 2-5 times in succession."},
    "Glare": {"Type": "Normal", "Power": 0, "Accuracy": 75, "PP": 30, "TM/HM": "", "Description": "Paralyzes opponent."},
    "Growl": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Lowers opponent's attack by 1."},
    "Growth": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Raises user's attack and special by 1."},
    "Guillotine": {"Type": "Normal", "Power": 0, "Accuracy": 30, "PP": 5, "TM/HM": "", "Description": "Causes a one-hit KO, if it hits."},
    "Gust": {"Type": "Flying", "Power": 40, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "Hits Pokémon using Fly/Bounce with double power."},
    "Harden": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Raises user's defense by 1."},
    "Haze": {"Type": "Ice", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Resets all stat changes."},
    "Headbutt": {"Type": "Normal", "Power": 70, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "30% chance of causing the opponent to flinch."},
    "High Jump Kick": {"Type": "Fighting", "Power": 85, "Accuracy": 90, "PP": 20, "TM/HM": "", "Description": "If it misses, the user loses half their HP."},
    "Horn Attack": {"Type": "Normal", "Power": 65, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "No additional effect."},
    "Horn Drill": {"Type": "Normal", "Power": 0, "Accuracy": 30, "PP": 5, "TM/HM": "", "Description": "Causes a one-hit KO, if it hits."},
    "Hydro Pump": {"Type": "Water", "Power": 110, "Accuracy": 80, "PP": 5, "TM/HM": "", "Description": "No additional effect."},
    "Hyper Beam": {"Type": "Normal", "Power": 150, "Accuracy": 90, "PP": 5, "TM/HM": "TM15", "Description": "User must recharge next turn."},
    "Hyper Fang": {"Type": "Normal", "Power": 80, "Accuracy": 90, "PP": 15, "TM/HM": "", "Description": "10% chance of causing the opponent to flinch."},
    "Hypnosis": {"Type": "Psychic", "Power": 0, "Accuracy": 60, "PP": 20, "TM/HM": "", "Description": "Puts opponent to sleep."},
    "Ice Beam": {"Type": "Ice", "Power": 90, "Accuracy": 100, "PP": 10, "TM/HM": "TM13", "Description": "10% chance of freezing the opponent."},
    "Ice Punch": {"Type": "Ice", "Power": 75, "Accuracy": 100, "PP": 15, "TM/HM": "TM33", "Description": "10% chance of freezing the opponent."},
    "Jump Kick": {"Type": "Fighting", "Power": 70, "Accuracy": 95, "PP": 25, "TM/HM": "", "Description": "If it misses, the user loses half their HP."},
    "Karate Chop": {"Type": "Fighting", "Power": 50, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "High critical hit ratio."},
    "Kinesis": {"Type": "Psychic", "Power": 0, "Accuracy": 80, "PP": 15, "TM/HM": "", "Description": "Lowers opponent's accuracy by 1."},
    "Leech Life": {"Type": "Bug", "Power": 20, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "User recovers half of damage inflicted on opponent."},
    "Leech Seed": {"Type": "Grass", "Power": 0, "Accuracy": 90, "PP": 10, "TM/HM": "", "Description": "1/8 of opponent's HP is drained each turn."},
    "Leer": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Lowers opponent's defense by 1."},
    "Lick": {"Type": "Ghost", "Power": 20, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "30% chance of paralyzing the opponent."},
    "Light Screen": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "TM16", "Description": "Halves damage from Special attacks for 5 turns."},
    "Lovely Kiss": {"Type": "Normal", "Power": 0, "Accuracy": 75, "PP": 10, "TM/HM": "", "Description": "Puts opponent to sleep."},
    "Low Kick": {"Type": "Fighting", "Power": 0, "Accuracy": 90, "PP": 20, "TM/HM": "", "Description": "The heavier the opponent, the stronger the attack."},
    "Meditate": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Raises user's attack by 1."},
    "Mega Drain": {"Type": "Grass", "Power": 40, "Accuracy": 100, "PP": 10, "TM/HM": "TM21", "Description": "User recovers half of damage inflicted on opponent."},
    "Mega Kick": {"Type": "Normal", "Power": 120, "Accuracy": 75, "PP": 5, "TM/HM": "", "Description": "No additional effect."},
    "Mega Punch": {"Type": "Normal", "Power": 80, "Accuracy": 85, "PP": 20, "TM/HM": "TM01", "Description": "No additional effect."},
    "Metronome": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM35", "Description": "Waggles a finger and uses any move in the game."},
    "Mimic": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM31", "Description": "Copies the opponent's last move."},
    "Minimize": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Sharply raises the user's Evasiveness."},
    "Mirror Move": {"Type": "Flying", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Counters the last move used by the opponent."},
    "Mist": {"Type": "Ice", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Prevents stat reduction for 5 turns."},
    "Night Shade": {"Type": "Ghost", "Power": 0, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "Inflicts damage equal to user's level."},
    "Pay Day": {"Type": "Normal", "Power": 40, "Accuracy": 100, "PP": 20, "TM/HM": "TM16", "Description": "A small amount of money is gained after the battle resolves."},
    "Peck": {"Type": "Flying", "Power": 35, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "No additional effect."},
    "Petal Dance": {"Type": "Grass", "Power": 120, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "User attacks for 2-3 turns but then becomes confused."},
    "Pin Missile": {"Type": "Bug", "Power": 25, "Accuracy": 95, "PP": 20, "TM/HM": "", "Description": "Hits 2-5 times in one turn."},
    "Poison Gas": {"Type": "Poison", "Power": 0, "Accuracy": 90, "PP": 40, "TM/HM": "", "Description": "Poisons the opponent."},
    "Poisonpowder": {"Type": "Poison", "Power": 0, "Accuracy": 75, "PP": 35, "TM/HM": "", "Description": "Poisons the opponent."},
    "Poison Sting": {"Type": "Poison", "Power": 15, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "May poison the opponent."},
    "Pound": {"Type": "Normal", "Power": 40, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "No additional effect."},
    "Psybeam": {"Type": "Psychic", "Power": 65, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "May confuse the opponent."},
    "Psychic": {"Type": "Psychic", "Power": 90, "Accuracy": 100, "PP": 10, "TM/HM": "TM29", "Description": "May lower the opponent's Special Defense."},
    "Psywave": {"Type": "Psychic", "Power": 0, "Accuracy": 80, "PP": 15, "TM/HM": "", "Description": "Inflicts damage 50-150% of user's level."},
    "Quick Attack": {"Type": "Normal", "Power": 40, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "User attacks first."},
    "Rage": {"Type": "Normal", "Power": 20, "Accuracy": 100, "PP": 20, "TM/HM": "TM20", "Description": "Increases user's Attack after being hit."},
    "Razor Leaf": {"Type": "Grass", "Power": 55, "Accuracy": 95, "PP": 25, "TM/HM": "", "Description": "High critical hit ratio."},
    "Razor Wind": {"Type": "Normal", "Power": 80, "Accuracy": 100, "PP": 10, "TM/HM": "TM02", "Description": "Charges on first turn, attacks on second."},
    "Recover": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "User recovers half its max HP."},
    "Reflect": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "TM33", "Description": "Halves damage from Physical attacks for 5 turns."},
    "Rest": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM44", "Description": "User sleeps for 2 turns, but user is fully healed."},
    "Roar": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "In wild battles, the opponent flees."},
    "Rock Slide": {"Type": "Rock", "Power": 75, "Accuracy": 90, "PP": 10, "TM/HM": "", "Description": "May cause flinching."},
    "Rock Throw": {"Type": "Rock", "Power": 50, "Accuracy": 90, "PP": 15, "TM/HM": "", "Description": "No additional effect."},
    "Rolling Kick": {"Type": "Fighting", "Power": 60, "Accuracy": 85, "PP": 15, "TM/HM": "", "Description": "May cause flinching."},
    "Sand Attack": {"Type": "Ground", "Power": 0, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "Lowers the opponent's accuracy."},
    "Scratch": {"Type": "Normal", "Power": 40, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "No additional effect."},
    "Screech": {"Type": "Normal", "Power": 0, "Accuracy": 85, "PP": 40, "TM/HM": "", "Description": "Sharply lowers the opponent's Defense."},
    "Seismic Toss": {"Type": "Fighting", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Inflicts damage equal to user's level."},
     "Selfdestruct": {"Type": "Normal", "Power": 200, "Accuracy": 100, "PP": 5, "TM/HM": "TM36", "Description": "User faints, but does massive damage."},
    "Sharpen": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Raises the user's Attack by 1 stage."},
    "Sing": {"Type": "Normal", "Power": 0, "Accuracy": 55, "PP": 15, "TM/HM": "", "Description": "Causes the opponent to fall asleep."},
    "Skull Bash": {"Type": "Normal", "Power": 130, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "Raises Defense on first turn, attacks on second."},
    "Sky Attack": {"Type": "Flying", "Power": 140, "Accuracy": 90, "PP": 5, "TM/HM": "TM43", "Description": "Charges on first turn, attacks on second. May cause flinching."},
    "Slam": {"Type": "Normal", "Power": 80, "Accuracy": 75, "PP": 20, "TM/HM": "", "Description": "No additional effect."},
    "Slash": {"Type": "Normal", "Power": 70, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "High critical hit ratio."},
    "Sleep Powder": {"Type": "Grass", "Power": 0, "Accuracy": 75, "PP": 15, "TM/HM": "", "Description": "Causes the opponent to fall asleep."},
    "Sludge": {"Type": "Poison", "Power": 65, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "May poison the opponent."},
    "Smog": {"Type": "Poison", "Power": 30, "Accuracy": 70, "PP": 20, "TM/HM": "", "Description": "May poison the opponent."},
    "Smokescreen": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Lowers the opponent's accuracy."},
    "Softboiled": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM41", "Description": "User recovers half its max HP."},
    "Solar Beam": {"Type": "Grass", "Power": 120, "Accuracy": 100, "PP": 10, "TM/HM": "TM22", "Description": "Charges on first turn, attacks on second."},
    "Sonic Boom": {"Type": "Normal", "Power": 0, "Accuracy": 90, "PP": 20, "TM/HM": "", "Description": "Always inflicts 20 HP."},
    "Spike Cannon": {"Type": "Normal", "Power": 20, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "Hits 2-5 times in one turn."},
    "Splash": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Doesn't do ANYTHING."},
    "Spore": {"Type": "Grass", "Power": 0, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "Causes the opponent to fall asleep."},
    "Stomp": {"Type": "Normal", "Power": 65, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "May cause flinching."},
    "Strength": {"Type": "Normal", "Power": 80, "Accuracy": 100, "PP": 15, "TM/HM": "HM04", "Description": "No additional effect."},
    "String Shot": {"Type": "Bug", "Power": 0, "Accuracy": 95, "PP": 40, "TM/HM": "", "Description": "Sharply lowers the opponent's Speed."},
    "Struggle": {"Type": "Normal", "Power": 50, "Accuracy": 100, "PP": 1, "TM/HM": "", "Description": "Only usable when all PP are gone. Hurts the user."},
    "Stun Spore": {"Type": "Grass", "Power": 0, "Accuracy": 75, "PP": 30, "TM/HM": "", "Description": "Paralyzes the opponent."},
    "Submission": {"Type": "Fighting", "Power": 80, "Accuracy": 80, "PP": 25, "TM/HM": "TM17", "Description": "User receives recoil damage."},
    "Substitute": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "TM50", "Description": "Uses HP to creates a decoy that takes hits."},
    "Super Fang": {"Type": "Normal", "Power": 0, "Accuracy": 90, "PP": 10, "TM/HM": "", "Description": "Cuts the opponent's HP in half."},
    "Supersonic": {"Type": "Normal", "Power": 0, "Accuracy": 55, "PP": 20, "TM/HM": "", "Description": "Confuses the opponent."},
    "Surf": {"Type": "Water", "Power": 90, "Accuracy": 100, "PP": 15, "TM/HM": "HM03", "Description": "Hits all adjacent Pokémon."},
    "Swift": {"Type": "Normal", "Power": 60, "Accuracy": 100, "PP": 20, "TM/HM": "TM39", "Description": "Ignores Accuracy and Evasiveness."},
    "Swords Dance": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "TM03", "Description": "Greatly raises the user's Attack."},
    "Tackle": {"Type": "Normal", "Power": 40, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "No additional effect."},
    "Tail Whip": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "Lowers the opponent's Defense."},
    "Take Down": {"Type": "Normal", "Power": 90, "Accuracy": 85, "PP": 20, "TM/HM": "", "Description": "User receives recoil damage."},
    "Teleport": {"Type": "Psychic", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Allows user to flee wild battles; no effect in trainer battles."},
    "Thrash": {"Type": "Normal", "Power": 120, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "User attacks for 2-3 turns but then becomes confused."},
    "Thunder": {"Type": "Electric", "Power": 110, "Accuracy": 70, "PP": 10, "TM/HM": "TM25", "Description": "May paralyze opponent. Hits Pokémon using Fly/Bounce with double power."},
    "Thunder Punch": {"Type": "Electric", "Power": 75, "Accuracy": 100, "PP": 15, "TM/HM": "", "Description": "May paralyze opponent."},
    "Thunder Shock": {"Type": "Electric", "Power": 40, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "May paralyze opponent."},
    "Thunder Wave": {"Type": "Electric", "Power": 0, "Accuracy": 90, "PP": 20, "TM/HM": "TM45", "Description": "Paralyzes opponent."},
    "Thunderbolt": {"Type": "Electric", "Power": 90, "Accuracy": 100, "PP": 15, "TM/HM": "TM24", "Description": "May paralyze opponent."},
    "Toxic": {"Type": "Poison", "Power": 0, "Accuracy": 90, "PP": 10, "TM/HM": "TM06", "Description": "Badly poisons the opponent."},
    "Transform": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 10, "TM/HM": "", "Description": "User takes on the form and attacks of the opponent."},
    "Tri Attack": {"Type": "Normal", "Power": 80, "Accuracy": 100, "PP": 10, "TM/HM": "TM49", "Description": "May paralyze, burn, or freeze opponent."},
    "Twineedle": {"Type": "Bug", "Power": 25, "Accuracy": 100, "PP": 20, "TM/HM": "", "Description": "Hits twice in one turn. May poison opponent."},
    "Vice Grip": {"Type": "Normal", "Power": 55, "Accuracy": 100, "PP": 30, "TM/HM": "", "Description": "No additional effect."},
    "Vine Whip": {"Type": "Grass", "Power": 45, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "No additional effect."},
    "Water Gun": {"Type": "Water", "Power": 40, "Accuracy": 100, "PP": 25, "TM/HM": "", "Description": "No additional effect."},
    "Waterfall": {"Type": "Water", "Power": 80, "Accuracy": 100, "PP": 15, "TM/HM": "HM07", "Description": "May cause flinching."},
    "Whirlwind": {"Type": "Normal", "Power": 0, "Accuracy": 100, "PP": 20, "TM/HM": "TM04", "Description": "Wild Pokémon flee from battle after use."},
    "Wing Attack": {"Type": "Flying", "Power": 35, "Accuracy": 100, "PP": 35, "TM/HM": "", "Description": "Attacks the opponent."},
    "Withdraw": {"Type": "Water", "Power": 0, "Accuracy": 100, "PP": 40, "TM/HM": "", "Description": "Raises the user's defense by 1."},
    "Wrap": {"Type": "Normal", "Power": 15, "Accuracy": 85, "PP": 15, "TM/HM": "", "Description": "Attacks for 2-5 turns; opponent cannot move until Wrap finishes."}
}