import re

try:
    infile = open("/home/juan/Descargas/gds_result.txt")

    for i in infile.readlines():
        print i
except:
    print "l cagate"