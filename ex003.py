#  制御構造　 反復
#
#   １からキーボードで入力した数までの自然数の合計を計算する
#　　
#　　
#



val = int(input("数字を入力して下しさい : "))

i = 0
total = 0

while i <= val :
    total = total + i
    i = i + 1
#慣れてくればここはもう少し省略できる

print("合計の値は"+str(total)+"です")
