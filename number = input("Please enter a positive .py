number = input("Please enter a positive integer number: ")
digits = len(number)
sum_1 = 0

if not number.isdigit() :
  print(number, "is invalid entry. Please enter a valid input.")
elif int(number) >= 0 :
  for i in range(digits) :

    sum_1 = sum_1 + int(number[i])** digits

    if sum_1 == int(number) :
      print(number, " is an Armstrong Number")
      break
    else:
      print(number, " is not an Armstrong Number"),
      break