from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from ui import Ui_MainWindow
import os

class Easy_editor(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.connects()
    
    def connects(self):
        self.ui.open_btn.clicked.connect(self.choose_folder)

    def filter(self, filenames):
        images = []
        for filename in filenames:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
                images.append(filename)

        return images

    def show_image_list(self):
        filenames = os.listdir(self.workdir)
        self.ui.image_list.clear()
        images = self.filter(filenames)
        self.ui.image_list.addItems(images)
        print(filenames)


    def choose_folder(self):
        self.workdir = QFileDialog.getExistingDirectory()
        self.show_image_list()


app = QApplication([])
ex = Easy_editor()
ex.show()
app.exec_()