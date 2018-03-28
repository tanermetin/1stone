#!/bin/python

import sys
import random
import numpy




#day 18 Queues & Stack // Palindrome

s = 'ahoioha' ;

l = len(s)

class Solution:

	def __init__(self):
		self.stack=[]
		self.queue=[]
		self.length=0

	def pushCharacter(self, letter):
		self.stack.append(letter)

	def enqueueCharacter(self, ch):
		self.queue.insert(0, ch)

	def popCharacter(self):
		return self.stack.pop()

	def dequeueCharacter(self):
		return self.queue.pop()


#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 

print  obj.stack 
obj.popCharacter()
print obj.stack
print "----"
print  obj.queue
obj.dequeueCharacter()
print  obj.queue


for i in range(l / 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    sys.stdout.write ("The word, "+s+", is a palindrome.")
else:
    sys.stdout.write ("The word, "+s+", is not a palindrome.")    
    
        








