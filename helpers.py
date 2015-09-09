import datetime

def validateDate(date):
    '''
    Check if a date in YYYY-MM-DD is valid.
    '''
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def next_weekday(weekday):
    '''
    Finds the next weekday from today's date corresponding to the value of d:
    0 = Monday
    1 = Tuesday
    ....
    7 = Sunday
    '''
    d = datetime.datetime.now()
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def getDays(teleBearsDays):
    '''
    Parses the teleBearsDays string to the format needed for next_weekday.
    0 = Monday
    1 = Tuesday
    ....
    7 = Sunday
    Thus, -M-W-F- : [0,2,4]
    '''
    l = []
    i = 7
    for char in teleBearsDays:
        if char != '-':
            l.append(i)
        i += 1
        if i > 7:
            i = 0
    return l
