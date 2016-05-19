# -*- coding: utf-8 -*-
def fi(n):
	if n == 0:
		return 0
	elif n==1:
		return 1
	else:
		return fi(n-1)+fi(n-2)
