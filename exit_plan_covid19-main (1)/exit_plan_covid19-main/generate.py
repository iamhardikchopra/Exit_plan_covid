import math
import random
import numpy
from tabulate import tabulate
import csv
import nameEncyclopedia


def generate_name(gender):
    if gender == "Male":
        num1 = random.randint(0, len(nameEncyclopedia.Male) - 1)
        num2 = random.randint(0, len(nameEncyclopedia.Surname) - 1)
        name_formed = nameEncyclopedia.Male[num1] + " " + nameEncyclopedia.Surname[num2]
        return name_formed

    elif gender == "Female":
        num1 = random.randint(0, len(nameEncyclopedia.Female) - 1)
        num2 = random.randint(0, len(nameEncyclopedia.Surname) - 1)
        name_formed = nameEncyclopedia.Female[num1] + " " + nameEncyclopedia.Surname[num2]
        return name_formed


def generate_age():
    age_generated = random.randint(15,80)
    return age_generated


def generate_gender():
    age_generated = random.randint(0,1)
    return "Male" if age_generated == 1 else "Female"


def isPregnant():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


def generate_bmi():
    num = random.randint(0,4)
    bmi_list = ["Thinness (< 18.5)", "Normal (18.5 - 25)", "Overweight (25 - 30)", "Obese Class I (30 - 35)",
                "Obese Class II (35 - 40)", "Obese Class III (> 40)"]
    return bmi_list[num];


def generate_tested_positive():
    positive = random.randint(0,1)
    return "Yes" if positive == 1 else "No"

def generate_smoke_count():
    #num = random.randint(0,2)
    val = numpy.random.choice(numpy.arange(0, 3), p=[0.3, 0.2, 0.5])
    list_option = ["Yes", "No", "Former"]
    return list_option[val]
 

def generate_workout_session():
    val = numpy.random.choice(numpy.arange(1, 7), p=[0.1, 0.2, 0.2, 0.2, 0.2, 0.1])
    return val


def generate_immune_power():
    val = numpy.random.choice(numpy.arange(1, 6), p=[0.2, 0.2, 0.2, 0.2 ,0.2])
    return val


def generate_sleep_strength():
    val = numpy.random.choice(numpy.arange(1, 6), p=[0.2, 0.2, 0.2, 0.2 ,0.2])
    return val


def generate_activeness_status():
    val = numpy.random.choice(numpy.arange(1, 6), p=[0.2, 0.2, 0.2, 0.2 ,0.2])
    return val        


def generate_heart_disease():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


def generate_diabetes_disease():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


def generate_lung_disease():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


def generate_kidney_disease():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


def generate_digestion_problem():
    val = numpy.random.choice(numpy.arange(0, 2), p=[0.6, 0.4])
    return "Yes" if val == 1 else "No"


if __name__ == '__main__':

    print(' _____          _                     _   ')
    print(' |  __ \        | |                   | |  ')
    print(' | |  | |  __ _ | |_  __ _  ___   ___ | |_ ')
    print(' | |  | | / _` || __|/ _` |/ __| / _ \| __|')
    print(' | |__| || (_| || |_| (_| |\__ \|  __/| |_ ')
    print(' |_____/  \__,_| \__|\__,_||___/ \___| \__|')
    print('╔══════════════════════════════════════════════════════╗')
    print('║ Creating Environment, Please wait for a minute...    ║')
    print('║ Generating Dataset for COVID-19 Vaccination:         ║')
    print('║                                                      ║')
    print('║                                                      ║')
    print('║ DO NOT Close this window.                            ║')
    print('║ Data Generated is completely Random and based on     ║')
    print('║ Probability and Statistics:                          ║')
    print('║ Thank you for using Concept Vaccine                  ║')
    print('╚══════════════════════════════════════════════════════╝')
    print('╔══════════════════════════════════════════════════════╗')
    print('║ Choose the Value of Number of Entries:               ║')
    print('╚══════════════════════════════════════════════════════╝')

    entries_count = int(input("Enter Your Choice Here:"))

    print('╔══════════════════════════════════════════════════════╗')
    print('║ SELECT GENERATION Technique:                         ║')
    print('║ 1. Quick Dataset Generation                          ║')
    print('║ 2. Manual Dataset Generation                         ║')
    print('║ 3. Custom Template Dataset Generation                ║')
    print('║ 4. Custom Choice Dataset Generation                  ║')
    print('╚══════════════════════════════════════════════════════╝')
    choice = int(input("Enter Your Choice:"))

    file = open("dataset.txt", "w")

    l = []
    count=0
    while entries_count > count:
        count = count + 1
        p = []
        _id = count
        _age = generate_age()
        _gender = generate_gender()
        _name = generate_name(_gender)
        _bmi = generate_bmi()
        _tested_positive = generate_tested_positive()
        _smoke = generate_smoke_count()
        _workout = generate_workout_session()
        _immune = generate_immune_power()
        _sleep = generate_sleep_strength()
        _active = generate_activeness_status()
        _heart = generate_heart_disease()
        _lung = generate_lung_disease()
        _diabetes = generate_diabetes_disease()
        _kidney = generate_kidney_disease()
        _digestion = generate_digestion_problem()
        _pregnant = "NULL";
        if _gender == "Female":
            _pregnant = isPregnant()

        p.append(_id)
        p.append(_name)
        p.append(_age)
        p.append(_gender)
        p.append(_pregnant)
        p.append(_bmi)
        p.append(_tested_positive)
        p.append(_smoke)
        p.append(_workout)
        p.append(_immune)
        p.append(_sleep)
        p.append(_active)
        p.append(_heart)
        p.append(_lung)
        p.append(_diabetes)
        p.append(_kidney)
        p.append(_digestion)
        l.append(p)

    table = tabulate(l, headers=['Id','Name', 'Age', 'Gender', 'Pregnant', 'BMI', 'Tested Positive ?', 'Smoke','Workout','Immune', 'Sleep', 'Active', 'Heart?','Lung?','Diabetes?','Kidney?','Digestion'
                        ],tablefmt='pretty')
    report = "Report of Above Table is:"
    file.write(table)
    file.write(report)

    # Converting to CSV for Apllying Algorithmn
    with open('data.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
#        writer.writerow(['Id','Name', 'Age', 'Gender','Pregrant', 'BMI', 'Tested Positive ?','Heart?','Lung?','Diabetes?','Kidney?'])
        writer.writerows(l)


    print(table)
    print(report)
    file.close()
