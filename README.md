# Resume Parser

This project is a resume parser that extracts and structures resume data according to the JSON Resume schema. It uses OpenAI's GPT-4o model to assist in parsing and structuring the data.

## Features

- Extracts resume data and structures it according to the JSON Resume schema.
- Supports various sections of a resume including work experience, education, awards, publications, skills, languages, interests, and references.

## Project Structure

- `schema.py`: Defines the data models for the resume sections using Pydantic.
- `assistant_setup.py`: Sets up the OpenAI assistant with the necessary instructions and tools.
- `document_processing.py`: Contains functions for processing resume documents.
- `main.py`: The main entry point for running the resume parser.
- `venv/`: Virtual environment directory.

## Setup

### Prerequisites

- Python 3.8 or higher
- An OpenAI API key

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

2. Create a virtual environment (recommended)
   python3 -m venv venv
   source venv/bin/activate

3. Install the dependencies
   pip install -r requirements.txt

4. Export your OPENAI_API_KEY
   ```sh
   export OPENAI_API_KEY="your_openai_api_key"
   ```

5. Run the main script
   ```sh
   python main.py
   ```
