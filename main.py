class flashcard:

    def _init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def _str_(self):
        
        return self.word + ' (' + self.meaning + ')'


flash = []

print("welcome to flashcard application")


while True:
    word = input("enter the name you want to add to flashcard: ")
    meaning = input("enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0 to stop adding flashcards, otherwise enter 1: "))
    if(option):
        break
    
print("\nYour flashcards")

for i in flash:
    print(">", i)

