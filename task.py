import sys
from collections import deque


def rewrite(argv):
    if len(argv) < 3:
        sys.stderr.write("Not enough arguments! usage: python task.py in.txt pant.txt")
        sys.exit(1)

    with open(argv[1], encoding='utf-8') as file:  # on Windows does not use UTF-8 by default
        input_file = file.read()

    input_file = input_file[:-1]
    letters_dict = {}
    output_string = ""
    output_ids = []
    counter = 0
    l_counter =0

    with open(argv[2], encoding='utf-8') as pant:
        for char in input_file:
            not_in_dict = True
            l_counter+=1
            if char == " " or char == " ":  # check for empty letter
                output_string += char
                output_ids.append(0)
            else:
                if char.lower() in letters_dict:
                    try:
                        arr = letters_dict[char.lower()].popleft()
                        output_string += arr[0]
                        output_ids.append(arr[1])
                        not_in_dict = False
                    except:
                        # Letter in dictionary is exhausted
                        not_in_dict = True
                if not_in_dict:
                    while True:
                        counter += 1
                        pant_char = pant.read(1)
                        if not pant_char:
                            sys.exit(1)
                        if pant_char.lower() == char.lower():
                            output_string += pant_char
                            output_ids.append(counter)
                            break
                        else:
                            # Letter does not exist in dictionary
                            if pant_char.lower() in letters_dict:
                                letters_dict[pant_char.lower()].append([pant_char, counter])
                            else:
                                letters_dict[pant_char.lower()] = deque([[pant_char, counter]])
        # input String can be now rewritten
        with open('test.output', mode='w', encoding='utf-8') as output_file:
            output_file.writelines([output_string, "\n\n", str(output_ids)])

if __name__ == "__main__":
    sys.exit(rewrite(sys.argv))
