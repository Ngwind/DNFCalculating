from base import *

class 毒神绝技能0(主动技能):
    名称 = '抛沙'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 398.8
    成长 = 54.8
    CD = 5.5
    TP成长 = 0.08
    TP上限 = 7

class 毒神绝技能1(主动技能):
    名称 = '擒月炎'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2137.6
    成长 = 230.4
    CD = 5.5
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能2(主动技能):
    名称 = '毒影针'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2034.0
    成长 = 240.0
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7

class 毒神绝技能3(主动技能):
    名称 = '双重投掷'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    关联技能 = ['抛沙']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.60 + 0.04* self.等级, 5)

class 毒神绝技能4(被动技能):
    名称 = '爪精通'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.21 + 0.01* self.等级, 5)

class 毒神绝技能5(主动技能):
    名称 = '砖袭'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2156.0
    成长 = 235.0
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 7


class 毒神绝技能6(主动技能):
    名称 = '挑衅'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01* self.等级, 5)


class 毒神绝技能7(主动技能):
    名称 = '伏虎霸王拳'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 455.5
    成长 = 51.5
    攻击次数 = 7
    基础2 = 902.7
    成长2 = 102.1
    攻击次数2 = 1
    CD = 15.0
    TP上限 = 7

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            if self.TP等级 == 0:
                return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (self.基础3 + self.成长3 * self.等级)) * self.倍率)
            else:
                return int((self.基础 + self.成长 * self.等级)  * (7.67 + self.TP等级)  * self.倍率 * 2)
                
class 毒神绝技能8(主动技能):
    名称 = '裂地飞沙'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7290.5
    成长 = 823.0
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.27
        self.CD *= 1.00

class 毒神绝技能9(主动技能):
    名称 = '毒雷引爆'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9767.3
    成长 = 1146.3
    CD = 24.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.07
        self.CD *= 0.90

class 毒神绝技能10(被动技能):
    名称 = '猛毒之血'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.015 * self.等级, 5)

class 毒神绝技能11(主动技能):
    名称 = '死亡毒雾'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 25321.6
    成长 = 7641.2
    CD = 145

class 毒神绝技能12(主动技能):
    名称 = '猛毒擒月炎'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 12315.1
    成长 = 1387.7
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.173
        self.CD *= 0.80


class 毒神绝技能13(主动技能):
    名称 = '爆碎砖袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 15667.0
    成长 = 1786.0
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1
    def 装备护石(self):
        self.倍率 *= 1.119
        self.CD *= 1.00

class 毒神绝技能14(被动技能):
    名称 = '猛毒之伤'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.16 + 0.02 * self.等级, 5)

class 毒神绝技能15(主动技能):
    名称 = '连环毒爆弹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 40371.4
    成长 = 4558.1
    CD = 40.0

class 毒神绝技能16(主动技能):
    名称 = '毒龙轰天雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 39593.1
    成长 = 4468.5
    CD = 45.0

class 毒神绝技能17(主动技能):
    名称 = '万毒噬心诀'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 47654.8
    成长 = 14387.1
    CD = 180.0
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

class 毒神绝技能18(主动技能):
    名称 = '万毒噬心诀x4'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 7179
    成长 = 1258
    CD = 1.0

class 毒神绝技能19(主动技能):
    名称 = '万毒噬心诀x5'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 10410
    成长 = 1617.5
    CD = 1.5


class 毒神绝技能20(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 毒神绝技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 毒神绝技能22(被动技能):
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

毒神绝技能列表 = []
i = 0
while i >= 0:
    try:
        exec('毒神绝技能列表.append(毒神绝技能'+str(i)+'())')
        i += 1
    except:
        i = -1

毒神绝技能序号 = dict()
for i in range(len(毒神绝技能列表)):
    毒神绝技能序号[毒神绝技能列表[i].名称] = i

毒神绝一觉序号 = 0
毒神绝二觉序号 = 0
毒神绝三觉序号 = 0
for i in 毒神绝技能列表:
    if i.所在等级 == 50:
        毒神绝一觉序号 = 毒神绝技能序号[i.名称]
    if i.所在等级 == 85:
        毒神绝二觉序号 = 毒神绝技能序号[i.名称]
    if i.所在等级 == 100:
        毒神绝三觉序号 = 毒神绝技能序号[i.名称]

毒神绝护石选项 = ['无']
for i in 毒神绝技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        毒神绝护石选项.append(i.名称)

毒神绝符文选项 = ['无']
for i in 毒神绝技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        毒神绝符文选项.append(i.名称)

class 毒神绝角色属性(角色属性):

    职业名称 = '毒神绝'

    武器选项 = ['爪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比']
    
    #默认
    伤害类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量','智力']

    主BUFF = 9.50
   
    #基础属性(含唤醒)
    基础力量 = 931.0
    基础智力 = 894.0
    
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
        self.技能栏= copy.deepcopy(毒神绝技能列表)
        self.技能序号= copy.deepcopy(毒神绝技能序号)

    def 站街力量(self):
        return int(max(self.力量,self.智力))

    def 站街智力(self):
        return self.站街力量()

    def 面板力量(self):
        if self.系统奶 == False:
            return max(int(int((self.力量 + self.进图力量)) * (1 + self.百分比力智)),int(int((self.智力 + self.进图智力)) * (1 + self.百分比力智)))
        else:
            return max(int(int((self.力量 + int((self.力量 - self.基础力量) * 1.35 + 7664) +self.进图力量)) * (1 + self.百分比力智)),int(int((self.智力 + int((self.智力 - self.基础智力) * 1.35 + 7664) +self.进图智力)) * (1 + self.百分比力智)))

    def 面板智力(self):
        return self.面板力量()

    def 装备基础(self):
        self.力量 += 防具力量[self.防具类型]
        self.智力 += 防具智力[self.防具类型]
        if 装备列表[装备序号[self.装备栏[0]]].品质 == '神话':
            self.力量 += 神话上衣额外力量[self.防具类型]
            self.智力 += 神话上衣额外智力[self.防具类型]

        for i in [0,1,2,3,4]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i],部位列表[i])
            else:
                x = 精通计算(100,装备列表[装备序号[self.装备栏[i]]].品质,0,部位列表[i])
            if '力量' in self.防具精通属性:
                self.力量 += x
            if '智力' in self.防具精通属性:
                self.智力 += x
  

        for i in [9,10]:
            if 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 左右计算(100,'史诗',self.强化等级[i])
                self.力量 += x
                self.智力 += x

        for i in range(0,12):
            if self.是否增幅[i] and 装备列表[装备序号[self.装备栏[i]]].所属套装 != '智慧产物':
                x = 增幅计算(100,装备列表[装备序号[self.装备栏[i]]].品质,self.强化等级[i])
                self.力量 += x
                self.智力 += x

        if 装备列表[装备序号[self.装备栏[11]]].所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'物理')
            self.魔法攻击力 += 武器计算(100,'史诗',self.强化等级[11],self.武器类型,'魔法')
            self.独立攻击力 += 锻造计算(100,'史诗',self.武器锻造等级)
        
        if 装备列表[装备序号[self.装备栏[8]]].所属套装 != '智慧产物':
            x = 耳环计算(100,装备列表[装备序号[self.装备栏[8]]].品质,self.强化等级[8])
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        for i in [5,6,7,8,9,10,11]:
            self.力量 += 装备列表[装备序号[self.装备栏[i]]].力量
            self.智力 += 装备列表[装备序号[self.装备栏[i]]].智力
            self.物理攻击力 += 装备列表[装备序号[self.装备栏[i]]].物理攻击力
            self.魔法攻击力 += 装备列表[装备序号[self.装备栏[i]]].魔法攻击力
            self.独立攻击力 += 装备列表[装备序号[self.装备栏[i]]].独立攻击力

    def 伤害计算(self, x = 0):
        self.装备基础()

        for i in self.装备栏:
            装备列表[装备序号[i]].城镇属性(self)
            装备列表[装备序号[i]].进图属性(self)

        for i in self.套装栏:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)

        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        基准倍率 = 1.5 * (1 - 443215 / (443215 + 20000)) * (1 + self.主BUFF/10)

        面板 = (self.面板智力()/250+1) * (self.魔法攻击力 + self.进图魔法攻击力) * (1 + self.百分比三攻)
 
        属性倍率=1.05+0.0045*max(self.火属性强化,self.冰属性强化,self.光属性强化,self.暗属性强化)
        增伤倍率=1+self.伤害增加
        增伤倍率*=1+self.暴击伤害
        增伤倍率*=1+self.最终伤害
        增伤倍率*=self.技能攻击力
        增伤倍率*=1+self.持续伤害*(1-0.1*self.持续伤害计算比例)
        增伤倍率*=1+self.附加伤害+self.属性附加*属性倍率
        伤害指数=面板*属性倍率*增伤倍率*基准倍率/100
        
        self.被动倍率计算()

        技能释放次数=[]
        技能单次伤害=[]
        技能总伤害=[]
    
        #技能单次伤害计算
        for i in self.技能栏:
            if i.是否主动==1:
                技能单次伤害.append(i.等效百分比(self.武器类型)*伤害指数*i.被动倍率)
            else:
                技能单次伤害.append(0)
      
        #技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害==1:
                if self.次数输入[self.技能序号[i.名称]] =='/CD':
                    技能释放次数.append(int(self.时间输入/i.等效CD(self.武器类型) + 1 +i.基础释放次数))
                else:
                    if self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]])+i.基础释放次数)
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)
    
        #单技能伤害合计
    
        for i in self.技能栏:
            if i.是否主动==1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]]*技能释放次数[self.技能序号[i.名称]]*(1+self.白兔子技能*0.20+self.年宠技能*0.10*self.宠物次数[self.技能序号[i.名称]]/技能释放次数[self.技能序号[i.名称]]+self.斗神之吼秘药*0.12))
            else:
                技能总伤害.append(0)
    
        总伤害=0
        for i in self.技能栏:
            总伤害+=技能总伤害[self.技能序号[i.名称]]
        
        if x==0:
            return 总伤害
    
        if x==1:
            详细数据=[]
            for i in range(0,len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i]!=0:
                    详细数据.append(技能总伤害[i]/技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害!=0:
                    详细数据.append(技能总伤害[i]/总伤害*100)
                else:
                    详细数据.append(0)
            return 详细数据

class 毒神绝(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 毒神绝角色属性()
        self.角色属性A = 毒神绝角色属性()
        self.角色属性B = 毒神绝角色属性()
        self.一觉序号 = 毒神绝一觉序号
        self.二觉序号 = 毒神绝二觉序号
        self.三觉序号 = 毒神绝三觉序号
        self.护石选项 = copy.deepcopy(毒神绝护石选项)
        self.符文选项 = copy.deepcopy(毒神绝符文选项)
