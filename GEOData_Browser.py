import re

#path = raw_input("Enter the path of the gds file\n")
new_file = ""

def first_filter(x):
    if x.find("Parkinson") != -1:
        print x

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