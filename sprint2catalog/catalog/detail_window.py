import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DetailWindow(Gtk.Window):
    
    #Una ventana que coge la imagen junto con el label y lo muestra en una ventana nueva
    def __init__(self, image, name, description, title):
        super().__init__(title=title)
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        self.set_border_width(15)
        self.set_default_size(200, 200)
        self.set_position(Gtk.WindowPosition.CENTER)

        box.pack_start(image, True, True, 0)

        box.pack_start(name, True, True, 0)

        box.pack_start(description, True, True, 0)

        self.add(box)
