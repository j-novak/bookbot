def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    result_list = dictionary_to_list(lc(file_contents))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc(file_contents)} words found in the document")
    print()
    for item in result_list:
        if item["key"].isalpha():
            print(f"The '{item["key"]}' character was found {item["value"]} times")
    print("--- End report ---")

def wc(input):
    return len(input.split())

def lc(input):
    result_dict = {}
    for character in input:
        lowercase_char = character.lower()
        if lowercase_char in result_dict:
            result_dict[lowercase_char] += 1
        else:
            result_dict[lowercase_char] = 1
    return result_dict

def sort_on(dict):
    return dict["key"]

def dictionary_to_list(dict):
    result_list = []
    for key, value in dict.items():
        result_list.append({"key": key, "value": value})
    result_list.sort(reverse=False, key=sort_on)
    return result_list

main()
