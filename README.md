# Python-Calulator
# Simple Python GUI Calculator

A very simple calculator application built using Python and the Tkinter library. This project is meant to demonstrate the use of basic GUI components, button actions, and evaluation of mathematical expressions in a simple and minimal calculator layout.

![Calculator Screenshot](screenshot1.png)

---

## ✨ Features

- GUI built with Tkinter  
- Supports:  
  - Basic arithmetic operations: `+`, `-`, `*`, `/`  
  - Parentheses `(` and `)`  
  - Decimal point `.`  
  - Clear (`C`) and Backspace (`back`) functions  
  - Rounded result to 2 decimal places  

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### How to Run

1. Clone the repository:
```
git clone https://github.com/your-username/simple-gui-calculator.git
cd simple-gui-calculator
```

2. Run the Python script:  
- python calc.py


---

## 🧠 How it Works

- The calculator uses a global `expression` variable to store the current input string.  
- Button clicks append characters to this expression.  
- `eval()` is used to evaluate the final expression when the `=` button is clicked.  
- Exception handling is in place to catch invalid expressions.  
- Results are rounded to two decimal places using Python's `round()`.  

---

## 📁 Project Structure
```
simple-gui-calculator/
├── calculator.py # Main application script
├── README.md # Project README file
└── screenshot.png # UI screenshot (optional)
```


---

## 🔧 Possible Improvements

- Add keyboard support  
- Add support for square root, power, etc.  
- Improve UI design and responsiveness  
- Add history of calculations  

---

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙌 Acknowledgements

Built with ❤️ using Python and Tkinter.


