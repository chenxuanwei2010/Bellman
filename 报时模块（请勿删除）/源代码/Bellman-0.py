#codding=utf-8
'''该程序主要分为个部分，分别用不同的字母表示， A为模块导入部分，B为变量设置部分，
C是pygame库音频初始化语句，D为函数定义部分，E为启动提示弹窗部分,F为调休校准部分，
G为星期调控和临时修改部分,主要通过对列表进行增减操作达到控制目的,H为报时部分，
曾经共分为交手机、上课、下课、放学和非报时时刻处理五个部分，#*需要区分星期,
要特别注意，现在已单独封装为函数，使得代码简短。
    lingsheng1-4为铃声文件路径，t为当前时间变量，weekday_num为当前星期变量，
b,c,d,e用于调休校准，rizhiweizhi为日志文件路径。
    常用日志语句放在字典rizhiyuju中方便进行调用的方式来写日志，非常用语句可以直接进行填写
    对表如下：
    r1:程序启动
    r2:预备铃打铃
    r3:上课铃打铃
    r4:下课铃打铃
    r5:放学铃打铃
    r6:下课提醒触发'''
# A
import time
import pygame
import tkinter as tk
import traceback
import ast
#B
t = time.localtime(time.time())
weekday_num = t.tm_wday  # 获取当前是星期几，0代表星期一，6代表星期天
lingsheng1= "E:\报时模块（请勿删除）\报时铃声\预备铃.mp3"
lingsheng2="E:\报时模块（请勿删除）\报时铃声\上课铃.mp3"
lingsheng3="E:\报时模块（请勿删除）\报时铃声\下课铃.mp3"
lingsheng4="E:\报时模块（请勿删除）\报时铃声\放学铃声(鸟之诗).mp3"
rizhiweizhi="E:\报时模块（请勿删除）\日志\日志.txt"
cuowurizhiweizhi="E:\报时模块（请勿删除）\日志\错误日志.txt"
linshi_file_path = "E:\报时模块（请勿删除）\临时修改\临时修改.txt"
baoshiyubei = ["0745", "0815", "1010", "1355", "1455", "1545", "1855", "2005"]  # 交手机/预备铃时间
baoshishangke = ["0750", "0820", "1015", "1400", "1500", "1550", "1900", "2010"]  # 上课铃时间
baoshizhaowan = ["0805", "2000", "2035"]  # 早读和晚自习下课时间
baoshixia = ["0950", "1445", "1540"]  # 其他课程下课时间
baoshishuangwu = ["1130"]  # 上午放学时间
baoshifangxue = ["1635"]  # 放学铃时间
baoshilinshi = []#用于存放临时时间点,程序启动时为空
rizhiyuju = {'r1':"程序启动","r2":"预备铃打铃","r3":"上课铃打铃","r4":"下课铃打铃","r5":"放学铃打铃","r6":"下课提醒触发"}
#C
pygame.mixer.init()
#D
def rizhi(a):#日志填写模块，a为日志内容
    with open(rizhiweizhi, 'a', encoding='utf-8') as file:
        now = time.strftime('%Y/%m/%d-%H:%M:%S')
        file.write(now + '\n')
        file.write(a + "\n")
        file.close()

def cuowu_try(func,func_name=""):#错误日志填写模块，a为try内容,b为错误日志内容
    try:
        return func()
    except Exception as e:
        with open(cuowurizhiweizhi, 'a', encoding='utf-8') as file:
            now = time.strftime('%Y/%m/%d-%H:%M:%S')
            file.write(now + '\n')
            if func_name:
                file.write(f"函数/操作: {func_name}\n")
            
            # 关键：记录类似你想要的格式
            tb = traceback.format_exc()
            file.write(f"异常详情:\n{tb}\n")
            
            file.write("-"*50 + "\n")
            
        rizhi(f'错误已记录到日志: {type(e).__name__} \n错误日志:'+str(e) +'已填写至错误日志文件')
        return None

def chuangkou(text,t,r):#弹窗快捷制作模块：text为提示文字，t为显示时间，单位毫秒,r为日志内容
    window = tk.Tk()
    window.title('提示')
    window.geometry('300x200')  # 注意：这里的乘是×不是*
    a = tk.Label(window, text=text, font=(1, 25))
    a.pack(pady=5)
    window.after(t, window.destroy)
    window.mainloop()
    rizhi(r)

def daling(x,y):#打铃模块，x为是否提示，y为铃声文件路径
    if x:#打铃不提示
        pygame.mixer.music.load(y)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        if y==lingsheng1:
            rizhi(rizhiyuju["r2"])
        elif y==lingsheng2:
            rizhi(rizhiyuju["r3"])
        elif y==lingsheng3:
            rizhi(rizhiyuju["r4"])
        elif y==lingsheng4:
            rizhi(rizhiyuju["r5"])
    else:#打铃并提示
        pygame.mixer.music.load(y)
        pygame.mixer.music.play()
        rizhi(rizhiyuju["r4"])
        chuangkou("老师\n您辛苦了\n不要忘记带走U盘",120000,rizhiyuju["r6"])

def chazhao(n, action_type="find"):
    """
    查找时间点所在列表
    n: 时间点字符串
    action_type: 操作类型，"find"=返回列表，"remove"=删除并返回True/False
    """
    lists_to_check = [
        (baoshiyubei, "预备铃"),
        (baoshishangke, "上课铃"),
        (baoshizhaowan, "早读晚自习下课"),
        (baoshixia, "其他课程下课"),
        (baoshishuangwu, "上午放学"),
        (baoshifangxue, "放学铃"),
        (baoshilinshi, "临时铃声")
    ]
    
    for lst, name in lists_to_check:
        if n in lst:
            if action_type == "remove":
                lst.remove(n)
                rizhi(f"已从{name}列表中删除时间点: {n}")
                return True
            else:  # find
                return lst
    return None

def baoshi():#报时模块
    n=time.strftime('%H%M')
    if n in baoshiyubei:#预备铃
        daling(1,lingsheng1)
        baoshiyubei.remove(n)
    elif n in baoshishangke:#上课铃
        daling(1,lingsheng2)
        baoshishangke.remove(n)
    elif n in baoshizhaowan:#早读和晚自习下课
        daling(1,lingsheng3)
        baoshizhaowan.remove(n)
    elif n in baoshixia:#其他课程下课
        daling(0,lingsheng3)
        baoshixia.remove(n)
    elif n in baoshishuangwu:#上午放学
        daling(0,lingsheng3)
        baoshixia.remove(n)
    elif n in baoshifangxue:#放学铃
        daling(1,lingsheng4)
        baoshifangxue.remove(n)
    elif n in baoshilinshi:#临时铃声
        daling(1,lingsheng1)
        baoshilinshi.remove(n)
    else:
        time.sleep(0.5)#非报时时刻处理
    
def liebiaocaozuo(a,b,c=None,d=None):#列表操作模块，a为时间点字符串，b为操作类型（0添加，1删除，2修改），c为操作列表，d为新时间点（修改时使用）
    zongliebiao = baoshiyubei + baoshishangke + baoshizhaowan + baoshixia + baoshishuangwu + baoshifangxue + baoshilinshi
    def jiancha_cunzai():#检查时间点是否在列表中，存在返回True，不存在返回False
        if a in zongliebiao:
            return  True
        elif a not in zongliebiao:
            return False
        else:
            return None
    def jiancha_weizhi():#检查时间点所在位置，存在返回列表，不存在返回False
        if c in [baoshiyubei, baoshishangke, baoshizhaowan, baoshixia, baoshishuangwu, baoshifangxue, baoshilinshi]:
            return True
        elif c not in [baoshiyubei, baoshishangke, baoshizhaowan, baoshixia, baoshishuangwu, baoshifangxue, baoshilinshi]:
            return False
        else:
            return None
    def jiancha_bianma(x=a):
        if a.isdigit() and len(x)==4:
            f=int(x[0:2])
            g=int(x[2:4])
            if 0<=f<=23 and 0<=g<=59:
                return True
            else:
                return False
        else:
            return False
    if jiancha_bianma and b in [0,1,2]:
        if b==0:
            if jiancha_cunzai:
                rizhi(f"添加时间点失败，列表中已存在该时间点: {a}")
            if not jiancha_cunzai:
                if jiancha_weizhi:
                    c.append(a)
                    rizhi(f"已在列表:{c}中添加时间点: {a}")
                elif not jiancha_weizhi:
                    baoshilinshi.append(a)
                    rizhi(f"为找到：{c},已在列表:临时铃声中添加时间点: {a}")
                else:
                    rizhi(f"添加时间点失败，列表位置错误: {c}")
            else:
                rizhi(f"添加时间点失败，程序异常")
        elif b==1 :
            if jiancha_cunzai:
                c=chazhao(n=a)
                c.remove(a)
                rizhi(f"已在列表:{c}中删除时间点: {a}")
            elif not jiancha_cunzai:
                rizhi(f"删除时间点失败，列表中无该时间点: {a}")
            else:
                rizhi(f"删除时间点失败，程序异常")
        elif b==2:
            if jiancha_cunzai:
                if jiancha_bianma(d):
                    c=chazhao(n=a)
                    c.remove(a)
                    c.append(d)
                    rizhi(f"已将时间点: {a} 修改为: {d}")
                else:
                    rizhi(f"修改时间点失败，新时间点格式错误: {d}")
            else:
                rizhi(f"修改时间点失败，列表中无该时间点: {a}")
    else:
        rizhi(f"列表操作失败，操作类型错误: {b} 或 时间点格式错误: {a}")

#E

chuangkou("报时模块已启动",1000,rizhiyuju['r1'])
#F
def tiaoxiu():
    rizhi("调休校准模块启动")
    global weekday_num
    weekday_num = globals()['weekday_num']
    t = globals()['t']
    b=0
    c=0
    d=0
    e=0
    if weekday_num > 4:
        with open('E:\报时模块（请勿删除）\调休校准\调休校准.txt', 'r') as file:
            a=0
            for line in file:
                if a== 0:
                    b = int(line.strip())
                elif a == 1:
                    c = int(line.strip())
                elif a == 2:
                    d = int(line.strip())
                elif a == 3:
                    e = int(line.strip())
                a += 1
            file.close()
        rizhi(f"读取调休校准数据: {b}年{c}月{d}日 调休至星期{e+1}")



        if t.tm_year!=b or t.tm_mon!=c or t.tm_mday!=d or e not in [0,1,2,3,4]:
            rizhi("需要进行调休校准")
            x=0
            while x == 0:#循环直到输入正确或超时, X用于跳出循环

                global global_value
                global_value = ""
                def get_input(event='<Return>'):
                    global global_value  # 声明使用全局变量
                    value = entry.get()  # 获取输入框的值
                    global_value = value  # 赋值给全局变量
                    root.destroy()  # 关闭窗口
                
                root = tk.Tk()
                root.geometry('300x200')
                root.title('提示')
                a = tk.Label(root, text="请输入\n调休后的星期\n（1-5）", font=(1, 25))
                a.pack(pady=5)
                # 输入框
                entry = tk.Entry(root)
                entry.pack(pady=10)
                # 绑定回车键
                entry.bind('<Return>', get_input)
                # 按钮 - command绑定点击事件
                button = tk.Button(root, text="确定", command=get_input)

                button.pack()
                try:
                    root.after(15000, root.destroy)  # 15秒后自动关闭窗口
                except:
                    pass
                root.mainloop()

                if global_value in ['1','2','3','4','5']:
                    f = int(global_value)
                    weekday_num = f-1
                    with open('E:\报时模块（请勿删除）\调休校准\调休校准.txt', 'w', encoding='utf-8') as file:
                        file.write(str(t.tm_year)+"\n")
                        file.write(str(t.tm_mon)+"\n")
                        file.write(str(t.tm_mday)+"\n")
                        file.write(str(e)+"\n")
                        file.close()
                    chuangkou("已切换模式",1000,'调休校准:已切换模式')
                    x += 1
                elif global_value == "":
                    weekday_num = 0
                    with open('E:\报时模块（请勿删除）\调休校准\调休校准.txt', 'w', encoding='utf-8') as file:
                        file.write(str(t.tm_year)+"\n")
                        file.write(str(t.tm_mon)+"\n")
                        file.write(str(t.tm_mday)+"\n")
                        file.write('1' +"\n")
                        file.close()
                        chuangkou("输入超时，\n已默认切换至\n周一模式",1000,'调休校准:输入超时，默认周一模式')
                    x+=1
                else:
                    chuangkou("输入有误,\n请重新输入.\n(1-5)",1000,'调休校准:输入有误，重新输入调休星期')
        elif t.tm_year==b and t.tm_mon==c and t.tm_mday==d:
            rizhi("当天已进行过调休校准，无需重复校准")
            weekday_num = e
    rizhi("调休校准模块运行完毕")

cuowu_try(lambda:tiaoxiu())

#G
def xingqitiaokong():#星期调控
    rizhi("星期调控模块启动")
    global weekday_num
    weekday_num = globals()['weekday_num']
    if weekday_num ==4:
        liebiaocaozuo('1442',0,baoshifangxue)
        for i in ["1455", "1545", "1855", "2005","1500", "1550", "1900", "2010","1445","1540","1635"]:
            liebiaocaozuo(i,1)
        rizhi("已将周五放学时间调整为14:45，并删除其他时间点")
    elif weekday_num == 0:
        for i in ["0745",'0750','0805']:
            liebiaocaozuo(i,1)
        rizhi("已删除周一早读时间点")
    rizhi("星期调控模块运行完毕")
cuowu_try(lambda:xingqitiaokong())

def linshixiugai():
    """临时修改模块"""
    rizhi("临时修改模块启动")
    weekday_num = globals()['weekday_num']
    
    with open(linshi_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, l in enumerate(lines[10:], start=11):  # 跳过前10行
        l = l.strip()  # 去除首尾空白字符
        
        # 跳过空行
        if not l:
            continue
        
        # 检查是否为关闭指令
        if '|' in l:
            parts = l.split('|')
            
            # 关闭指令（2个部分）
            if len(parts) == 2:
                command_type, command_value = parts
                if command_type == 'OFF':
                    if command_value == '程序':
                        rizhi('接收到临时关闭程序指令，程序即将关闭')
                        chuangkou("报时模块即将关闭", 1000, '临时修改模块:接收到关闭程序指令，程序即将关闭')
                        exit()
                    elif command_value == '模块':
                        rizhi('接收到临时关闭模块指令，模块即将关闭')
                        return
                    else:
                        rizhi(f'临时修改模块:未知关闭指令: {command_value}')
                else:
                    rizhi(f'临时修改模块:未知指令类型: {command_type}')
                continue
            
            # 增删改指令（5个部分）
            elif len(parts) == 5:
                n, m, x, y, z = parts
                
                try:
                    # 解析星期列表
                    weekday_list = ast.literal_eval(z)
                    
                    # 检查当前星期是否在允许的星期列表中
                    if weekday_num in weekday_list:
                        if n == '加':
                            # 添加操作
                            liebiaocaozuo(m, 0, eval(y))
                        elif n == '删':
                            # 删除操作
                            liebiaocaozuo(m, 1, eval(y))
                        elif n == '改':
                            # 修改操作
                            liebiaocaozuo(m, 2, eval(y), x)
                        else:
                            rizhi(f'临时修改模块:第{i}行未知操作指令: {n}')
                    else:
                        rizhi(f'临时修改模块:第{i}行当前星期{weekday_num}不在执行范围，跳过')
                        
                except Exception as e:
                    rizhi(f'临时修改模块:第{i}行解析失败: {e}, 行内容: {l}')
                    
            else:
                rizhi(f'临时修改模块:第{i}行指令格式错误，应有2或5个部分，实际有{len(parts)}个部分: {l}')
                
        else:
            rizhi(f'临时修改模块:第{i}行缺少分隔符|，跳过: {l}')
    
    rizhi("临时修改模块运行完毕")
cuowu_try(lambda:linshixiugai())
    
#H
rizhi('报时模块循环运行')   
while 1:
    cuowu_try(lambda:baoshi())
