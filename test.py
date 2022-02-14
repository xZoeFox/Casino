with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","r") as a:
    line1 = a.readline()
    line1 = line1.replace("\n","")
    name = line1.split("|")[0]
    cash = int(line1.split("|")[1])
    cash_st = str(cash-1)




with open(r"C:\Users\bejtx\OneDrive\Desktop\GameDev\Projekti\ENG\Casino\users.txt","w") as a2:
    a2.write(name+"|"+cash_st)
