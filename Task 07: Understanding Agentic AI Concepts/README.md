# 🧠 Task 07: Understanding Agentic AI Concepts

Link to code: [01\_ai\_agents\_first](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first)

This task will help you understand some important concepts behind how OpenAI's Agent SDK is built.

---

### ❓ 1. Why is the `Agent` class defined as a `dataclass`?

Using `@dataclass` in Python makes it easy to create classes that store data.

✅ Benefits:

* It automatically adds useful methods like `__init__`, `__repr__`, etc.
* It keeps the code **clean** and **short**.
* The `Agent` class mostly stores data like `name`, `tools`, `instructions`, so it’s perfect for a dataclass.

🔗 [Agent Class Source Code](https://openai.github.io/openai-agents-python/ref/agent/)

---

### 🧾 2a. What are `instructions` in the Agent class? Why can it be a **callable**?

`instructions` are like the **system prompt** – they tell the agent what kind of role it should play.

🧠 Example: “You are a helpful assistant.”

👉 Sometimes, we want these instructions to **change based on the situation**. That’s why `instructions` can also be a **callable function** – to generate the prompt dynamically.

---

### 👤 2b. Why is the **user prompt** passed in the `run` method, not stored in the Agent?

The **user prompt** is the actual question or task given by the user at runtime.

It is passed into the `Runner.run()` method like this:

```python
Runner.run(user_input)
```

💡 This makes sense because:

* The Agent should stay fixed.
* The **user input changes every time**, so it should be passed in when the agent runs.

Also, `run()` is a **classmethod** so it can be called without making an object first.

🔗 [Runner Class Reference](https://openai.github.io/openai-agents-python/ref/run/)

---

### 🏃‍♂️ 3. What is the purpose of the `Runner` class?

The `Runner` class is responsible for:

* Managing how the agent runs step-by-step.
* Taking the user's input and passing it through the agent.
* Calling tools if needed.
* Returning the final answer.

🎯 In simple words: **Runner is the controller that runs the agent.**

---

### 📦 4. What are generics in Python? Why do we use `TContext`?

**Generics** let us write flexible and reusable code.

Example:

```python
from typing import TypeVar, Generic

T = TypeVar('T')

def get_first_item(items: list[T]) -> T:
    return items[0]
```

Here, `T` can be **any type** (string, number, object, etc.)

🧠 Why use `TContext`?

* `TContext` is a generic that represents the context passed to the agent.
* It could be anything (user info, conversation state, etc.)
* Using generics makes the Agent framework **reusable for all kinds of situations**.
