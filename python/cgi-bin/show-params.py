#!/user/bin/env python3
import cgi

# ヘッダの表示
print("Content-Type: text/html; charset=utf-8")
print("") # 空行

print("<pre>")
# URLパラメータを取得する
form = cgi.FieldStorage()

# formに"mode"が含まれるか?
if "mode" in form:
    print("mode=", form["mode"].value)
else:
    print("mode=空")

# 特定のパラメータを取得して表示
mode = form.getvalue("mode", default="")
print("mode=", mode)

# すべてのパラメータを取得して表示
print("--- all params ---")
for k in form.keys():
    print(k, "=", form.getvalue(k))
