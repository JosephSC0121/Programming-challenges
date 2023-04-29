# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome():
    sumNum = 0 
    for x in range(0,1000001):
            str_num = str(x)
            if str_num == str_num[::-1]:
                numero_binario = bin(x)[2:]
                binario_str = str(numero_binario) 
                if numero_binario == binario_str[::-1]:                      
                        sumNum += x
    return sumNum
if __name__ == "__main__":
    print(palindrome())

 



