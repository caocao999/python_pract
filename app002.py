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
    task = input("行った作業内容を入力してください。")
    task = "[作業内容]:"+task
    return task





#==============================================================
#
#  ファイルへの書き込み
#
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
