Title: neovimのset pasteの挙動
Date: 2018-04-23
Tags: develop,neovim

## 問題点
- neovim の `:set paste`の挙動がvimのときと反対になってるように見える。
- つまり、defaultでインデントがある文字列がそのまま貼り付けできて、`:set paste`をするとindentが入ってしまう。

## 環境
- neovim v2.2.0
- tmux 2.3
- fish 2.7.1

## 調べる
- 落ち着いて`:help paste`を見てみる。
- [neovim option](https://neovim.io/doc/user/options.html#'paste')
```
This option is obsolete; |bracketed-paste-mode| is built-in.
```
- なんかneovimではpaste optionは廃止されているらしい。
- brackted-paste-mode とは？
- [bracketed paste mode](https://cirw.in/blog/bracketed-paste)
- xtermの拡張で貼り付け時に文字列の前に`<ESC>200~` 後ろに`<ESC>201~` がつくようになる。
- つまり、手で打った文字かpasteした文字かを判別することができる。
- [vim で bracketed paste modeに対応させる記事](https://srad.jp/~doda/journal/506765/)もあった。

## 結論
- 最近の端末はBracketed Paste Mode に対応しているのでneovimではset pasteする必要はない。
- neovimでset pasteしたときにインデントが入ってしまうのは謎だがobsoleteなんだから使わなければいいや。

## 参考
- [neovim option](https://neovim.io/doc/user/options.html#'paste')
- [bracketed paste mode](https://cirw.in/blog/bracketed-paste)
- [XTerm Control Sequences](http://invisible-island.net/xterm/ctlseqs/ctlseqs.html#h2-Bracketed-Paste-Mode)

