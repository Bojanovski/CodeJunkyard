
#################################################################
#
#	This code was used to get the "Priority Mail" achievement 
#	in World of Warcraft:
#	https://www.wowhead.com/achievement=12439/priority-mail
#
#################################################################

import wx
import os
import numpy
import win32api, win32con
import time

try:
    from PIL import Image
except ImportError:
    import Image
	
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def imagetopil(wxImage):
	"""Convert wx.Image to PIL Image."""
	wxImage = wxImage.Mirror(False)
	w = wxImage.GetWidth()
	h = wxImage.GetHeight()
	data = wxImage.GetData()
	
	red_image   = Image.frombuffer('L',(w,h),data[0::3])
	green_image = Image.frombuffer('L',(w,h),data[1::3])
	blue_image  = Image.frombuffer('L',(w,h),data[2::3])
	pilImage = Image.merge('RGB', (red_image, green_image, blue_image))
	return pilImage

class Ocr:

	def __init__(self):
		# Need to create an App instance before doing anything
		self.app = wx.App()
		return

	def ss(self, offset_x=780, offset_y=723, width=800, height=80):
		screen = wx.ScreenDC()
		size = screen.GetSize()
		bmp = wx.Bitmap(width, height)
		mem = wx.MemoryDC(bmp)
		mem.Blit(0, 0, width, height, screen, offset_x, offset_y)
		del mem  # Release bitmap
		file_name = "ss.png"
		wxImage = bmp.ConvertToImage()
		wxImage = wxImage.ConvertToGreyscale()
		wxImage = wxImage.Scale(width / 2, height / 2, wx.IMAGE_QUALITY_HIGH)
		pilImage = imagetopil(wxImage)
		
		# Simple image to string
		text = pytesseract.image_to_string(pilImage)
		
		zones = [("Allerian Stronghold" , 3),
		("Altar of Sha'tar" , 3),
		("Area 52" , 3),
		("Aerie Peak" , 2),
		("Astranaar" , 1),
		("Azurewing Repose" , 6),
		("Booty Bay" , 2),
		("Bradensbrook" , 6),
		("Brill" , 2),
		("Camp Oneqwah" , 4),
		("Cenarion Refuge" , 3),
		("Conquest Hold" , 4),
		("Cosmowrench" , 3),
		("Dawn's Blossom" , 5),
		("Deliverance Point" , 6),
		("Everlook" , 1),
		("Feathermoon Stronghold" , 1),
		("Frosthold" , 4),
		("Gadgetzan" , 1),
		("Garadar" , 3),
		("Goldshire" , 2),
		("Greywatch" , 6),
		("Halfhill" , 5),
		("Honor Hold" , 3),
		("Kamagua" , 4),
		("Kharanos" , 2),
		("Klaxxi'vess" , 5),
		("Lion's Landing" , 5),
		("Longying Outpost" , 5),
		("Lor'danel" , 1),
		("Lorlathil" , 6),
		("Menethil Harbor" , 2),
		("Meredil" , 6),
		("Moa'ki Harbor" , 4),
		("Nesingwary Base Camp" , 4),
		("Nighthaven" , 1),
		("Nordrassil" , 1),
		("One Keg" , 5),
		("Ramkahen" , 1),
		("Sentinel Hill" , 2),
		("Shackle's Den" , 6),
		("Skyhorn" , 6),
		("Soggy's Gamble" , 5),
		("Stonard" , 2),
		("Sylvanaar" , 3),
		("Tarren Mill" , 2),
		("The Argent Stand" , 4),
		("The Crossroads" , 1),
		("Thrallmar" , 3),
		("Thunder Cleft" , 5),
		("Thunder Totem" , 6),
		("Tian Monastery" , 5),
		("Tranquillien" , 2),
		("Valdisdall" , 6),
		("Valiance Keep" , 4),
		("Warsong Hold" , 4),
		("Whisperwind Grove" , 1),
		("Wyrmrest Temple" , 4),
		("Zabra'jin" , 3),
		("Zouchin Village" , 5)]
		
		continents = ["N/A",
		"Kalimdor",
		"Eastern Kingdoms",
		"Outland",
		"Northrend",
		"Pandaria",
		"Broken Isles"]
		
		# find the continent and click on it
		time_to_sleep = 0.5 
		to_print = text + "  --->  "
		for zone in zones:
			if text == zone[0]:
				to_print += continents[zone[1]]
				if (zone[1] == 1):
					click(750, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				if (zone[1] == 2):
					click(915, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				if (zone[1] == 3):
					click(1050, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				if (zone[1] == 4):
					click(1200, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				if (zone[1] == 5):
					click(1360, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				if (zone[1] == 6):
					click(1520, 650)
					to_print += "\nclicked on " + continents[zone[1]]
					time.sleep(time_to_sleep)
				break
		
		print(to_print)
		
		return
		
		
a = Ocr()
while (True):
	a.ss()