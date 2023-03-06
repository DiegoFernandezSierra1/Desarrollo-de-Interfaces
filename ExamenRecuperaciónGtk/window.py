import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell
from gi.repository import GdkPixbuf
class MainWindow (Gtk.Window) :
    
    vbox = Gtk.VBox(False, 2)
    
    def __init__(self, data_source):
        super().__init__ ( title = "Fotos")
        self.connect ("destroy" , Gtk.main_quit)
        self.set_border_width(15)
        self.set_default_size(500 , 500)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        header = Gtk.HeaderBar (title = "Lista de Juegos")
        header.set_subtitle ("2023")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        

        flowbox = Gtk.FlowBox()
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER , Gtk.PolicyType.AUTOMATIC)
        scrolled.add(flowbox)
        
        
        self.vbox.pack_start(scrolled, True, True, 0)
        
        self.add(self.vbox)
        
        #sacando los datos de la lista resultante de recorrer el json y crear imágenes con esos datos 
        #y creando una celda con cada imagen y nombre
        for item in data_source:
            cell = Cell(item.get("nombre"), item.get("descripcion"),item.get("gtk_image"))
            flowbox.add(cell)
            
 