

def arithmetic_average(grade_a, grade_b, grade_c, average_type='A'):
    if average_type in ['A', 'a']:
        return (grade_a + grade_b + grade_c) / 3
    elif average_type in ['P', 'p']:
        return (grade_a * 5 + grade_b * 3 + grade_c * 2) / 10
    return 'Unexpected average type.'


print(arithmetic_average(10, 15, 20, 'A'))
print(arithmetic_average(10, 15, 20, 'p'))
print(arithmetic_average(10, 15, 20, 'z'))
