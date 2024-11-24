def quiz():
    capitals = {
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Finland": "Helsinki",
        "Austria": "Vienna"
    }

    for country, capital in capitals.items():
        answer = input(f"What is the capital of {country}? ")
        
        if answer.lower() == capital.lower():
            print("Right!")
        else:
            print(f"Wrong! The correct answer is {capital}.")
quiz()