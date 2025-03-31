import streamlit as st
from PIL import Image
import requests
import io
import base64
import json
import os
from dotenv import load_dotenv

load_dotevn()

# Hugging Face API Configuration
HF_API_URL_IMAGE = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
HF_API_URL_TEXT = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
os.environ["HF_TOKEN"] = HF_TOKEN  

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}"}

# Convert image to base64
def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

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

# Generate fashion insights using Mistral
def generate_fashion_insights(caption):
    prompt = f"""
    Given the image caption: "{caption}", analyze the clothing item and provide fashion insights.

    Fashion Analysis:
    - CATEGORY & TYPE:  Identify the category (Topwear, Bottomwear, Footwear, Accessories) and specific type (T-shirt, Jeans, Sneakers, etc.).
    - MATERIAL & FABRIC:  Predict the fabric (Cotton, Denim, Wool, Silk) based on its texture and pattern.
    - COLOR & AESTHETICS: Describe primary/secondary colors, patterns (Stripes, Floral, Solid), and their significance in fashion.
    - SEASON SUITABILITY: Is it suitable for Summer, Winter, Spring, or Fall?
    - GENDER & TARGET AUDIENCE: Is it designed for Men, Women, Unisex, or Kids?
    - OCCASION & STYLING TIPS: Suggest best occasions (Casual, Formal, Party, Sportswear) and styling ideas.
    - BRAND & TREND ANALYSIS: Predict if this follows a trend or classic style.
    - PRICING & MARKET INSIGHTS: Estimate price range and discuss affordability.

    Provide a structured JSON output.
    """

    response = requests.post(
        HF_API_URL_TEXT,
        headers=HEADERS,
        json={"inputs": prompt},
    )

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and len(result) > 0:
            insights_text = result[0].get("generated_text", "No insights generated.")
            
            try:
                insights_json = json.loads(insights_text)
                return insights_json
            except json.JSONDecodeError:
                return {"error": "Failed to parse insights as JSON", "raw_response": insights_text}
        return {"error": "No insights generated."}
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}

# Streamlit UI
st.title("AI Fashion Insights Generator 👗👕")

st.write("Upload an image to receive AI-powered fashion insights in JSON format.")

# Upload image
image_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Generate Caption
    caption = generate_caption(image)
    
    # Generate Fashion Insights
    fashion_insights = generate_fashion_insights(caption)
    
    # Display JSON output
    st.json({"caption": caption, "fashion_insights": fashion_insights})
