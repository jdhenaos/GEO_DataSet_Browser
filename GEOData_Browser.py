import re

#path = raw_input("Enter the path of the gds file\n")
new_file = ""

try:
    infile = open("gds_result.txt")

    for i in infile.readlines():
        new_file += i

except:
    print "The file do not exist"

data = re.split("\n(\d+)\. ",new_file)

for n in data:
    print n