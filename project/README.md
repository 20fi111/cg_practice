# ゲームろぐっ！
#### Video Demo:  https://youtu.be/4aDTnEZPtZE
#### Description:

**概要**
「ゲームろぐっ！」はゲームを遊ぶ際に使用します。ゲームを遊ぶときに使っていただくことで、ゲームをどれだけ遊んだのか、いつ遊んだのかを記録することが可能です。また、登録できるゲームのタイトルに制限はないため、ゲームを遊ぶとき以外にも利用することができ、TODOリストのように使っていただくこともできます。
そのため、ゲーム以外にも様々な用途で活用していただくことを望みます。

**各種ファイルについて**

**app.py:**
本プロジェクトはflaskを使用しており、app.pyでページの表示やデータベースへの登録を管理しています。

**templatesフォルダ**
flaskを利用するにあたり、htmlファイルを保存しています。

**layout.html:**
各ページにおける基本構成部分が書かれています。

**games.html**
gamelog.dbのgametitleテーブルに登録された内容を表示するページです。

**history.html**
gamelog.dbのlogテーブルに登録された内容を表示するページです。

**index.html**
ホームページであり、登録されているゲームのタイトルを表示し、その横に記録の開始ボタン、終了ボタンが表示されるページです。
開始ボタン、終了ボタンを押すと、gamelog.dbの書き換えや登録を行います。

**newgame.html**
新規ゲームの登録を行うページです。gamelog.dbのgametitleテーブルに新規項目を登録します。

**db/gamelog.db**
データベースとしてgamelog.dbが格納されています。
gamelog.dbにはgametitle、logの二つのテーブルがあります。
gametitleはid,title,playtime,lastplay,starttime_kariで構成されています。
logはid,title,starttime,finishtimeで構成されています。

**static/images/gamelog_logo.png**
「ゲームろぐっ！」のロゴ画像です。

**開発にあたり省略した機能、今後追加したい機能など**
開発にあたり、ユーザー情報の省略を行いました。理由としは、今回のプロジェクトは現状他人との共有要素などはなく、開発言語はWebではあるけれど、Web上で公開しないと決めたからです。
そのため、ユーザー情報の取得や利用を削除しました。しかし、これは今後追加する可能性があります。
またcssはbootstrapのみの利用とし、新たに追加するのを諦めました。これは開発にかけられる時間の関係上省略せざるを得なかった部分です。そのため今後更新したいと考えています。
javascriptの利用を諦めたのも同じ理由です。現状は終了ボタンを開始ボタンを押さなくても押せてしまい、それによっておこる不具合の解消ができていないため、これらの解消も行いたいと考えています。



**使い方**
簡単な「ゲームろぐっ！」の使い方を説明します。

**1.新規ゲームの登録**

「ゲームろぐっ！」を初めて使う場合には、新規ゲームの登録を行う必要があります。
以下の手順にそって、ゲームの登録を行いましょう。

・上側ナビバーの一番右に存在するNewGameをクリックし、登録画面に移動します。
・登録画面に移動したら、登録したいゲームのタイトルを中央のフォームに入力します。
・最後に登録ボタンを押します。
・これで登録は完了です。

**2.記録の開始**

ゲームの登録が完了したら、実際に記録をとってみましょう。記録の取り方は以下の手順です。

・上側ナビバーのHome、もしくはゲームろぐっ！のロゴをクリックし、Homeページに移動します。
・「1.新規ゲームの登録」を行っていれば、ゲームタイトルと開始ボタン、終了ボタンが表示されています。(表示されていなければ「1.新規ゲームの登録」を行ってください。)
・ゲームを遊び始める前に、遊ぶゲームと同じタイトルが書かれている欄の開始ボタンを押します。
・ゲームを遊び終えたら、同じ欄の終了ボタンを押します。
・これで記録は完了です。

**3.Games画面、History画面の確認**

これまでの手順でゲームの記録が完了しました。ここで記録された情報を確認したいと思っているはずです。その時にはGames画面、History画面を確認しましょう。

Games画面：ここでは登録したゲームの情報として、「ゲームのタイトル、そのゲームの総プレイ時間、そのゲームを最後に遊んだ日」を確認できます。この画面への行き方は以下の通りです。
・上側ナビバーのGamesをクリックすることで、Games画面に移動します。

History画面：ここでは記録を行った履歴を確認することができます。履歴として「タイトル、記録開始時間、記録終了時間」を確認することが可能です。この画面への行き方は以下の通りです。
・上側ナビバーのHistoryをクリックすることで、History画面に移動します。


**注意点**
上記の「使い方」の項目から、「ゲームろぐっ！」の使い方を十分理解できたと思います。
そのため「ゲームろぐっ！」をさっそく使っていただきたいのですが、その前に注意点にについても理解していただき、「ゲームろぐっ！」を快適に使ってほしいと思います。

**1.登録を行う際の注意点**
・「ゲームろぐっ！」では、データベース内に同じものがあるかどうかの判定現状を行っていません。そのため、同じタイトルを分けて登録することが可能となっています。
・もしも同じタイトルを登録してしまうと記録を行う際に予期せぬ不具合が起きる可能性が考えられます。そのため、同じタイトルを登録することを避けてください。
・また、データベース内容の削除機能がないため、もし登録してしまった場合は、外部ソフトなどで直接データベースにアクセスし、誤って登録したものを消してください。

**2.記録の際の注意点**
・「ゲームろぐっ！」では、開始ボタン、終了ボタンは記録の状況にかかわらずいつでも押せるようになっています。
・開始ボタンを一度押し、記録を始めた後、もう一度開始ボタンを押すと開始時間を更新し、記録が正しく取れないことが懸念されます。
・開始ボタンを押していない状態。つまり記録を行っていない状態で終了ボタンを押すと予期せぬ不具合を引き起こす可能性があります。そのため終了ボタンは開始ボタンを押した後に押すようにしてください。

**3.ユーザー情報などについて**
「ゲームろぐっ！」ではユーザー情報の取得を行っていません。そのため複数人での使用や、インターネット上で公開して使うことを想定していません。

**最後に**
以上が「ゲームろぐっ！」の使い方や注意点になります。