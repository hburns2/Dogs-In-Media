# Puppy Bowl Lineup(s): Season IX - Season XIV
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/puppy-bowl-xiv-starting-lineup/;
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/puppy-bowl-xiii-starting-lineup/;
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/puppy-bowl-xii-starting-lineup/;
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/xi-starting-lineup/;
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/x-starting-lineup/;
http://www.animalplanet.com/tv-shows/puppy-bowl/photos/ix-starting-lineup-pictures/

**Date accessed:** September 18, 2018 --> downloaded HTML files

**October 2, 2018:** Used XPath to extract the season lineups from X-XIV (2014-2018). Extracted data includes name of dog, team, breed, age, and location. This raw data can be found in X_lineup.txt - XIV_lineup.txt. A screenshot of the XPath query built to extract said data can be found in the "XPath_sample_image.png" file.

**October 4, 2018:** Copied .txt files into Excel. Separated the data into columns by deliminator. Uploaded into OpenRefine and used OpenRefine and Python to clean datasets. Columns outside Name and Breed were removed based on the scope of this project. These clean datasets were then added to the Clean_Datasets folder and labeled as "Copy of..."

**October 17, 2018:** Cleaned data was exported into a new Excel file with 3 other datasets: AKC, Westminster, and KnowYourMeme.

## Data cleaning assessment
This data source required quite a bit of cleaning, all of which was done in either Execl or OpenRefine, with each year possessing its own specific data cleaning needs. Years 10 and 11 were separated by colons as deliminators. Years 12 - 15 were separated by slashes (however, also contained colons indication name, breed, sex, and location). The first pass of restructuring the data, not to be separated by punctuation but placed into individual columns, occured in Excel. This largely separated out what I needed, but extensive cleaning still needed to occur. Each dataset was uploaded individually into OpenRefine.

All files ended up with unnecessary columns that were removed, such as name, sex, fun fact, and age. For X, due to the delimination, the text within "Breed" all ended with the word "Sex" appended at the end. Using a simple Python script, I removed the word from the Breed column. Additionally, a few of the longer breed names had their information cut off when text was initially extracted from the website, so I manually added the final letters to complete the breed names when needed. XI ended up with "Breed: " before the names of each breed which, likewise, was removed using Python within OpenRefine. XII had the most cleaning involved, as the raw data included missing values. Within the raw data, the second column represented team name. However, not every dog had a team name entered. Therefore, some values from the third column, Breed, ended up populating the second column. Since this dataset was relatively small, the migration from one column to the next was done by hand. XIII and XIV were the easiest to clean, as the raw data separated cleanly once parsed by deliminator. However, these later years denoted mixed breed by using "-" instead of the earlier "/". I ran a simple Python script within OpenRefine to replace all instances of "-" with "/" to create uniformity across all datasets.

Each dataset was then text faceted individually to check spelling. Once cleaned, all five fives were exported into new Excel files. The data from these were all taken and then combined into a master file. This was then once again uploaded into OpenRefine. The master file had all of the whitespaces removed and then I once again text faceted to ensure spelling was correct and uniform. Once exported back into Excel, the column was sorted alphabetically in preparation for being added to the combined file. 

Entirely, this cleaning process took approximately 4 hours.

## Authorship and Attribution
All data from The Puppy Bowl belongs to Animal Planet and thus Discovery Inc. After reading through Discovery's copyright policies, I believed that the data I wished to use would fall under fair use. I contacted Discovery asking for permission to use their data, covering all of my bases, however never heard a response.

## Semantic Contents
The individual datasets largely contain the same few fields, give or take a few depending on the year. Always mentioned is the dog's name, their breed, and their sex. While some years, team name was added. Since I was only interested in breed, my final dataset only includes a single column (breed name) and consists of 221 rows.

## Collection Process
The individual datafiles were collected using XPath for webscraping. Following the links provided at the top of the page will bring you to each year's "Starting Lineup." On the far right side of the page, near the middle, is a "View all photos" link. Clicking that link will cause a gallery to pop up over your initial page, containing the photographs of every dog in that year's starting line-up. Using the same XPath code per year (a screenshot of the code can be found within Dogs-in-Media/PuppyBowl/XPath_sample_image.png), I was able to extract, at bare minimum, each competing dog's name and breed. This information was then input into a .txt file (this raw data can be found at Dogs-in-Media/PuppyBowl/Raw_Datasets) and was then input into Excel to begin the cleaning process (described above).

## Data Structure
The final PuppyBowl dataset, as mentioned before, only contained a single column. This column contained textual data (breed names) spanning 221 rows. This data is stored in an Excel file.

## Other
As the final dataset is a combined file, there are no missing values within this column. 

It is important to note that while some dogs possessed multiple breeds (i.e. Husky/Labrador), if the breed was documented as, for example, "Husky mix," the dog was categorized as being just a Husky. Additionally, since further detail was not documented, "Corgi" was encoded to be "Pembroke Welsh Corgi" in the final dataset.
