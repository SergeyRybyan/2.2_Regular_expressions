import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
for row in contacts_list:
    full_name = " ".join(row[:3])
    pattern = r"\s+"
    repl = r" "
    full_name = re.sub(pattern, repl, full_name)
    full_name = full_name.strip()
    full_name = full_name.split(" ")
    while len(full_name) < 3:
        full_name = full_name + [" "]
    row[0] = full_name[0].strip()
    row[1] = full_name[1].strip()
    row[2] = full_name[2].strip()
    pattern_phone = (r"(\+7|8)?[\s*]?[\(]?(\d{3})[\)]?[-\s*]?(\d{3})"
                     r"[-\s*]?(\d{2})[-\s*]?(\d{2})")
    repl_phone = r"+7(\2)\3-\4-\5"
    row[5] = re.sub(pattern_phone, repl_phone, row[5])
    if len(row[5]) > 16:
        pattern_phone = r"(.{16})(\D*)(\d*)(\D*)"
        repl_phone = r"\1 доб.\3"
        row[5] = re.sub(pattern_phone, repl_phone, row[5])
updated_contacts_list = []
i = 0
for row in contacts_list:
    i += 1
    k = i
    if k == len(contacts_list)-1:
        break
    while k < len(contacts_list)-1:
        if row[0] == contacts_list[k][0] and row[1] == contacts_list[k][1]:
            if len(row[2]) == 0:
                row[2] = contacts_list[k][2]
            if len(row[3]) == 0:
                row[3] = contacts_list[k][3]
            if len(row[4]) == 0:
                row[4] = contacts_list[k][4]
            if len(row[5]) == 0:
                row[5] = contacts_list[k][5]
            if len(row[6]) == 0:
                row[6] = contacts_list[k][6]
            del contacts_list[k]
        k += 1
    updated_contacts_list.append(row)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(updated_contacts_list)
