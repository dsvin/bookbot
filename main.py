from stats import word_count
from stats import character_count
from stats import sort_dict
import sys
if len(sys.argv)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

hello = sys.argv[1]
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    frank = get_book_text(hello)
    return(frank)

frank = main()


wc = word_count(frank)
cc = character_count(frank)
sd = sort_dict(diction=cc)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {hello}...")
print("----------- Word Count ----------")
print(wc)
print("--------- Character Count -------")
for i in sd:
    if i["char"].isalpha():
        print(i["char"]+':',i["num"])
print("============= END ===============")
