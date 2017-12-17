from datetime import datetime
from html.parser import HTMLParser
import psycopg2
from urllib.request import urlopen


class HabrahabrParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.titles = False
        self.hublink = False
        self.nick = False
        self.article = False
        self.ul = False
        self.time = False

        self.dict = {}
        self.table = []
        self.hashtags = []

    def handle_starttag(self, tag, attrs):
        if tag == 'article':
            for name, value in attrs:
                if name == 'class' and value == 'post post_preview':
                    self.article = True

        if tag == 'ul':
            for name, value in attrs:
                if name == 'class' and value == 'post__hubs inline-list':
                    self.ul = True

        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'post__title_link':
                    self.titles = True

        if tag == 'a':
            for name, value in attrs:
                if name == 'class' and value == 'inline-list__item-link hub-link ':
                    self.hublink = True

        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'post__time':
                    self.time = True

        if tag == 'span':
            for name, value in attrs:
                if name == 'class' and value == 'user-info__nickname user-info__nickname_small':
                    self.nick = True

    def handle_data(self, data):
        if self.article is True:
            if self.titles:
                self.dict['title'] = data
            if self.ul is True:
                if self.hublink:
                    self.hashtags.append(data)
                    self.dict['hashtags'] = self.hashtags
                    # print(self.hashtags)
            if self.nick:
                self.dict['author'] = data
            if self.time:
                self.dict['time'] = self.parse_time(data)

    def handle_endtag(self, tag):
        if tag == 'article':
            self.article = False
            self.table.append(self.dict)
            self.dict = {}
        if tag == 'ul':
            self.ul = False
            self.hashtags = []
        self.titles = False
        self.hublink = False
        self.nick = False
        self.time = False

    def parse_time(self, data):
        month_values = {
            'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 10,
            'декабря': 12, }

        today_yesterday = {
            'сегодня': '17 12 2017',
            'вчера': '16 12 2017'
        }
        date_str = data
        for k, v in month_values.items():
            date_str = date_str.replace(k, str(v) + ' ' + str(datetime.now().year))

        for k, v in today_yesterday.items():
            date_str = date_str.replace(k, v)

        datetime_object = datetime.strptime(date_str, '%d %m %Y в %H:%M')
        return datetime_object

    def connnect(self):
        conn = psycopg2.connect(dbname='articles', user='postgres', password='gjufyrf')
        cursor = conn.cursor()

        for row in self.table:
            cursor.execute("""
            INSERT INTO public.tituser(title, author, time)
            VALUES (%s, %s, %s);
            """, (row['title'], row['author'], row['time']))
            for tag in row['hashtags']:
                cursor.execute("""
                     INSERT INTO public.titusertags(title, hashtag)
                     VALUES (%s, %s);
                     """, (row['title'], tag))

        conn.commit()

        cursor.close()
        conn.close()


if __name__ == '__main__':
    for i in range(90):
        response = urlopen('https://habrahabr.ru/top/monthly/page{num}/'.format(num=str(i)))
        html = response.read().decode('utf-8')

        parser = HabrahabrParser()
        parser.feed(html)
        parser.connnect()

