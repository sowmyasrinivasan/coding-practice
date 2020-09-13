## Say "Hello, World!" With Python
print("Hello, World!")


## Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    else:
        if (n in range(2, 6)) or (n > 20):
            print("Not Weird")
        elif n in range(6, 21):
            print("Weird")

        
## Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


## Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


## Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i**2)


## Write a function
def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 100 == 0 and year % 400 == 0:
        leap = True
    
    return leap

year = int(input())


## Print Function
if __name__ == '__main__':
    n = int(input())
    result = ""
    for i in range(1, n + 1):
        result = result + str(i)
    print(result)


## List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i, j, k] 
    for i in range(0, x+1) 
    for j in range(0, y+1) 
    for k in range(0, z+1)
    if (i + j + k != n)])


## Find the Runner-Up Score!
if __name__ == '__main__':
    n=input()
    a=map(int,input().split())
    a=list(set(a))
    a.remove(max(a))
    print (max(a))


## Nested Lists
if __name__ == '__main__':
    arr = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        scores.append(score)
    
    scores_min = min(scores)
    s = [i for i in scores if i != scores_min]
    m = min(s)
    students = []
    for i in arr:
        if i[1] == m:
            students.append(i[0])
    
    students.sort()
    for i in students:
        print(i)


## Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x = sum(student_marks[query_name])/3.0
    print(format(x, '.2f'))





























