import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from screeninfo import get_monitors
from win32api import GetMonitorInfo, MonitorFromPoint

class UI_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resolution = QDesktopWidget().screenGeometry()
        self.sizes_resolution=[round(self.resolution.width()//100),round(self.resolution.height()//100)]

        self.setGeometry(0,0,self.sizes_resolution[0]*60,self.sizes_resolution[1]*60)
        self.setWindowTitle("XYZ-MusicPlayer")
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.move_screen()
        self.init_UI()
        self.get_task_bar_height()
        self.init_main_part()
    def init_UI(self):
        self.x=0
        self.r_list=[]
        self.full_opened=False
        self.what_clicked="login"

        self.init_topbar()
        self.setStyleSheet("background-color:black;"
                           "font-family: Helvetica;")

        self.old_pos = None

    def init_topbar(self):
        img=QPixmap("images/logo/logo.jpg")
        self.img_name=QLabel(self)
        self.img_name.setGeometry(self.x+10,0,50,50)
        self.img_name.setPixmap(img)


        self.name=QLabel("XYZ-MusicPlayer",self)
        self.name.setStyleSheet("color:whitesmoke;"
                           "font-size:20px;"
                           "font-weight:200;")
        self.name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.name.setGeometry(self.x+55,10,self.sizes_resolution[0]*20,self.sizes_resolution[1]*2)


        self.btn_minimum=QPushButton("—",self)
        self.btn_minimum.setGeometry((self.x+self.sizes_resolution[0]*60)-50*3,0,50,50)
        self.btn_minimum.clicked.connect(self.minim)
        self.btn_minimum.setStyleSheet("QPushButton{"
                                       "color:whitesmoke;"
                                       "font-size: 30px;"
                                       "font-weight: 200;"
                                       "}"
                                       "QPushButton::hover{"
                                       "background-color:red;"
                                       "border:none;"
                                       "border-radius:10px;"
                                       "}")


        self.btn_full = QPushButton("🗖", self)
        self.btn_full.setGeometry((self.x+self.sizes_resolution[0]*60) - 50 * 2, 0, 50, 50)
        self.btn_full.clicked.connect(self.max_size)
        self.btn_full.setStyleSheet("QPushButton{"
                                    "color:whitesmoke;"
                                       "font-size: 30px;"
                                       "font-weight: 200;"
                                    "}"
                                    "QPushButton::hover{"
                                       "background-color:red;"
                                       "border:none;"
                                       "border-radius:10px;"
                                       "}")
        self.flag_max=False


        self.btn_close = QPushButton("✕", self)
        self.btn_close.setGeometry((self.x+self.sizes_resolution[0]*60) - 50 , 0, 50, 50)
        self.btn_close.clicked.connect(self.close_app)
        self.btn_close.setStyleSheet("QPushButton{"
                                     "color:whitesmoke;"
                                    "font-size: 30px;"
                                    "font-weight: 200;"
                                     "}"
                                     "QPushButton::hover{"
                                       "background-color:red;"
                                       "border:none;"
                                       "border-radius:10px;"
                                       "}")

        self.text_made_by=QLabel("Made by sdqsz2",self)
        self.text_made_by.setGeometry(0,self.sizes_resolution[1]*58,self.sizes_resolution[0]*60,self.sizes_resolution[1]*2)
        self.text_made_by.setStyleSheet("color:whitesmoke;"
                                        "font-size:"+str(
            abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) +"px;"
                                                                                  "font-family:Helvetica;")
        self.text_made_by.setAlignment(Qt.AlignCenter)


    def init_main_part(self):
        self.textes_reg=["QPushButton{color:whitesmoke;font-size:"+str(abs(round(self.sizes_resolution[0]-self.sizes_resolution[1]*4)))+"px;font-weight:500;font-family: Helvetica;}QPushButton::hover{border:1.5px solid whitesmoke;border-top-left-radius: 0px;border-top-right-radius: 10px;border-bottom-left-radius:10px;border-bottom-right-radius: 0px;}","QPushButton{color:whitesmoke;font-size:"+str(abs(round(self.sizes_resolution[0]-self.sizes_resolution[1]*4)))+"px;font-weight:500;font-family: Helvetica;border:1.5px solid whitesmoke;border-top-left-radius: 0px;border-top-right-radius: 10px;border-bottom-left-radius:10px;border-bottom-right-radius: 0px;}"]
        self.textes_log=["QPushButton{color:whitesmoke;font-size:"+str(abs(round(self.sizes_resolution[0]-self.sizes_resolution[1]*4)))+"px;font-weight:500;font-family: Helvetica;}QPushButton::hover{border:1.5px solid whitesmoke;border-top-left-radius: 10px;border-top-right-radius: 0px;border-bottom-left-radius:0px;border-bottom-right-radius: 10px;}","QPushButton{color:whitesmoke;font-size:"+str(abs(round(self.sizes_resolution[0]-self.sizes_resolution[1]*4)))+"px;font-weight:500;font-family: Helvetica;border:1.5px solid whitesmoke;border-top-left-radius: 10px;border-top-right-radius: 0px;border-bottom-left-radius:0px;border-bottom-right-radius: 10px;}"]
        self.login = QPushButton("Login",self)
        self.login.setGeometry(self.sizes_resolution[0]*30-self.sizes_resolution[0]*5,self.sizes_resolution[1]*6,round(self.sizes_resolution[0]*5.5),self.sizes_resolution[1]*2)
        self.login.setStyleSheet(self.textes_log[1])
        self.login.clicked.connect(self.login_clicked)

        self.reg=QPushButton("Registration",self)
        self.reg.setGeometry(self.sizes_resolution[0]*30+self.sizes_resolution[0]*1,self.sizes_resolution[1]*6,round(self.sizes_resolution[0]*5.5),self.sizes_resolution[1]*2)
        self.reg.setStyleSheet(self.textes_reg[0])
        self.reg.clicked.connect(self.reg_clicked)

        self.textes_stylesheet=["color: #d0cece;""font-size:"+str(abs(round(self.sizes_resolution[0]-self.sizes_resolution[1]*4)))+"px;""font-family:Helvetica;"]
        self.lineedits_stylesheets=["color:#c5c2c2;""background-color:#343232;""border:none;""border-radius:5px;""padding:5px;"]

        self.init_reg()
        self.hide_reg()
        self.init_login()

    def init_login(self):
        self.nickname = QLabel("Nickname/email", self)
        self.nickname.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 24,
                                  self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.nickname.setStyleSheet(self.textes_stylesheet[0])
        self.nickname.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.nickname_input = QLineEdit("", self)
        self.nickname_input.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 27,
                                        self.sizes_resolution[0] * 56, round(self.sizes_resolution[1] * 2.5))
        self.nickname_input.setStyleSheet(self.lineedits_stylesheets[0])
        self.nickname_input.setPlaceholderText("Nickname/email")

        self.password = QLabel("Password", self)
        self.password.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 31,
                                  self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.password.setStyleSheet(self.textes_stylesheet[0])
        self.password.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.password_input = QLineEdit("", self)
        self.password_input.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 34,
                                        self.sizes_resolution[0] * 56, round(self.sizes_resolution[1] * 2.5))
        self.password_input.setStyleSheet(self.lineedits_stylesheets[0])
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)


        self.btn_submit_login = QPushButton("Login", self)
        self.btn_submit_login.setGeometry(round(self.sizes_resolution[0] * 27.5), self.sizes_resolution[1] * 50,
                                          self.sizes_resolution[0] * 5, self.sizes_resolution[1] * 3)
        self.btn_submit_login.setStyleSheet("background-color:#439f76;"
                                            "color:whitesmoke;"
                                            "border:none;"
                                            "border-radius:5px;"
                                            "font-size:" + str(
            abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;")
        self.btn_submit_login.clicked.connect(self.submit_login_clicked)

    def init_reg(self):
        self.nickname_reg = QLabel("Nickname", self)
        self.nickname_reg.setGeometry(self.sizes_resolution[0] *53, self.sizes_resolution[1] * 24,
                                  self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.nickname_reg.setStyleSheet(self.textes_stylesheet[0])
        self.nickname_reg.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        self.nickname_input_reg = QLineEdit("", self)
        self.nickname_input_reg.setGeometry(self.sizes_resolution[0] *53, self.sizes_resolution[1] * 27,
                                        self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
        self.nickname_input_reg.setStyleSheet(self.lineedits_stylesheets[0])
        self.nickname_input_reg.setPlaceholderText("Nickname")

        self.password_reg=QLabel("Password",self)
        self.password_reg.setGeometry(self.sizes_resolution[0] *53, self.sizes_resolution[1] * 31,
                                  self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.password_reg.setStyleSheet(self.textes_stylesheet[0])
        self.password_reg.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.password_input_reg = QLineEdit("", self)
        self.password_input_reg.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 34,
                                        self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
        self.password_input_reg.setStyleSheet(self.lineedits_stylesheets[0])
        self.password_input_reg.setPlaceholderText("Password")
        self.password_input_reg.setEchoMode(QLineEdit.Password)

        self.password_reg_confirm = QLabel("Confirm password", self)
        self.password_reg_confirm.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 38,
                                      self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.password_reg_confirm.setStyleSheet(self.textes_stylesheet[0])
        self.password_reg_confirm.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.password_reg_confirm_input = QLineEdit("", self)
        self.password_reg_confirm_input.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 41,
                                            self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
        self.password_reg_confirm_input.setStyleSheet(self.lineedits_stylesheets[0])
        self.password_reg_confirm_input.setPlaceholderText("Repeat password")
        self.password_reg_confirm_input.setEchoMode(QLineEdit.Password)

        self.show_name = QLabel("Name", self)
        self.show_name.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 45,
                                              self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
        self.show_name.setStyleSheet(self.textes_stylesheet[0])
        self.show_name.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.show_name_input = QLineEdit("", self)
        self.show_name_input.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 48,
                                                    self.sizes_resolution[0] * 45,
                                                    round(self.sizes_resolution[1] * 2.5))
        self.show_name_input.setStyleSheet(self.lineedits_stylesheets[0])
        self.show_name_input.setPlaceholderText("Name")
        self.show_name_input.setEchoMode(QLineEdit.Password)

        self.btn_submit_reg = QPushButton("Registration", self)
        self.btn_submit_reg.setGeometry(round(self.sizes_resolution[0] * 77.5), self.sizes_resolution[1] * 60,
                                          self.sizes_resolution[0] * 5, self.sizes_resolution[1] * 3)
        self.btn_submit_reg.setStyleSheet("background-color:#23451e;color:#9b9797;border:none;border-radius:5px;font-size:" + str(abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;")
        self.btn_submit_reg.clicked.connect(self.submit_reg_clicked)
        self.btn_submit_reg.setDisabled(True)
    def hide_reg(self):
        self.nickname_reg.setHidden(True)
        self.password_reg.setHidden(True)
        self.password_reg_confirm.setHidden(True)
        self.show_name.setHidden(True)
        self.show_name_input.setHidden(True)
        self.nickname_input_reg.setHidden(True)
        self.password_input_reg.setHidden(True)
        self.password_reg_confirm_input.setHidden(True)
        self.btn_submit_reg.setHidden(True)
    def show_reg(self):
        self.nickname_reg.setHidden(False)
        self.password_reg.setHidden(False)
        self.show_name.setHidden(False)
        self.show_name_input.setHidden(False)
        self.password_reg_confirm.setHidden(False)
        self.nickname_input_reg.setHidden(False)
        self.password_input_reg.setHidden(False)
        self.password_reg_confirm_input.setHidden(False)
        self.btn_submit_reg.setHidden(False)

    def hide_login(self):
        if self.full_opened!=True and self.flag_max!=True:
            self.nickname.setHidden(True)
            self.nickname_input.setHidden(True)
            self.password.setHidden(True)
            self.password_input.setHidden(True)
            self.btn_submit_login.setHidden(True)
    def show_login(self):
        self.nickname.setHidden(False)
        self.nickname_input.setHidden(False)
        self.password.setHidden(False)
        self.password_input.setHidden(False)
        self.btn_submit_login.setHidden(False)
    def move_reg(self,mode):
        if mode==1:
            self.nickname_reg.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*17,self.sizes_resolution[0]*45,self.sizes_resolution[1]*2)
            self.nickname_input_reg.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*20,self.sizes_resolution[0]*56,round(self.sizes_resolution[1] * 2.5))
            self.password_reg.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*24,self.sizes_resolution[0]*45,self.sizes_resolution[1]*2)
            self.password_input_reg.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*27,self.sizes_resolution[0]*56,round(self.sizes_resolution[1]*2.5))
            self.password_reg_confirm.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*31,self.sizes_resolution[0]*45,self.sizes_resolution[1]*2)
            self.password_reg_confirm_input.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*34,self.sizes_resolution[0]*56,round(self.sizes_resolution[1]*2.5))
            self.show_name.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*38,self.sizes_resolution[0]*45,self.sizes_resolution[1]*2)
            self.show_name_input.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*41,self.sizes_resolution[0]*56,round(self.sizes_resolution[1]*2.5))
            self.btn_submit_reg.move(round(self.sizes_resolution[0]*27.5),self.sizes_resolution[1]*53)
        else:
            self.nickname_reg.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 24,
                                          self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
            self.nickname_input_reg.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 27,
                                                self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
            self.password_reg.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 31,
                                          self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
            self.password_input_reg.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 34,
                                                self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
            self.password_reg_confirm.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 38,
                                                  self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
            self.password_reg_confirm_input.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 41,
                                                        self.sizes_resolution[0] * 45,
                                                        round(self.sizes_resolution[1] * 2.5))
            self.show_name.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 45,
                                       self.sizes_resolution[0] * 45, self.sizes_resolution[1] * 2)
            self.show_name_input.setGeometry(self.sizes_resolution[0] * 53, self.sizes_resolution[1] * 48,
                                             self.sizes_resolution[0] * 45,
                                             round(self.sizes_resolution[1] * 2.5))
            self.btn_submit_reg.move(round(self.sizes_resolution[0] * 77.5), self.sizes_resolution[1] * 55)
    def reg_clicked(self):
        btns_stylesheets={"default":"background-color:#439f76;color:whitesmoke;border:none;border-radius:5px;font-size:" + str(abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;",
                          "clicked":"background-color:#23451e;color:#9b9797;border:none;border-radius:5px;font-size:" + str(abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;"}

        self.reg.setStyleSheet(self.textes_reg[1])
        self.login.setStyleSheet(self.textes_log[0])
        self.btn_submit_login.setDisabled(True)
        self.btn_submit_login.setStyleSheet(btns_stylesheets['clicked'])
        self.btn_submit_reg.setDisabled(False)
        self.btn_submit_reg.setStyleSheet(btns_stylesheets['default'])
        self.what_clicked="reg"
        if self.flag_max!=True and self.full_opened!=True:
            self.hide_login()
            self.move_reg(1)
            self.show_reg()
    def login_clicked(self):
        btns_stylesheets = {
            "default": "background-color:#439f76;color:whitesmoke;border:none;border-radius:5px;font-size:" + str(
                abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;",
            "clicked": "background-color:#23451e;color:#9b9797;border:none;border-radius:5px;font-size:" + str(
                abs(round(self.sizes_resolution[0] - self.sizes_resolution[1]) * 1)) + "px;"}

        self.reg.setStyleSheet(self.textes_reg[0])
        self.login.setStyleSheet(self.textes_log[1])
        self.btn_submit_login.setDisabled(False)
        self.btn_submit_login.setStyleSheet(btns_stylesheets['default'])
        self.btn_submit_reg.setDisabled(True)
        self.btn_submit_reg.setStyleSheet(btns_stylesheets['clicked'])
        self.what_clicked="login"
        if self.flag_max!=True and self.full_opened!=True:
            self.hide_reg()
            self.move_reg(0)
            self.show_login()
    def submit_login_clicked(self):
        pass
    def submit_reg_clicked(self):
        pass




    def get_task_bar_height(self):
        m = get_monitors()[0]
        self.monitorInfo = {}
        self.monitorInfo['width'] = m.width
        self.monitorInfo['height'] = m.height
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        monitor_area = monitor_info.get("Monitor")
        work_area = monitor_info.get("Work")
        self.taskbar_height = monitor_area[3] - work_area[3]

    def minim(self):
        self.showMinimized()

    def close_app(self):
        self.close()

    def move_obj(self,mode):
        if mode==1:
            self.btn_minimum.move(self.resolution.width()-50*3,0)
            self.btn_full.move(self.resolution.width()-50*2,0)
            self.btn_close.move(self.resolution.width()-50,0)
            self.login.move(self.sizes_resolution[0]*50-self.sizes_resolution[0]*5,self.sizes_resolution[1]*6)
            self.reg.move(self.sizes_resolution[0]*50+self.sizes_resolution[0]*1,self.sizes_resolution[1]*6)
            self.nickname_input.setGeometry(self.sizes_resolution[0]*2,self.sizes_resolution[1]*27,self.sizes_resolution[0]*45,round(self.sizes_resolution[1]*2.5))
            self.password_input.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 34,
                                            self.sizes_resolution[0] * 45, round(self.sizes_resolution[1] * 2.5))
            self.btn_submit_login.move(round(self.sizes_resolution[0]*23.5),self.sizes_resolution[1]*60)
            self.text_made_by.setGeometry(0,self.sizes_resolution[1]*97,self.sizes_resolution[0]*100,self.sizes_resolution[1]*2)

        else:
            self.btn_minimum.move((self.x + self.sizes_resolution[0] * 60) - 50 * 3, 0)
            self.btn_full.move((self.x + self.sizes_resolution[0] * 60) - 50 * 2, 0)
            self.btn_close.move((self.x + self.sizes_resolution[0] * 60) - 50, 0)
            self.login.move(self.sizes_resolution[0] * 30 - self.sizes_resolution[0] * 5, self.sizes_resolution[1] * 6)
            self.reg.move(self.sizes_resolution[0] * 30 + self.sizes_resolution[0] * 1, self.sizes_resolution[1] * 6)
            self.nickname_input.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 27,
                                      self.sizes_resolution[0] * 56, round(self.sizes_resolution[1] * 2.5))
            self.password_input.setGeometry(self.sizes_resolution[0] * 2, self.sizes_resolution[1] * 34,
                                            self.sizes_resolution[0] * 56, round(self.sizes_resolution[1] * 2.5))
            self.btn_submit_login.move(round(self.sizes_resolution[0]*27.5),self.sizes_resolution[1]*50)
            self.text_made_by.setGeometry(0,self.sizes_resolution[1]*58,self.sizes_resolution[0]*60,self.sizes_resolution[1]*2)



    def max_size(self):
        if self.flag_max==False:
            self.setGeometry(0,0,self.resolution.width(),self.resolution.height()-self.taskbar_height)
            self.flag_max=True
            self.full_opened=True
            self.btn_full.setText("🗗")
            self.move_obj(1)

            self.show_reg()
            self.move_reg(0)
            self.show_login()

        else:
            self.setGeometry(0,0,self.sizes_resolution[0]*60,self.sizes_resolution[1]*60)
            self.move_screen()
            self.flag_max=False
            self.full_opened=False
            self.btn_full.setText("🗖")
            self.move_obj(0)

            self.hide_login()
            self.hide_reg()

            if self.what_clicked=="login":
                self.move_reg(0)
                self.hide_reg()
                self.show_login()
            elif self.what_clicked=="reg":
                self.hide_login()
                self.show_reg()
                self.move_reg(1)


    def move_screen(self):
        self.move((self.resolution.width() // 2) - (self.frameSize().width() // 2),
                  (self.resolution.height() // 2) - (self.frameSize().height() // 2))


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return

        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)



def main():
    app = QApplication(sys.argv)  # создаем обьект класса QApplication
    window = UI_app()  # создаем обьект класса MainWindow
    window.show()  # показываем окно
    sys.exit(app.exec_())  # обрабатываем закрывание окна

if __name__=="__main__":
    main()