tup= ()
while True :
      roll = int(input("Enter a roll number :- "))
      name = input("Enter name :-")
      mark = input("Enter marks (OUT OF 30):-")
      subject=input("Enter the subject name :-")
      tup += ( (roll,name,subject,mark ),)
      user = input("Do you want to quit enter yes =")
      if user == "yes":
            print(tup)
            break
#BY VARUN GAUTAM(XI-A)
