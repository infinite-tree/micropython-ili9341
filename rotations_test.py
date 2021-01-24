from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import tt14

# https://forum.micropython.org/viewtopic.php?t=4041
# It looks like there are 2 available SPI buses on the ESP32: HSPI=1 and VSPI = 2.
# HSPI is MOSI=GPIO13, MISO=GPIO12 and SCK=GPIO14
# VSPI is MOSI=GPIO23, MISO=GPIO19 and SCK=GPIO18
TFT_SPI_ID = 2
TFT_MISO_PIN = 19
TFT_MOSI_PIN = 23
TFT_CLK_PIN = 18
TFT_CS_PIN = 15
TFT_DC_PIN = 2
TFT_RST_PIN = 4


text = 'F'

spi = SPI(TFT_SPI_ID,
          baudrate=40000000,
          miso=Pin(TFT_MISO_PIN),
          mosi=Pin(TFT_MOSI_PIN),
          sck=Pin(TFT_CLK_PIN))

display = ILI9341(spi,
                  cs=Pin(TFT_CS_PIN),
                  dc=Pin(TFT_DC_PIN),
                  rst=Pin(TFT_DC_PIN),
                  w=320,
                  h=240,
                  r=0)
display.erase()
display.set_font(tt14)
display.set_pos(0,0)
display.print(text)
display.set_pos(0,20)
display.print(text)
display.set_pos(40,20)
display.print(text)

