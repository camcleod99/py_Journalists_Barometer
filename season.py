import datetime as dt

dt_now = dt.datetime.now()

def get_now():
    return dt_now

def get_season():
    STRING_WINTER = "❄️️"
    STRING_SPRING = "🌲️"
    STRING_SUMMER = "☀️️"
    STRING_AUTUMN = "🍂️"

    dt_spring = dt.datetime(dt_now.year,3, 21)
    dt_summer = dt.datetime(dt_now.year,6, 21)
    dt_autumn = dt.datetime(dt_now.year,9, 21)
    dt_winter = dt.datetime(dt_now.year,12, 21)
    dt_last_winter = dt.datetime(dt_now.year - 1,12,21)
    dt_next_spring = dt.datetime((dt_now.year + 1),3, 21)

    if dt_now < dt_spring:      return (dt_now - dt_last_winter).days, (dt_spring - dt_now).days, STRING_WINTER
    elif dt_now < dt_summer:    return (dt_winter - dt_now).days, (dt_summer - dt_now).days, STRING_SPRING
    elif dt_now < dt_autumn:    return (dt_spring - dt_now).days, (dt_autumn - dt_now).days, STRING_SUMMER
    elif dt_now < dt_winter:    return (dt_summer - dt_now).days, (dt_winter - dt_now).days, STRING_AUTUMN
    else:                       return (dt_autumn - dt_now).days, (dt_next_spring - dt_now).days, STRING_WINTER