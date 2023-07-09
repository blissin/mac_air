import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, \
                            QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QStandardItem

# https://www.youtube.com/watch?v=WnHkx-AvTBA

class checkableComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.closeOnLineEditClick = False
        
        self.lineEdit().installEventFilter(self)
        
        # self.view().viewport().installEventFilter(self)
        
        self.model().dataChanged.connect(self.updateLineEditField) #clicked data event
                
    # def evnetFilter(self, widget, event):
    #     if widget == self.lineEdit():
    #         if event.type() == QEvent.QMouseButtonRelease:
    #             if self.closeOnLineEditClick:
    #                 self.hidePopup()
    #             else:
    #                 self.showPopup()
    #             return True
    #         return super().eventFilter(widget, event)
        
    #     if widget == self.view().viewport()    :
    #         if event.type() == QEvent.MouseButtonRelease:
    #             idx = self.view().indexAt(event.pos())
    #             item = self.model().item(idx.row())
                
    #             if item.checkState() == Qt.Checked:
    #                 item.setCheckStae(Qt.Unchecked)
    #             else:
    #                 item.setCheckState(Qt.Checked)
    #             return True
    #         return super().eventFilter(widget, event)

    # def hidePopup(self):
    #     super().hidePopup()
    #     self.startTimer(100)

    def addItems(self, items, itemList=None):
        for idx, txt in enumerate(items):
            try:
                data = itemList[idx]
            except(TypeError, IndexError):
                data = None
            self.addItem(txt, data)
        
    def addItem(self, text, userData=None):
        item = QStandardItem()
        item.setText(text)
        if userData:
            item.setData(userData)
        
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)
        
    def updateLineEditField(self):
        text_container=[]
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                text_container.append(self.model().item(i).text())
        print(text_container)
        text_string = ', '.join(text_container)
        self.lineEdit().setText(text_string)

class checkableComboBox2(QComboBox):
    def __init__(self):
        super().__init__()
        # self.activated.connect(self.clicked)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # self.model().dataChanged.connect(self.updateLineEditField)

    def clicked(self, index):
        option = self.itemText(index)
        print(option)

    def addItems(self, items, itemList=None):
        for idx, txt in enumerate(items):
            self.addItem(txt)
    
    def addItem(self, text, userData=None):
        item = QStandardItem()
        item.setText(text)
        item.setFlags(Qt.ItemIsEnabled|Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)
    
    def updateLineEditField(self):
        text_container=[]
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                text_container.append(self.model().item(i).text())
        print(text_container)
        text_string = ', '.join(text_container)
        self.lineEdit().setText(text_string)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_heigth = 1200, 200
        self.setMinimumSize(self.window_width, self.window_heigth)
        self.setStyleSheet('''
                           Qwidget{
                               font-size : 50px
                           }
                           ''')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        combobox = checkableComboBox()
        combobox.addItems(colors)
        self.layout.addWidget(combobox)

        combobox2 = checkableComboBox2()
        combobox2.addItems(colors)
        self.layout.addWidget(combobox2)
        
        btn = QPushButton('Retrive', clicked=lambda:print(combobox.lineEdit().text()))
        self.layout.addWidget(btn)
        
if __name__ == '__main__':
    
    colors = ['blue','yellow','orange']
    
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('closing')
        