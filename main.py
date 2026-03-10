from api_stuff import sample_monsters, monster_details
from monster import Monster, Action
from encounter import encounter_builder



def parse_action(api_action):
    parsed = []

    for a in api_action:
        damage_list = []
        for d in a.get("damage", []):
            dice = d.get("damage_dice")
            if dice:
                damage_list.append(dice)
        
        dc_detail = a.get("dc") or {}
        dc_type = None
        dc_value = None
        if dc_detail:
            dc_type = dc_detail.get("dc_type", {}).get("name")
            dc_value = dc_detail.get("dc_value")

        parsed.append(Action(
            name=a.get("name", "Unknown"),
            damage_dice=damage_list if damage_list else None,
            dc_type=dc_type,
            dc_value=dc_value
        ))

        
    return parsed

sampled = sample_monsters()

parsed_monsters = []

for m in sampled:
    detail = monster_details(m["index"])

    if isinstance(detail["armor_class"], list):
        detail["armor_class"] = detail["armor_class"][0]["value"]

    monster_object = Monster(
        name=detail["name"],
        hit_points=detail["hit_points"],
        armor_class=detail["armor_class"],
        challenge_rating=detail["challenge_rating"],
        actions=parse_action(detail["actions"])
    )
    parsed_monsters.append(monster_object)



party_size = int(input("Party Size: "))
party_level = int(input("Party Level: "))
difficulty = input("Difficulty (easy/medium/hard/TPK): ").lower()

encounter = encounter_builder(parsed_monsters, party_size, party_level, difficulty)




print("\n Encounter Generated:\n")

for m in encounter:
    print(f"{m.name}")
    print(f"CR: {m.challenge_rating}")
    print(f"HP: {m.hit_points}")
    print(f"AC: {m.armor_class}")

    for a in m.actions:
        dmg = ", ".join(a.damage_dice) if a.damage_dice else "No damage"
        if a.dc_value:
            print(f"  - {a.name}: {dmg} | DC {a.dc_value} {a.dc_type}")
        else:
            print(f"  - {a.name}: {dmg}")
#I had to get chat help with converting the list into a string in a proper format. It also added this horizontal line for me
    print("-" * 40)