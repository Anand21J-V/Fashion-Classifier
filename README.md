# AI Fashion Insights Generator

## Overview
The **AI Fashion Insights Generator** is a Streamlit-based web application that leverages Hugging Face models to analyze fashion items from images. The application performs the following tasks:
- Generates a descriptive caption for an uploaded image using **Salesforce's BLIP Image Captioning model**.
- Extracts fashion-related insights from the caption using **Mistral AI's Mixtral-8x7B-Instruct model**.
- Displays structured JSON output with category, material, colors, season suitability, and more.

## Features
- **Image Upload**: Users can upload an image in JPG, PNG, or JPEG format.
- **AI-powered Captioning**: Automatically generates captions for images.
- **Fashion Analysis**: Provides insights on clothing category, material, color, season suitability, gender targeting, occasion, brand trend, and estimated pricing.
- **JSON Output**: Returns structured data for further use in fashion-related applications.

## Technologies Used
- **Streamlit**: For the web-based user interface.
- **Hugging Face Transformers API**: For image captioning and fashion insights.
- **PIL (Pillow)**: For image processing.
- **Requests**: To interact with Hugging Face APIs.
- **Python Dotenv**: To manage API keys securely.

## Installation
### Prerequisites
Ensure you have Python installed (version 3.7+ recommended).

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/ai-fashion-insights.git
   cd ai-fashion-insights
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your **Hugging Face API token**:
   ```
   HF_TOKEN=your_huggingface_api_token
   ```
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Upload an image using the Streamlit interface.
2. The app will generate a caption for the image.
3. The caption is then analyzed to extract detailed fashion insights.
4. The results will be displayed in JSON format on the UI.

## Example JSON Output
```json
{
  "caption": "A stylish red leather jacket with a zipper.",
  "fashion_insights": {
    "CATEGORY & TYPE": "Jacket - Leather",
    "MATERIAL & FABRIC": "Leather",
    "COLOR & AESTHETICS": "Red, Solid",
    "SEASON SUITABILITY": "Winter, Fall",
    "GENDER & TARGET AUDIENCE": "Unisex",
    "OCCASION & STYLING TIPS": "Casual, Biker Look",
    "BRAND & TREND ANALYSIS": "Classic style, Timeless fashion",
    "PRICING & MARKET INSIGHTS": "$100 - $300"
  }
}
```

## Troubleshooting
- Ensure your Hugging Face API token is valid and correctly set in the `.env` file.
- If the JSON output is incorrect or missing, verify the API responses in the logs.
- If `load_dotenv()` is not working, install `python-dotenv`:
  ```bash
  pip install python-dotenv
  ```

## License
This project is open-source and available under the **MIT License**.

## Author
**Anand Vishwakarma**

