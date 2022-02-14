from user import User
from boxes import obj_boxes
from slot import obj_slot
from bingo import obj_bingo

class Casino(User):

    def __init__(self):
        super().__init__()

    def welcome(self):
        while True:
            with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
                self.line1 = a.readline()
                self.line1 = self.line1.replace("\n","")
                self.name = self.line1.split("|")[0]
                self.cash = int(self.line1.split("|")[1])
                self.cash_st = str(self.cash)
                self.money = int(self.cash_st)
            print("\n____________________________CASINO____________________________________")
            print("\nWelcome to the Casino, " + str(self.name) + ". Your account balance is: " + str(self.money) + "$")
            print("If you want to see a list of commands, type /commands")
            casino_menu = input("Enter the command: ")
            
            if casino_menu == "/commands":
                print("\n____________________________COMMAND LIST____________________________________\n")
                print("If you do not have money, enter the command /boxes")
                print("If you want to access the slot machine enter the command /slot")
                print("If you want to access bingo, enter the command /bingo")
                print("To leave the casino, type /quit")
                print("_____________________________________________________________________________\n")
            elif casino_menu == "/boxes":
                obj_boxes.pick_one()
            elif casino_menu == "/slot":
                obj_slot.spin()
            elif casino_menu == "/bingo":
                obj_bingo.start_bingo()
            elif casino_menu == "/quit":
                print("You left the Casino!")
                self.cash_st = str(self.money)
                with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","w") as a2:
                    a2.write(self.name+"|"+self.cash_st)
                break
            else:
                print(f"{casino_menu} command does not exist try again!")

start_casino = Casino()

start_casino.welcome()