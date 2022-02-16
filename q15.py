a = eval(input("Enter tuple"))
sum = 0
mean = 0
me= 0
for i in range (len(a)):
        sum = 0
        for j in range (len(a[i])):
                sum = sum+a [i][j]
        mean = sum /(j +1)
        print ("Mean element  ", i + 1 , ":",mean)
        me += mean
print ("Mean of means : ",me /3)
#BY VARUN GAUTAM(XI-A)
