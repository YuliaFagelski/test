
class Seat:
    def __init__(self, seatNumber,isReserved):
        self.seatNumber = seatNumber
        self.isReserved = isReserved


#setters
    def set_seatNumber(self,seatNumber):
        self.seatNumber = seatNumber

    def set_isReserved(self,isReserved):
        self.isReserved = isReserved

#getters

    def get_seatNumber(self):
        return self.seatNumber

    def get_isReserved(self):
        return self.isReserved

    def reserve(self):
        self.isReserved = True
        return self.isReserved

    def unreserve(self):
        self.isReserved = False
        return self.isReserved


#def main():
#    s=Seat(3,'True')
#    print(s.get_isReserved())
#    s.set_isReserved(False)
#    print(s.get_isReserved())
#    s.reserve()
#    print(s.get_isReserved())
#    s.unreserve()
#    print(s.get_isReserved())
#if __name__ == "__main__":
#    main()
