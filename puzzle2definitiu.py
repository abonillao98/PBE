import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib, Gdk, GObject
import Lcd
import threading

class Lcd_TextViewWindow(Gtk.Window):
    def __init__(self):
        #Inicialitzacio i titol de la finestra
        Gtk.Window.__init__(self, title="Puzzle 2 LCD")
        #Ajustem el tamany predeterminat de la finestra
        self.set_default_size(305, 120)

        #Creem l'objecte lcd
        self.lcd = Lcd.Lcd()

        #Creem i afegim un Grid per a ficar els diferents elements
        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textview()
        self.create_button()

        css = Gtk.CssProvider()
        css.load_from_path("estils.css")
        context = Gtk.StyleContext()
        screen = Gdk.Screen.get_default()
        context.add_provider_for_screen(screen, css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    #Funcio que crea el botó
    def create_button(self):
        #Es crea el botó amb una etiqueta i se li afageix la funcio que ha de fer
        self.button = Gtk.Button.new_with_label("Display")
        self.button.connect("clicked", self.clicked_on_me)

        #Afegim el boto al Grid despres del TextView
        self.grid.attach(self.button, 0, 1, 9, 1)

    #Funcio que s'executa al polsar el botó
    def clicked_on_me(self, button):
        start_iter = self.textbuffer.get_start_iter()
        end_iter = self.textbuffer.get_end_iter()
        text = self.textbuffer.get_text(start_iter, end_iter, True)

        #Es crida a la funció de print del nostre LCD
        self.lcd.printLcd(text)

    def create_textview(self):
        self.textview = Gtk.TextView()
        # Wrap per a que la finestra no s'expandeixi
        # AL arribar al final de la linia
        self.wrap = Gtk.WrapMode(1)
        self.textview.set_wrap_mode(self.wrap)

        #S'estableix el tamany de 20 caracters x 4 files
        self.textview.set_size_request(208,77) # 229, 96
        self.textview.set_monospace(True)

        #S'afegeix el grid a la primera posicio del grid
        self.textbuffer = self.textview.get_buffer()
        self.grid.attach(self.textview, 3, 0, 3, 1)

#main
if __name__ == "__main__":
    win = Lcd_TextViewWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

#! /usr/bin/env python
# PBE Telematica - Grup 1 - Puzzle 1
# Autor: Alejandro Bonilla Orellana

# Import de les llibreries necesaries
import drivers
from time import sleep

# Definim la classe i el mètode:
class Lcd:
        def print_Lcd(self,text):
                display = drivers.Lcd()
                try:
                        print("Escribim al display")
                        while True:
                                display.lcd_display_string("Identificador:",1)
                                display.lcd_display_string(text,2)
                except KeyboardInterrupt:
                # Si es fa un ctrl + C se surt del While
                        display.lcd_clear()
                        print(" Adéu!")
                        
# main
if __name__ == "__main__":
        lcd = Lcd()
        identificador = input("Introdueix identificador: ")
        lcd.print_Lcd(identificador)
