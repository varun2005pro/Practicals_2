tup = eval(input("Enter a tuple :-"))
count = 0
for i in tup :
      if count <  tup.count(i):
            count = tup.count(i)

for i in tup :
      if count == tup.count(i) :
            print("mode = ",i)
            break
#BY VARUN GAUTAM(XI-A)
