🔑 Python Password Generator and Strength Checker
🚀 Features

* **Customizable Length:** Generate passwords between 8 and 50 characters long.
* **Character Selection:** Choose to include uppercase letters, lowercase letters, numbers, and custom symbols.
* **Strength Assessment:** Provides a subjective rating (**Weak**, **Medium**, or **Strong**) based on length and character diversity.

📋 Prerequisites

Python 3.x: The script is written in standard Python 3 and requires no external libraries beyond the built-in `random` and `string` modules.

⚙️ How to Run the Script

1.  Save the Code:Save the provided code into a file named `password_generator 1.py`.
2.  Open Terminal: Navigate to the directory where you saved the file.
3.  Execute: Run the script using the Python interpreter:

    ```bash
    python3 password_generator 1.py
    ```

4.  Follow Prompts: The script will guide you through entering the desired password length and the character types to include.

---

 📖 Code Overview

The script is divided into two main functions and a primary execution loop (`try...while True`):

### `make_password(length, upper, lower, numbers, symbols)`

This function is responsible for the generation logic.

* It builds a pool of available characters (`chars`) based on the boolean flags (`upper`, `lower`, `numbers`, `symbols`).
* It then loops `length` times, randomly selecting a character from the pool for each position.
  Note: If no character types are selected, it returns an empty string, which the main loop catches.

### `check_strength(password)`

This function assigns a strength score to the generated password based on a simple heuristic:

1.  Length Points:
    * `+1` point for length $\ge 8$.
    * `+2` points for length $\ge 12$.
2.  Character Diversity Points:
    * `+1` point for having at least one uppercase character.
    * `+1` point for having at least one lowercase character.
    * `+1` point for having at least one digit.

The total score is translated into a rating:
Weak: Score $< 3$
Medium: Score $3$ or $4$
Strong: Score $\ge 5$

 ⚠️ Security Notes

Character Set

The symbols used in this generator are: `!@#$%^&*()-_=+`

 Strength Metric Limitations

The `check_strength` function provides a **subjective, heuristic-based rating**. For a more mathematically rigorous assessment of security, the **entropy** (measured in bits) of the password should be calculated.
