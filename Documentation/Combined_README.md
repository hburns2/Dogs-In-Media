# Final dataset

The final dataset fully came together on December 4, 2018

## Authorship and Attribution
This dataset contains elements from American Kennel Club, Westminster Dog Show, KnowYourMeme, Wikipedia, and The Puppybowl. The code used to create this dataset belongs to myself, Halle Burns, as well as Elizabeth Wickes, my project mentor.

## Semantic Contents
This is my final dataset for this project. Should I have more time to continue parsing through Wikipedia entries and flagging them as relevant or not, the contents of this dataset will change. This dataset contains 9 columns as well as __ number of rows. A single row will detail the popularity ranking of a dog breed, its classification, as well as the number of times that breed has been involved in The Puppybowl, Westminster Dog Show's Best in Show, and KnowYourMeme's confirmed dog memes. Additionally, the number of Wikipedia pages devoted to or strongly representing an individual breed as well as the sum of the words in the Wikipedia pages from the aforementioned column.

## Data Structure
This data is stored in a .csv file. The file contains 9 columns reflecting:
* The popularity ranking from the AKC (numerical)
* Associated breed names from the AKC (textual)
* The AKC classification standard for each breed (categorical)
* The number of times the breed has appeared in the last five years of The Puppybowl (numerical)
* The number of times the breed has appeared in the Westminster Dog Show's Best in Show Winner's list (numerical)
* The number of times the breed has appeared in confirmed memes from the KnowYourMeme site (numerical)
* The JSON pathway associated with each breed name (textual)
* The number of Wikipedia articles associated with each breed name (textual)
* The sum of the number of words of Wikipedia articles associated with each breed name (numerical)

## Other
Description of columns:
* **Ranked Number (AKC)** - This is the numerical ranking (from 2017) associated with each dog breed. Each value will be unique as they represent the ranked standing of each individual breed.
* **Breed Name** - This column gets its values from AKC and contains the names of 24 selected dog breeds. Each value in this column will be a unique breed name.
* **Breed Class (AKC)** - As defined by the AKC (and manually compiled), this column notes the breed classification for each selected dog breed. Examples of breed classification are Sporting, Toy, Herding, Working, etc. Each classification gives supplement information about each breed. For instance, Working dogs are, as the name states, bred to work. They are known for being larger, intelligent, and alert dogs with tendencies toward protectiveness. Working dogs are typically guard dogs or frequently involved in rescue operations.
* **PuppyBowl_Number Contestants (Last 5 Years)** - This column contains numerical values noting the number of times each of the selected dog breeds was featured in the Puppy Bowl's starting lineup over the last 5 years
* **Westminster (all time)** - This column contains numerical values noting the number of times each of the selected dog breeds won Westminster Dog Show's Best in Show
* **KnowYourMeme** - This column contains numerical values noting the number of times each of the selected dog breeds is mentioned as having a meme derrived from them
* **Wiki_Path** - The unique JSON pathway associated with each selected breed name. This JSON filepath was created locally.
* **Wiki_Num_Page** - The number of Wikipedia articles associated with each selected AKC breed name
* **Wiki_Wordcounts** - The sum of the number of words of Wikipedia articles associated with each selected AKC breed name.

While there are no missing values, there are times where the value entered in PuppyBowl, Westminster, and KnowYourMeme will be zero. This zero value indicates that the breed was not present in the individual dataset.
