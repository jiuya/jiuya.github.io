Title: ODROID-HC4のススメ
Date: 2020-12-21
Tags: develop,odroid,ubuntu,hubot

この記事は[高知工科大 Advent Calendar 2020](https://adventar.org/calendars/5887)の17日目の記事です。  
そしてこの記事はメモなのでそのうち更新されるかもしれない。  

## ODROID-HC4とは
韓国SBCメーカーHardkernel社のNAS向けSBCである。    

![ODROID-HC4](https://cdn.hardkernel.com/wp-content/uploads/2020/10/ODROID-HC4_hdd-800x800.jpg)  

画像を見てもらうと分かる通りSATA接続でHDDがそのままブッ刺せる。  
一見外付けHDDに見えるが、正体はHDDが刺せるSBC。もちろんSSDでも動く。  
3.5inch以外に一応2.4inchも刺さる。（固定されないので不安定ではある）  

正面からは見えないが、1xMicroSDスロット・1x1GbEポート・1xUSB2.0・1xHDMI2.0(4K/60Hz出力可能)がついている。  
ブートはMicroSD/SATA(HDD/SDD)/USBストレージ/PXEから可能。（MicroSDからが楽ではある）  
HDMI2.0がついておりS905X3（STBなどで採用されているSoC）なので、メディアプレイヤー的な使い方も可能。  

電源が15V4A品と微妙に手に入りづらいので買うときに一緒にACアダプタも買ったほうが良い。(ACアダプタは$9.4)  

**自分の思う利点をまとめると**  

- そこそこ速度の出るSATAポートが２つある。
- mainline linux kernel Ubutnu20.04が動く。
- NASとラズパイなんかで動かしていたBotなどが小さな機器で完結する。
- HDDの物理的な換装が容易。
- NASを買うと思うと安い。$65 + $9.4(ACアダプタ) + 送料
- いろいろイジる用SBCを常時稼働させる理由を作れる。（自分にとっては地味に一番利点）
   
**要するにSBC収集家にとっては中々イカスSBCなのである。**  

## 現在の環境
- OS: Armbian_20.11.3_Odroidhc4_focal 
- Linux Kernel: 5.9.14
- SATAスロット1: 6TB
- SATAスロット2: 空き 
- ssh,xrdp セットアップ済み
 
#### NAS
- Sambaを動かしNAS運用している。 

```console
$ sudo apt -y update
$ sudo apt -y upgrade
$ sudo mkdir /mnt/hdd
$ sudo bash -c 'echo "/dev/sda1       /mnt/hdd        ntfs-3g permissions,locale=ja_JP.UTF-8  0       2" >> /etc/fstab'
$ sudo apt -y install samba
$ sudo vim /etc/samba/smb.conf // sambaの設定をここでする
$ sudo pdbedit -a ユーザー名
$ sudo systemctl enable smbd
$ sudo reboot
```

#### Slack Bot
- HubotでWOL サーバーにしている。[参考文献](https://k-side.hatenablog.jp/entry/2016/05/30/180000)  
  （自分用Slackチームで ```@home wol``` と打つと自宅のメインPCにWOLパケットが送られるサーバー）  
![slack-wol.png](images/slack-wol.png)  

Hubot・wakeonlan インストール/setup  

```console
$ sudo apt -y install nodejs
$ sudo apt -y install npm
$ sudo apt -y install wakeonlan
$ mkdir ~/hubot
$ mkdir ~/hubot/magic
$ cd ~/hubot/magic
$ sudo npm install -g coffee-script hubot
$ sudo npm install -g yo generator-hubot
$ sudo npm install -g forever
$ sudo vim /etc/systemd/system/hubot.service //systemd ユニットファイル書く
$ sudo systemctl daemon-reload
$ sudo systemctl enable hubot
```
スクリプト部分は割愛  

#### [narou.rb](https://github.com/whiteleaf7/narou/wiki)
- narou.rb の narou WEB UIサーバーを動かして、ローカルLAN内からアクセスできるようにしている。
- Web UI上にURLを貼り付けるとダウンロード・ePub変換され、GoogleDriveにePubが保存されるようにしている。(narou.rbのePub保存先にGoogleDrive([google-drive-ocamlfuse](https://github.com/astrada/google-drive-ocamlfuse))を指定している)
- (そしてGoogle Drive上のePubをAndroidのMoon+ Readerで読む!快適！)

narou.rb インストール。  

```console
$ sudo apt install -y ruby
$ sudo apt install -y ruby-dev
$ sudo apt install -y default-jre
$ sudo gem install narou
$ sudo vim /etc/systemd/system/narou-web.service //systemd ユニットファイル書く
$ sudo systemctl daemon-reload
$ sudo systemctl enable narou-web
```
google-drive-ocamlfuse インストール。(ブラウザ認証があるのでxrdp上のシェルで)  

```console
$ sudo add-apt-repository ppa:alessandro-strada/ppa
$ sudo apt update
$ sudo apt -y install firefox firefox-locale-ja // GUIのブラウザで認証のため
$ sudo apt install -y google-drive-ocamlfuse
$ google-drive-ocamlfuse
```
```sudo vim /usr/bin/gdfuse``` で以下の内容を書き込む。（ユーザー名は認証時のLinuxユーザー名）

```bash
#!/bin/bash

su ユーザー名 -l -c "/usr/bin/google-drive-ocamlfuse -label $1 $*"
exit 0
```
```/mnt/gdrive```にマウント。
```console
$ sudo mkdir /mnt/gdrive
$ sudo bash -c 'echo "gdfuse#default  /mnt/gdrive     fuse    uid=1000,gid=1000,allow_other,user,_netdev     0       0" >> /etc/fstab'
$ mount -a
```
narou WEB UI上でePub出力先を```/mnt/gdrive```以下の好きなディレクトリに設定する。  

## 今後したいこと
- SATAスロットが一本空いてるのでそのうちソフトウェアRAID1したい。
- Slackに```@home narou URL```とすることでなろう小説をダンロード・ePub変換を走らせたい。（やってみたがHubotのスクリプトで```narou download URL```が動かない。有識者求む。）
- microSDの命が消える前にイメージバックアップを仕込みたい。

## 参考
[Slack から Hubot 経由で会社にあるパソコンの電源をオンにする](https://k-side.hatenablog.jp/entry/2016/05/30/180000)