## Utility

Managing a large mod list on a self hosted dedicated server can be a pain. I wrote a quick python script that parses a json file and then prints a formatted list of your workshop IDs and mod IDs. This is useful for maintaining a list of all the server mods that is much easier to read and modify over time.

### Usage

Just create a json file in this directory that contains your mod information called `mods.json` and run:

```bash
python3 mod_list.py
```

The script will run and print the formatted strings you need to supply the Helm chart variables with the mods that you want.

Example mods.json file:
```json
{
    "Brita's Weapon Pack": {
        "workshop_id": 2200148440,
        "mod_id": "Brita"
    },
    "Arsenal[26] GunFighter Mod [2.0]": {
        "workshop_id": 2297098490,
        "mod_id": "Arsenal(26)GunFighter[MAIN MOD 2.0]"
    },
    "Brita's Armor Pack": {
        "workshop_id": 2460154811,
        "mod_id": "Brita_2"
    },
    "RotatorsLib": {
        "workshop_id": 2732594572,
        "mod_id": "RotatorsLib"
    },
    "86 Oshkosh P19A + Military Trailer": {
        "workshop_id": 2566953935,
        "mod_id": "86oshkoshP19A"
    },
    "Water Trailer": {
        "workshop_id": 2732639855,
        "mod_id": "rWaterTrailer;rWaterTrailerSemi"
    }
}
```

The above example also shows how to format a mod entry when the mod contains more than 1 mod ID. In that case, you need to include a `;` between the multiple mod IDs.

### Side Thoughts
I realize that the initial work to create the json file may seem like more work than just dropping all the IDs straight into mod ID and workshop ID values file for the Helm chart. However, this will make it **much easier** to make changes to your mod list, especially if it is a large list. 

Additionally, I was going to make the source `mods.json` file YAML instead as that would be quicker to build but I wanted to avoid having users install Python packages to run the script (pyyaml in this case) whereas the json library is built in.
