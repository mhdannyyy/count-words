# Program 1: Count Words

## 1. What the Program Does

This Python program counts the number of words in a sentence entered by the user. It uses the `split()` method to separate the sentence into words and `len()` to count them. If the user enters an empty sentence or only spaces, the program displays "No sentence was entered."

## 2. How to Run the Program

1. Install Python 3 on your computer.
2. Save the source code as `count_words.py`.
3. Open a terminal in the folder containing the file.
4. Run the command `python count_words.py`.
5. Enter a sentence when prompted and press Enter.

## 3. Test Results

| Test Case       | Input                | Expected Result          | Status |
| --------------- | -------------------- | ------------------------ | ------ |
| Normal sentence | `I love programming` | Number of words: 3       | Pass   |
| Empty input     | Press Enter          | No sentence was entered. | Pass   |
| Spaces only     | `   `                | No sentence was entered. | Pass   |
| Single word     | `Hello`              | Number of words: 1       | Pass   |

## 4. One Limitation

The program counts words based on spaces and whitespace rather than understanding the meaning of a sentence. For example, `hello,world` is counted as one word because there is no space between the two words.
