import re

def pascal_to_snake(pascal_case_string):
    snake_case_string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', pascal_case_string)
    snake_case_string = re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_case_string).lower()
    return snake_case_string

def camel_to_snake(camel_case_string):
    return pascal_to_snake(camel_case_string)


def is_leap_year(year):
    # If a year is divisible by 4, it could be a leap year.
    if year % 4 == 0:
        # But if it's also divisible by 100, it might not be.
        if year % 100 == 0:
            # However, if it's divisible by 400, it is a leap year.
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False