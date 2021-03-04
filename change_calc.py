#つり銭計算プログラム雛形


def input_number(msg):
    msg = msg + " : "
    return int(input(msg))

def change_calc(denom,change,result_dic):
    tmp = change // denom
    coins[denom] = tmp
    return change - denom * tmp

if __name__ == '__main__':
    coins ={500:0,100:0,50:0,10:0,5:0,1:0}
    price = input_number("商品価格");
    amt = input_number("投入金額");

    #釣り銭金額の計算
    change = amt - price
    print("===============================================")
    print("受取金額{0}　入金額{1}　　お釣り金額{2}".format(price,amt,change))
    print("===============================================")
    print("(お釣り金種内訳)")

    #金種ごとに必要な硬貨の枚数の計算
    change = change_calc(500,change,coins)
    change = change_calc(100,change,coins)
    change = change_calc(50,change,coins)
    change = change_calc(10,change,coins)
    change = change_calc(5,change,coins)
    change = change_calc(1,change,coins)

    #金種の内訳表示
    for k, v in coins.items():
        print("{0: >3}円硬貨:{1: >2}枚".format(k,v))
