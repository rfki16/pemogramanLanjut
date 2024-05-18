str_input = input("Masukan nilai anda : ")

grade = int(str_input)

if grade == 100:
    print("Perfect")
elif grade >= 85:
    print("Good Job")
elif grade >= 70:
    print("Passed the exam")