def get_name (person):
    return person["name"]

def get_favourite_tv_show (person):
    return person["favourites"]["tv_show"]

def likes_to_eat (person, food):
    snacks = person["favourites"]["snacks"]
    return food in snacks
    # for snack in snacks:
    #     if snack == food:
    #         return True
    # return False

def add_friend (person, new_friend):
    person["friends"].append(new_friend)

def remove_friend(person, old_friend):
    person["friends"].remove(old_friend)

def total_money(people):
    total_monies = 0
    for person in people:
        total_monies += person["monies"]
    return total_monies

def check_person_has_money(person, amount):
    if person["monies"] < amount:
        raise ValueError("lender ran out of monies")

def lend_money(lender, lendee, amount):
    check_person_has_money(lender, amount)
    lender["monies"] -= amount
    lendee["monies"] += amount

def concatLists(lists):
    result = []
    for list in lists:
        result += list
    return result

# this doesn't take account of iterators!
# leave off the [] to use iterators instead!
def all_favourite_foods(people):
    return concatLists(person["favourites"]["snacks"] for person in people)

def find_no_friends(people):
    # no_friends = []
    # for person in people:
    #     if len(person["friends"]) == 0:
    #         no_friends.append(person)
    # return no_friends
    return [person for person in people if len(person["friends"]) == 0]

def unique_favourite_tv_shows(people):
    # unique_tv_shows = []
    # for person in people:
    #     tv_show = person["favourites"]["tv_show"]
    #     if tv_show not in unique_tv_shows:
    #         unique_tv_shows.append(tv_show)
    # return unique_tv_shows
    # NB this is a generator comprehension, not a list comprehension
    return set(person["favourites"]["tv_show"] for person in people)