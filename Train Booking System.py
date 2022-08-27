class Train:

    def __init__(self,name,fair,seats):
        self.name=name
        self.fair=fair
        self.seats=list(range(1,seats+1))
        self.totalseats=seats
        self.availSeats=seats

    def trainStatus(self):
        print(f"The Name of Train : ",self.name)
        print("Available Seats : ",self.availSeats)

    def trainFair(self):
        print(f"Fair of this train is ",self.fair)

    def bookTicket(self,wantBook):

        if wantBook not in self.seats:
            print("Seat is Not Available. !!")
        else:
            print("Congratulations!,Your Ticket is Booked..")
            print("Your Seat Number is ",wantBook)
            self.seats.remove(wantBook)
            self.availSeats=self.availSeats-1
            print("Available Seats : ",self.seats)
            
    def availableTicket(self):
        print("Available Seats : ",self.seats)
        
    def bookedTickets(self):
        return self.totalseats-self.availSeats
    
    def cancelTicket(self,seatNo):
        if(seatNo in self.seats):
            print("Seat is Not Booked. Please Enter Another Seat.")
        else:
            print("Your Ticket is Cancelled")
            self.availSeats=self.availSeats+1
            self.seats.insert(seatNo-1,seatNo)
            self.seats.sort()
            print("Available Seats : ",self.seats)

print('''
WELCOME **''')
sts=100
fair=150
local=Train("Rajdhani Express",fair,sts)
local.trainStatus()
local.trainFair()

def main():
    try:
        while True:
            x=int(input('''
Select Operation :
1. Book Ticket
2. Cancel Ticket
3. Check Train Status
4. Exit
--> '''))
    
            if x==1:
                b=s=int(input("How Many Tickets You Want to Buy : "))
                if(b in range(1,sts+1)):
                    while b>0:
                        a=int(input("Enter Which Seat You Want : "))
                        local.bookTicket(a)
                        b-=1
                    print("Total Ticket Fair : ",fair*s,"Rs.")
                main()
            elif x==2:
                if local.bookedTickets() != 0:
                    c=q=int(input("How Many Tickets You Want to Cancel : "))
                    if(c in range(1,local.bookedTickets()+1)):
                        while c>0:
                            x=int(input("Which Seat You Want to Cancel : "))
                            if(x in range(1,sts+1)):
                                local.cancelTicket(x)
                            else:
                                print("Enter Seat No in 1 to 100.")
                                x=int(input("Which Seat You Want to Cancel : "))
                                local.cancelTicket(x)
                            c-=1
                        print("Refund Fair : ",140*q,"Rs.")
                        local.trainStatus()
                        local.availableTicket()
                        main()
                    else:
                        print("Seats Are not Booked ..!!")
                        main()
                else:
                    print("Seats not booked Yet..!!")
                    main()
                    
            elif x==3:
                local.trainStatus()
                print('Booked Tickets : ',local.bookedTickets())
                local.availableTicket()
                main()
            elif x==4:
                break
            else:
                print("Please Enter Valid Input ....!!!")
                main()
    except:
        print("Not Valid Input !!")
        main()
    
main()