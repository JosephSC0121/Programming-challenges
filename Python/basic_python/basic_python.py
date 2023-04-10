import math
import random
import numpy as np
from datetime import date
from statistics import mode
#hello world 1-5
def hello_world(): 
    msg = "Hello world"
    for i in range(6):
        print(msg)
#Calculate and square root 2-3 
def calculate(num1,num2):
    print("Add: ",num1+num2, "Sub: ", num1-num2, "mult: ", num1*num2, "Div: ", num1/num2) 
#Swap varibales 4
def swap():
    a = 10
    b = 20
    print("a =", a ,"b =", b)
    a,b = b, a   
    print("a =", a ,"b =", b)
#random num 6
def random_num():
    num = random.randint(1,100)
    print(num)
    return num
#even or odd 7
def even_odd():
    #funtion
    num = random_num() 
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")
#Find largest 8
def largest():
    list = [10,2,3,40,10,50,7,10]
    aux = list[0]
    for num in list:
        if num > aux:
            aux=num
    print(aux)
    # aux = max(list)
#Prime number 9
def prime_number(num):
    print(num)
    if num < 2:
        return print("Not a prime number")
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return print("Not a prime number") 
    return print("Prime number")
#Factorial 10 
def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact=fact*i
    print(fact)
    # print(math.factorial(n))
#ASCII value 11
def findASCII(character):
    ASCII = ord(character)
    print(ASCII)
#Date 12
def date_now():
    today = date.today()
    print(today)

#matrix 13 14 
def matrix_operations():

    matrix = np.random.randint(0,10,(3,3))
    matrix_two = np.random.randint(0,10,(3,3))
    add = matrix+matrix_two
    sub = matrix - matrix_two
    mult = matrix.dot(matrix_two)
    trans =  matrix.T

    print("\ninitial matrix\n", matrix, matrix_two, "\nAdd: \n", add, "\nub: \n", sub, "\nmult: \n", mult, "\nTrans: \n", trans)
#sort characters 15
def sort_characters():
    list= ['d','x','b','a','y','g']
    sorted_list = sorted(list)
    print(sorted_list)

#most common 
def most_common():
    list = [1,1,2,3,5,2,4,6,7,8,9,8,2]
    most_common = mode(list)
    print(most_common)

if __name__ == "__main__":

    #choose the exercise 
    most_common()



