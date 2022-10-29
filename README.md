
# Python Codes (EN)

This repository contains 10 Python programs made in my freshman year at the _Universidade Federal de Uberlândia_ (Federal University of Uberlândia).
Each code solves 1 out of 10 problems given to us students.

PS.: The code was mainly written in Portuguese.

- `aritmetica.py`: Basic operations with 2 numbers given by user.
- `conversao-tempo.py`: Breaks down _n_ seconds into days, hours, minutes and seconds.
- `jogo-avatar.py`: _Avatar: The Last Airbender_ game about elemental manipulation training. The user constantly informs an element and attributes a value
to it. The opposing element's value is then lowered by half the given value. The opposing relationships within elements are **FIRE** &harr; **WATER** and **EARTH** &harr; **AIR**. When done playing, final values are displayed.
- `vacinacao.py`: A program about COVID-19 vaccine monthly supply management. The user is prompted about the quantity of vaccines in each monthly supply. Each supply has its vaccines given out to citizens according to a priority. At the end of the program, the user is informed about **the amount of people given both doses**, **the amount of people only given the 1st dose**, **the amount of people given an overdue 2nd dose** and **the amount of people awaiting an overdue 2nd dose**. The priority is (_highest_ to _lowest_):
    1. Citizens awaiting an overdue 2nd dose.
    2. Citizens awaiting an on-time 2nd dose.
    3. Citizens not yet vaccinated.
- `porteiro-castelo.py`: A _Rá-Tim-Bum_ (Brazilian TV series) themed program. The user is prompted a password to enter a castle. The password is comprised of numbers and is then evaluated whether it can be sorted in ascending order by "rotating" it or not. The "rotation" means, e.g., turning _a b c d e_ into _b c d e a_. If the sequence can be sorted this way, the castle gatekeeper opens the castle gates. If not, it is then said to be invalid.

AJUSTAR DAQUI PRA BAIXO

- `problema-mochila.py`: A simplified version of the infamous _Knapsack Problem_. The user is supposed to be soon going on a trip and is packing a knapsack. They first informs the capacity of the knapsack and the number of objets they intend to take to the trip.
- `sentido-vida.py`: A code about DNA and complementary base pairing. The user is prompted a DNA string and a primer, both written as nitrogenous bases. The code then displays the locations in the DNA string where the primer can be paired with. If there are no locations, the program outputs a _no pairing locations_ message.
- `similaridade-maxima.py`: A game about similarity. The player inputs an _n_ number and a table as an _n x n_ matrix. The upper left corner is the (0, 0) position. The x value increases leftward and the y value increases downward. After that, they input another _m_ number (_m_ < _n_) and a _m x m_ matrix. Both matrices are written as rows of 0s and 1s. 0s mean white squares, whereas 1s represent black squares. The code then takes the most similar _m x m_ submatrix of the table to the _m x m_ matrix input and outputs its position and similarity percentage.
- `batalha-naval.py`: A battleship-like game. The user first inputs a table as a _10 x 10_ matrix made of uppercase letters and periods (.). The letters represent ships, whereas periods represent empty water spots. The player then inputs an _n_ number and is prompted a hit guess _n_ times. Each guess is comprised of a row (A to J) followed by blank spaces and by a column (1 to 10). At last, the algorithm takes each guess and outputs whether it hits (or sinks) a ship or lands on water.
- `pandemia-fakenews.py`: A program about fake news spread and containment. The user inputs a population grid as an _n x n_ matrix made of numbers (0 to 9), hashes (#) and periods (.), which represent dangerous people, safe people and empty squares, respectively. Dangerous people are gullible ones who believe in fake news and share them with others; their numbers indicate the spread range at all four directions. Safe people, on the other hand, are those who identify fake news and block their spread. The second user input is a pair of coordinates made of a row (0 to _n_ - 1), blank spaces and a column (0 to _n_ - 1). The fake news start spreading at the given coordinates and are recursively spread and contained within the population grid. Every dangerous person infected by fake news are turned into Xs in the grid. The program then displays the altered population grid.
