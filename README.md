# 📖 Sliding Window String Matcher

This project scans an input string look for pairs of "a" and "b" that are exactly five positions apart (there will be four characters between)
Both a....b and b....a are supported and ALL matches are reported at the end with their respective positions.

This was my first real project in Python after a six year hiatus. It was built to practice:

1. iteration over strings
2. avoiding index errors with boundary checks
3. conditional logic
4. reporting results clearly

---

## ⚙️ How It Works

1. Program takes a string input from the user.
2. The string is converted to lowercase for case-insensitive matching.
3. Each index is checked against the character
4. If the pair is `a...b`, or `b...a` the program records the match
5. At the end the total number of matches is reported.

---

### Definition of "Five Apart"

Characters are considered "five apart if the second character is at `i + 5`.

Example: in the string `axxxxb`, the `a` at index `0` and the b at index `5` are **five apart** (with four characters between them)

---

### 💻 Example Usage

```bash
$ python matcher.py
input a string ababababa
Match at 0 and 5
Match at 1 and 6
Match at 2 and 7
Match at 3 and 8
Scanned exactly 4 matches!

$ python matcher.py
input a string axxxb
No matches
```

### 🧪 Edge Cases

1. Strings shorter than 5 characters are rejected with a message.
2. String capitalization is irrelevant.
3. Multiple and overlapping matches are reported.
4. Non-alphabetic characters are treated the same as any other other character

---

### 🚀 Future Improvements

1. Make the gap configurable (not just 5)
2. Allow matching arbitrary character pairs
3. Package as a CLI tool with command-line flags.

---

### 📜 License

This project is protected under the MIT liscense
    Plain English: You can use, modify, and share this code however you'd like - even commercially. Just keep the liscense notice, and note that it's provided as-is with no warranty.

### ✍️ To Wrap Up

It has been a long time since I've wrote a real program in Python by myself. This code is messy (A lot of `if/elif/else`, a variable for user input followed by another variable to make it lowercase, and most unforgivable of all: no comments), and could be significantly optimized. I could have copied and pasted it into and from ChatGPT to make it cleaner, but I didn't because I want the option to look back at this as a reminder of how far I've progressed. Thank you for viewing my repository. 😁
