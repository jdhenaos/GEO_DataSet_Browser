import re

#path = raw_input("Enter the path of the gds file\n")
new_file = ""

def second_filter(y):
    init_pos = y.find("Organism:")
    final_pos = y.find(":",init_pos+9)
    print y[init_pos:final_pos]

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