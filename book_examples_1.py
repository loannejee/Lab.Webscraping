# Example Project - Working with Multiple Pages and Items
# GOAL: Get title of every book with a 2 star rating

import requests
import bs4

# 1. Figure out the URL structure to go through every page
# http://books.toscrape.com/catalogue/page-1.html
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# 2. Scrap every page in the catalogue


# 3. Figure out what tag/class represents the Star rating
# From inspect, each book is contained in an <article/> html tag with class="product_pod"
res = requests.get(base_url.format(1)) # Testing first page
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')
print(len(products)) # 20 should return because there are 20 books per page/list


# 4. Filter by that star rating using an if statement
# After investigating the html structure of each book, we find out we need to use:
# print(books[0].select('a')[1]['title']) to grab the title
two_star_titles = []
for pageNum in range(1, 51):
    scrape_url = base_url.format(pageNum)
    resObj = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(resObj.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            # 5. Store the results to a list
            two_star_titles.append(book_title)


print(two_star_titles)


