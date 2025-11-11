import random

# Define all word banks
word_bank_fruits = [
    'apple', 'banana', 'mango', 'grape', 'kiwi', 'pineapple', 'orange', 'papaya',
    'pear', 'peach', 'plum', 'cherry', 'watermelon', 'blueberry', 'raspberry', 'fig', 'pomegranate'
]
word_bank_vegetables = [
    'carrot', 'broccoli', 'spinach', 'potato', 'onion', 'cabbage', 'pepper', 'zucchini',
    'cauliflower', 'tomato', 'celery', 'lettuce', 'radish', 'beetroot', 'eggplant', 'turnip', 'leek'
]
word_bank_anime = [
    'naruto', 'bleach', 'onepiece', 'attackontitan', 'deathnote', 'demonlayer', 'jujutsukaisen', 'myheroacademia',
    'tokyoghoul', 'hunterxhunter', 'dragonball', 'chainsawman', 'spyxfamily', 'blackclover', 'fairytail', 'swordartonline'
]
word_bank_cars = [
    'tesla', 'mustang', 'camry', 'civic', 'corvette', 'audi', 'bmw', 'porsche',
    'mercedes', 'volkswagen', 'jeep', 'subaru', 'nissan', 'toyota', 'hyundai', 'mazda', 'chevrolet'
]
word_bank_actors = [
    'dicaprio', 'pitt', 'johansson', 'washington', 'streep', 'hanks', 'roberts', 'bale',
    'damon', 'cruise', 'kidman', 'mcconaughey', 'lawrence', 'gosling', 'denzel', 'blanchett', 'phoenix'
]
word_bank_countries = [
    'japan', 'brazil', 'canada', 'egypt', 'germany', 'india', 'australia', 'france',
    'italy', 'china', 'mexico', 'russia', 'spain', 'southafrica', 'argentina', 'norway', 'sweden'
]
word_bank_vocab = [
    'obfuscate', 'ephemeral', 'ubiquitous', 'quintessential', 'cacophony', 'serendipity', 'juxtapose', 'ineffable',
    'ameliorate', 'perspicacious', 'loquacious', 'vociferous', 'idiosyncratic', 'magnanimous', 'recalcitrant', 'equanimity', 'verisimilitude'
]
word_bank_bikes = [
    'ducati', 'harley', 'yamaha', 'kawasaki', 'honda', 'suzuki', 'ktm', 'triumph',
    'royalenfield', 'bmw', 'aprilia', 'mvagusta', 'bajaj', 'hero', 'indian', 'benelli', 'husqvarna'
]
word_bank_books = [
    '1984', 'dune', 'it', 'frankenstein', 'dracula', 'hobbit', 'gatsby', 'mockingbird',
    'catch22', 'lordoftherings', 'harrypotter', 'bravenewworld', 'fahrenheit451', 'thealchemist', 'thebookthief', 'themartian', 'prideandprejudice'
]
word_bank_movies = [
    'inception', 'avatar', 'titanic', 'interstellar', 'gladiator', 'joker', 'matrix', 'parasite',
    'godfather', 'shawshank', 'darkknight', 'forrestgump', 'fightclub', 'pulpfiction', 'whiplash', 'la_la_land', 'dunkirk'
]

# Dictionary to map category names to word banks
categories = {
    'fruits': word_bank_fruits,
    'vegetables': word_bank_vegetables,
    'anime': word_bank_anime,
    'cars': word_bank_cars,
    'actors': word_bank_actors,
    'countries': word_bank_countries,
    'vocab': word_bank_vocab,
    'bikes': word_bank_bikes,
    'books': word_bank_books,
    'movies': word_bank_movies
}


# Hangman stages: 0 wrong guesses up to 6 wrong guesses
hangman_stages = [
    """
     _______
    |/      
    |       
    |       
    |       
    |       
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |       
    |       
    |       
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |       |
    |       |
    |       
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|
    |       |
    |       
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |       
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |      / 
    |
    |___
    """,
    """
     _______
    |/      |
    |      ( )
    |      /|\\
    |       |
    |      / \\
    |
    |___
    """
]


# Ask user to choose a category
while True:
    print("🎯 Choose a category:")
    for cat in categories:
        print(f"- {cat}")

    chosen_category = input("Enter category name (or type 'esc' to exit): ").strip().lower()

    if chosen_category == 'esc':
        print("👋 Thanks for playing! Goodbye.")
        break

    # Validate and pick a word
    if chosen_category in categories:
        word = random.choice(categories[chosen_category]).lower()
        guessedWord = ['_' for _ in word]
        attempts = 6

        print(f"\nYour word has been chosen from '{chosen_category}' category. Start guessing!")

        while attempts > 0:
            print('\nCurrent word: ' + ' '.join(guessedWord))
            guess = input('Guess a letter: ').lower()

            if guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        guessedWord[i] = guess
                print('✅ Great guess!')
            else:
                attempts -= 1
                print(hangman_stages[6 - attempts])
                print(f'❌ Wrong guess! Attempts left: {attempts}')

            if '_' not in guessedWord:
                print('\n🎉 Congratulations!! You guessed the word: ' + word)
                break

        if attempts == 0 and '_' in guessedWord:
            print('\n😢 You\'ve run out of attempts! The word was: ' + word)

    else:
        print("⚠️ Invalid category. Please restart and choose from the listed options.")




