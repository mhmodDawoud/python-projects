# Guessing Game

A small Python game where the player has 3 tries to guess a secret word.

## What does it do?

1. The program has a secret word stored in the code.
2. It asks the player to guess the word.
3. The player has **3 tries**.
4. If the player guesses the word, the program prints a win message.
5. If the player uses all 3 tries without guessing it, the program prints `Out of limit :(`.

## How it works

1. `secret_word` is the word the player must guess.
2. `guess` starts as an empty text, so the loop can start.
3. `guess_limit` is the number of tries left (it starts at 3).
4. The `while` loop keeps running as long as **both** conditions are true:
   - the guess is not the secret word, and
   - there are still tries left (`guess_limit > 0`).
5. Inside the loop, the program asks for a guess and removes one try with `guess_limit -= 1`.
6. After the loop ends, `if guess == secret_word` checks if the player won or lost.

## How to run

1. Install Python 3.
2. Save the code in a file, for example `game.py`.
3. Open a terminal in the same folder and run:

```
python game.py
```

## Example

Winning on the 3rd try:

```
Enter guess word: hello
Enter guess word: test
Enter guess word: MD1
You win :) The secret word is MD1
```

Losing:

```
Enter guess word: a
Enter guess word: b
Enter guess word: c
Out of limit :(
```

## Notes

- **The game is case-sensitive.** `md1` is not the same as `MD1`, so a lowercase guess is wrong. To accept both, compare with `guess.upper() == secret_word`.
- **The old version is commented out.** The first part of the file (lines starting with `#`) is an older version that used a flag called `out_of_guesses`. It does the same job, but the new version is shorter and easier to read.
- **To change the number of tries,** change the value of `guess_limit`.
- **To change the secret word,** change the value of `secret_word`.

## Ideas to improve it

- Show how many tries are left after each wrong guess.
- Let the player play again after the game ends.
- Choose the secret word randomly from a list of words.
