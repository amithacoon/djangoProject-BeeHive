import vertexai

from vertexai.generative_models import (
    GenerationConfig,
    GenerativeModel,
)


def call_gemini_api(prompt, model_name="gemini-1.5-flash"):
  """
  Calls the Gemini API with a provided prompt and model name.

  Args:
      prompt: The text prompt to send to the Gemini API.
      model_name: The name of the Gemini model to use (optional, defaults to 'gemini-1.5-flash').

  Returns:
      A string containing the response from the Gemini API.
  """

  # Initialize Vertex AI (replace with your project details)
  project_id = "YOUR_PROJECT_ID"
  location = "us-central1"  # Adjust location as needed
  vertexai.init(project=project_id, location=location)

  # Create a GenerativeModel object
  model = GenerativeModel(model_name)

  # Configure the generation request
  config = GenerationConfig(prompt=prompt)

  # Generate text content using the Gemini model
  response = model.generate_content(config=config)

  # Return the generated text
  return response.text
