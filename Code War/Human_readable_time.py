
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    a = seconds // 60
    ss = seconds % 60
    mm = a % 60
    hh = a // 60
    if hh > 99:
        hh = 99
    if ss < 10:
        ss = "0" + str(ss)
    if mm < 10:
        mm = "0" + str(mm)
    if hh < 10:
        hh = "0" + str(hh)
    return str(hh)+':' + str(mm)+':' + str(ss)


seconds = 86399
print(make_readable(seconds))
