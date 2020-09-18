age_str = input("Enter your Age: ")
age = int(age_str)

if age <= 6:
    print("Bus is free")
elif age<=12:
    print("Bus fare is 450")
elif age<=18:
    print("Bus fare is 720")
elif age<=64:
    print("Bus fare is 1200")
else:
    print("Bus is free")
    
