import requests, os, json


class LineNotify:
    """
    .token = 送信するトークン
    .message = 送信するメッセージ
    .imege = 画像データ(任意)
    """

    def __init__(self):
        self.image = None

    def GetToken(self, TokenName: str):
        """
        トークンリストからトークンを取得
        """
        TokensPath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "tokens/tokens.json"
        )
        try:
            with open(TokensPath, mode="r", encoding="utf-8") as TokensFile:
                Tokens = json.load(TokensFile)
            Token = Tokens[TokenName]
        except:
            raise NameError("File not found")
        else:
            return Token

    def OpenImage(self, ImagePath):
        """
        画像ファイルの取得
        """
        try:
            Image = open(ImagePath, "rb")
        except:
            raise NameError("File not found")
        else:
            return Image

    def SendLine(self):
        """
        送信
        """
        Url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"message": self.message}
        try:
            if self.image is None:
                re = requests.post(Url, headers=headers, data=data)
            else:
                files = {"imageFile": self.image}
                re = requests.post(Url, headers=headers, data=data, files=files)
        except:
            raise Exception("Bad Requests")
        else:
            return {"status_code": re.status_code, "text": re.text}


def main():
    TokenName = input("TokenName:")
    Line = LineNotify()
    try:
        Line.token = Line.GetToken(TokenName)
    except:
        print("正しいファイルが見つかりません")
        exit()
    Line.message = input("Message:")
    if input("Send image?(y/n):") == "y":
        ImagePath = input("ImagePath:")
        try:
            Line.image = Line.OpenImage(ImagePath)
        except:
            print("正しい画像ファイル見つかりません")
            exit()
    try:
        re = Line.SendLine()
    except:
        print("送信に失敗しました")
        exit()
    else:
        print("Sended")


if __name__ == "__main__":
    main()
