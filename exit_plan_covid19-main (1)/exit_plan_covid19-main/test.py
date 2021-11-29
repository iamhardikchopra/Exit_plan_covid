# Importing Libaraies
import pandas as pd
import csv
from tabulate import tabulate
import time
import weights
"""
number of records
new feature: 
healthy person records
more prone record
"""

def get_prone(final):
    prone_list=[]
    for i in final:
        prone_list.append(i.weight)
    prone_list.sort()
    return prone_list


def print_table(final):
    table_list = []
    rank=1
    for i in final:
        items = []
        items.append(i.id)
        items.append(i.name)
        items.append(i.age)
        items.append(i.gender)
        items.append(i.pregrant)
        items.append(i.bmi)
        items.append(i.tested_positive)
        items.append(i.smoke)
        items.append(i.workout)
        items.append(i.immune)
        items.append(i.sleep)
        items.append(i.active)
        items.append(i.heart)
        items.append(i.lung)
        items.append(i.diabetes)
        items.append(i.kidney)
        items.append(i.digestion)
        items.append(i.weight)
        items.append(rank)
        rank = rank+1
        table_list.append(items)


    table = tabulate(table_list,
                     headers=['Id', 'Name', 'Age', 'Gender', 'Pregrant', 'BMI', 'Tested Positive ?','Smoke?','Workout?','Immune?','Sleep','Active', 'Heart?',
                              'Lung?', 'Diabetes?', 'Kidney?','Digestion?', 'Weight','Rank'
                              ], tablefmt='pretty')
    print(table)
    print()
    return


class Weight_allotment:

    def age_weight_allotment(self, age):

        if int(age) <= 4:
            return weights.ext_age * weights.age_0_4
        elif int(age) <= 17:
            return weights.ext_age * weights.age_5_17
        elif int(age) <= 29:
            return weights.ext_age * weights.age_18_29
        elif int(age) <= 39:
            return weights.ext_age * weights.age_30_39
        elif int(age) <= 49:
            return weights.ext_age * weights.age_40_49
        elif int(age) <= 64:
            return weights.ext_age * weights.age_50_64
        elif int(age) <= 74:
            return weights.ext_age * weights.age_65_74
        elif int(age) <= 84:
            return weights.ext_age * weights.age_75_84
        else:
            return weights.ext_age * weights.age_85

    def gender_weight_allotment(self, gender):

        if gender == 'Male':
            return weights.ext_gender * weights.gender_male
        else:
            return weights.ext_gender * weights.gender_female

    def bmi_weight_allotment(self, bmi):

        bmi_list = ["Thinness (< 18.5)", "Normal (18.5 - 25)", "Overweight (25 - 30)", "Obese Class I (30 - 35)", "Obese Class II (35 - 40)", "Obese Class III (> 40)"]
        if bmi == bmi_list[0]:
            return weights.ext_bmi * weights.bmi_thinner
        elif bmi == bmi_list[1]:
            return weights.ext_bmi * weights.bmi_normal
        elif bmi == bmi_list[2]:
            return weights.ext_bmi * weights.bmi_overweight
        elif bmi == bmi_list[3]:
            return weights.ext_bmi * weights.bmi_obese1
        elif bmi == bmi_list[4]:
            return weights.ext_bmi * weights.bmi_obese1

    def tested_positive_weight_allotment(self, status):

        if status == 'Yes':
            return weights.ext_tested_positive * weights.covid_yes
        elif status == 'No':
            return weights.ext_tested_positive * weights.covid_no

    def heart_weight_allotment(self, heart):

        if heart == 'Yes':
            return weights.ext_heart * weights.heart_yes
        elif heart == 'No':
            return weights.ext_heart * weights.heart_no

    def lungs_weight_allotment(self, lungs):

        if lungs == 'Yes':
            return weights.ext_lungs * weights.lungs_yes
        elif lungs == 'No':
            return weights.ext_lungs * weights.lungs_no

    def diabetes_weight_allotment(self, lungs):

        if lungs == 'Yes':
            return weights.ext_diabetes * weights.diabetes_yes
        elif lungs == 'No':
            return weights.ext_diabetes * weights.diabetes_no

    def kidney_weight_allotment(self, kidney):

        if kidney == 'Yes':
            return weights.ext_kidney * weights.kidney_yes
        elif kidney == 'No':
            return weights.ext_kidney * weights.kidney_no


class MasterSheet:
    def __init__(self, idd, name, age, gender, pregrant, bmi, tested_positive, smoke, workout, immune, sleep, active, heart, lung, diabetes, kidney, digestion):
        self.id = idd
        self.name = name
        self.age = age
        self.gender = gender
        self.pregrant = pregrant
        self.bmi = bmi
        self.tested_positive = tested_positive
        self.smoke = smoke
        self.workout = workout
        self.immune = immune
        self.sleep = sleep
        self.active = active
        self.heart = heart
        self.lung = lung
        self.diabetes = diabetes
        self.kidney = kidney
        self.digestion = digestion
        self.weight = 0
        obj = Weight_allotment()

        age_weight = obj.age_weight_allotment(self.age)
        gender_weight = obj.gender_weight_allotment(self.gender)

        bmi_weight = obj.bmi_weight_allotment(self.bmi)
        tested_positive_weight = obj.tested_positive_weight_allotment(self.tested_positive)


        heart_weight= obj.heart_weight_allotment(self.heart)
        lung_weight= obj.lungs_weight_allotment(self.lung)
        diabetes_weight= obj.diabetes_weight_allotment(self.diabetes)
        kidney_weight= obj.kidney_weight_allotment(self.kidney)
        
        x = age_weight + gender_weight + tested_positive_weight + bmi_weight + heart_weight + lung_weight + diabetes_weight + kidney_weight
        self.weight = float("{:.5f}".format(x))
        # Assigning weight as per Age

#    def calculate_weight


if __name__ == '__main__':

    print("  ______      _ _     _____  _                    _____           _     _       __  ___   ")
    print(" |  ____|    (_) |   |  __ \| |              _   / ____|         (_)   | |     /_ |/ _ \  ")
    print(" | |__  __  ___| |_  | |__) | | __ _ _ __   (_) | |     _____   ___  __| |______| | (_) | ")
    print(" |  __| \ \/ / | __| |  ___/| |/ _` | '_ \      | |    / _ \ \ / / |/ _` |______| |\__, | ")
    print(" | |____ >  <| | |_  | |    | | (_| | | | |  _  | |___| (_) \ V /| | (_| |      | |  / /  ")
    print(" |______/_/\_\_|\__| |_|    |_|\__,_|_| |_| (_)  \_____\___/ \_/ |_|\__,_|      |_| /_/   ")

    print('╔══════════════════════════════════════════════════════╗')
    print('║ Creating Environment, Please wait for a minute...    ║')
    print('║                                                      ║')
    print('║ DO NOT Close this window.                            ║')
    print('║ This Algorithm of Ranking will provide the efficient║')
    print('║ order of Vaccination.                                ║')
    print('║ This can implemented in various RURAL areas to       ║')
    print('║ reduce the mortality.                                ║')
    print('║ Thank you for using Concept Vaccine                  ║')
    print('╚══════════════════════════════════════════════════════╝')
    print('╔══════════════════════════════════════════════════════╗')
    print('║ Choose the Type of Dataset:                          ║')
    print('║ 1. Survey Conducted Dataset                          ║')
    print('║ 2. Randomized Generated Dataset                      ║')
    print('╚══════════════════════════════════════════════════════╝')
    dataset_type = int(input("Enter Your Choice Here:"))

    # TODO: option between choosing csv file or excel file
    # if dataset_type == 1:
    #     csv_file='abc.csv'
    # elif dataset_type == 2:
    #     csv_file='data.csv'
    # else:
    #     print("Opps!!Invalid Option")
    #     exit()

    final=[]
    # Reading the csv file
    # list of object
    with open('data.csv') as csv_file:
        csvReader = csv.reader(csv_file)
        for row in csvReader:
            items = []
            obj = MasterSheet(row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16])
            final.append(obj)


    # TODO: Print before sorting
    print('╔══════════════════════════════════════════════════════╗')
    print('║ Following the your Selected Dataset:                 ║')
    print('╚══════════════════════════════════════════════════════╝')

    print_table(final)
    print("Please Wait we are Evaluating the Best Results..")
    time.sleep(5)
    # TODO: Sort
    final.sort(key=lambda x : x.weight,reverse=True)
    # TODO: Print after sorting
    print_table(final)
    prone_list = get_prone(final)


    textfile = open("list.py", "w")
    textfile.write("prone_list=[")
    for element in prone_list:
        textfile.write(str(element) + ",")
    textfile.write("]")

    textfile.close()
    # with open('weights_ds.csv', 'w', newline='') as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerows(prone_list)



