from user import User
from random import randint, choice
from time import sleep

class SlotMachine(User):

    def __init__(self):
        super().__init__()

    def spin(self):
        with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
                self.line1 = a.readline()
                self.line1 = self.line1.replace("\n","")
                self.name = self.line1.split("|")[0]
                self.cash = int(self.line1.split("|")[1])
                self.cash_st = str(self.cash)
                self.money = int(self.cash_st)
        while True:
            self.fruits = ["Grape", "Banana", "Cherry", "Apple", "Orange", "Starwberry", "Pineapple"]
            self.fruit1 = choice(self.fruits)
            self.fruit2 = choice(self.fruits)
            self.fruit3 = choice(self.fruits)
            spin_money = randint(10000, 15000)
            print("\n____________________________SLOT____________________________________")
            print(f"\nThe Jackpot value is {spin_money}$")
            slot_start = input("To start the slot machine, type /spin | price: 500$ , to leave type /exit: ")
            if slot_start == "/spin":
                if self.money < 500:
                    print("You have no money! Open the box with command /boxes!")
                    break
                else:
                    self.money -= 500
                    print("You put 500$ in the slot machine")
                half = self.fruit1 == self.fruit2 != self.fruit3 or self.fruit1 == self.fruit3 != self.fruit2 or self.fruit2 == self.fruit3 != self.fruit1
                full = self.fruit1 == self.fruit2 == self.fruit3
                print(f"\n{self.user_name} you started the slot machine, your fruits: {self.fruit1}|{self.fruit2}|{self.fruit3}")
                if half:
                    self.money += spin_money // 2
                    print(f"Congratulations you won half the jackpot: {spin_money // 2}$, you currently have: {self.money}$")
                    sleep(3)
                elif full:
                    self.money += spin_money
                    print(f"Congratulations on winning the jackpot: {spin_money}$, you currently have: {self.money}")
                    sleep(3)
                else:
                    print("You didn't win anything, good luck next tname!")
                    print(f"Your account balance is {self.money}$")
                    sleep(3)
            elif slot_start == "/exit":
                print("You gave up!")
                self.cash_st = str(self.money)
                with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","w") as a2:
                    a2.write(self.name+"|"+self.cash_st)
                break
            else:
                print("Wrong command!")


obj_slot = SlotMachine()


