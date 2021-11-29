import list
import test

def binary_search(arr, val):
    start = 0  # Starting point of the list
    end = len(arr)-1  # Ending point of the list

    while start < end:
        middle = (start + end)//2
        print("Start: " + str(start))
        print("End: " + str(end))
        print("Middle: " + str(middle))
        if arr[middle] >= val:
            end = middle
        else:
            start = middle + 1
    return start


def show(arr):
    for i in arr:
         print(i)


if __name__ == '__main__':
    print("  _   __   _____    _____     ____    _   _   ______ ")
    print(" (_) / /  |  __ \  |  __ \   / __ \  | \ | | |  ____|")
    print("    / /   | |__) | | |__) | | |  | | |  \| | | |__   ")
    print("   / /    |  ___/  |  _  /  | |  | | | . ` | |  __|  ")
    print("  / / _   | |      | | \ \  | |__| | | |\  | | |____ ")
    print(" /_/ (_)  |_|      |_|  \_\  \____/  |_| \_| |______|")

    print('╔══════════════════════════════════════════════════════╗')
    print('║ Fill up your Details:                                ║')
    print('╚══════════════════════════════════════════════════════╝')

    row = [1,"Darpan Kant",31,"Male","NULL","Thinness (< 18.5)","No","Former",6,1,1,2,"Yes","Yes","No","Yes","No"]
    # 1. NAME:
    name = input("Enter Your Name:")
    print('══════════════════════════════════════════════════════')
    # 2. AGE
    age = input("Enter Your Age:")
    print('══════════════════════════════════════════════════════')
    # 3. GENDER
    gender_option = int(input("Choose your Option:\n1.Male\n2.Female\n"))
    if gender_option==1:
        gender ="Male"
    else:
        gender = "Female"
    print('══════════════════════════════════════════════════════')
    # 4. PREGRANT
    pregnant = "NULL"
    if gender_option == 2:
        pregnant_option = input("Status of Pregnacy:\n1.Yes\n2.No\n")
        if pregnant_option == 1:
            pregnant = "Yes"
        else:
            pregnant = "No"
        print('══════════════════════════════════════════════════════')
    # 5. BMI
    bmi_list = ["Thinness (< 18.5)", "Normal (18.5 - 25)", "Overweight (25 - 30)", "Obese Class I (30 - 35)",
                "Obese Class II (35 - 40)", "Obese Class III (> 40)"]
    bmi_option = input("Select BMI Category:\n1. Thinness (< 18.5)\n2. Normal (18.5 - 25)\n3. Overweight (25 - 30)\n4. Obese Class I (30 - 35)\n"
                       "5. Obese Class II (35 - 40)\n6.Obese Class III (> 40)\n")
    bmi = bmi_list[int(bmi_option)-1]
    print('══════════════════════════════════════════════════════')
    # 6. TESTED POSITIVE?
    binary =["Yes","No"]
    test_positive = binary[int(input("Tested Positive Before?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 7. SMOKE
    smoke_option = ["Yes","No","Former"];
    smoke = smoke_option[int(input("How often you Smoke?:\n1.Yes\n2.No\n3.Former\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 8. WORKOUT
    workout = int(input("Frequency of Workout/Yoga ?\nNOTE:Range=[1,6]\n"))
    print('══════════════════════════════════════════════════════')
    # 9. IMMUNE
    immune = int(input("How Strongly you believe your Immune Power is? ?\nNOTE:Range=[1,5]\n"))
    print('══════════════════════════════════════════════════════')
    # 10. SLEEP
    sleep = int(input("How Sound is your Sleep?\nNOTE:Range=[1,5]\n"))
    print('══════════════════════════════════════════════════════')
    # 11. ACTIVE
    active = int(input("How Active is your Life Style?\nNOTE:Range=[1,5]\n"))
    print('══════════════════════════════════════════════════════')
    # 12. HEART DISEASE
    heart = binary[int(input("Do you have any Heart Disease?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 13. LUNG DISEASE
    lung = binary[int(input("Do you have any Lung Disease?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 14. DIABETES PROBLEM
    diabetes = binary[int(input("Do you have any Diabetes Problem?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 15. KIDNEY PROBLEM
    kidney = binary[int(input("Do you have any Kidney Problem?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')
    # 16. DIGESTION PROBLEM
    digestion = binary[int(input("Do you have any Digestion Problem?:\n1.Yes\n2.No\n"))-1]
    print('══════════════════════════════════════════════════════')

    obj = test.MasterSheet(1,name,age,gender_option,pregnant,bmi,test_positive,smoke,workout,immune,sleep,active,heart,lung,diabetes,kidney,digestion)
    # obj = test.MasterSheet(1, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
    #                   row[12], row[13], row[14], row[15], row[16])
    print(obj.weight)

    weight_calculated = obj.weight
    prone_list = list.prone_list
    total = len(prone_list)
    print(total)

    # prone_list.sort()
    # show(prone_list)
    rank_of_input = binary_search(prone_list, weight_calculated)
    print(rank_of_input)
    print(prone_list[rank_of_input])
    prone_val = float(100-((total-rank_of_input)/total)*100)
    print(str(prone_val)+"%")