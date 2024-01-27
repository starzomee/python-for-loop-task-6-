expenese = [2100 , 2300  , 3200 , 2700 , 2950]

total = sum(expenese)
print(total)

# lets do it using for loop

total_value = 0 
for item in expenese:
    total_value += item
print(total_value)

#...........................................................
"""After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

Using for loop figure out how many times you got heads"""
count = 0 
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

for items in result:
    if items == 'heads':
        count += 1
    print("head count is :" , count) 



# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1 , 11):
    if i % 2 == 0 :
        continue
    print(i*i)


# .............................................
# 3. # 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

def get_month(amount):
    for i in range(len(month_list)):
        if amount == expense_list[i]:
            return month_list[i]
    return "Not Found"

amount = int(input("Enter the expense amount: "))
print(f"The expense occurred in the month: {get_month(amount)}")
    
