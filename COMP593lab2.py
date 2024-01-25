def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Liam McCurdy",
        "student_id": 10308949,
        "pizza_toppings": ["PEPPERONI", "BACON", "CHEESE"],
        "movies": [
            {
                "title": "the thing",
                "genre": "sci-fi"
            },
            {
                "title": "halloween",
                "genre": "horror"
            }
        ]
    }
    
    # TODO: Step 3 - Add another movie to the data structure
    about_me["movies"].append({"title": "Barbie", "genre": "comedy"})

    # Call the print_student_name_and_id function
    print_student_name_and_id(about_me)

    # TODO: Step 5 - Function that adds pizza toppings to data structure
    toppings_to_add = ["ONION", "HAM"]
    add_pizza_toppings(about_me, toppings_to_add)

    # Call the print_pizza_toppings function
    print_pizza_toppings(about_me)

    # Call the print_movie_genres function
    print_movie_genres(about_me)

    # Call the print_movie_titles function
    print_movie_titles(about_me["movies"])

# TODO: Step 4 - Function that prints student name and ID
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for topping in toppings:
        about_me["pizza_toppings"].append(topping)
        about_me["pizza_toppings"].sort()
        about_me["pizza_toppings"] = [t.lower() for t in about_me["pizza_toppings"]]
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print("\nMy favourite pizza toppings are:")
    for topping in about_me["pizza_toppings"]:
        print(f"- {topping}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genres = [movie["genre"] for movie in about_me["movies"]]
    print(f"\nI like to watch {', '.join(genres)} movies.")
    return

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    titles = [movie["title"].capitalize() for movie in movie_list]
    print(f"\nSome of my favourite movies are {', '.join(titles)}")
    return
    
if __name__ == '__main__':
    main()
