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
    about_me["movies"].append({"title": "Evil Dead", "genre": "horror"})
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me["full_name"]
    first_name = full_name.split()[0]
    student_id = about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Sir {first_name}.\nMy student ID is {student_id}.")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    new_toppings = {"ONION", "HAM"}
    for topping in toppings:
        about_me["pizza_toppings"].append(toppings)
        about_me["pizza_toppings"].sort()
        about_me["pizza_toppings"].str.lower()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genre= about_me["genre"]
    for genre in ["genre"]:
        print(f'I like to watch {genre[0]}, {genre[1]}, {genre[2]}')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()