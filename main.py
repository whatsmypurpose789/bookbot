import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

asd = sys.argv[1]

from stats import word_number
from stats import character_count
from stats import sort

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {asd}...")
    print("----------- Word Count ----------")
    print(f"Found {word_number(asd)} total words")
    print("--------- Character Count -------")

    character_count(asd)  # populates stats.characters
    sorted_chars = sort()
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

