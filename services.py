from PIL import ImageTk, Image
import os

class images:
	def image_make(path_, sw_, sh_):
		image = Image.open(path_)
		image = image.resize((sw_,sh_) , Image.ANTIALIAS)
		image = ImageTk.PhotoImage(image)
		return image
