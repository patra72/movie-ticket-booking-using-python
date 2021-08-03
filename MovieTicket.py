#import library modules
import time
import random

#Define variables
options="yes"
Ticket_No=random.randint(0,200)#used in Ticket receipt
Category=[]#list includes Ticket category
unit_cost=[]#list includes cost per ticket
total_qty=[]#list includes total quantity per category
total_cost=[]#list includes total cost per category

LogoDate=time.strftime("%d/%m/%Y",time.localtime(time.time()))
present_month_year=time.strftime("%m/%Y",time.localtime(time.time()))
Logoclock=time.strftime("%r",time.localtime(time.time()))
DateTime=time.strftime("%d/%m/%Y %H:%M:%S",time.localtime(time.time()))#used in Ticket Receipt

#print Welcome Message
print("*"*80)
print(LogoDate+"\t\t"+"Welcome to Movie Ticket Booking App"+"\t"+' '+Logoclock)
print("*"*80)
print("\t\t\t\t\t\t"+'Developed by sachin patra')
print(' ')

#price details against Ticket Category
def price_detail():
    print('')
    print("Price Details:")
    print(' ')
    print('Ticket Category                     Cost  ')
    print("-"*30)
    print('Adult                               100$   ')
    print('Child                                20$    ')
    print('Senior                               50$   ')
    print('Concession                           70$   ')
    print(' ')

#price calculation against category selection
def calculation():
    ticket_type=int(input("How many category tickets do you want to purchase?(1-4)  "))
    if ticket_type > 4 or ticket_type==0:
        print("Invalid type count.retry!!!!")
        print(' ')
        ticket_type=int(input("How many category tickets do you want to purchase?(1-4)  "))

    print(' ')
    for i in range(ticket_type):
        Choose_Category=input("Choose a category for A for Adult,C for Child,S for Senior and CO for Concession")
        if Choose_Category=='A':
            Adult_qty=int(input("How many adult tickets do you want to purchase ? "))
            print(' ')
            Total_adult_price=Adult_qty*100
            CatType='Adult'
            Category.append(CatType)
            cost=100
            unit_cost.append(cost)
            total_qty.append(Adult_qty);
            total_cost.append(Total_adult_price)

        elif Choose_Category=='C':
            Child_qty=int(input("How many Child Tickets do you want to purchase? "))
            print(' ')
            Total_child_price=Child_qty*20
            CatType='Child'
            Category.append(CatType)
            cost=20
            unit_cost.append(cost)
            total_qty.append(Child_qty);
            total_cost.append(Total_child_price)

        
        elif Choose_Category=='S':
            Senior_qty=int(input("How many Senior Citizen Tickets do you want to purchase? "))
            print(' ')
            Total_senior_price=Senior_qty*50
            CatType='Senior'
            Category.append(CatType)
            cost=50
            unit_cost.append(cost)
            total_qty.append(Senior_qty);
            total_cost.append(Total_senior_price)

        elif Choose_Category=='CO':
            concession_qty=int(input("How many Concession Tickets do you want to purchase? "))
            print(' ')
            Total_concession_price=concession_qty*70
            CatType='Concession'
            Category.append(CatType)
            cost=70
            unit_cost.append(cost)
            total_qty.append(concession_qty);
            total_cost.append(Total_concession_price)

        else:
            print(' ')
            print('Please choose a valid category')
            print(' ')


#Cart Detail before Payment Process
def cart_detail():
    print(' ')
    print('Bill Details: ')
    print(' ')
    print("Ticket Category",' \t',"Unit Cost",'\t\t',"Qty",'\t\t',"Total Cost")
    print('-'*80)
    #use to design the bill template
    subtotal=0
    for i in range(len(Category)):
        print(Category[i],'\t\t',unit_cost[i],'\t\t',total_qty[i],'\t\t',total_cost[i])
        subtotal=int(total_cost[i])+subtotal

    print('\t\t\t\t','----------------------------')
    print('\t\t\t\t','Subtotal : ',str(subtotal),'$')

    Tax_price=subtotal*0.15
    print('\t\t\t\t','Tax Amount(15%): ',str(Tax_price),'$')
    
    print('\t\t\t\t','----------------------------')
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total cost of all tickets with Tax: ',str(Total),'$')


#Ticket Receipt after Payment Process
def ticket_receipt():
    print(' ')
    print('***********************************************************************')
    print("Ticket No: ",Ticket_No,"\t\t\t\t\t",'Date : ',DateTime)
    print('***********************************************************************')
    print("Ticket Category",'\t',"Unit Cost",'\t\t',"Qty",'\t\t',"Total Cost")
    print(' ')

    #used to design template for Ticket Receipt
    subtotal=0
    for i in range(len(Category)):
        print(Category[i],'\t\t',unit_cost[i],'\t\t',total_qty[i],'\t\t',total_cost[i])
        subtotal=int(total_cost[i])+subtotal

    print('\t\t\t\t','----------------------------')
    print('\t\t\t\t','Subtotal : ',str(subtotal),'$')

    Tax_price=subtotal*0.15
    print('\t\t\t\t','Tax Amount(15%): ',str(Tax_price),'$')
    
    print('\t\t\t\t','----------------------------')
    Total=Tax_price+subtotal
    print('\t\t\t\t','Total cost of all tickets with Tax: ',str(Total),'$')

#function used to write purchase data in to file
def data_write_file(Category,total_qty,unit_cost,total_cost):
    with open('transactions.txt','w') as f:

        #design data representation template
        f.write('***********************************\n')
        f.write('Ticket No: %d\n'%Ticket_No)
        f.write(DateTime)
        f.write('\n')
        f.write('***********************************\n')
        f.write('\n')

        for i in range(len(Category)):
            f.write('Category: ')
            f.write('%s\n'%Category[i])
            f.write('Qty: ')
            f.write('%d\n'%total_qty[i])
            f.write('Unit Cost: ')
            f.write('%d\n'%unit_cost[i])
            f.write('Total Cost: ')
            f.write('%d\n'%total_cost[i])
            f.write('\n')

        f.write('-----------------------------------\n')
        subtotal=0
        for i in range(len(total_cost)):
            subtotal=total_cost[i]+subtotal
        f.write("Total Cost(in $) %.f\n"%subtotal)
        Tax_price=subtotal*0.15
        Total=Tax_price+subtotal
        f.write("Total Cost with Tax(in $) %.f\n"%Total)
        f.write('-----------------------------------\n')
        f.close()

#Ticket Purchasing Process
def purchase_ticket():
    print('The tickets categories are Adult,Child,Seniors and Concessions.')
    print(' ')
    show_price=input("Do you want to know the price against categories? Y/N or y/n ")

    print(' ')
    if show_price in 'Y' or show_price in 'y':
        price_detail()
    elif show_price in 'N' or show_price in 'n':
        print('Let\'s purchase tickets')
        print(' ')
    else:
        print('Sorry your answer is not valid.')
        show_price=input("Do you want to know the price against categories? Y/N or y/n ")
        print(' ')

    calculation()
    print(' ')
    cart_detail()
    print(' ')
    print('Please Enter your Credit Card details to proceed payment')
    print(' ')
    print('Credit Card details: ')
    print('-'*20)

    Card_number=input('Enter your Credit Card Number(min 14 digit long): ')
    if len(Card_number)< 14 or len(Card_number)> 14:
        print(' ')
        print('Invalid Credit Card number.retry!!!')
        Card_number=input('Enter your Credit Card Number(min 14 digit long): ')

    print(' ')
    Expiry_date=input('Enter your valid Expiry date of your card(in month/year like 12/2020): ')
    if Expiry_date <= present_month_year:
        print('Invalid Expiry date.retry!!!')
        print(' ')
        Expiry_date=input('Enter your valid Expiry date of your card(in month/year like 12/2020): ')
        print(' ')

    print('Thank you for your information.We are processing your payment........')
    print(' ')
    print('You have successfully purchased the tickets.')
    print(' ')
    ticket_receipt()
    print(' ')
    print('Thank you for purchasing!!!! Choose option to close the application or continue.')
    data_write_file(Category,total_qty,unit_cost,total_cost)


#Main Menu Options
while options in ("y","yes","Y","Yes"):
    print('Selection Options')
    print('1.Show Price Details')
    print('2.Purchase Tickets')
    print('3.Exit')
    print('\n')
    choice=input('Choose a valid option as 1 or 2 or 3: ')
    print(' ')
    if choice=='1':
        price_detail()
        Buy_ticket=input('Do you want to purchase tickets? Y/N or y/n')
        print(' ')
        if Buy_ticket in ('y','Y'):
            purchase_ticket()

    elif choice=='2':
        purchase_ticket()

    elif choice=='3':
        print('Thank you for visiting us!!!!!!')
        break

    else:
        print('Choose a valid option')
        option="yes"
        
    
    
                      
              
            
    
        
        
            
                              
                              
