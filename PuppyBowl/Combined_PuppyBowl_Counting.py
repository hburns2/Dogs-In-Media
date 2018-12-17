import csv
from collections import Counter

# reading in my combined data file with breeds from all of the years I am investigating
with open("Combined_PuppyBowl_Datafiles.csv", "r") as infile:
    csv_reader = csv.reader(infile)
    words_list = list(csv_reader)       # Making my data into a list

word_counts = Counter()         # Using Counter and a for-loop to figure out how many times each breed appeared
for line in words_list:
    for word in line:
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
