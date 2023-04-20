def classFactory(iface):
    from .plugin_core import PluginCore
    return PluginCore(iface)