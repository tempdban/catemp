#!/usr/bin/env python
#coding=utf-8

class baseca(object):
	"""docstring for baseca"""
	def __init__(self, arg1,arg2):
		self.__m = arg1
		self.__n = arg2
		self.__arr1 = {}
		self.__arr2 = {}
		for i in xrange(__m+2):
			for j in xrange(__n+2):
				__arr1[(__m,__n)] = 0
				__arr2[(__m,__n)] = 0
	def __checkmn(self, arg1,arg2):
		if arg1<__m and arg2<__n:
			return True
		else:
			return False
	def __plus1(self, arg1,arg2):
		return (arg1+1,arg2+1)
	def __0(self, arg1,arg2):
		if __checkmn(arg1,arg2):
			__arr2[__plus1(arg1,arg2)] = 0
		else:
			raise NameError("下标越界")
	def __1(self, arg1,arg2):
		if __checkmn(arg1,arg2):
			__arr2[__plus1(arg1,arg2)] = 1
		else:
			raise NameError("下标越界")
	def __revise(self, arg1,arg2):
		if __checkmn(arg1,arg2):
			__arr2[__plus1(arg1,arg2)] = int(not __arr1[__plus1(arg1,arg2)])
		else:
			raise NameError("下标越界")
	def __collect8(self,arg1,arg2):
		(m,n)=__plus1(arg1,arg2)
		return __arr1[(m-1,n-1)]+__arr1[(m-1,n)]+__arr1[(m-1,n+1)]+__arr1[(m,n-1)]+__arr1[(m,n+1)]+__arr1[(m+1,n-1)]+__arr1[(m+1,n)]+__arr1[(m+1,n+1)]
	def stepin(self,arg1,arg2):
		for m in xrange(__m):
			for n in xrange(__n):
				result=__collect8(m,n)
				if result==arg1:
					__1(m,n)
				elif result==arg2:
					pass
				else:
					__0(m,n)
		__arr1=__arr2
	def run(self,arg1,arg2):
		while True:
			stepin(arg1,arg2)