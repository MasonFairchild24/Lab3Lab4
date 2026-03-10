import random

def calculate_cr(level, difficulty):
    difficulty_adjustment = {
        "easy": -2,
        "medium": -1,
        "hard": 0,
        "tpk": 1
    }

    base_cr = level + difficulty_adjustment[difficulty]
    return max(0, base_cr - 1), base_cr + 1

def encounter_builder(monsters, party_size, party_level, difficulty):
    min_cr, max_cr = calculate_cr(party_level, difficulty)

    val = []
    for m in monsters:
        if m.challenge_rating >= min_cr and m.challenge_rating <= max_cr:
            val.append(m)
    if len(val) == 0:
        print("No monsters matched CR range.")
        return []  
        
    return random.sample(val, min(len(val), party_size))