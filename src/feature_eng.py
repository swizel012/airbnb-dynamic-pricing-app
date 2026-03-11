def get_stay_category(nights):
    if nights == 1:
        return "single_night"
    elif nights <= 3:
        return "short_stay"
    elif nights <= 7:
        return "weekly_stay"
    else:
        return "long_stay"


def get_booking_window(lead_time):
    if lead_time <= 1:
        return "last_minute"
    elif lead_time <= 7:
        return "short_notice"
    elif lead_time <= 30:
        return "planned"
    else:
        return "early_booking"


def get_season(month):
    if month in [1,10]:
        return "cool_high"
    elif month in [11, 12]:
        return "holiday_peak"
    else:
        return "low_season"
    

