from user import User
from random import randint
from time import sleep

class Bingo(User):

    def __init__(self):
        super().__init__()
        

    def start_bingo(self):
        with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
                self.line1 = a.readline()
                self.line1 = self.line1.replace("\n","")
                self.name = self.line1.split("|")[0]
                self.cash = int(self.line1.split("|")[1])
                self.cash_st = str(self.cash)
                self.money = int(self.cash_st)
        while True:
            neka_lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43',
         '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75']
            self.all_numbers_list1 = []
            self.all_numbers_list2 = []
            while len(self.all_numbers_list2) != 32:
                self.all_numbers_list1.append(randint(0,75))
                for n in self.all_numbers_list1:
                    if str(n) not in self.all_numbers_list2:
                        self.all_numbers_list2.append(str(n))
            self.user_numbers = []
            self.check_list = []
            bingo_jackpot =  randint(50000,100000)
            print("\n____________________________BINGO____________________________________")
            print(f"\nThe Jackpot value is {bingo_jackpot}$")
            bingo_start = input("To start the bingo, type /bingo | price: 1000$ , to leave type /exit: ")
            if bingo_start == "/bingo":
                number = 0
                while number != 6:
                    number += 1
                    try:
                        add_num = input(f"Type your {number}. number: ")
                        if add_num in neka_lista:
                            self.user_numbers.append(add_num)
                            print(f"Your {number}. number is: {add_num} !")
                        else:
                            print("Wrong entry, the entry must be a number from 0 to 75!")
                            break
                    except:
                        print("Wrong entry, the entry must be a number from 0 to 75!")
                        break
                else:
                    for n in self.user_numbers:
                        if n not in self.check_list:
                            self.check_list.append(n)
                        else:
                            print(f"You can't have the same numbers!")
                            break
                    
                    if len(self.check_list) == 6: 
                        print("\nYou entered all 6 numbers!")
                        if self.money < 1000:
                            print("You have no money! Open the box with command /boxes!")
                            break
                        else:
                            self.money -= 1000
                            print("You paid 1000$ for a bingo ticket!")
                            print(f"{self.user_name}, your numbers are: {self.user_numbers}")

                        # numbers drawn:                
                        print("The draw begins:")
                        for n in self.all_numbers_list2:
                            print(f"Number drawn: {n}")
                            sleep(0.5)

                        print(f"The numbers drawn are: {self.all_numbers_list2}")
                        bingo_numbers = self.all_numbers_list2 
                        
                        
                        same_numbers = set(self.user_numbers) & set(bingo_numbers)
                        same_numbers = list(same_numbers)
                        same_numbers.sort()
                        print(f"The numbers that match are: {same_numbers}")

                        if len(same_numbers) == 5:
                            print(f"{self.user_name}, congratulations you won a five in the amount of {bingo_jackpot // 2}$")
                            self.money += bingo_jackpot // 2
                            print(f"Your account balance is {self.money}$")
                            sleep(3)
                        elif len(same_numbers) == 6:
                            print(f"{self.user_name}, congratulations you won Bingo in the amount of {bingo_jackpot}$")
                            self.money += bingo_jackpot
                            print(f"Your account balance is {self.money}$")
                            sleep(3)
                        else:
                            print(f"{self.user_name}, you didn't win anything, good luck next tname!!")
                            print(f"Your account balance is {self.money}$")
                            sleep(3)
            
            elif bingo_start == "/exit":
                print("You gave up!!")
                self.cash_st = str(self.money)
                with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","w") as a2:
                    a2.write(self.name+"|"+self.cash_st)
                break
            else:
                print("Wrong command!")



obj_bingo = Bingo()



