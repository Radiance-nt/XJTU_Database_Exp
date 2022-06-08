import random
import time
import os

S_LEN = 1000
C_LEN = 500
SC_LEN = 2000

SNO_START = int(1033e3)

# yyyy, mm, dd, h, m ,s
date1 = (1999, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = time.mktime(date1)
date2 = (2002, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = time.mktime(date2)

first_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤", "许", "何",
              "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏",
              "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞", "任", "袁", "柳", "酆", "鲍", "史",
              "唐", "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕", "郝", "邬", "安", "常", "乐", "于", "时", "傅",
              "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹", "姚", "邵", "堪", "汪"]
last_name = ['玉', '明', '龙', '芳', '军', '玲', '', '立', '玲', '', '国', "地", "为", "子", "中", "", "", "", "国", "年", "着", "就",
             "那", "和", "要", "她", "出", "也", "", "", "", "自", "以", "会", "家", "可", "下", "事", "把", "还", "用", "第", "样", "道",
             "想", "作", "种", "开", "美", "总", "从", "无", "情", "己", "面", "最", "女", "但", "现", "前", "些", "所", "同", "日", "手",
             "又", "行", "意", "动", "方", "期", "它", "头", "经", "长", "儿", "回", "位", "分", "爱", "老", "因", "很", "给", "名", "法",
             "间", "斯", "知", "世", "什", "两", "次", "使", "身", "者", "被", "高", "已", "亲", "其", "进", "此", "话", "常", "与", "活",
             "正", "感", "见", "明", "问", "力", "理", "尔", "点", "文", "几", "定", "本", "公", "特", "做", "外", "孩", "相", "西", "果",
             "走", "将", "月", "十", "实", "向", "声", "车", "全", "信", "重", "三", "机", "工", "物", "气", "每", "并", "别", "真", "打",
             "太", "新", "比", "才", "便", "夫", "再", "书", "部", "水", "像", "眼", "等", "体", "却", "加", "电", "主", "界", "门", "利",
             "海", "受", "听", "表", "德", "少", "克", "代", "员", "许", "稜", "先", "口", "由", "死", "安", "写", "性", "马", "光", "白",
             "或", "住", "难", "望", "教", "命", "花", "结", "乐", "色", "更", "拉", "东", "神", "记", "处", "让", "母", "父", "应", "直",
             "字", "场", "平", "报", "友", "关", "放", "至", "张", "认", "接", "告", "入", "笑", "内", "英", "军", "候", "民", "岁", "往",
             "何", "度", "山"]
genders = ['女', '男']
dorms = ['东', '西']
sno = SNO_START

first_class = ['深度', '爱情', '经济', '电机', '电路', '睡眠', '操作', '数据库', '', '']
last_class = ['学习', '课程', '教学', '项目', '基础']
deps = ['CS', 'EE', 'SC', 'HH', 'AI', 'HW']

snos = []
cnos = []

log = open(os.path.join('.', 'expand'), 'w')


def gen_name():
    while True:
        full_name = random.choice(first_name) + random.choice(last_name) + random.choice(last_name)
        if len(full_name) > 1:
            return full_name


def record(msg):
    print(msg, end='')
    log.write('%s' % msg)
    log.flush()


record('INSERT INTO S249 VALUES \n')
for i in range(S_LEN):
    count = random.randint(1, 3)
    sno = sno + count
    full_name = gen_name()
    random_time = random.uniform(time1, time2)  # uniform返回随机实数 time1 <= time < time2
    birthday = time.strftime("%Y-%m-%d", (time.localtime(random_time)))

    gender = random.choice(genders)
    height = random.uniform(1.4, 2.0)
    height = round(height, 2)
    dorm = '%s%d舍%d%d' % (random.choice(dorms), random.randint(1, 20),
                          random.randint(1, 20), random.randint(1, 22),)
    snos.append(sno)
    if i != S_LEN - 1:
        record("({}, '{}', '{}', '{}', {}, '{}'),\n".format(sno, full_name, gender, birthday, height, dorm))
    else:
        record("({}, '{}', '{}', '{}', {}, '{}');\n".format(sno, full_name, gender, birthday, height, dorm))
record('\n\n')


def cache(func):
    ca = {}
    while True:
        args = func()
        if not ca.get(args):
            ca[args] = True
            yield args


record('INSERT INTO C249 VALUES \n')
cno_gen = cache(lambda: ('%s-%d' % (random.choice(deps), random.randint(1, 100))))
for i in range(C_LEN):
    cno = next(cno_gen)

    class_name = random.choice(first_class) + random.choice(first_class) + random.choice(last_class)
    full_name = gen_name()

    ctime = random.randrange(20, 60, 4)

    gender = random.choice(genders)
    credit = random.randrange(1, 13) / 2
    credit = round(credit, 1)
    cnos.append(cno)
    if i != C_LEN - 1:
        record("('{}', '{}', {}, {}, '{}'),\n".format(cno, class_name, ctime, credit, full_name))
    else:
        record("('{}', '{}', {}, {}, '{}');\n".format(cno, class_name, ctime, credit, full_name))

record('\n\n')

record('INSERT INTO SC249 VALUES \n')
key_gen = cache(lambda: (random.choice(snos), random.choice(cnos)))
for i in range(SC_LEN):
    key = next(key_gen)
    grade = random.randrange(80, 200) / 2
    grade = round(grade, 1)
    if i != SC_LEN - 1:
        record("({}, '{}', {}),\n".format(key[0], key[1], grade))
    else:
        record("({}, '{}', {});\n".format(key[0], key[1], grade))
record('\n\n')

record('-- Finish')

log.flush()
log.close()

