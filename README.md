# LineNotify

## About

LineNotifyAPI を用いて、特定の LINE グループに対してメッセージ及び画像を送信するためのツール  
他プログラムなどからライブラリとして読み出されることを前提に作成されている  
[LineNotify](https://notify-bot.line.me/ja/)  
[LINE Notify API Document](https://notify-bot.line.me/doc/ja/)

## main.py

オブジェクト指向で記述されている  
このファイルをライブラリとして読み出すことが推奨される  
このプログラムを単体で実行することで、プロンプトより送信することもできる

## command.py

コマンドライン引数で main.py の操作を可能にしたもの  
使用法: `python command.py {TokenName} {Message} {ImagePath(optional)}`  
例: `python command.py MyTalkRoom HelloWorld! C:/image.png`

## tokens/tokens.json

ここに使用するトークンを保存することを推奨する  
キーの名前でそのトークンを呼び出す事ができる  
機密情報のため、取り扱いには注意すること  
本リポジトリには`tokens-sample/tokens.json`内にサンプルファイルがある  
`tokens-sample`から`tokens`にディレクトリ名を変更することで使用できる

## Pythonのバージョン

`Python 3.11.6` で動作を確認済み  
Python3 系統であればおそらく動く(たぶん)

## 必要なライブラリ

| main.py            | command.py |
| ------------------ | ---------- |
| requests, os, json | sys        |

注: command.py を使用する際には、main.py のライブラリも必要である
