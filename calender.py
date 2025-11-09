# calender

import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='admin',database='my_project')
cur=con.cursor()
d={1:('Jan',31),2:('Feb',28,29),3:('Mar',31),4:('Apr',30),5:('May',31),6:('June',30),7:('July',31),8:('Aug',31),9:('Sep',30),10:('Oct',31),11:('Nov',30),12:('Dec',31)}
d1={1:'Sun',2:'Mon',3:'Tue',4:'Wed',5:'Thu',6:'Fri',7:'Sat'}
def calendar(x,b,a):
    q='select dayname("{}") as today'.format(x)
    cur.execute(q)
    s=cur.fetchone()
    print()
    print('\t\t','Month -',d[int(b)][0])
    print()
    for i in d1:
        print(d1[i],end='\t')
        if s[0][:3]==d1[i] :
            x=i
    print()
    if int(a)%4==0 and int(b)==2:
        z=30
    else:
        z=d[int(b)][1]
    print('   \t'*(x-1),end='')
    for i in range(1,9-x):
        print(i,' \t ',end='')
    print()
    c=0
    for i in range(9-x,z+1):
        print(' ',end='')
        print(i,end=' \t')
        c+=1
        if c==7:
            print()
            c=0
    print()
    print()
def work1():
    print()
    while True:
        a=input('Enter date in format (yyyymmdd)')
        if a.isdigit() and int(a[4:6]) in d and len(a)==8:
            condition=(int(a[:4])%4==0 and (int(a[6:])<=d[int(a[4:6])][1] or int(a[6:])<=d[int(a[4:6])][2])) or (int(a[:4])%4!=0 and int(a[6:])<=d[int(a[4:6])][1])
            if condition :
                q='select dayname("{}") as today'.format(a)
                cur.execute(q)
                s=cur.fetchall()
                print('Day',s[0][0])
                print()
                break
            else:
                print('Enter correct format')
        else:
            print('Enter correct format')
def work2():
    print()
    while True:
        a=input('Enter year:')
        b=input('Enter month number:')
        if  a.isdigit() and b.isdigit() and len(a)==4 and 12>=int(b)>=1:
            if len(b)==1:
                x=a+'0'+b+'01'
                break
            elif len(b)==2:
                x=a+b+'01'
                break
            else:
                print('Entered incorrect entry')
        else:
            print('Entered incorrect entry')
    calendar(x,b,a)
def work3():
    q='select curdate() as today'
    cur.execute(q)
    s=cur.fetchone()
    q='select dayname(curdate()) as today'
    cur.execute(q)
    a=cur.fetchone()
    print("\nToday's date and day-",s[0],',',a[0])
    print()
def work4():
    print()
    while True:
        a=input('Enter year:')
        if  a.isdigit() and len(a)==4:
            break
        else:
            print('Entered incorrect entry')
    for i in range(1,13):
        b=str(i)
        if len(b)==1:
            x=a+'0'+b+'01'
        else:
            x=a+b+'01'
        calendar(x,b,a)
while True:
    print('\tCalender Window\t')
    print('What you want to see?')
    print("1.Today's date and day\n2.Enter today's date and see day\n3.Enter month number and year see that month\n4.Enter year and see full calender\n5.Exit")
    a=int(input('Enter your choice:'))
    if a==2:
        work1()
    elif a==3:
        work2()
    elif a==1:
        work3()
    elif a==5:
        print('\tThank you\t')
        break
    elif a==4:
        work4()
    else:
        print('Enter accordinly\n')



