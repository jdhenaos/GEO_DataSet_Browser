import re

#path = raw_input("Enter the path of the gds file\n")
new_file = ""
dic_chip = {}
res = 0
ar_res= []
res_std = []

def third_filter(w):
    init_pos = w.find("ftp://ftp.ncbi.nlm.nih.gov/geo/series/")
    final_pos = w.find("GSE",init_pos+1)
    if w[init_pos:final_pos] != "":
        return w

def second_filter(y):
    init_pos = y.find("Organism:")
    final_pos = y.find(":",init_pos+9)
    if y[init_pos:final_pos].find(";") == -1:
        return third_filter(y)

def first_filter(x):
    if x.find("Parkinson") != -1:# or x.find("Multiple Sclerosis") != -1 or x.find("multiple sclerosis") != -1:
        return second_filter(x)

try:
    infile = open("gds_result.txt","r")

    for i in infile.readlines():
        new_file += i

except:
    print "The file do not exist"

try:
    outfile = open("MultipleSclerosis_Chips.txt","w")
except:
    print "File is not created"

try:
    outfile2 = open("MultipleSclerosis_Studies.txt","w")
except:
    print "File is not created"

data = re.split("\n(\d+)\. ",new_file)

for n in data:
    if re.match("\D",n):
        if first_filter(n) != None:
            res_std.append(first_filter(n))
            t = re.search("(GPL)\d*",first_filter(n))
            if dic_chip.has_key(t.group(0)):
                dic_chip[t.group(0)] += 1
            else:
                dic_chip[t.group(0)] = 1

for w in dic_chip.items():
    if w[1] > res:
        res = w[1]
        ar_res = [w[0],w[1]]

for q in res_std:
    if q.find(ar_res[0]) != -1:
        init_pos = q.find("Accession:")
        final_pos = q.find("ID:",init_pos+1)
        if q[init_pos:final_pos] != "":
            outfile.writelines(q[init_pos+11:final_pos]+"\n")
            outfile2.writelines(q+"\n")


infile.close()
outfile.close()
outfile2.close()