# AI Outfit Recommendation Agent 👕🤖

A simple **Reflex-Based Agent** implemented in Python that recommends suitable clothing based on the current **weather condition** and **time of day**.

This project is part of **Artificial Intelligence – Assignment #1**.

## 📌 Project Description

The agent receives two inputs from the user:

- **Weather condition**
- **Time of day**

Based on these inputs, the agent applies a set of predefined rules and provides a suitable outfit recommendation.

## 🧠 How It Works

The agent uses a **rule-based decision system**.

It checks the user's weather and time, then selects the appropriate recommendation.

### Supported Weather Conditions

- `sunny`
- `rainy`
- `snowy`
- `cloudy`

### Supported Times

- `morning`
- `afternoon`
- `evening`
- `night`

## 📋 Rules

| Weather            | Time                          | Recommendation                                       |
| ------------------ | ----------------------------- | ---------------------------------------------------- |
| Sunny              | Morning / Afternoon           | Wear light clothing and a sunhat.                    |
| Rainy              | Morning / Afternoon           | Wear a waterproof jacket.                            |
| Rainy              | Night                         | Wear warm waterproof clothing and carry an umbrella. |
| Snowy              | Morning / Afternoon / Evening | Wear heavy winter clothing.                          |
| Other combinations | Any                           | Default recommendation                               |

## 🛠️ Technologies

- Python 3
- Conditional Statements (`if`, `elif`, `else`)
- Functions
- User Input

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```
