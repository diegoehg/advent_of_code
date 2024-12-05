import re

digits_words = {
        "one": 1,
        "eno": 1,
        "two": 2,
        "owt": 2,
        "three": 3,
        "eerht": 3,
        "four": 4,
        "ruof": 4,
        "five": 5,
        "evif": 5,
        "six": 6,
        "xis": 6,
        "seven": 7,
        "neves": 7,
        "eight": 8,
        "thgie": 8,
        "nine": 9,
        "enin": 9,
        }

def parse_digit(match):
    if(match.isdecimal()):
        return int(match)
    else:
        return digits_words.get(match)


calibration_sum = 0
sub_pattern = "|".join([k for k in digits_words.keys()])
pattern = rf"(\d|{sub_pattern})"

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        matches = re.findall(pattern, line)
        first_digit = parse_digit(matches[0])

        matches = re.findall(pattern, line[::-1])
        last_digit = parse_digit(matches[0])

        number = int(f'{first_digit}{last_digit}')

        calibration_sum += number

print(f'Calibration sum: {calibration_sum}')
