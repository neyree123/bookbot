from stats import get_word_count, get_character_counts, get_sorted_list
import sys

def get_book_text( filepath ):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    word_count = get_word_count(text)

    char_counts = get_character_counts(text)
    sorted_ls = get_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_ls:
        if(d["name"].isalpha()):
            print(f"{d["name"]}: {d["num"]}")
    print("============= END ===============")

main()