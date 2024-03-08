# python-hangman-game

Project Description:

My project is a Hangman game where player guess words read from a text file.

The game progresses as follows:

1. Player select the difficulty level, which determines the number of lives they have.
2. The game starts with the secret word displayed as question marks representing the missing letters.
3. Incorrect guesses decrease lives, while correct guesses reveal letters in the word.
4. The game ends when the player either guesses the word correctly or runs out of lives.

Implementation Details:

- Secret words are defined in the text file the user creates and the secret word is randomly chosen using Python's `Random.choice` function.
- The game supports words of any length and even sentences, with spaces requiring additional guesses.
- Exception handling is implemented to handle errors in file naming.
- Additional functions, like `difficulty()` and `update_clue()`, enhance the user experience by facilitating difficulty selection and updating the displayed word clues.
- The game provides feedback to the user on whether they have won or lost.

Overall, the project offers an interactive and enjoyable Hangman experience with customizable difficulty levels and customizable secret word list.
