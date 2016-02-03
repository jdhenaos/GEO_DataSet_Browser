import re

#path = raw_input("Enter the path of the gds file\n")
new_file = ""
dic_chip = {}

def chip_counter(z):
    counter = 1
    t = re.search("(GPL)\d*",z)
    if dic_chip.has_key(t.group(0)):
        counter += 1
        dic_chip[t.group(0)] = counter
    else:
        dic_chip[t.group(0)] = counter

def second_filter(y):
    init_pos = y.find("Organism:")
    final_pos = y.find(":",init_pos+9)
    if y[init_pos:final_pos].find(";") == -1:
        chip_counter(y)

def first_filter(x):
    if x.find("Parkinson") != -1:
        second_filter(x)

try:
    infile = open("gds_result.txt")

    for i in infile.readlines():
        new_file += i

except:
    print "The file do not exist"

data = re.split("\n(\d+)\. ",new_file)

for n in data:
    if re.match("\D",n):
        first_filter(n)

for w in dic_chip.items():
    print  w