#! /usr/bin/env python
# PBE Telematica - Grup 1 - Puzzle 1
# Autor: Alejandro Bonilla Orellana

# Import de les llibreries necesaries
import drivers
import time

# Definim la clase i el mètode:
class Lcd:

    # Es llegeixen 4 linies i es retornen
    def inputText(self):
        lines = []
        i = 1
        while i < 5:
            line = input()
            line = line[:20] # Trunquem la linia a un màxim de 20 caracters per a que no surti de l'LCD
            lines.append(line)
            i += 1
        self.textLcd = '\n'.join(lines)
        return self.textLcd
    # S'agafa l'atribut textLcd i es printeja a cada filera segons es veuen \n
    def printLcd(self, textLcd):
        display = drivers.Lcd()
        try:
            lines = textLcd.split('\n') # Dividir l'string
            for i, line in enumerate(lines, start=1):
                display.lcd_display_string(line, i)
        except KeyboardInterrupt:
            return 0

# main
if __name__ == "__main__":
    lcd = Lcd()
    text = lcd.inputText()
    lcd.printLcd(text)
