
print('=====================================')
print('     LIBRARY MANAGEMENT SYSTEM')
print('=====================================')

# Login Details
username = 'admin'
password = '1234'

user = input('Enter Username : ')
pwd  = input('Enter Password : ')

# Book Details
book1 = 'Python Basics'
book1_qty = 5

book2 = 'Java Fundamentals'
book2_qty = 4

book3 = 'C Programming'
book3_qty = 3

book4 = 'DBMS'
book4_qty = 2

book5 = 'HTML CSS'
book5_qty = 6

fine = 0

if user == username and pwd == password:

    print('\nLogin Successful')

    while True:

        print('\n=====================================')
        print('             MAIN MENU')
        print('=====================================')
        print('1. View Books')
        print('2. Issue Book')
        print('3. Return Book')
        print('4. Check Stock')
        print('5. Fine Calculator')
        print('6. Student Details')
        print('7. Exit')
        print('=====================================')

        choice = int(input('Enter Your Choice : '))

        match choice:
            case 1:
                print('\n============= BOOKS =============')
                print('1.', book1, 'Quantity =', book1_qty)
                print('2.', book2, 'Quantity =', book2_qty)
                print('3.', book3, 'Quantity =', book3_qty)
                print('4.', book4, 'Quantity =', book4_qty)
                print('5.', book5, 'Quantity =', book5_qty)

            case 2:
                print('\n============= ISSUE BOOK =============')
                print('1.', book1)
                print('2.', book2)
                print('3.', book3)
                print('4.', book4)
                print('5.', book5)

                book_id = int(input('Choose Book Number : '))

                if book_id == 1:

                    if book1_qty > 0:
                        student = input('Enter Student Name : ')
                        book1_qty -= 1
                        print(book1, 'Issued Successfully')
                        print('Remaining Quantity =', book1_qty)
                    else:
                        print('Book Out Of Stock')

                elif book_id == 2:

                    if book2_qty > 0:
                        student = input('Enter Student Name : ')
                        book2_qty -= 1
                        print(book2, 'Issued Successfully')
                        print('Remaining Quantity =', book2_qty)
                    else:
                        print('Book Out Of Stock')

                elif book_id == 3:

                    if book3_qty > 0:
                        student = input('Enter Student Name : ')
                        book3_qty -= 1
                        print(book3, 'Issued Successfully')
                        print('Remaining Quantity =', book3_qty)
                    else:
                        print('Book Out Of Stock')

                elif book_id == 4:

                    if book4_qty > 0:
                        student = input('Enter Student Name : ')
                        book4_qty -= 1
                        print(book4, 'Issued Successfully')
                        print('Remaining Quantity =', book4_qty)
                    else:
                        print('Book Out Of Stock')

                elif book_id == 5:

                    if book5_qty > 0:
                        student = input('Enter Student Name : ')
                        book5_qty -= 1
                        print(book5, 'Issued Successfully')
                        print('Remaining Quantity =', book5_qty)
                    else:
                        print('Book Out Of Stock')

                else:
                    print('Invalid Book Choice')

            case 3:
                print('\n============= RETURN BOOK =============')
                print('book_id 1.', book1)
                print('book_id 2.', book2)
                print('book_id 3.', book3)
                print('book_id 4.', book4)
                print('book_id 5.', book5)

                r = int(input('Enter Book Number : '))

                if r == 1:
                    book1_qty += 1
                    print(book1, 'Returned Successfully')

                elif r == 2:
                    book2_qty += 1
                    print(book2, 'Returned Successfully')

                elif r == 3:
                    book3_qty += 1
                    print(book3, 'Returned Successfully')

                elif r == 4:
                    book4_qty += 1
                    print(book4, 'Returned Successfully')

                elif r == 5:
                    book5_qty += 1
                    print(book5, 'Returned Successfully')

                else:
                    print('Invalid Choice')

            case 4:

                print('\n============= STOCK CHECK =============')

                if book1_qty < 2:
                    print(book1, 'Low Stock')

                if book2_qty < 2:
                    print(book2, 'Low Stock')

                if book3_qty < 2:
                    print(book3, 'Low Stock')

                if book4_qty < 2:
                    print(book4, 'Low Stock')

                if book5_qty < 2:
                    print(book5, 'Low Stock')

            case 5:

                print('\n============= FINE CALCULATOR =============')

                days = int(input('Enter Late Days : '))

                fine = days * 5

                print('Total Fine =', fine)

            case 6:

                print('\n============= STUDENT DETAILS =============')

                s_name = input('Enter Student Name : ')
                roll = input('Enter Roll Number : ')
                course = input('Enter Course Name : ')
                mobile = input('Enter Mobile Number : ')

                print('\nStudent Details Saved Successfully')

                print('Name =', s_name)
                print('Roll Number =', roll)
                print('Course =', course)
                print('Mobile =', mobile)

            case 7:

                print('\nThank You For Using Library System')
                break

            case _:

                print('Invalid Menu Choice')

else:

    print('Invalid Username Or Password')



