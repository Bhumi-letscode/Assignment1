#1.Write a program that takes two numbers as input and prints their sum.

x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
sum=x+y
print("The sum of the two numbers is: ",sum)

#2.Write a python program that checks whether a given number is even or odd.

num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

#3.Write a python program that calculates the factorial of a given number.

num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial does not exist for negative numbers.")
elif num==0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,num+1):
        factorial=factorial*i
print("The factorial of the number is: ",factorial)

#4.Write a program that asks the user for their name and then prints a greeting message.

name=input("Enter your name: ") 
print("Hello",name) 

#5.Write a program that takes a string input from the user and writes it to a text file.

string=input("Enter a string: ")
file=open("string.txt","w")
file.write(string)
file.close()

#6.Write a program that reads the content of a text file and prints it to the console.

file=open("string.txt","r")
print(file.read())
file.close()

#7.Write a python program that takes a string as input and returns its length.

string=input("Enter a string: ")
print("The length of the string is: ",len(string))

#8.Write a python program that concatenates two strings and returns the result.

string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
result=string1+string2
print("The concatenated string is: ",result)

#9.Write a python program that checks if a substring is present in a given string.

string=input("Enter a string: ")
substring=input("Enter a substring: ")
if substring in string:
    print("The substring is present in the string.")
else:
    print("The substring is not present in the string.")

#10.Write a python program that converts a given string to uppercase.

string=input("Enter a string: ")
print("The string in uppercase is: ",string.upper())

#11.Write a python program that generates the first n numbers in the Fibonacci sequence.

n=int(input("Enter the number of terms: "))
a=0
b=1
count=0
if n<=0:
    print("Enter a positive integer.")
elif n==1:
    print("The Fibonacci sequence is: ",a)
else:
    print("The Fibonacci sequence is: ")
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c

#12.Write a python program that calculates the sum of the digits of a given number.

num=int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print("The sum of the digits of the number is: ",sum)

#13.Write a program that asks the user for their birth year and calculates their age.

birth_year=int(input("Enter your birth year: "))
current_year=2021
age=current_year-birth_year
print("Your age is: ",age)

#14.Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines=[]
while True:
    line=input("Enter a line: ")
    if line:
        lines.append(line)
    else:
        break
for line in lines:
    print(line)

#15.Write a program that reads data from a CSV file and prints it to the console.

import csv
with open("data.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#16.Write a program in python that counts the frequency of each character in a string.

string=input("Enter a string: ")
frequency={}
for char in string:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print("The frequency of each character in the string is: ",frequency)

#17.Write a program in python that converts a given string to title case (first letter of each word capitalized).

string=input("Enter a string: ")
print("The string in title case is: ",string.title())

#18.Write a python program that checks if two strings are anagrams of each other.

string1=input("Enter the first string: ")
string2=input("Enter the second string: ")
if sorted(string1)==sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#19.Write a python program that removes all punctuation from a given string.

string=input("Enter a string: ")
punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punctuation=""
for char in string:
    if char not in punctuation:
        no_punctuation=no_punctuation+char
print("The string without punctuation is: ",no_punctuation)

#20.Write a python program that takes a list of numbers and returns their sum.
#     
n=int(input("Enter the number of elements in the list: "))
list=[]
sum=0
for i in range(n):
    element=int(input("Enter an element: "))
    list.append(element)
for element in list:
    sum=sum+element
print("The sum of the elements in the list is: ",sum)

#21.Write a python program that counts the occurrences of a specific element in a list.

n=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(n):
    element=int(input("Enter an element: "))
    list.append(element)
element=int(input("Enter the element to count: "))
count=0
for i in list:
    if i==element:
        count=count+1
print("The number of occurrences of the element in the list is: ",count)

#22.Write a python program that returns the minimum and maximum values in a list of numbers.

n=int(input("Enter the number of elements in the list: "))
list=[]
for i in range(n):
    element=int(input("Enter an element: "))
    list.append(element)
print("The minimum value in the list is: ",min(list))
print("The maximum value in the list is: ",max(list))

#23.Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

temp=float(input("Enter the temperature: "))
unit=input("Enter the unit (C/F): ")
if unit=="C":
    fahrenheit=(temp*9/5)+32
    print("The temperature in Fahrenheit is: ",fahrenheit)
elif unit=="F":
    celsius=(temp-32)*5/9
    print("The temperature in Celsius is: ",celsius)
else:
    print("Invalid unit.")

#24.Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
operator=input("Enter the operator (+, -, *, /): ")
if operator=="+":
    print("The sum of the two numbers is: ",x+y)
elif operator=="-":
    print("The difference of the two numbers is: ",x-y)
elif operator=="*":
    print("The product of the two numbers is: ",x*y)
elif operator=="/":
    print("The quotient of the two numbers is: ",x/y)
else:
    print("Invalid operator.")

#25.Write a program that copies the contents of one text file to another.

file1=open("file1.txt","r")
file2=open("file2.txt","w")
file2.write(file1.read())
file1.close()
file2.close()

#26.Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

string=input("Enter a string: ")
prefix=input("Enter the prefix: ")
suffix=input("Enter the suffix: ")
if string.startswith(prefix):
    print("The string starts with the prefix.")
else:
    print("The string does not start with the prefix.")
if string.endswith(suffix):
    print("The string ends with the suffix.")
else:
    print("The string does not end with the suffix.")

#27.Write a program in python that converts a string into a list of its characters.

string=input("Enter a string: ")
list=[]
for char in string:
    list.append(char)
print("The list of characters in the string is: ",list)