data = '''
1.表达式求值
a=float(input())
b=float(input())
c=float(input())
x=(-b+(b*b-4*a*c)**0.5)/(2*a)
print(f'{x:.2f}')


2.三角函数计算
import math
a=eval(input())
b=eval(input())
x=(-b+math.sqrt(2*a*math.sin(math.pi/3)*math.cos(math.pi/3)))/(2*a)
print(f'{x:.2f}')


3.计算存款利息
p=int(input())    #本金
n=int(input())    #存款年限
r=float(input())   #年利率
total=p*(1+r)**n
interest=total-p    #利息
print(f'利息={interest:.2f}')


4.三角形周长及面积
import math        # 导入math库
a = eval(input())
b = eval(input())
c = eval(input())
s = (a + b + c) / 2.0
m = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# m=math.sqrt(s * (s - a) * (s - b) * (s - c))    # 第二种开根号方法
print(f'周长={a + b + c:.2f}')
print(f'面积={m:.2f}') 


5.换披萨
import math
m=int(input())  #输入大披萨直径m
n=int(input())   #输入小披萨直径n

mr=int(m*2.54)/2   #计算大披萨直径的厘米，取整，再计算半径
nr=int(n*2.54)/2   #计算小披萨直径的厘米，取整，再计算半径

num=(mr*mr)/(nr*nr)  #计算大小披萨面积比值
print(math.ceil(num))  #格式化输出向上取整


6.一元二次方程求根
a=float(input())
b=float(input())
c=float(input())
d=b**2-4*a*c 
if a==0 and  b==0:
        print('Data error!')
elif a == 0 and b != 0:
    print(f'{- c / b:.2f}')
elif d<0:
        print('该方程无实数解')
elif d==0:
        print(f'{-b/(2*a):.2f}')
else:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        if x1<x2:
            x1,x2=x2,x1
        print(f'{x1:.2f} {x2:.2f}')


7.今年多少天？
year=int(input())
if (year%400==0) or (year%4==0 and year%100!=0):
    print(366)
else:
    print(365)


8.判断三角形并计算面积
a=float(input())
b=float(input())
c=float(input())
if a+b>c and a+c>b and b+c>a:
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('YES')
    print(f'{s:.2f}')
else:
    print('NO')



9.判断是否直角三角形
a=eval(input())
b=eval(input())
c=eval(input())
duan=min(a,b,c)    #最短的边长
chang=max(a,b,c)   #最长的边长
zhong=sum([a,b,c])-duan-chang
if duan<=0 or duan+zhong<=chang:
    print('NO')
elif duan**2+zhong**2==chang**2:
    print('YES')
else:
    print('NO')



10.今天是第几天
y,m,d=map(int,input().split('/'))
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if (y%4==0 and y%100!=0) or (y%400==0):
     days[1]=29
countday=sum(days[:m-1])+d   #前面月份的天数加上当月天数
print(f'{y}年{m}月{d}日是{y}年第{countday}天')


11.身高测算
x=int(input())
y=int(input())
g=input()
if g=='男':
    h=(x+y)*1.08/2
    print(int(h))
elif g=='女':
    h=(x*0.923+y)/2
    print(int(h))
else:
    print('无对应公式')



12.个税计算器
s=float(input())
if s<0:
    print('error')
else:
    a=s-5000      #5000以下免征税
    if a<=0:
        t,n=0,0
    elif a<=3000:
        t,n=3,0
    elif a<=12000:
        t,n=10,210
    elif a<=25000:
        t,n=20,1410
    elif a<=35000:
        t,n=25,2660
    elif a<=55000:
        t,n=30,4410
    elif a<=80000:
        t,n=35,7160
    else:
        t,n=45,15160
    tax=abs(a*t/100-n)
    print(f'应缴税款{tax:.2f}元，实发工资{s-tax:.2f}元。')




13.判断闰年
year=int(input())
if year %400==0 or (year%4==0 and year%100!=0):
    print(True)
else:
    print(False)


14.分段函数A
x=int(input())
if x>-10 and x<0:
    y=2*x**3+4*x**2+3
elif x>=0 and x<6:
    y=x+14
elif x>=6 and x<10:
    y=6*x
else:
    y='ERROR'
print(y)



15.数列求和
n=int(input())
s=0
t=0
for i in range(1,n+1):
    t=t*10+i
    s=s+t
print(s)



16.百分制成绩转换五分制(循环)
while True:
    score = eval(input())
    if score < 0:
        print('end')
        break
    elif score > 100:
        print('data error!')
    elif score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('E')



17.正负交错数列前n项和
n = int(input())
s = 1                        # 首项不进入循环
f= -1                         # 符号，第二项是负值，
a, b = 1, 1          # 分母数字符合斐波拉契数列
for i in range(1, n):             # 从1到n-1遍历n-1次
	a,b = b,a+b  # 下一个数值是前面两个数的加和
	s = s + f * i / b             # 注意分子是 i
	f = -f                                   # 改变正负号
print(f'{s:.6f}')


18.求数列前n项的平方和
n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + i * i
print(sum)



19.计算整数各位数字之和
print(sum(map(int, list(input()))))



20.分类统计字符个数
import string
str = input()

letter = digit = other = 0
for s in str:
    if s in string.ascii_letters:
        letter = letter + 1
    elif s in string.digits:
        digit = digit + 1
    else:
        other = other + 1
print("letter = {}, digit = {}, other = {}".format(letter, digit, other))



21.用户登录C
error_num = 0
while error_num < 3:
    username = input()
    password = input()
    if (username == 'admin'or username == 'administrator')  and password == '123456':
    #注意or与and优先级，需要括号
        print("登录成功")
        break
    else:
        print("登录失败")
        error_num += 1


22.二分法求平方根B
import math

def sqrt_binary(num, accuracy):
	low, high = 0, num + 0.25             
	while True:                           
		x = (high + low) / 2              
		if abs(x * x - num) <= accuracy:  
			return x                     
		elif x * x - num < 0:             
			low = x                       
		else:                             
			high = x      

n, error = map(float, input().split(','))      
print('{:.8f}'.format(sqrt_binary(n, error)))  
print('{:.8f}'.format(math.sqrt(n)))           




23.编写函数输出自除数
def selfDivisor(num):
    if '0' in str(num):
        return False          
    for c in str(num):        
        if num % int(c) != 0: 
            return False      
    else:                      
        return True

n=int(input())
for num in range(1,n+1):      
    if selfDivisor(num):      
        print(num,end=' ')    



24.身份证号基本信息
id = input()              
year = id[6:10]           
month = id[10:12]         
date = id[12:14]          
if int(id[16]) % 2 == 0: 
    gender = '女'
else:                           
    gender = '男'
print('出生：{}年{}月{}日'.format(year,month,date))  
print('性别：{}'.format(gender))  



25.货币转换
money = input()
rate = float(input())    # 输入汇率
if money[-1] in '￥$'  and rate > 0:    # 当最后一位为'￥'时
    change,sign = (rate * float(money[0:-1]),'￥') if money[-1] == '$' else (float(money[0:-1]) / rate,'$') # 计算兑换金额
    print("{:.2f}{}".format(change,sign))
else:
    print("Data error!")



26.个人信息提取（控制结构）
info = input().split()
print(f'姓名：{info[1]}')
print(f'班级：{info[2]}')
for i in range(len(info[-1])):
    year = info[-1][i:i + 4]
    if year.isdigit():
        print(f'出生：{year}年')



27.统计单词的数量
s = input()
ls = s.split()
print(len(ls))



28.各位数字之和为5的数
n = int(input())
for i in range(1,n+1):
    if sum(map(int,list(str(i))))==5:
        print(i,end = ' ')


29.输出单词
s = input().split()
for i in s :
    print(i)


30.完美立方数
N =  int(input())
ls = []
for i in range(1,N + 1): 
    ls.append(i * i * i) 
for a in range(2,N + 1):  #a从2-N
    for b in range(2,a):  #b,c,d都不会大于a，这样可减少计算量
        for c in range(b,a):  #c大于等于b
            for d in range(c,a):  
                if ls[a-1] == ls[b-1] + ls[c-1] + ls[d-1]:
     #if a * a * a == b * b * b + c * c * c + d * d * d :
                    print("Cube = {},Triple = ({},{},{})".format(a,b,c,d))



31.绩点计算
score = {'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.5, 'D': 1.3, 'D-': 1.0,
         'F': 0.0}
credit_ls, gpa_ls = [],[]
while True:
    s = input()
    if s == '-1':
        break
    elif s in score.keys():
        credit = float(input())
        credit_ls.append(credit)
        gpa_ls.append(score.get(s) * credit)
    else:
        print('data error')
gpa_ave = sum(gpa_ls) / sum(credit_ls)
print(f'{gpa_ave:.2f}')



32.查询省会
capitals = {'湖南':'长沙','湖北':'武汉','广东':'广州','广西':'南宁','河北':'石家庄','河南':'郑州','山东':'济南','山西':'太原','江苏':'南京','浙江':'杭州','江西':'南昌','黑龙江':'哈尔滨','新疆':'乌鲁木齐','云南':'昆明','贵州':'贵阳','福建':'福州','吉林':'长春','安徽':'合肥','四川':'成都','西藏':'拉萨','宁夏':'银川','辽宁':'沈阳','青海':'西宁','海南':'海口','甘肃':'兰州','陕西':'西安','内蒙古':'呼和浩特','台湾':'台北','北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','香港':'香港','澳门':'澳门'}
while True:
    province = input()
    if province == '':
        break
    else:
        print(capitals.get(province,'输入错误'))



33.英汉词典
import string


def read_to_dic(filename):
    my_dic = {}
    with open(filename, 'r', encoding='utf-8') as data:
        for x in data:
            x = x.strip().split(maxsplit=1)
            my_dic.update({x[0]: x[1]})
    return my_dic


def sentence_to_lst(sentence):
    sentence = sentence.replace("n't", ' not')
    sentence = sentence.replace("'s", ' is')
    for x in string.punctuation:
        sentence = sentence.replace(x, ' ')
    sentence_lst = sentence.split()
    return sentence_lst


def query_words(sentence_lst, my_dic):
    for word in sentence_lst:
        word = word.lower()
        print(word, my_dic.get(word, '自己猜'))


if __name__ == '__main__':
    my_str = input()
    file = 'dicts.txt'
    dic = read_to_dic(file)
    lst = sentence_to_lst(my_str)
    query_words(lst, dic)



34.统计字母数量
s = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
with open('The Old Man and the Sea.txt','r',encoding='utf-8') as data:
	txt = data.readlines()
if n > len(txt):
	n = len(txt)
mystr = ' '.join(txt[:n])
# print(mystr)
ls = [[x,mystr.lower().count(x)] for x in s ]
ls.sort(key = lambda x:(-x[1],x[0]))
#print(ls)
for i in ls:
	print('{} 的数量是 {:>3} 个'.format(i[0],i[1]))



35.统计文章字符数
def readFile(filename,num):
    with open(filename,'r',encoding='utf-8') as file:  
        content = file.readlines()                    
    txt = ''.join(content[:num])      
    # 列表的前num行连接为字符串
    return  len(txt),len(set(txt))                     
    # 以元组形式返回字符串长度和集合长度

if __name__ == '__main__':
    num= int(input())                  # 输入读取文件行数
    name = 'The Great Learning.txt'    # 文件名
    content = readFile(name,num)       # 传入文件和行数
    print(*content)                    # 将返回的元组解包输出



36.查询高校信息
with open('university.csv','r',encoding='utf-8') as Uname:
    ls = Uname.readlines()
#按行读文件为字符串列表
name = input()
for line in ls:
    if name in line:
        print(ls[0].strip())
        print(line.strip())



37.查询高校名
def read_csv_to_lst(filename):
	"""接收CSV文件名为参数，读取文件内容到二维列表，每行数据根据逗号切分为子列表，返回二维列表。"""
	with open(filename, 'r', encoding='utf-8') as f:
		university_lst = [line.strip().split(',') for line in f]
	return university_lst


def query_name(word, university_lst):
	"""接收一个字符串和列表名为参数，从列表中查询学校名包含参数字符串的学校名，以列表形式返回。"""
	uni_name_lst = []
	for university in university_lst:
		if word in university[1]:
			uni_name_lst.append(university[1])
	return uni_name_lst


if __name__ == '__main__':
	file = 'university.csv'
	uni_lst = read_csv_to_lst(file)    # 获得高校信息二维列表
	key_word = input()                 # 输入查询关键字
	ls = query_name(key_word, uni_lst) 
	# 查询包含关键的校名，得到列表
	print(*ls,sep='\n')                
	# 解包输出列表中的元素，用换行符做分隔 符，实现换行输出的效果





38.通讯录（文件读取）
def read():
    inFile = open("info.csv", 'r',encoding='GBK')
    for line in inFile:
         tr = line.strip().split(',')
         dic[tr[0]]=tr[1:]

def show():
    for name,value in dic.items():
        print(name,value[0],value[1])

dic={}
read()
c=input()
if c=='A':
    show()
elif c=='D':
    print(dic)
else:
    print("ERROR")




39.利用数据文件统计成绩
data = open('成绩单.csv','r', encoding='utf-8')
score = [line.strip().split(',') for line in data]
n = int(input())
score.sort(key = lambda x:int(x[9]))
if n > len(score):
    n = len(score)
print('最低分{}分,最高分{}分'.format(score[0][9],score[-1][9]))
print(score[:n])
print(score[-n:])
print([round(sum(int(x[i]) for x in score) / len(score),2) for i in range(3,len(score[0])-1)])  #每道题的平均分

data.close()



40.研究生录取数据分析A
with open('admit2.csv','r',encoding='utf-8') as f:
    ls=[x.strip().split(',') for x in f]
ls=[x for x in ls[1:]]    #去掉表头的第一行的列表

p9=[x for x in ls if eval(x[-1])>=0.9]
p8=[x for x in ls if eval(x[-1])>=0.8]
p7=[x for x in ls if eval(x[-1])<=0.7]
n=input()

if n=='1':
    w=[x for x in p8 if eval(x[1])>=4]
    print(f'Top University in >=80%:{len(w)/len(p8)*100:.2f}%')
elif n=='2':
    print(f'TOEFL Average Score:{sum(eval(x[3]) for x in p8)/len(p8):.2f}')
    print(f'TOEFL Max Score:{max(eval(x[3]) for x in p8):.2f}')
    print(f'TOEFL Min Score:{min(eval(x[3]) for x in p8):.2f}')
elif n=='3':
    print(f'CGPA Average Score:{sum(eval(x[4]) for x in p8)/len(p8):.3f}')
    print(f'CGPA Max Score:{max(eval(x[4]) for x in p8):.3f}')
    print(f'CGPA Min Score:{min(eval(x[4]) for x in p8):.3f}')
elif n=='Research':
    l9=[x for x in p9 if x[-4]=='1']
    l7 = [x for x in p7 if x[-4] == '1']
    print(f'Research in >=90%:{len(l9)/len(p9)*100:.2f}%')
    print(f'Research in <=70%:{len(l7)/len(p7)*100:.2f}%')
else:
    print('ERROR')



41.图书数据分析（A）
def number(): #输出图书数据的总数量
    print(len(ls))

def rank(): #输入一个书籍编号，分别输出编号对应的书籍信息（编号,书名,出版社,现价,原价,评论数,推荐指数）
    num=input()
    for i in ls:
        if num==i[0]:
           for j in i:
               print(j)
           break

def namesort1():   #输出名字最长的n本书，长度相同按现价从高到低排序
    ls.sort(key=lambda x:len(x[1]),reverse=True)
    n=int(input())
    for i in ls[:n]:
        print(i[1])

def comment1():#输出评论数量最多的10本书的书名和评论数，按评论数量降序排序
    ls.sort(key = lambda x: int(x[5][:-3]), reverse = True)
    for i in ls[:10]:
        print(i[1],i[5])

with open('CBOOK.csv','r',encoding='GBK')as f:
    ls=[x.strip().split(',') for x in f]
ls=[x for x in ls[1:]]   #去掉列表第一行
c=input()
if c=='record':
    number()
elif c=='rank':
    rank()
elif c=='maxname':
    namesort1()
elif c=='maxcomment':
    comment1()
else:
    print('无数据')



42.大学排行榜分析
def read_file(file,m):
    """读文件中的学校名到列表中，返回前m个记录的学校集合"""
    with open(file, "r", encoding="utf-8") as data:
        ls = [line.strip().split()[1] for line in data]
    return set(ls[:m])


def either_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在这两个排行榜中均在前m个记录的学校名，按照学校名称排序，
    返回排序后的列表
    """
    either_set = alumni & soft
    return sorted(list(either_set))




def all_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在两个榜单中名列前m的所有学校名，按照学校名称排序，
    返回排序后的列表
    """
    all_in_set = alumni | soft
    return sorted(list(all_in_set))


def only_alumni(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni榜单中名列前m但soft榜单中未进前m的学校名，
    按照学校名称排序，返回排序后的列表
    """
    only_alumni_set = alumni - soft
    return sorted(list(only_alumni_set))


def only_once(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni和soft榜单中名列前m，但不同时出现在两个榜单的学校名，
    按照学校名称排序，返回排序后的列表
    """
    only_once_set = alumni ^ soft
    return sorted(list(only_once_set))



def judge(n):
    if n in '1234':
        m=int(input())
        alumni_set = read_file('./alumni.txt',m)
        soft_set = read_file('./soft.txt',m)
        if n=='1':
            either_rank = either_in_top(alumni_set, soft_set)
            print(f'两榜单中均名列前{m}的学校：')
            print(either_rank)
        elif n=='2':
            all_rank = all_in_top(alumni_set, soft_set)
            print(f'两榜单名列前{m}的所有学校：')
            print(all_rank)
        elif n=='3':
            only_in_alumni_rank = only_alumni(alumni_set, soft_set)
            print(f'alumni中名列前{m}，soft中未进前{m}的学校：')
            print(only_in_alumni_rank)
        elif n=='4':
            alumni_soft_rank = only_once(alumni_set, soft_set)
            print(f'不同时出现在两个榜单前{m}的学校：')
            print(alumni_soft_rank)
    else:
        print('Wrong Option')
        

if __name__ == '__main__':
    num = input()
    judge(num)
    



43.罗马数字转换
def RInt(s):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,
   'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    t=0
    while len(s)>0:
        if s[0:2] in d:
            t+=d[s[0:2]]
            s=s[2:]
        else:
            t+=d[s[0]]
            s=s[1:]
    return t

s=input()
print(RInt(s))




44.商品房数据统计
with open('wuhan2021s1.csv','r',encoding='GBK') as f:
    ls=[x.strip().split(',') for x in f]
ls=ls[1:]
n=input()
if n=='规模降序':
    for i in sorted(ls,key=lambda x:eval(x[-1]),reverse=True):
        print(' '.join(i))
elif n=='规模升序':
    for i in sorted(ls,key=lambda x:eval(x[-1])):
        print(' '.join(i))
elif n in set([i[1] for i in ls]):   #如果是某个区名
    for i in ls:
        if i[1]==n:
            print(' '.join(i))
    s=sum([eval(i[-1]) for i in ls if i[1]==n])
    print(f'{s:.2f}平方米')
elif n=='总规模':
    s=sum([eval(i[-1]) for i in ls])
    print(f'{s:.2f}平方米')
else:
    print('错误输入')





45.统计文本中单词数
filename = input() 
with open(filename, 'r') as file:  
        text = file.read()  # 文件内容读成一个字符串
pl='（!"#$%&()*+,./:;<=>?@[\]^_{|}~\n）'
for ch in pl:  
    text = text.replace(ch, ' ')  
ls=text.split()              # 根据空格将字符串切分为列表返回
print(len(ls))             # 输出列表长度，即单词数量



46.2019慈善排行
with open('2019Charity.csv','r',encoding='UTF-8') as f:
    ls=[x.strip().split(',') for x in f]
title = ls[0]
ls=ls[1:]

n=input()
if n.lower()=='total':
    print('Total:{}万元'.format(sum([eval(i[-1]) for i in ls])))
elif n.isdigit() and 1<=eval(n)<=100:
    for i in ls:
        if i[0]==n:
              print(' '.join(i))
elif n in [i[3] for i in ls]:
    for i in ls:
        if i[3]==n:
            print(' '.join(i[:4]))
else:
    print('No Record')




47.酒店评价数据分析
import jieba

def total():
    print('总评论:',len(ls))
    lp=[i[0] for i in ls] #统计好评和差评的0/1列表
    print('好评:',lp.count('1'))
    print('差评:',lp.count('0'))

def goodcomment():
    lgood=[i[1] for i in ls if i[0]=='1']
    good=''.join(lgood) #好评字符串
    lq = jieba.lcut(good)
    d={}
    for i in lq:
        if len(i)>1 and i.isdigit()==False and i not in ex:
            d[i]=d.get(i,0)+1
    p=sorted(d.items(),key = lambda x:x[1],reverse=True)[:15]
    for i in p:
        print(i[0]+':',i[1])
    
def badcomment():
    lbad=[i[1] for i in ls if i[0]=='0']
    bad=''.join(lbad)  #差评字符串
    lt = jieba.lcut(bad)
    d={}
    for i in lt:
        if len(i)>1 and i.isdigit()==False and i not in ex:
            d[i]=d.get(i,0)+1
    p=sorted(d.items(),key = lambda x:x[1],reverse=True)[:15]
    for i in p:
        print(i[0]+':',i[1])
        
def ave():
    pj=sum([len(i[1]) for i in ls])/len(ls)
    print(f'{pj:.0f}')

with open('comment.csv', 'r', encoding='GBK') as f:
    ls=[i.strip().split(',',maxsplit=1) for i in f.readlines()[1:]]
    
ex=['不错','比较','可以','感觉','没有',
    '我们','就是','还是','非常','但是',
    '不过','有点','一个','一般','下次',
    '携程','不是','晚上','而且','他们',
    '什么','不好','时候','知道','这样',
    '这个','还有','总体','位置','客人',
    '因为','如果','这里','很多','选择',
    '居然','不能','实在','不会','这家',
    '结果','发现','竟然','已经','自己',
    '问题','不要','地方','只有','第二天',
    '酒店','房间','虽然']
n=input()
if n=='总评':
    total()
elif n=='平均':
    ave()
elif n=='好评':
    goodcomment()
elif n=='差评':
    badcomment()
else:
    print('无数据')




48.体育收入排行2012-2019
def fopen():
    l=[]
    with open('2012-19sport.csv','r',encoding='UTF-8') as f:
        for i in f.readlines():
            l.append(i.strip().split(','))

    for i in l:
        i[0]=i[0].strip('#')
    return l
#sportclass()获得排行中所有的运动类别,返回排序列表
def sportclass(lt):
    s=set()
    for i in lt[1:]:
        s.add(i[-2])
    return sorted(s)

lt=fopen()
c=input()  #输入选项
if c.isdigit() and 2012<=eval(c)<=2019: #如果输入的是年份，继续输入需要显示的n名运动员
    n=int(input())
    if n>100:    #如果超过100，输出所有当年信息
        n=100
    ln=[]
    for i in lt[1:]:
        if i[-1]==c:
            ln.append(i)
    for i in ln[:n]:
        print(' | '.join(i))
elif c.lower()=='sport':  #如果输入sport, 输出所有运动选项并编号，并统计n年的该运动板块总收入
    d={}   #字典存放键值对，选项：运动类别
    n = input()  # 年份
    ln=[]
    for i in lt[1:]:
        if i[-1] == n:
            ln.append(i)
    lsc=sportclass(ln)
    for i,j in enumerate(lsc):
        print('{}: {}'.format(i+1,j))
        d[i+1]=j
    k=input()   #输入运动选项
    s=0
    for i in lt[1:]:
        if i[-1]==n and i[-2]==d[int(k)]:
            print(' | '.join(i))
            s+=eval(i[2][1:-1])
    print('TOTAL: ${:.2f} M'.format(s))
else:
    print('Wrong Input')




49.查找数字
ls=input().split()
[print(x) for x in set(ls) if ls.count(x)%2!=0]




50.共有前缀（列表/集合）
ls=input().split()
lt=sorted(ls,key=lambda x:len(x))
k=len(lt[0])   #最小字符串长度
for i in range(k,0,-1):  
    r=set()
    for j in ls:
        r.add(j[0:i])
    if len(r)==1:
        print(r.pop())
        break
else:
    print('NOT FOUND')




51.查找特征数（集合/列表）
ls=list(map(int,input().split()))
s=sorted(set(ls),reverse=True)
for x in s:
    if x==ls.count(x):
        print(x)
        break
else:
    print(-1)




52.查找数列中重复数字
D, d = set(), set()
for i in list(map(int, input().split())):
    if i in D: d.add(i)
    else: D.add(i)
print(sorted(d))



53.通讯录
def menu():
    print('\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存)


dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

print(dic)
menu()
c=input()
if c=='3':
    name=input()
    if name in dic:
        tel=input()
        dep=input()
        dic[name][0] =tel
        dic[name][1]=dep
        print('Success')
    else:
        print('No Record')
    print(dic)
else:
    print('ERROR')



54.通讯录（查询）
def menu():
    print(\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存)

dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

print(dic)
menu()
c=input()
if c=='4':
    name=input()
    if name in dic:
         print(name,end=' ') 
         for i in dic.get(name):
            print(i,end=' ')
         print("\nSuccess")
    else:
        print("No Record")
    print(dic)
else:
    print("ERROR")



55.通讯录（删除）
def menu():
    print(\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存)


dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

print(dic)
menu()
c=input()
if c=='2':
    name=input()
    if name in dic:
        del dic[name]
        print("Success")
    else:
        print("No Record")
    print(dic)
else:
    print("ERROR")



56.通讯录（添加）
def menu():
    print(\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存)
dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

print(dic)
menu()
c=input()
if c=='1':
    name=input()
    if name in dic:
        print('Fail')
    else:
        tel=input()
        dep=input()
        dic[name]=[tel,dep]
        print('Success')
    print(dic)
else:
    print('ERROR')





57.2024政府工作报告数据提取
import string

def Read_report(name):  
    #读取报告原文，返回字符串。
    with open(name,'r',encoding='UTF-8') as f:
        return f.read()


def Short(s):  
    #定义函数，判断字符串s中是否包含数字字符
    for i in s:
        if i.isdigit():
            return True
    return False
    

def Sign_delete(s):  
    #定义函数，将报告字符串中的所有中文标点符号替换成英文空格，以便后续分割列表。
    sign = ['＂', '＃', '＄', '％', '＆', '＇', '（', '）', '＊', '＋', '，', '－', '／', '：', '；', '＜', '＝', '＞', '＠', '［', '＼', '］', '＾', '＿', '｀', '｛', '｜', '｝', '～', '?', '?', '?', '?', '?', '\u3000', '、', '〃', '〈', '〉', '《', '》', '「', '」', '『', '』', '【', '】', '〔', '〕', '〖', '〗', '?', '?', '?', '?', '?', '〝', '〞', '?', '?', '?', '?', '–', '—', '‘', '’', '?', '“', '”', '?', '?', '…', '?', '﹏', '﹑', '﹔', '·', '．', '！', '？', '?', '。']
    for i in sign:
        s=s.replace(i,' ')
    return s


name = '2024政府工作报告.txt'
report  = Read_report(name)   #读取报告文件
report  = Sign_delete(report) #替换报告中符号，以便后续分隔
key = input()  #输入关键词
# 下方继续后续流程设计代码
if key in report:
    print(report.count(key))
    ls=[x for x in report.split() if key in x]
    print(*ls,sep='\n')
elif key=='数字短句':
    ls=[x for x in report.split() if Short(x)]
    print(*ls,sep='\n')
else:
    print('未找到关键词')






58.英文小说词频统计
import string
with open('novel.txt', 'r', encoding  = 'utf-8') as f:
        s=f.read()
#文件中数据被读取为字符串 s
s=s.lower()
for c in string.punctuation:
    s=s.replace(c,' ')
ls=s.split()
key=input()
if key=='count_1':
    md={}
    for word in ls: 
        md[word] = md.get(word, 0) + 1 
    smd = sorted(md.items(), key=lambda x: x[1], reverse=True)
    for i in range(30):
        w,c=smd[i]
        print(w,c)

elif key=='count_2':
    md={}
    for word in ls:
        if len(word) >=2:           
            md[word] = md.get(word, 0) + 1 
    smd = sorted(md.items(), key=lambda x: x[1], reverse=True)
    for i in range(30):
        w,c=smd[i]
        print(w,c)

elif key=='count_3':
    md={}
    ex = ['that', 'with', 'said', 'have', 'which', 'this', 'your', 'will', 'from', 'what', 'then', 'count', 'they', 'were', 'would', 'when', 'well', 'there', 'know', 'more', 'young', 'them', 'only', 'madame', 'replied', 'time', 'their', 'some', 'like', 'very', 'father', 'into', 'could', 'should', 'than', 'shall', 'been']
    for word in ls:
        if len(word) >=4 and word not in ex:           
            md[word] = md.get(word, 0) + 1 
    smd = sorted(md.items(), key=lambda x: x[1], reverse=True)
    for i in range(7):
        w,c=smd[i]
        print(w,c)
else:
    print('Error')





59.态密度曲线绘制
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Fangsong']
plt.rcParams['axes.unicode_minus'] = False
with open('DosOfBaTiO3.txt','r') as f:
    ls=[x.strip().split() for x in f]
x=[float(x[0]) for x in ls]
y=[float(x[1]) for x in ls]
plt.plot(x,y,linestyle='-',color='b',linewidth=1)
plt.xlabel('Energy(Ha)')
plt.ylabel('Density of States(electrons/Ha)')
plt.show()



60.XRD谱图绘制
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Fangsong']
plt.rcParams['axes.unicode_minus'] = False

with open('XRD_AFO.csv','r') as f:
    ls=[x.strip().split() for x in f]
x=[float(x[0]) for x in ls]
y=[float(x[1]) for x in ls]
plt.plot(x,y,linestyle='--',linewidth=2,color='b')
plt.title('X射线衍射图谱')
plt.xlabel('Position(2-Theta)')
plt.ylabel('Intensity')
plt.show()



61.绘制温度曲线
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
with open('9.1 某月温度.txt','r') as f:
    ls=[x.strip().split() for x in f]
x=[int(i[0]) for i in ls]
h=[int(i[1]) for i in ls]
l=[int(i[2]) for i in ls]
plt.plot(x,h,marker='*',color='g')
plt.plot(x,l,marker='o',color='r')
plt.xticks(list(range(1,32)))
plt.yticks(list(range(-10,30,5)))
plt.title('9月温度曲线图')
plt.show()
'''
