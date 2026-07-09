print("--Q1:-Given a number n, print the multiplication table from 1 to 10 for n in a single line, separated by spaces.")
n=int(input("Enter a number to print its multiplication table: "))
for i in range (1, 11):
    print(n*i,end="")




print("--Q2:-You are given a String S, you need to print its characters at even indices(index starts at 0).")
s = input("Enter a string: ")

for word in s[0::2]:      
    print(word, end=" ") # 1st method

for  i in range(len(s)):
        if i%2==0:        
            print(s[i],end="") # 2nd method




print("--Q3:-Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.")
x = int(input("Enter a number: "))
while(x>=0):
    print(x, end=" ")
    x-=1



print("--Q4:- Given a positive integer x, the task is to print the numbers from 1 to x in the order as 1^2, 2^2, 3^2, 4^2, 5^2, ... (in increasing order).")
x = int(input("Enter a positive integer: "))
while(x>0):
    print(x**2, end=" ")
    x-=1

print("--Q5:--You are given a number n. The number n can be negative or positive." \
" If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. " \
"If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.")
def neg(n):
    print(n, end=" ")
    
    if n == 0:
        return
    
    neg(n + 1)


def pos(n):
    if n < 0:
        return
    
    print(n, end=" ")
    pos(n - 1)


n = int(input())

if n < 0:
    neg(n)
else:
    pos(n - 1)