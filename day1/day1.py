import re

def extract_numbers(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers.append(append_first_and_last(extract_numbers_regex(line)))
    return numbers

def extract_numbers_regex(string):
    numbers = re.findall(r'\d+', string)
    return ''.join(numbers)

def append_first_and_last(numbers):
    return int(numbers[0] + numbers[-1])

if __name__ == '__main__':
    file_path = 'input.txt'
    numbers = extract_numbers(file_path)
    print(sum(numbers))
