


#文字列の作成
str1 = 'xyx'
str2 = "abc"
str3 = '''
<html>
<head>
    <title>
        Python 入門
    </title>
</head>
<body>

    <h1>Welcome</h1>
</body>
</html>
'''

print("===============str1=====================")
print(str1)

print("===============str2=====================")
print(str2)

print("===============str3=====================")
print(str3)


#文字列の連結
print("============文字列連結=========================")
s = "abc"+'xyz'
print(s)
s = s*10
print(s)

#文字列の抽出
print("============文字列抽出=========================")


i = 0
for c in "abcdefghijklmnopqrstuvxyz":
    print(" {0}:{1} ".format(i,c),end="")
    i = i + 1

s = "abcdefghijklmnopqrstuvxyz"

s = s[0:-1:2]

print()
print(s)



print()













#
