import re

possible_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def extract_numbers(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        numbers.extend(
            append_first_and_last(get_numbers(line)) for line in file
        )
    return numbers

def get_numbers(line):
    return [get_number(line, True), get_number(line, False)]

def get_number(line, is_first=True):
    for i in range(1, len(line) + 1):
        substr = line[:i] if is_first else line[-i:]
        for possible_number in possible_numbers:
            if possible_number in substr:
                return possible_number if re.match(r'\d+', possible_number) else convert_to_number(possible_number)

            
def convert_to_number(possible_number):
    if possible_number == "one":
        return '1'
    elif possible_number == "two":
        return '2'
    elif possible_number == "three":
        return '3'
    elif possible_number == "four":
        return '4'
    elif possible_number == "five":
        return '5'
    elif possible_number == "six":
        return '6'
    elif possible_number == "seven":
        return '7'
    elif possible_number == "eight":
        return '8'
    elif possible_number == "nine":
        return '9'
    

def append_first_and_last(numbers):
    return int(numbers[0] + numbers[-1])

if __name__ == '__main__':
    file_path = 'input.txt'
    numbers = extract_numbers(file_path)
    print(sum(numbers))
