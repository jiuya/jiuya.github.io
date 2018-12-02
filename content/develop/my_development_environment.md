Title: 自分の開発環境
Date: 2018-12-03
Tags: develop,debian,i3wm

この記事は[高知工科大 Advent Calendar 2018](https://adventar.org/calendars/2959)の三日目の記事です。
## 初めに
いよいよ毎年恒例Advent Calendarの時期がやってきました。

これといって書くことが思いつかなかったので2018年の自分の開発環境(Linux)でも書こうと思います。

主にマイコンの開発や組み込みLinuxの開発に使用してます。

## PC
PCはThinkPad X250を使用してます。
メモリが4GB(少ねぇ)でCPUがi5-5300Uです。重い作業はメインPC(Windows)でやらせるのでスペックは抑えめです。そのうちメモリ8GBにはしたいです。

## ディストリビューション
OSはDebianのStable(stretch)です。
Debianを選択した理由は主に以下の点です。
- Ubuntu Desktopと比べていらないものが入ってない。
- Ubuntu Desktopより簡単にディスプレイマネージャ、ウィンドウマネージャを変更できる。
- Gentooと比べて非力なPCでも初期セットアップが早い。
- Archはpacmanに慣れることができなかった。

サービスマネージャはDebianのdefaultのsystemdを使用しています。

## ディスプレイマネージャ、ウィンドウマネージャ
ディスプレイマネージャはLightDMです。選択理由はメジャーだから。むしろ他のディスプレイマネージャをあまり使ったことがない。

ウィンドウマネージャはタイル型ウィンドウマネージャのi3wmです。  
タイル型ウィンドウマネージャとはWindowsなどのようにウィンドウが重なることがなくタイル状に等間隔に配置されるウィンドウマネージャの総称です。  
i3の選択理由は以下の点です。
- ほぼキーボードで作業できる。一応マウスも使える。(自分のキーバインドでは```Windows key + Enter```でターミナルが開く、```Windows key + →```でウィンドウ移動など)
- ダイアログウインドウなどは普通のデスクトップ環境と同じように使える。ダイアログでないウインドウもショートカットキーでタイル化解除(フローティング化)させることが可能。  

```Windows key + Enter``` でターミナルを開らける快感を覚えると戻って来れなくなります。  
詳細は他のサイトに譲ります。  
[タイル型ウインドウマネージャーが凄い - i3wm](https://trap.jp/post/425/)

## ターミナル環境
使用しているターミナルは[Sakura](https://launchpad.net/sakura)を使用してます。  
テキストエディタでもサーバーの会社でもないです。  
```libvte(gnome-terminal)```ベースの端末エミュレータです。  
画面分割やタブなどの機能はtmuxやvimなどで行うので、シンプルなlibvteベースのターミナルがほしかったのでこれにしました。

## tmux
昔はscreenを使っていましたが今はtmuxです。  
prefixは```Ctrl+a```にしています。Caps LockをCtrlに割り当てているので、そこから近いaを選択しているだけです。minicomのdefaultのprefixと被っているのがちょっと問題ではあります。  

tpmを使ってplugin管理もしてます。
以下が入れているpluginです。
```
set -g @tpm_plugins '               \
 tmux-plugins/tpm                   \
 tmux-plugins/tmux-yank             \
 tmux-plugins/tmux-open             \
 tmux-plugins/tmux-resurrect        \
 tmux-plugins/tmux-battery          \
 tmux-plugins/tmux-pain-control     \
 tmux-plugins/tmux-copycat          \
 tmux-plugins/tmux-prefix-highlight \
'
```
```tmux-yank```や```tmux-copycat```などのコピー系プラグインは端末に表示されているすべての情報を簡単にコピーペーストできるので非常に便利です。  

## shell
shellはfish shell+neovimを使用しています。  
パッケージ管理にはFishermanを使用してます。  
fish は特に設定しなくても見やすくて使いやすいシェルになるのでおすすめです。  
ただbashやzshの記法に慣れているとパイプとかリダイレクトとかで自分はよく間違えるのでその辺はめんどくさいです。

## おわりに
2018年は転職?したりといろいろ変化のあった年だったので開発環境の入れ替えなどをしました。  
この辺の情報はすぐトレンドが移るのでこれからもキャッチアップし続けれる人間になりたいなーと思いました。  
書くの疲れたのでこの辺で終わります。

