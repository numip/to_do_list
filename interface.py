from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import sys
import json
import os


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('to_do_list.ui', self)
        if 'save.json' in os.listdir('./'):
            self.start()
        self.show()
        self.ui.saveButton.clicked.connect(self.save)

    def save(self):
        values = {}
        for i in range(1, 18):
            values[i] = {
                'checkBox': getattr(self.ui, f"checkBox_{i}", False).isChecked(),
                'lineEdit': getattr(self.ui, f"lineEdit_{i}", False).text()
            }
        values['textEdit'] = self.ui.textEdit.toPlainText()
        with open('save.json', 'w') as f:
            json.dump(values, f)

    def start(self):
        with open('save.json', 'r') as r:
            values = json.load(r)
        for i in range(1, 18):
            getattr(self.ui, f"checkBox_{i}", False).setChecked(values[str(i)]['checkBox'])
            getattr(self.ui, f"lineEdit_{i}", False).setText(values[str(i)]['lineEdit'])
        self.ui.textEdit.setText(values['textEdit'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = Login()
    sys.exit(app.exec())
