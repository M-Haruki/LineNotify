# python command.py {TokenName} {Message} {ImagePath(optional)}

import sys
from main import LineNotify

# コマンドライン引数の取得
args = sys.argv

if len(args) == 3:
    IsImage = False
elif len(args) == 4:
    IsImage = True
    ImagePath = args[3]
else:
    print("引数が不適切です。")
    print("使用法: python command.py {TokenName} {Message} {ImagePath(optional)}")
    exit()
Line = LineNotify()

TokenName = args[1]
Line.message = args[2]

# 実行
try:
    Line.token = Line.GetToken(TokenName)
except:
    print("正しいファイルが見つかりません")
    exit()
if IsImage:
    try:
        Line.image = Line.OpenImage(ImagePath)
    except:
        print("正しい画像ファイル見つかりません")
        exit()
    try:
        Line.SendLine()
    except:
        print("送信に失敗しました")
        exit()
    else:
        print("Sended")
else:
    try:
        Line.SendLine()
    except:
        print("送信に失敗しました")
        exit()
    else:
        print("Sended")
