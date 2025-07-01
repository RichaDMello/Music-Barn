from Menu_Functions import *
print()
print('\t\t\t~~~~~~~~~~~~~~~~~~~~')
print('\t\t\t-----Welcome to-----')
print('\t\t\t\/\The Music Barn/\/\n')
print('\t\t\t~~~~~~~~~~~~~~~~~~~~')
print('\t\tHere to help with your music needs!\n')
print()
while True:
    print('\t\tAre you signing in as \n\t\t1.a Customer\n\t\t2.an Employee\n\t\t3.Exit program')
    print()
    ch=input('\t\tEnter choice:')
    print()
    if ch=='1':
        Customer()
        break
    elif ch=='2':
        n=5
        for k in range(n):
            Pass=input('\t\tEnter password:')
            print()
            if Pass=='********':
                l=1
                Employee()
                break
            else:
                l=n-1-k
                print('\t\tIncorrect password. You have',l,'tries left.')
                j=input('\t\tPress any key to continue')
        if l==0:
            break
    elif ch=='3':
        print('\tThank you!')
        break
    else:
        print('\tIncorrect option number, please try again')
        ch=input('\tPress any key to continue')
