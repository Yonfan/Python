#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-06 21:08:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_FORM():
	return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('success.html', username = username)
	return render_template('form.html', message = 'sign failed!', username = username)

if __name__ == '__main__':
	app.run()
