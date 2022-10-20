def get_name (person):
    return person["name"]

def get_favourite_tv_show (person):
    return person["favourites"]["tv_show"]

def likes_to_eat (person, food):
    snacks = person["favourites"]["snacks"]
    for snack in snacks:
        if snack == food:
            return True
    return False

def add_friend (person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends"].remove(old_friend)

def total_money(people):
    total_monies = 0
    for person in people:
        total_monies += person["monies"]
    return total_monies

def lend_money(lender, lendee, amount):
    lender["monies"] -= amount
    lendee["monies"] += amount

def all_favourite_foods(people):
    all_foods = []
    for person in people:
        all_foods += person["favourites"]["snacks"]
    return all_foods

def find_no_friends(people):
    no_friends = []
    for person in people:
        if len(person["friends"]) == 0:
            no_friends.append(person)
    return no_friends

def unique_favourite_tv_shows(people):
    unique_tv_shows = []
    for person in people:
        tv_show = person["favourites"]["tv_show"]
        if tv_show in unique_tv_shows:
            pass
        else:
            unique_tv_shows.append(tv_show)
    return unique_tv_shows