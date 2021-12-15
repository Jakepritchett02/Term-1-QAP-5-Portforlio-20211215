# Purpose: One Stop Insurance Company Policy Data Program
# Author: Jacob Pritchett
# Date: December 2021


from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")


#Defaults
f = open("OSICDef.dat","r")
POL_NUM = int(f.readline())
BASIC_PRM = float(f.readline())
EXTRA_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_CAR = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

while True:
    #Inputs
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        CustName = input("Enter the Customer Name: ")
        if CustName == "":
            print("Invalid first name - cannot be blank.")
        elif set(CustName).issubset(allowed_char) == False:
            print("Invalid first name - cannot contain invalid characters. ")
        else:
            CustName = CustName.title()

        CustAddress = input("Enter the Customers Street Address:  ")
        City = input("Enter the Customers City:  ")
        Prov = input("Enter the Customers Province:  ")
        PostCode = input("Enter the Customers Postal Code:  ")

        while True:
            CustPhoneNum = input("Enter the Customer Phone Number (9999999999): ")

            if len(CustPhoneNum) != 10:
                print("Invalid home phone - must be 10 digits.")
            elif CustPhoneNum.isdigit() == False:
                print("Invalid Phone Number  - must be 10 digits.")
            else:
                CustPhoneNum = "(" + CustPhoneNum[0:3] + ") " + CustPhoneNum[3:6] + "-" + CustPhoneNum[6:]
                break

        NumberCarInsured = int(input("Enter the Number of Additional Cars being Insured:   "))
        ExtraLiability = input("Does the Customer want Extra Liability (Y/N):  ")
        if ExtraLiability.upper() == "Y":
            ExtraLiability = EXTRA_LIABILITY
        else:ExtraLiability = 0.00
        GlassCoverage = input("Does the Customer want Glass Coverage(Y/N):  ")
        if GlassCoverage.upper() == "Y":
            GlassCoverage = GLASS_COVERAGE
        else:GlassCoverage = 0.00
        LoanerCar = input("Does the Customer want a Loaner Car(Y/N):  ")
        if LoanerCar.upper() == "Y":
            LoanerCar = LOANER_CAR
        else: LoanerCar = 0.00
        PaymentType = input("How does the Customer want to Pay (Full(F)/Monthly(M)):   ")
        PaymentType = PaymentType.upper()

    #Calculations
        ExtraCarPremiums = (NumberCarInsured * BASIC_PRM) * 0.75
        InsurancePremium = BASIC_PRM + ExtraCarPremiums
        TotalExtraCost = EXTRA_LIABILITY + GLASS_COVERAGE + LOANER_CAR
        TotalInsurancePremium = InsurancePremium + TotalExtraCost
        HST = HST_RATE * TotalInsurancePremium
        TotalCost = TotalInsurancePremium + HST
        MonthlyPayment = (TotalCost + PROCESSING_FEE)/12
        if PaymentType.upper() == "F":
            MonthlyPayment = 0.00

    #Receipt

        print()
        print("        One Stop Insurance Company")
        print("       Policy Detailed Receipt")
        print()
        print(f"Policy Issue Date:   {d1}")
        print(f"Policy No:  {POL_NUM}")
        print()
        print("Customer Information:")
        print(CustName)
        print(CustAddress)
        print(City.capitalize()+",",   Prov.upper(),   PostCode)
        print()
        print("Policy Details:")
        print()
        print(f"Basic Premium:                ${BASIC_PRM:>10,.2f}")
        print(f"Additional Vehicles Premium:  ${ExtraCarPremiums:>10,.2f}")
        print(f"Extra Liability:              ${ExtraLiability:>10,.2f}")
        print(f"Glass Coverage:               ${GlassCoverage:>10,.2f}")
        print(f"Loaner Car:                   ${LoanerCar:>10,.2f}")
        print(" "*30, "_"*10)
        print(f"SubTotal:                     ${TotalInsurancePremium:>10,.2f}")
        print(f"HST:                          ${HST:>10,.2f}")
        print(" "*30, "_"*10)
        print(f"Total Insurance Cost:         ${TotalCost:>10,.2f}")
        print()
        print(f"Monthly Payment:              ${MonthlyPayment:>10,.2f}   ")
        print()
        print("    One Stop Insurance Company")
        print("  For All Your Insurance Needs!!")
        print()

        f = open("Policies.dat", "a")
        f.write("{}, ".format(str(POL_NUM)))
        POL_NUM += 1
        f.write("{}, ".format(str(CustName)))
        f.write("{}, ".format(str(CustAddress)))
        f.write("{}, ".format(str(City)))
        f.write("{}, ".format(str(Prov)))
        f.write("{}, ".format(str(PostCode)))
        f.write("{}, ".format(str(CustPhoneNum)))
        f.write("{}, ".format(str(NumberCarInsured)))
        f.write("{}, ".format(str(ExtraLiability)))
        f.write("{}, ".format(str(GlassCoverage)))
        f.write("{}, ".format(str(LoanerCar)))
        f.write("{}, ".format(str(PaymentType)))
        f.write("{}\n".format(str(TotalCost)))
        f.close()
        print("Policy Processed and Saved")
        print()
        Continue = input("Do you want to process another Policy (Y/N)?: ")
        if Continue.upper() == "N":
            break


    f = open("OSICDef.dat", "w")
    f.write("{}\n".format(str(POL_NUM)))
    f.write("{}\n".format(str(BASIC_PRM)))
    f.write("{}\n".format(str(EXTRA_CAR_DISCOUNT)))
    f.write("{}\n".format(str(EXTRA_LIABILITY)))
    f.write("{}\n".format(str(GLASS_COVERAGE)))
    f.write("{}\n".format(str(LOANER_CAR)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PROCESSING_FEE)))
    f.close()
    print()

    # Detailed Report

    import datetime

    Today = datetime.datetime.now()

    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF {}".format(Today.strftime("%d-%b-%y")))
    print()
    print("POLICY  CUSTOMER              INSURANCE      EXTRA       TOTAL")
    print("NUMBER  NAME                   PREMIUM       COSTS      PREMIUM")
    print("="*65)


    CustCounter = 0
    f = open("Policies.dat","r")
    for PolicyLine in f:
        PolDat = PolicyLine.split(",")
        #print(PolDat)
        POL_NUM = PolDat[0]
        CustName = PolDat[1].strip()
        TotalCost = float(PolDat[12].strip())
        NumberCarInsured = int(PolDat[7].strip())
        ExtraLiability = float(PolDat[8].strip())
        GlassCoverage = float(PolDat[9].strip())
        LoanerCar = float(PolDat[10].strip())


        InsurancePremium = BASIC_PRM + (BASIC_PRM * NumberCarInsured * 0.75)
        TotalExtraCost = ExtraLiability + GlassCoverage + LoanerCar

        TotalCostStr = "${:,.2f}".format(TotalCost)
        TotalCostPad = "{:>9}".format(TotalCostStr)
        InsurancePremiumStr = "${:,.2f}".format(InsurancePremium)
        InsurancePremiumPad = "{:>9}".format(InsurancePremiumStr)
        TotalExtraCostStr = "${:,.2f}".format(TotalExtraCost)
        TotalExtraCostPad = "{:>9}".format(TotalExtraCostStr)

        print("{}    {:<20}  {}   {}     {} ".format(POL_NUM,CustName,InsurancePremiumPad,TotalExtraCostPad,TotalCostPad))
        CustCounter += 1
    f.close()


    print("="*65)
    print("Total Policies: {}".format(CustCounter))
    print()
    print()

#Exception Report

    print("ONE STOP INSURANCE COMPANY")
    print("POLICY LISTING AS OF {}".format(Today.strftime("%d-%b-%y")))
    print()
    print("POLICY  CUSTOMER                TOTAL                   TOTAL        MONTHLY")
    print("NUMBER  NAME                   PREMIUM        HST       COST         PAYMENT")
    print("="*78)

    CustCounter = 0
    TotalInsurancePremiumAcc = 0
    HSTAcc = 0
    MonthlyPaymentAcc = 0
    TotalCostAcc = 0

    f = open("Policies.dat","r")
    for PolicyLine in f:
        PolDat = PolicyLine.split(",")
        #print(PolDat)
        POL_NUM = PolDat[0]
        CustName = PolDat[1].strip()
        PaymentType = PolDat[11].strip()
        TotalCost = float(PolDat[12].strip())
        NumberCarInsured = int(PolDat[7].strip())
        ExtraLiability = float(PolDat[8].strip())
        GlassCoverage = float(PolDat[9].strip())
        LoanerCar = float(PolDat[10].strip())

        if PaymentType == "M":
            TotalExtraCost = ExtraLiability + GlassCoverage + LoanerCar
            ExtraCarPremiums = (BASIC_PRM * NumberCarInsured) * 0.75
            TotalInsurancePremium = TotalExtraCost + ExtraCarPremiums + BASIC_PRM
            HST = TotalInsurancePremium * HST_RATE
            MonthlyPayment = TotalInsurancePremium + HST
            MonthlyPayment = (TotalCost + PROCESSING_FEE) / 12

            TotalCostStr = "${:,.2f}".format(TotalCost)
            TotalCostPad = "{:>9}".format(TotalCostStr)

            TotalInsurancePremiumStr = "${:,.2f}".format(TotalInsurancePremium)
            TotalInsurancePremiumPad = "{:>9}".format(TotalInsurancePremiumStr)

            HSTStr = "${:,.2f}".format(HST)
            HSTPad = "{:>9}".format(HSTStr)

            MonthlyPaymentStr = "${:,.2f}".format(MonthlyPayment)
            MonthlyPaymentPad = "{:>9}".format(MonthlyPaymentStr)

            print("{}  {:<20}    {}   {}   {}    {} ".format(POL_NUM, CustName,TotalInsurancePremiumPad, HSTPad,TotalCostPad, MonthlyPaymentPad))

            CustCounter += 1
            TotalInsurancePremiumAcc += TotalInsurancePremium
            HSTAcc += HST
            MonthlyPaymentAcc += MonthlyPayment
            TotalCostAcc += TotalCost

            TotalInsurancePremiumAccStr = "${:,.2f}".format(TotalInsurancePremiumAcc)
            TotalInsurancePremiumAccPad = "{:>9}".format(TotalInsurancePremiumAccStr)

            HSTAccStr = "${:,.2f}".format(HSTAcc)
            HSTAccPad = "{:>9}".format(HSTAccStr)

            MonthlyPaymentAccStr = "${:,.2f}".format(MonthlyPaymentAcc)
            MonthlyPaymentAccPad = "{:>9}".format(MonthlyPaymentAccStr)

            TotalCostAccStr = "${:,.2f}".format(TotalCostAcc)
            TotalCostAccPad = "{:>9}".format(TotalCostAccStr)

    print("="*78)
    print("Total Policies:{}             {}   {}    {}    {} ".format(CustCounter,TotalInsurancePremiumPad,HSTAccPad,TotalCostAccPad,MonthlyPaymentAccPad ))
    f.close()
    break