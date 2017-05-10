from flask import Flask, render_template, request
import db_summary_article_day
import db_article_list

app = Flask(__name__)

@app.route("/")
def day_list():
    return render_template('summary_article_day.html', days=db_summary_article_day.selectDayList())

@app.route("/article_list_day")
def article_list():
    return render_template('article_list.html', articles=db_article_list.selectArticleByDay(request.args.get("day")))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
