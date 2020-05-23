
##############################

增幅系数 = [0, 1, 2, 3, 4, 6, 8, 10, 12, 13, 17, 33, 50, 67, 108, 150, 192, 267, 342, 417, 500]
增幅成长系数 = {'稀有':1.0, '神器':1.3, '勇者':1.1, '传说':1.4, '史诗':1.5, '神话':1.6}
增幅品级加分 = {'稀有':45, '神器':45, '勇者':45, '传说':46, '史诗':46, '神话':46}
增幅品级底数 = {'稀有':5, '神器':6, '勇者':5, '传说':6, '史诗':7, '神话':8}

def 增幅计算(装备等级,品质,强化等级):
    if 装备等级 == 55:
        装备等级 += 2
    return int((装备等级 + 增幅品级加分[品质] - 0.000000000001) * 增幅成长系数[品质] * 增幅系数[强化等级] / 100 ) + 增幅品级底数[品质]

##############################

耳环强化系数 = [0, 18, 27, 36, 45, 54, 68, 80, 92, 104, 135, 210, 315, 420, 631, 877, 1123, 1542, 1962, 2383, 2838]
耳环成长系数 = {'普通':0.4, '高级':0.7, '稀有':1.0, '神器':1.25, '传说':1.35, '史诗':1.45, '神话':1.55}
耳环品级加分 = {'普通':24, '高级':30, '稀有':26, '神器':28, '传说':29, '史诗':30, '神话':31}

def 耳环计算(装备等级,品质,强化等级):
    return int((装备等级 + 耳环品级加分[品质]) / 520 * 耳环成长系数[品质] * 耳环强化系数[强化等级])

##############################

左右强化系数 = [0, 8, 12, 16, 20, 24, 28, 33, 38, 43, 48, 90, 135, 180, 270, 375, 480, 660, 840, 1020, 1215]
左右成长系数 = {'普通':0.4, '高级':0.7, '稀有':1.0, '神器':1.25, '勇者':1.1, '传说':1.35, '史诗':1.45, '神话':1.55}
左右品级加分 = {'普通':24, '高级':24, '稀有':26, '神器':28, '勇者':27, '传说':29, '史诗':30, '神话':31}

def 左右计算(装备等级,品质,强化等级):
    return int((装备等级 + 左右品级加分[品质]) / 320 * 左右成长系数[品质] * 左右强化系数[强化等级])

##############################

武器强化系数 = [0, 20, 26, 36, 47, 58, 69, 82, 110, 146, 187, 269, 367, 430, 492, 554, 617, 680, 743, 806, 869]
武器成长系数 = {'普通':0.4, '高级':0.7, '稀有':1.0, '神器':1.25, '勇者':1.1, '传说':1.35, '史诗':1.45, '神话':1.55}
武器品级加分 = {'普通':8, '高级':8, '稀有':10, '神器':12, '勇者':11, '传说':13, '史诗':14, '神话':15}
武器类型列表 = ['左轮', '手炮', '步枪', '手弩', '自动手枪', '短剑', '光剑', '巨剑', '太刀', '钝器', '法杖', '魔杖', '棍棒', '矛', '扫把', 
        '手套', '臂铠', '爪', '拳套', '东方棍', '十字架', '念珠', '图腾', '镰刀', '战斧', '匕首', '双剑', '权杖', '苦无', '战戟', '长枪', '光枪',
        '暗矛', '长刀', '小太刀', '重剑', '源力剑']
物理系数 = [0.9783, 0.9954, 0.9900, 0.9684, 0.9576, 0.9855, 0.9837, 1.0080, 0.9855, 0.9990, 0.9855, 0.9810, 0.9972, 1.0080, 0.9900, 0.9855, 1.0080,0.9900, 
        0.9945, 0.9855, 0.9900, 0.9810, 0.9945, 0.9945, 1.0080, 0.9811, 0.9918, 0.9729, 0.9810, 1.0080, 0.9945, 0.9855, 0.9855, 0.9972, 0.9900, 1.0080, 0.9855]
魔法系数 = [0.9693, 0.9576, 0.9765, 0.9765, 0.9846, 1.0035, 0.9810, 0.9810, 0.9945, 0.9855, 1.0080, 0.9990, 0.9810, 0.9765, 0.9990, 1.0035, 0.9810, 0.9900,
        0.9855, 0.9900, 0.9855, 1.0035, 0.9810, 0.9945, 0.9765, 0.9810, 0.9720, 1.0035, 0.9990, 0.9765, 0.9810, 1.0035, 0.9945, 0.9810, 0.9900, 0.9810, 1.0035]

def 武器计算(装备等级,品质,强化等级,武器类型,伤害类型):
    if 装备等级 <= 55 and 装备等级 >= 50:
        装备等级 += 2
    index = 武器类型列表.index(武器类型)
    if 伤害类型 == '物理':
        武器系数 = 物理系数[index]
    else:
        武器系数 = 魔法系数[index]
    return int((装备等级 + 武器品级加分[品质]) / 72 * 武器成长系数[品质] * 武器强化系数[强化等级] * 武器系数)

##############################

锻造强化系数 = [0, 2, 3, 4, 6, 8, 13, 18, 25]
锻造成长系数 = {'普通':0.4, '高级':0.7, '稀有':1.0, '神器':1.25, '勇者':1.1, '传说':1.35, '史诗':1.45, '神话':1.55}
锻造品级加分 = {'普通':8, '高级':8, '稀有':10, '神器':12, '勇者':10, '传说':13, '史诗':14, '神话':15}

def 锻造计算(装备等级,品质,锻造等级):
    return int(round((装备等级 + 锻造品级加分[品质]) / 8 * 锻造成长系数[品质] * 锻造强化系数[锻造等级], 0))

##############################

部位系数 = {'上衣':0.30, '头肩':0.20, '下装':0.25, '腰带':0.10, '鞋':0.15}
品级加分 = {'稀有':5, '神器':8, '勇者':11, '传说':14, '史诗':17, '神话':18}

def 精通计算(装备等级,品质,强化等级,部位):
    return round((20 + 2.5 * (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)

##############################

