from . import jalali
from django.utils import timezone
def jalali_converter(time):
    time=timezone.localtime(time)
    time_str="{},{},{}" .format(time.year,time.month,time.day)
    persian_month={
    1: "فروردین",
    2: "اردیبهشت",
    3:"خرداد",
    4: "تیر",
    5:"مرداد",
    6:"شهریور",
    7:"مهر",
    8:"آبان",
    9:"آذر",
    10:"دی",
    11:"بهمن",
    12:"اسفند",
    }

    jdate=list(jalali.Gregorian(time_str).persian_tuple())
    str_jdate="{} {} {}, ساعت {}:{}".format(
        jdate[2],
        persian_month[jdate[1]],
        jdate[0],
        time.hour,
        time.minute,
    )
    return str_jdate