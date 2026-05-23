def recommend_fertilizer(crop, soil_condition="normal"):

    if crop == "Rice":
        return "Nitrogen-rich fertilizer (Urea)"

    elif crop == "Wheat":
        return "Balanced NPK fertilizer"

    elif crop == "Maize":
        return "High phosphorus fertilizer"

    else:
        return "Organic compost recommended"