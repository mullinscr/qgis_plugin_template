"""
Example of a ui controller file. Here you will connect the slots and signals
necessary for the desired functionality, and add any necessary additional ui
methods.

Note: QDialog should be replaced with QDockWidget if that is what is being
developed.

"""

from pathlib import Path

from qgis.PyQt.uic import loadUiType
from qgis.PyQt.QtWidgets import QDialog

FORM_CLASS, _ = loadUiType(Path(__file__).parent / 'your_ui_file.ui')

class GenericUI(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(GenericUI, self).__init__(parent)
        self.setupUi(self)