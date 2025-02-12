import sys
import string
from tabulate import tabulate

def check_for_errors(argv_len, argvs):
    if argv_len < 2:
        sys.exit("Too few arguements")
    elif argv_len > 2:
        sys.exit("Too many arguements")
    elif not argvs[1].endswith(".txt"):
        sys.exit("Incorrect file format")

def remove_punctuation(input_file):
    try:
        with open(input_file, "r") as file:
            reader = file.read().lower()
        reader = reader.translate(str.maketrans("", "", string.punctuation))
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return reader

def get_frequency(file):
    split_words = file.split()
    frequency_dict = {}
    for word in split_words:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict

def find_percentage(frequencies):
    total = sum(frequencies.values())
    return [[word, counter, str(round(counter/total*100, 2))+'%'] for word, counter in frequencies.items()]


def main():
    check_for_errors(len(sys.argv), sys.argv)
    no_punctuation_file = remove_punctuation(sys.argv[1])
    word_frequencies = get_frequency(no_punctuation_file)
    sorted_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    percentage_data = find_percentage(dict(sorted_frequencies))
    print(tabulate(percentage_data, headers=["Word", "#", "%"], tablefmt="fancy_outline"))
if __name__ == "__main__":
    main()
