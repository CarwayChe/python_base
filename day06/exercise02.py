#练习２：经理：[曹操,刘备,孙权]  技术员：[曹操,刘备,张飞,关羽]
#计算：
#1. 即是经理也是技术员的有谁？
#2. 是经理，但不是技术员的有谁？
#3. 是技术员，但不是经理的有谁？
#4. 张飞是经理吗？
#5. 身兼一职的都有谁？
#6. 经理和技术员总共有多少人？

list01 = ["曹操","刘备","孙权"]
list02 = ["曹操","刘备","张飞","关羽"]

set01 = frozenset(list01)
set02 = frozenset(list02)
#1. 即是经理也是技术员的有谁？
print(set01  &  set02)

#2. 是经理，但不是技术员的有谁？
print(set01  - set02)

#3. 是技术员，但不是经理的有谁？
print(set02  - set01)

#4. 张飞是经理吗？
print("张飞" in set01)

#5. 身兼一职的都有谁？
print(set02  ^ set01)

#6. 经理和技术员总共有多少人？
print(len(set02  | set01))
