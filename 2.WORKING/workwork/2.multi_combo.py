import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QListView, QAbstractItemView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MultiSelectComboBox(QComboBox):
    def __init__(self, items):
        super(MultiSelectComboBox, self).__init__()
        self.items = items
        self.setView(QListView())
        self.view().setSelectionMode(QAbstractItemView.MultiSelection)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setAlignment(Qt.AlignLeft)

        for item in items:
            self.addItem(item)

class CheckableComboBox(QComboBox):
    def __init__(self, items):
        super(CheckableComboBox, self).__init__()
        self.items = items
        self.setView(QListView())

        model = QStandardItemModel(self)
        self.setModel(model)
        self.view().setModel(model)

        for item in items:
            item = QStandardItem(item)
            item.setCheckable(True)
            item.setCheckState(Qt.Unchecked)
            model.appendRow(item)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(100, 100, 300, 50)

    combo = MultiSelectComboBox(["Option 1", "Option 2", "Option 3", "Option 4"])
    combo = CheckableComboBox(["Option 1", "Option 2", "Option 3", "Option 4"])
    combo.setGeometry(10, 10, 150, 30)
    window.setCentralWidget(combo)
    window.show()
    sys.exit(app.exec_())
