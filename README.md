# Selenium-Test-
Tests using Selenium WebDriver programmed in Python. 

# What this code does

The following script performs the following actions:

1. Opens Mercado Libre.
2. Selects the country (Mexico in this example).
3. Types **"Playstation 5"** into the search bar and starts the search.
4. Applies filters by selecting **New** and **Local**.
5. Sorts the results from **highest price to lowest price**.
6. Saves the first 5 items and prints them in the console.

---

## Requirements to run this script

- Python installed (Version 3.X recommended)
- Google Chrome installed
- `chromedriver.exe` file in the same folder where the Python script is located
- Chrome and Chromedriver versions **must match**  
  (It's recommended to download the latest chromedriver and update Chrome as well)

---

## How to run the script

1. Clone or download this repository.
2. Make sure `chromedriver.exe` is in the same folder as the script `Test_Mercado_libre.py`.
3. Install dependencies: `pip install selenium`
4. Run the script: ` python Test_Mercado_libre.py`
