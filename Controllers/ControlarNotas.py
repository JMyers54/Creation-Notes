

class ControladorNotas():
    def __init__(self, vista, modelo):
        self.vista =vista
        self.modelo = modelo

        self.vista.BotonAbrir.clicked.connect(self.abrirArchivoLogica)
        self.vista.BotonGuardar.clicked.connect(self.GuardarArchivoLogica)
        self.vista.BotonVolver.clicked.connect(self.VolverArchivoLogica)
        self.vista.BotonCrear.clicked.connect(self.CrearArchivoLogica)
        self.vista.BotonNuevo.clicked.connect(self.CrearArchivoLogica)
        self.rutaActual = None
    
    def abrirArchivoLogica(self):
        ruta,contenido = self.modelo.AbrirArchivo()
        if contenido is not None:
            self.rutaActual = ruta
            self.vista.ActivarEdicion(contenido)    

    def GuardarArchivoLogica(self):
        texto = self.vista.EditarNotas.toPlainText()
        ruta = self.modelo.GuardarArchivo(self.rutaActual, texto)
        if ruta is not None:
            self.rutaActual = ruta
    
    def VolverArchivoLogica(self):
        #setCurrentWidget habre un widget en este caso le decimos que habra el anterior 
        #haciendo el efecto de volver
        self.vista.stack.setCurrentWidget(self.vista.pantallaMenu)

    def CrearArchivoLogica(self):
        self.rutaActual = None
        self.vista.ActivarEdicion("")