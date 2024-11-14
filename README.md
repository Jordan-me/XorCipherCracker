# XOR Cracking Project

This project aims to implement an XOR cracking technique to decipher encrypted data. It supports XOR cracking based on a given key length and various cryptographic analysis methods. The project is structured for ease of understanding and maintainability.

## Project Structure

The project is organized into several folders, each serving a distinct purpose:  
- **/project-root**
  - **/resources/**: Store input-output-related files
    - `ciphers.txt`: Input cipher text (you need to provide key-length and beneath provide the cipher)
    - `decrypt_ciphers.txt`: Decrypted cipher text output
  - **/xor_encryption_decryption/**: Store encryption and decryption-related scripts
    - `encryption.py`: Script for encryption/decryption functions
    - `key_guessing.py`: Script for guessing encryption keys given key length known
  - **/analysis/**: Store analysis and score-related scripts
    - `grams_analysis.py`: Script for n-gram analysis
    - `score_english.py`: Script for scoring decrypted text against the English language
  - **/utils/**: Store utility and helper scripts
    - `utils.py`: Helper functions
    - `consts.py`: Constants used throughout the project
  - **/tests/**: Store test scripts
    - `test.py`: Unit tests for project components
  - `main.py`: Main entry point for the project
  - `.gitignore`: Git ignore file
    
## Requirements

To run this project, you need to have Python installed on your local machine. You may also want to create a virtual environment for managing dependencies. 

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jordan-me/XorCipherCracker.git
    ```

2. Navigate into the project directory:

    ```bash
    cd XorCipherCracker/
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

## Usage

### Running the main script:

The main script, `main.py`, is the entry point for the project. You can run it as follows:

```bash
python main.py
```