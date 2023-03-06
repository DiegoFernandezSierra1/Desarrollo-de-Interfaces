import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from load_window import LoadWindow

class MainWindow(Gtk.Window):
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    label = Gtk.Label("Juegos más esperados")
    button = Gtk.Button(label="Listar videojuegos")

    def __init__(self) -> None:
        super().__init__(title="Juegos esperados")
        self.connect("destroy",Gtk.main_quit)
        self.set_default_size(300,200)
        self.button.connect("clicked",self.on_button_clicked)
        self.add(self.box)
        self.box.pack_start(self.label,True,False,0)
        self.box.pack_start(self.button,True,False,0)
    #Boton que cuando es clicado te manda a la pantalla de carga de los videojuegos
    def on_button_clicked(self,widget):
        win=LoadWindow()
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()