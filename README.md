
# Python Programming

This repository contains 10 Python programs created in my freshman year at the _Universidade Federal de Uberlândia_ (Federal University of Uberlândia).
Each one solves 1 out of 10 problems given to us students.

PS.: The algorithms were mainly written in Portuguese.

- `aritmetica.py`: Basic operations with 2 numbers given by user.
- `conversao-tempo.py`: Breaks down _n_ seconds into days, hours, minutes and seconds.
- `jogo-avatar.py`: _Avatar: The Last Airbender_ game about elemental manipulation training. The user constantly informs an element and attributes a value
to it. The opposing element's value is then lowered by half the given value. The opposing relationships within elements are **FIRE** &harr; **WATER** and **EARTH** &harr; **AIR**. When the player is done playing, final values are displayed.
- `vacinacao.py`: A program about COVID-19 vaccine monthly supply management. The user is prompted about the quantity of vaccines in each monthly supply. Each supply has its vaccines given out to citizens according to a priority. At the end, the code tells about **the amount of people given both doses**, **the amount of people only given the 1st dose**, **the amount of people given an overdue 2nd dose** and **the amount of people awaiting an overdue 2nd dose**. The priority is (_highest_ to _lowest_):
    1. Citizens awaiting an overdue 2nd dose.
    2. Citizens awaiting an on-time 2nd dose.
    3. Citizens not yet vaccinated.
- `porteiro-castelo.py`: A _Rá-Tim-Bum_ (Brazilian TV series) themed program. The user is prompted a password to enter a castle. The password is a sequence of numbers and is then evaluated whether it can be sorted in ascending order by "rotating" it or not. The "rotation" means, e.g., turning **_a b c d e_** into **_b c d e a_**. If the sequence can be sorted this way, the castle gatekeeper opens the castle gates. If not, it is then said to be invalid.
- `problema-mochila.py`: A simplified version of the infamous _Knapsack Problem_. The user is supposed to be soon travelling and must pack a knapsack. They first inform the capacity of the bag and the number of objects they intend to take to the trip. The program then asks for each item's weight and an arbitrary value based on importance. After so, the algorithm fills the knapsack as much as possible with the most valuable items by weight. Finally, it displays the knapsack's net value and weight.
- `sentido-vida.py`: A code about DNA and complementary base pairing. The user is prompted a DNA string and a primer, both written as sequences of nitrogenous bases. The program then displays the locations in the DNA string where the primer can be paired with. If there are no locations, it outputs a _no pairing locations_ message.
- `similaridade-maxima.py`: A game about similarity. The player inputs a table as an _n x n_ matrix and then an _m x m_ matrix (_m_ < _n_). Both matrices are made of numbers. The code then takes the most similar _m x m_ submatrix of the table to the _m x m_ matrix input and outputs its position in the _n x n_ table and similarity percentage.
- `batalha-naval.py`: A battleship-like game. The user first inputs a _10 x 10_ grid of uppercase letters and periods (.). The letters are ships, whereas periods indicate empty water squares. The player is then constantly prompted a hit guess composed of a row (A to J) and a column (1 to 10). At last, the algorithm takes each guess and outputs whether it hits (or sinks) a ship or lands on water.
- `pandemia-fakenews.py`: A program about fake news spread and containment. The user inputs an _n x n_ population grid made of numbers (0 to 9), hashes (#) and periods (.). Such symbols represent dangerous people, safe people and empty squares, respectively. Dangerous people are gullible ones who believe in fake news and share them with others; their numbers indicate the spread range at all four directions. Safe people, on the other hand, are those who identify fake news and block their spread. The player is then prompted a pair of coordinates comprised of a row (0 to _n_ - 1) and a column (0 to _n_ - 1). The fake news begin at the given coordinates and are recursively spread and contained within the population grid. Whenever a dangerous person gets a fake news, they become infected, turn into an X in the grid and share the fake news. At the end, the code displays the population grid after all infections.
