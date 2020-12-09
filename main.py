import sys
from functools import partial
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
import random
import Ui_menu_choice
# import number_guess

def guess_dinner(ui):
    guess = ui.textEdit.toPlainText()
    if guess.find("不") != 1:
        if guess.isdigit():
            if int(guess) == number2:
                ui.textEdit_2.setText("恭喜你猜中了，今天就是吃"+str(number2)+":"+dinner+"哦~")
            elif int(guess) > number2:
                ui.textEdit_2.setText("不对哦，序号还要小一点呢！")
            else:
                ui.textEdit_2.setText("不对哦，序号还要大一点呢！")
        elif guess.isalpha():
            try: 
                guess = num[menu.index(guess)]
                if int(guess) == number2:
                    ui.textEdit_2.setText("恭喜你猜中了，今天就是吃"+str(number2)+":"+dinner+"哦~")
                elif int(guess) > number2:
                    ui.textEdit_2.setText("不对哦，正确菜名还在上面呢！")
                else:
                    ui.textEdit_2.setText("不对哦，正确菜名还在下面呢！")
            except:
                ui.textEdit_2.setText("请输入正确的菜名哦~")
        else:
            ui.textEdit_2.setText("需要在上方输入序号或者菜名哦,如果不想猜了，请输入我不猜~")                
    else:
        ui.textEdit_2.setText("诶呀，真可惜！今天吃的是" + dinner + "啦~")

def no_guess(ui):
    ui.textEdit_2.setText("诶呀，真可惜！今天吃的是" + dinner + "啦~")

def re_guess(ui):
    global number2
    number2 = random.choice(num)
    global dinner
    dinner = menu[number2-1]
    ui.textEdit_2.setText("哼！挑剔鬼！已经换菜了啦，重新输入吧~")

def point_guess(ui):
    global number2
    global dinner
    guess = ui.textEdit.toPlainText()
    if guess.isdigit():
        dinner = menu[int(guess)-1]
        ui.textEdit_2.setText("那就听你一回吧~好好享用" + dinner + "哦！")
    elif guess.isalpha():
        try: 
            number2 = num[menu.index(guess)]
            dinner = menu[number2-1]
            ui.textEdit_2.setText("那就听你一回吧~好好享用" + dinner + "哦！")
        except:
            ui.textEdit_2.setText("请输入正确的菜名哦~")
    else:
        ui.textEdit_2.setText("那需要输入正确的菜名或者序号哦~")

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_menu_choice.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    menu = ["费大厨","胖哥俩","思必客","自煮水饺",
    "自煮火锅","蛙来哒","汴京炸鸡","娟娟",
    "椰子鸡","食三姨","肯德基","蛋包饭",
    "黄焖鸡","烤肉","烧烤","小龙虾",
    "寿司","粉面","小笼包"] 
    number1 = len(menu)
    num = ([x for x in range(1,number1+1)])
    zip1 = zip(num,menu)
    dict1 = dict(zip1)
    number2 = random.choice(num)
    dinner = menu[number2-1]

    ui.pushButton.clicked.connect(partial(guess_dinner,ui))
    ui.pushButton_2.clicked.connect(partial(no_guess,ui))
    ui.pushButton_3.clicked.connect(partial(re_guess,ui))
    ui.pushButton_4.clicked.connect(partial(point_guess,ui))
    sys.exit(app.exec_())
    
