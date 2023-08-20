# Wordlist Generator

Wordlist Generator is a Python script that generates and inserts wordlists into a MariaDB database. It allows you to specify characters, minimum and maximum word length, and generates all possible combinations of characters within the specified length range.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 (at least) installed.
- MariaDB installed and running.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/eduardo45MP/WLG.git
   ```

2. Change to the project directory:

   ```sh
   cd WLG
   ```

3. Install the required Python packages:

   ```sh
   pip install tqdm mariadb
   ```

## Usage

1. Run the `main.py` script:

   ```sh
   python main.py
   ```

2. Follow the prompts to configure the wordlist generation:
   - Enter the name of the wordlist table.
   - Enter the characters to include in the words (e.g., 0123456789).
   - Enter the minimum word length.
   - Enter the maximum word length.

3. The script will create the specified table in the MariaDB database and start generating and inserting wordlists.

## Contributing

Contributions are welcome! Feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License.
