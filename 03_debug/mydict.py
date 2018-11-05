#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$
class Dict(dict):
	"""docstring for MyDict"""
	def __init__(self, **kw):
		super().__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError as e:
			raise AttributeError(r"'dict' object has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value	
		

