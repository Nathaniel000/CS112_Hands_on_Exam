pili = eval(input("Enter the number you want to convert to:"))
print()
you_pili = eval(input("Press [1] to convert to Binary Number\n" 
                      "Press [2] to convert to Octal Number\n" 
                      "Press [3] to convert to Hexadecimal Number\n" 
                      "In what value would you like to convert your number?"))

if you_pili == 1:
    decimal_bin = format(pili, "b")
    print()
    print(f"The binary value of {pili} is {decimal_bin}.")

elif you_pili == 2:
    decimal_oc = format(pili, "o")
    print()
    print(f"The octal value of {pili} is {decimal_oc}.")

elif you_pili == 3:
    decimal_hex = format(pili, "x")
    print()
    print(f"The hexadecimal value of {pili} is", decimal_hex.upper())

else:
    print("Invalid input. Please try again.")
