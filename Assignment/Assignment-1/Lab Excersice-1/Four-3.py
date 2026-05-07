marks = int(input("Enter student marks : "))
if marks>=90 and marks<=100:
    print("Grade A+")
elif marks>=70 and marks<90:
    print("Grade A")
elif marks>=60 and marks<70:
    print("Grade B+")
elif marks>=50 and marks<60:
    print("Grade B")
elif marks>=35 and marks<50:
    print("Grade C")
elif marks>=0 and marks<35:
    print("Fail")
else:
    print("Invalid marks")
    