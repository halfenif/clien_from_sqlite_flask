import const_config
import dbms

constDBMS = const_config.get_dbms()
constSQLSelect = "SELECT a.day, a.cnt FROM tb_summary_day a ORDER BY a.day DESC"

def selectDayList():
    print("Start selectDayList")
    conn = dbms.connect.sqlite(constDBMS)
    cur = conn.cursor()
    cur.execute(constSQLSelect)
    return cur.fetchall()

if __name__ == '__main__':
    for item in selectDayList():
        print(item["day"] + " : " + format(item["cnt"], ','))
