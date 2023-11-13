#!/usr/bin/env python
import csv
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
translation_dummy_path = root.joinpath("Source/translation_dummy.cpp")
monstdat_path = root.joinpath("Packaging/resources/assets/txtdata/monsters/monstdat.tsv")
unique_monstdat_path = root.joinpath("Packaging/resources/assets/txtdata/monsters/unique_monstdat.tsv")

with open(translation_dummy_path, 'w') as temp_source:
    temp_source.write(f'/**\n')
    temp_source.write(f' * @file translation_dummy.cpp\n')
    temp_source.write(f' *\n')
    temp_source.write(f' * Do not edit this file manually, it is automatically generated\n')
    temp_source.write(f' * and updated by the extract_translation_data.py script.\n')
    temp_source.write(f' */\n')
    temp_source.write(f'#include "utils/language.h"\n')
    temp_source.write(f'\n')
    with open(monstdat_path, 'r') as tsv:
        reader = csv.DictReader(tsv, delimiter='\t')
        for row in reader:
            name = row['name']
            var_name = row['_monster_id'] + "_NAME"
            temp_source.write(f'const char *' + var_name + ' = P_("monster", "' + name + '");\n')
    with open(unique_monstdat_path, 'r') as tsv:
        reader = csv.DictReader(tsv, delimiter='\t')
        for row in reader:
            name = row['name']
            var_name = name.upper().replace(' ', '_').replace('-', '_') + "_NAME"
            temp_source.write(f'const char *' + var_name + ' = P_("monster", "' + name + '");\n')
