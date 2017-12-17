import psycopg2
import argparse


def get_data(query, *args):
    conn = psycopg2.connect(dbname='articles', user='postgres', password='gjufyrf')
    cursor = conn.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("action", type=int,
                        help=u"1 - Получим список статей по заданному хэш-тэгу в заданный период времени"
                             u"2 - Получаем список популярных статей за неделю"
                             u"3 - Получаем топ 10 популярных хэш-тэгов, т.е. те, у которых больше всего статей"
                             u"4 - Получаем список самых активных пользователей, те, у которых больше всего статей")
    parser.add_argument("--hashtag", action="store", help=u'Искомый хештег')
    parser.add_argument("--period_start", action='store', help=u'Начало периода')
    parser.add_argument("--period_end", action='store', help=u'Конец периода')
    args = parser.parse_args()
    if args.action == 1:
        if args.hashtag:
            if args.period_start:
                if args.period_end:
                    query = """
                    SELECT articles.id
                        , articles.title
                        , articles.author
                        , articles.time
                        , tags.hashtag
                    FROM public.tituser as articles 
                        LEFT JOIN public.titusertags as tags ON (articles.title = tags.title)
                    WHERE tags.hashtag = (%s)
                    AND articles.time between (%s) and (%s)
                    ORDER BY articles.time;
                    """
                    rows = get_data(query, args.hashtag, args.period_start, args.period_end)
                    print("\nRows: \n")
                    for row in rows:
                        print("   ", row)
    if args.action == 2:
        if args.period_start:
            if args.period_end:
                query = """
                SELECT title, "time"
                    FROM public.tituser
                WHERE "time" between (%s) and (%s)
                ORDER BY "time";
                """
                rows = get_data(query, args.period_start, args.period_end)
                print("\nRows: \n")
                for row in rows:
                    print("   ", row)

    if args.action == 3:
        query = """
        SELECT hashtag, count (hashtag) as N 
            FROM public.titusertags
        GROUP BY hashtag
        ORDER BY N desc
        LIMIT 10;
        """
        rows = get_data(query)
        print("\nRows: \n")
        for row in rows:
            print("   ", row)

    if args.action == 4:
        query = """
        SELECT author, count (author) as N 
            FROM public.tituser
        GROUP BY author
        ORDER BY N desc;
        """
        rows = get_data(query)
        print("\nRows: \n")
        for row in rows:
            print("   ", row)

