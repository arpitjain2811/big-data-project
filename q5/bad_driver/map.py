lookuptable={}
# i=0
import sys
import StringIO
import csv
import datetime

with open('lookuptable') as f:
    for line in f:
        values=line.strip().strip('\n').split('\t')
        lookuptable[values[0]]=float(values[1])
        # i+=1
# print i,len(lookuptable)
for line in sys.stdin:

    csv_file = StringIO.StringIO(line.strip())
    csv_reader = csv.reader(csv_file)

    for l in csv_reader:
        if l[0] == "medallion" or l[14]=='UNKNOWN' or l[15]=='UNKNOWN':
            continue
        else:
            try:
                driver=l[1]
                pickup = l[14]
                dropoff = l[15]
                key = pickup + '|' + dropoff
                evil_score=(float(l[9])-lookuptable[key])/lookuptable[key]
                if evil_score>0:
                    print driver+','+evil_score
            except:
                continue; 