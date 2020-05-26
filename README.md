
<h1> 多種多様なシステムをRSNP通信可能にする<br>汎用ユニットの開発</h1>  

<h2> サービス利用マニュアル Ver.2.8</h2>

<h4> 芝浦工業大学 知能機械システム研究室　岡野　憲，松日楽　信人</h4>

本システムをご利用予定の方は，お手数ですが下記の連絡先までご連絡ください．また，改善点などのご意見がある方も，下記の連絡先までご連絡ください．**RSNP(Robot Service Network Protocol)をご利用いただくには，使用条件にご同意していただき，RSi事務局にお問い合わせしていただく必要がありますので，ご注意ください．** RSiとRSNPに関しては以下のURLでご参照ください．RSNPユニットのハードウェア，ソフトウェアの仕様に関しては，以下のURLをご参照ください．各種修正履歴に関しては以下のURLをご参照ください．  

RSiとRSNPに関してURL：http://robotservices.org/  
RSNPユニットの仕様：https://github.com/SatoshiOkano/RSNPUnit/blob/master/Specification.md  
各種修正履歴：https://github.com/SatoshiOkano/RSNPUnit/releases

~~~text  
連絡先：  
芝浦工業大学 機械機能工学科 知能機械システム研究室  
〒135-8548 東京都江東区豊洲3-7-5  
機械工学専攻 修士2年 岡野　憲 Okano Satoshi  
TEL:03-5859-8073
E-mail:md18020@shibaura-it.ac.jp  
~~~  

<div style="page-break-before:always"></div>

<h2>目次</h2>

<!-- TOC -->

- [はじめに](#はじめに)
- [ユニットを使用するための準備](#ユニットを使用するための準備)
    - [RSNPユニットの電源投入](#rsnpユニットの電源投入)
    - [RSNPユニットを直接操作する場合](#rsnpユニットを直接操作する場合)
    - [RSNPユニットとPCとの接続](#rsnpユニットとpcとの接続)
    - [RSNPユニットに接続する](#rsnpユニットに接続する)
        - [ケース1-Linux，Mac OSの場合](#ケース1-linuxmac-osの場合)
        - [ケース2-Windowsの場合](#ケース2-windowsの場合)
        - [Tera Termのダウンロード＆インストール](#tera-termのダウンロード＆インストール)
        - [RSNPユニットに接続](#rsnpユニットに接続)
        - [Raspberry Piにログイン](#raspberry-piにログイン)
        - [ケース1，ケース2-共通](#ケース1ケース2-共通)
    - [無線LAN接続設定](#無線lan接続設定)
    - [java(jdk)のインストール](#javajdkのインストール)
    - [GitHubからファイルをダウンロード](#githubからファイルをダウンロード)
    - [propertiesファイルの設定](#propertiesファイルの設定)
- [RSNPユニットの動作実行](#rsnpユニットの動作実行)
    - [RSNP通信プログラムの実行](#rsnp通信プログラムの実行)
    - [プログラム実行のデーモン化](#プログラム実行のデーモン化)
    - [RTミドルウエアでの接続を行うケース](#rtミドルウエアでの接続を行うケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [ROSでの接続を行うケース](#rosでの接続を行うケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [ミドルウエアを使用していない，Socket通信で接続するケース](#ミドルウエアを使用していないsocket通信で接続するケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [ミドルウエアを使用していない，Serial通信で接続するケース](#ミドルウエアを使用していないserial通信で接続するケース)
        - [RSNPユニットに接続する](#rsnpユニットに接続する)
    - [状態の確認](#状態の確認)
- [RSNPユニットへの通信データ仕様](#rsnpユニットへの通信データ仕様)
- [ライセンス](#ライセンス)
- [参考文献](#参考文献)

<!-- /TOC -->

<div style="page-break-before:always"></div>  

## 1. はじめに  

近年，労働人口の減少等から，その補完としてロボットの活用が期待されている．平成22年に発表されたNEDOの資料[1]では，ロボット市場の拡大がされている．ゆえに，今後，ロボットの台数が増加するのも必然である．そこで，増加した多数のロボットを管理，監視するためのシステムが必要になってくる．また，各ロボットからデータを取得することで，そのデータを活用した様々なサービスを期待することができる．そこで，本提案で開発した汎用ユニット(以下，「RSNPユニット」と記載)を，多種多様なロボットやデバイスに外付けで接続することで，取得したデータをRSNP(Robot Serivice Networking Protocol)[2]通信でインターネット経由でサーバにアップロードして蓄積し，Webブラウザ等のGUI上で各ロボットの状態を管理，監視することができる．以下の図のようにRSNPユニットをロボットやデバイスに接続して使用することが可能である．  
<img src="https://user-images.githubusercontent.com/44587055/63586989-c2505680-c5dd-11e9-8ae9-64afd83e85de.png" width=60%>  

**※現状，RSNPユニットは，産業技術大学院大学(品川)サーバの次のエンドポイントへ接続します．**  
http://robots.aiit.ac.jp:8080/EnqueteRobots2017/services  
  
## 2. ユニットを使用するための準備  

ユニットを使用するためにいくつかのソフトを予め，ダウンロード，インストール，設定する必要があります．ご了承ください．  

### 2.1 RSNPユニットの電源投入  

まず，RSNPユニットの電源を入れます．電源ボタンは搭載していないため以下の図に示すように，microUSBにusbケーブルを接続します．OSをシャットダウンしたら，ケーブルを抜いてください．  

<img src="https://user-images.githubusercontent.com/44587055/63603070-c8592e00-c603-11e9-820d-ba7243321181.png" width=35%>  

<div style="page-break-before:always"></div>  

### 2.2 RSNPユニットを直接操作する場合  

HDMI接続可能なモニタ，USBtype-Aのキーボード，マウスを用意可能である場合は，下の図のように接続することで，PCのように扱うことが可能です．ただし，環境が初めから整っている場合を以外は，次の2.3節に従って接続することも可能です．  

<img src="https://user-images.githubusercontent.com/44587055/63636425-0f99fa00-c6aa-11e9-9a9b-3b106aa13967.png" width=60%>  

### 2.3 RSNPユニットとPCとの接続  

RSNPユニットの初期設定を行うために，PCと有線で接続します．現状，LANケーブルで接続する方法のみがあります． 
※この方法で接続する場合，予め設定してあるソフトウェアでないと接続できません．ご利用予定の方は，冒頭の連絡先にご連絡ください．  

**LANケーブルとの接続**  
LANケーブルでPCに接続するために，以下の図に示すように配線します．ケーブルの種類は，クロスかストレートのどちらでも接続可能です． PCとの接続には，LANからUSB-typeA変換ハブ，LANからUSB-typeC変換ハブを使用すれば，PCにLANポート(Ethernetポート)が無くても，接続可能です．  

<img src="https://user-images.githubusercontent.com/44587055/63603082-cf803c00-c603-11e9-9604-efef516c6334.png" width=45%>  

LANポート同士で接続した場合  

<img src="https://user-images.githubusercontent.com/44587055/63603092-d60eb380-c603-11e9-88ed-a2e9b6bb35d4.png" width=45%>  

USB-typeAに接続した場合  

<img src="https://user-images.githubusercontent.com/44587055/63603101-dc9d2b00-c603-11e9-8295-bd30382e91f9.png" width=45%>  

USB-typeCに接続した場合  

### 2.4 RSNPユニットに接続する  

#### ケース1-Linux，Mac OSの場合  

Linuxを使用している場合，次のコマンドを実行することで，RSNPユニットに接続することができます．  
`~$ ssh pi@rsnpunit.local -p 22`  

#### ケース2-Windowsの場合

RSNPユニットにリモートでSSH接続するためのソフトウェアが必要になります．  
設定すれば，コマンドプロンプトからRSNPユニットへ接続することもできますが，今回は，ソフトウェアを使用します．クライアントソフトウェアとして**Tera Term**を使用します．  

#### 2.4.1 Tera Termのダウンロード＆インストール  
  
以下のサイトより，ダウンロードとインストールを行ってください．  
**窓の杜 Tera Term**  
https://forest.watch.impress.co.jp/library/software/utf8teraterm/  

<div style="page-break-before:always"></div>  

#### 2.4.2 RSNPユニットに接続  

次に，インストールしたTera Termを起動します．  

以下のような画面が表示されます．  
 <img src="https://user-images.githubusercontent.com/44587055/58787570-08240100-8625-11e9-84c8-be85ba970c81.png" width=60%>  

ここで，ホストに"rsnpunit"と，TCPポートに"22"と入力し，"OK"をクリックします．  

#### 2.4.3 Raspberry Piにログイン  

次にRaspberry Piにログインをします．  
上記で"OK"をクリック後に以下のような画面が表示されます．  
 <img src="https://user-images.githubusercontent.com/44587055/58788978-014abd80-8628-11e9-87a8-6826dc60c4a5.png" width=60%>  

ユーザ名に"pi"と，パスフレーズに"8073"と入力し，"OK"をクリックします．  

<div style="page-break-before:always"></div>  

#### ケース1，ケース2-共通  

RSNPユニットに接続すると以下のような画面が表示されます．  

<img src="https://user-images.githubusercontent.com/44587055/63604122-ffc8da00-c605-11e9-9512-c9dffb785908.png" width=60%>  

### 2.5 無線LAN接続設定  

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
接続されたか確認のため，以下のようにコマンドを入力し実行します．  
`~$ ifconfig`  
`wlan0:`という項目の`inet`の行に数字の羅列が載っていれば，接続されています．
数字が無い場合は，再度，SSID，パスワードの確認し，RSNPユニットの再起動をしてください．  

再起動のコマンドは，以下のとおりです．
`~$ sudo reboot`
なお，シャットダウンのコマンドは，以下のとおりです．  
`~$ sudo poweroff`

以上で，無線LANの設定は終了になります．  

<div style="page-break-before:always"></div>  

### 2.6 java(jdk)のインストール  

java(jdk)をインストールします．以下のようにコマンドを入力し実行します．  
`~$ sudo apt-get install openjdk-8-jdk`  
java(jdk)がインストールされたか念のため確認します．以下のようにコマンドを入力し実行します．  
`~$ java -version`
これでバージョンが表示されれば，インストール完了です．  

### 2.7 GitHubからファイルをダウンロード  

必要なファイルをダウンロードします．  
まず，任意のディレクトにダウンロードします．  
今回はホームディレクトリにダウンロードします．
ホームディレクトリに戻るために，次のようにコマンドを入力し実行します．  
`~$ cd`  
リポジトリをクローンします(ファイルをダウンロードします)．次のようにコマンドを入力し実行します．  
`~$ git clone https://github.com/SatoshiOkano/RSNPUnit.git`  
ダウンロードが成功したか確認するため，以下のようにコマンドを入力します．  
`~$ ls`  
ダウンロードが成功していれば，`"RSNPUnit"`というディレクトリが存在します．  

### 2.8 propertiesファイルの設定  

前節でダウンロードした`"DataLog"`ディレクトリに移動します．  
以下のようにコマンドを入力し実行します．  
`~$ cd ~/RSNPUnit/DataLog/`  

移動すると，`"Config.properties"`というファイルがあります．  
次に，以下のようにコマンドを入力します．  
`~$ sudo nano Config.properties`  

デフォルトでは，以下のように記述されています．  

~~~text
Configuretion
robot_id  = 1  
robot_pw  = 8073  
end_point = http://robots.aiit.ac.jp:8080/UpdateNotificationState/services
send_interval = 10000
ip_address = 127.0.0.1
port = 8000
~~~  

各パラメータの意味は，次のようになっています．  

- **robot_id** ： ロボットの識別ID
- **robot_wd**：  ロボット固有のパスワード
- **end_point** ： データを送信するサーバのアドレス  
- **send_interval** ： 送信時間間隔,単位は[ms]
- **ip_address** : RSNPユニット本体のIPアドレス
- **port** ： Socket通信のポート番号  

必要に応じて，これらの各パラメータを変更します．  

<div style="page-break-before:always"></div>  

## 3 RSNPユニットの動作実行  

プログラムを起動してから，接続する必要があるので注意してください．  

### 3.1 RSNP通信プログラムの実行  

まず，`"RSNPNotifi.jar"`を実行します．  
`~$ cd`でホームディレクトリに移動します．  
`RSNPUnit`ディレクトリに移動するため，以下のようにコマンドを入力します．  
`~$ cd ~/RSNPUnit/`  
※RSNPUnitSystemDirの場所によって異なるので注意してください．

次に，実行するために以下のようにコマンドを入力します．  
`~$ java -jar RSNPNotifi.jar`  
※現状，jdk1.8以下で動作します．jdk10以上では動作しませんのでご注意ください．  

停止するときは，"Ctrl"+"c"キーを入力することで停止します．  

### 3.2 プログラム実行のデーモン化  

このままだと，RSNPユニットを動作する際に，毎回ログインを行い，コマンドを入力し実行する必要があります．そこで，プログラム実行を，RSNPユニットに電源を投入した際に自動で行うようにします．これをデーモン化といいます．ここでは，デーモン化の設定を行います．まず，サービスファイルの作成を行います．ただ，今回は既に作成してあるファイルを特定のディレクトリに移動するだけです．次のように，コマンドを入力し実行します．  
`~$ sudo cp ~/RSNPUnit/Service/rsnpnotifi.service /etc/systemd/system/`  
また，起動用のshファイルをコピーします．  
`~$ sudo cp ~/RSNPUnit/Service/Running.sh /home/pi/`  
次に．サービスファイルの登録を行います．  
`~$ sudo systemctl enable rsnpnotifi.service`  
次に，サービスファイルのリロードをします，次のようにコマンドを入力し実行します．  
`~$ sudo systemctl daemon-reload`  
起動します，次のようにコマンドを入力し実行します．  
`~$ sudo systemctl start rsnpnotifi.service`  
サービスが動いているか確認します．次のようにコマンドを入力し実行します．  
`~$ sudo systemctl status rsnpnotifi.service`  
これでデーモン化は完了です．  
deamon.log が大容量になることがあるので、ログ機能をオフにします．  
`~$ sudo nano /etc/rsyslog.conf`  
この conf ファイル内の記述を変更します．  
`daemon.* -/var/log/daemon.log`  
この記述を探し，コメントアウトします．  
`#daemon.* -/var/log/daemon.log`  
ファイルを保存し終了します．  

### 3.3 RTミドルウエアでの接続を行うケース  

ロボットまたはデバイスがRTミドルウエアを実装している場合，こちらのケースでRSNPユニットと接続することを推奨します．Socket通信を用いてRSNPユニットと接続します．  

<img src="https://user-images.githubusercontent.com/44587055/63647106-7a553f00-c757-11e9-85ab-3d12445eaf94.png" width=50%>  

以下の各バージョンで動作確認済みです．  

|               OS                | OpenRTM-aist ver. |
| :-----------------------------: | :----------: |
| Windows 7,Windows 8, Windows 10 | 1.1.2, 1.2.0 |

次のURLから"RSNPUnitConnector Comp"をダウンロードをしてください．  
https://github.com/SatoshiOkano/RSNPUnit.git  

`RSNPUnit/RSNPUnitConnector_RTM_rtc/RSNPUnitConnectorComp`内に`RSNPUnitConnector.py`があるので，RTCを起動するにはこのpyファイルを実行してください．また，テストデータ送信用RTCとして`SampleSendTest RTC`を用意してあります．任意のデータをコンフィグレーションパラメータに適用することで`RSNPUnitConnector RTC`に送信することができます．`RSNPUnit/RSNPUnitConnector_RTM_rtc/SampleSendTestComp`内に`RSNPUnitConnector.py`があるので，RTCを起動するにはこのpyファイルを実行してください．  

RSNPUnitConnector RTCの仕様は，次の表のとおりです．  

<img src="https://user-images.githubusercontent.com/44587055/63603822-5386f380-c605-11e9-8deb-563cd069e728.png" width=40%>  

SampleDataIn(Inport)には，フォーマットに準拠したデータを送る必要があります．フォーマットに関しては，"4章 通信データ仕様"に記しているので，参照してください．また，TimedString型のInportを設けていますが，最終的にフォーマットに準拠したデータを出力できれば，他に作成し直して構いません．Python言語で作成してあります．

#### RSNPユニットに接続する  

コンフィグレーションパラメータの"IPaddress"と"SocketPort"は，"2.8節 propertiesファイルの設定"と同じ値に設定する必要があります．設定後，RTCをアクティベートにすることで，RSNPユニットに接続することができます．正常に接続できれば，RTCはグリーンになりアクティベート状態になります．  

<img src="https://user-images.githubusercontent.com/44587055/63647401-b5597180-c75b-11e9-9715-994c98419a74.png" width=45%>  

<div style="page-break-before:always"></div>  

### 3.4 ROSでの接続を行うケース  

ロボットまたはデバイスがROSを実装している場合，こちらのケースでRSNPユニットと接続することを推奨します．Socket通信を用いてRSNPユニットと接続します．パッケージ名はrsnpunitconnector_pkg，ノード名はrsnpunitconnectorとなります．  

<img src="https://user-images.githubusercontent.com/44587055/63647169-197a3680-c758-11e9-946c-e9c56fe8ace9.png" width=50%>  

|               OS                | ROS ver. |
| :-----------------------------: | :----------: |
| Ubuntu 16.04, Ubuntu18.04 | Kinetic, Melodic |

次のURLから"rsnpunitconnector"をダウンロードをしてください．
https://github.com/SatoshiOkano/RSNPUnit.git  

`rsnpunitconnector_pkg/src`内に`rsnpunitconnector.py`があるので，nodoを起動するにはこのpyファイルを実行してください．また，テストデータ送信用nodeとして`samplesendtest`を用意してあります．現状，カウントと時刻のデータを出力する仕様となっています．実装する際にはそちらを参考にしてください．また，`rsnpunitconnector_pkg/msg`内では，msgファイルを定義していますが，string型の`message_data`となっています．subscribe topicsには，フォーマットに準拠したデータを入れる必要があります．フォーマットに関しては，"4章 通信データ仕様"に記しているので，参照してください．また，String型のmsgを設けていますが，最終的にフォーマットに準拠したデータを出力できれば，他に作成し直して構いません．Python言語で作成してあります．  

#### RSNPユニットに接続する  

`rsnpunitconnector_pkg/src`内に`config.ini`があるので，RSNPユニットに接続するためにはそれを編集します．設定したパラメータでプログラムを実行するためにconfig.iniの"IPaddress"と"Port"は，"2.8節 propertiesファイルの設定"と同じ値に設定する必要があります．  

<div style="page-break-before:always"></div>  

### 3.5 ミドルウエアを使用していない，Socket通信で接続するケース  

ロボットまたはデバイスがミドルウエアを実装していない場合，提供しているサンプルソースコードをもとに実装してください．現状，Python言語のみの提供ですが，C++，Javaのサンプルソースコードも提供予定です．  

<img src="https://user-images.githubusercontent.com/44587055/63647183-580ff100-c758-11e9-8fe6-68b29c98bb44.png" width=50%>  

次のURLからサンプルソースコードをダウンロードをしてください．
https://github.com/SatoshiOkano/RSNPUnit.git  

`RSNPUnit\RSNPUnitConnector(Socket_sample)`内の`Socket_sam.py`がサンプルソースコードとなります．  
`Config.ini`は，パラメータ設定ファイルとなります．  

#### RSNPユニットに接続する  

設定したパラメータでプログラムを実行するためにConfig.iniの"IPaddress"と"Port"は，"2.8節 propertiesファイルの設定"と同じ値に設定する必要があります．

### 3.6 ミドルウエアを使用していない，Serial通信で接続するケース  

ロボットまたはデバイスがミドルウエアを実装していない場合，こちらのサンプルソースコードをもとに実装してください．現状，Python言語のみの提供ですが，C++，Javaのサンプルソースコードも提供予定です．また，Python言語の本サンプルソースコードを使用するには，シリアル通信をするためのpythonモジュールである"pyserial"が必要となります．pip等を使用して予め"pyserial"をダウンロードする必要があります．  

<img src="https://user-images.githubusercontent.com/44587055/63647186-6fe77500-c758-11e9-8daf-3ce94a0ca5f1.png" width=50%>  

次のURLからサンプルソースコードをダウンロードをしてください．
https://github.com/SatoshiOkano/RSNPUnit.git  

`RSNPUnit\RSNPUnitConnector(Serial_sample)`内の`Serial_sam.py`がサンプルソースコードとなります．  `Config.ini`は，パラメータ設定ファイルとなります．  

#### RSNPユニットに接続する  

設定したパラメータでプログラムを実行するためにConfig.iniの"IPaddress"と"Port"は，"2.8節 propertiesファイルの設定"と同じ値に設定する必要があります．  

### 3.7 RSNPユニットハードを使わないケース  

本システムはRSNPユニットを外付けすることで容易にRSNP通信できます．しかし，ユニットハードを用いなくても，PC上でRSNPNotifi.jarを実行し，それにSocket通信でデータ送信することで，RSNP通信できます．  

<img src="https://user-images.githubusercontent.com/44587055/68920189-d9a37800-07b7-11ea-9419-a63dbe55434b.png" width=60%>  

次のURLからサンプルソースコードをダウンロードをしてください．
https://github.com/SatoshiOkano/RSNPUnit.git  

`RSNPUnit`内の`RSNPNotifi.jar`がメインの実行ファイルととなります．実行するために以下のようにターミナルまたはコマンドプロンプト等でコマンドを入力します．  
`~$ java -jar RSNPNotifi.jar`  

#### RSNPユニットに接続する  

設定したパラメータでプログラムを実行するためにConfig.iniの"IPaddress"と"Port"は，"2.8節 propertiesファイルの設定"と同じ値に設定する必要があります．"IPaddress"はローカルホストである"127.0.0.1"で接続することを推奨します．  

### 3.8 状態の確認  

ロボットまたはデバイスからRSNPユニットにデータを送信すると，RSNPでサーバに送信されます．
サーバにアクセスすることでWebブラウザ上に状態が反映されているか確認することができます．  

デフォルト設定のままの場合，以下のURLにアクセスすることで確認することができます．  
http://robots.aiit.ac.jp:8080/Robomech2019/  

以下のようにブラウザ上で表示されていれば，確認完了です．  
今回は，単にRaspberryPiの稼働状況と，それに接続されたセンサの状態を表示する一例となっています．

"robot_id"=1のロボットで"result"="test_string"を送信した例を下の図に示す．  
<img src="https://user-images.githubusercontent.com/44587055/68925161-ce574900-07c5-11ea-93fb-5263e5ad1dc5.png" width=60%>  

他にもロボットの画像に差し替えたり，表示するデータの種類も変更して表示情報を変更することができます．  

## 4. RSNPユニットへの通信データ仕様

RSNPユニットからロボットまたはデバイス間のデータのやり取りはSocket,Serial通信で行います．  
送信データは現状，**文字列型データ**です．ただし，以下の5種類のデータで定義づける必要があります．  

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
`{"data":[{"ac_id":"1","ac":"挨拶回数","re_id":"1","re":3,"co":""},{"ac_id":"2","ac":"人数","re_id":"2","re":5,"co":""}]}`  
となります(コメントは無しのため，空欄("")となっています)．つまり，最終的にこのデータ形式で**文字列型データ**で送信することになります．  
データが複数種類の場合は，配列の成分が増加し，  
``{"data":[{...},{...},{...},...]}``  
となります．今回は5種類まで対応しています．  

## 5. ライセンス  

本プロジェクトで作成したソフトウェアのライセンスは，MIT Licenseとなります．  
https://github.com/SatoshiOkano/RSNPUnit/blob/master/LICENSE  

## 参考文献  

[1] NEDO "2035年までのロボット産業の将来市場予測"，http://www.nedo.go.jp/content/100080673.pdf, 最終閲覧日2019年8月20日  
[2] ロボットサービスイニシアチブ，Robot Service Network Protocol2.3 仕様書 第1.0版，2010  
[3] OpenRTM-aist, https://openrtm.org/openrtm/ja, 最終閲覧日2019年8月20日  
[4] ROS Wiki, http://wiki.ros.org/ja, 最終閲覧日2019年8月20日  
