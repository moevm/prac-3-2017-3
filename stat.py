# -*- coding: utf-8 -*-
import csv
import argparse
import datetime
NEWLINE = ''
SEMICOLON = ';'
PERCENT = '%'
INPUT_FILE = 'sourse.csv'
OUTPUT_FILE = 'programming_{}.csv'
TABLE_ONE = ['таблица 1']
TABLE_TWO = ['таблица 2']
TABLE_THREE = ['таблица 3']
TABLE_FOUR = ['таблица 4']
USER_ID = 'id'
LAST_NAME = 'Фамилия'
FIRST_NAME = 'Имя'
TOTAL = 'Баллы'
PERCENTAGE_OF_TOTAL = '% от общего числа'
SCORED_0_POINTS = ['Студенты, которые набрали 0 баллов']
SCORED_MAX_SCORE = ['Студенты, которые набрали максимальный балл']
LESS_40_PERCENT = 'Количество студентов, набравших < 40 %;{}'
MORE_40_LESS_70_PERCENT = 'Количество студентов, набравших > 39% и < 71%;{}'
MORE_70_PERCENT = 'Количество студентов, набравших > 70%;{}'

def pars():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--max', type=int, nargs=1, help='Max Score')
    parser.add_argument('-n', '--name', nargs=1, help='Module Name')
    max_score = parser.parse_args()
    module_name = parser.parse_args()
    return max_score.max[0], module_name.name

def read_file():
    output_file = open(OUTPUT_FILE.format(str(datetime.datetime.now().strftime('%d %B'))), 'wb')
    wrtr = csv.writer(output_file)
    return wrtr, output_file

def close_file(output_file):
    output_file.close()

def filling_table():
    user_id = []
    last_name = []
    first_name = []
    total = []
    input_file = open(INPUT_FILE, 'rb')
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
                if i == SEMICOLON:
                    flag_id = bool(0)
                    flag_last = bool(1)
                    continue
                else :
                    id += i
            if flag_last:
                if i == SEMICOLON:
                    flag_last = bool(0)
                    flag_first = bool(1)
                    continue
                else:
                    last += i
            if flag_first:
                if i == SEMICOLON:
                    flag_first = bool(0)
                    flag_total = bool(1)
                    continue
                else:
                    first += i
            if flag_total:
                if i == SEMICOLON:
                    flag_id = bool(0)
                else:
                    tot += i
        user_id.append(id)
        last_name.append(last)
        first_name.append(first)
        total.append(tot)

    input_file.close()
    return user_id, last_name, first_name, total

def summary_table(wrtr, user_id, last_name, first_name, total, value):
    myTable = NEWLINE
    myTable += USER_ID
    myTable += SEMICOLON
    myTable += LAST_NAME
    myTable += SEMICOLON
    myTable += FIRST_NAME
    myTable += SEMICOLON
    myTable += TOTAL
    myTable += SEMICOLON
    myTable += PERCENTAGE_OF_TOTAL
    myTable += SEMICOLON
    wrtr.writerow([myTable])

    for i in range(0, len(user_id)):
        myTable = NEWLINE
        myTable += user_id[i]
        myTable += SEMICOLON
        myTable += last_name[i]
        myTable += SEMICOLON
        myTable += first_name[i]
        myTable += SEMICOLON
        myTable += total[i]
        myTable += SEMICOLON
        myTable += str(int(total[i]) * 100 / value)
        myTable += PERCENT
        wrtr.writerow([myTable])

def number_points(wrtr, user_id, last_name, first_name, total, value):
    for i in range(0, len(user_id)):
        if int(total[i]) == value:
            myTable = ''
            myTable += user_id[i]
            myTable += SEMICOLON
            myTable += last_name[i]
            myTable += SEMICOLON
            myTable += first_name[i]

            wrtr.writerow([myTable])

def percentage(wrtr, total, max_value):
    count_one = 0
    count_two = 0
    count_three = 0
    for i in range(0, len(total)):
        if int(total[i]) * 100 / max_value < 40:
            count_one += 1
        if 40 <= int(total[i]) * 100 / max_value <= 70:
            count_two += 1
        if int(total[i]) * 100 / max_value > 70:
            count_three += 1
    wrtr.writerow([LESS_40_PERCENT.format(count_one)])
    wrtr.writerow([MORE_40_LESS_70_PERCENT.format(count_two)])
    wrtr.writerow([MORE_70_PERCENT.format(count_three)])

def first_table(wrtr, module_name, max_score, user_id, last_name, first_name, total):
    wrtr.writerow(module_name)
    wrtr.writerow(NEWLINE)
    wrtr.writerow(TABLE_ONE)
    if __name__ == '__main__':
        summary_table(wrtr, user_id, last_name, first_name, total, max_score)

def second_table(wrtr, user_id, last_name, first_name, total):
    wrtr.writerow(NEWLINE)
    wrtr.writerow(TABLE_TWO)
    wrtr.writerow(SCORED_0_POINTS)
    if __name__ == '__main__':
        number_points(wrtr, user_id, last_name, first_name, total, 0)

def third_table(wrtr, user_id, last_name, first_name, total, max_score):
    wrtr.writerow(NEWLINE)
    wrtr.writerow(TABLE_THREE)
    wrtr.writerow(SCORED_MAX_SCORE)
    if __name__ == '__main__':
        number_points(wrtr, user_id, last_name, first_name, total, max_score)

def fourth_table(wrtr, total, max_score):
    wrtr.writerow(NEWLINE)
    wrtr.writerow(TABLE_FOUR)
    if __name__ == '__main__':
        percentage(wrtr, total, max_score)

def main():
    if __name__ == '__main__':
        max_score, module_name = pars()
        wrtr, output_file = read_file()
        user_id, last_name, first_name, total = filling_table()
        first_table(wrtr, module_name, max_score, user_id, last_name, first_name, total)
        second_table(wrtr, user_id, last_name, first_name, total)
        third_table(wrtr, user_id, last_name, first_name, total, max_score)
        fourth_table(wrtr, total, max_score)
        close_file(output_file)

if __name__ == '__main__':
    main()

'''if __name__ == '__main__':
    max_score, module_name = pars()
    wrtr, output_file = read_file()
    user_id, last_name, first_name, total = filling_table()
    first_table()
    second_table()
    third_table()
    fourth_table()
    close_file()'''