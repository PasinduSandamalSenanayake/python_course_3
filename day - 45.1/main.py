from bs4 import BeautifulSoup # Beautiful soup is a library for pulling data out of HTML files.

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser") # html.parser helps to contents
#
# # How to access website.html data using code.
# # print(soup.title) Get the title of the web page, .a , .p , .h2 when use those things that can get the related things in here.
# # print(soup.prettify())  # Full code with proper structure.
#
#
# #  Finds in website
# all_anchor_tags = soup.find_all(name="a") # a is links in the web
#
# for tag in all_anchor_tags:
#     print(tag.getText())  # getText() - get only text of the tag
#
# unique_data = soup.find_all(name="h1", id="name")
# print(unique_data)


import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find(name="a", class_="storylink")
print(article_tag)



