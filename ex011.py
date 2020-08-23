#  関数（引数あり）
#
#　 一年定期預金の金利計算      　　
#　　
#



#関数定義
def calc(pamt,pint):
    total = 0
    total = pamt+pamt*(pint/100.0)
    return total

#実際に画面にhelloと表示（４回）

amt = int(input("元金を入力してください　：　"))
interest_rate = float(input("年金りを％で入力してください　：　"))
ans = calc(amt,interest_rate)
print(ans)
