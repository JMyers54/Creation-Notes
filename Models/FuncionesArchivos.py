from PySide6.QtWidgets import QFileDialog

class FuncionesArchivos():
    def __init__(self):
        pass
    
    def AbrirArchivo(self):
        # cuando utilice QfileDialog debo declara dos variables para los valores que devuelve la libreria
        ruta, file = QFileDialog.getOpenFileName(None,"Abrir Archivo","Documentos (*.txt *.docx)")

        if ruta:
            # "r" significa leer, encoding("utf-8") se utiliza para caractese en español
            with open(ruta, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
                return ruta, contenido
        return None,None
    
    def GuardarArchivo(self, ruta, texto):

        if ruta is None:
            ruta, file = QFileDialog.getSaveFileName(None,"Guardar Archivo","Documentos (*.txt *.docx)")
            if not ruta:
                return None
            
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(texto)
        
        return ruta