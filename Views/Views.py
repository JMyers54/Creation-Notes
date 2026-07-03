from PySide6.QtWidgets import QWidget, QLabel, QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QTextEdit, QStackedWidget
from PySide6.QtCore import Qt


class WidgetPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()

        self.pantallaMenu = self.CrearPantallaMenu()
        self.pantallaEdicion = self.CrearPantallaEdicion()

        self.stack.addWidget(self.pantallaMenu)
        self.stack.addWidget(self.pantallaEdicion)

        layoutPrincipal = QVBoxLayout()
        layoutPrincipal.addWidget(self.stack)
        self.setLayout(layoutPrincipal)

    def CrearPantallaMenu(self):
        Widget = QWidget()
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0,150,0,0)
        layout.setSpacing(20)

        self.NombreApp = QLabel("New Note")
        self.LabelNuevo = QLabel("Nuevo Archivo")
        self.Label1 = QLabel("Abrir Archivo")

        self.BotonNuevo = QPushButton("Nuevo Archivo")
        self.BotonNuevo.setFixedWidth(150)

        self.BotonAbrir = QPushButton("Abrir Archivo")
        self.BotonAbrir.setFixedWidth(150)

        layout.addWidget(self.LabelNuevo, 1, 1, Qt.AlignCenter)
        layout.addWidget(self.BotonNuevo, 2, 1)
        layout.addWidget(self.Label1,3,1,Qt.AlignCenter)
        layout.addWidget(self.BotonAbrir,4,1)

        Widget.setLayout(layout)
        return Widget
    
    def CrearPantallaEdicion(self):
        Widget = QWidget()
        Layout = QVBoxLayout()
        Layout.setContentsMargins(10,10,10,10)
        Layout.setSpacing(10)

    # --- Fila superior: solo el botón Guardar, alineado a la derecha ---
        BarraSuperior = QHBoxLayout()
        self.BotonGuardar = QPushButton("Guardar")
        self.BotonGuardar.setFixedWidth(150)

        self.BotonVolver = QPushButton("Volver")
        self.BotonVolver.setFixedWidth(150)

        self.BotonCrear = QPushButton("Nuevo Archivo")
        self.BotonCrear.setFixedWidth(150)

        BarraSuperior.addStretch()

        BarraSuperior.addWidget(self.BotonGuardar)
        BarraSuperior.addWidget(self.BotonVolver)
        BarraSuperior.addWidget(self.BotonCrear)

        self.EditarNotas = QTextEdit()
        Layout.addLayout(BarraSuperior)
        Layout.addWidget(self.EditarNotas, stretch=1)

        Widget.setLayout(Layout)
        return Widget
    
    def ActivarEdicion(self,contenido=""):
        self.ContenidoSeguro = str(contenido)
        self.EditarNotas.setPlainText(self.ContenidoSeguro)
        self.stack.setCurrentWidget(self.pantallaEdicion)