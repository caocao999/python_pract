#  データ構造　 リスト（≒配列）
#
#   キーボードから月（数字）を入力すると、その英略語が表示される   　　
#　　
#


#これがリスト
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]

m = int(input("お好きな月を数字で入力してくダサい(1-12)　：　"))

print(months[m-1])
