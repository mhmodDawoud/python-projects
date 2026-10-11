# Password Generator

A small Python program that asks the user for a password length and then generates a random password made of letters, digits and symbols.

## What does it do?

1. Shows a colored banner at the start and at the end (using `pyfiglet` and `termcolor`).
2. Asks the user how many characters the password should have.
3. Checks the input:
   - If it is not a number, it asks again.
   - If it is less than 6, it asks again.
4. Builds the password from four groups of characters:
   - lowercase letters (`a-z`)
   - uppercase letters (`A-Z`)
   - digits (`0-9`)
   - symbols (like `!@#$%`)
5. Prints the password.

## How it works

1. `string.ascii_lowercase`, `string.ascii_uppercase`, `string.digits` and `string.punctuation` give the characters of each group.
2. `list(...)` turns each group into a list, and `random.shuffle(...)` mixes each list.
3. `part_1` and `part_2` are 30% of the length each.
4. The first loop adds one lowercase and one uppercase letter, `part_1` times.
5. The second loop adds one digit and one symbol, `part_2` times.
6. `"".join(password)` joins the list into one text and `print` shows it.

## Requirements

Install the two libraries once:

```
pip install termcolor pyfiglet
```

## How to run

1. Install Python 3.
2. Save the code in a file, for example `password.py`.
3. Open a terminal in the same folder and run:

```
python password.py
```

## Example

```
Enter number of character for the password: 10
tEeFjG6{2:5!
```

## Known issues (good things to fix next)

- **The length is not exact.** The program builds `4 x 30%` of the number, which is about 120%. When you enter 10 you get 12 characters, and when you enter 20 you get 24.
- **It crashes with big numbers.** There are only 10 digits, so entering 36 or more gives `IndexError: list index out of range`.
- **The pattern is predictable.** The password is not shuffled at the end, so it always has letters first, then digits and symbols at the end.
- **Not safe for real passwords.** The `random` module is not made for security. For real passwords use the `secrets` module.

## Ideas to improve it

- Shuffle the final password with `random.shuffle(password)`.
- Make the final length exactly the number the user entered.
- Let the user choose if they want symbols or digits.
