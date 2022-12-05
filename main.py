import FormatValues as FV
import datetime
Today = datetime.datetime.today()

f = open("OsicDef.dat", "r")
PolicyNum = int(f.readline())
BasicPremium = float(f.readline())
AddCarDis = float(f.readline())
ExtraLiaCov = float(f.readline())
CosOfGlassCov = float(f.readline())
CosLoanCarCov = float(f.readline())
HST_RATE = float(f.readline())
MonthPayProcessFee = float(f.readline())
f.close()

while True:
    CustFN = input("Please enter the customers first name: ").title()
    CustLN = input("Please enter the customers last name: ").title()
    CustAddress = input("Please enter the customers current address: ").title()
    CustCity = input("Please enter the customers current residing city: ").title()
    CustProvince = input("Please enter the customers current residing province: ").title()
    CustPostalCode = input("Please enter the customers current postal: ")
    CustPhoneNum = input("Please enter the customers phone number (XXX-XXX-XXXX): ")
    InsureCarNum = int(input("Please enter the number of cars being insured: "))
    Liability = input("Please enter Y if the Customer wants liability coverage, enter N if not: ").upper()
    GlassCov = input("Please enter Y if the customer wants glass coverage, enter N if not: ").upper()
    LoanerCar = input("Please enter Y if the customer owns a loaned car, enter N if not: ").upper()
    PayMethod = input("Please enter the customers payment method (F for Full or M for Monthly): ").upper()

    ExtraCar = InsureCarNum - 1
    DisCarNum = BasicPremium * AddCarDis
    InsurePre = (BasicPremium * 1) + (BasicPremium - DisCarNum)*ExtraCar

    if Liability == "Y":
        LiabilityCharges = ExtraLiaCov * InsureCarNum
    else: LiabilityCharges = 0

    if GlassCov == "Y":
        GlassCovCost = CosOfGlassCov * InsureCarNum
    else:
        GlassCovCost = 0

    if LoanerCar == "Y":
        LoanerCarCost = CosLoanCarCov * InsureCarNum
    else:
        LoanerCarCost = 0

    # Print fixing
    if Liability == "Y":
        Liability = "Yes"
    else: Liability = "No"

    if GlassCov == "Y":
        GlassCov = "Yes"
    else: GlassCov = "No"

    if LoanerCar == "Y":
        LoanerCar = "Yes"
    else: LoanerCar = "No"

    TotalExtraCos = LiabilityCharges + GlassCovCost + LoanerCarCost
    TotInsurePre = InsurePre + TotalExtraCos
    HST = TotInsurePre * HST_RATE
    TotalCost = TotInsurePre + HST

    if PayMethod == "M":
        PayMethod = "Monthly"
        MonthlyPay = (TotalCost + MonthPayProcessFee) / 8
    elif PayMethod == "F":
        PayMethod = "Full"
        MonthlyPay = int()
    else:
        MonthlyPay = int()

    print(" ")
    print(" "*6, "One Stop Insurance Company")
    print(" "*6, Today)
    print("-"*40)
    print(f"Customer Name:      {CustFN} {CustLN:<24s}")
    print(f"Customer Address:   {CustAddress}")
    print(f"City:               {CustCity}")
    print(f"Province:           {CustProvince}")
    print(f"Postal Code:        {CustPostalCode}")
    print(f"Phone Number:       {CustPhoneNum}")
    print(f"-"*40)
    print(f"Cars Being Insured: {InsureCarNum}")
    print(f"Liability Coverage: {Liability}")
    print(f"Glass Coverage:     {GlassCov}")
    print(f"Loaned Car:         {LoanerCar}")
    print(f"Payment Method:     {PayMethod}")
    print(f"-"*40)
    print(f"Subtotal Cost:      {FV.FDollar2(InsurePre)}")
    print(f"-"*40)
    print(f"Extra costing:      {FV.FDollar2(TotalExtraCos)}")
    print(f"Insurance Premium:  {FV.FDollar2(TotInsurePre)}")
    print(f"HST:                {FV.FDollar2(HST)}")
    print(f"Total Costing:      {FV.FDollar2(TotalCost)}")
    print(f"Payment Method:     {PayMethod}")
    print(f"Monthly Pay Plan    {FV.FDollar2(MonthlyPay)}")

    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(PolicyNum)))
    f.write("{}, ".format(CustFN))
    f.write("{}, ".format(CustLN))
    f.write("{}, ".format(CustAddress))
    f.write("{}, ".format(CustCity))
    f.write("{}, ".format(CustProvince))
    f.write("{}, ".format(CustPostalCode))
    f.write("{}, ".format(CustPhoneNum))
    f.write("{}, ".format(str(InsureCarNum)))
    f.write("{}, ".format(Liability))
    f.write("{}, ".format(GlassCov))
    f.write("{}, ".format(LoanerCar))
    f.write("{}, ".format(PayMethod))
    f.write("{}\n ".format(str(TotInsurePre)))

    f.close()

    print(" ")
    print("Policy information processed and saved")
    PolicyNum += 1

    End = input("Would you like to make another transaction? Type end to finish, press any key to make another: ").upper()
    if End == "END":
        break

    f = open("OsicDef.dat", "w")
    f.write("{}\n ".format(str(PolicyNum)))
    f.write("{}\n ".format(str(TotInsurePre)))
    f.write("{}\n ".format(str(BasicPremium)))
    f.write("{}\n ".format(str(AddCarDis)))
    f.write("{}\n ".format(str(ExtraLiaCov)))
    f.write("{}\n ".format(str(CosOfGlassCov)))
    f.write("{}\n ".format(str(CosLoanCarCov)))
    f.write("{}\n ".format(str(HST_RATE)))
    f.write("{}\n ".format(str(MonthPayProcessFee)))
    f.close()





