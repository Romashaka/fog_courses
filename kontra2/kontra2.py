from urllib.request import urlopen
#  from bs4 import BeautifulSoup as Soup
#  from datetime import datetime
#  import psycopg2
from html.parser import HTMLParser

# Будем юзать html.parser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = False
        self.hublink = False
        self.nick = False
        self.table = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'post__title_link':
                    self.title = True

        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'inline-list__item-link hub-link ':
                    self.hublink = True

        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'user-info__nickname user-info__nickname_small':
                    self.nick = True

    def handle_data(self, data):
        if self.title:
            self.table.append({'title': data})
        if self.hublink:
            self.table.append({'hashtag': data})
        if self.nick:
            self.table.append({'nickname': data})

    def handle_endtag(self, tag):
        self.title = False
        self.hublink = False
        self.nick = False

    def table_get(self):
        for num, item in enumerate(self.table, 1):
            print(f'{num}. {item}')


response = urlopen('https://habrahabr.ru/top/')
html = response.read().decode('utf-8')

parser = MyHTMLParser()
parser.feed(html)
parser.table_get()


#  Прости мыльце, тебя запретили :'-(
# my_url = 'https://habrahabr.ru/top/'
#
# client = ureq(my_url)
# page_html = client.read()
# client.close()
#
# page_soup = Soup(page_html, 'html.parser')
# ar_list = page_soup.find_all('article', {'class': 'post post_preview'})
#
#
# table = []
# for h2 in ar_list:
#     link = h2.find('h2', {'class': 'post__title'}).find('a').get('href')
#     text = h2.find('h2', {'class': 'post__title'}).find('a').text
#     user = h2.find('span', {'class': 'user-info__nickname user-info__nickname_small'}).text
#     link_us = h2.find('header', {'class': 'post__meta'}).find('a').get('href')
#     time1 = str(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'))
#     table.append({'title': text, 'url': link, 'usr': user, 'usr_link': link_us, 'time1': time1})
#  for num, item in enumerate(table, 1):
#      print(f'{num}. {item}')
#
#
# conn = psycopg2.connect(dbname='habr', user='postgres', password='gjufyrf')
# cursor = conn.cursor()
#
# # cursor.executemany("""INSERT INTO public.info(title,url,usr,usr_link,time1) VALUES (%(title)s, %(url)s,
# # %(usr)s, %(usr_link)s, %(time1)s)""", table)
# #
# # conn.commit()
#
# cursor.execute("SELECT * FROM public.info")
# rows = cursor.fetchall()
# print("\nRows: \n")
# for row in rows:
#     print("   ", row)
#
# cursor.close()
# conn.close()


