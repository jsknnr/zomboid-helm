#!/usr/bin/python3
import json

workshop_ids = ""
mod_ids = ""

with open("mods.json", "r") as mods_json:
    mod_data = json.load(mods_json)

for k, v in mod_data.items():
    workshop_ids += f"{v['workshop_id']};"
    mod_ids += f"{v['mod_id']};"

print("Workshop IDs:")
print(workshop_ids[:-1])
print()
print("Mod IDs:")
print(mod_ids[:-1])
