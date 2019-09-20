#!/usr/bin/env python3
# coding: utf8
import operator
players=[{'point': 0, 'name': 'A'},{'point': 5, 'name': 'B'},{'point': 5, 'name': 'A'},]
print(players)
players.sort(key=operator.itemgetter('name')) # 第2キー: name asc
print(players)
players.sort(key=operator.itemgetter('point'), reverse=True) # 第1キー: point desc
print(players)

