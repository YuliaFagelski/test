from Theater import *
from Show import *
from Booking import *
import random
import sys
from datetime import datetime
def main():

    shows = []
    theatres =[]
    bookings = []
    customers = []
    repeat = 1
    bill = 0

    file_path= 'U:\\file1_exp.txt'
    with open(file_path) as f:
        huge_list = f.read().split()

    print("------------------------------------")
    print(":Cinema Booking System by Ladybug:")
    print("------------------------------------\n")
    print("Please Enter 1 to Add Theatre")
    print("Please Enter 2 to Add Show")
    print("Please Enter 3 to Display Shows")
    print("Please Enter 4 to Make Booking")
    print("Please Enter 5 to Cancel Booking")
    print("Please Enter 6 to Exit\n")
    option=int(input("Enter Option: "))

    #for test
    theatre = Theater('Glilot',  10)
    theatre.createRows(10)
    theatres.append(theatre)

    show =Show('aladin','Drama', "22/07/2019","22/07/2019",'Cinema',theatre)
    shows.append(show)
    # for test

    def validate(date_text):
        day,month,year = date_text.split('/')
        try:
            datetime(int(year),int(month),int(day))
            return True
        except ValueError:
            return False

    while True:
        #option != 6:

        if option == 1 :
            print("ADD THEATRE Selected")
            print("-------------------------\n")
            theatreName =input("Enter a name for the theatre: \n")
            rowCount = int(input("Enter the number of rows:"))
            theatre = Theater(theatreName,rowCount)
            theatre.createRows(rowCount)
            theatre.printTheater1()
            theatres.append(theatre)

        if option == 2:

            print("ADD SHOW Selected")
            print("-------------------------\n")

            showDate=input("Enter the date of the Show [DD/MM/YYYY]:")
            while validate(showDate) == False:
                showDate = input("Enter the date of the Show [DD/MM/YYYY]:")
            showName=input("Enter name of Show: \n")
            for i in range(theatres.__len__()):
                print(str(i + 1) + " " + theatres[i].get_theatreName())
            theatreNumber=int(input("Select a theatre by typing the number:"))
            s=Show(showName,'Drama', showDate,showDate,'Cinema',theatres[(theatreNumber-1)])
            shows.append(s)
            #print(shows[0].get_name())

        if option == 3:

            print("DISPLAY SHOWS Selected")
            print("-------------------------\n")
            for i in range(shows.__len__()):
                print(shows[i].get_name()+ ' at '+ shows[i].get_release_date()+' in '+shows[i].getTheater().get_theatreName())

        if option == 4:

            print("MAKE BOOKING Selected")
            print("-------------------------\n")
            CustomerwName = input("Enter your name: \n")
            rnd = random.randint(0,999)
            #costumerId = rnd.nextInt(999)
            customer = Customer(CustomerwName,rnd)
            customers.append(customer)
            for i in range(shows.__len__()):
                print("Show Number: "+ str(i + 1) + " Show Name:   "+shows[i].get_name()+ ' Show Date: '+ shows[i].get_release_date()+' in '+shows[i].getTheater().get_theatreName())


            print("-------------------------")
            showNumber =int(input("Enter the show number: "))
            repeat = 1

            while repeat == 1:
                shows[showNumber - 1].getTheater().printTheater1()
                print()
                selectedRow = int(input("Enter the row: "))
                selectedSeat = int(input("Enter the seat: "))
                print()
                booking = Booking(selectedRow, selectedSeat, customer, shows[showNumber - 1])

                if booking.reserveSeat() == False:
                    bill = bill + booking.getCost()
                    bookings.append(booking)
                    print("The seat is now reserved for you.")

                else:
                    print("Sorry the seat is already reserved.")

                print()
                repeat = int(input("Enter 1 to reserve another seat or 2 to check out: "))

            print("Costumer ID: " + str(customer.get_ID()))
            print("Total costs: " + str(bill) + " Euro")
            bill=0
            print()

        if option == 5:

            print("CANCEL BOOKING Selected")
            print("-------------------------\n")
            customerId=int(input("Enter the costumer id: "))
            for i in range(bookings.__len__()):
                if bookings[i].getCostumer() == customerId:
                    bookings[i].unreserveSeat()
                    print("Your reservation has been canceled!")

        if option == 6:
            sys.exit()

        print()
        option = int(input("Enter Option: "))

if __name__ == "__main__":
    main()
