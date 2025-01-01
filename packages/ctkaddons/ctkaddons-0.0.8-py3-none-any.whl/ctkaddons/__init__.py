from .calender import CTkCalender
from .date_select import CTkDateSelect
from .multipane import CTkMultiPane

from PIL import Image
import customtkinter as ctk
import multipledispatch


@multipledispatch.dispatch(str)
def set_image(path: str, size=(20, 20)) -> ctk.CTkImage:
	img = Image.open(path)

	return ctk.CTkImage(img, img, size)


@multipledispatch.dispatch(str, str)
def set_image(light_path: str, dark_path: str, size=(20, 20)) -> ctk.CTkImage:
	light_img = Image.open(light_path)
	dark_img = Image.open(dark_path)

	return ctk.CTkImage(light_img, dark_img, size)
