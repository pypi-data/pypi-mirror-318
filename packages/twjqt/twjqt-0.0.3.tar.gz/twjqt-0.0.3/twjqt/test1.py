import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMainWindow, QMessageBox
from twjqt import music,news,movie,remark,food

def musiccrawl():
    music.get_music_data()
def moviecrawl():
    movie.get_movie_data()
def foodcrawl():
    food.get_food_data()
def remarkcrawl():
    remark.get_hot_topics()
def newscrawl():
    news.main()


# 槽函数
def on_click_messBox():
    messBox = QMessageBox()
    messBox.setWindowTitle(u'操作提示')
    messBox.setText(u'执行成功')
    messBox.exec_()

app=QApplication(sys.argv)

mywindow=QWidget()
# 设置窗口
mywindow.setWindowTitle('爬虫')
mywindow.resize(600,500)
mywindow.move(300,300)

# 添加纯文本
label=QLabel('欢迎使用爬虫程序',mywindow)
label.setGeometry(250,50,100,20)


# 设置按钮事件
button1=QPushButton('音乐',mywindow)
button1.setGeometry(250,100,100,50)
button1.clicked.connect(musiccrawl)
button1.clicked.connect(on_click_messBox)

button2 = QPushButton('电影', mywindow)
button2.setGeometry(250, 150, 100, 50)
button2.clicked.connect(moviecrawl)
button2.clicked.connect(on_click_messBox)

button3 = QPushButton('餐厅', mywindow)
button3.setGeometry(250, 200, 100, 50)
button3.clicked.connect(foodcrawl)
button3.clicked.connect(on_click_messBox)

button3 = QPushButton('评论', mywindow)
button3.setGeometry(250, 250, 100, 50)
button3.clicked.connect(remarkcrawl)
button3.clicked.connect(on_click_messBox)

button3 = QPushButton('热搜', mywindow)
button3.setGeometry(250, 300, 100, 50)
button3.clicked.connect(newscrawl)
button3.clicked.connect(on_click_messBox)



mywindow.show()
app.exec_()