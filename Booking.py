from Customer import *
from Show import *

class Booking:
    #costumer=None
    #show=None

    def __init__(self, row_number,seat_number,costumer,show):
        self.row_number=row_number
        self.seat_number = seat_number
        self.costumer = costumer
        self.show = show
        self.cost = 0

    def setRowNumber(self, row_number):
            self.row_number = row_number

    def setSeatNumber(self, seat_number):
        self.seat_number = seat_number

    def setCost(self, cost):
        self.cost = self.cost + cost
        return self.cost

    def printCost(self):
        return self.cost

    def setcostumer(self, costumer):
        self.costumer = costumer

    def setshow(self, show):
        self.show = show

    # getters

    def getRowNumber(self):
            return self.row_number
    def getSeatNumber(self):
            return self.seat_number

    def getCost(self):
            if self.row_number >=1 and self.row_number <= self.show.getTheater().get_rowCount()/2:
                return 40
            if self.row_number > self.show.getTheater().get_rowCount()/2 and self.row_number <= self.show.getTheater().get_rowCount() :
                return 50

    def reserveSeatstatus(self):
        return self.show.getTheater().getRows()[self.row_number-1].getSeats()[self.seat_number-1].get_isReserved()

    def reserveSeat(self):
        if self.show.getTheater().getRows()[self.row_number-1].getSeats()[self.seat_number-1].get_isReserved()== True:
            return True
        else:
            self.show.getTheater().getRows()[self.row_number-1].getSeats()[self.seat_number-1].reserve()
            return False

    #   # if self.show.getTheatre().getRows().get(self.row_number).getSeats().get(self.seat_number).get_isReserved() == True:
    #        print("Sorry the seat is already reserved.")
    #    else:
    #        self.show.getTheatre().getRows().get(self.row_number).getSeats().get(self.seat_number).reserve()
    #        self.setRowNumber(self.row_number);
    #        self.setSeatNumber(self.seat_number);
    #        print("The seat is now reserved for you.")


    def unreserveSeat(self):
        self.show.getTheater().getRows()[self.row_number-1].getSeats()[self.seat_number-1].unreserve()

    def getCostumer(self):
        return self.costumer.get_ID()
