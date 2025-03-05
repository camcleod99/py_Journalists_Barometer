import re
import tkinter as tk
from season import *

if __name__ == '__main__':
    season = get_season()
    now = get_now()
    print(f"{now.year}-{'{:0>2}'.format(now.month)}-{'{:0>2}'.format(now.day)}")
    print(f"This is day {'{:0>3}'.format(dt_now.timetuple().tm_yday)} of 2025")
    print(f"This is day {(season[0])} of {season[2]}")
    print(f"There is {(season[1])} days left of {season[2]}")
