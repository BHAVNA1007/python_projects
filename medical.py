print("---------------------------------")
print("    Info Medical_Store    ")
print("---------------------------------\n")

customer = ''
password = ''

while True:
    print("          LOGIN\n")
    customer  = input("    Enter your name: ")
    password = input("    Enter your password: ")

    if customer == "Bhavna" and password == "123":
        print("\nLogin Successful")
        break
    else:
        print("\n       Login Failed")
        print("Please enter correct username and password\n")

dolo = "Dolo"
dolo_price = ''
dolo_quantity = ''
dolo_amount = 0
dolo_bill = 0
dolo_gst = 0


para = "Paracitamol"
para_price = ''
para_quantity = ''
para_amount = 0
para_bill = 0
para_gst = 0


crocin = "crocin"
crocin_price = ''
crocin_quantity = ''
crocin_amount =0
crocin_bill =0
crocin_gst = 0


aspirin = "aspirin"
aspirin_price = ''
aspirin_quantity = ''
aspirin_amount = 0
aspirin_bill = 0
aspirin_gst = 0


digene = "digene"
digene_price = ''
digene_quantity = ''
digene_amount = 0
digene_bill = 0
digene_gst = 0


customer_name = ""
customer_age = ""
customer_city = ""
customer_phone = ""

discount = 0
customer_type = ''

total = 0



while True:
    print("---------------------------------")
    print(" ***  Welcome  Menu  ***")
    print("---------------------------------\n ")

    print("01. View all Medicines and Prices")
    print("02. Buy Medicine ")
    print("03. Check Medicine stock")
    print("04. Expiry Check ")
    print("05. Customer Details")
    print("06. Discount Offers ")
    print("07. Tax/GST Calculation")
    print("08. Final Bill ")
    print("09. Exit\n")
    print("-------------------------")
    choice = int(input("    Enter your choice: "))
    print("-------------------------\n\n")
    match choice:

        case 1:
            print(" View all Medicines and Prices\n")
            print("Medicines name    $ price")

            para_price = 100
            print(f"1. {para}         {para_price}")

            dolo_price = 100
            print(f"2. {dolo}           {dolo_price}")

            crocin_price = 100
            print(f"3. {crocin}         {crocin_price}")

            aspirin_price = 100
            print(f"4. {aspirin}        {aspirin_price}")

            digene_price = 100
            print(f"5. {digene}         {digene_price}")

        case 2:
            print(" buy medicines\n")
            while True:

                print("1.dolo")
                print("2.paracitamol")
                print("3. crocin")
                print("4. aspirin")
                print("5. digene")
                print("6. Exit")
                medicine = int(input("Enter Medicine which you want to buy: "))

                match medicine:
                    case 1:
                        print("dolo added")
                        dolo_quantity = int(input("Enter quantity: "))
                    case 2:
                        print("crocin added")
                        crocin_quantity = int(input("Enter quantity: "))
                    case 3:
                        print("paracitamol added")
                        para_quantity = int(input("Enter quantity: "))
                    case 4:
                        print("aspirin added")
                        aspirin_quantity = int(input("Enter quantity: "))
                    case 5:
                        print("digene added")
                        digene_quantity = int(input("Enter quantity: "))
                    case 6:
                        print("Exit")
                        break
                    case _:
                        print("Invalid input. Please try again......")

        case 3:
            print(" Check Medicine in stock\n")
            if  dolo_quantity != "":
               if int(dolo_quantity) >= 4:
                  print("not in stock")
               else:
                  print("Available in stock")

            if crocin_quantity != "":
               if int(crocin_quantity) >= 4:
                  print("not in stock")
               else:
                  print("Available in stock")

            if para_quantity != "":
               if int(para_quantity) >= 4:
                  print("not in stock")
               else:
                  print("Available in stock")

            if aspirin_quantity != "":
               if int(aspirin_quantity) >= 4:
                  print("not in stock")
               else:
                  print("Available in stock")

            if digene_quantity != "":
               if int(digene_quantity) >= 4:
                  print("not in stock")
               else:
                  print("Available in stock")

        case 4:
            print(" Expiry check \n")
            medicine = ""
            expiry_year = 2026
            expiry_month = 12
            curr_year = int(input('Enter the current year: '))
            curr_month = int(input('Enter the current month: '))

            if crocin == "dolo":
                expiry_year = 2026
                expiry_month = 12
                if curr_year <= expiry_year and curr_month <= expiry_month:
                    print("dolo   not in use")
                else:
                    print("dolo   in use")

            if para == "Paracitamol":
                expiry_year = 2025
                expiry_month = 12
                if curr_year <= expiry_year and curr_month <= expiry_month:
                    print("Paracitamol  not in use")
                else:
                    print("Paracitamol  in use")

            if crocin == "crocin":
                expiry_year = 2024
                expiry_month = 12
                if curr_year <= expiry_year and curr_month <= expiry_month:
                    print("crocin   not in use")
                else:
                    print("crocin   in use")

            if aspirin == "aspirin":
                expiry_year = 2026
                expiry_month = 12
                if curr_year <= expiry_year and curr_month <= expiry_month:
                    print("aspirin  not in use")
                else:
                    print("aspirin  in use")

            if digene == "digene":
                expiry_year = 2025
                expiry_month = 12
                if curr_year <= expiry_year and curr_month <= expiry_month:
                    print("digene  not in use")
                else:
                    print("digene  in use")

        case 5:
            print("------------------------------")
            print(" Customer details ")
            print("------------------------------\n")
            customer = input("Customer name: ")
            customer_age = int(input("Enter your age: "))
            customer_city = input("Enter your city: ")
            customer_phone = int(input("Enter your phone number: "))

            print("\nThank you for filling details")
            print("-----------------------------\n\n")

        case 6:
            print("Discount Offers")
            customer_type = input("Enter your customer type: ")
            discount = 10
            if customer_type == "regular_customer":
                print("10 % discount offers")
            else:
                print("No Discount Offers")

        case 7:
             print("GST AND TAX CALCULATION")
             if para_quantity != "" and para_price !=0:
                 para_amount = int(para_price) * int(para_quantity)
                 print("Paracitamol amount without gst :",para_amount)
                 para_gst = 10
                 para_gst_amount = para_amount * para_gst/100
                 print("paracitamol amount including gst :",para_gst_amount )
                 para_bill = para_amount + para_gst_amount
                 print("paracitamol Bill including gst :",para_bill)

             else:
                 para_bill = para_bill+ 0

             if dolo_quantity != "" and dolo_price !=0:
                 dolo_amount = int(dolo_price) * int(dolo_quantity)
                 print("Dolo amount without gst :",dolo_amount)
                 dolo_gst = 20
                 dolo_gst_amount  = dolo_amount  * dolo_gst/100
                 print("dolo amount including gst :", dolo_gst_amount )
                 dolo_bill = dolo_amount + dolo_gst_amount
                 print("dolo bill including gst :",dolo_bill)
             else:
                 dolo_bill =dolo_bill + 0

             if crocin_quantity != "" and crocin_price !=0:
                 crocin_amount = int(crocin_price) * int(crocin_quantity)
                 print("Crocin amount without gst :",crocin_amount)
                 crocin_gst = 10
                 crocin_gst_amount = crocin_amount * crocin_gst/100
                 print("crocin amount including gst :", crocin_gst_amount)
                 crocin_bill = crocin_amount + crocin_gst_amount
                 print("crocin bill including gst :", crocin_bill)

             else:
                 crocin_bill  =crocin_bill + 0

             if digene_quantity !=0 and digene_price !=0:
                 digene_amount = int(digene_price) * int(digene_quantity)
                 print("Digene amount without gst :",digene_amount)
                 digene_gst = 20
                 digene_gst_amount= digene_amount * digene_gst/100
                 print("digene amount including gst :", digene_gst_amount)
                 digene_bill = digene_amount + digene_gst_amount
                 print("digene bill including gst :", digene_bill)
             else:
                 digene_bill = digene_bill + 0

             if aspirin_quantity != "" and aspirin_price !=0:
                 aspirin_amount = int(aspirin_price) * int(aspirin_quantity)
                 print("Aspirin amount without gst :",aspirin_amount)
                 aspirin_gst = 10
                 aspirin_gst_amount = aspirin_amount * aspirin_gst/100
                 print("aspirin amount including gst :", aspirin_gst_amount)
                 aspirin_bill = aspirin_amount + aspirin_gst_amount
                 print("aspirin bill including gst :", aspirin_bill)
             else:
                 aspirin_bill  =aspirin_bill + 0

        case 8:
             print("------------------------------------")
             print("      ****      Bill      ****")
             print("------------------------------------\n\n")
             print("Customer Nmane:",customer)
             print("Customer Age:",customer_age)
             print("Customer City:",customer_city)
             print("Customer Phone:\n\n",customer_phone)

             total = total+dolo_bill+ para_bill + crocin_bill + digene_bill + aspirin_bill

             print(" medicine       price       quntity       gst       bill ")
             print(f" {dolo}       {dolo_price}     {dolo_quantity}     {dolo_gst}     {dolo_bill}\n")
             print(f" {para}    {para_price}     {para_quantity}     {para_gst}     {para_bill}\n")
             print(f" {digene}     {digene_price}   {digene_quantity}   {digene_gst}   {digene_bill}\n")
             print(f" {aspirin}    {aspirin_price}  {aspirin_quantity}  {aspirin_gst}  {aspirin_bill}\n")
             print(f" {crocin}     {crocin_price}   {crocin_quantity}   {crocin_gst}   {crocin_bill}\n")

             print('-------------------------------------')
             print(f"Final bill :                       {total} ")
             print('-------------------------------------\n\n')

        case 9:
            print("Thank you for visiting medicine!!!!!!")
            break

        case _:
            print("Invalid input.Please try again....")




