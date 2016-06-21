import sys
from collections import deque


def rewrite(argv):
    if len(argv) < 3:
        sys.stderr.write("Not enough arguments! usage: python task.py in.txt pant.txt")
        sys.exit(1)

    with open(argv[1], encoding='utf-8') as file:  # on Windows does not use UTF-8 by default
        input_file = file.read()

    print(input_file)
    letters_dict = {}
    output_string = ""
    output_ids = []
    counter = 1
    l_counter =0

    with open(argv[2], encoding='utf-8') as pant:
        print("Pant is opend")
        for char in input_file:
            print(output_string)
            not_in_dict = True
            print("Chr: " + char + " index:" + str(l_counter))
            l_counter+=1
            if char == " " or char == " ":  # check for empty letter
                output_string += char
                output_ids.append(0)
            else:
                if char.lower() in letters_dict:
                    try:
                        print("Trying "+char+" lower: "+char.lower())
                        arr = letters_dict[char.lower()].popleft()
                        output_string += arr[0]
                        output_ids.append(arr[1])
                        not_in_dict = False
                        print("found in dict")
                    except:
                        # Letter in dictionary is exhausted
                        not_in_dict = True
                if not_in_dict:
                    print("not in dict")
                    while True:
                        counter += 1
                        if counter < 250:
                            print("Counter is: "+ str(counter) + " looking for: "+char)
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
        # input String can be rewritten
        # todo: generate output
        print(output_ids)
        print(output_string)

if __name__ == "__main__":
    sys.exit(rewrite(sys.argv))
