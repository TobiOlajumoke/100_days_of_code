age = input("What is your current age? ")

age_as_int = int(age)
days = 365 * age_as_int
weeks = 52 * age_as_int
months = 12 * age_as_int
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")