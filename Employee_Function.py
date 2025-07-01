import mysql.connector
#alter function
def alter():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
    mycursor=mydb.cursor()
    while True:
        print("\n\t\t Update Menu")
        print("\t\t------------")
        print("\t\t1.Track")
        print("\t\t2.Artist")
        print("\t\t3.Genre")
        print("\t\t4.Date of Entry")
        print("\t\t5.Number of Records Purchased")
        print("\t\t6.Price")
        print("\t\t7.I would not like to alter anything\n")
        x=input("\tWhat would you like to update? ")
        print()
        if x=="1":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=input("\tEnter the altered track name:")
                query="update playlist set Track='{}' where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")

        elif x=="2":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=input("\tEnter the altered Artist name:")
                query="update playlist set Artist='{}' where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")

        elif x=="3":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=input("\tEnter the altered Genre:")
                query="update playlist set Genre='{}' where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")

        elif x=="4":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=input("\tEnter the altered Date of Entry:")
                query="update playlist set DOE='{}' where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")

        elif x=="5":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=int(input("\tEnter the altered Number of Records Purchased:"))
                query="update playlist set No_Purchased={} where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")

        elif x=="6":
            a=int(input("\tChoose the record number to be updated:"))
            mycursor.execute('select * from playlist where Rno={}'.format(a))
            c=mycursor.fetchall()
            if c==[]:
                print("\tRecord doesn't exist")
            else:
                b=float(input("\tEnter the altered Price:"))
                query="update playlist set Price={} where Rno={}".format(b,a)
                mycursor.execute(query)
                mydb.commit()
                print("\tRecord updated!")
        elif x=="7":
            break
        else:
            print("\tInvalid Option")
            key=input("\tPress any key to continue.")

#insert function
def insert(): 
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
    mycursor=mydb.cursor()
    while True:
        an=input('\tEnter the Record Number:')
        try:
            a=int(an)
        except:
            print('\tMake sure your record number contains numeric values only.\n')
            continue
        break
    mycursor.execute('select * from playlist where Rno={}'.format(a))
    c=mycursor.fetchall()
    if c!=[]:
        print("\tRecord number already exists.\n")
    else:
        try:
            b=input("\tEnter the track name:")
            c=input('\tEnter Name of the Artist:')
            d=input('\tEnter the Genre:')
            e=input('\tEnter the date of entry (yyyy-mm-dd):')
            f=float(input('\tEnter the price of the record:'))
            query="insert into playlist values({},'{}','{}','{}','{}',0,{})".format(a,b,c,d,e,f)
            mycursor.execute(query)
            mydb.commit()
            print('\tRecord added.\n')
        except:
            print('\tAn error occured, please try again.\n')


#display function
import mysql.connector
from tabulate import tabulate
def display():
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
    mycursor=mydb.cursor()
    mycursor.execute('\tselect * from playlist')
    result=mycursor.fetchall()
    print(tabulate(result,headers=['Rno','Track','Artist','Genre','Date of Entry','No.  of records purchased','Price'],tablefmt='psql'))

#delete function
def delete():     
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='limejuice', database='music_barn')
    mycursor=mydb.cursor()
    mycursor.execute('select count(*) from playlist')
    c=mycursor.fetchall()
    a=int(input('\tEnter the record number to be deleted:'))
    mycursor.execute('delete from playlist where Rno={}'.format(a))
    mydb.commit()
    mycursor.execute('select count(*) from playlist')
    c1=mycursor.fetchall()
    if c1<c:
        print('\tRecord deleted')
    else:
        print("\tRecord doesn't exist")