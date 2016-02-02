import re

#path = raw_input("Enter the path of the gds file\n")
new_file = []

try:
    infile = open("/home/juan/Descargas/gds_result.txt")

    for i in infile.readlines():
        new_file.append(i)

except:
    print "The file Do not exist"

range_init = 0
range_final = 6

while range_final <= len(new_file):
    for n in new_file[range_init:range_final]:
        print n
    range_init += 6
    range_final += 6