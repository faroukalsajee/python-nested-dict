from utilities_sets import get_total_items, display_all_items, add_item, remove_item, get_the_union_of


# sets below
def main():
    set1 = {'apple', 'banana', 'orange', 'peach'}
    set2 = {'banana', 'pineapple', 'peach', 'watermelon'}

    print('the total number of set1 is ', get_total_items(set1))

    add_item('cantaloupe', set1)
    print('Added ‘cantaloupe’ to the set1 and the resulting set1 is')
    display_all_items(set1)
    remove_item('watermelon', set2)
    print('removed \'watermelon\' from the set2 and the resulting set2 is')
    display_all_items(set2)
    print('this is the union of set1 & set2', get_the_union_of(set1, set2))


if __name__ == "__main__":
    main()
