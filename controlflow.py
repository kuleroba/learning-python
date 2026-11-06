# progrsm to check if s number is even or odd
number=int(input("enter the number"))
if number%2==0:
    print(f"{number} is even number")

else:
    print(f"{number} is odd number")

    # program to check elegibility to vote

    age=int(input("enter your age"))
    if age>=18:
        print("eligible to vote")
    else:
        print("you are not eligible to vote")

        # if elif else

        # program to check grades

        grade=int(input("enter your grade"))
        if grade>=70:
            print("you score is A")

        elif grade>=60:
            print("score is B")
        elif grade>=50:
            print("score is C")
        else:
            print("score is D")
