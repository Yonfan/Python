# -*- coding: utf-8 -*-
def trim(s):
	if len(s) == 0:    #空字符串
	    return "" 
	n = 0              #全是空格
	for i in s:        
	    if i != " ":
	        break
	    n += 1;
	if n == len(s):
	    return ""
	while True:        #掐头
	    if s[0] == " ":
	        s = s[1:]
	    else:
	        break
	while True:        #去尾
	    if s[-1] == " ":
	        s = s[:-1]
	    else:
	        break 
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试1失败!')
elif trim('  hello') != 'hello':
    print('测试2失败!')
elif trim('  hello  ') != 'hello':
    print('测试3失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试4失败!')
elif trim('') != '':
    print('测试5失败!')
elif trim('    ') != '':
    print('测试6失败!')
else:
    print('测试成功!')