﻿from math import *
from PublicReference.base import *
    
class 元素圣灵技能0(主动技能):
    名称 = '烈焰冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2229
    成长 = 252
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 7

class 元素圣灵技能1(被动技能):
    名称 = '属性精通'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.30 + 0.02 * self.等级 , 5)


class 元素圣灵技能2(主动技能):
    名称 = '虚无之球'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 287
    成长 = 32
    攻击次数 = 8
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 元素圣灵技能3(主动技能):
    名称 = '冰墙'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4243.3
    成长 = 478.7
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 7

class 元素圣灵技能4(主动技能):
    名称 = '雷旋'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2111.275
    成长 = 238.725
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 7


class 元素圣灵技能5(主动技能):
    名称 = '天雷冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9102.7317
    成长 = 1028.2683
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2753


        
class 元素圣灵技能6(主动技能):
    名称 = '极冰盛宴'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 8266.7369
    成长 = 933.2631
    CD = 19.0
    TP成长 = 0.10
    TP上限 = 7


class 元素圣灵技能7(主动技能):
    名称 = '湮灭黑洞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 12854
    成长 = 1452
    CD = 35.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2783


class 元素圣灵技能8(主动技能):
    名称 = '杰克降临'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15037.0278
    成长 = 1697.9722
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.212

        
class 元素圣灵技能9(主动技能):
    名称 = '元素之幕'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14416.3044
    成长 = 1626.6956
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.CD *= 0.95
        self.倍率 *= 1.282
        
class 元素圣灵技能10(被动技能):
    名称 = '魔力增幅'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.075 + 0.015 * self.等级, 5)

class 元素圣灵技能11(主动技能):
    名称 = '陨星幻灭'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 74495
    成长 = 12300
    CD = 145.0
    def 等效CD(self, 武器类型):
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.0, 1)

class 元素圣灵技能12(主动技能):
    名称 = '元素震荡'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 26363.667
    成长 = 2977.333
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2364

class 元素圣灵技能13(主动技能):
    名称 = '圣灵水晶'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 38665.5625
    成长 = 4365.4375
    CD = 40.0

class 元素圣灵技能14(被动技能):
    名称 = '元素奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 元素圣灵技能15(主动技能):
    名称 = '元素之门'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 44675.235
    成长 = 5044.765
    CD = 45.0

class 元素圣灵技能17(主动技能):
    名称 = '第六元素'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 109517.4
    成长 = 33073.6
    CD = 180.0
    def 等效CD(self, 武器类型):
        if 武器类型 == '法杖':
            return round(self.CD / self.恢复 * 1.1, 1)
        if 武器类型 == '魔杖':
            return round(self.CD / self.恢复 * 1.0, 1)
    

class 元素圣灵技能16(主动技能):
    名称 = '圣灵符文'
    所在等级 = 75
    等级上限 = 11
    基础等级 = 1
    是否有伤害 = 0
    是否主动技能 = 1
    关联技能 = ['属性精通']
    冷却关联技能 = ['魔法秀']
    
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.118 + 0.0128 * self.等级 , 3)
            
    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.1458 + 0.0139* self.等级 , 3)
    
    
class 元素圣灵技能18(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    冷却关联技能 = ['冰墙','元素之门','元素之幕','元素震荡','圣灵水晶','烈焰冲击','天雷冲击','雷旋','杰克降临','湮灭黑洞','极冰盛宴','虚无之球']

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '魔杖':
            return round(1 - 0.0216 * self.等级 , 3)
        if 武器类型 == '法杖':
            return round(1.1*(1 - 0.0216 * self.等级), 3)
    
    
class 元素圣灵技能19(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 元素圣灵技能20(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 元素圣灵技能21(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

元素圣灵技能列表 = []
i = 0
while i >= 0:
    try:
        exec('元素圣灵技能列表.append(元素圣灵技能'+str(i)+'())')
        i += 1
    except:
        i = -1

元素圣灵技能序号 = dict()
for i in range(len(元素圣灵技能列表)):
    元素圣灵技能序号[元素圣灵技能列表[i].名称] = i

元素圣灵一觉序号 = 0
元素圣灵二觉序号 = 0
元素圣灵三觉序号 = 0
for i in 元素圣灵技能列表:
    if i.所在等级 == 50:
        元素圣灵一觉序号 = 元素圣灵技能序号[i.名称]
    if i.所在等级 == 85:
        元素圣灵二觉序号 = 元素圣灵技能序号[i.名称]
    if i.所在等级 == 100:
        元素圣灵三觉序号 = 元素圣灵技能序号[i.名称]

元素圣灵护石选项 = ['无']
for i in 元素圣灵技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        元素圣灵护石选项.append(i.名称)

元素圣灵符文选项 = ['无']
for i in 元素圣灵技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        元素圣灵符文选项.append(i.名称)

class 元素圣灵角色属性(角色属性):

    职业名称 = '元素圣灵'

    武器选项 = ['魔杖','法杖']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.85
   
    #基础属性(含唤醒)
    基础力量 = 832.0
    基础智力 = 939.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
  
    def __init__(self):
        self.技能栏= copy.deepcopy(元素圣灵技能列表)
        self.技能序号= copy.deepcopy(元素圣灵技能序号)
    def 属性精通加成倍率(self):
        for i in self.技能栏:
            if i.名称 == '圣灵符文':
               for j in i.关联技能:
                      return ( (self.技能栏[self.技能序号[j]].加成倍率(self.武器类型)-1.0)*i.加成倍率(self.武器类型)+1.0)
    def 魔法秀加成(self):
        for i in self.技能栏:
            if i.名称 == '圣灵符文':
               for j in i.冷却关联技能:
                      return (1.0-(1.0-self.技能栏[self.技能序号[j]].CD缩减倍率(self.武器类型))*(1+i.CD缩减倍率(self.武器类型)))
                      
    def CD倍率计算(self):
        for i in self.技能栏:
            if i.冷却关联技能 !=['无']:
                if i.冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD倍率 *= i.CD缩减倍率(self.武器类型)
                if i.名称 =='魔法秀':
                      for l in i.冷却关联技能:
                        self.技能栏[self.技能序号[l]].CD倍率 *= self.魔法秀加成()
                elif i.名称 !='圣灵符文':
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD倍率 *= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 !=['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD倍率 *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD倍率2 *= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 !=['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD倍率 *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD倍率 *= i.CD缩减倍率3(self.武器类型)       
                        
    def 被动倍率计算(self):
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                   if i.名称 !='属性精通':
                      for j in self.技能栏:
                          if j.是否有伤害 == 1:
                             j.被动倍率 *= i.加成倍率(self.武器类型)
                   if i.名称 == '属性精通':
                      for l in self.技能栏:
                          if l.是否有伤害 == 1:
                             l.被动倍率 *= self.属性精通加成倍率()
                elif i.名称 != '圣灵符文':
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)     
            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else :
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)
            # Will添加
            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else :
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)         
    

class 元素圣灵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 元素圣灵角色属性()
        self.角色属性A = 元素圣灵角色属性()
        self.角色属性B = 元素圣灵角色属性()
        self.一觉序号 = 元素圣灵一觉序号
        self.二觉序号 = 元素圣灵二觉序号
        self.三觉序号 = 元素圣灵三觉序号
        self.护石选项 = copy.deepcopy(元素圣灵护石选项)
        self.符文选项 = copy.deepcopy(元素圣灵符文选项)
 
