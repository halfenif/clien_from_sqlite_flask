import const_config
import dbms

constDBMS = const_config.get_dbms()
constSQLSelectByDay = "SELECT SUBSTR(a.pubdate,11,9) pubdate, a.seq, a.title, a.postuser FROM tb_article a WHERE a.pubdate LIKE ? || '%' ORDER BY a.seq DESC"

def selectArticleByDay(day):
    print("Start selectArticle")
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelectByDay, (day, ))
    return cur.fetchall()

if __name__ == '__main__':
    for item in selectArticle():
        print(item)
