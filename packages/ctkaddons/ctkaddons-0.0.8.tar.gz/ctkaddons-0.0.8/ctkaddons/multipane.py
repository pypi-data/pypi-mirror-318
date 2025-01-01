from typing import Any
import customtkinter as ctk
import tkscenes

from .errors.multipane_errors import *


class CTkMultiPane(ctk.CTkBaseClass):
	"""
	Defaut widget for any multipane widgets
	"""
	def __init__(
			self, master: Any,
			bar_fg_color=None,
			bar_bg_color="transparent",
			side="top",
			**kwargs
	) -> None:
		super().__init__(master, **kwargs)

		self._frame = ctk.CTkFrame(master, fg_color="transparent")

		self._scenes: dict[str, tkscenes.Scene] = {}
		self._buttons: dict[str, ctk.CTkButton] = {}

		self._side = side

		if side in ["left", "right"]:
			self._bar = ctk.CTkScrollableFrame(
				self._frame,
				fg_color=bar_fg_color,
				bg_color=bar_bg_color,
				orientation="vertical",
				width=150
			)
		if side in ["top", "bottom"]:
			self._bar = ctk.CTkScrollableFrame(
				self._frame,
				fg_color=bar_fg_color,
				bg_color=bar_bg_color,
				orientation="horizontal",
				height=40
			)

		self._main_pane = ctk.CTkFrame(
			self._frame,
			fg_color="transparent"
		)

	def add(self, name: str, key=None, **kwargs) -> None:
		if key is None:
			key = name.lower()

		self._scenes[key] = tkscenes.Scene()
		self._buttons[key] = ctk.CTkButton(
			self._bar,
			text=name,
			command=lambda: self.change_scene(key),
			**kwargs
		)
		if self._side in ["left", "right"]:
			self._buttons[key].pack(side="top", pady=5)
		if self._side in ["top", "bottom"]:
			self._buttons[key].pack(side="left", padx=5)

	def __getitem__(self, item: str) -> tkscenes.Scene:
		if item not in list(self._scenes.keys()):
			raise SceneNotFoundError(item)

		return self._scenes[item]

	def change_scene(self, key: str) -> None:
		if key not in list(self._scenes.keys()):
			raise SceneNotFoundError(key)

		for ikey in self._scenes:
			if ikey != key:
				self._scenes[ikey].unload()

		self._scenes[key].load()

	def _load(self) -> None:
		if self._side in ["top", "bottom"]:
			self._bar.pack(fill="x", side=self._side, padx=5, pady=5)
			self._main_pane.pack(fill="both", side=self._side, padx=5, pady=5, expand=True)
		if self._side in ["left", "right"]:
			self._bar.pack(fill="y", side=self._side, padx=5, pady=5)
			self._main_pane.pack(fill="both", side=self._side, padx=5, pady=5, expand=True)

		if len(list(self._scenes.values())) == 0:
			raise NoSceneCreatedError

		list(self._scenes.values())[0].load()

	def pack(self, **kwargs):
		self._frame.pack(**kwargs)
		self._load()

	def grid(self, **kwargs):
		self._frame.grid(**kwargs)
		self._load()

	def place(self, **kwargs):
		self._frame.place(**kwargs)
		self._load()

	def pack_forget(self):
		self._frame.pack_forget()

	def grid_forget(self):
		self._frame.grid_forget()

	def place_forget(self):
		self._frame.place_forget()

	@property
	def main_pane(self) -> ctk.CTkFrame:
		return self._main_pane
