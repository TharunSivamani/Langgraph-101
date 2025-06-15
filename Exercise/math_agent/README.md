# 🏗️ Graph II – Arithmetic Node Exercise

### 📌 Task Description

Create a **Graph node** that accepts:

* A list of integers (`values`)
* A name (`name`)
* An operation (`operation`) – either `"+"` for addition or `"*"` for multiplication

The node will perform the operation **within the same node** and return a formatted message with the result.

---

### 🧠 Logic

* If `operation == "+"`, **add** all integers in the list.
* If `operation == "*"`, **multiply** all integers in the list.
* Return the result in the format:
  👉 `"Hi <name>, your answer is: <result>"`

---

### 🧾 Example

**Input:**

```json
{
  "name": "Jack Sparrow",
  "values": [1, 2, 3, 4],
  "operation": "*"
}
```

**Output:**

```
Hi Jack Sparrow, your answer is: 24
```

---

### 💡 Hint

> You need an `if`-statement inside the node logic to decide between addition and multiplication.
