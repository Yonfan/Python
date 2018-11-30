# -*- coding: utf-8 -*-

import re

title = u'你好，hello， 世界'
# 中文的 unicode 编码范围 主要在 [u4e00-u9fa5]，这里说主要是因为这个范围并不完整，比如没有包括全角（中文）标点，不过，在大部分情况下，应该是够用的。
pattern = re.compile(r'[\u4e00-\u9fa5]+')
res = pattern.findall(title)

print(res)


