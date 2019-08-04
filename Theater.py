from Row import *
class Theater:
    Theater_number=0

    def __init__(self,theatreName,rowCount):
        Theater.Theater_number += 1
        self.theatreName=theatreName
        self.rowCount = rowCount
        self.rows = []


#setters
   # #def set_Theater_number(self,Theater_number):
   #     self.Theater_number = Theater_number

    def set_theatreName(self,theatreName):
        self.theatreName = theatreName

    def set_rowCount(self,rowCount):
        self.rowCount = rowCount

#getters

    def get_Theater_number(self):
        return self.Theater_number

    def get_theatreName(self):
        return self.theatreName

    def printTheatre(self):
        return self.theatreName

    def get_rowCount(self):
        return self.rowCount

    def createRows(self,num):
        for i in range(self.rowCount):
            r= Row(i,num)
            self.rows.append(r)
            r.createSeats()

    def printTheater(self):
        for i in range(self.rowCount):
            self.rows[i].printSeats()
            print()

    def printTheater1(self):
        for i in range(self.rows.__len__()):
            print()
            for y in range(self.rows[i].getseatCount()):
                if (self.rows[i].seats[y].get_isReserved()) :
                    print("X ", end =" ")
                else :
                    print(str(self.rows[i].seats[y].get_seatNumber()+1) + " ", end =" ")






   #def printTheater(self):
   #    for i in range(self.rowCount):
   #        print(str(self.rows[i].get_rowNumber()) + "  | ")
   #        for y in range(self.rows[i].seatCount):
   #            #(Seat seat: row.getSeats()):
   #            if (self.rows[y].getSeats()[y].get_isReserved()) :
   #                print("X ")
   #            else :
   #                (str(self.rows[y].getSeats()[y].get_seatNumber()) + " ")


   #        print("\n")


    def getRows(self):
        return self.rows



#def main():
#  #  r = Row(10, 10)
#    t = Theater(10, 10)
#    t.createRows(10)
#    t.printTheater()
#
#
#if __name__ == "__main__":
#    main()
