import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Button(QPushButton):
    def move_btn(self,btn,mode,res):
        if mode==0:
            btn.move()


