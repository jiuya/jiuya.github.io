Title: Raspberry Pi でfishのビルド
Date: 2018-04-24
Tags: develop,Raspberry Pi,fish shell

## 動機
- 自分のメインの環境をfishにしてfishの楽さを知ってしまったのでラズパイにも入れたい。
## 環境
- Raspberry Pi 3 Model B V1.2
- rasbian-stretch-lite 2018-04-18

## 準備
- 必要なパッケージをインストールする。
```
$ sudo aptitude install cmake autoconf git g++ libncurses5-dev \
gettext libreadline-dev libeditline-dev doxygen libedit-dev
```
## ビルド
```
$ git clone https://github.com/fish-shell/fish-shell.git
$ cd fish-shell
$ mkdir build
$ cd build
$ cmake .. -DCMAKE_BUILD_TYPE=Release
$ make
$ sudo make install
```
