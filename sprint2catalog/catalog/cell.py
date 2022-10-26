import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from detail_window import DetailWindow

class Cell(Gtk.EventBox):
    
    def __init__(self, name, description, image):
        super().__init__()
        self.name = name
        self.description = description
        self.image = image
        
        #Creo la box con la imagen y un label(nombre)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(Gtk.Label(label=name), False, False, 0)
        box.pack_start(image, True, True, 0)
        self.add(box)
        self.connect("button-release-event", self.on_click)
        
    # método que le pasa al label y este a su vez al detail window cuando se vuelve a clicar en la imagen
    def on_click(self, widget, event):
        image = Gtk.Image()
        image.set_from_pixbuf(self.image.get_pixbuf())
        
        name = Gtk.Label(label=self.name)
        description = Gtk.Label(label=self.description)
        dwin= DetailWindow(image, name, description, self.name)
        dwin.show_all()
        
