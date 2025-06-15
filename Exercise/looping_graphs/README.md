# 🎯 Automatic Higher or Lower Game

## 🧠 Exercise for Graph V

### Your Task

Implement an **Automatic Higher or Lower Game** using a guessing graph.

The goal is for the graph (automated guessing agent) to determine a hidden number between **1 and 20** by guessing intelligently based on hints.

---

### 🔍 Game Rules

* The graph makes a guess and receives a **hint**:

  * **"higher"** if the guess is too low
  * **"lower"** if the guess is too high
  * If the guess is correct, the game **stops**
* The graph has a **maximum of 7 guesses**
* The graph should update its **lower and upper bounds** after each guess
* The game stops when:

  * The correct number is guessed
  * **OR** the graph reaches **7 attempts**

---

### 🔢 Input Format

```json
{
  "player_name": "Student",
  "guesses": [],
  "attempts": 0,
  "lower_bound": 1,
  "upper_bound": 20
}
```

---

### 💡 Hint

Update the bounds after every guess based on the response from the hint node:

* If hint is `"higher"` → set `lower_bound = guess + 1`
* If hint is `"lower"` → set `upper_bound = guess - 1`

---

### ✅ Objective

Build a graph-based system that:

* Guesses a number within a range intelligently (e.g., using binary search)
* Uses the hints to narrow down the possible range
* Stops correctly when the number is found or max attempts are reached

---

### 📌 Example

Let’s say the number to guess is **13**.

1. Guess: 10 → Hint: “higher”
2. Guess: 15 → Hint: “lower”
3. Guess: 13 → Correct! 🎉

---

### 🛠️ Technologies

* Graph V framework (as shown in the provided course/video)
* Python or any logic-based backend to simulate the game