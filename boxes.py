from user import User
from random import randint
from time import sleep

class Boxes(User):
    
    def __init__(self):
        super().__init__()
    
    def _bonus(self):
        bonus_money = randint(1000, 5000)
        self.money += bonus_money
        print(f"{self.user_name}, you opened the box with {bonus_money}$, so now you have: {self.money}$")
        self.cash_st = str(self.money)
        with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","w") as a2:
            a2.write(self.name+"|"+self.cash_st)
        a2.close
        sleep(3)

    def pick_one(self):
        while True:
            with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
                self.line1 = a.readline()
                self.line1 = self.line1.replace("\n","")
                self.name = self.line1.split("|")[0]
                self.cash = int(self.line1.split("|")[1])
                self.cash_st = str(self.cash)
                self.money = int(self.cash_st)
            print("\n____________________________BOXES____________________________________")
            pick = input("\nWhich box do you want to open: 1, 2 or 3?: ")
            if self.money < 500:
                if pick == "1":
                    print("You opened the box number 1!")
                    Boxes._bonus(self)
                    break
                elif pick == "2":
                    print("You opened the box number 2!")
                    Boxes._bonus(self)
                    break
                elif pick == "3":
                    print("You opened the box number 3!")
                    Boxes._bonus(self)
                    break
                else:
                    print("Wrong box number!")
            else:
                print(f"You must have less than 500$ to open the box! You have {self.money}$")
                sleep(3)
                break



obj_boxes = Boxes()