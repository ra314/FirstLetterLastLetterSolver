This program solves the game [First Letter Last Letter](https://www.thegamegal.com/2010/09/01/first-letter-last-letter/) for a given list of words.

The game is a turn based 2 player game.
On the first turn, the first player can pick and say any word.
On subsequent turns the current player must pick a word whose first letter is the same as the last letter of the previously said word.
No word can be repeated twice.
You lose if you have no words that you can say that follow the rule.

The solver uses the minimax algorithm.
The names should be provided separated by spaces in a file called "names.txt".
