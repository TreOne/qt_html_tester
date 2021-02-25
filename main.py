# coding=utf-8
import sys

from PyQt4.QtGui import QApplication, QMainWindow, QWidget

from previewer_ui import Ui_Form


class Previewer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Previewer, self).__init__(parent)
        self.setupUi(self)

    def on_previewButton_clicked(self):
        text = self.plainTextEdit.toPlainText()
        self.webView.setHtml(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(u'HTML Tester by TreOne')
        self.centralWidget = Previewer(self)
        self.setCentralWidget(self.centralWidget)
        self.setStartupText()

    def setStartupText(self):
        html = u"""<html>
<body>
<head>
  <title>Пример HTML кода</title>
</head>
<h1>HTML Tester</h1>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quis bibendum elit, eget venenatis nisl. Quisque vitae nibh eu justo congue pulvinar. Nam lobortis finibus diam id aliquam.</p>
<table border = 1 cellspacing="0" cellpadding="1" width = '100%'>
  <tr>
    <td align='center' width = '15%'><b>Код</b></td>
    <td align='center' width = '75%'><b>Наименование</b></td>
    <td align='center' width = '10%'><b>Количество</b></td>
  </tr>
  <tr>
    <td align='center'><i>001</i></td>
    <td align='left'>Тест A</td>
    <td align='center'>10</td>
  </tr>
  <tr>
    <td align='center'><i>002</i></td>
    <td align='left'>Тест Б</td>
    <td align='center'>25</td>
  </tr>
  <tr>
    <td align = 'center' colspan='2' ><b>ИТОГО</b></td>
    <td align = 'center'><b>35</b></td>
  </tr>
</table>
</body>
</html>"""
        self.centralWidget.plainTextEdit.setPlainText(html)
        self.centralWidget.webView.setHtml(html)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
