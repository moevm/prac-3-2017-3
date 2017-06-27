# -*- coding: utf-8 -*-
import csv
import argparse
import datetime

def fillingTable(user_id, last_name, first_name, total):
    input_file = open("sourse.csv", "rb")
    rdr = csv.reader(input_file)
    next(rdr)
    for user in rdr :
        id = ''
        last = ''
        first = ''
        tot = ''
        flag_id = bool(1)
        flag_last = bool(0)
        flag_first = bool(0)
        flag_total = bool(0)

        for i in user[0]:
            if flag_id:
                if i == ';':
                    flag_id = bool(0)
                    flag_last = bool(1)
                    continue
                else :
                    id += i
            if flag_last:
                if i == ';':
                    flag_last = bool(0)
                    flag_first = bool(1)
                    continue
                else:
                    last += i
            if flag_first:
                if i == ';':
                    flag_first = bool(0)
                    flag_total = bool(1)
                    continue
                else:
                    first += i
            if flag_total:
                if i == ';':
                    flag_id = bool(0)
                else:
                    tot += i

        #print(user_id)
    #for i in range(0, len(myTable)) :
    #    print(myTable[i])
        user_id.append(id)
        last_name.append(last)
        first_name.append(first)
        total.append(tot)

    input_file.close()

def numberPoints(user_id, last_name, first_name, total, value):
    for i in range(0, len(user_id)):
        if int(total[i]) == value:
            myTable = ''
            myTable += user_id[i]
            myTable += ';'
            myTable += last_name[i]
            myTable += ';'
            myTable += first_name[i]

            wrtr.writerow([myTable])

def percentage(total, maxValue):
    count_one = 0
    count_two = 0
    count_three = 0
    for i in range(0, len(total)):
        if int(total[i]) * 100 / maxValue < 40:
            count_one += 1
        if 40 <= int(total[i]) * 100 / maxValue <= 70:
            count_two += 1
        if int(total[i]) * 100 / maxValue > 70:
            count_three += 1
    wrtr.writerow(['Количество студентов, набравших < 40 %;{}'.format(count_one)])
    wrtr.writerow(['Количество студентов набравших > 39% и < 71%;{}'.format(count_two)])
    wrtr.writerow(['Количество студентов, набравших > 70%;{}'.format(count_three)])


parser = argparse.ArgumentParser()
parser.add_argument('-m', '--max', type=int, nargs=1, help='Max Score')
parser.add_argument('-n', '--name', nargs=1, help='Module Name')
maxScore = parser.parse_args()
moduleName = parser.parse_args()

output_file = open('programming_{}.csv'.format(str(datetime.datetime.now().strftime('%d %B'))), 'wb')
wrtr = csv.writer(output_file)

user_id = []
last_name = []
first_name = []
total = []
fillingTable(user_id, last_name, first_name, total)

wrtr.writerow(moduleName.name)
wrtr.writerow(['таблица 1'])
wrtr.writerow('?')
wrtr.writerow('')
wrtr.writerow(['таблица 2'])
wrtr.writerow(['Студенты которые набрали 0 баллов'])
numberPoints(user_id, last_name, first_name, total, 0)

for i in maxScore.max:
    maxValue = i

wrtr.writerow('')
wrtr.writerow(['таблица 3'])
wrtr.writerow(['Студенты, которые набрали максимальный балл'])
numberPoints(user_id, last_name, first_name, total, maxValue)

wrtr.writerow('')
wrtr.writerow(['таблица 4'])
percentage(total, maxValue)

output_file.close()