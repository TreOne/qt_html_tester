# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'previewer.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(911, 688)
        self.horizontalLayout_4 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.editorBox = QtGui.QGroupBox(self.splitter)
        self.editorBox.setObjectName(_fromUtf8("editorBox"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.editorBox)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.editorBox)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.clearButton = QtGui.QPushButton(self.editorBox)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.horizontalLayout.addWidget(self.clearButton)
        self.previewButton = QtGui.QPushButton(self.editorBox)
        self.previewButton.setObjectName(_fromUtf8("previewButton"))
        self.horizontalLayout.addWidget(self.previewButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.previewerBox = QtGui.QGroupBox(self.splitter)
        self.previewerBox.setObjectName(_fromUtf8("previewerBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.previewerBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.webView = QtWebKit.QWebView(self.previewerBox)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.horizontalLayout_3.addWidget(self.webView)
        self.horizontalLayout_4.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.clearButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "HTML Tester", None))
        self.editorBox.setTitle(_translate("Form", "HTML код", None))
        self.clearButton.setText(_translate("Form", "Очистить", None))
        self.previewButton.setText(_translate("Form", "Просмотр (F5)", None))
        self.previewButton.setShortcut(_translate("Form", "F5", None))
        self.previewerBox.setTitle(_translate("Form", "Результат", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

