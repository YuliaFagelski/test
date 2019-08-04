class Customer:
    def __init__(self, Fullname,ID):
        self.Fullname = Fullname
        self.ID = ID


#setters
    def set_Fullname(self,Fullname):
        self.Fullname = Fullname

    def set_ID(self,ID):
        self.ID = ID

#getters

    def get_Fullname(self):
        return self.Fullname

    def get_ID(self):
        return self.ID

    def print(self):
        print(self.Fullname + " "+self.ID)

#def main():
#   s=Customer('Yulia','123')
#   s.print()
#if __name__ == "__main__":
#   main()
