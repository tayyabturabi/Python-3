percentage1 = input("Enter Your Percentage")

num_percentage = int(percentage1)

if num_percentage  > 100:
    print("Invalid")

elif num_percentage >= 90 and num_percentage <= 100:
    print("A1 Garde")

elif num_percentage >= 80 and num_percentage < 90:
    print("A Grade")

elif num_percentage >= 70 and num_percentage < 80:
    print("B Grade")

elif num_percentage >= 60 and num_percentage < 70:
    print("C Grade")
else:
    print("Fail")