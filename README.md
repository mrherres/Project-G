# Project-G
Group project for Advanced Programming.

--- Instructions for using the program ---
When you start the program, with "python3 gui.py", there will first be a pop
up message giving the rules for the game:
-only words with 4 letters or longer
-only Dutch words
-only use words once

When clicking this message away, the game starts.
In the entry field users can fill in answers and check them by clicking the
"check" button in the gui.
There is also the option to show a hint, this will reveal the pangram word
character by character. This does however deduct a point for each letter given!


--- Who did what ---

On april 5, Cain made the first addition to gui.py by adding the function get_input. This function added a textbox and a button.

On april 6, Twan added the functions create_text_icon and check_score.
The funciton create_text_icon is used to make the puzzle itself show up, using 7 text icons.
The function check_score is where the users anwers are checked.


On april 7, Cain made some small changes to gui.py


From april 8 and onwards, we started doing discord calls, so we could work together on the project.

Cain made a start with load_words.py, a program to open and edit the word list so we could use it, by creating the functions load_words and remove_punc.

Cain and Harmen worked together on the functions seven_char_words, get_uniq and get_random_word, while Twan focused on the honeycomb for the puzzle.


On april 9, Harmen added correct_answer_finder to load_words and minor changes to gui.py\y


On april 10, we worked together via discord once again.

Cain made the functions from load_words.py compatible in gui.py

Harmen added must_use_char_pick to load_words.py and made changes to correct_answer_finder and get_random_word.

Twan and Harmen created the function index_word in gui.py.

Twan made multiple changes to gui.py and load_words.py to integrate new functions.

Harmen made multiple corrections and slightly edited load_words so it could read the dutchwords text file. He also added pangram check and a functional scoring and counting system and a remaining words status along with some minor changes to gui.py.

Twan made changes to the interface.


On april 12 and 13, the program already worked and only visual and minor changes were left to be made.

Twan en Cain got rid of pycodestyle errors.
Cain made the puzzle solver program.

All of us contributed to the readme.

Twan made the hint and intro message


---Commits---

--- Commits on Apr 13, 2020 ---

    Finish README
    @CainWeideman
    CainWeideman commited 2 minutes ago

    README format
    @harmen01
    harmen01 committed 10 minutes ago

    README: who did what
    @harmen01
    harmen01 committed 30 minutes ago
 
    Edited README
    @CainWeideman
    CainWeideman committed 6 hours ago
 
    Pycodestyle fixed and added documentation to load_words
    @CainWeideman
    CainWeideman committed 6 hours ago
 
    puzzle_solver commit #2: optimisation and pycodestyle
    @CainWeideman
    CainWeideman committed 7 hours ago

--- Commits on Apr 12, 2020 ---

    Commit puzzle_solver
    @CainWeideman
    CainWeideman committed yesterday

    Tidied up the program so that pycodestyle gives no errors. Also added…
    @mrherres
    mrherres committed 23 minutes ago

    Made an intro message and a hint function.
    @mrherres
    mrherres committed 2 hours ago

--- Commits on Apr 10, 2020 ---

    Minor changes to the interface.
    @mrherres
    mrherres committed 2 days ago

    Fixed a wrong parameter
    @harmen01
    harmen01 committed 2 days ago

    Added a remaining words counter, does not display correctly at the mo…
    @harmen01
    harmen01 committed 2 days ago

    Added pangram_check and a functional score counting system
    @harmen01
    harmen01 committed 2 days ago

    Minor interface changes
    @mrherres
    mrherres committed 2 days ago

    Fixed the index placement of the random word that is used.
    @mrherres
    mrherres committed 2 days ago

    index_word changes
    @harmen01
    harmen01 committed 2 days ago

    Minor bug fixes
    @mrherres
    mrherres committed 2 days ago

    Big commit: imported load_words into gui and made the functions compatible.
    @CainWeideman
    CainWeideman committed 2 days ago

--- Commits on Apr 9, 2020 ---

    Added correct_answer_finder and minor updates
    @harmen01
    harmen01 committed 3 days ago

--- Commits on Apr 8, 2020 ---

    Minor changes to the honeycomb.
    @mrherres
    mrherres committed 4 days ago

    Created the honeycomb style.
    @mrherres
    mrherres committed 4 days ago

    Added a working score function. Also made a change that the game reco…
    @mrherres
    mrherres committed 4 days ago

--- Commits on Apr 7, 2020 ---

    GUI commit #3: Gui: get_input function was made.
    @CainWeideman
    CainWeideman committed 5 days ago

--- Commits on Apr 5, 2020 ---

    GUI #1: Gui: Entry and Textbox added to window.
    @CainWeideman
    CainWeideman committed 7 days ago

