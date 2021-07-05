# Finite Automata word acceptance
Both versions DFA and NFA are the same, since this program doesn't verify if the automata gotten as input is an DFA or not. Based on DFS we find the right 'road' if there is one. In the file "succesiune" the states traveled are written in the order start to finish state. For the lambda/epsilon NFA there's no succesiune file, but it can easily be modified to display the states traveled.

## Input form
1. Number of states of automata
2. The labels for the states (anything separated by space)
3. Number of transitions
4. For the following ... lines the transitions of the automata are put like this: `start-state`  `end-state`  `letter`. For the lambda/epsilon NFA the letter is 'lambda', but can easily be changed in code to something simpler. 
5. The label of the start state
6. Number of final states
7. The labels for the final states (separated by space)
8. Number of words to verify
9. For the following ... lines the words

## Output form
For the number of words, in 'date.out' put there's DA - yes the word was accepted by the automata or NU - wasn't accepted.
In 'succesiune.out' each word that was accepted is displayed and underneath is the states traveled. For the NFA if there are multiple modalities to accept the word all of them are displayed. 
