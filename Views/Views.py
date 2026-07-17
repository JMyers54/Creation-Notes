from PySide6.QtWidgets import QWidget, QLabel, QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QTextEdit, QStackedWidget
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from Views.Styles import TemaOscuro

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
        self.setStyleSheet(TemaOscuro)

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

        #Layout principal: vertical -> [Barra superior | resto]
        Layout = QVBoxLayout()
        Layout.setContentsMargins(11,11,11,11)
        Layout.setSpacing(11)
        
        #barra Superior
        Barrasuperior = QHBoxLayout()
        self.LabelNombreArchivo = QLabel("Sin titulo")
        self.BotonToggle = QPushButton()
        self.BotonToggle.setIcon(QIcon("Utils/Icons/Barra.png"))  # Replace "icon.png" with the actual icon file path
        self.BotonToggle.setIconSize(QSize(30, 20))
        self.BotonToggle.setFixedWidth(30)
        Barrasuperior.addWidget(self.BotonToggle)
        Barrasuperior.addWidget(self.LabelNombreArchivo)
        Barrasuperior.addStretch()
        
        # --- Fila Inferior---
        FilaInferior = QHBoxLayout()

        BarraLateral = QVBoxLayout()
        BarraLateral.setContentsMargins(4,4,4,4)
        BarraLateral.setSpacing(4)

        self.BotonGuardar = QPushButton()
        self.BotonGuardar.setIcon(QIcon("Utils/Icons/Guardar.png"))  # Replace "icon.png" with the actual icon file path
        self.BotonGuardar.setIconSize(QSize(20, 20))
        self.BotonGuardar.setFixedWidth(30)
        self.BotonVolver = QPushButton()
        self.BotonVolver.setIcon(QIcon("Utils/Icons/Volver.png"))  # Replace "icon.png" with the actual icon file path 
        self.BotonVolver.setIconSize(QSize(20, 20)) 
        self.BotonVolver.setFixedWidth(30)
        self.BotonNuevaCarpeta = QPushButton()
        self.BotonNuevaCarpeta.setIcon(QIcon("Utils/Icons/NuevaCarpeta.png"))  # Replace "icon.png" with the actual icon file path 
        self.BotonNuevaCarpeta.setIconSize(QSize(20, 20)) 
        self.BotonNuevaCarpeta.setFixedWidth(30)
        self.BotonEliminar = QPushButton()
        self.BotonEliminar.setIcon(QIcon("Utils/Icons/Basura.png"))  # Replace "icon.png" with the actual icon file path 
        self.BotonEliminar.setFixedWidth(30)
        self.BotonEliminar.setIconSize(QSize(20, 20))


        BarraLateral.addWidget(self.BotonGuardar)
        BarraLateral.addWidget(self.BotonVolver)
        BarraLateral.addWidget(self.BotonNuevaCarpeta)
        BarraLateral.addWidget(self.BotonEliminar)
        BarraLateral.addStretch()
        
        self.ContenedorBarra = QWidget()
        self.ContenedorBarra.setLayout(BarraLateral)
        self.ContenedorBarra.setFixedWidth(50)

        self.EditarNotas = QTextEdit()

        FilaInferior.addWidget(self.ContenedorBarra)
        FilaInferior.addWidget(self.EditarNotas,stretch=1)


        Layout.addLayout(Barrasuperior)
        Layout.addLayout(FilaInferior, stretch=1)

        Widget.setLayout(Layout)
        return Widget
    
    def ActivarEdicion(self,contenido=""):
        self.ContenidoSeguro = str(contenido)
        self.EditarNotas.setPlainText(self.ContenidoSeguro)
        self.stack.setCurrentWidget(self.pantallaEdicion)