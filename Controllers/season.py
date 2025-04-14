import datetime as dt
dt_now = dt.datetime.now()
STRING_SEASON = ("❄️️", "🌲️", "☀️️", "🍂️")

def get_now():
    return dt_now

def get_season():
    dt_spring = dt.datetime(dt_now.year,3, 21)
    dt_summer = dt.datetime(dt_now.year,6, 21)
    dt_autumn = dt.datetime(dt_now.year,9, 21)
    dt_winter = dt.datetime(dt_now.year,12, 21)
    dt_last_winter = dt.datetime(dt_now.year - 1,12,21)
    dt_next_spring = dt.datetime((dt_now.year + 1),3, 21)

    if dt_now < dt_spring:
        return (dt_now - dt_last_winter).days, (dt_spring - dt_last_winter).days, STRING_SEASON[0]
    elif dt_now < dt_summer:
        return (dt_now - dt_spring).days, (dt_summer - dt_spring).days, STRING_SEASON[1]
    elif dt_now < dt_autumn:
        return (dt_now - dt_summer).days, (dt_autumn - dt_summer).days, STRING_SEASON[2]
    elif dt_now < dt_winter:
        return (dt_now - dt_autumn).days, (dt_winter - dt_autumn).days, STRING_SEASON[3]
    else:
        return (dt_now - dt_winter).days, (dt_next_spring - dt_winter).days, STRING_SEASON[0]