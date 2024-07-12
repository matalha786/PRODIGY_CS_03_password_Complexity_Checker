# PRODIGY_CS_03_password_Complexity_Checker

# Password Complexity Checker

This is a GUI-based tool that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The program is built using Python and the `tkinter` library.

## Features

- Check password strength based on:
  - Length
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Provide feedback to improve password strength
- User-friendly GUI
- Scalable and adjustable window layout

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/password-complexity-checker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd password-complexity-checker
   ```

3. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

4. Install the required library (tkinter is usually included with Python, but in some environments you might need to install it):

   ```bash
   pip install tk
   ```
## Usage 1

1. run `password_checker.py`.

## Usage 2

1. Save the script as `password_checker.pyw`.
2. Run the script by double-clicking the `password_checker.pyw` file. The GUI should open without showing a terminal window.

## GUI Layout

- **Enter Password**: Input field to enter the password you want to check.
- **Check Password**: Button to trigger the password strength assessment.
- **Result**: Displays the strength and feedback for the entered password.

## Example

### Password Assessment

1. Enter your password: `Hello123!`
2. Click "Check Password"
3. Result: 
   - Strength: Strong
   - Feedback: Your password is strong.

### Weak Password Example

1. Enter your password: `hello`
2. Click "Check Password"
3. Result: 
   - Strength: Weak
   - Feedback: Password must be at least 8 characters long. Include at least one uppercase letter. Include at least one number. Include at least one special character.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.

