#! /usr/bin/env python
# PBE Telematica - Grup 1 - Puzzle 1
# Autor: Alejandro Bonilla Orellana

# Import de les llibreries necesaries
import drivers
from time import sleep

# Definim la clase i el mètode:
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