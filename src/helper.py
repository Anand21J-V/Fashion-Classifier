# FOR GENERATING CAPTIONS 

# Generate a caption for the uploaded image
def generate_caption(image):
    img_base64 = image_to_base64(image)
    response = requests.post(
        HF_API_URL_IMAGE,
        headers=HEADERS,
        json={"inputs": {"image": img_base64}},
    )
    
    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("generated_text", "No caption generated.")
        return "No caption generated."
    else:
        return f"Error: {response.status_code}, {response.text}"


# Convert image to base64
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")