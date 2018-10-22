# モジュールのインポート
import syaku

# モジュールの関数を使う
v = syaku.syaku_to_cm(10)
print("10尺=", v, "cm")

v = syaku.syaku_to_cm(20)
print("20尺=", v, "cm")

# 短い名前の変数に代入する
s2cm = syaku.syaku_to_cm

print("10尺=", s2cm(10), "cm")
print("20尺=", s2cm(20), "cm")
