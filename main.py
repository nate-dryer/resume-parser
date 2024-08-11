# main.py
import os
from document_processing import read_pdf, read_docx
from assistant_setup import client, assistant
from schema import ResumeSchema

def process_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith('.pdf'):
            content = read_pdf(file_path)
        elif filename.endswith('.docx'):
            content = read_docx(file_path)
        else:
            print(f"Unsupported file type: {filename}")  # Specific error message for unsupported file types
            continue  # Skip unsupported files

        # Use the assistant to process this content
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "Extract resume information."},
                {"role": "user", "content": content},
            ],
            response_format=ResumeSchema,
        )

        resume_data = completion.choices[0].message.parsed
        print(resume_data)

if __name__ == "__main__":
    directory_path = "/Users/nathandryer/development/resumes"
    process_directory(directory_path)
