# Project - QAP 5
# Author - Cody Fisher
# Date - 08/21/2021, 09/12/2021,
# Purpose - To calculate insurance premiums for One Stop Insurance Company and save them to a data file which can
# be displayed for future reference

# Imports
import datetime
import time

# Program loop
while True:

    # OSICDef.dat file read
    f = open('OSICDef.dat', 'r')
    POLICYNUMBER = int(f.readline())
    BASICPREMIUM = float(f.readline())
    CARDISCOUNT = float(f.readline())
    EXTRALIABILITY = float(f.readline())
    GLASSCOVERAGE = float(f.readline())
    LOANERCAR = float(f.readline())
    HST = float(f.readline())
    PROCESSINGFEE = float(f.readline())
    f.close()

    # Policy Date
    Now = datetime.datetime.now()
    PolicyDate = Now.strftime('%d-%b-%y')

    # Inputs
    while True:
        CustFirst = input('First Name: ')
        if CustFirst == '':
            print('Cannot leave blank..')
        else:
            break
    CustFirst = CustFirst.title()

    while True:
        CustLast = input('Last Name: ')
        if CustLast == '':
            print('Cannot leave blank..')
        else:
            break
    CustLast = CustLast.title()

    while True:
        Street = input('Street: ')
        if Street == '':
            print('Cannot leave blank..')
        else:
            break
    Street = Street.title()

    while True:
        City = input('City: ')
        if City == '':
            print('Cannot leave blank..')
        else:
            break
    City = City.capitalize()

    while True:
        Province = input('Province: ')
        if Province == '':
            print('Must enter a province abbreviations (ie: NL, ON, NS, ect...')
        elif len(Province) != 2:
            print('Must enter a province abbreviations (ie: NL, ON, NS, ect...')
        elif Province.upper() == 'ON':
            break
        elif Province.upper() == 'NL':
            break
        elif Province.upper() == 'PE':
            break
        elif Province.upper() == 'NS':
            break
        elif Province.upper() == 'NB':
            break
        elif Province.upper() == 'QC':
            break
        elif Province.upper() == 'MB':
            break
        elif Province.upper() == 'SK':
            break
        elif Province.upper() == 'AB':
            break
        elif Province.upper() == 'BC':
            break
        elif Province.upper() == 'YT':
            break
        elif Province.upper() == 'NT':
            break
        elif Province.upper() == 'NU':
            break
        else:
            print('Must Enter a Province Abbreviations (ie: NL, ON, NS, ect...')

    while True:
        Postal = input('Postal code: ')
        if len(Postal) != 6:
            print('Postal code must be 6 characters long')
        elif Postal == '':
            print('Cannot leave blank..')
        else:
            break

    while True:
        Phone = input('Phone number: ')
        if len(Phone) != 10:
            print('Invalid phone number.. 10 digit number please. ')
        elif Phone == '':
            print('Cannot leave blank')
        else:
            break

    while True:
        CarsInsured = input('Number of cars insured: ')
        if CarsInsured.isdigit() is False:
            print('Value entered is not a number.')
        else:
            break
    CarsInsured = int(CarsInsured)

    while True:
        ExtraLiability = input('Would you like extra liability? [Y or N]: ')
        if ExtraLiability.upper() == 'Y':
            break
        elif ExtraLiability.upper() == 'N':
            break
        else:
            print('Must enter Y or N..')

    while True:
        GlassCoverage = input('Would you like glass coverage? [Y or N]: ')
        if GlassCoverage.upper() == 'Y':
            break
        elif GlassCoverage.upper() == 'N':
            break
        else:
            print('Y for Yes and N for No please.')

    while True:
        LoanerCar = input('Would you like a loaner car? [Y or N]: ')
        if LoanerCar.upper() in 'Y':
            break
        elif LoanerCar.upper() in 'N':
            break
        else:
            print('Y for Yes and N for No please.')

    while True:
        PayWay = input('Would you like to pay in full or monthly? [F or M]: ')
        if PayWay.upper() in 'F':
            break
        elif PayWay.upper() in 'M':
            break
        else:
            print('F for full and M for Monthly please.')

    # Uppercase
    ExtraLiability = ExtraLiability.upper()
    GlassCoverage = GlassCoverage.upper()
    LoanerCar = LoanerCar.upper()
    PayWay = PayWay.upper()

    # Loops
    if ExtraLiability == 'Y':
        LiabilityCost = EXTRALIABILITY
    else:
        LiabilityCost = 0

    if GlassCoverage == 'Y':
        GlassCost = GLASSCOVERAGE
    else:
        GlassCost = 0

    if LoanerCar == 'Y':
        LoanerCost = LOANERCAR
    else:
        LoanerCost = 0

    # Calculations
    CarsForCost = CarsInsured - 1
    DiscountCarCost = BASICPREMIUM - (BASICPREMIUM * CARDISCOUNT)
    InsurancePremium = BASICPREMIUM + (CarsForCost * DiscountCarCost)
    ExtraCost = (LiabilityCost + GlassCost + LoanerCost) * CarsInsured
    TotalPremium = InsurancePremium + ExtraCost
    Hst = TotalPremium * HST
    TotalCost = TotalPremium + Hst

    # Loops after calculations
    TotalCostCalc = 0
    if PayWay == 'F':
        TotalCostCalc = TotalCost
    else:
        TotalCostCalc = TotalCost + PROCESSINGFEE

    if PayWay == 'F':
        PaymentSchedule = TotalCost
    else:
        PaymentSchedule = (TotalCost + PROCESSINGFEE) / 12

    if PayWay.upper() == 'F':
        Payment = 'Full'
    else:
        Payment = 'Monthly'

    if ExtraLiability.upper() == 'Y':
        ExtraLia = 'Yes'
    else:
        ExtraLia = 'No'

    if GlassCoverage.upper() == 'Y':
        GlassCov = 'Yes'
    else:
        GlassCov = 'No'

    if LoanerCar.upper() == 'Y':
        Loaner = 'Yes'
    else:
        Loaner = 'No'

    # Bonus.. To find the day of first payment
    # Datetime Conversions
    TodayDay = Now.strftime('%d')
    TodayMonth = Now.strftime('%m')
    TodayYear = Now.strftime('%Y')
    FirstPaymentDay = 1

    # Conversions to integers
    TodayDay = int(TodayDay)
    TodayMonth = int(TodayMonth)
    TodayYear = int(TodayYear)

    # Loops for first payment day
    if TodayDay <= 25:
        FirstPaymentMonth = TodayMonth + 1
    else:
        FirstPaymentMonth = TodayMonth + 2

    if FirstPaymentMonth == 13:
        FirstPaymentMonth = 1
        FirstPaymentYear = TodayYear + 1
    elif FirstPaymentMonth == 14:
        FirstPaymentMonth = 2
        FirstPaymentYear = TodayYear + 1
    else:
        FirstPaymentYear = TodayYear

    FirstPaymentDateO = datetime.datetime(FirstPaymentYear, FirstPaymentMonth, FirstPaymentDay)

    # Policy number format
    PolicyNum = '{}-{}{}'.format(POLICYNUMBER, CustFirst[0], CustLast[0])

    # Formatting
    CustName = '{} {}'.format(CustFirst, CustLast)
    PhoneNumber = "(" + Phone[0:3] + ") " + Phone[3:6] + "-" + Phone[6:]
    DiscountCarCost = '${:,.2f}'.format(DiscountCarCost)
    InsurancePremiumFor = '${:,.2f}'.format(InsurancePremium)
    ExtraCostFor = '${:,.2f}'.format(ExtraCost)
    TotalPremiumFor = '${:,.2f}'.format(TotalPremium)
    HstFor = '${:,.2f}'.format(Hst)
    TotalCostFor = '${:,.2f}'.format(TotalCostCalc)
    FirstPayment = FirstPaymentDateO.strftime('%d-%b-%y')
    PaymentScheduleFormat = '${:,.2f}'.format(PaymentSchedule)
    ProcessingFeeFormat = '${:,.2f}'.format(PROCESSINGFEE)

    # Padding
    CustNamePad = '{:>27}'.format(CustName)
    FirstPaymentPad = '{:>18}'.format(FirstPayment)
    PolicyDatePad = '{:>19}'.format(PolicyDate)
    StreetPad = '{:>25}'.format(Street)
    CityPad = '{:>27}'.format(City)
    CarsInsuredPad = '{:>19}'.format(CarsInsured)
    ExtraLiaPad = '{:>3}'.format(ExtraLia)
    GlassCovPad = '{:>3}'.format(GlassCov)
    LoanerPad = '{:>3}'.format(Loaner)
    PaymentPad = '{:>24}'.format(Payment)
    InsurancePad = '{:>16}'.format(InsurancePremiumFor)
    ExtraCostPad = '{:>20}'.format(ExtraCostFor)
    TotalPremiumPad = '{:>21}'.format(TotalPremiumFor)
    HstPad = '{:>28}'.format(HstFor)
    TotalCostPad = '{:>26}'.format(TotalCostFor)
    PaymentSchedulePad = '{:>9}'.format(PaymentScheduleFormat)
    ProcessingFeePad = '{:>17}'.format(ProcessingFeeFormat)

    # Printing
    print()
    print()
    print(' ' * 12, 'One Stop')
    print(' ' * 8, 'Insurance Company')
    print('-' * 34)
    print('Policy Start: ', PolicyDatePad)
    print('First Payment: ', FirstPaymentPad)
    print('Name: ', CustNamePad)
    print('Street: ', StreetPad)
    print('City: ', CityPad)
    print('Province: ', ' ' * 20, Province)
    print('Postal Code: ', ' ' * 13, Postal)
    print('Phone: ', ' ' * 11, PhoneNumber)
    print('_' * 34)
    print('Cars Insured: ', CarsInsuredPad)
    print('Extra Liability? ', ' ' * 12, ExtraLiaPad)
    print('Glass Coverage?', ' ' * 14, GlassCovPad)
    print('Loaner Car(s)? ', ' ' * 14, LoanerPad)
    print('Payment: ', PaymentPad)
    print('_' * 34)
    print('Total Insurance: ', InsurancePad)
    print('Total Extra: ', ExtraCostPad)
    print(' ' * 23, '-' * 10)
    print('Before Tax: ', TotalPremiumPad)
    print('Tax: ', HstPad)
    if PayWay.upper() == 'M':
        print('Processing Fee: ', ProcessingFeePad)
    print(' ' * 23, '-' * 10)
    print('Total: ', TotalCostPad)
    if PayWay.upper() == 'M':
        print('Monthly Payment: ', ' ' * 6, PaymentSchedulePad)
    print('-' * 34)

    # Data save for Policies.dat
    f = open('Policies.dat', 'a')
    f.write('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} \n'.format(PolicyNum,
            PolicyDate, CustName, Street, City, Province, Postal, PhoneNumber, CarsInsured, ExtraLiability,
            GlassCoverage, LoanerCar, PayWay, InsurancePremium, ExtraCost, TotalPremium, Hst, TotalCost,
            PaymentSchedule))
    f.close()

    # Saving notification
    print()
    print()
    print("Saving ... ", end="")
    print()
    print()
    for wait in range(1, 19):
        print('█', end=' ')
        time.sleep(.10)

    print()
    print()
    print('Policy processed and saved! ')

    # Policy number +1
    POLICYNUMBER = POLICYNUMBER + 1

    # Write back to OSICDef.dat
    f = open('OSICDef.dat', 'w')
    f.write('{}\n'.format(str(POLICYNUMBER)))
    f.write('{}\n'.format(str(BASICPREMIUM)))
    f.write('{}\n'.format(str(CARDISCOUNT)))
    f.write('{}\n'.format(str(EXTRALIABILITY)))
    f.write('{}\n'.format(str(GLASSCOVERAGE)))
    f.write('{}\n'.format(str(LOANERCAR)))
    f.write('{}\n'.format(str(HST)))
    f.write('{}\n'.format(str(PROCESSINGFEE)))
    f.close()

    RunAgain = input('Would you like to make another entry? [Y or N]: ')
    if RunAgain.upper() == 'Y':
        pass
    else:
        break

# Loop for detailed report
PolicyCtr = 0
TotalPolPremium = 0
TotalPolExtraCost = 0
TotalPolTotalPremium = 0

# Date modification
Today = Now.strftime('%d-%b-%y')

# Prints before loop
print()
print('ONE STOP INSURANCE COMPANY')
print('ALL POLICY LISTINGS AS OF', Today)
print()
print('POLICY', ' ' * 1, 'CUSTOMER', ' ' * 13, 'INSURANCE', ' ' * 4, 'EXTRA', ' ' * 4, 'TOTAL')
print('NUMBER', ' ' * 1, 'NAME', ' ' * 18, 'PREMIUM', ' ' * 5, 'COSTS', ' ' * 3, 'PREMIUM')
print('=' * 66)

f = open('Policies.dat', 'r')
for Policyline in f:
    PolicyData = Policyline.split(',')
    PolNumber = PolicyData[0].strip()
    PolName = PolicyData[2].strip()
    PolPremium = float(PolicyData[13].strip())
    PolExtraCost = float(PolicyData[14].strip())
    PolTotalPremium = float(PolicyData[15].strip())
    PolicyCtr += 1
    TotalPolPremium += PolPremium
    TotalPolExtraCost += PolExtraCost
    TotalPolTotalPremium += PolTotalPremium

    # Formatting
    PolPremiumFormat = '${:,.2f}'.format(PolPremium)
    PolExtraCostFormat = '${:,.2f}'.format(PolExtraCost)
    PolTotalPremiumFormat = '${:,.2f}'.format(PolTotalPremium)

    # Padding
    PolNumberPad = '{:>7}'.format(PolNumber)
    PolNamePad = '{:<21}'.format(PolName)
    PolPremiumPad = '{:>10}'.format(PolPremiumFormat)
    PolExtraCostPad = '{:>11}'.format(PolExtraCostFormat)
    PolTotalPremiumPad = '{:>11}'.format(PolTotalPremiumFormat)

    # Prints
    print(' {} {} {} {} {}'.format(PolNumberPad, PolNamePad, PolPremiumPad,  PolExtraCostPad, PolTotalPremiumPad))

# Formatting after loop
TotalPolPremFormat = '${:,.2f}'.format(TotalPolPremium)
TotalPolExtraCostFormat = '${:,.2f}'.format(TotalPolExtraCost)
TotalPolTotalPremiumFormat = '${:,.2f}'.format(TotalPolTotalPremium)

# Padding after loop
PolicyCtrPad = '{:<3}'.format(PolicyCtr)
TotalPolPremPad = '{:>23}'.format(TotalPolPremFormat)
TotalPolExtraCostPad = '{:>11}'.format(TotalPolExtraCostFormat)
TotalPolTotalPremiumPad = '{:>11}'.format(TotalPolTotalPremiumFormat)

# Prints after loop
print('=' * 66)
print('Total Policies: {} {} {} {}'.format(PolicyCtr, TotalPolPremPad, TotalPolExtraCostPad,
                                           TotalPolTotalPremiumPad))
print()

# Loop for exception report
PolicyCtr = 0
TotalPolTotalPremium = 0
TotalPolHst = 0
TotalPolTotalCost = 0
TotalPolMonthlyPayment = 0

print()
print('ONE STOP INSURANCE COMPANY')
print('ALL MONTHLY PAYMENT POLICY LISTINGS AS OF', Today)
print()
print('POLICY', ' ', 'CUSTOMER', ' ' * 14, 'TOTAL', ' ' * 14, 'TOTAL', ' ' * 5, 'MONTHLY')
print('NUMBER', ' ', 'NAME', ' ' * 17, 'PREMIUM', ' ' * 5, 'HST', ' ' * 4, 'COST', ' ' * 5, 'PAYMENT')
print('=' * 73)

f = open('Policies.dat', 'r')
for Policyline in f:
    PolicyData = Policyline.split(',')
    PolNumber = PolicyData[0].strip()
    PolName = PolicyData[2].strip()
    PolHst = PolicyData[16].strip()
    PolTotalCost = PolicyData[17].strip()
    PolPaymentSchedule = PolicyData[18].strip()
    PolPayWay = PolicyData[12].strip()
    PolTotalPremium = float(PolicyData[15].strip())

    # Conversions
    PolHst = float(PolHst)
    PolTotalCost = float(PolTotalCost)
    PolPaymentSchedule = float(PolPaymentSchedule)

    # Formatting
    PolTotalPremiumFormat = '${:,.2f}'.format(PolTotalPremium)
    PolHstFormat = '${:,.2f}'.format(PolHst)
    PolTotalCostFormat = '${:,.2f}'.format(PolTotalCost)
    PolPaymentScheduleFormat = '${:,.2f}'.format(PolPaymentSchedule)

    # Padding
    PolNumberPad = '{:>7}'.format(PolNumber)
    PolNamePad = '{:<21}'.format(PolName)
    PolTotalPremiumPad = '{:>10}'.format(PolTotalPremiumFormat)
    PolHstPad = '{:>10}'.format(PolHstFormat)
    PolTotalCostPad = '{:>10}'.format(PolTotalCostFormat)
    PolPaymentSchedulePad = '{:>10}'.format(PolPaymentScheduleFormat)

    # Loop for print
    if PolPayWay == 'M':
        print('{} {} {} {} {} {}'.format(PolNumberPad, PolNamePad, PolTotalPremiumPad, PolHstPad, PolTotalCostPad,
                                         PolPaymentSchedulePad))
        PolicyCtr += 1
        TotalPolTotalPremium += PolTotalPremium
        TotalPolHst += PolHst
        TotalPolTotalCost += PolTotalCost
        TotalPolMonthlyPayment += PolPaymentSchedule
    else:
        pass

# Formatting after loop
TotalPolTotalPremiumFormat = '${:,.2f}'.format(TotalPolTotalPremium)
TotalPolHstFormat = '${:,.2f}'.format(TotalPolHst)
TotalPolTotalCostFormat = '${:,.2f}'.format(TotalPolTotalCost)
TotalPolMonthlyPaymentFormat = '${:,.2f}'.format(TotalPolMonthlyPayment)


# Padding after loop
PolicyCtrPad = '{:<3}'.format(PolicyCtr)
TotalPolTotalPremiumPad = '{:>20}'.format(TotalPolTotalPremiumFormat)
TotalPolHstPad = '{:>10}'.format(TotalPolHstFormat)
TotalPolTotalCostPad = '{:>10}'.format(TotalPolTotalCostFormat)
TotalPolMonthlyPaymentPad = '{:>10}'.format(TotalPolMonthlyPaymentFormat)

# Prints after loop
print('=' * 73)
print('Total Policies: {} {} {} {} {} '.format(PolicyCtrPad, TotalPolTotalPremiumPad, TotalPolHstPad,
                                               TotalPolTotalCostPad, TotalPolMonthlyPaymentPad))
print()
