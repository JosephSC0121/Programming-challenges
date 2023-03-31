def findFizzBuzz(n):
    for i in range(1, n+1):
        aux=""
        if i % 3 == 0:
            aux="Fizz"
        if i % 5 == 0:
            aux+="Buzz"
        print(i if not aux else aux)

if __name__ == "__main__":
    findFizzBuzz(100)