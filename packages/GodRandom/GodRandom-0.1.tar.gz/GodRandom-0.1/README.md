
# GodRandom - A Simple Library for Generating Random Data

**Note:** This is my first library, so please don't judge too harshly. If you have questions, feel free to reach out! 😊  

## Installation

Install via pip:  

```bash
pip install godrandom
```  

Or download the source code and install it locally:  

```bash
pip install .
```  

Alternatively, clone the repository:  

```bash
git clone https://github.com/Dron3916/GodRandom.git
```  

## Usage  

First, import the library:  

**`test.py`**  

```python
from GodRandom import Random

# Your API key
api = "YOUR API KEY FROM RANDOM.ORG!"

# Example usage
# Basic check
Random.hello()

# Generate random integers
data_int = Random.get_randint(api=api, min=1, max=5, amount=4, replacement=True)  # 'replacement' defaults to False

# Generate random decimals
data_dec = Random.get_randdec(api=api, amount=4, decimalPlaces=2)

# Generate random UUIDs
data_uuid = Random.get_randuuid(api=api, amount=1)

# Generate random strings
data_string = Random.get_randstring(api=api, amount=1, length=4, characters="abcdifghufslpo")

# Get API usage information
data_user = Random.get_api_info(api=api)

# Print all generated data
print(data_int, data_dec, data_uuid, data_string, data_user)
```  

## Parameters  

Here is a quick reference for key parameters used in the library:  

- **`api`**: Your API key from RANDOM.ORG. Ensure it is valid and active.
- **`min`** (int): Minimum value for generating integers.
- **`max`** (int): Maximum value for generating integers.
- **`amount`** (int): Number of random values to generate.
- **`replacement`** (bool): Whether values can repeat (default: `False`).
- **`decimalPlaces`** (int): Number of decimal places for random decimals. Example:  
  - `decimalPlaces=1` → `0.1`
  - `decimalPlaces=5` → `0.00000`
- **`length`** (int): Length of each generated string (must be between 1 and 32). All strings will have the same length.
- **`characters`** (str): A string containing the set of characters to be used in random strings. The maximum length is 128 characters.  

## Features  

The library is simple and easy to use. It provides the following functionalities:  

1. Generate random integers (`get_randint`)  
2. Generate random decimal numbers (`get_randdec`)  
3. Generate random UUIDs (`get_randuuid`)  
4. Generate random strings (`get_randstring`)  
5. Get your API usage details (`get_api_info`)  

Feel free to explore and use it in your projects! 🎉  
