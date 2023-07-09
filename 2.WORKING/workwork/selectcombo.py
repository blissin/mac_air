from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QStandardItemModel, QStandardItem

class CheckableComboBox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.setView(QComboBox.QListView())  # Set the view to a QListView

    def showPopup(self):
        # Customize the behavior when the combo box is expanded
        self.view().setSelectionMode(QComboBox.QListView.ExtendedSelection)
        super(CheckableComboBox, self).showPopup()

    def hidePopup(self):
        # Customize the behavior when the combo box is collapsed
        self.view().setSelectionMode(QComboBox.QListView.NoSelection)
        super(CheckableComboBox, self).hidePopup()

    def setItemCheckState(self, index, state):
        # Set the check state of an item at the given index
        model = self.model()
        item = model.item(index)
        if item is not None:
            item.setCheckState(state)

    def itemCheckState(self, index):
        # Get the check state of an item at the given index
        model = self.model()
        item = model.item(index)
        if item is not None:
            return item.checkState()

    def checkedItems(self):
        # Get a list of checked items
        model = self.model()
        checked_items = []
        for index in range(model.rowCount()):
            if self.itemCheckState(index) == Qt.Checked:
                checked_items.append(self.itemText(index))
        return checked_items

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a checkable combo box
        self.combo_box = CheckableComboBox(self)

        # Create a model and populate the combo box
        model = QStandardItemModel(self.combo_box)
        items = ['Item 1', 'Item 2', 'Item 3']
        for item in items:
            model.appendRow(QStandardItem(item))
        self.combo_box.setModel(model)

        # Connect a slot to handle item toggled event
        self.combo_box.currentIndexChanged.connect(self.handle_item_toggled)

        # Set the combo box as the central widget
        self.setCentralWidget(self.combo_box)

    def handle_item_toggled(self, index):
        # Get the selected item and its checked state
        item = self.combo_box.itemText(index)
        checked = self.combo_box.itemCheckState(index)

        # Print the selected item and its checked state
        print(f"Selected item: {item}")
        print(f"Checked state: {checked}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
