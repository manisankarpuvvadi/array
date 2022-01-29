#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
import array as arr
s=input().split(" ")
s1=list(map(int,s))
k=int(input("Enter the sum value:"))
myarr=arr.array("i",s1)
c=0
for i in range(0,len(myarr)):
    for j in range(i+1,len(myarr)):
        if myarr[i]+myarr[j]==k:
            c=c+1
print(c)
#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
import array as arr
s=input().split(",")
l1=list(map(int,s))
l=arr.array("i",l1)
i=0
j=len(l)-1
while i<len(l)//2:
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
    i=i+1
    j=j-1
#print(l)
print(*l)
#Q3. Write a program to check if two strings are a rotation of each other?
s=input("Enter a string:")
s1=input("Enter a string:")
para=s+s
if len(s)==len(s1):
    if s1 in para:
        print("True")
else:
    print("False")
#Q4. Write a program to print the first non-repeated character from a string?

import math as mt
NO_OF_CHARS = 256
def firstNonRepeating(string):
	
	arr=[-1 for i in range(NO_OF_CHARS)]
	for i in range(len(string)):
		if arr[ord(string[i])]==-1:
			arr[ord(string[i])]=i
		else:
			arr[ord(string[i])]=-2
	res=10**18
	
	for i in range(NO_OF_CHARS):
		
		if arr[i]>=0:
			res=min(res,arr[i])
	return res
string=input("Enter a string:")
index=firstNonRepeating(string)
if index==10**18:
	print("Either all characters are repeating or string is empty")
else:
	print("First non-repeating character is",string[index])
#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         

n = int(input("Enter the number of disks"))
TowerOfHanoi(n, 'A', 'C', 'B')
#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression
def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False



def postToPre(post_exp):

	s = []

	
	length = len(post_exp)

	
	for i in range(length):

		
		if (isOperator(post_exp[i])):

			
			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			
			temp = post_exp[i] + op2 + op1

			
			s.append(temp)

		
		else:

			
			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans



if __name__ == "__main__":

	post_exp = "AB+CD-"
	
	# Function call
	print("Prefix : ", postToPre(post_exp))
#Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
	stack = []
	
	
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			
			stack.append(prefix[i])
			i -= 1
		else:
		
			
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False


if __name__=="__main__":
	str = "*-A/BC-/AKL"
	print(prefixToInfix(str))
#Q8. Write a program to check if all the brackets are closed in a given code snippet.
def areBracketsBalanced(expr):
	stack = []

	
	for char in expr:
		if char in ["(", "{", "["]:

			
			stack.append(char)
		else:

			
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	
	if stack:
		return False
	return True



if __name__ == "__main__":
	expr = input("Enter expression:")

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")
#Q9. Write a program to reverse a stack.

class Stack:

	
	def __init__(self):
		self.Elements = []
		
    
	def push(self, value):
		self.Elements.append(value)
	
	
	def pop(self):
		return self.Elements.pop()
	
	
	def empty(self):
		return self.Elements == []
	
	
	def show(self):
		for value in reversed(self.Elements):
			print(value)


def BottomInsert(s, value):

	
	if s.empty():
		
		
		s.push(value)
		
	
	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)


def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)



stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()
Q10. Write a program to find the smallest number using a stack.
class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())




