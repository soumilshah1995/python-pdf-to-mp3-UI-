# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Audiov2.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import requests
from PyQt5 import QtWidgets
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import PyPDF2

class Ui_Audio(object):
    def setupUi(self, Audio):
        Audio.setObjectName("Audio")
        Audio.resize(592, 434)
        self.textBrowser = QtWidgets.QTextBrowser(Audio)
        self.textBrowser.setGeometry(QtCore.QRect(60, 10, 461, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.txt_write = QtWidgets.QTextEdit(Audio)
        self.txt_write.setGeometry(QtCore.QRect(60, 100, 451, 151))
        self.txt_write.setObjectName("txt_write")

        self.gridLayoutWidget = QtWidgets.QWidget(Audio)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 260, 451, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.btn_choosefile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_choosefile.setStyleSheet("\n"
                                          "font: 14pt \".SF NS Text\";")
        self.btn_choosefile.setObjectName("btn_choosefile")
        self.gridLayout.addWidget(self.btn_choosefile, 0, 1, 1, 1)

        self.txt_pdf_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_pdf_name.setObjectName("txt_pdf_name")

        self.gridLayout.addWidget(self.txt_pdf_name, 0, 0, 1, 1)

        self.btn_download_mp3_pdf = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_download_mp3_pdf.setStyleSheet("\n"
                                                "font: 14pt \".SF NS Text\";")
        self.btn_download_mp3_pdf.setObjectName("btn_download_mp3_pdf")
        self.gridLayout.addWidget(self.btn_download_mp3_pdf, 0, 2, 1, 1)
        self.txt_name_text = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_name_text.setObjectName("txt_name_text")
        self.gridLayout.addWidget(self.txt_name_text, 1, 0, 1, 1)
        self.btn_download_text = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_download_text.setStyleSheet("\n"
                                             "font: 14pt \".SF NS Text\";")
        self.btn_download_text.setObjectName("btn_download_text")
        self.gridLayout.addWidget(self.btn_download_text, 1, 1, 1, 2)

        self.retranslateUi(Audio)
        QtCore.QMetaObject.connectSlotsByName(Audio)


    def retranslateUi(self, Audio):
        _translate = QtCore.QCoreApplication.translate
        Audio.setWindowTitle(_translate("Audio", "Form"))
        self.textBrowser.setHtml(_translate("Audio", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Welcome to Text/PDF to Audio Converter Software</span></p>\n"
                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>"))
        self.txt_write.setHtml(_translate("Audio", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Type your text here</p></body></html>"))
        self.btn_choosefile.setText(_translate("Audio", "Choose PDF File"))
        self.txt_pdf_name.setText(_translate("Audio", "Namefille"))
        self.btn_download_mp3_pdf.setText(_translate("Audio", "Download MP3"))
        self.txt_name_text.setText(_translate("Audio", "Namefille"))
        self.btn_download_text.setText(_translate("Audio", "Download MP3 File"))

        # BUTTON HANDLERS
        self.btn_choosefile.clicked.connect(self.btn_choosefile_handler)
        self.btn_download_mp3_pdf.clicked.connect(self.btn_download_mp3_pdf_handler)
        self.btn_download_text.clicked.connect(self.btn_download_text_handler)


    def btn_choosefile_handler(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]


    def btn_download_mp3_pdf_handler(self):

        self.path
        self.txt_pdf_name

        pdfFileObj = open(self.path, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        mytext = ""

        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            mytext += pageObj.extractText()

        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }

        url = 'https://text-to-speech-demo.ng.bluemix.net/api/v1/synthesize?t'

        params= {
            'text': 'hello everyone i am going to teach you python',
            'voice': 'en-US_AllisonV2Voice',
            'download': True,
            'accept': 'audio/mp3'
        }

        params['text'] = mytext

        response = requests.get(url, headers=headers,params=params)

        with open('{}.mp3'.format(self.txt_pdf_name.text()),'wb') as f:
            f.write(response.content)

        self.pop_message("Download Complete ")


    def btn_download_text_handler(self):

        txt_name_file_v = self.txt_name_text.text()
        txt_write_v = self.txt_write.toPlainText()

        headers = {
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Referer': 'http://www.wikipedia.org/',
            'Connection': 'keep-alive',
        }
        url = 'https://text-to-speech-demo.ng.bluemix.net/api/v1/synthesize?t'
        params= {
            'text': 'hello everyone i am going to teach you python',
            'voice': 'en-US_AllisonV2Voice',
            'download': True,
            'accept': 'audio/mp3'
        }

        params['text'] = txt_write_v
        response = requests.get(url, headers=headers,params=params)

        with open('{}.mp3'.format(txt_name_file_v),'wb') as f:
            f.write(response.content)

        self.pop_message("Download Complete ")



    def pop_message(self,text):

        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Audio = QtWidgets.QWidget()
    ui = Ui_Audio()
    ui.setupUi(Audio)
    Audio.show()
    sys.exit(app.exec_())