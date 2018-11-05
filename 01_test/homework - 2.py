# -*- coding: utf-8 -*-
def product(*numbers):
	if numbers is None
		raise TypeError
	sum = 1
	for n in numbers:
		sum = sum * n
	return sum

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('1测试失败!')
elif product(5, 6) != 30:
    print('2测试失败!')
elif product(5, 6, 7) != 210:
    print('3测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('4测试失败!')
else:
    try:
        product()
        print('5测试失败!')
    except TypeError:
        print('6测试成功!')