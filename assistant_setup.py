import os
import openai
from schema import ResumeSchema  # Import the schema you defined

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI()

# Create the assistant with instructions and tool functions
assistant = client.beta.assistants.create(
    instructions="You are a resume parser. Use the provided functions to read documents and extract information according to the JSON Resume schema.",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "extract_resume_data",
                "description": "Extract and structure resume data according to the JSON Resume schema",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_content": {
                            "type": "string",
                            "description": "The content of the resume"
                        }
                    },
                    "required": ["file_content"],
                    "additionalProperties": False
                },
                "strict": True
            }
        }
    ],
    model="gpt-4o"
)

def parse_resume(resume_content):
    """Function to parse resume content using OpenAI assistant"""
    
    response = assistant.call(
        function_name="extract_resume_data",
        function_arguments={"file_content": resume_content}
    )
    
    if 'error' in response:
        raise ValueError(f"Error in resume parsing: {response['error']}")
    
    parsed_data = response.get("result", {})
    return parsed_data

def validate_parsed_data(parsed_data):
    """Validate parsed resume data against the ResumeSchema"""
    
    schema = ResumeSchema()
    validation_result = schema.validate(parsed_data)
    
    if validation_result:
        raise ValueError(f"Schema validation failed: {validation_result}")
    
    return parsed_data

def main():
    # Example resume content, this would normally be read from a file
    example_resume_content = """
    John Doe
    Senior Product Manager
    Email: john.doe@example.com
    Phone: +123456789
    Experience:
    - Senior Product Manager at XYZ Corp, 2018-2023
    - Product Manager at ABC Inc, 2015-2018
    Education:
    - MBA from University of Somewhere, 2012-2014
    - B.S. in Computer Science, 2008-2012
    """
    
    try:
        # Step 1: Parse the resume content
        parsed_data = parse_resume(example_resume_content)
        
        # Step 2: Validate the parsed data against the schema
        valid_data = validate_parsed_data(parsed_data)
        
        print("Parsed and validated resume data:")
        print(valid_data)
        
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()