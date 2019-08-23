
<h1>多種多様なシステムをRSNP通信可能にする
<br>汎用ユニット<h1>


<h2> サービス利用マニュアル Ver.2.0  </h2>

芝浦工業大学　理工学研究科　機械工学専攻　知能機械システム研究室　岡野　憲，松日楽　信人

改善点などのご意見があれば，下記までご連絡ください．  
 
連絡先：  
芝浦工業大学 機械機能工学科 知能機械システム研究室  
〒135-8548 東京都江東区豊洲3-7-5  
機械工学専攻 修士2年 岡野　憲 Okano Satoshi  
E-mail:md18020@shibaura-it.ac.jp  

<h2> 目次  </h2>

<!-- TOC -->

- [1. はじめに](#1-はじめに)
- [2. ユニットを使用するための準備](#2-ユニットを使用するための準備)
- [2. X デーモン化，ssh設定，フローチャートダウンロードした場合，最初から持っている場合](#2-x-デーモン化ssh設定フローチャートダウンロードした場合最初から持っている場合)
    - [2.1 RSNPユニットの電源投入](#21-rsnpユニットの電源投入)
    - [2.2 RSNPユニットとPCとの接続](#22-rsnpユニットとpcとの接続)
    - [2.3 RSNPユニットに接続する](#23-rsnpユニットに接続する)
        - [ケース1-Linux，Mac OSの場合](#ケース1-linuxmac-osの場合)
        - [ケース2-Windowsの場合](#ケース2-windowsの場合)
        - [2.3.1 Tera Termのダウンロード＆インストール](#231-tera-termのダウンロード＆インストール)
        - [2.3.2 RSNPユニットに接続](#232-rsnpユニットに接続)
        - [2.3.3 Raspberry Piにログイン](#233-raspberry-piにログイン)
    - [ケース1，ケース2-共通](#ケース1ケース2-共通)
    - [2.4 Wi-Fi接続設定](#24-wi-fi接続設定)
    - [2.4 java(jdk)のインストール](#24-javajdkのインストール)
    - [2.5 Githubからリポジトリをクローンする](#25-githubからリポジトリをクローンする)
    - [2.6 propertiesファイルの設定](#26-propertiesファイルの設定)
- [3 RSNPユニットの動作実行](#3-rsnpユニットの動作実行)
    - [3.1 RSNP通信プログラムの実行](#31-rsnp通信プログラムの実行)
    - [3.2 RTミドルウエアでの接続を行うケース](#32-rtミドルウエアでの接続を行うケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [3.3 ROSでの接続を行うケース](#33-rosでの接続を行うケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [3.4 ミドルウエアを使用していないケース](#34-ミドルウエアを使用していないケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
        - [デバイスをSeiral通信で接続する場合](#デバイスをseiral通信で接続する場合)
    - [3.5 状態の確認](#35-状態の確認)
- [5. 通信データ仕様](#5-通信データ仕様)

<!-- /TOC -->

## 1. はじめに  

近年，労働人口の減少等から，その補完としてロボットの活用が期待されている．平成22年に発表されたNEDOの資料[1]では，ロボット市場の拡大がされている．ゆえに，今後，ロボットの台数が増加するのも必然である．そこで，増加した多数のロボットを管理，監視するためのシステムが必要になってくる．また，各ロボットからデータを取得することで，そのデータを活用した様々なサービスを期待することができる．そこで，本提案で開発した汎用ユニット(以下，「RSNPユニット」と記載)を，多種多様なロボットやデバイスに外付けで接続することで，取得したデータをRSNP(Robot Serivice Networking Protocol)[2]通信でインターネット経由でサーバにアップロードして蓄積し，Webブラウザ等のGUI上で各ロボットの状態を管理，監視することができる．以下の図のようにRSNPユニットをロボットに接続して使用することが可能である．  
<img src="https://user-images.githubusercontent.com/44587055/63586989-c2505680-c5dd-11e9-8ae9-64afd83e85de.png" width=60%>  

**※現状，RSNPユニットは，産業技術大学院大学(品川)サーバの次のエンドポイントへ接続します．**  
http://robots.aiit.ac.jp:8080/UpdateNotificationState/services  
  
## 2. ユニットを使用するための準備  

ユニットを使用するためにいくつかのソフトを予め，ダウンロード，インストール，設定する必要があります．ご了承ください．  

## 2.X デーモン化，ssh設定，フローチャートダウンロードした場合，最初から持っている場合

### 2.1 RSNPユニットの電源投入  

まず，RSNPユニットの電源を入れます．電源ボタンは搭載していないため以下の図に示すように，microUSBにusbケーブルを接続します．  
<img src="https://user-images.githubusercontent.com/44587055/63603070-c8592e00-c603-11e9-820d-ba7243321181.png" width=45%>  

### 2.2 RSNPユニットとPCとの接続  

RSNPユニットの初期設定を行うために，PCと有線で接続します．  
現状，LANケーブルで接続する方法のみがあります．  
**LANケーブルとの接続**  
LANケーブルでPCに接続するために，以下の図に示すように配線します．ケーブルの種類は，クロスかストレートのどちらでも接続可能です． PCとの接続には，LANからUSB-typeA変換ハブ，LANからUSB-typeC変換ハブを使用すれば，PCにLANポート(Ethernetポート)が無くても，接続可能です．  

<img src="https://user-images.githubusercontent.com/44587055/63603082-cf803c00-c603-11e9-9604-efef516c6334.png" width=45%>  

LANポート同士で接続した場合  

<img src="https://user-images.githubusercontent.com/44587055/63603092-d60eb380-c603-11e9-88ed-a2e9b6bb35d4.png" width=45%>  

USB-typeAに接続した場合  

<img src="https://user-images.githubusercontent.com/44587055/63603101-dc9d2b00-c603-11e9-8295-bd30382e91f9.png" width=45%>  

USB-typeCに接続した場合  

### 2.3 RSNPユニットに接続する  

#### ケース1-Linux，Mac OSの場合  

Linuxを使用している場合，次のコマンドを実行することで，RSNPユニットに接続することができます．  
`~$ ssh raspberrypi`  

#### ケース2-Windowsの場合  

RSNPユニットにリモートでSSH接続するためのソフトウェアが必要になります．  
設定すれば，コマンドプロンプトからRSNPユニットへ接続することもできますが，今回は，ソフトウェアを使用します．クライアントソフトウェアとして**Tera Term**を使用します．  

#### 2.3.1 Tera Termのダウンロード＆インストール  
  
以下のサイトより，ダウンロードとインストールを行ってください．  
**窓の杜 Tera Term**  
https://forest.watch.impress.co.jp/library/software/utf8teraterm/  

#### 2.3.2 RSNPユニットに接続  

次に，インストールしたTera Termを起動します．  

以下のような画面が表示されます．  
 <img src="https://user-images.githubusercontent.com/44587055/58787570-08240100-8625-11e9-84c8-be85ba970c81.png" width=60%>  

ここで，ホストに"raspberrypi"と，TCPポートに"22"と入力し，"OK"をクリックします．  

#### 2.3.3 Raspberry Piにログイン  

次にRaspberry Piにログインをします．  
上記で"OK"をクリック後に以下のような画面が表示されます．  
 <img src="https://user-images.githubusercontent.com/44587055/58788978-014abd80-8628-11e9-87a8-6826dc60c4a5.png" width=60%>  

ユーザ名に"pi"と，パスフレーズに"8073"と入力し，"OK"をクリックします．

### ケース1，ケース2-共通  

RSNPユニットに接続すると以下のような画面が表示されます．  

<img src="https://user-images.githubusercontent.com/44587055/63604122-ffc8da00-c605-11e9-9512-c9dffb785908.png" width=60%>  

### 2.4 Wi-Fi接続設定  
RSNPユニットに対して，ロボットやデバイスを接続する場合，有線LANで接続します．しかし，RSNP通信自体は現状，無線LANを使用することを前提としています(1. はじめに 図を参照)．そこで，ここでは無線LANの接続設定を行います．  
まず，接続するルータ等のSSIDとパスワードを調べます．  
次に，`wpa_supplicant.conf`ファイルをエディタで編集します．  
`~$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`  

※ファイルを編集するためのエディタとして今回は"nano"を使用していますが，好みのものを使用してください．以下，"nano"を使用します．

次のとおりに追記してください．  
~~~text
network={
     ssid="SSIDを記述"
     psk="パスワードを記述"
}
~~~

次に，RSNPユニットの無線LANを再起動します．以下のようにコマンドを入力し実行します．  
`~$ sudo ifdown wlan0`  
数秒すると無線LANはオフになるので，以下のようにコマンドを入力し実行します．  
`~$ sudo ifup wlan0`  
以上で，無線LANが接続可能になります．

### 2.4 java(jdk)のインストール  

java(jdk)をインストールします．以下のようにコマンドを入力し実行します．  
`~$ sudo apt-get install java-1.8.0-openjdk`  

java(jdk)がインストールされたか念のため確認します．以下のようにコマンドを入力し実行します．  
`~$ java -version`  

これでバージョンが表示されれば，インストール完了です．  

### 2.5 Githubからリポジトリをクローンする  

必要なファイルをダウンロードします．  
任意のディレクトリ以下に次のようにコマンドを入力し実行します．  
`~$ git clone https://github.com/SatoshiOkano/RSNPUnit.git`  

次に，ダウンロードされたか確認するため，以下のようにコマンドを入力します．  
`~$ ls`  

ダウンロードされていれば，`"RSNPUnit"`というディレクトリが存在します．  

### 2.6 propertiesファイルの設定  

ダウンロードしたディレクトリ内に`"DataLog"`というディレクトリがあるので，そこに移動します．  
以下のようにコマンドを入力し実行します．  
`~$ cd /RSNPUnit/DataLog`  

移動すると，`"Config.properties"`というファイルがあります．  
次に，以下のようにコマンドを入力します．  
`~$ sudo nano Config.properties`  

デフォルトでは，以下のように記述されています．  

~~~text
Configuretion
robot_id  = 1  
end_point = http://robots.aiit.ac.jp:8080/UpdateNotificationState/services
send_interval = 10000
ip_address = 169.254.183.9
port = 8000
~~~  

各パラメータの意味は，次のようになっています．  

- **robot_id** ： ロボットの識別ID  
- **end_point** ： サーバのアドレス  
- **send_interval** ： 送信時間間隔
- **ip_address** : RSNPユニット本体のIPアドレス
- **port** ： Socket通信のポート番号  

必要に応じて，これらの各パラメータを変更します．  

## 3 RSNPユニットの動作実行  

プログラムを起動してから，接続する必要があるので注意してください．  

### 3.1 RSNP通信プログラムの実行  

まず，`"RSNPcomms.jar"`を実行します．
`RSNPUnit`ディレクトリに移動するため，以下のようにコマンドを入力します．  
`~$ cd ./RSNPUnit`  
※RSNPUnitディレクトリの場所によって異なるので注意してください．

次に，実行するために以下のようにコマンドを入力します．  
`~$ java -jar RSNPcomms.jar`  

停止するときは，"Ctrl"+"c"キーを入力することで停止します．  

### 3.2 RTミドルウエアでの接続を行うケース  

ロボットまたはデバイスがRTミドルウエアを実装している場合，こちらのケースでRSNPユニットと接続することを推奨します．
以下の各バージョンで動作確認済みです．  

|               OS                | OpenRTM-aist |
| :-----------------------------: | :----------: |
| Windows 7,Windows 8, Windows 10 | 1.1.2, 1.2.0 |

次のURLから"RSNPUnitConnectorRTC"をダウンロードをしてください．  

http://githubXXXXXXXX  

RTSystemEditor上で，RTCは次の表のように表示されます．  
<img src="https://user-images.githubusercontent.com/44587055/63603822-5386f380-c605-11e9-8deb-563cd069e728.png" width=40%>  

Inportには，フォーマットに準拠したデータを入れる必要があります．フォーマットに関しては，**X章 データ通信仕様**に記しているので，参照してください．  
TimedString型のInportを設けていますが，最終的にフォーマットに準拠したデータを出力できれば，他に作成し直して構いません．

#### RSNPユニットに接続する  

ROS lauchファイルを記述する．
コンフィグレーションパラメータを次のように設定する．  


### 3.3 ROSでの接続を行うケース  

ロボットまたはデバイスがROSを実装している場合，こちらのケースでRSNPユニットと接続することを推奨します．

#### RSNPユニットに接続する  

コンフィグレーションパラメータを次のように設定します．  

### 3.4 ミドルウエアを使用していないケース  

ロボットまたはデバイスがミドルウエアを実装していない場合，こちらのケースでRSNPユニットと接続することを推奨します．  

#### RSNPユニットに接続する  

コンフィグレーションパラメータを次のように設定します．  

#### デバイスをSeiral通信で接続する場合


### 3.5 状態の確認  

ロボットまたはデバイスからRSNPユニットにデータを送信すると，RSNPでサーバに送信される．
サーバにアクセスすることでWebブラウザ上に状態が反映されているか確認することができます．  

以下のURLにアクセスすることで確認することができます．  
http://robots.aiit.ac.jp:8080/Robomech2019/  

以下のようにブラウザ上で表示されていれば，確認完了です．  
robot_id=1のロボットを稼働させた例を下の図に示す．  
<img src="https://user-images.githubusercontent.com/44587055/58847016-4caeab80-86bc-11e9-9b39-e87f95fe140a.png" width=60%>  

## 5. 通信データ仕様

RSNPユニットからロボットまたはデバイス間のデータのやり取りはSocket,Serial通信で行います．  
ただし，以下の5種類のデータで定義づける必要があります．  

- **Action_id**
- **Action名**  
- **Result_id**  
- **Resultデータ**  
- **コメント**  

各データの意味は，次のようになっています．
**Action_id**とは，**Action名**に対する紐づけidです．  
**Action名**とは，ロボットが行った動作名などです．  
**Result_id**とは，**Resultデータ**に対する紐づけidです．  
**Resultデータ**とは，ロボットから得たデータ(変数)などです．  
**コメント**とは，コメント記述を入れたい場合に用います．  
例えば，挨拶を3回，人数カウントを5人としたロボットがあったとします．この場合，データの仕様は次のようになります．  

|     データ名     | データ1  | データ2 |
| :--------------: | :------: | :-----: |
|  **Action_id**   |    1     |    2    |
|   **Action名**   | 挨拶回数 |  人数   |
|  **Result_id**   |    1     |    2    |
| **Resultデータ** |    3     |    5    |
|   **コメント**   |   無し   |  無し   |

ここで，実際のデータ形式は以下のようなjson形式としてます．`{...}`内において，先頭に`「"data":」`があり，その次に配列のカッコ(`[]`)内において，1種類のデータが配列の1つの要素に入ります．ダブルクォーテーション(`"`)で囲んだ仕様名と値をカンマ(`:`)で区切ります．3点(`...`)には，対応するデータ等が入ります．見やすいように改行してありますが，実際は1行でデータ送信してください．これ以外の仕様でのデータを送信するとRSNPユニット側で受信できないのでご注意ください．  

~~~text
{  
  "data":  
  [  
    {  
      "ac_id": ... ,  
      "ac": ... ,  
      "re_id": ... ,  
      "re": ... ,  
      "co": ...  
    },  
    {...},  
    ...  
  ]  
}  
~~~  

データ名は以下の表のように短縮形となっているのでご注意ください．  

|     データ名     |  省略形   |
| :--------------: | :-------: |
|  **Action_id**   | **ac_id** |
|   **Action名**   |  **ac**   |
|  **Result_id**   | **re_id** |
| **Resultデータ** |  **re**   |
|   **コメント**   |  **co**   |

上記のロボットの例の場合は，  
`{"data":[{"ac_id":1,"ac":"挨拶回数","re_id":1,"re":3,"co":""},{"ac_id":2,"ac":"人数","re_id":2,"re":5,"co":""}]}`  
となります．(コメントは無しのため，空欄("")となっている)  
複数種類の場合は，配列の成分が増加し，  
``{"data":[{...},{...},{...},...]}``  
となる．今回は5種類まで対応している．  
