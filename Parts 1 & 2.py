def example_1():
    # Create a string of Commander Keen game titles
    games_str = 'Commander Keen in Invasion of the Vorticons Commander Keen in Goodbye, Galaxy! Commander Keen in ' \
                'Aliens Ate My Babysitter! '

    # Convert the string to a list of game titles
    games_list = games_str.split()
    print('Part 1:', '\n')
    print("List using split(): ", games_list, '\n')

    # Delete three words from the list using different operations
    del games_list[1]
    games_list.pop(3)
    games_list.remove('Commander')
    print("List after deleting three words: ", games_list, '\n')

    # Sort the list
    games_list.sort()
    print("List after sorting: ", games_list, '\n')

    # Add new words to the list using different operations
    games_list.append('Commander Keen in The Earth Explodes')
    games_list.insert(2, 'Commander Keen in The Armageddon Machine')
    games_list.extend(['Commander Keen in Keen Dreams', 'Commander Keen in Goodbye, Universe!'])
    print("List after adding new words: ", games_list, '\n')

    # Convert the list back to a string
    games_str_new = ' '.join(games_list)
    print("String using join(): ", games_str_new, '\n')

    # Print the new string of game titles
    print("New string of game titles: ", games_str_new, '\n')


def example_2():
    # Create a nested list of levels in Commander Keen in Invasion of the Vorticons
    level_list = [['Mars', 'Vorticon Mothership'], ['Vorticon Mothership', 'Vorticon Elite Guard Base'],
                  ['Vorticon Elite Guard Base', 'Shadowlands'], ['Shadowlands', 'The Defense Tunnel']]

    # Print the first level of the first set of levels in the nested list
    print('Print the first level of the first set of levels in the nested list:\n', level_list[0][0], '\n')


def example_3():
    # Use the * operator to create a new list of game titles repeated five times
    games_list = ['Commander Keen in Invasion of the Vorticons',
                  'Commander Keen in Goodbye, Galaxy!',
                  'Commander Keen in Aliens Ate My Babysitter!']
    games_list_repeated = games_list * 5
    print('Use the * operator to create a new list of game titles repeated five times:\n', games_list_repeated, '\n')


def example_4():
    # Use list slices to extract a sublist of game titles
    games_list = ['Commander Keen in Invasion of the Vorticons',
                  'Commander Keen in The Armageddon Machine',
                  'Commander Keen in Goodbye, Galaxy!',
                  'Commander Keen in Keen Dreams',
                  'Commander Keen in Goodbye, Universe!',
                  'Commander Keen in The Earth Explodes']
    games_list_sub = games_list[1:4]
    print('Use list slices to extract a sublist of game titles:\n', games_list_sub, '\n')


def example_5():
    # Use the += operator to add a list of games to the end of another list of games
    games1 = ['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!']
    games2 = ['Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Keen Dreams']
    games1 += games2
    print('Use the += operator to add a list of games to the end of another list of games:\n', games1, '\n')


def example_6():
    # Define a list of Commander Keen games
    keen_games = ['Commander Keen in Invasion of the Vorticons',
                  'Commander Keen in Goodbye, Galaxy!',
                  'Commander Keen in Aliens Ate My Babysitter!',
                  'Commander Keen in Keen Dreams',
                  'Commander Keen in The Armageddon Machine']

    # Define a new list that will contain the filtered elements
    filtered_keen_games = []

    # Iterate over the keen_games list, and append each element that contains "!" to the filtered list
    for game in keen_games:
        if "!" in game:
            filtered_keen_games.append(game)

    # Print the original and filtered lists
    print('Example 6:')
    print("Original list: ", keen_games)
    print("Filtered list of '!': ", filtered_keen_games, '\n')


def example_7():
    # Define a list of Commander Keen games
    keen_games = ['Commander Keen in Invasion of the Vorticons',
                  'Commander Keen in Goodbye, Galaxy!',
                  'Commander Keen in Aliens Ate My Babysitter!',
                  'Commander Keen in Keen Dreams',
                  'Commander Keen in The Armageddon Machine']

    # Assign the first three elements of the list to a new variable
    first_three = keen_games[:3]

    # Concatenate the first three elements of the list to itself
    first_three = keen_games + first_three

    # Print both the original list and the new list
    print('Example 7:')
    print("Original list: ", keen_games)
    print("New list: ", first_three)
    print("Oops, we seem to have concatenated the list to the first three elements of itself by a silly mistake. "
          "Thinking about it, we can see that this is because we assigned the first three elements of the list to a "
          "new variable, and then concatenated the new variable to the original list. This means that the new "
          "variable is still pointing to the first three elements of the list, and so when we concatenate the list to "
          "itself, we are actually concatenating the first "
          "three elements of the list to itself. To fix this, we can simply assign the first three elements of the "
          "list to a new variable, and then concatenate the new variable to the original list.")


def main():
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()


if __name__ == '__main__':
    main()
