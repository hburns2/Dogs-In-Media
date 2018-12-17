# KnowYourMeme
https://knowyourmeme.com/

**Date accessed:** October 17, 2018

**October 17, 2018:** Dataset was created by looking up "dog" in the KnowYourMeme search area. Memes marked as confirmed by the site were then written in an Excel file. In other columns, the year of each meme's emergence as well as any dog breed associated each meme were noted. Once complete, this file was uploaded into OpenRefine. Whitespaces were cleaned and spelling was checked. Cleaned data was exported into a new Excel file with 3 other datasets: PuppyBowl, Westminster, and AKC.

## Data cleaning assessment
This data required quite a bit of curation but very minimal cleaning. Even though this data was compiled straight from the website into Excel by hand, the dataset was still uploaded into OpenRefine to clean any whitespaces, double check spelling, and ensure the uniformity in the date formats. In total, the cleaning aspect of this process took maximum 5 minutes, as there were very few data points being utilized in this set.

## Authorship and Attribution
Know Your Meme is published by Literally Media, Ltd. However, similar to Wikipedia, the information on the site is crowd-sourced. Anyone can submit a meme or updates to the site.

## Semantic Contents
This dataset contains the name, associated breed (if one exists), and origin year of popular dog-related memes. This data is being used to cover a gap in media. While my other sources are largely competition-based, memes have picked up popularity over the past 10 or so year, becomming quite the staple in social media. Hopefully, by looking at meme data, I will be able to capture another facet of media culture.

## Collection Process
This data was compiled and curated by hand. Therefore, my overall process in this case was very different. I began with just taking a look at the information KnowYourMeme provided for entries. This typically included some background on the meme itself, examples of the meme, a timeline developed by GoogleTrends, related memes, and external references.

My first thought was that I would search each AKC breed in the KnowYourMeme search box and see what appeared. This proved to be a fairly fruitless endeavor, as either memes were not encoded with specific breed names mentioned or what was returned was not "confirmed." There are 2 types of memes on KnowYourMeme, a submission and a confirmed. Submissions are frequently one-offs, sent in by someone in the community, and typically rather obscure. For this, I decided to focus on confirmed memes.

So, instead I did a simple search for "dog," which pulled up a number of confirmed results. In an Excel file, I marked the name of the confirmed meme. Then, I went inside each page and looked to see whether any dog breeds were specifically associated with that meme. For example, the Doge meme is associated with Shiba Inus. Then, I noted the year each meme originated. Should I have more time and wish to revist this down the road, I think it would be interesting to look at the year mentioned in these memes and compare them to the timestamps of the Wikipedia pages pulled.

## Data Structure
This data is kept in an Excel spreadsheet. It consists of 3 columns and 18 rows. The first column is an open text field, meant to capture the name of the meme being examined. The next column, Associated Breed, is categorical in nature and, if a specific breed is a prominant feature in a meme, it is notated. Otherwise, "N/A" is used to mark absence. Finally, the last category is an associated date. While it is supposed to be numerical in nature, my raw dataset contained notes indicating origin as well as the date marking spread of popularity. Since the date would not be featured in my final dataset, this column was not cleaned and remains containing 2 different data types.

## Other
There are 3 columns represented in this data: Meme Name, Associated Breed, and Associated Date. The Meme Name column notes the names of each confirmed meme that centered a dog in its content. The second field, Associated Breed, looks to identify the breed of the dog being featured. The final column, Associated Date, notes the earliest known date when the meme first surfaced.

Technically, there are missing values within this dataset. When a breed could not be identified, the column was marked as N/A. This is not to say that there is not one singular dog associated with the meme, only that the breed was not specified. There are 5 instances of a missing value in the "Associated Breed" column. 

There are a multitude of unique values. However, the ones I am most concerned about for this project involves the dog breeds. Looking strictly at the breed section, while Golden Retriever and Shiba Inu repeat, the others are unique in nature. Several of the breeds listed here are less popular ones. Which, when combined with Westminster and Puppy Bowl data, allowed me to see a much larger selection of dogs than before.
