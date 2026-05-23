def recommend_crop(temp, rainfall):

    if rainfall > 2000 and temp > 25:
        return "Rice"

    elif rainfall > 1500:
        return "Sugarcane"

    elif temp < 20:
        return "Wheat"

    elif 20 <= temp <= 30:
        return "Maize"

    else:
        return "Barley"