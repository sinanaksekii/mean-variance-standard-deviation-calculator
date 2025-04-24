# 📊 Mean, Variance, and Standard Deviation Calculator

This project is part of the **Data Analysis with Python** certification curriculum by [freeCodeCamp](https://www.freecodecamp.org/). It demonstrates how to perform fundamental matrix statistics using **NumPy** in Python.

The goal is to compute mean, variance, standard deviation, max, min, and sum values across rows, columns, and the flattened version of a 3×3 matrix.

---

## 🚀 Features

- ✅ Input validation (raises `ValueError` if input list length ≠ 9)
- ✅ NumPy-powered matrix reshaping and aggregation
- ✅ Returns all results in a structured Python dictionary
- ✅ Thorough unit testing support (`test_module.py`)

---

## 🧠 Example Usage

```python
from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

Returns:

{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.666..., 0.666..., 0.666...], 6.666...],
  'standard deviation': [[2.44..., 2.44..., 2.44...], [0.81..., 0.81..., 0.81...], 2.58...],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

🗂️ Project Structure
├── mean_var_std.py       # Main function logic
├── main.py               # Development/test runner
├── test_module.py        # Unit tests (freeCodeCamp format)
└── README.md             # Project documentation

📦 Technologies Used

Python
NumPy

👤 Author
Sinan Akseki
🔗 GitHub • LinkedIn

🎓 License
This project is part of the freeCodeCamp curriculum.
Feel free to fork, learn, and build upon it for educational purposes.