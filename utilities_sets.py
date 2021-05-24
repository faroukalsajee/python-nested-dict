def get_total_items(s):
    return len(s)


def display_all_items(set1):
    for items in set1:
        print(items)


def add_item(item, the_set):
    the_set.add(item)


def remove_item(item, the_set):
    the_set.remove(item)


def get_the_union_of(set1, set2):
    new_set = set1.union(set2)
    return new_set
