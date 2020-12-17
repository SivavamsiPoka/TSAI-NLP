#write a program in python for first element in the List
print(l[0])
#Calculator Program in Python
def calc(n):

    s=0

    p=1

    a=int(input("first number"))

    b=int(input("second number"))

    if n==1:

        s=a+b

        print("sum",s)

    elif n==2:

        p=a*b

        print("prod",p)

    elif n==3:

        s=a-b

        print("diff",s)

    else:

        p=a/b

        print("divide",p)

i=int(input("enter for calculation 1. add 2. product 3.subtract 4.divide"))

calc(i)
#Heap Sort Program In Python
def heapify(arr, n, i):

    largest = i

    l = 2 * i + 1

    r = 2 * i + 2



    if l < n and arr[i] < arr[l]:

        largest = l



    if r < n and arr[largest] < arr[r]:

        largest = r



    if largest != i:

        arr[i],arr[largest] = arr[largest],arr[i]



        heapify(arr, n, largest)



def heapSort(arr):

    n = len(arr)

    for i in range(n, -1, -1):

        heapify(arr, n, i)

    for i in range(n-1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]

        heapify(arr, i, 0)

arr = [ 12, 11, 13, 5, 6, 7]

heapSort(arr)

n = len(arr)

print ("Sorted array is:")

for i in range(n):

    print ("%d" %arr[i])
#Insertion Sort Program in Python
def insort(a):

    for i in range(1, len(a)):

        b=a[i]

        j=i-1

        while j>=0 and b<a[j]:

            a[j],a[j+1]=a[j+1],a[j]

            j -= 1



a = [ 5, 6, 4, 1,3,2]

insort(a)

for i in a:

    print (i)
#Linear Search in Python
n=int(input("Enter the number to be searched (1-10):"))

a=[1, 2, 4, 3,5,7,9,8,6,10 ]

for i in range(1,(len(a))):

    if n==a[i]:

        print("number found at",i+1)
#GCD of two numbers in Python
def gcd(a,b):

    small=0

    gd=0

    if a>b:

        small==b

    else:

        small==a

    for i in range(1, small+1):

        if((a % i == 0) and (b % i == 0)):

            gd=i

    return gd

a=int(input("Enter the first number: "))

b=int(input("Enter second number: "))

t=gcd(a,b)

print("GCD is:",t)
#Square Root Program in Python
def sqrt(n):

    x=n**0.5

    print(x)

n=int(input("Enter the number whose square root you need to find: "))

sqrt(n)
#Program to convert decimal to binary in Python
def dectobin(n):

    if n>1:

        dectobin(n//2)

    print(n%2,end='')

n=int(input("Enter the decimal number: "))

dectobin(n)
#Print diamond pattern in Python
n=int(input("enter the number of rows"))

for i in range(n):

    for j in range(1,int((n/2))-i+3):

        print(sep=" ",end=" ")

    for k in range(1,i+2):

        print("*", end=" ")



    print()

for i in range(n):

    for j in range(1,5-(int((n/2))-i+3)+2):

        print(sep=" ",end=" ")

    for k in range(1,5-i):

        print("*", end=" ")

    print()
#Python program for compound interest
n=int(input("Enter the principle amount:"))

rate=int(input("Enter the rate:"))

years=int(input("Enter the number of years:"))

for i in range(years):

    n=n+((n*rate)/100)

print(n)
#Program for binary search using recursion in Python
def binary(a, fir, las, term):

    mid=int((fir+las)/2)

    if term>a[mid]:

        binary(a, mid, las, term)

    elif term<a[mid]:

        binary(a,fir, mid, term)

    elif term==a[mid]:

        print("Number found at", mid+1)

    else:

        print("Number is not there in the array")

b=[1,2,3,4,5]

fir=0

las=len(b)

term=4

binary(b,fir,las,term)
#Program to print the biggest number out of three in Python
l=[]

for i in range(3):

    n=int(input("Enter the no.:"))

    l.append(n)

big=0

for i in l:

    if i>big:

        big=i;

print("The Biggest no. of all 3 is:",big)
#Bubble Sort in Python
arr=[1,5,9,3,2,6]

n=len(arr)

for i in range(n):

    for j in range(0,n-i-1):

        if arr[j]>arr[j+1]:

            temp=arr[j+1]

            arr[j+1]=arr[j]

            arr[j]=temp

print("Sorted Array : ", arr )
#Reverse string program in Python
string=input("Enter a string:")

revstring=string[::-1]

print(revstring)
#Area of Circle Program in Python
r = int(input("Enter the radius:"))

area = 3.14*r*r

print("The area is:", area)
#Anagram Program in Python
a=input("Enter string 1:")

b=input("Enter string 2:")

count=0

for i in a:

    for j in b:

        if i==j:

            count=count+1

if count==len(a):

    print("Strings are anagram of each other.")

else:
    print("Strings are not anagram of each other.")
#Area of Triangle Python Program
a=int(input("area with sides(1) or base-height(2) :"))

if a==2:

    b=int(input("enter the base:"))

    h=int(input("enter the height:"))

    area= float(0.5*b*h)

    print("area is", area)

else:

    s1=float(input("enter side 1:"))

    s2=float(input("enter side 2:"))

    s3=float(input("enter side 3:"))

    s=float((s1+s2+s3)/2)

    area = (s*(s-s1)*(s-s2)*(s-s3)) ** 0.5

    print("area is", area)
#Python program to find average of N numbers
n=int(input("Enter the total number you want to enter:"))

sum=0

for i in range(n):

    x=int(input("Enter the number:"))

    sum=sum+x

avg=sum/n

print("Average=",avg)
#Armstrong Number Program in Python
n=input("Enter a number :")

l=len(n)

n=int(n)

a=n

arm=0

for i in range(l+1):

    b=a%10

    a=a/10

    arm=arm+(b**l)

if (arm != n):

    print("It is not an Armstrong no.")

else:

    print("It is an Armstrong no.")
#Factorial Program in Python
n= int(input("Enter the number you want to find the factorial of: "))

prod=1

for i in range(1,n+1):

    prod=prod*i

print(prod)
#Program to Check Leap year in Python
n= int(input("Enter the year you want to check?"))

if (n%4==0):

    if (n%100==0):

        if (n%400==0):

            print("It is a leap year")

        else:

            print("It is not a leap year")

    else:

        print("It is a leap year")

else:

    print("It is not a leap year")
#Program to search an element using Binary Search in Python
def binsearch(A, a, b, q):

    m=int((a+b)/2)

    if (q> A[m]):

        binsearch(A, m, b, q)

    elif (q<A[m]):

        binsearch(A, a, m, q)

    elif (q== A[m]):

        print("the element is found on index:" )

        print(m+1)

    else:

        print("item not present in the list")

n=int(input("enter the total no. of elements: "r))

print("enter the elements:")

A=[]

for i in range(n):

    a=int(input())

    A.append(a)

print("enter the no. to be searched:")

q=int(input())

binsearch(A, 0, n-1, q)
#Fibonacci series in Python
n= int(input("enter the number of elements you want in series:"))
c=[]
c.append(0)
c.append(1)
a=0
b=1
d=0

for i in range( 1, n-1):
    d=a+b
    c.append(d)
    a=b
    b=d

for i in c:
    print(i)
#Prime Number Program in Python
n= int(input( "enter the number that has to be checked:"))
a=0
for i in range(2,int((n/2))):
    if(n%i ==0):
        a=a+1
if(a>1):
    print("it is not prime")
else:
    print("it is prime ")
#program to check given number is palindrome or not
n= int(input("Enter the number:"))
temp=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if (temp==rev) :
    print('It is a palindrome ')
else:
    print('It is not a palindrome')
#Program to add two numbers in Python
a=int(input('enter the first number:'))

b=int(input('enter the second number:'))

sum=a+b

print('sum:', sum)
#Program to Print Hello World in Python
print('Hello World!')
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=",")
print("\b")
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")
#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
n = int(input())
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)
#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)
#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
n = int(input())


def shortFact(x):
    return 1 if x <= 1 else x * shortFact(x - 1)


print(shortFact(n))
#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
n = int(input())
ans = {}
for i in range(1, n + 1):
    ans[i] = i * i
print(ans)
#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

n = int(input())
ans = {i: i * i for i in range(1, n + 1)}
print(ans)

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
lst = input().split(",")
tpl = tuple(lst)  # tuple method converts list to tuple

print(lst)
print(tpl)
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i j.*Note: i=0,1.., X-1; j=0,1,¡­Y-1.
x, y = map(int, input().split(","))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i * j)
    lst.append(tmp)

print(lst)
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i j.*Note: i=0,1.., X-1; j=0,1,¡­Y-1.
x, y = map(int, input().split(","))
lst = [[i * j for j in range(y)] for i in range(x)]
print(lst)

#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lst = []

while input():
    x = input()
    if len(x) == 0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s


for line in map(str.upper, user_input()):
    print(line)
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
word = input().split()

for i in word:
    if (
        word.count(i) > 1
    ):
        word.remove(i)

word.sort()
print(" ".join(word))
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
word = input().split()
[
    word.remove(i) for i in word if word.count(i) > 1
]
word.sort()
print(" ".join(word))
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
word = sorted(
    list(set(input().split()))
)
print(" ".join(word))
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
def check(x):
    total, pw = 0, 1
    reversed(x)

    for i in x:
        total += pw * (ord(i) - 48)
        pw *= 2
    return total % 5


data = input().split(",")
lst = []

for i in data:
    if check(i) == 0:
        lst.append(i)

print(",".join(lst))
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
    return int(x, 2) % 5 == 0


data = input().split(",")

data = list(
    filter(check, data)
)
print(",".join(data))
#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

data = input().split(",")
data = list(
    filter(lambda i: int(i, 2) % 5 == 0, data)
)
print(",".join(data))
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
lst = []

for i in range(1000, 3001):
    flag = 1
    for j in str(i):
        if ord(j) % 2 != 0:
            flag = 0
    if flag == 1:
        lst.append(str(i))

print(",".join(lst))
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
def check(element):
    return all(
        ord(i) % 2 == 0 for i in element
    )


lst = [
    str(i) for i in range(1000, 3001)
]
lst = list(
    filter(check, lst)
)
print(",".join(lst))
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

lst = [str(i) for i in range(1000, 3001)]
lst = list(
    filter(lambda i: all(ord(j) % 2 == 0 for j in i), lst)
)
print(",".join(lst))
#Write a program that accepts a sentence and calculate the number of letters and digits.
word = input()
letter, digit = 0, 0

for i in word:
    if ("a" <= i and i <= "z") or ("A" <= i and i <= "Z"):
        letter += 1
    if "0" <= i and i <= "9":
        digit += 1

print("LETTERS {0}\nDIGITS {1}".format(letter, digit))
#Write a program that accepts a sentence and calculate the number of letters and digits.
word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        digit += 1
print(
    f"LETTERS {letter}\n{digits}"
)
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
word = input()
upper, lower = 0, 0

for i in word:
    if "a" <= i and i <= "z":
        lower += 1
    if "A" <= i and i <= "Z":
        upper += 1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
word = input()
upper, lower = 0, 0

for i in word:
    lower += i.islower()
    upper += i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
word = input()
upper = sum(
    1 for i in word if i.isupper()
)
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

string = input("Enter the sentense")
upper = 0
lower = 0
for x in string:
    if x.isupper() == True:
        upper += 1
    if x.islower() == True:
        lower += 1

print("UPPER CASE: ", upper)
print("LOWER CASE: ", lower)

#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
a = input()
total, tmp = 0, str()

for i in range(4):
    tmp += a
    total += int(tmp)

print(total)
#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total)
#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
lst = input().split(",")

seq = []
lst = [int(i) for i in lst]
for i in lst:
    if i % 2 != 0:
        i = i * i
        seq.append(i)


seq = [
    str(i) for i in seq
]
print(",".join(seq))
#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
lst = [str(int(i) ** 2) for i in input().split(",") if int(i) % 2]
print(",".join(lst))
#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
ss = input().split()
word = sorted(set(ss))

for i in word:
    print("{0}:{1}".format(i, ss.count(i)))
#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
ss = input().split()
dict = {}
for i in ss:
    i = dict.setdefault(
        i, ss.count(i)
    )

dict = sorted(
    dict.items()
)
for i in dict:
    print("%s:%d" % (i[0], i[1]))
#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
ss = input().split()
dict = {
    i: ss.count(i) for i in ss
}
dict = sorted(
    dict.items()
)
for i in dict:
    print("%s:%d" % (i[0], i[1]))

#Write a method which can calculate square value of number


n = int(input())
print(n ** 2)
#Define a function which can compute the sum of two numbers.
sum = lambda n1, n2: n1 + n2
print(sum(1, 2))
#Define a function that can convert a integer into a string and print it in console.
sum = lambda s1, s2: int(s1) + int(s2)
print(sum("10", "45"))
#Define a function that can accept two strings as input and concatenate them and then print it in console.
sum = lambda s1, s2: s1 + s2
print(sum("10", "45"))
#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
def printVal(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
printVal(s1, s2)
#Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
func = (
    lambda a, b: print(max((a, b), key=len))
    if len(a) != len(b)
    else print(a + "\n" + b)
)
#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def printDict():
    dict = {i: i ** 2 for i in range(1, 21)}
    print(dict)


printDict()
#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
def printDict():
    dict = {i: i ** 2 for i in range(1, 21)}
    print(dict.keys())


printDict()
#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)


printList()
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
def printList():
    lst = [i ** 2 for i in range(1, 21)]

    for i in range(5):
        print(lst[i])


printList()
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
func = lambda: ([i ** 2 for i in range(1, 21)][:5])
print(*(func()), sep="\n")
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(19, 14, -1):
        print(lst[i])


printList()
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5, 20):
        print(lst[i])


printList()
#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))


printTupple()

#Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))


print(square_of_numbers())
#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(0, 5):
    print(tpl[i], end=" ")
print()
for i in range(5, 10):
    print(tpl[i], end=" ")
#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lst1, lst2 = [], []

for i in range(0, 5):
    lst1.append(tpl[i])

for i in range(5, 10):
    lst2.append(tpl[i])

print(lst1)
print(lst2)
#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lt = int(len(tup) / 2)
print(tup[:lt], tup[lt:])

#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("The Original Tuple:", tp)

[
    print("Splitted List :{List}".format(List=tp[x : x + 5]))
    for x in range(0, len(tp), 5)
]
#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl1 = tuple(i for i in tpl if i % 2 == 0)
print(tpl1)
#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tpl1 = tuple(
    filter(lambda x: x % 2 == 0, tpl)
)
print(tpl1)
#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")
#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
input = input("Enter string:")
output = "".join(
    ["Yes" if input == "yes" or input == "YES" or input == "Yes" else "No"]
)
print(str(output))
#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x ** 2, li)
print(list(squaredNumbers))
#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
def even(x):
    return x % 2 == 0


def squer(x):
    return x * x


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = map(
    squer, filter(even, li)
)
print(list(li))
#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
def even(x):
    return x % 2 == 0


evenNumbers = filter(even, range(1, 21))
print(list(evenNumbers))
#Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
def sqr(x):
    return x * x


squaredNumbers = list(map(sqr, range(1, 21)))
print(squaredNumbers)
#Write a function to compute 5/0 and use try/except to catch the exceptions.
def divide():
    return 5 / 0
#Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
email = "john@google.com"
email = email.split("@")
print(email[0])
#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
email = input().split()
ans = []
for word in email:
    if word.isdigit():
        ans.append(word)
print(ans)
#Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
email = input().split()
ans = [word for word in email if word.isdigit()]
print(ans)
#Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
s = input()
u = s.encode("utf-8")
print(u)
#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i / (i + 1)
print(round(sum, 2))
#Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=0 with a given n input by console (n>0).
def f(n):
    if n == 0:
        return 0
    return f(n - 1) + 100


n = int(input())
print(f(n))
#Please write assert statements to verify that every number in the list [2,4,6,8] is even.


data = [2, 4, 5, 6]
for i in data:
    assert i % 2 == 0, "{} is not an even number".format(i)
#Please write a program which accepts basic mathematic expression from console and print the evaluation result.
expression = input()
ans = eval(expression)
print(ans)
#Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

def binary_search_Ascending(array, target):
    lower = 0
    upper = len(array)
    print("Array Length:", upper)
    while lower < upper:
        x = (lower + upper) // 2
        print("Middle Value:", x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x


Array = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]
print("The Value Found at Index:", binary_search_Ascending(Array, 82))
#Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
idx = 0


def bs(num, num_list):
    global idx
    if len(num_list) == 1:
        if num_list[0] == num:
            return idx
        else:
            return "No exit in the list"
    elif num in num_list[: len(num_list) // 2]:
        return bs(num, num_list[: len(num_list) // 2])
    else:
        idx += len(num_list) // 2
    return bs(num, num_list[len(num_list) // 2 :])


print(bs(66, [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99, 100]))
