# Wikipedia API, JSON

**October 19, 2018:** Code received from Elizabeth Wickes (GitHub: elliewix). Code was being used as part of a UIUC iSchool 452 lecture on JSON

**October 24, 2018:** Compiled a list of dogs to search based on combined dog data (AKC, PuppyBowl, Westminster, and KnowYourMemes). Began to run those dog breeds through provided code and compiled results. Results from this can be found under Results folder.

**October 30, 2018:** Began pulling data from JSON files using Python and exporting Page Titles, Page IDs, and Word Counts to .csv files. This marks the beginning of tagging each page as t/f (further explained in the next section)

**December 5, 2018:** Due to nearing deadline, ended the tagging process having only marked approximately 7000 values out of 15000 as t/f

## Data cleaning assessment
This dataset will likely require some of the most time intensive cleaning and curation. The alphabetized files from other datasets were then run and the counts for each dog breed mentioned was determined. This data was then input into a master file, combining the breeds (in ranked order) from AKC, with columns denoting PuppyBowl, Westminster, and Memes. The rows were filled with how many times each breed was mentioned in each dataset. For example, the Boxer, ranked 11th on AKC popularity, occurred 4 times in the last 5 years of the PuppyBowl, 4 times in Westminster Dog Show, and 1 time in KnowYourMeme. Dogs that possessed data in two or more categories were flagged. Those flagged breeds were then ran through code, received from Elizabeth Wickes, pertaining to the Wikipedia API. This code specifically pulls the namespace, page id, page title, page size, word count, a snippet, and timestamp of last edit and creates a combined JSON file. These 24 breed names then output 24 JSON files of various size.

A Python script was written grabbing the filepaths of each breed JSON file, and exported select information (file name, page id, page title, word count, and snippet) to a new Excel file. This file contains upwards of 15,000 total rows. As suggested by Elizabeth, a Keep column was added. As I go through each file name, I indicate by hand "t" for true or "f" for false. While some pages are obvious in respect to their inclusion, (i.e. the page "Pembroke Welsh Corgi" should be kept), others are harder to judge and may require actually looking up the page on Wikipedia to determine its status. Once completed, all of the "t"s will be filtered out and exported to a new file. This new file will be my official Wikipedia dataset. So far, I have spent upwards of 4 hours on this cleaning aspect. I expect to spend at least another 5+ hours to complete designating t/f for each entry.

## Authorship and Attribution
Wikipedia JSON extraction code was written by and belongs to Elizabeth Wickes (Github: elliewix). The Wikimedia Foundation owns the wikipedia.org domain being utilzied for this project, however it us unclear who owns individual Wikipedia pages and their respective contents.

## Semantic Contents
The datafile for this source contains 6 columns and 15,416 rows. This file combines the output from the 24 JSON files (1 for each selected breed). This dataset is being used as the primary media comparison.

## Collection Process
Based on the AKC rankings, there are over 190+ different breeds being compared. However, for the scale of this project, this was too many to consider. Looking at the combined data from the Puppy Bowl, Westminster, and KnowYourMeme, I narrowed this list to 24 dog breeds that would be run through Elizabeth's code. The code takes whatever text I enter and pulls any Wikipedia page containing that text, outputting a page ID, title, snippet, and wordcount to a separate JSON file. In many cases, I decided to run the breed name plus the word "dog" in an attempt to narrow down searches as much as possible. For example, "Boxer" pulled thousands of pages of results. "Boxer AND dog", however, pulled far less.

Once the 24 JSON files were created, I wrote a Python script to pull every file in the directory with a .json file type, read in their contents, and had the contents exported to a new combined file (my official dataset for this project). There, line by line, I hand-coding "t" or "f" depending on whether the page featured the specified dog breed or not.

## Data Structure
Most of the data in my Wikipedia data file would not be used for my final dataset. In fact, only the path and wordcount ultimately mattered. That being said, this file (.csv) contained 6 columns. The first, path, was categorical in nature and represented which JSON file the data in each row came from. Then, there was pagetitle, an open-text column that listed the title of the Wikipedia page being pulled. After that, pageid, a numeric column that documented the unique IDs of each Wikipedia page being pulled. Following pageid was wordcount, which documented the number of words each page contained. Then, my added column, labeled "Keep," which was a boolean, to be filled with t or f values. And finally, the last column was snippets, which contained a snippet from the selected Wikipedia page, highlighting the lines surrounding where my search terms appeared. 

## Other
This was the hardest data file to put together. There are many missing datapoints, however only from the "Keep" column. I ran out of time, as hand-coding each of these articles was far more difficult than I expected. Often, it required me to actually go into the specified Wikipedia page and read the article to discover whether it was relevant to my project or not. Therefore, I only made it approximately 7000 entries in. The entries marked are in no particular order, however, they were initially approached based on which I could easily categorize just by looking at the title or the snippet. Out of the 7000 or so marked entries, only a little over 100 ended up being kept due to relevance.
