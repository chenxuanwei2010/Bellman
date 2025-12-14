import time
import pygame
import tkinter as tk
cuowurizhiweizhi="E:\报时模块（请勿删除）\日志\错误日志.txt"
def jiancha_bianma(a):
        if a.isdigit() and len(a)==4:
            f=int(a[0:2])
            g=int(a[2:4])
            print(f,g)
            if 0<=f<=23 and 0<=g<=59:
                return True
            else:
                return False
        else:
            return False
print(jiancha_bianma("1234"))