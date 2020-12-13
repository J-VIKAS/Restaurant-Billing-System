import random

def Menu():
    print("Menu : -")
    print("_____________________________________________")
    print("|  Item Code  |    Item Name   |     Cost    |")
    print("_____________________________________________")
    print("|     1001    |      Tea       |     0.5$    |")
    print("|     1002    |     Coffee     |     0.7$    |")
    print("|     1003    |    Milkshake   |     1.2$    |")
    print("|     1004    |     Pastry     |     2.0$    |")
    print("|     1005    |  French Frie  |      2.5$    |")
    print("|     1006    |     Pizza      |     7.0$    |")
    print("|     1007    |    Hot Dog     |     4.0$    |")
    print("______________________________________________")

class Queue:

    def __init__(self):
        print("******* WELCOME TO FORT COLLINS RESTAURANT *******\n")
        self.Queue = []
        self.MenuCode = [1001, 1002, 1003, 1004, 1005, 1006, 1007]
        self.MenuName = ["Tea", "Coffee", "Milkshake", "Pastry ", "French Frie", "Pizza", "Hot Dog"]
        self.MenuCost = [0.5, 0.7, 1.2, 2.0, 2.5, 7.0, 4.0]

    def addCustomer(self):
        print("Enter Details Of the Customer : -")
        print("Enter Your Name : - ")
        Name = input()
        print("Enter Your Mobile Number : - ")
        PhoneNumber = int(input())
        print("Enter Your Email : - ")
        Email = input()
        self.Queue.append([Name,PhoneNumber,Email])
        print("Updated Customer List : -",self.Queue)

    def CreateBill(self,Order):
        Details = self.Queue[0]
        print("Details of the customer: -")
        print("Name : -",Details[0])
        print("Phone Number : -",Details[1])
        print("Email : -",Details[2],"\n")
        print("Your Bill No. =",random.randrange(1000,9999,100))
        print("__________________________________________________________________________________________|")
        print("| Serial No","|","ItemCode"," |","  ItemName  ","|","  Cost(per item)  ","|"," Quantity ","|"," Final Amount ","|")
        print("__________________________________________________________________________________________|")
        TotalCost = 0
        for i in range(len(Order)):
            TotalCost += (Order[i][1])*(self.MenuCost[Order[i][0]-1001])
            ItemNameSpacesleft = ((12 - len(self.MenuName[Order[i][0]-1001]))//2)*" "
            ItemNameSpacesrigth = (12 - len(self.MenuName[Order[i][0]-1001]) - len(ItemNameSpacesleft))*" "
            Costleft = (((18 - len(str(self.MenuCost[Order[i][0]-1001])))//2)-1)*" "
            Costright =  (18 - len(str(self.MenuCost[Order[i][0]-1001])) - len(Costleft))*" "
            Qleft = ((10-len(str(Order[i][1])))//2)*" "
            Qright = ( 10-len(str(Order[i][1])) - len(Qleft))*" "
            Aleft = ((14 - len(str(Order[i][1]*self.MenuCost[Order[i][0]-1001])))//2)*" "
            Arigth = (14 - len(str(Order[i][1]*self.MenuCost[Order[i][0]-1001])) - len(Aleft))*" "
            print("|    ",i+1,"    |  ",self.MenuCode[Order[i][0]-1001],"  |"+ItemNameSpacesleft,self.MenuName[Order[i][0]-1001],ItemNameSpacesrigth+" |"+Costleft,self.MenuCost[Order[i][0]-1001],Costright+"|"+Qleft,Order[i][1],Qright+"|"+Aleft,Order[i][1]*self.MenuCost[Order[i][0]-1001],Arigth+"|")
        print("|_________________________________________________________________________________________|")
        print("| Total Amount                                                                   = ",str(TotalCost)+"$",  "|\n")
        self.LastLine()
        self.Queue.remove(self.Queue[0])

    def LastLine(self):
        print("\nHope You Enjoy Our Services")
        print("We wish you come here again")
        print("Good Day Ma'am/Sir")

    def BookOrder(self):
        print("\nHello Ma'am/Sir",self.Queue[0][0])
        print("Please Place your Order Here : -")
        Order = []
        while(1):
            print("\nChoose from here: - ")
            print("1). Show Menu")
            print("2). Exit and Calculate Bill")
            print("Choose your choice number : - ")
            choice = int(input())
            if choice == 1:
                print()
                Menu()
                print("Choose the item code :- ")
                ItemCode = int(input())
                print("Quantity of the item : - ")
                Quantity = int(input())
                Order.append([ItemCode,Quantity])
            elif choice == 2:
                print()
                self.CreateBill(Order)
                break
            else:
                print("Wrong Entry From User")
                print("Please try again\n")

def Main ():
    q = Queue()
    q.addCustomer()
    q.BookOrder()

Main()