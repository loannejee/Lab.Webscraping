# Web Scraping Exercises
# Complete the Tasks Below

# TASK: Import any libraries you think you'll need to scrape a website.
import requests
import bs4


# TASK: Use requests library and BeautifulSoup to connect to 
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.
res = requests.get("http://quotes.toscrape.com/")
res.text


# TASK: Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(res.text,"lxml")
author_names = set()
author_list = soup.select('.author')

for author in author_list:
    if (author not in author_names):
        author_names.add(author.text)


# TASK: Create a list of all the quotes on the first page.
quotes = []
quote_list = soup.select('.text')
for quote in quote_list:
    quotes.append(quote.text)


# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from
# the requests text shown on the top right from the home page (e.g Love
# Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath
# each quote, try to find a class only present in the top right tags, perhaps check
# the span.
tags = []
tag_list = soup.select('.tag-item')
for tag in tag_list:
    tags.append(tag.text)




# ==================================================================================

# Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website. Unknown Number of Pages.

base_url = 'https://quotes.toscrape.com/page/'

# Choose some huge page number we know doesn't exist
page_url = base_url+str(9999999)

# Obtain Request
res = requests.get(page_url)

# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')

# This solution requires that the string "No quotes found!" only occurs on the last page.
# If for some reason this string was on the other pages, we would need to be more detailed.
"No quotes found!" in res.text

page_still_valid = True
author_names_final = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = base_url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page ***
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for author in soup.select(".author"):
        # unique authors only
        if (author.text not in author_names_final):
            author_names_final.add(author.text)
        
    # Go to Next Page
    page += 1

print(author_names_final)




