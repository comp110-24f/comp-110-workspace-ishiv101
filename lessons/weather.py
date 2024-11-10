def get_weather_report() -> str:
    """tells us what to do based on the weather"""
    weather: str = input("What is the weather")
    if weather == "rainy" or weather == "cold":
        print("bring a jacket")
    elif weather == "hot":
        print("keep cool out there")
    else:
        print("I do not recognize this weather")
    return weather


get_weather_report()
