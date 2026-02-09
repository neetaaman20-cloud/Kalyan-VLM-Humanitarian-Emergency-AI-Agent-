import ollama

def analyze_image(image_path):
    """
    Analyzes the photo and returns a detailed description 
    of the emergency or medical situation.
    """
    response = ollama.generate(
        model='moondream',
        prompt='Describe the medical emergency or injury in this image concisely for a first responder.',
        images=[image_path]
    )
    return response['response']