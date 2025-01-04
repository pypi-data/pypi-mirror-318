# inp_kwargs
**Easily validate user inputs with Python, no hassle required!**

A Python library for easy input validation using kwargs. This library helps to easily validate inputs such as integers, strings, and more, without needing to write complex validation logic.

## Example

### Validating an Integer Input

```python
from inp_kwargs import input_int

# Request a number between 1 and 100
number = input_int("Enter a number between 1 and 100: ", 
                   error_txt="Error: You have to input an integer.",
                   min_value=1, 
                   error_min="Error: The number must be greater than or equal to 1.",
                   max_value=100, 
                   error_max="Error: The number must be less than or equal to 100.")

print(f"You entered: {number}")

# Request a number between 1 and 100 without custom error messages
number = input_int("Enter a number: ", min_value=1, max_value=100)
print(f"You entered: {number}")

```

# `input_int` Function Validations

The `input_int` function supports the following validation options:

### 1. **Minimum Value** (`min_value`)
   - Ensures the input is greater than or equal to the specified minimum value.
   - **Usage**: `min_value=10`

### 2. **Maximum Value** (`max_value`)
   - Ensures the input is less than or equal to the specified maximum value.
   - **Usage**: `max_value=100`

### 3. **Range** (`range`)
   - Ensures the input is in the specified range of values.
   - **Usage**: `range=[10, 20, 30]`

### 4. **Allowed Values** (`allowed_values`)
   - Ensures the input matches one of the allowed values.
   - **Usage**: `allowed_values=[5, 10, 15]`

### 5. **Even Number** (`even`)
   - Ensures the input is an even number.
   - **Usage**: `even=True`

### 6. **Odd Number** (`odd`)
   - Ensures the input is an odd number.
   - **Usage**: `odd=True`

### 7. **Multiple of** (`multiple_of`)
   - Ensures the input is a multiple of a specified number.
   - **Usage**: `multiple_of=5`

### 8. **Type Error Message** (`type_error_message`)
   - Customizes the error message when the input is not a valid integer.
   - **Usage**: `type_error_message="Invalid input!"`

## Features
- Validate integer inputs with custom error messages.
- Set minimum and maximum value constraints.
- Simple and reusable functions for input validation.


## Installation
You can install inp_kwargs directly from PyPI:
```bash
pip install inp_kwargs
```

## License
MIT License. See the LICENSE file for more details.