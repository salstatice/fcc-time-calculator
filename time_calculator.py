def add_time(start, duration, weekday=None):
    # parse time
    start_time = start.split(' ')[0].split(':')
    start_min = int(start_time[0]) * 60 + int(start_time[1])
    if start.split(' ')[1] == 'PM':
      start_min = start_min + (12 * 60)
    duration_min = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])
    
    # calculate time
    total_min = start_min + duration_min

    # day display
    days_later = total_min // (24 * 60)
    days_later_str = ''
    if days_later == 1:
        days_later_str = ' (next day)'
    elif days_later > 1:
        days_later_str = ' ({} days later)'.format(days_later)

    # weekday display
    weekday_str = ''
    if weekday is not None:
        weekday_list = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        if weekday.lower() in weekday_list:
            weekday_num = weekday_list.index(weekday.lower())
            total_weekday = weekday_num + days_later
            weekday_num = total_weekday % 7
            weekday_str = ', {}'.format(weekday_list[weekday_num].capitalize())
    
    # time display
    new_min = total_min % (24 * 60)
    new_hour = new_min // 60
    display_min = str(new_min % 60).rjust(2, '0')
    meridiem = ''
    if new_hour >= 12:
        meridiem = 'PM'
        if new_hour > 12:
            new_hour = new_hour - 12
    else:
        meridiem = 'AM'
        if new_hour == 0:
            new_hour = new_hour +12

    new_time = '{}:{} {}{}{}'.format(new_hour, display_min, meridiem, weekday_str,  days_later_str)

    return new_time