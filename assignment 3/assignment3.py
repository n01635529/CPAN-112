year = float(input("Enter year: "))
months = float(input("Enter months: "))
days = float(input("Enter days: "))
principal = float(input("Principal: "))
rate = float(input("Rate (In %): "))

def getTime(year, months, days):
    totalYears = float(year + (months / 12) + (days / 365))
    return totalYears

def simpleInterest(totalYears, principal, rate):
    ratePercent = rate / 100
    simpleInterest = principal * ratePercent * totalYears
    return simpleInterest

def output():
    print("Total time in years is", round(getTime(year, months, days), 1), "years")
    print("Total interest earned is $", round(simpleInterest(getTime(year, months, days), principal, rate), 2))

output()