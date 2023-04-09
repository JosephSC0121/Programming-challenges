import math
import random
#hello world 1-5
def hello_world(): 
    msg = "Hello world"
    for i in range(6):
        print(msg)
#Calculate and square root 2-3 
def calculate():
    num1 = int(input("Type a number: "))
    num2 = int(input("Type a number: "))
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
if __name__ == "__main__":
    #choose the funtion 
    largest()
