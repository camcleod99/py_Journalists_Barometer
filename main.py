import re
import tkinter as tk
from season import *
import pyperclip

if __name__ == '__main__':
    season = get_season()
    now = get_now()
    print(f"{now.year}-{'{:0>2}'.format(now.month)}-{'{:0>2}'.format(now.day)}")
    print(f"{now.strftime("%a")}")
    print(f"This is day {'{:0>3}'.format(now.timetuple().tm_yday)} of 2025")
    print(f"This is day {(season[0])} of {season[2]}")
    print(f"There is {(season[1])} days left of {season[2]}")

    journal_string = f"📅️ {now.strftime("%a")} | 🌏️ {'{:0>3}'.format(now.timetuple().tm_yday)} / 365 | 🌲️ {season[0]} / {season[0] + season [1]}"
    pyperclip.copy(journal_string)
    print(f"📅️ {now.strftime("%a")} | 🌏️ {'{:0>3}'.format(now.timetuple().tm_yday)} / 365 | 🌲️ {season[0]} / {season[0] + season [1]}")
