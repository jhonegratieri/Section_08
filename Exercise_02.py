

def convert_date(day, month, year):
    list_of_months = {'01': 'January',
                      '02': 'February',
                      '03': 'March',
                      '04': 'April',
                      '05': 'May',
                      '06': 'June',
                      '07': 'July',
                      '08': 'August',
                      '09': 'September',
                      '10': 'October',
                      '11': 'November',
                      '12': 'Dezember'
                      }

    if month == '01':
        ordinal_suffix = 'st'
    elif month == '02':
        ordinal_suffix = 'nd'
    elif month == '03':
        ordinal_suffix = 'rd'
    ordinal_suffix = 'th'

    if month in list_of_months.keys():
        print(f'The date inputted is {list_of_months[month]} {day}{ordinal_suffix}, {year}.')


convert_date(*input('Enter a date. Use format DD/MM/YYYY:').split('/'))
