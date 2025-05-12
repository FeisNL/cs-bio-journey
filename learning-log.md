📚 **Study Journal**

---

### ✅ 5 May 2025 — Setup & Core Concepts
**What I did:**
- Set up the GitHub repository for tracking my study progress
- Created and committed the initial version of `learning-log.md`
- Started the MITx 6.00.1x Computer Science course
- Learned the difference between algorithms and programs
- Reviewed what computation really is, and debunked common CS myths

---

### ✅ 6 May 2025 — Syntax, Semantics & Architecture
**What I did:**
- Reformatted and organized the learning log in Markdown
- Practiced using `git add`, `git commit`, and `git push`
- Studied:
  - Stored-program vs fixed-program computers
  - Syntax vs static semantics vs dynamic semantics in code

---

### ✅ 7 May 2025 — Biology & Anki Decks
**What I did:**
- Completed the biology learning sequence
- Scored 8/8 on quiz questions
- Created an Anki deck: **Biochem Set 1**
- Practiced spaced repetition for 10 minutes
- Logged key challenges and small wins

---

### ✅ 8 May 2025 — Lecture 2 + Problem Set 1 (Newton's Method)
**What I did:**
- Completed first 12 slides of Lecture 2 (MITx 6.00.1x)
- Practiced `if`, `else`, and `while` with finger exercises
- Tackled Problem Set 1 – Question 1 (Newton’s Square Root)
- Learned Newton’s update rule:

  `x = x - f(x)/f'(x)` → `guess = guess - (((guess ** 2) - a) / (2 * guess))`

- Committed working code (`ps1_scratch.py`)
- Summarized Newton’s Method in a PDF

**What was challenging:**
- Understanding where `f'(x) = 2x` comes from
- Linking visual slope with the formula
- Asking questions without feeling overwhelmed

**Points to improve:**
- Sketch graphs to visualize slope
- Write key ideas in my own words
- Accept that learning deeply takes time

---

### ✅ 10 May 2025 — Counting Substrings with For Loops
**What I did:**
- Completed walkthrough of `count 'bob'` problem from Problem Set 1
- Learned and practiced the **sliding window technique** using `s[i:i+3]`
- Understood correct loop boundaries: `for i in range(len(s) - 2):`
- Identified and corrected common beginner mistakes:
  - Using `count =+ 1` instead of `+=`
  - Looping with `range(len(s))` instead of `len(s) - 2`
  - Forgetting to use `str()` in `print()`

**What was challenging:**
- Realizing that I couldn’t use `for char in s` for slicing with indexes
- Understanding why `range(len(s) - 2)` works and not `-3`

**Points to improve:**
- Practice writing loop logic from scratch
- Try short “fix the syntax” quizzes to internalize structure
- Keep asking why — not just copying patterns

**Notes:**
- It’s totally normal to struggle with this at first — combining slicing, indexing, conditionals and counters is hard at the start
- But I understood it and can now explain it back confidently!

## 🗓️ Summary for 11–12 May 2025 – Week 1 Days 6 & 7
### ✅ What I Accomplished

**Saturday (11 May)**
- Completed `ps1_scratch.py` prototype of Newton’s Method
- Learned how to safely accept user input using `try/except`
- Refactored code to validate input and prevent crashes
- Learned the importance of `main()` and `if __name__ == "__main__":`
- Fixed common bugs: `guesss`, extra parentheses, indentation, and scope issues

**Sunday (12 May)**
- Finalized and cleaned up `ps1.py` for submission
- Wrote detailed print statements with guess + step counter
- Saved the final version into the problem set folder
- Generated a fully documented Word summary for `ps1.py`
- Committed and pushed `ps1.py` to GitHub using best Git practices

### 💡 What I Learned
- How Newton’s method approximates square roots via iteration
- How scope, indentation, and user validation affect real-world Python scripts
- How to structure scripts professionally using `main()` and entry points
- How to use Git to track versions and organize problem sets clearly