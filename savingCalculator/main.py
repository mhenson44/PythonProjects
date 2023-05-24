#display greetings for Bob
greeting = 'Hello '
name = 'Bob'
print(greeting+name)

#Hours worked per day, week, year, an costs per week
hourly_pay = 20
hours_per_week = 40
hours_per_year = 48
cost_per_week = 400


#Calculate weekly, and yearly income/spending
weekly_income = hourly_pay * hours_per_week
yearly_income = hours_per_year * weekly_income
spend_per_year = cost_per_week*52
savings_per_year = yearly_income - spend_per_year




#Output

print("Your weekly income is: " +str(weekly_income))
print("Your yearly income is: " +str(yearly_income))
print("Your yearly spending is: " +str(spend_per_year))
print("Your yearly savings is: " +str(savings_per_year))

