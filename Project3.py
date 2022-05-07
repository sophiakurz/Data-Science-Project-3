
import csv


f_in = open('/Users/sreedhar/Downloads/U.S._Chronic_Disease_Indicators__CDI_.csv', 'r')
total = 0
for line in f_in.readlines():
    total += 1
print(total)



f_in = open('/Users/sreedhar/Downloads/U.S._Chronic_Disease_Indicators__CDI_.csv', 'r')
count = 0
for line in f_in.readlines():
    if 'Cardiovascular' in line:
        if 'White' in line: 
            #print(line)
            count += 1
print(count)



f_in = open('/Users/sreedhar/Downloads/U.S._Chronic_Disease_Indicators__CDI_.csv', 'r')
count2 = 0
for line in f_in.readlines():
    if 'Cardiovascular' in line:
        if 'Black' in line:
            #print(line)
            count2 += 1
print(count2)



f_in = open('/Users/sreedhar/Downloads/U.S._Chronic_Disease_Indicators__CDI_.csv', 'r')
count3 = 0
for line in f_in.readlines():
    if 'Black' in line:
        #print(line)
        count3 += 1
print(count3)



f_in = open('/Users/sreedhar/Downloads/U.S._Chronic_Disease_Indicators__CDI_.csv', 'r')
count4 = 0
for line in f_in.readlines():
    if 'White' in line:
        #print(line)
        count4 += 1
print(count4)






