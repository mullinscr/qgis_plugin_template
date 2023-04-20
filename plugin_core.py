"""
Loads the plugin into QGIS.
"""


class PluginCore:
    def __init__(self, iface):
        self.iface = iface
        self.actions = [] # Not needed for QGIS, just used in the `unload` method.
        self.menu_item = 'Plugin Name'

    def initGui(self):
        """
        Add the necessary QActions to the toolbar and menu and connect the signals
        to the relevant ui / methods.

        Example:

        self.toolbar = self.iface.addToolBar('Your toolbar')

        icon = QIcon('path/to/icon')
        self.action_one = QAction(icon, 'Action Name', self.iface.mainWindow())
        self.action_one.triggered.connect(self.method_to_call)
        self.toolbar.addAction(self.action_one)
        self.actions.append(self.action_one)
        self.iface.addPluginToMenu(self.menu_item, self.action_one)
        """
        pass

    def unload(self):
        """
        Will likely want to remove the added toolbar actions and menu items.

        Example:

        for action in self.actions:
            self.iface.removePluginMenu(self.menu_item, action)
            self.toolbar.removeAction(action)

        del self.toolbar
        """
        pass