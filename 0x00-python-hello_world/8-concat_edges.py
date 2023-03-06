#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = ' '.join([str.split()[5],str.split()[6],str.split()[12], str.split()[0]])
str = str[39:66] + str[107:112] + str[0:7]
print(str)
