import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
for row in contacts_list:
    full_name = " ".join(row[:3])
    full_name = full_name.strip()
    full_name = full_name.split(" ")
    for index, element in enumerate(full_name):
        if len(element) == 0:
            del full_name[index]
    while len(full_name) < 3:
        full_name = full_name + [" "]
    row[0] = full_name[0]
    row[1] = full_name[1]
    row[2] = full_name[2]
    pattern_phone = (r"(\+7|8)?[\s*]?[\(]?(\d{3})[\)]?[-\s*]?(\d{3})"
                     r"[-\s*]?(\d{2})[-\s*]?(\d{2})(\D*)(\d*)(\D*)")
    repl_phone = r"\7"
    extension = re.sub(pattern_phone, repl_phone, row[5])
    if not extension:
        repl_phone = r"+7(\2)\3-\4-\5"
    else:
        repl_phone = r"+7(\2)\3-\4-\5 доб.\7"
    row[5] = re.sub(pattern_phone, repl_phone, row[5])
updated_contacts_list = []
dict_contact_list = {}
for row in contacts_list:
    k = 0
    while k < len(row):
        row[k] = row[k].strip()
        k += 1
    key = (row[0], row[1])
    value = (row[2], row[3], row[4], row[5], row[6])
    if key not in dict_contact_list:
        dict_contact_list[key] = value
    else:
        new_value = dict_contact_list[key]
        new_value = list(new_value)
        k = 0
        while k < len(new_value):
            if len(new_value[k]) == 0:
                new_value[k] = value[k]
            k += 1
        dict_contact_list[key] = tuple(new_value)
for key, value in dict_contact_list.items():
    key = list(key)
    value = list(value)
    contact = key + value
    updated_contacts_list.append(contact)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(updated_contacts_list)
