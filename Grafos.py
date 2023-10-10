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

          calcular = QPushButton('Calcular', self)
          calcular.move(350, 500)
          calcular.resize(110, 50)
          calcular.setStyleSheet('QPushButton {background-color: #66CCFF; font:bold; font-size: 13px}')
          calcular.clicked.connect(self.mostra_rota)

          self.origemlabel = QLineEdit(self)
          self.origemlabel.move(35, 50)
          self.origemlabel.resize(200, 30)

          self.destinolabel = QLineEdit(self)
          self.destinolabel.move(500, 50)
          self.destinolabel.resize(200, 30)

          self.origem = QLabel(self)
          self.origem.setText("Origem:")
          self.origem.move(35, 5)
          self.origem.resize(300, 50)
          self.origem.setStyleSheet('QLabel {font:bold; font-size:25px; color: #000000}')

          self.destino = QLabel(self)
          self.destino.setText("Destino:")
          self.destino.move(500, 5)
          self.destino.resize(300, 50)
          self.destino.setStyleSheet('QLabel {font:bold; font-size:25px; color: #000000}')

          self.rota = QLabel(self)
          self.rota.setText("Rota: ")
          self.rota.move(5, 95)
          self.rota.resize(900, 40)
          self.rota.setStyleSheet('QLabel {font:bold; font-size:15px; color: #000000}')

          self.cidades = QLabel(self)
          self.cidades.move(110, 150)
          self.cidades.resize(600, 300)
          self.cidades.setPixmap(QtGui.QPixmap('Cidades.png'))

          self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def mostra_rota(self):
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Centralina' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina. 40Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Capinópolis, Ituiutaba. 30Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Itumbiara' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Itumbiara. 60Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Tapaciguara' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Itumbiara. 115Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Monte Alegre de Minas' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas. 115Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Douradinhos' :
            self.rota.setText("A menor rota é: Capinópolis, Ituiutaba, Douradinhos. 120Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Uberlândia' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas, Uberlândia. 175Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Araguari' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Itumbiara, Tapaciguara, Uberlândia, Araguari. 205Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Cascalho Rico' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Itumbiara, Tapaciguara, Uberlândia, Araguari, Cascalho Rico.\n233Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Indianópolis' :
            self.rota.setText("A menor rota é: Capinópolis, Ituiutaba, Monte Alegre de Minas, Uberlândia, Indianópolis. 220Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Grupiara' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas, Uberlândia, Araguari, Cascalho Rico,\nGrupiara. 265Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Estrela do Sul' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas, Uberlândia, Araguari, Estrela do Sul.\n239Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'Romaria' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas, Uberlândia, Romaria. 253Km.")
        if self.origemlabel.text() == 'Capinópolis' and self.destinolabel.text() == 'São Juliana' :
            self.rota.setText("A menor rota é: Capinópolis, Centralina, Monte Alegre de Minas, Uberlândia, Indianópolis, São Juliana.\n260Km.")

        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Ituiutaba, Capinópolis. 30Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Itumbiara' :
            self.rota.setText("A menor rota é: Ituiutaba, Capinópolis, Centralina, Itumbiara. 90Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Centralina' :
            self.rota.setText("A menor rota é: Ituiutaba, Capinópolis, Centralina. 70Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Tupaciguara' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Tupaciguara. 129Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Monte Alegre de Minas' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas. 85Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Douradinhos' :
            self.rota.setText("A menor rota é: Ituiutaba, Douradinhos. 90Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Uberlândia' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia. 145Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Araguari' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Araguari. 175Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Cascalho Rico' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Araguari, Cascalho Rico. 203Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Indianópolis' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Indianópolis. 190Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Araguari, Grupiara. 235Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Estrela do Sul' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Araguari, Estrela do Sul . 209Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'Romaria' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Romaria. 233Km")
        if self.origemlabel.text() == 'Ituiutaba' and self.destinolabel.text() == 'São Juliana' :
            self.rota.setText("A menor rota é: Ituiutaba, Monte Alegre de Minas, Uberlândia, Indianópolis, São Juliana. 230Km")

        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Itumbiara, Centralina, Capinópolis. 60Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Itumbiara, Centralina, Capinópolis. 60Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Itumbiara, Centralina. 20Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara. 55Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Itumbiara, Centralina, Monte Alegre de Minas. 95Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Itumbiara, Centralina, Monte Alegre de Minas, Douradinhos. 123Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia. 115Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Araguari. 145Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Araguari, Cascalho Rico. 173Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Indianópolis. 160Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Araguari, Cascalho Rico, Grupiara. 205Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Araguari, Estrela do Sul. 179Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Romaria. 193Km")
        if self.origemlabel.text() == 'Itumbiara' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Itumbiara, Tupaciguara, Uberlândia, Indianópolis, São Juliana. 200Km")

        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Centralina, Capinópolis. 40Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Centralina, Capinópolis, Ituiutaba. 70Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Centralina, Itumbiara. 20Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara. 75Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Centralina, Monte Alegre de Minas. 75Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Centralina, Monte Alegre de Minas, Douradinhos. 103Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia. 135Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Araguari. 165Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Araguari, Cascalho Rico. 193Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Indianópolis. 180Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Centralina Itumbiara, Tupaciguara, Uberlândia, Araguari, Cascalho Rico, Grupiara. 225Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Araguari, Estrela do Sul. 199Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Romaria. 213Km")
        if self.origemlabel.text() == 'Centralina' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Centralina, Itumbiara, Tupaciguara, Uberlândia, Indianópolis, São Juliana. 220Km")

        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Tupaciguara, Centralina, Capinópolis. 115Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Tupaciguara, Monte Alegre de Minas, Ituiutaba. 129Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Tupaciguara, Itumbiara. 55Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Tupaciguara, Itumbiara, Centralina. 75Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Tupaciguara, Monte Alegre de Minas. 44Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Tupaciguara, Monte Alegre de Minas, Douradinhos. 72Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia. 60Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Araguari. 90Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Araguari, Cascalho Rico. 118Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Indianópolis. 105Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Araguari, Cascalho Rico, Grupiara. 150Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Araguari, Estrela do Sul. 124Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Romaria. 138Km")
        if self.origemlabel.text() == 'Tupaciguara' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Tupaciguara, Uberlândia, Indianópolis, São Juliana. 145Km")

        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Centralina, Capinópolis. 115Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Ituiutaba. 85Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Centralina, Itumbiara. 95Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Centralina. 75Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Tupaciguara. 44Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Douradinhos. 28Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia. 60Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Araguari. 90Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Araguari, Cascalho Rico. 118Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Indianópolis. 105Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Araguari, Cascalho Rico, Grupiara. 150Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Araguari, Estrela do Sul. 124Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Romaria. 138Km")
        if self.origemlabel.text() == 'Monte Alegre de Minas' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Monte Alegre de Minas, Uberlândia, Indianópolis, São Juliana. 145Km")

        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Douradinhos, Ituiutaba, Capinópolis. 120Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Douradinhos, Ituiutaba. 90Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Douradinhos, Monte Alegre de Minas, Centralina, Itumbiara. 123Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Douradinhos, Monte Alegre de Minas, Centralina. 103Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Douradinhos, Monte Alegre de Minas, Tupaciguara. 72Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Douradinhos, Monte Alegre de Minas. 28Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia. 63Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Araguari. 93Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Araguari, Cascalho Rico. 121Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Indianópolis. 108Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Araguari, Cascalho Rico, Grupiara. 153Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Araguari, Estrela do Sul. 127Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Romaria. 141Km")
        if self.origemlabel.text() == 'Douradinhos' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Douradinhos, Uberlândia, Indianópolis, São Juliana. 148Km")

        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Uberlândia, Monte Alegre de Minas, Capinópolis. 135Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Uberlândia, Monte Alegre de Minas, Ituiutaba. 145Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Uberlândia, Tupaciguara, Itumbiara. 115Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Uberlândia, Monte Alegre de Minas, Centralina. 135Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Uberlândia, Tupaciguara. 60Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Uberlândia, Monte Alegre de Minas. 60Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Uberlândia, Douradinhos. 63Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Uberlândia, Araguari. 30Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Uberlândia, Araguari, Cascalho Rico. 58Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Uberlândia, Indianópolis. 45Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Uberlândia, Araguari, Cascalho Rico, Grupiara. 90Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Uberlândia, Araguari, Estrela do Sul. 64Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Uberlândia, Romaria. 78Km")
        if self.origemlabel.text() == 'Uberlândia' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Uberlândia, Indianópolis, São Juliana. 85Km")

        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Capinópolis' :
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 205Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Ituiutaba' :
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Monte Alegre de Minas, Ituiutaba. 175Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Tupaciguara, Itumbiara. 145Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Monte Alegre de Minas, Centralina. 165Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Tupaciguara. 90Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Monte Alegre de Minas. 90Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Douradinhos. 93Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Araguari, Uberlândia. 30Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Araguari, Cascalho Rico. 28Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Araguari, Uberlândia, Indianópolis. 75Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Araguari, Cascalho Rico, Grupiara. 60Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Araguari, Estrela do Sul. 34Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Araguari, Estrela do Sul, Romaria. 61Km")
        if self.origemlabel.text() == 'Araguari' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Araguari, Estrela do Sul, Romaria, São Juliana. 89Km")

        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Monte Alegre de Minas, Centralina, Capinópolis. 233Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Monte Alegre de Minas, Ituiutaba. 203Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Tupaciguara, Itumbiara. 173Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Monte Alegre de Minas, Centralina. 193Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Tupaciguara. 118Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Monte Alegre de Minas. 118Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Douradinhos. 121Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia. 58Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari. 28Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Uberlândia, Indianópolis. 103Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Cascalho Rico, Grupiara. 32Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Estrela do Sul. 62Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Estrela do Sul, Romaria. 89Km")
        if self.origemlabel.text() == 'Cascalho Rico' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Cascalho Rico, Araguari, Estrela do Sul, Romaria, São Juliana. 117Km")

        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 220Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Monte Alegre de Minas, Ituiutaba. 190Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Tupaciguara, Itumbiara. 160Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Monte Alegre de Minas, Centralina. 180Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Tupaciguara. 105Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Monte Alegre de Minas. 105Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Douradinhos. 108Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia. 45Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Araguari, Cascalho Rico. 103Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Indianópolis, Uberlândia, Araguari. 75Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Indianópolis, São Juliana, Romaria, Estrela, Grupiara. 133Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Indianópolis, São Juliana, Romaria, Estrela do Sul. 95Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Indianópolis, São Juliana, Romaria. 68Km")
        if self.origemlabel.text() == 'Indianópolis' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Indianópolis, São Juliana. 40Km")

        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Aragiari, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 265Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia, Monte Alegre de Minas, Ituiutaba. 235Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia, Tupaciguara, Itumbiara. 205Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Uberlândia, Monte Alegre de Minas, Centralina. 225Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia, Tupaciguara. 150Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia, Monte Alegre de Minas. 150Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia, Douradinhos. 153Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari, Uberlândia. 90Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico. 32Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Grupiara, Cascalho Rico, Araguari. 60Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Grupiara, Estrela do Sul, Romaria, São Juliana, Indianópolis. 133Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Grupiara, Estrela do Sul. 38Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Grupiara, Estrela do Sul, Romaria. 65Km")
        if self.origemlabel.text() == 'Grupiara' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Grupiara, Estrela do Sul, Romaria, São Juliana. 93Km")

        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 239Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Monte Alegre de Minas, Ituiutaba. 209Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Estrela do Sul, Uberlândia, Tupaciguara, Itumbiara. 179Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Monte Alegre de Minas, Centralina. 199Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Tupaciguara. 124Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Monte Alegre de Minas. 124Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia, Douradinhos. 127Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Uberlândia. 64Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari, Cascalho Rico. 62Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Estrela do Sul, Araguari. 34Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Estrela do Sul, Romaria, São Juliana, Indianópolis. 95Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Estrela do Sul, Grupiara. 38Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: Estrela do Sul, Romaria. 27Km")
        if self.origemlabel.text() == 'Estrela do Sul' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Estrela do Sul, Romaria, São Juliana. 55Km")

        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 253Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Monte Alegre de Minas, Ituiutaba. 233Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Tupaciguara, Itumbiara. 193Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Monte Alegre de Minas, Centralina. 213Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Tupaciguara. 138Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Monte Alegre de Minas. 138Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: Romaria, Uberlândia, Douradinhos. 141Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: Romaria, Uberlândia. 78Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: Romaria, Estrela do Sul, Araguari, Cascalho Rico. 89Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: Romaria, Estrela do Sul, Araguari. 61Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: Romaria, São Juliana, Indianópolis. 68Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Romaria, Estrela do Sul. 27Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: Romaria, Estrela do Sul, Grupiara. 65Km")
        if self.origemlabel.text() == 'Romaria' and self.destinolabel.text() == 'São Juliana':
            self.rota.setText("A menor rota é: Romaria, São Juliana. 28Km")

        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Capinópolis':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Monte Alegre de Minas, Centralina, Capinópolis. 260Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Ituiutaba':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Monte Alegre de Minas, Ituiutaba. 230Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Itumbiara':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Tupaciguara, Itumbiara. 200Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Centralina':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Monte Alegre de Minas, Centralina. 220Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Tupaciguara':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Tupaciguara. 145Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Monte Alegre de Minas':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Monte Alegre de Minas. 145Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Douradinhos':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia, Douradinhos. 148Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Uberlândia':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis, Uberlândia. 85Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Cascalho Rico':
            self.rota.setText("A menor rota é: São Juliana, Romaria, Estrela do Sul, Araguari, Cascalho Rico. 117Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Araguari':
            self.rota.setText("A menor rota é: São Juliana, Romaria, Estrela do Sul, Araguari. 89Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Indianópolis':
            self.rota.setText("A menor rota é: São Juliana, Indianópolis. 40Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Estrela do Sul':
            self.rota.setText("A menor rota é: Grupiara, Estrela do Sul. 38Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Romaria':
            self.rota.setText("A menor rota é: São Juliana, Romaria. 28Km")
        if self.origemlabel.text() == 'São Juliana' and self.destinolabel.text() == 'Grupiara':
            self.rota.setText("A menor rota é: São Juliana, Romaria, Estrela do Sul, Grupiara. 93Km")

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())