import os

class ControladorNotas():
    def __init__(self, vista, modelo):
        self.vista =vista
        self.modelo = modelo

        self.vista.BotonAbrir.clicked.connect(self.abrirArchivoLogica)
        self.vista.BotonGuardar.clicked.connect(self.GuardarArchivoLogica)
        self.vista.BotonVolver.clicked.connect(self.VolverArchivoLogica)
        self.vista.BotonNuevo.clicked.connect(self.CrearArchivoLogica)
        self.vista.BotonToggle.clicked.connect(self.BotonBarraLogica)
        self.rutaActual = None
    
    def abrirArchivoLogica(self):
        ruta,contenido = self.modelo.AbrirArchivo()
        if contenido is not None:
            self.rutaActual = ruta
            self.vista.ActivarEdicion(contenido)    
            self.vista.LabelNombreArchivo.setText(os.path.basename(ruta))  # Update the label with the file name

    def GuardarArchivoLogica(self):
        texto = self.vista.EditarNotas.toPlainText()
        ruta = self.modelo.GuardarArchivo(self.rutaActual, texto)
        if ruta is not None:
            self.rutaActual = ruta
    
    def VolverArchivoLogica(self):
        #setCurrentWidget habre un widget en este caso le decimos que habra el anterior 
        #haciendo el efecto de volver
        self.vista.LabelNombreArchivo.setText("Sin Titulo")  # Clear the label when going back
        self.vista.stack.setCurrentWidget(self.vista.pantallaMenu)

    def CrearArchivoLogica(self):
        self.rutaActual = None
        self.vista.ActivarEdicion("")
    
    def BotonBarraLogica(self):
        if self.vista.ContenedorBarra.isVisible():
            self.vista.ContenedorBarra.hide()
        else:
            self.vista.ContenedorBarra.show()