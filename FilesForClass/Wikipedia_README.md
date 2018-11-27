# Wikipedia API, JSON

**October 19, 2018:** Code received from Elizabeth Wickes (GitHub: elliewix). Code was being used as part of a UIUC iSchool 452 lecture on JSON

**October 24, 2018:** Compiled a list of dogs to search based on combined dog data (AKC, PuppyBowl, Westminster, and KnowYourMemes). Began to run those dog breeds through provided code and compiled results. Results from this can be found under Results folder.

**October 30, 2018:** Began pulling data from JSON files using Python and exporting Page Titles, Page IDs, and Word Counts to .csv files.

## Data cleaning assessment
This dataset will likely require some of the most time intensive cleaning and curation. The alphabetized files from other datasets were then run and the counts for each dog breed mentioned was determined. This data was then input into a master file, combining the breeds (in ranked order) from AKC, with columns denoting PuppyBowl, Westminster, and Memes. The rows were filled with how many times each breed was mentioned in each dataset. For example, the Boxer, ranked 11th on AKC popularity, occurred 4 times in the last 5 years of the PuppyBowl, 4 times in Westminster Dog Show, and 1 time in KnowYourMeme. Dogs that possessed data in two or more categories were flagged. Those flagged breeds were then ran through code, received from Elizabeth Wickes, pertaining to the Wikipedia API. This code specifically pulls the namespace, page id, page title, page size, word count, a snippet, and timestamp of last edit and creates a combined JSON file. These 24 breed names then output 24 JSON files of various size.

A Python script was written grabbing the filepaths of each breed JSON file, and exported select information (file name, page id, page title, word count, and snippet) to a new Excel file. This file contains upwards of 15,000 total rows. As suggested by Elizabeth, a Keep column was added. As I go through each file name, I indicate by hand "t" for true or "f" for false. While some pages are obvious in respect to their inclusion, (i.e. the page "Pembroke Welsh Corgi" should be kept), others are harder to judge and may require actually looking up the page on Wikipedia to determine its status. Once completed, all of the "t"s will be filtered out and exported to a new file. This new file will be my official Wikipedia dataset. So far, I have spent upwards of 4 hours on this cleaning aspect. I expect to spend at least another 5+ hours to complete designating t/f for each entry.

## Authorship and Attribution
Wikipedia JSON extraction code was written by and belongs to Elizabeth Wickes (Github: elliewix). The Wikimedia Foundation owns the wikipedia.org domain being utilzied for this project, however it us unclear who owns individual Wikipedia pages and their respective contents.

## Semantic Contents

## Collection Process

## Data Structure

## Other
