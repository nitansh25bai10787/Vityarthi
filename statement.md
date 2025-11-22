 📝 Project Statement: Simple Password Generator
 1. ❓ Problem Statement

In an increasingly digital world, users often rely on simple, memorable, and insecure passwords, making their accounts vulnerable to dictionary attacks and brute-force methods. The goal of this project is to address this security gap by providing a simple, accessible, and locally executed tool that generates highly random, customizable passwords and provides an immediate, heuristic-based assessment of their complexity.

🎯 2. Scope of the Project

The scope of this project is intentionally narrow and focused on core password utility:

Generation: Generating random strings based on user-specified length and character sets (uppercase, lowercase, numbers, and a fixed set of symbols).
Assessment: Providing a basic, subjective rating (Weak, Medium, Strong) based on length thresholds and character diversity.
Execution Environment: The solution is a standalone Python script intended for command-line execution (CLI) and does not require external libraries beyond Python's standard distribution (`random` and `string`).
Exclusions: The scope does not include advanced features like:
    * Entropy calculation (a more mathematical strength metric).
    * Saving or storing generated passwords (for security reasons).
    * Graphical User Interface (GUI).
    * Checking against known compromised passwords (e.g., Have I Been Pwned lists).

👥 3. Target Users

The primary target users are individuals who need a quick and easy way to create strong passwords without relying on web-based services.

Casual Computer Users: Individuals who are aware of the need for strong passwords but lack a dedicated password manager.
Developers/IT Professionals: Users who need to quickly generate secure keys or passwords for testing, configuration, or temporary access.
Students Learning Python: The code serves as a practical, easy-to-understand example of combining user input, randomization, and conditional logic.

✨ 4. High-Level Features

The tool provides the following core capabilities:

A. Password Generation
Length Control: Allows users to define a password length between 8 and 50 characters.
Customizable Character Set: Users can toggle the inclusion of four character types:
    1.  Uppercase letters (`A-Z`)
    2.  Lowercase letters (`a-z`)
    3.  Numbers (`0-9`)
    4.  A fixed set of symbols (`!@#$%^&*()-_=+`)

B. Password Strength Check
Heuristic Rating: Provides a rating of "Weak," "Medium," or "Strong" based on a weighted point system.
Scoring Factors: The strength score is calculated based on:
* Meeting a minimum length threshold (8 and 12 characters).
* The presence of at least one character from each selected category (uppercase, lowercase, and digits).

C. User Interface
Command Line Interface (CLI): Fully interactive via text prompts.
Error Handling: Catches invalid length inputs and ensures at least one character type is selected before attempting generation.
