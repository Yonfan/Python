# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5

bmi_xiaoming = weight / (height*height)
print('bmi_xiaoming = %.1f' % bmi_xiaoming)
if bmi_xiaoming < 18.5:
	print('过轻')
elif bmi_xiaoming < 25:
	print('正常')
elif bmi_xiaoming < 28:
	print('过重')
elif bmi_xiaoming < 32:
	print('肥胖')
else:
	print('严重肥胖')

