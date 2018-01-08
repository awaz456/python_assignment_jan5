my_list = list(range(0,100))
my_list=list(filter(lambda x:x%2!=0,my_list))
#4.filter prime numbers
fp = open("D:\\python class\\primes.txt","a")

for num in my_list:
    for i in range(2,num-1):
        if (num%i == 0):
            break
    else:
        fp.write("{}\t".format(str(num)))
fp.close()

#5.using context manager
with open("D:\\python class\\primes1.txt","a") as fp:
    for num in my_list:
        for i in range(2, num - 1):
            if (num % i == 0):
                break
        else:
            fp.write("{}\t".format(str(num)))

#6.read txt file created
with open("D:\\python class\\primes1.txt","r")as fp:
    print(fp.read())
