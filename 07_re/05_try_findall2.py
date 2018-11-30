# -*- coding: utf-8 -*-

import re

# re模块提供一个方法叫compile模块，提供我们输入一个匹配的规则
# 然后返回一个pattern实例，我们根据这个规则去匹配字符串
# pattern = re.compile(r'\d+\.\d*')   # 匹配小数

# 通过partten.findall()方法就能够全部匹配到我们得到的字符串
# result = pattern.findall("123.141593, 'bigcat', 232312., 3.15")

# findall 以列表形式返回全部能匹配的子串，如果没有匹配，则返回一个空列表。
# print(len(result))

# print(type(result))

html_str = r'''
<h4>
                            <a href="/article/45061.html"><b>刘备三顾茅庐</b></a></h4>
                        <div class="f18 mb20">
                            　　刘备三人第三次来到隆中，诸葛亮在午睡，为了不打扰他，刘备恭敬地在台阶下等候。<br />
　　张飞见了，很生气刚要骂娘，被刘备训斥了。<br />
　　孔明醒来见刘备三顾茅庐，诚心诚意，就把房子卖给他了。
                            
                        </div>
                        <div class="ft">
                        <li><span class="pageinfo">共 <strong>506</strong>页<strong>5057</strong>条</span></li>
'''

# 找到所有的段子内容<div class = "f18 mb20"></div>
# re.S 如果没有re.S 则是只匹配一行有没有符合规则的字符串，如果没有则下一行重新匹配
# 如果加上re.S 则是将所有的字符串将一个整体进行匹配

pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)

result = pattern.findall(html_str)

print(result[0].replace("<br />", "").strip())
print("*"*100)
# findall 以 列表形式 返回全部能匹配的子串给result
for item in result:
    print(item)

pattern2 = re.compile(r'<span.*?class="pageinfo">.*?<strong>(\d+)</strong>', re.S)
total = pattern2.findall(html_str)
print(int(total[0]))
