# pip install requests
# pip install lxml
# pip install bs4

# Example Task 0 - Grabbing the title of a page ====================================
import requests
# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter 
# Note sometimes you need to run this twice if it fails the first time

res = requests.get("http://www.example.com")
type(res)  # you get <class 'requests.models.Response'>

# Now we use BeautifulSoup to analyze the extracted page. This library already has 
# lots of built-in tools and methods to grab information/string from the html file
import bs4
soup = bs4.BeautifulSoup(res.text,"lxml") # BeautifulSoup uses lxml to go through the html document, from raw string to neat soup object

# Pass in html tag, returns a list [...]
title_tag = soup.select('title')
title_tag[0]
title_text = title_tag[0].getText()



# Example Task 1 - Grabbing all elements of a class ================================
res2 = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup2 = bs4.BeautifulSoup(res2.text,"lxml")
# Note depending on your IP Address, 
# This class may be called something different
# Look for the class name from inspect
soup2.select(".toctext")
# If you want to only print strings from the list:
for item in soup2.select(".toctext"):
    print(item.text)



# Example Task 3 - Getting an Image from a Website =================================
res3 = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup3 = bs4.BeautifulSoup(res3.text,'lxml')
image_info = soup3.select('.image')
# Check the src for the picture you want
computer = image_info[0]
# With the actual src link, you can grab the image directly like this:
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
# The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
image_link.content
# To save it on this directory:
# file name: computer_image.jpg
# mode: write binary (wb)
f = open('computer_image.jpg','wb')
f.write(image_link.content)
f.close()
