from Seat import *

class Row:


    def __init__(self,rowNumber,seatCount):

        self.rowNumber = rowNumber
        self.seatCount = seatCount
        self.seats = []



#getters

    def get_rowNumber(self):
        return self.rowNumber

    def getSeats(self):
        return self.seats

    def getseatCount(self):
        return self.seatCount

    def createSeats(self):
        for i in range(self.seatCount):
            s= Seat(i,False)
            self.seats.append(s)


    def printSeats(self):
        print(self.seats[3].isReserved)
        #for i in range(self.seatCount):
            #if self.seats[i].isReserved == True:
            #    print('X', end =" ")
            #else:
            #    print(self.seats[i].get_seatNumber()+1, end =" ")



#def main():
#    d=Row(3,5)
#    d.createSeats()
#    d.printSeats()
#if __name__ == "__main__":
#    main()

