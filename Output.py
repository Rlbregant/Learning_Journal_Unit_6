Part 1:

List using split():  ['Commander', 'Keen', 'in', 'Invasion', 'of', 'the', 'Vorticons', 'Commander', 'Keen', 'in', 'Goodbye,', 'Galaxy!', 'Commander', 'Keen', 'in', 'Aliens', 'Ate', 'My', 'Babysitter!']

List after deleting three words:  ['in', 'Invasion', 'the', 'Vorticons', 'Commander', 'Keen', 'in', 'Goodbye,', 'Galaxy!', 'Commander', 'Keen', 'in', 'Aliens', 'Ate', 'My', 'Babysitter!']

List after sorting:  ['Aliens', 'Ate', 'Babysitter!', 'Commander', 'Commander', 'Galaxy!', 'Goodbye,', 'Invasion', 'Keen', 'Keen', 'My', 'Vorticons', 'in', 'in', 'in', 'the']

List after adding new words:  ['Aliens', 'Ate', 'Commander Keen in The Armageddon Machine', 'Babysitter!', 'Commander', 'Commander', 'Galaxy!', 'Goodbye,', 'Invasion', 'Keen', 'Keen', 'My', 'Vorticons', 'in', 'in', 'in', 'the', 'Commander Keen in The Earth Explodes', 'Commander Keen in Keen Dreams', 'Commander Keen in Goodbye, Universe!']

String using join():  Aliens Ate Commander Keen in The Armageddon Machine Babysitter! Commander Commander Galaxy! Goodbye, Invasion Keen Keen My Vorticons in in in the Commander Keen in The Earth Explodes Commander Keen in Keen Dreams Commander Keen in Goodbye, Universe!

New string of game titles:  Aliens Ate Commander Keen in The Armageddon Machine Babysitter! Commander Commander Galaxy! Goodbye, Invasion Keen Keen My Vorticons in in in the Commander Keen in The Earth Explodes Commander Keen in Keen Dreams Commander Keen in Goodbye, Universe!

Print the first level of the first set of levels in the nested list:
Mars

Use the * operator to create a new list of game titles repeated five times:
['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!']

Use list slices to extract a sublist of game titles:
['Commander Keen in The Armageddon Machine', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Keen Dreams']

Use the += operator to add a list of games to the end of another list of games:
['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Keen Dreams']

Example 6:
Original list:  ['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Keen Dreams', 'Commander Keen in The Armageddon Machine']
Filtered list of '!':  ['Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!']

Example 7:
Original list:  ['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Keen Dreams', 'Commander Keen in The Armageddon Machine']
New list:  ['Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!', 'Commander Keen in Keen Dreams', 'Commander Keen in The Armageddon Machine', 'Commander Keen in Invasion of the Vorticons', 'Commander Keen in Goodbye, Galaxy!', 'Commander Keen in Aliens Ate My Babysitter!']
Oops, we seem to have concatiated the list to the first three elements of itself by a silly mistake. Thinking about it, we can see that this is because we assigned the first three elements of the list to a new variable, and then concatenated the new variable to the original list. This means that the new variable is still pointing to the first three elements of the list, and so when we concatenate the list to itself, we are actually concatenating the first three elements of the list to itself. To fix this, we can simply assign the first three elements of the list to a new variable, and then concatenate the new variable to the original list.

Process finished with exit code 0