from tkinter import Tk, Canvas, Label
from tkmacosx import Button
import pyperclip
import calendar
import Api.sunrisesunset as sunrise_sunset
import Api.openweather as openweather
import Controllers.season as season
from datetime import datetime

COLOR_BACKGROUND = '#B1DDC6'

class MainView:
    def __init__(self):
        self.text_date = self.set_date()
        self.text_sun = self.set_sun()
        self.text_journal = self.set_journal()

        self.root = Tk()
        self.root.title = "Journalist's Barometer"
        self.root.config(padx=50, pady=50, bg=COLOR_BACKGROUND)
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.config(bg=COLOR_BACKGROUND, highlightthickness=0)

        self.label_date = Label(text="Date", padx=5, width=10)
        self.label_journal = Label(text="Journal String", padx=5, width=10)
        self.label_sun = Label(text="Sunrise", padx=5, width=10)
        self.label_journal.config(padx=5)

        self.text_date = Label(text=self.text_date, padx=5, pady=5, width=50, background=COLOR_BACKGROUND)
        self.text_sun = Label(text=self.text_sun, padx=5, pady=5, width=50, background=COLOR_BACKGROUND)
        self.text_journal = Label(text=self.text_journal, padx=5, pady=5, width=50, background=COLOR_BACKGROUND)

        self.button_date = Button(text="📋️", command=self.copy_date, borderless=1, highlightthickness=0, )
        self.button_journal = Button(text="📋️", command=self.copy_journal, borderless=1, highlightthickness=0, )
        self.button_sun = Button(text="📋️", command=self.copy_sun, borderless=1, highlightthickness=0, )
        self.button_save_journal = Button(text="📋️ Copy Journal", command=self.copy_journal_entry, borderless=1, highlightthickness=0, width=300, )

        self.label_date.grid(column=1, row=1)
        self.label_journal.grid(column=1, row=2)
        self.label_sun.grid(column=1, row=3)

        self.text_date.grid(column=2, row=1)
        self.text_journal.grid(column=2, row=2)
        self.text_sun.grid(column=2, row=3)

        self.button_date.grid(column=3, row=1)
        self.button_journal.grid(column=3, row=2)
        self.button_sun.grid(column=3, row=3)

        self.button_save_journal.grid(column=2, row=4)

    @staticmethod
    def set_sun():
        sun_times = sunrise_sunset.get_sun_times()
        return f"🌅️ {sun_times[0]} | 🌇️ {sun_times[1]}"

    @staticmethod
    def set_date():
        return f"{datetime.now().year}-{'{:0>2}'.format(datetime.now().month)}-{'{:0>2}'.format(datetime.now().day)}"

    @staticmethod
    def set_journal():
        now_season = season.get_season()
        now_date = datetime.now()
        year_days = 366 if calendar.isleap(now_date.year) else 365
        return f"📅️ {now_date.strftime("%a")} | 🌏️ {'{:0>3}'.format(now_date.timetuple().tm_yday)} / {year_days} | {now_season[2]} {now_season[0]} / {now_season[1]}"

    @staticmethod
    def set_weather(self):
        #TODO: Get Weather Data
        #TODO: Display Weather Data
        return "-"

    def copy_date(self):
        pyperclip.copy(self.text_date.cget("text"))

    def copy_journal(self):
        pyperclip.copy(self.text_journal.cget("text"))

    def copy_sun(self):
        pyperclip.copy(self.text_date.cget("text"))

    def copy_journal_entry(self):
        date = self.text_date.cget("text")
        journal = self.text_journal.cget("text")
        sun = self.text_sun.cget("text")
        pyperclip.copy(f"# {date}\n{journal}\n{sun}")



