'''
S = NP VP           -> 句子 = 名詞子句 + 動詞子句
NP = DET Adj* N PP* -> 名詞子句 = 定詞 + 名詞
VP = V NP           -> 動詞子句 = 動詞 + 名詞子句
PP = P NP           -> 副詞子句 = 副詞 + 名詞子句
'''

import random as r

PP = ['我', '他', '我們']
count = ['一杯', '兩杯', '三杯', '四杯']
drinks = ['奶茶', '冬瓜茶','紅茶', '綠茶','水果茶']
ice = ['冰塊正常','去冰','微冰','完全去冰']
ingredients = ['加珍珠','加粉圓','加QQ','加野果','加仙草']

def S():
    return NP() + ' ' + VP()
def NP():
    return N() + '要'
def VP():
    return  Number() + ' ' + WhatkindDrink()
def WhatkindDrink():
    return Drink() + ' ' +Detail()
def Detail():
    return r.choice(ice) + ' '+ r.choice(ingredients)
def N():
    return r.choice(PP)
def Drink():
    return r.choice(drinks)
def Number():
    return r.choice(count)

print(S())