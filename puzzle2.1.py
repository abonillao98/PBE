import Lcd
import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk

class Finestra(Gtk.Window):

    def __init__(self):
        self.lcd = Lcd.Lcd()

        # Creem finestra
        Gtk.Window.__init__(self, title = "Puzzle2 LCD")
        Gtk.Window.set_default_size(self,200, 100)
        self.connect("destroy", Gtk.main_quit)
        self.set_border_width(5)
        self.set_resizable(False)

        # Caixa principal

        self.principal = Gtk.Box(orientation = "vertical")
        self.add(self.principal)

        # Caixa per introduir text

        self.input = Gtk.TextView()
        self.input.set_size_request(80,80)

        # Caixa pel boton
        
        self.boton = Gtk.Button(label = "Display")
        self.boton.connect("clicked", self.sendLcd)
        #
        self.principal.pack_start(self.input,False,False,0)
        self.principal.add(self.boton)

    def sendLcd(self, widget):
        start_iter = self.input.get_buffer().get_start_iter()
        end_iter = self.input.get_buffer().get_end_iter()
        text = self.input.get_buffer().get_text(start_iter, end_iter, True)
        self.lcd.printLcd(text)


finestra = Finestra()
finestra.show_all()
Gtk.main()
