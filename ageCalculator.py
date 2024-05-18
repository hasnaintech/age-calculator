# Program to find an age of a person
import datetime 

def main():
    birth_year = int(input("Your birth year: "))
    birth_month = int(input("Your birth month: "))
    birth_date = int(input("Your birth date: "))

    # Calculation
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    current_date = today.day
    
    # age = current_year - birth_year

    dob = datetime.date(birth_year, birth_month, birth_date)
    age = today - dob

    age_years = age.days // 365
    age_months = (age.days % 365) // 30
    age_days = (age.days % 365) % 30

    # Output
    print("You are", age_years, "years,", age_months, "months, and", age_days, "days old!")

    if age_years > 12 and age_years < 20:
        print("Hello teen!")

    if age_years > 3 and age_years < 5:
        print("You should start talking soon!")

    if age_years > 0 and age_years < 3:
        print("Hello, you must be the baby's guardian! :)")

    if age_years > 60:
        print("You are too old to work!")

    if age_years > 100:
        print("You must have died!")

if __name__ == "__main__":
    main()