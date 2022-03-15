

def time_in_seconds(hour, minutes, seconds):
    return int(hour) * 3600 + int(minutes) * 60 + int(seconds)


time = time_in_seconds(*input('Enter a time. Use format HH:MM:SS: ').split(':'))

print(f'The time inserted equivalent to {time} seconds.')
