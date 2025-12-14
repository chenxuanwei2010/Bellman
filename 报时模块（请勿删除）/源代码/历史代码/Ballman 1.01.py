import time
import pygame
import tkinter as tk
import datetime
now = datetime.datetime.now()
weekday_num = now.weekday()
t = time.localtime(time.time())
pygame.mixer.init()
file1= "E:\报时模块（请勿删除）\报时铃声\预备铃.mp3"
file2="E:\报时模块（请勿删除）\报时铃声\上课铃.mp3"
file3="E:\报时模块（请勿删除）\报时铃声\下课铃.mp3"
file4="E:\报时模块（请勿删除）\报时铃声\放学铃声(鸟之诗).mp3"
if 1:
    window = tk.Tk()
    window.title('提示')
    window.geometry('300x200')  # 注意：这里的乘是×不是*
    a = tk.Label(window, text="程序已开启", font=(1, 25))
    a.pack(pady=5)
    window.after(1000, window.destroy)
    window.mainloop()
while 1:
    t = time.localtime(time.time())
    #交手机
    if t.tm_hour == 7 and t.tm_min == 45 and t.tm_sec == 0:  #早读
         pygame.mixer.music.load(file1)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
             time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 8 and t.tm_min == 15 and t.tm_sec == 0: #上午1，2节
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 10 and t.tm_min == 10 and t.tm_sec == 0:#上午3，4节
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 13 and t.tm_min == 55 and t.tm_sec == 0:#第五节课
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 14 and t.tm_min == 55 and t.tm_sec == 0:#第六节课
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
    elif t.tm_hour == 15 and t.tm_min == 45 and t.tm_sec == 0:#第七节课
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 18 and t.tm_min == 55 and t.tm_sec == 0:#第八节课
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 20 and t.tm_min == 5 and t.tm_sec == 0:#第9节课
        pygame.mixer.music.load(file1)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒

    #上课
    elif t.tm_hour == 7 and t.tm_min == 50 and t.tm_sec == 0:  #早读 上课
         pygame.mixer.music.load(file2)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
             time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 8 and t.tm_min == 20 and t.tm_sec == 0:  # 上午1，2节 上课
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 10 and t.tm_min == 15 and t.tm_sec == 0:  # 上午3,4节 上课
         pygame.mixer.music.load(file2)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
             time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 14 and t.tm_min == 0 and t.tm_sec == 0:  # 上午5节 上课
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 15 and t.tm_min == 0 and t.tm_sec == 0:  # 上午6节 上课
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 15 and t.tm_min == 50 and t.tm_sec == 0:  # 上午7节 上课
         pygame.mixer.music.load(file2)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
             time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 19 and t.tm_min == 0 and t.tm_sec == 0:  # 第八节 上课
         pygame.mixer.music.load(file2)
         pygame.mixer.music.play()
         while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
             time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 20 and t.tm_min == 10 and t.tm_sec == 0:  # 第9节 上课
        pygame.mixer.music.load(file2)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒

    # 下课
    elif t.tm_hour == 8 and t.tm_min == 5 and t.tm_sec == 0:  # 早读 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 9 and t.tm_min == 50 and t.tm_sec == 0:  # 第1，2节 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 14 and t.tm_min == 45 and t.tm_sec == 0:# 第5节 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 15 and t.tm_min == 40 and t.tm_sec == 0:# 第6节 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 20 and t.tm_min == 0 and t.tm_sec == 0:# 第8节 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 20 and t.tm_min == 35 and t.tm_sec == 0:# 第9节 下课
        pygame.mixer.music.load(file3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()

    #放学
    elif t.tm_hour == 11 and t.tm_min == 30 and t.tm_sec == 0:# 上午放学
        pygame.mixer.music.load(file4)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
        window = tk.Tk()
        window.title('下课了')
        window.geometry('300x200')  # 注意：这里的乘是×不是*
        a = tk.Label(window, text="老师\n您辛苦了\n不要忘记带走U盘", font=(1, 25))
        a.pack(pady=5)
        window.after(120000, window.destroy)
        window.mainloop()
    elif t.tm_hour == 16 and t.tm_min == 35 and t.tm_sec == 0:# 下午放学
        pygame.mixer.music.load(file4)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    elif t.tm_hour == 14 and t.tm_min == 45 and t.tm_sec == 0 and weekday_num==4:# 周五下午放学
        pygame.mixer.music.load(file4)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # 检查音乐是否正在播放
            time.sleep(0.1)  # 每次循环等待0.1秒
    else:
        time.sleep(1)
