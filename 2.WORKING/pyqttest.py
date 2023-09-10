import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QListView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class ComboListViewApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('ComboBox and ListView Example')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        # 리스트뷰 생성
        self.listView = QListView(self)
        layout.addWidget(self.listView)

        # 콤보박스1 생성 (id)
        self.comboBox1 = QComboBox(self)
        layout.addWidget(self.comboBox1)

        # 콤보박스2 생성 (number)
        self.comboBox2 = QComboBox(self)
        layout.addWidget(self.comboBox2)

        # 콤보박스3 생성
        self.comboBox3 = QComboBox(self)
        layout.addWidget(self.comboBox3)

        # 문자열 리스트
        self.str_list = [
            '1111_555_202307111200',
            '2222_777_202308152345',
            '3333_888_202309201030',
            '4444_999_202310101515',
            '5555_111_202311112230',
            '1111_555_202311112245',
            '1111_555_202311112300',
            '1111_777_202311112315',
            '1111_999_202311112330'
        ]

        # 리스트뷰 모델 생성
        self.model = QStandardItemModel()

        for s in self.str_list:
            # 문자열을 언더스코어로 분리
            parts = s.split('_')

            # 콤보박스1에 아이템 추가 (id)
            self.comboBox1.addItem(parts[0])

            # 콤보박스2에 아이템 추가 (number)
            self.comboBox2.addItem(parts[1])

            # 콤보박스3에 아이템 추가 (time)
            self.comboBox3.addItem(parts[2])

            # 리스트뷰 모델에 아이템 추가
            item = QStandardItem(s)
            self.model.appendRow(item)

        # 리스트뷰에 모델 설정
        self.listView.setModel(self.model)

        # 콤보박스 선택 이벤트에 대한 시그널 및 슬롯 연결
        self.comboBox1.currentIndexChanged.connect(self.updateComboBox2And3)
        self.comboBox2.currentIndexChanged.connect(self.updateComboBox1And3)
        self.comboBox3.currentIndexChanged.connect(self.updateComboBox1And2)

        # 위젯을 담을 수 있는 레이아웃을 설정
        container = QWidget(self)
        container.setLayout(layout)

        # QMainWindow에 위젯 설정
        self.setCentralWidget(container)

    def updateComboBox2And3(self):
        # 선택된 콤보박스1의 값 가져오기
        selected_id = self.comboBox1.currentText()

        # ComboBox2 업데이트
        self.comboBox2.clear()  # 기존 항목 제거

        # '1111_'로 시작하는 항목 필터링
        filtered_list = [s for s in self.str_list if s.startswith(selected_id + '_')]

        # 필터링된 항목에서 '1111_' 다음 부분 (number)을 추출하여 ComboBox2에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox2.addItem(parts[1])

        # ComboBox3 업데이트
        self.comboBox3.clear()  # 기존 항목 제거

        # 필터링된 항목에서 '1111_' 다음 부분 (time)을 추출하여 ComboBox3에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox3.addItem(parts[2])

    def updateComboBox1And3(self):
        # 선택된 콤보박스2의 값 가져오기
        selected_number = self.comboBox2.currentText()

        # ComboBox1 업데이트
        self.comboBox1.clear()  # 기존 항목 제거

        # '1111_'로 시작하는 항목 필터링
        filtered_list = [s for s in self.str_list if s.split('_')[1] == selected_number]

        # 필터링된 항목에서 '1111_' 다음 부분 (id)을 추출하여 ComboBox1에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox1.addItem(parts[0])

        # ComboBox3 업데이트
        self.comboBox3.clear()  # 기존 항목 제거

        # 필터링된 항목에서 '1111_' 다음 부분 (time)을 추출하여 ComboBox3에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox3.addItem(parts[2])

    def updateComboBox1And2(self):
        # 선택된 콤보박스3의 값 가져오기
        selected_time = self.comboBox3.currentText()

        # ComboBox1 업데이트
        self.comboBox1.clear()  # 기존 항목 제거

        # '1111_'로 시작하는 항목 필터링
        filtered_list = [s for s in self.str_list if s.split('_')[2] == selected_time]

        # 필터링된 항목에서 '1111_' 다음 부분 (id)을 추출하여 ComboBox1에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox1.addItem(parts[0])

        # ComboBox2 업데이트
        self.comboBox2.clear()  # 기존 항목 제거

        # 필터링된 항목에서 '1111_' 다음 부분 (number)을 추출하여 ComboBox2에 추가
        for s in filtered_list:
            parts = s.split('_')
            self.comboBox2.addItem(parts[1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ComboListViewApp()
    window.show()
    sys.exit(app.exec_())

