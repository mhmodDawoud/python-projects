# Vowel Translator

A small Python program that takes a phrase from the user and replaces every vowel with a star (`*`).

## What does it do?

The vowels are: `a`, `e`, `i`, `o`, `u`.
The program goes through the phrase letter by letter:

- If the letter is a vowel (uppercase or lowercase), it is replaced with `*`.
- If the letter is not a vowel, it stays the same.

## How it works

1. `translate(str)` creates an empty text called `translation`.
2. A `for` loop takes each letter of the phrase.
3. `letter.lower()` turns the letter to lowercase, so `A` and `a` are both checked as vowels.
4. If the letter is in `"aieoue"`, `*` is added to `translation`. Otherwise the same letter is added.
5. At the end, the function returns the new text.
6. `input()` asks the user for a phrase, and `print()` shows the result.

## How to run

1. Install Python 3.
2. Save the code in a file, for example `translate.py`.
3. Open a terminal in the same folder and run:

```
python translate.py
```

## Example

```
Enter a phrase: Hello World
H * ll *  W * rld
```

```
Enter a phrase: Python
Pyth * n
```

## Notes

- The `if letter.isupper()` check does the same thing in both branches, so you can remove it and the result will be the same.
- `str` is the name of a built-in Python type. It is better to name the parameter `text` or `phrase`.
- The letter `e` appears twice in `"aieoue"`. It works, but `"aeiou"` is enough.
