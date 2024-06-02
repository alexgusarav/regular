from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
reg_ph_pattern = r'(8|\+7){1}\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})'
reg_phdop_pattern = r'(\s+\(*[доб.]{4}\s(\d+)\)*)+'
zamena_pattern = r'+7(\2)\3-\4-\5'
zamena_pfdop = r' доб. \2'

for con_list in contacts_list:
    if con_list[0] == 'lastname':
        continue
    con_list[5] = re.sub(reg_ph_pattern, zamena_pattern, con_list[5])
    con_list[5] = re.sub(reg_phdop_pattern, zamena_pfdop, con_list[5])
    fio = []
    if len(con_list[0].split(' ')) > 1:
        if len(con_list[0].split(' ')) == 3:
            fio = con_list[0].split(' ')
            con_list[0] = fio[0]
            con_list[1] = fio[1]
            con_list[2] = fio[2]
        if len(con_list[0].split(' ')) == 2:
            fio = con_list[0].split(' ')
            con_list[0] = fio[0]
            con_list[1] = fio[1]
    if len(con_list[1].split(' ')) > 1:
        fio = con_list[1].split(' ')
        con_list[1] = fio[0]
        con_list[2] = fio[1]

for con_list in contacts_list:
    for lnd, fnd, snd, orgd, posd, phd, emd in contacts_list:
        if con_list[0] == lnd and con_list[1] == fnd:
            if con_list[2] == '':
                con_list[2] = snd
            if con_list[3] == '':
                con_list[3] = orgd
            if con_list[4] == '':
                con_list[4] = posd
            if con_list[5] == '':
                con_list[5] = phd
            if con_list[6] == '':
                con_list[6] = emd

li = []
for i in contacts_list:
  if i not in li:
    li.append(i)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(li)
  # datawriter.writerows(contacts_list)