import csv
f = open('year_cat_rate.csv','r')
reader = f.read().splitlines()
for r in reader:
    if(r.split(',')[1]==' Western '):
        print('%s,'%(r.split(',')[2]))
