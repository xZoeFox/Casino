class User:
    def __init__(self):

        self.full = "xZoeFox|5000"
        self.user_name = self.full.split("|")[0]
        self.money = int(self.full.split("|")[1])
        with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
            self.line1 = a.readline()
            self.line1 = self.line1.replace("\n","")
            self.name = self.line1.split("|")[0]
            self.cash = int(self.line1.split("|")[1])
            self.cash_st = str(self.cash)

            
        
korisnik = User()

   
    
        

    






