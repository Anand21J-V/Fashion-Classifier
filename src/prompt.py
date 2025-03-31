# PROMPT USED


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
