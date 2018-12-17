import json
import csv
import os
import glob

# Using glob.glob to find any filepath in the directory that ends in .json
allfiles = glob.glob('*.json')

# Printing a list of all files ending in .json in that directory
print(allfiles)

allrows = []
for path in allfiles:

    infile = open(path, "r")    # Creating a for-loop that will loop over all files in the directory and read in their text
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

# Creating an outfile containing the combined text from all .json files in the directory
headers = ['path','pagetitle', 'pageid', 'wordcount', 'snippet']

with open('allresults.csv', 'w', newline='') as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(allrows)
