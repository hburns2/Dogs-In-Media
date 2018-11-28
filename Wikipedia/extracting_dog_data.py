# use GLOB
# export csv
# T/F
# title/page id

import json
import csv
import os
import glob

allfiles = glob.glob('*.json')

print(allfiles)
# import os
# going to create a list i.e. listdir(source)
# for file in filepath + file
allrows = []
for path in allfiles:

    infile = open(path, "r")
    text = infile.read()
    infile.close()

    data = json.loads(text)

    for record in data:
        row = []
        row.append(path)
        pagetitle = record['title'].encode('utf-8')
        pageid = record['pageid']
        wordcount = record['wordcount']
        snippet = record['snippet'].encode('utf-8')
        row.append(pagetitle)
        row.append(pageid)
        row.append(wordcount)
        row.append(snippet)
        allrows.append(row)

headers = ['path','pagetitle', 'pageid', 'wordcount', 'snippet']

with open('allresults.csv', 'w', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(allrows)
