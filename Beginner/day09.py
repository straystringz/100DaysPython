# pro_dict = {
#     "bug": "An error in a program that causes malfunction",
#     "Function": "A piece of code that can be easily called over and over again",  # noqa
# }


# print(pro_dict)


# pro_dict["Loop"] = "The action of doing something over and over again"
# print(pro_dict)


# for key in pro_dict:
#     print(f"{key.upper()}\n{pro_dict[key]}")


# print(pro_dict)


# students_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
#     "Choco": 2,
# }

# students_grades = {}

# for key in students_scores:
#     if students_scores[key] <= 70:
#         students_grades[key] = "Fail"
#     elif students_scores[key] > 70 and students_scores[key] <= 80:
#         students_grades[key] = "Acceptable"
#     elif students_scores[key] > 80 and students_scores[key] <= 90:
#         students_grades[key] = "Exceeds Expectations"
#     else:
#         students_grades[key] = "Outstanding"
# print(students_grades)


# travel_log_1 = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }


# travel_log_2 = {
#     "City Visited": {"Paris": 3, "Lille": 4, "Dijon": 2},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }


# travel_log_3 = {
#     "France": {"cities Visited": ["Paris" "Lille", "Dijon"], "total_visits": 12},  # noqa
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# }


# travel_log_4 = [
#     {
#         "country": "France",
#         "cities Visited": ["Paris", "Lille", {"Dijon": "just once"}],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# ]
# print(travel_log_4[0]["cities Visited"][2]["Dijon"])


# travel_log_5 = [
#     {
#         "country": "France",
#         "cities Visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5,
#     },
# ]


# def add_new_country(country, no_of_visits, cities_visited):
#     print(f"You've visited {country} {no_of_visits} times")
#     print(f"You've been to {cities_visited}")

#     travel_log_5.append(
#         {
#             "country": country,
#             "total_visits": cities_visited,
#             "cities_visited": cities_visited,
#         }
#     )


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log_5)


from gavel_art import logo

print(logo)


def silent_auction(bids):
    win_name = ""
    for names in bids:
        if bids[names] == max(bids.values()):
            win_name = names
    return f"the winner is {win_name} with the auction of ${bids[win_name]}"


next_user = True
bids = {}

while next_user:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    any_other_user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()  # noqa
    if any_other_user != "yes":
        break

print(silent_auction(bids))
