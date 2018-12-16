# Westminster Best in Show
https://fwkc-web-prod.corebine.com/en/best-in-show-winners

**Date accessed:** September 4, 2018

**October 4, 2018:** Data was cleaned using OpenRefine. Columns deemed unnecessary for the scope of this project were deleted.

**October 17, 2018:** Cleaned data was exported into a new Excel file with 3 other datasets: PuppyBowl, AKC, and KnowYourMeme.

**October 19, 2018:** Permission was officially received from Westminster Dog Show to utilize their data in this project.

## Data cleaning assessment
Minimal cleaning was necessary for this dataset. Several rows that were indicated as missing data were edited out in Excel prior to being uploaded into OpenRefine. Once in OpenRefine, rows deemed unnecessary (name of dog, names of owners, and names of judges) were removed. This left just the breed data. Whitespace was removed. The breed column was then text faceted and evaluated to detect any spelling inconsistencies. Once cleaned, the data was then exported to a new Excel file and then sorted alphabetically in preparation for combining data. In total, the cleaning took approximately 5 to 10 minutes total to complete.

## Authorship and Attribution
All data from this dataset belongs to the Westminster Kennel Club. The data was ultized with their permission.

## Semantic Contents
This is a relatively small dataset. The original dataset included the dog's name and breed as well as the year they won best in show. Additionally, the name of their owner or trainer was detailed along with the names of those on the judging panel (should they have information from that year). During cleaning, most columns were removed, leaving only the names of the dog breeds. The file is 112 rows long.

## Collection Process
The actually collection of this data was incredibly simple. It already existed in tabular form on Westminster's website, under Best in Show and past winners. It was simply a matter of selecting all of the data and copy/pasting it into an Excel file.

## Data Structure
The data is stored in an Excel file. The cleaned file only includes one column (dog breed) and 112 rows. The column is the names of each dog breed and each row reflects a winning dog. The information in this column is textual and is being treated as categorical.

## Other
There is a single column in the cleaned version of this dataset. This column contains 112 rows. This singular column contains the breed of the dog that won the Westminster Dog Show from 1907 until 2017 (the 2018 awards had not yet taken place when the data was extracted). There are missing values in this dataset. While there are unique values (i.e. a dog breed only being represented once in this dataset), they will not be listed here since the dataset is comprised of over 100 rows.
