import datetime
from Theater import *

class Show:
    free_seats =0
    occupied_seats =0
    #theater=None

    num_of_shows = 0

    def __init__(self, name, genre, release_date,screening_date,screening_place,theater):
        Show.num_of_shows += 1
        self.show_number=Show.num_of_shows
        self.name = name
        self.genre = genre
        self.release_date = release_date
        self.screening_date= screening_date
        self.screening_place = screening_place
        self.theater=theater
        self.seats = []


#setters
    def set_name(self,name):
        self.name = name

    def set_genr(self,genre):
        self.genre = genre

    def set_release_date(self,release_date):
        self.release_date = release_date

    def set_screening_place(self,screening_place):
        self.screening_place = screening_place

    def setTheater(self,theatreName, Theater_number,rowCount):
        self.theater.theatreName = theatreName
        self.theater.Theater_number = Theater_number
        self.theater.rowCount = rowCount

#getters
    def get_name(self):
        return self.name

    def get_genre(self):
        return self.genre

    def get_release_date(self):
        return self.release_date

    def get_screening_date(self):
        return self.screening_date

    def get_screening_place(self):
        return self.screening_place

    def get_free_seats(self):
        return self.free_seats

    def get_occupied_seats(self):
        return self.occupied_seats

    def getTheater(self):
        return self.theater

    def getshow_number(self):
        return self.show_number

    def getFreeSeatsCount(self):
        for i in range (len(self.seats)):
            if self.seats[i].get_isReserved() == False:
                self.free_seats=self.free_seats+1

        return self.free_seatsfree_seats








#def main():
#    print("hi")
#if __name__ == "__main__":
#    main()
