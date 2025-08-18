# main.py

from recommender.engine import recommend_outfit

def main():
    print("👕 Welcome to the Outfit Recommender 👗")
    print("Please answer a few questions:\n")

    weather = input("Enter weather (hot / mild / cold): ").strip().lower()
    occasion = input("Enter occasion (casual / formal / party): ").strip().lower()
    gender = input("Enter gender (male / female): ").strip().lower()

    outfit = recommend_outfit(weather, occasion, gender)
    print("\n" + outfit)

if __name__ == "__main__":
    main()
    #hi
