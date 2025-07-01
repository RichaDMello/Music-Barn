import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
mycursor=mydb.cursor()
from tabulate import tabulate
#Add to cart function
def Add_to_cart():
    while True:
        n=input('\tEnter Record Number of the track:')
        try:
            no=int(n)
        except:
            print('Invalid record number. Make sure it is only number character')
        break
    query1='create table if not exists Cart(rno int(5) primary key, title varchar(20),artist varchar(20), price decimal(5,2))'
    mycursor.execute(query1)
    mydb.commit()
    try:
        query2='select * from playlist where rno={}'.format(no)
        mycursor.execute(query2)
        result=mycursor.fetchall()
        for k in result:
            title,artist,pri=k[1],k[2],k[6]
        query3='insert into Cart values({},"{}","{}",{})'.format(no,title,artist,pri)
        mycursor.execute(query3)
        mydb.commit()
        print('\tAdded to cart.')
        query4='select count(*) from cart'
        mycursor.execute(query4)
        count=mycursor.fetchall()
        print('\tThere are',count[0][0],'items in your cart.')
    except:
        print('\tIncorrect record number, try again please.')
    print()
def Display_cart():
    query='select * from cart'
    mycursor.execute(query)
    result=mycursor.fetchall()
    print()
    if result==[]:
        print('\tYour cart is empty.')
        ch=input('\tPress any key to continue.')
        print()
        return
    print(tabulate(result,headers=['Record Number','Track','Artist','Price'],tablefmt='psql'))
    print()

def RecordNumber_sort():
    query='select * from playlist order by Rno'
    mycursor.execute(query)
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Record Number','Track','Artist','Genre','Release Date','Records Sold','Price'],tablefmt='psql'))

def Artist_sort():
    query='select * from playlist order by artist'
    mycursor.execute(query)
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Record Number','Track','Artist','Genre','Release Date','Records Sold','Price'],tablefmt='psql'))

def Dateofrec_sort():
    query='select * from playlist order by DOE'
    mycursor.execute(query)
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Record Number','Track','Artist','Genre','Release Date','Records Sold','Price'],tablefmt='psql'))

def Price_sort():
    query='select * from playlist order by price'
    mycursor.execute(query)
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Record Number','Track','Artist','Genre','Release Date','Records Sold','Price'],tablefmt='psql'))

          
#display menu function
def Display_menu():
    print('\t\tWould you like to see the music sorted by:')
    print('\t\t------------------------------------------')
    print('\t\t1.Record Number\n\t\t2.Artist\n\t\t3.Date of recording\n\t\t4.Price\n\t\t5.Return to Main Menu\n')
    while True:
        ch=input('\tTake Your Pick: ')
        print()
        if ch=='1':
            RecordNumber_sort()
        elif ch=='2':
            Artist_sort()
        elif ch=='3':
            Dateofrec_sort()
        elif ch=='4':
            Price_sort()
        elif ch=='5':
            break
        else:
            print('\tInvalid Option. Please try Again')
        print('\tPress 5 to return to Main Menu')
        print()

def Remove_from_cart():
    no=int(input('\tEnter record number to be removed:'))
    try:
        mycursor.execute('select count(*) from cart')
        c1=mycursor.fetchall()
        query='Delete from cart where rno={}'.format(no)
        mycursor.execute(query)
        mydb.commit()
        query4='select count(*) from cart'
        mycursor.execute(query4)
        count=mycursor.fetchall()
        if c1>count:
                print('\tRecord removed.')
        print('\tThere are',count[0][0],'items in your cart.\n')
    except:
        print('Incorrect record number. Please try again.')
    print()

def Checkout():
    query='select rno,price from cart'
    mycursor.execute(query)
    result=mycursor.fetchall()
    if result==[]:
        print('\tYour cart is empty. Add records you want to purchase to your cart and try again.')
    ans=input('\tAre you sure you would like to proceed to checkout? (y or n):')
    if ans=='n':
        print()
        return
    elif ans=='y':
        Price=0
        for k in result:
            Price+=k[1]
            no=k[0]
            query2='update playlist set No_Purchased=No_purchased+1 where rno={}'.format(no)
            mycursor.execute(query2)
            mydb.commit()
        print('\tTotal amount=',Price,'/-')
        print('\tPlease pay at the counter.')
        ch=input('\tPress any key when amount paid')
        query3='delete from cart'
        mycursor.execute(query3)
        mydb.commit()
        print()
    else:
        print('\tInvalid answer. Answer "y" or "n"')
        ch=input('\tPress any key to continue:')
        print()

#search function-customer
def Searchmusic():
    while True:
        print('\t\tHow would you like to look for more music?')
        print('\t\t------------------------------------------')
        print('\t\t1.By Track\n\t\t2.By Artist\n\t\t3.Exit')
        ch=input('\tWhich would you prefer: ')
        try:
            if ch=='1':
                Track_search()
            elif ch=='2':
                Artist_search()
            elif ch=='3':
                break
        except:
            print('\tInvalid Option!Please Try Again!')
            key=input('\tPress any key to continue')
        print()



#To search for music by the name of the song
def Track_search():
    L=[]
    print('\t*Remember song titles are case sensitive.*')
    songname=input('\tEnter Track to be Searched:')
    mycursor.execute('Select * from playlist where Track="{}"'.format(songname))
    result=mycursor.fetchall()
    if result==[]:
        print("\tTrack not found. We'll be sure to have it next time!")
        return
    for k in result:
        if k[1]==songname:
            L.append(k)
            print(tabulate(L,headers=['Rec No','Track','Artist','Genre','DOE','No. of Rec','Price'],tablefmt='psql'))
    print()


def Artist_search():
    L=[]
    print('\t* Remember Artist names are case sensitive.*')
    artistname=input('\tEnter name of Artist:')
    mycursor.execute('select * from playlist where Artist="{}"'.format(artistname))
    result=mycursor.fetchall()
    if result==[]:
        print("\tArtist not found. We'll be sure to have it next time!")
        return
    for k in result:
        if k[2]==artistname:
            L.append(k)
            print(tabulate(L,headers=['Rec No','Track','Artist','Genre','DOE','No. of Rec','Price'],tablefmt='psql'))
    print()
    
#function for suggestions
def Suggestions():
    while True:
        print("\t\tChoose a Genre and we'll give you our suggestions!")
        print('\t\t--------------------------------------------------')
        print('\t\t1.Best sellers\n\t\t2.Bollywood\n\t\t3.Country\n\t\t4.K-pop\n\t\t5.Pop\n\t\t6.Rock\n\t\t7.Exit\n')
        ch=input("\tSo what'll it be? " )
        try:
            if ch=='1':
                Bestsellers()
            elif ch=='2':
                Bollywood()
            elif ch=='3':
                Country()
            elif ch=='4':
                Kpop()
            elif ch=='5':
                Pop()
            elif ch=='6':
                Rock()
            elif ch=='7':
                break
        except:
            print('\tInvalid Option! Please Try Again.')
            l=input('\tPress any key to continue')
        print()


#bestseller function

def Bestsellers():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[4]>5:
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Genre','Recs Sold','Price'],tablefmt='psql'))

def Bollywood():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[3]=='Bollywood':
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Recs Sold','Price'],tablefmt='psql'))
     
def Country():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[3]=='Country':
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Recs Sold','Price'],tablefmt='psql'))

            
def Kpop():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[3] in'Kpop':
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Recs Sold','Price'],tablefmt='psql'))

def Pop():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[3]=='Pop':
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Recs Sold','Price'],tablefmt='psql'))

def Rock():
    L=[]
    mycursor.execute('Select Rno,Track,Artist,Genre,No_purchased,price from playlist')
    resultg=mycursor.fetchall()
    for k in resultg:
        if k[3]=='Rock':
            L.append(k)
    print(tabulate(L,headers=['Rec No','Track','Artist','Recs Sold','Price'],tablefmt='psql'))
