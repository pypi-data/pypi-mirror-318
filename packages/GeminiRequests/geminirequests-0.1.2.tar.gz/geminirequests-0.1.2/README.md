# GeminiRequests

**GeminiRequests** is a Python library (and code example) designed for interacting with Google’s **Gemini AI** text generation model using the `requests` library.  
This code provides the `Gen` class, which allows you to store dialogue history, send requests to the API, load/save conversation history, and more.  
**Note:** The last message in the dialogue history **must** always be from the user when generating text.



## Features

1. **Easy integration with Gemini AI**:  
   Uses the standard `requests` library to send HTTP requests to Google’s Gemini AI API.

2. **Dialogue history management**:  
   The `Gen` class keeps track of conversation history (a list of messages with roles and text), making it highly useful for context-dependent tasks.  
   **Important:** Ensure the last message in the history is from the user before calling `generate()`.

3. **Convenient export and import methods**:  
   - `export_history(filename)` / `import_history(filename)`  
   - `import_history_anyway(filename)` (attempts to load history and creates a file if it doesn’t exist)

4. **API key management**:  
   On the first run, it automatically creates a `gemini_api_key` file (in the `GeminiRequests` folder) where you can save your API key.

---

## Installation and Setup
### Installing from PyPI
   ```bash
   pip install GeminiRequests
   ```

### GitHub
1. **Clone the repository** (or copy this code into your project):  
   ```bash
   git clone https://github.com/Python-shik/GeminiRequests.git
   ```

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
   If you’re only using this module, you can simply install:
   ```bash
   pip install requests
   ```

#### Set up the API key:  
   - On the first run, the script will ask you to enter your Gemini AI API key.
   - The key will be saved in the `GeminiRequests/gemini_api_key` file.

---


## Usage

Assume the file with the `Gen` class is stored in the `GeminiRequests` folder. Example:

```python
from GeminiRequests import Gen  # Assuming the file is named gen.py

# Create an instance of the class. 
# On the first run, you’ll be prompted to enter your API key if the gemini_api_key file is missing.
ai = Gen()

# Add some messages to the dialogue history
ai.history_add(role="user", content="Hello, Gemini!")
ai.history_add(role="model", content="hey.")

# Ensure the last message in the history is from the user
ai.history_add(role="user", content="What else can you do?")

# Generate a response
response = ai.generate()
print("Response from Gemini AI:", response)

# Save the history
ai.export_history("dialog_history.pkl")

# Clear local history (from memory)
ai.history = []

# Load history again if needed
ai.import_history("dialog_history.pkl")
```

### The `Gen` Class and Its Methods

- **`Gen(history=[], system_instructions=None)`**  
  Constructor. On the first run, it creates a `gemini_api_key` file if it doesn’t exist.  
  - `history`: a list of dictionaries like `{"role": ..., "parts": [{"text": ...}]}`, describing the current conversation history.  
  - `system_instructions`: a list of instructions sent as part of the request (essentially "prompts" or "context" from the system).

- **`history_add(role, content)`**  
  Adds a new message (role and text) to the dialogue history.

- **`generate()`**  
  Sends the dialogue history (and system instructions, if any) to the API and retrieves the generated text.  
  **Important:** Ensure the last message in the history is from the user before calling this method.

- **`export_history(filename)` / `import_history(filename)`**  
  Save/load the dialogue history to/from a file using `pickle`.

- **`import_history_anyway(filename)`**  
  Attempts to load the history from a file. If the file doesn’t exist, it creates one and retries.

- **`clear_history(filename)`**  
  Deletes the history file and clears the history from memory.

---


## License

This project is distributed under the **MIT License**.  
You are free to modify and use the code in your projects, including commercial ones.

---

## Author

Developed by [Illya Lazarev](https://github.com/Python-shik)  
Email: sbdt.israel@gmail.com

If you have ideas or suggestions for improvements, feel free to submit pull requests or open an [Issue](https://github.com/Python-shik/GeminiRequests/issues).

