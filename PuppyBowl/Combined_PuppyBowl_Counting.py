import csv
from collections import Counter

with open("Combined_PuppyBowl_Datafiles.csv", "r") as infile:
    csv_reader = csv.reader(infile)
    words_list = list(csv_reader)

word_counts = Counter()
for line in words_list:
    for word in line:
        word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
