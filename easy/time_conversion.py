def timeConversion(s):
    time_parts = s.split(':')

    hour = int(time_parts[0])
    minute = int(time_parts[1])
    second = int(time_parts[2][:2])
    meridiem = time_parts[2][2:]

    if meridiem == 'PM' and hour != 12:
        hour += 12
    elif meridiem == 'AM' and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}:{second:02}"


if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)
