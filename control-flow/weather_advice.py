def weather_advice(): 
     # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold):")
   
   # Provide clothing recommendations based on user input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")

    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")

    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")

    else:
        print("Sorry, I don't have recommendations for this weather.")
        
#Run the weather_advice function
weather_advice()



