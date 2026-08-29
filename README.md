# 🔤 Word Guessing Game (Hangman)

## Overview

A basic Hangman-style word guessing game built in Python, played entirely in the command line. The player guesses letters to reveal a hidden word within a limited number of incorrect attempts, with the game tracking guessed letters and remaining tries.

## 🕹️ How to Play
When you start the game, you’ll be prompted to choose a category from the list:

- Fruits
- Vegetables
- Anime
- Cars
- Actors
- Countries
- Vocabulary
- Bikes
- Books
- Movies

Once you select a category, a random word from that category will be chosen. You’ll see underscores (_) representing each letter of the word. Guess one letter at a time:
  - ✅ Correct guesses reveal the letter’s position(s) in the word.
  - ❌ Wrong guesses decrease your remaining attempts and display part of the Hangman.

You have 6 attempts before the full Hangman is drawn. Guess the word before you run out of tries to win! You can type esc anytime to exit the game.

## Features

- CLI-based interactive gameplay
- Random word selection
- Tracks correctly and incorrectly guessed letters
- Attempt counter with game-over condition
- Win/lose end states with the correct word revealed on loss

## Technologies Used

- **Python 3.x**

## Concepts Demonstrated

- Control flow and loops for game state management
- String manipulation and indexing
- Input validation (handling repeated/invalid guesses)
- Basic CLI UX design

## Run It Yourself

```bash
git clone https://github.com/HRITHIKA-NAIR/Build-a-Word-Guessing-Game-with-Python.git
cd Build-a-Word-Guessing-Game-with-Python
python main.py
```
