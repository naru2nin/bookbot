from collections import defaultdict

def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def countwords(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()
        #print(words)
        count = 0
        for word in words:
            if word != 0:
                count += 1
        #print(count)
        return count

def print_report(path, dict_item, count):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document\n")

    #converting the dictionary to 2 lists
    keys_list = list(dict_item.keys())
    #print(len(keys_list))
    values_list = list(dict_item.values())

    for i in range(len(keys_list)):
        print(f"The '{keys_list[i]}' character was found {values_list[i]} times")

    print("--- End report ---")

def count_letter_duplicates(path_to_file):
    with open(path_to_file) as f:
        paragraph = f.read()
        
    # Initialize a default dictionary to count letter occurrences
        letter_count = defaultdict(int)
    
    # Iterate over each character in the paragraph
        for char in paragraph:
            if char.isalpha():  # Check if the character is a letter
                letter_count[char.lower()] += 1
    
    # Convert to a regular dictionary before returning
        #print(dict(letter_count)) 

        #letter_count.sort(reverse=True, key=sort_on)
        #print(letter_count)
        #print(type(letter_count))

        #this makes the dictionary sorted in decending order
        sorted_letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    
        #print(sorted_letter_count)
        #print(type(sorted_letter_count))
        return sorted_letter_count





def main():
    pathtofile = "books/frankenstein.txt"
    #read_file(pathtofile)
    totalwordcount = countwords(pathtofile)
    dictlettercount = count_letter_duplicates(pathtofile)
    print_report(pathtofile, dictlettercount, totalwordcount)
    return 0

if __name__ == "__main__":
    main()
