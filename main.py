import re
import tkinter as tk
from tkinter import Tk, Canvas, Label, PhotoImage
from tkmacosx import Button
from turtledemo.nim import COLOR

from season import *
import pyperclip
import calendar

COLOR_BACKGROUND = '#B1DDC6'

if __name__ == '__main__':
    # Setup
    season = get_season()
    now = get_now()
    year_days = 366 if calendar.isleap(now.year) else 365

    string_date = f"{now.year}-{'{:0>2}'.format(now.month)}-{'{:0>2}'.format(now.day)}"
    string_journal = f"📅️ {now.strftime("%a")} | 🌏️ {'{:0>3}'.format(now.timetuple().tm_yday)} / {year_days} | {season[2]} {season[0]} / {season[0] + season[1]}"

    # Functions
    def copy_date():
        pyperclip.copy(string_date)
        return None

    def copy_journal():
        pyperclip.copy(string_journal)
        return None

    # Screen
    win = Tk()
    win.title("Journalist's Barometer")
    win.config(padx=50, pady=50, bg=COLOR_BACKGROUND)

    canvas = Canvas(height=800, width=800)
    canvas.config(bg=COLOR_BACKGROUND, highlightthickness=0)

    # Labels
    label_email = Label(text="Date", padx=5, width=10)
    label_email.grid(column=1, row=1)

    label_website = Label(text="Journal String", padx=5, width=10)
    label_website.config(padx=5)
    label_website.grid(column=1, row=2)

    # Text Fields
    label_date = Label(text=string_date, padx=5, pady=5, width=50, background=COLOR_BACKGROUND)
    label_date.grid(column=2, row=1)

    label_journal = Label(text=string_journal, padx=5, pady=5, width=50, background=COLOR_BACKGROUND)
    label_journal.config(padx=5)
    label_journal.grid(column=2, row=2)

    # Buttons
    button_find_password = Button(text="📋️", command=copy_date,borderless=1, highlightthickness=0, background="grey")
    button_find_password.grid(column=3, row=1)

    button_save_email = Button(text="📋️", command=copy_journal,borderless=1, highlightthickness=0,  background="grey")
    button_save_email.grid(column=3, row=2)

    win.mainloop()
