# 🛹 Exercise for Graph IV

## 🧠 Your Task

Build the graph as shown in the image!
You will need to **make use of 2 conditional edges** to direct the flow.

---

## ⚙️ Graph Structure

The graph follows this structure:

```
              _start_
                 |
              router
             /      \
  addition_operation  subtraction_operation
         |                     |
     add_node           subtract_node
             \         /
               router2
             /        \
  addition_operation2  subtraction
         |                    |
     add_node2           subtract_node
              \        /
               __end__
```

---

## 🧾 Input

```python
initial_state = AgentState(
    number1 = 10,
    operation = "-",
    number2 = 5,
    number3 = 7,
    number4 = 2,
    operation2 = "+",
    finalNumber = 0,
    finalNumber2 = 0
)
```

---

## 📤 Expected Flow

* Step 1: Based on `operation`, go to either `add_node` or `subtract_node`.
* Step 2: Based on `operation2`, go to `add_node2` or `subtract_node`.
* Step 3: Finish at `end`.

> Use conditional routing to move through `router` and `router2` accordingly.
