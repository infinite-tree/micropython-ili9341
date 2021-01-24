# test of printing multiple fonts to the ILI9341 on an M5Stack using H/W SP
# MIT License; Copyright (c) 2017 Jeffrey N. Magee

from ili934xnew import ILI9341, color565
from machine import Pin, SPI
import tt14
import glcdfont
import tt14
import tt24
import tt32

fonts = [glcdfont,tt14,tt24,tt32]

text = 'Now is the time for all good men to come to the aid of the party.'

TFT_SPI_ID = 2
TFT_MISO_PIN = 19
TFT_MOSI_PIN = 23
TFT_CLK_PIN = 18
TFT_CS_PIN = 15
TFT_DC_PIN = 2
TFT_RST_PIN = 4


def init(r):
    spi = SPI(
        TFT_SPI_ID,
        baudrate=40000000,
        miso=Pin(TFT_MISO_PIN),
        mosi=Pin(TFT_MOSI_PIN),
        sck=Pin(TFT_CLK_PIN))

    return ILI9341(
        spi,
        cs=Pin(TFT_CS_PIN),
        dc=Pin(TFT_DC_PIN),
        rst=Pin(TFT_RST_PIN),
        w=320,
        h=240,
        r=r)

def run(display):
    display.erase()
    display.set_pos(0,0)
    for ff in fonts:
        display.set_font(ff)
        display.print(text)

def test(rotation=1):
    display = init(rotation)
    run(display)

