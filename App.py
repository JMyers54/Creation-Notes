from PySide6.QtWidgets import QApplication
from Views.Views import WidgetPrincipal
from Models.FuncionesArchivos import FuncionesArchivos
from Controllers.ControlarNotas import ControladorNotas


def main():
        app = QApplication([])
        vista = WidgetPrincipal()
        vista.setWindowTitle("New Note")
        vista.resize(500,500)
        modelo = FuncionesArchivos()
        controlador = ControladorNotas(vista, modelo)

        vista.show()   
        app.exec()
if __name__ == "__main__":
        main()