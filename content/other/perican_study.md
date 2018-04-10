Title: このサイトの更新方法
Date: 2018-04-09 13:43

# 更新しようとしたら使い方を忘れていたのでメモ


## 準備
- `$ pelican-quickstart` が行われているものとする。
- このリポジトリをクローンする。
```
$ git clone --recursive -b source https://github.com/jiuya/jiuya.github.io.git
```
- 必要なパッケージをインストールする。
```
$ pip install -r requirements.txt
```


## 記事を書く
- `content/` 以下に記事を書きマークダウンで保存する。

## Githubにアップロード
- マークダウン形式のファイルをHTMLファイルに変換する。
- 変換したファイルを**ghp-import**を使用してGithubにpushする。
```
$ make html
$ ghp-import output
$ git push -f origin gh-pages:master
```
- (追記) githubにアップロードはMakefileに含まれていた。
```
$ make html
$ make github
```
でも良い。

## 参考
- [PelicanとGitHub-pagesでブログ開設](https://qiita.com/akimach/items/dfcac164ac5669a6378://kazukousen.github.io/python-pelican-install.html)
- [ブログジェネレータをTinkererからPelicanに移行した](https://memo.laughk.org/2014/08/10/tinker2pelican-repo.html)

