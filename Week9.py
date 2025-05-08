import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QInputDialog, QLabel, QComboBox

class InputDialogDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Dialog Demo")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.select_button = QPushButton("Choose from list")
        self.select_button.clicked.connect(self.show_select_dialog)
        layout.addWidget(self.select_button)

        self.name_button = QPushButton("Get name")
        self.name_button.clicked.connect(self.show_text_dialog)
        layout.addWidget(self.name_button)

        self.int_button = QPushButton("Enter an integer")
        self.int_button.clicked.connect(self.show_int_dialog)
        layout.addWidget(self.int_button)

        self.result_label = QLabel("Results will appear here.")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def show_select_dialog(self):
        languages = ['C', 'C++', 'Java', 'Python', 'Ruby']
        item, ok = QInputDialog.getItem(self, "Select input dialog", "List of languages", languages, 0, False)
        if ok and item:
            self.result_label.setText(f"Selected language: {item}")

    def show_text_dialog(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.result_label.setText(f"Your name: {text}")

    def show_int_dialog(self):
        num, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Enter a number:")
        if ok:
            self.result_label.setText(f"Entered number: {num}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
