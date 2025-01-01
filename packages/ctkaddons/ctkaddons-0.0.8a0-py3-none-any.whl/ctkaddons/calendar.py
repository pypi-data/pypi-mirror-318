from typing import Any
import customtkinter as ctk
import datetime
import math
import tkscenes as scn

month_names = [
    None,
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_len = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leep_year(year: int) -> bool:
    """
    Check if the year is a leep year
    :param year: The year you want to check
    :return: True if it is a leap year and False if it is not
    """
    if year % 100 == 0:
        return True
    if year % 4 == 0:
        return True
    return False


class CTkCalendar(ctk.CTkBaseClass):
    """
    Creates a calender widget
    """
    def __init__(
            self, master: Any,
            date=datetime.date.today(),
            today_color=None,
            today_highlight_color=None,
            **kwargs
    ):
        super().__init__(master, **kwargs)

        self._today = datetime.date.today()

        self.frame = ctk.CTkFrame(master)
        self.frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.labels = [
            ctk.CTkLabel(self.frame, text="Sun"),
            ctk.CTkLabel(self.frame, text="Mon"),
            ctk.CTkLabel(self.frame, text="Tue"),
            ctk.CTkLabel(self.frame, text="Wed"),
            ctk.CTkLabel(self.frame, text="Thu"),
            ctk.CTkLabel(self.frame, text="Fri"),
            ctk.CTkLabel(self.frame, text="Sat")
        ]
        self.dates = scn.Scene()

        if today_color is None:
            self._today_color = "#f07220"
        else:
            self._today_color = today_color

        if today_highlight_color is None:
            self._today_highlight_color = "#a8600e"
        else:
            self._today_highlight_color = today_highlight_color

        self._config_grid(date)
        self._add_dates()

        self._has_drawn = False

    def _add_dates(self):
        for i in range(self._num_of_days):
            if datetime.date(self._year, self._month, i + 1) == self._today:
                color = self._today_color
                hover_color = self._today_highlight_color
            else:
                color = None
                hover_color = None
            self.dates[str(i + 1)] = ctk.CTkButton(
                self.frame,
                text=str(i + 1),
                fg_color=color,
                hover_color=hover_color
            )
            self.dates[str(i + 1)].set_mode(
                "grid",
                row=(i + self._weekday) // 7 + 1,
                column=(i + self._weekday) % 7,
                padx=5, pady=5,
                sticky="nsew"
            )

    def _config_grid(self, date):
        self.frame.rowconfigure([0, 1, 2, 3, 4, 5], weight=0)

        self._month = date.month
        self._year = date.year
        self._weekday = datetime.date(self._year, self._month, 1).weekday() + 1

        if self._weekday > 6:
            self._weekday = 0

        if self._month == 2:
            if is_leep_year(self._year):
                self._num_of_days = 29
            else:
                self._num_of_days = 28
        else:
            self._num_of_days = month_len[self._month]

        self.frame.rowconfigure([int(i) + 1 for i in range(math.ceil((self._weekday + self._num_of_days) / 7))], weight=1)

    def __getitem__(self, item: str | int) -> ctk.CTkButton:
        """
        Returns the button at date
        :param item: The date, can be int or string
        :return: CTkButton
        """
        return self.dates[str(item)].widget

    def _map(self):
        self._has_drawn = True

        # pack date bar
        for index, item in enumerate(self.labels):
            item.grid(row=0, column=index)

        self.dates.load()

    def pack(self, **kwargs):
        """
        Pack this widget
        :param kwargs:
        :return:
        """
        self.frame.pack(**kwargs)
        self._map()

    def grid(self, **kwargs):
        """
        Grid this widget
        :param kwargs:
        :return:
        """
        self.frame.pack(**kwargs)
        self._map()

    def place(self, **kwargs):
        """
        Place this widget
        :param kwargs:
        :return:
        """
        self.frame.pack(**kwargs)
        self._map()

    def pack_forget(self):
        """
        Unmap this widget and do not use it for the packing order.
        :return:
        """
        self.frame.pack_forget()

    def grid_forget(self):
        """
        Unmap this widget and do not use it for the packing order.
        :return:
        """
        self.frame.grid_forget()

    def place_forget(self):
        """
        Unmap this widget and do not use it for the packing order.
        :return:
        """
        self.frame.place_forget()

    def change_time(self, date: datetime.date) -> None:
        """
        Change the current month
        :param date:
        :return:
        """
        self.dates.destroy()
        self._config_grid(date)
        self._add_dates()

        if self._has_drawn:
            self.dates.load()

    @property
    def year(self) -> int:
        """
        Returns the current year
        :return:
        """
        return self._year

    @property
    def month(self) -> int:
        """
        Returns the current month
        :return:
        """
        return self._month

    @property
    def len_of_month(self) -> int:
        """
        Returns the number of days in the current month
        :return:
        """
        return len(self.dates.children)
