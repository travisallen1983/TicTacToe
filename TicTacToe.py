import time
import random

SPACE = ' '
VERTICAL_LINE = ':'
HORIZONTAL_LINE = '.'
VERTICAL_FORMAT = (SPACE * 3) + VERTICAL_LINE + (SPACE * 3) + VERTICAL_LINE + (SPACE * 3)
HORIZONTAL_FORMAT = HORIZONTAL_LINE * 11

TOP_LEFT = [1, 2]
TOP_CENTER = [5, 6]
TOP_RIGHT = [9, 10]
CENTER_LEFT = [1, 2]
CENTER = [5, 6]
CENTER_RIGHT = [9, 10]
BOTTOM_LEFT = [1, 2]
BOTTOM_CENTER = [5, 6]
BOTTOM_RIGHT = [9, 10]


WAYS_TO_WIN = [
               [[0, 0], [0, 1], [0, 2]]  # Top Row
               , [[1, 0], [1, 1], [1, 2]]  # CENTER Row
               , [[2, 0], [2, 1], [2, 2]]  # Bottom Row
               , [[0, 0], [1, 0], [2, 0]]  # First Column
               , [[0, 1], [1, 1], [2, 1]]  # Second Column
               , [[0, 2], [1, 2], [2, 2]]  # Third Column
               , [[0, 0], [1, 1], [2, 2]]  # Diagonal Left to Right
               , [[0, 2], [1, 1], [2, 0]]  # Diagonal Right to Left
               ]


def print_matrix(vertical_one
                 , horizontal_one
                 , vertical_two
                 , horizontal_two
                 , vertical_three) -> None:
    print(vertical_one)
    print(horizontal_one)
    print(vertical_two)
    print(horizontal_two)
    print(vertical_three)


def print_message(character, number_of_character, message, number_of_spaces) -> None:
    print('\n')
    print(character * number_of_character)
    print((' ' * number_of_spaces) + message + (' ' * number_of_spaces))
    print(character * number_of_character)
    print('\n')


def play_game(grid_vertical, grid_horizontal) -> list:

    vertical_string_one = grid_vertical
    horizontal_string_one = grid_horizontal
    vertical_string_two = grid_vertical
    horizontal_string_two = grid_horizontal
    vertical_string_three = grid_vertical

    total_x_wins = 0
    total_o_wins = 0
    total_draws = 0

    player_mark = ''

    output_list = []
    for total in range(0, 10_000):
        available_selection = [
                               [0, 0], [0, 1], [0, 2]  # Top Row
                               , [1, 0], [1, 1], [1, 2]  # Center Row
                               , [2, 0], [2, 1], [2, 2]  # Bottom Row
                               ]  # Bottom Row
        if total == 0:
            print_message('*', 13
                          , "LET'S PLAY!", 1)

            print_matrix(vertical_string_one
                         , horizontal_string_one
                         , vertical_string_two
                         , horizontal_string_two
                         , vertical_string_three
                         )

            print_message('*', 12
                          , "X's PICK!", 2)
            # time.sleep(1)
        if total > 0:
            print_message('*', 13
                          , "NEXT GAME!", 1)
            print_matrix(vertical_string_one
                         , horizontal_string_one
                         , vertical_string_two
                         , horizontal_string_two
                         , vertical_string_three
                         )
            print_message('*', 12
                          , "X's PICK!", 2)
            # time.sleep(1)
        x_selected_cells = []
        o_selected_cells = []

        selection = []

        x_turn_to_play = True
        o_turn_to_play = False

        x_wins = False
        o_wins = False

        for i in range(0, 9):
            if x_turn_to_play is True:
                x_selection = random.choice(available_selection)
                available_selection.remove(x_selection)
                x_selected_cells.append(x_selection)
                selection = x_selection
                player_mark = 'X'
            elif o_turn_to_play is True:
                o_selection = random.choice(available_selection)
                available_selection.remove(o_selection)
                o_selected_cells.append(o_selection)
                selection = o_selection
                player_mark = 'O'
            if selection == [0, 0]:
                vertical_string_one = (vertical_string_one[:TOP_LEFT[0]]
                                       + player_mark
                                       + vertical_string_one[TOP_LEFT[1]:]
                                       )
            elif selection == [0, 1]:
                vertical_string_one = (vertical_string_one[:TOP_CENTER[0]]
                                       + player_mark
                                       + vertical_string_one[TOP_CENTER[1]:]
                                       )
            elif selection == [0, 2]:
                vertical_string_one = (vertical_string_one[:TOP_RIGHT[0]]
                                       + player_mark
                                       + vertical_string_one[TOP_RIGHT[1]:]
                                       )
            elif selection == [1, 0]:
                vertical_string_two = (vertical_string_two[:CENTER_LEFT[0]]
                                       + player_mark
                                       + vertical_string_two[CENTER_LEFT[1]:]
                                       )
            elif selection == [1, 1]:
                vertical_string_two = (vertical_string_two[:CENTER[0]]
                                       + player_mark
                                       + vertical_string_two[CENTER[1]:]
                                       )
            elif selection == [1, 2]:
                vertical_string_two = (vertical_string_two[:CENTER_RIGHT[0]]
                                       + player_mark
                                       + vertical_string_two[CENTER_RIGHT[1]:]
                                       )
            elif selection == [2, 0]:
                vertical_string_three = (vertical_string_three[:BOTTOM_LEFT[0]]
                                         + player_mark
                                         + vertical_string_three[BOTTOM_LEFT[1]:]
                                         )
            elif selection == [2, 1]:
                vertical_string_three = (vertical_string_three[:BOTTOM_CENTER[0]]
                                         + player_mark
                                         + vertical_string_three[BOTTOM_CENTER[1]:]
                                         )
            elif selection == [2, 2]:
                vertical_string_three = (vertical_string_three[:BOTTOM_RIGHT[0]]
                                         + player_mark
                                         + vertical_string_three[BOTTOM_RIGHT[1]:]
                                         )

            print_matrix(vertical_string_one
                         , horizontal_string_one
                         , vertical_string_two
                         , horizontal_string_two
                         , vertical_string_three
                         )

            match_one_x = False
            match_two_x = False
            match_three_x = False
            if i >= 4:
                for groups in WAYS_TO_WIN:
                    for cell in groups:
                        for player_selection in x_selected_cells:
                            if player_selection == cell and match_one_x is False:
                                match_one_x = True
                            elif player_selection == cell and match_two_x is False:
                                match_two_x = True
                            elif player_selection == cell and match_three_x is False:
                                match_three_x = True
                    if match_one_x is True and match_two_x is True and match_three_x is True:
                        x_wins = True
                        print_message('*', 11
                                      , "X WINS!", 2)
                        break
                    else:
                        match_one_x = False
                        match_two_x = False
                        match_three_x = False

                match_one_o = False
                match_two_o = False
                match_three_o = False
                for groups in WAYS_TO_WIN:
                    for cell in groups:
                        for player_selection in o_selected_cells:
                            if player_selection == cell and match_one_o is False:
                                match_one_o = True
                            elif player_selection == cell and match_two_o is False:
                                match_two_o = True
                            elif player_selection == cell and match_three_o is False:
                                match_three_o = True
                    if match_one_o is True and match_two_o is True and match_three_o is True:
                        o_wins = True
                        print_message('*', 11
                                      , "O WINS!", 2)
                        break
                    else:
                        match_one_o = False
                        match_two_o = False
                        match_three_o = False

            if x_wins is True:
                break
            if o_wins is True:
                break

            if x_turn_to_play is True:
                x_turn_to_play = False
                o_turn_to_play = True
            elif o_turn_to_play is True:
                o_turn_to_play = False
                x_turn_to_play = True

            if i != 8 and x_turn_to_play is True:
                print_message('*', 12
                              , "X's PICK!", 2)
            elif i != 8 and o_turn_to_play is True:
                print_message('*', 12
                              , "O's PICK!", 2)

                # time.sleep(1)

            if i == 8 and x_wins is False and o_wins is False:
                print_message('*', 12
                              , "DRAW!", 3)

        vertical_string_one = VERTICAL_FORMAT
        horizontal_string_one = HORIZONTAL_FORMAT
        vertical_string_two = VERTICAL_FORMAT
        horizontal_string_two = HORIZONTAL_FORMAT
        vertical_string_three = VERTICAL_FORMAT

        if x_wins:
            total_x_wins += 1
        elif o_wins:
            total_o_wins += 1
        else:
            total_draws += 1

    output_list.append(total_x_wins)
    output_list.append(total_o_wins)
    output_list.append(total_draws)

    return output_list


def main():
    run_game = play_game(VERTICAL_FORMAT, HORIZONTAL_FORMAT)
    print('X Wins: ' + str(run_game[0]))
    print('O Wins: ' + str(run_game[1]))
    print('Draws: ' + str(run_game[2]))


if __name__ == '__main__':
    main()
