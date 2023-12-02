use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn extract_numbers(file_path: &str) -> Vec<String> {
    let mut numbers = Vec::new();
    let file = File::open(file_path).expect("Failed to open file");
    let reader = BufReader::new(file);
    let re = Regex::new(r"\d").expect("Failed to create regex");

    for line in reader.lines() {
        if let Ok(line) = line {
            let extracted_numbers = extract_numbers_regex(&re, &line);
            numbers.push(append_first_and_last(&extracted_numbers));
        }
    }

    numbers
}

fn extract_numbers_regex<'a>(re: &'a Regex, string: &'a str) -> Vec<String> {
    let mut numbers = Vec::new();

    for capture in re.captures_iter(string) {
        if let Some(number) = capture.get(0) {
            numbers.push(number.as_str().to_string());
        }
    }
    numbers
}

fn append_first_and_last(numbers: &[String]) -> String {
    let first = numbers.first().cloned().unwrap_or_default();
    let last = numbers.last().cloned().unwrap_or_default();

    let result = format!("{}{}", first, last);

    result
}

fn main() {
    let file_path = "input.txt";
    let numbers = extract_numbers(file_path);
    let sum: usize = numbers.iter().filter_map(|s| s.parse::<usize>().ok()).sum();
    println!("{}", sum);
}
