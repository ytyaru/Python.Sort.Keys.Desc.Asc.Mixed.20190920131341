#!/usr/bin/env python3
# coding: utf8
import operator
names=[(1,'A'),(2,'B'),(2,'A'),(1,'C')]
print(names)
names.sort(key=operator.itemgetter(1)) # 第2キー
print(names)
names.sort(key=operator.itemgetter(0), reverse=True) # 第1キー
print(names)

