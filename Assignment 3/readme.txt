Learn to Program: The Fundamentals // Assignment 3

A3 Problem Domain: Word Search Game

For A3, you will implement a word search game. The game involves an rectangular board of uppercase letters that is read from a file. For example, here are the file contents representing a (tiny) 2 row by 4 column board:

ANTT
XSOB
The game also involves a non-empty words list read from a file. For example, here are example file contents for a words list:

ANT
BOX
SOB
TO

To make it a bit more challenging, there may be words in the words list that do not appear in the board, and the word list is not shown to the players.

The object of the game is for the players to view the board and find words (remember that the words list is unknown to the players). Words may be contained in rows (from left to right) or columns (from top to bottom), but not backwards. When a player correctly guesses a word that occurs in the words list, that player is awarded points according to a scoring system described in the starter code. The game ends when all words on the board that appear in the words list have been guessed.

The player with the highest score wins.

The words from the words list and the letters of the board are made up of alphabetic, uppercase characters.

Here is some information about how the functions relate to each other and how they are used in the game:

is_valid_word: checks whether a word that player guessed is in the words list.
make_str_from_row: creates a string from the list of single character strings representing a row. 
make_str_from_column: creates a string from the list of single character strings representing a column. 
board_contains_word_in_row: checks whether a word occurs in any of the rows of the board. 
board_contains_word_in_column: checks whether a word occurs in any of the columns of the board. 
board_contains_word: checks whether a word occurs in any of the rows or columns of the board.
word_score: calculates the score that a correctly guessed word earns. A word that is only 1 or 2 letters long earns 0 points, a word that is 3-6 letters long earns 1 point per letter, a word that is 7-9 letters long earns 2 points per letter, and a word that is 10 or more letters long earns 3 points per letter.
update_score: adds the score that a correctly guessed word earns to a player's score.
num_words_on_board: counts how many words from the words list appear on a particular board.
read_words: creates a words list made up of the words from a file. 
read_board: creates a board made up of the rows of letters from a file. 

=============================================================================================================
Fun stuff: play the game!

The course provided a driver for the game:  a3_driver.py
