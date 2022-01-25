import sys
from anonfile import AnonFile
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnonUploadR(object):
    def setupUi(self, AnonUploadR):
        self.file_path = ""

        AnonUploadR.setObjectName("AnonUploadR")
        AnonUploadR.resize(402, 179)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AnonUploadR.sizePolicy().hasHeightForWidth())
        AnonUploadR.setSizePolicy(sizePolicy)
        self.statusLabel = QtWidgets.QLabel(AnonUploadR)
        self.statusLabel.setText("Status : Idle")
        self.statusLabel.setGeometry(QtCore.QRect(10, 0, 300, 20))
        self.openFile = QtWidgets.QPushButton(AnonUploadR)
        self.openFile.setGeometry(QtCore.QRect(10, 150, 171, 23))
        self.openFile.setObjectName("openFile")
        self.longLink_Label = QtWidgets.QLabel(AnonUploadR)
        self.longLink_Label.setGeometry(QtCore.QRect(10, 20, 381, 16))
        self.longLink_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.longLink_Label.setObjectName("longLink_Label")
        self.shortLink_Label = QtWidgets.QLabel(AnonUploadR)
        self.shortLink_Label.setGeometry(QtCore.QRect(10, 80, 381, 16))
        self.shortLink_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.shortLink_Label.setObjectName("shortLink_Label")
        self.longLink = QtWidgets.QTextEdit(AnonUploadR)
        self.longLink.setGeometry(QtCore.QRect(10, 50, 381, 16))
        self.longLink.setAlignment(QtCore.Qt.AlignCenter)
        self.longLink.setObjectName("longLink")
        self.shortLink = QtWidgets.QTextEdit(AnonUploadR)
        self.shortLink.setGeometry(QtCore.QRect(10, 110, 381, 16))
        self.shortLink.setAlignment(QtCore.Qt.AlignCenter)
        self.shortLink.setObjectName("shortLink")
        self.uploadFile = QtWidgets.QPushButton(AnonUploadR)
        self.uploadFile.setGeometry(QtCore.QRect(220, 150, 171, 23))
        self.uploadFile.setObjectName("uploadFile")
        self.shortLink.setTabChangesFocus(False)
        self.longLink.setTabChangesFocus(False)
        self.shortLink.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.longLink.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.longLink.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shortLink.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.shortLink.setReadOnly(True)
        self.longLink.setReadOnly(True)
        self.retranslateUi(AnonUploadR)
        QtCore.QMetaObject.connectSlotsByName(AnonUploadR)


    def open_file(self):
        self.statusLabel.setText("Status : Waiting")
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(None, "Open", "", "All *.*")
        if self.file_name[0] != '':
            self.file_path = self.file_name[0]
            self.statusLabel.setText(f"Status : {self.file_path} ")

    def upload_file(self):
        try:
            self.statusLabel.setText("Status : Uploading")
            upload = anon.upload(self.file_path, progressbar=True)
            self.longLink.setText(upload.url.geturl())
            link = upload.url.geturl()
            splitLink = link.split("/")
            newLink = f"https://anonfiles.com/{splitLink[3]}"
            self.shortLink.setText(newLink)
            self.statusLabel.setText("Status : Complete")
            self.statusLabel.setText("Status : Idle")
        except:
            self.statusLabel.setText("Status : Failed")


    def retranslateUi(self, AnonUploadR):
        _translate = QtCore.QCoreApplication.translate
        AnonUploadR.setWindowTitle(_translate("AnonUploadR", "AnonUploadR"))
        self.openFile.setText(_translate("AnonUploadR", "Browse"))
        self.longLink_Label.setText(_translate("AnonUploadR", "Download Link Extended "))
        self.shortLink_Label.setText(_translate("AnonUploadR", "Download Link Short"))
        self.longLink.setText(_translate("AnonUploadR", "none"))
        self.shortLink.setText(_translate("AnonUploadR", "none"))
        self.uploadFile.setText(_translate("AnonUploadR", "Upload"))
        self.openFile.clicked.connect(self.open_file)
        self.uploadFile.clicked.connect(self.upload_file)

if __name__ == "__main__":
    anon = AnonFile()
    app = QtWidgets.QApplication(sys.argv)
    AnonUploadR = QtWidgets.QWidget()
    ui = Ui_AnonUploadR()
    ui.setupUi(AnonUploadR)
    AnonUploadR.show()
    sys.exit(app.exec_())
