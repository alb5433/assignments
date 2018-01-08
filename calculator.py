#!/usr/bin/env python2
x,= raw_input("Value_1? " )
y = raw_input("Value_2? " )
x = int(x)
y = int(y)
def multiply (x,y):
	return (x * y)
def add (x,y):
	return (x + y)
def subtract (x,y):
	return (x - y)
def divide (x,y):
	return (x / y)

print "I'm going use the calculator functions to multiply Value-1 and Value_2"
z = multiply(x,y)
print "The answer is... "
print z