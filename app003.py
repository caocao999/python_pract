#日誌自動生成アプリ
# 2020.08.26
#
#
import sys
from datetime import datetime
from datetime import date
import time


#===========================================
if  len(sys.argv) != 2:
    print("お名前（途中に空白なし）を入力してください")
    sys.exit(1)

#ヘッダ生成
header = """
====================================
お疲れ様です。{0}です。
{1}の業務報告をいたします。

""".format(sys.argv[1],date.today())



#勤務場所を記入　
def workingplace():
    tmp = input("勤務場所を入力してださい")
    s_place = "[勤務地]:"+tmp
    return s_place

#勤務時間を記入　
def workingtime():
    w_begin = input("勤務開始時間を入力してださい")
    w_end = input("勤務終了時間を入力してださい")
    s_time = "[勤務時間]:{0} ~ {1}".format(w_begin,w_end)
    return s_time

#勤務内容
def workingtasks():
    body = ""
    count = 0
    max_tasks  = 5;
    msg ="""


          最大５項目の作業が入力可能です。"
          途中、終了の場合は改行のみを入力"


    """
    print(msg)
    while count < max_tasks:
        count = count + 1
        buff = input("行った作業内容を入力してください。")
        if len(buff)  == 0 :
            break
        task = "[作業内容{0}]:".format(count)+buff
        body = body + "\n"+ task
    return body





#==============================================================
#
#  ファイルへの書き込み
#

if  __name__ == '__main__':
    title = "業務報告{0}.txt".format(date.today())
    m_place = workingplace()
    m_time = workingtime()
    m_tasks = workingtasks()
    body = """
    {0}
    {1}
    {2}
    """.format(m_place,m_time,m_tasks)



file = open(title,"w")
file.write(header)
file.write(body)
file.close()
