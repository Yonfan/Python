# -*- coding: utf-8 -*-

'''
当然我们可以通过WSGI来进行简单的web实现
但是一当客户的请求开始变得复杂起来的时候
你需要怎么去做？
利用 environ 提取出HTTP请求的信息，然后进行逐个判断吗？
显然这样做实在是太麻烦了！而且不利于维护！
于是就出现了web框架
Flask 是其中的一个比较流行的框架
'''

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'
@app.route('/signin', methods=['GET'])
def signin_form():
	return '''<form action="/signin" method="post">
			<p><input name="username" /></p>
			<p><input name="password" type="password" /></p>
			<p><input value="Sign In" type="submit" /></p>
			</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	# 需要从request对象读取表单内容：
	if request.form['username']=='admin' and request.form['password']=='password':
		return '<h3>Hello, %s!</h3>' % (request.form['username'])
	return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
	app.run()
