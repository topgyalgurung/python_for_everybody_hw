import re

file=input("Name of file: ")
temp=open(file)

lst=list()
for line in temp:
    line=line.rstrip()
    y=re.findall('[0-9]+',line)
    lst=lst+y

sum=0
for z in lst:
    sum=sum+int(z)

print(sum)
"""
import re
print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
"""