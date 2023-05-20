from flask import Flask, flash, redirect, render_template, request, session, redirect
from functools import wraps
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session

import datetime
import pandas as pd

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#データベースを使用できるようにする
db = SQL("sqlite:///db/gamelog.db")

@app.route("/")
def index():
    #ホームページ
    gametitle= db.execute("SELECT title,starttime_kari FROM gametitle")
    return render_template("index.html", gametitle=gametitle)

@app.route("/startlog",methods=["POST"])
def start_log():
        #開始時間の取得
        starttime = datetime.datetime.now()
        starttime = starttime.replace(microsecond = 0)
        title = request.form.get("gametitle")
        #取得した時間をデータベースに登録し再度ホームの表示
        db.execute("UPDATE gametitle SET starttime_kari = ? WHERE title = ?", starttime, title)

        return redirect("/")

@app.route("/finishlog",methods=["POST"])
def finish_log():
        #ログの終了、終了時間の取得、htmlから送ってきたタイトル、開始時間の取得。
        #データベースからプレイ時間を取っておく。
        str_starttime = request.form.get("starttime")
        starttime = datetime.datetime.strptime(str_starttime,'%Y-%m-%d %H:%M:%S')
        finishtime = datetime.datetime.now()
        finishtime = finishtime.replace(microsecond = 0)
        gametitle = request.form.get("gametitle")
        db_playtime = db.execute("SELECT playtime FROM gametitle WHERE title = ?", gametitle)

        #終了時間と開始時間から今回のログにかかった時間を取得。
        #経過時間を今までのプレイ時間に足して、総プレイ時間を計算。
        playtime = db_playtime[0]["playtime"]
        playtime = pd.to_timedelta(playtime)
        plus_playtime = finishtime - starttime
        re_playtime = playtime + plus_playtime

        re_playtime = str(re_playtime)
        lastplay = finishtime.date()

        #データベースに結果を入れる
        db.execute("UPDATE gametitle SET playtime = ?, lastplay = ?, starttime_kari = '' WHERE title = ?", re_playtime, lastplay, gametitle)

        db.execute("INSERT INTO log (title, starttime, finishtime) VALUES (?, ?, ?)", gametitle, starttime, finishtime)

        return redirect("/")

@app.route("/history")
def history():
    #履歴ページ
    history = db.execute("SELECT * FROM log ORDER BY finishtime")
    return render_template("history.html", history=history)

@app.route("/games")
def games():
    #登録されたゲームに関する情報
    games = db.execute("SELECT * FROM gametitle")
    return render_template("games.html", games=games)

@app.route("/newgame",methods=["GET","POST"])
def newgame():
    #ⓦたらしいゲームの登録ページ
    if request.method == "GET":
        return render_template("newgame.html")
    else:
        new_title = request.form.get("title")
        db.execute("INSERT INTO gametitle (title, playtime) VALUES (?, '00:00:00')", new_title)
        return redirect("/")


