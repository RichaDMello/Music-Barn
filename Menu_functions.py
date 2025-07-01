from tabulate import tabulate
from Cart_Functions import *
from employeefunctions import *
import mysql.connector 
mydb=mysql.connector.connect(host='localhost',user='root',database='music_barn',passwd='limejuice')
mycursor=mydb.cursor()
#function for customer-The Music Barn
def Customer():
    print('\t\t-------------------------------------------------')
    print('\t\tHello! Welcome to The Music Barn! Happy Shopping!')
    print('\t\t-------------------------------------------------\n')
   
    while True:
        print('\t\taming Menu:')
        print('\t\t----------')
        print('\t\t1.All The Songs We Have\n\t\t2.Add To Cart\n\t\t3.Remove from cart\n\t\t4.Display Cart\n\t\t5.Proceed To Checkout\n\t\t6.Suggestions\n\t\t7.Search for more music\n\t\t8.Exit\n')
        ch=input('\tWhat would you like to do? ')
        print()
        if ch=='1':
            Display_menu()
        elif ch=='2':
            Add_to_cart()
        elif ch=='3':
            Remove_from_cart()
        elif ch=='4':
            Display_cart()
        elif ch=='5':
            Checkout()
        elif ch=='6':
            Suggestions()
        elif ch=='7':
            Searchmusic()
        elif ch=='8':
            print('\tThank you for shopping at the Music Barn. Please come again!')
            break
        else:
            print('\ERROR! Invalid Option! Please Try Again!')
            key=input('\tPress any key to continue')

def Employee():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
    mycursor=mydb.cursor()
    while True:
        a=input('\tEnter employee ID:')
        print()
        try:
            n=int(a)
        except:
            print('\tMake sure your employee ID has only number characters.')
            continue
        mycursor.execute("select EmpName from emp where EmpID={}".format(n))
        res=mycursor.fetchall()
        if res==[]:
            print('\tInvalid Employee Number. Try again.')
            ch=input('\tPress any key to continue')
        else:
            break
    w=res[0]
    print('\tWelcome back',w[0],'!\n')
    while True:
        print('\t\tMain Menu')
        print('\t\t---------')
        print('\t\t1.Insert new values \n\t\t2.Alter the existing values \n\t\t3.Display the records \n\t\t4.Delete a record \n\t\t5.Exit\n')
        x=input('\tWhat are we doing today? ')
        print()
        if x=='1':
            insert()
        elif x=='2':
            alter()
        elif x=='3':
            display()
        elif x=='4':
            delete()
        elif x=='5':
            print('\tGood Bye! Have a nice day!\n')
            break
        else:
            print('\tInvalid option')
            q=input('\tPress any key to continue')
