import gi
import requests, threading, shutil
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib,GdkPixbuf
from window import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk. Label( "Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.Orientation. VERTICAL, spacing=20)
    
    def __init__(self):
        super().__init__(title="")
        self. connect("destroy", Gtk.main_quit)
        self.set_border_width(60)
        self.set_resizable(False)
        self.spinner.props.active = True
        self.set_position(Gtk.WindowPosition.CENTER)
        
        #Creacion de una box con un spinner y un label descriptivo
        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)
        self.launch_load()
        
    def start_main_window(self, loaded_items_list):
        win = MainWindow(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()

    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()
        
    #Funcion para extraer del catalog.json los nombres, descripciones y urls de imagenes y crea una imagen temporal para ser usada
    def load_json(self):
        response = requests.get("https://raw.githubusercontent.com/CarlosAfundacion/EXAMEN/main/games.json")
        json_list = response.json()
        
        result = []
        
        for json_item in json_list:
            nombre = json_item.get("nombre")
            descripcion = json_item.get("descripcion")
            imagen_url = json_item.get("imagen_url")
            r = requests.get(imagen_url, stream=True)
            with open("temp.png","wb") as f:
                shutil.copyfileobj(r.raw, f)
            imagen_url = Gtk.Image.new_from_file("temp.png")
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("temp.png", 300, 300, False)
            imagen_url.set_from_pixbuf(pixbuf)
            result.append({"nombre": nombre, "descripcion": descripcion, "gtk_image": imagen_url})

        GLib.idle_add(self.start_main_window, result)
        
        

