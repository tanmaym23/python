print("welcome to tip calculator")
amount=float(input("what is your total bill? $"))
tip=int(input("what percentage of tip would u live to give? 7, 10, 12, 15"))
people=int(input("how many people to split the bill?"))
a=(amount+(amount*(tip/100)))/people
final=round(a,2)
print(final)