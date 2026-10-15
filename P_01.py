# Write a Program to input the basic salary of an employee
# and caclulate its gross salary according to the following
# Bsaic salary <= 10000 : HRA = 20% DA =80%
# Bsaic salary <= 20000 : HRA = 25% DA =90%
# Bsaic salary . 20000 : HRA = 30% DA =95%
#__________________________________________________________#

basic_salary = float(input("Enter the basic salary: "))

# Calculate HRA and DA based on salary tiers
if basic_salary <= 10000:
    hra = 0.20 * basic_salary
    da = 0.80 * basic_salary
elif basic_salary <= 20000:
    hra = 0.25 * basic_salary
    da = 0.90 * basic_salary
else:
    hra = 0.30 * basic_salary
    da = 0.95 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + hra + da

# Display the result
print("HRA: {hra}")
print("DA: {da}")
print("Gross Salary: {gross_salary}")
