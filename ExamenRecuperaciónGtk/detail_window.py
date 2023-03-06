import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DetailWindow(Gtk.Window):
    
    #Una ventana con una box que coge la imagen y el label y lo muestra en una nueva ventana
    def __init__(self, image, nombre, descripcion,title):
        super().__init__(title=title)
        
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        
        self.set_border_width(15)
        self.set_default_size(200, 200)
        self.set_position(Gtk.WindowPosition.CENTER)

        box.pack_start(image, True, True, 0)

        box.pack_start(nombre, True, True, 0)

        box.pack_start(descripcion, True, True, 0)


        self.add(box)
