import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela(QMainWindow):
    def __init__ (self):
          super ().__init__()

          self.topo = 100
          self.esquerda = 100
          self.largura = 800
          self.altura = 600
          self.titulo = 'Menor distância'

          self.caixatexto = QLineEdit(self)
          self.caixatexto.move(35,50)
          self.caixatexto.resize(200, 30)

          self.caixatexto2 = QLineEdit(self)
          self.caixatexto2.move(500, 50)
          self.caixatexto2.resize(200, 30)

          self.label_1 = QLabel(self)
          self.label_1.setText("Digite a Origem:")
          self.label_1.move(35, 5)
          self.label_1.resize(300, 50)
          self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #FF0000}')

          self.label_2 = QLabel(self)
          self.label_2.setText("Digite o Destino:")
          self.label_2.move(500, 5)
          self.label_2.resize(300, 50)
          self.label_2.setStyleSheet('QLabel {font:bold; font-size:25px; color: #FF0000}')

          self.labelcaixa = QLabel(self)
          self.labelcaixa.setText("Rota: ")
          self.labelcaixa.move(350, 75)
          self.labelcaixa.resize(300, 50)
          self.labelcaixa.setStyleSheet('QLabel {font:bold; font-size:25px; color: #FF0000}')

          botao1 = QPushButton('Calcular', self)
          botao1.move(350, 500)
          botao1.resize(110, 50)
          botao1.setStyleSheet('QPushButton {background-color: #66CCFF; font:bold; font-size: 13px}')
          botao1.clicked.connect(self.botao1_click)

          self.cidades = QLabel(self)
          self.cidades.move(110, 70)
          self.cidades.resize(700, 500)
          self.cidades.setPixmap(QtGui.QPixmap('Cidades.png'))


          self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText("O botão 1 ta clicado")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #543073}')
        self.carro.setPixmap(QtGui.QPixmap('Mars.png'))


    def botao2_click(self):
        self.label_1.setText("O botão 2 ta clicado")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color: #543073}')
        self.carro.setPixmap(QtGui.QPixmap('Mars.png'))

    def mostratexto(self):
        conteudo = self.caixatexto.text()
        self.labelcaixa.setText('Digitou: ' + conteudo)




aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())

