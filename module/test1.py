# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023/10/30 9:45
# File : test1.py

string = "  hello world  "
pattern = "helloworld"

# 删除字符串前后的空格字符
string_stripped = string.strip()
print(string_stripped)

if pattern in string_stripped:
    print("匹配成功")
else:
    print("匹配失败")