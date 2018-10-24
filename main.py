file_lines = []
words = []
punct_marks = '$_;:—.,!?1234567890[]()"“”\n'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


# Implementation of a bubble sort as a base sorting algorithm (not used)
def bubble_sort(list):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(list) - 1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                flag = 1
    return list


# My implementation of split() method (not used)
def my_split(raw_string):
    words_list = []
    while raw_string.count(' ') > 0:
        x = raw_string.find(' ')
        words_list.append(raw_string[:x])
        raw_string = raw_string[x + 1:]
    words_list.append(raw_string)
    return words_list


# Deletes punctuation marks and digits from a string
def del_marks(string):
    for mark in punct_marks:
        string = string.replace(mark, '')
    return string


# Decides lexicographic ordering for two words. Returns True if 'a' is before 'b' in a dictionary
def sort_two(a, b):
    for z in range(min(len(a), len(b))):
        if a[z] != b[z]:
            if alphabet.find(a[z]) > alphabet.find(b[z]):
                return True
            else:
                return False
    if len(a) > len(b):
        return True
    else:
        return False


# Lexicographic sorting algorithm based on a bubble sort
def alpha_sort(list):
    flag = 1
    while flag == 1:
        flag = 0
        for i in range(len(list) - 1):
            if sort_two(list[i], list[i+1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                flag = 1
    return list


# TODO: Use another base sorting algorithm (probably heap sort)
# Main program
def main():
    print('a: Song')
    print('b: Wiki article')
    print('c: Novel')
    while True:
        file_to_open = input('Choose a text to sort: ')
        if file_to_open == 'a':
            file_to_open = 'song.txt'
            break
        elif file_to_open == 'b':
            file_to_open = 'wiki.txt'
            break
        elif file_to_open == 'c':
            file_to_open = 'novel.txt'
            break
        else:
            print('Invalid input. Please, try again')

    with open(file_to_open, encoding='UTF-8') as data:
        for line in data:
            if line != '\n':
                file_lines.append(del_marks(line.lower()))

    # Generating one list of separate words
    for i in range(len(file_lines)):
        raw_string = file_lines[i]
        for word in raw_string.split():
            words.append(word)

    print(f'Text divided into separate words: {words}')
    alpha_sort(words)
    print(f'Text divided into separate words and sorted: {words}')

    # Beautifully printing a dictionary from a sorted list
    current_letter = ''
    current_word = ''
    same_word_count = 1
    for i in range(len(words)):

        if words[i] != current_word and same_word_count > 1:
            print(f'({same_word_count})', end='')

        if words[i][:1] != current_letter:
            print()
            current_letter = words[i][:1]
            print(f'{current_letter.capitalize()}:', end='')

        if words[i] != current_word:
            current_word = words[i]
            print(f' {current_word}', end='')
            same_word_count = 1
        else:
            same_word_count += 1


if __name__ == '__main__':
    main()
