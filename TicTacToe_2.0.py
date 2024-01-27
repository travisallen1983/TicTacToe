import random
import json

# The tic-tac-toe matrix printed to the console
SPACE = ' '
VERTICAL_LINE = ':'
HORIZONTAL_LINE = '.'
VERTICAL_FORMAT = (SPACE * 3) + VERTICAL_LINE + (SPACE * 3) + VERTICAL_LINE + (SPACE * 3)
HORIZONTAL_FORMAT = HORIZONTAL_LINE * 11

# The indexes where a players mark will be inserted into the tic-tac-toe matrix
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
               , [[1, 0], [1, 1], [1, 2]]  # Center Row
               , [[2, 0], [2, 1], [2, 2]]  # Bottom Row
               , [[0, 0], [1, 0], [2, 0]]  # Left Column
               , [[0, 1], [1, 1], [2, 1]]  # Center Column
               , [[0, 2], [1, 2], [2, 2]]  # Right Column
               , [[0, 0], [1, 1], [2, 2]]  # Diagonal Left to Right
               , [[0, 2], [1, 1], [2, 0]]  # Diagonal Right to Left
               ]


def read_previous_game_data(folder_location, file_name) -> dict:
    file = folder_location + file_name
    try:
        with open(file, 'r') as open_json:
            dictionary = json.load(open_json)
    except FileNotFoundError:
        with open(file, 'w') as output_file:
            dictionary = {'WINS': [], 'LOSSES': []}
            create_json = json.dumps(dictionary, indent=4)
            output_file.write(create_json)
    return dictionary


def write_updated_game_data(folder_location, file_name, results) -> None:
    file = folder_location + file_name

    create_json = json.dumps(results, indent=4)

    with open(file, 'w') as output_file:
        output_file.write(create_json)


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


def play_defense(player, vertical_string_one, vertical_string_two, vertical_string_three) -> list:
    defend_position = []

    row_one = [vertical_string_one[1], vertical_string_one[5], vertical_string_one[9]]
    row_two = [vertical_string_two[1], vertical_string_two[5], vertical_string_two[9]]
    row_three = [vertical_string_three[1], vertical_string_three[5], vertical_string_three[9]]
    column_one = [vertical_string_one[1], vertical_string_two[1], vertical_string_three[1]]
    column_two = [vertical_string_one[5], vertical_string_two[5], vertical_string_three[5]]
    column_three = [vertical_string_one[9], vertical_string_two[9], vertical_string_three[9]]
    vertical_one = [vertical_string_one[1], vertical_string_two[5],vertical_string_three[9]]
    vertical_two = [vertical_string_one[9], vertical_string_two[5], vertical_string_three[1]]

    if row_one.count(player) == 2 and row_one.count(' ') == 1:
        defend_position.append([0, row_one.index(' ')])
    elif row_two.count(player) == 2 and row_two.count(' ') == 1:
        defend_position.append([1, row_two.index(' ')])
    elif row_three.count(player) == 2 and row_three.count(' ') == 1:
        defend_position.append([2, row_three.index(' ')])
    elif column_one.count(player) == 2 and column_one.count(' ') == 1:
        defend_position.append([column_one.index(' '), 0])
    elif column_two.count(player) == 2 and column_two.count(' ') == 1:
        defend_position.append([column_two.index(' '), 1])
    elif column_three.count(player) == 2 and column_three.count(' ') == 1:
        defend_position.append([column_three.index(' '), 2])
    elif vertical_one.count(player) == 2 and vertical_one.count(' ') == 1:
        defend_position.append([vertical_one.index(' '), vertical_one.index(' ')])
    elif vertical_two.count(player) == 2 and vertical_two.count(' ') == 1:
        column_index = 2 - vertical_two.index(' ')
        defend_position.append([vertical_two.index(' '), column_index])
    return defend_position


def play_game(grid_vertical, grid_horizontal, previous_wins_and_losses, number_of_games) -> dict:

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
    ranked_winning_choices = []
    ranked_losing_choices = []
    game_data = previous_wins_and_losses

    for total in range(0, number_of_games):
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
        if total > 0:
            print_message('*', 13
                          , 'NEXT GAME!', 1)
            print_matrix(vertical_string_one
                         , horizontal_string_one
                         , vertical_string_two
                         , horizontal_string_two
                         , vertical_string_three
                         )
            print_message('*', 12
                          , "X's PICK!", 2)
        x_selected_cells = []
        o_selected_cells = []

        selection = []

        x_turn_to_play = True
        o_turn_to_play = False

        x_wins = False
        o_wins = False

        get_wins_data = game_data.get('WINS')

        for i in range(0, 9):
            if x_turn_to_play is True:
                x_selection = []
                best_choice = 0
                if get_wins_data != []:
                    for x in range(len(get_wins_data[0])):
                        if get_wins_data[0][x][0] > best_choice and get_wins_data[0][x][1] in available_selection:
                            x_selection = get_wins_data[0][x][1]
                            best_choice = get_wins_data[0][x][0]
                elif x_selection == []:
                    x_selection = random.choice(available_selection)
                if i > 1:
                    defense = play_defense('O', vertical_string_one, vertical_string_two, vertical_string_three)
                    if defense != [] and defense[0] in available_selection:
                        x_selection = defense[0]
                available_selection.remove(x_selection)
                x_selected_cells.append(x_selection)
                selection = x_selection
                player_mark = 'X'
            elif o_turn_to_play is True:
                o_selection = []
                best_choice = 0
                if get_wins_data != []:
                    for o in range(len(get_wins_data[0])):
                        if get_wins_data[0][o][0] > best_choice and get_wins_data[0][o][1] in available_selection:
                            o_selection = get_wins_data[0][o][1]
                            best_choice = get_wins_data[0][o][0]
                elif o_selection == []:
                    o_selection = random.choice(available_selection)
                if i > 1:
                    defense = play_defense('X', vertical_string_one,vertical_string_two,vertical_string_three)
                    if defense != [] and defense[0] in available_selection:
                        o_selection = defense[0]
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
                              , 'DRAW!', 3)

        vertical_string_one = VERTICAL_FORMAT
        horizontal_string_one = HORIZONTAL_FORMAT
        vertical_string_two = VERTICAL_FORMAT
        horizontal_string_two = HORIZONTAL_FORMAT
        vertical_string_three = VERTICAL_FORMAT

        if x_wins:
            total_x_wins += 1
            ranked_winning_choices.append(x_selected_cells)
            ranked_losing_choices.append(o_selected_cells)
        elif o_wins:
            total_o_wins += 1
            ranked_winning_choices.append(o_selected_cells)
            ranked_losing_choices.append(x_selected_cells)
        else:
            total_draws += 1

    output_list.append(total_x_wins)
    output_list.append(total_o_wins)
    output_list.append(total_draws)

    print('X Wins: ' + str(output_list[0]))
    print('O Wins: ' + str(output_list[1]))
    print('Draws: ' + str(output_list[2]))

    if game_data.get('WINS') == []:
        previous_win_rank = []
        previous_win_value = []
    else:
        previous_win_rank = [x for x, y in game_data.get('WINS')[0]]
        previous_win_value = [y for x, y in game_data.get('WINS')[0]]
    win_rank = previous_win_rank
    win_value = previous_win_value
    for choice in ranked_winning_choices:
        for i in range(len(choice)):
            if choice[i] not in win_value:
                win_value.append(choice[i])
                win_rank.append(1)
            if choice[i] in win_value:
                for j in range(len(win_value)):
                    if choice[i] == win_value[j]:
                        win_rank[j] = win_rank[j] + 1
    win_value_plus_rank = []
    win_value_rank = []
    for i in range(len(win_rank)):
        win_value_plus_rank.append(win_rank[i])
        win_value_plus_rank.append(win_value[i])
        win_value_rank.append(win_value_plus_rank)
        win_value_plus_rank = []

    if game_data.get('LOSSES') == []:
        previous_loss_rank = []
        previous_loss_value = []
    else:
        previous_loss_rank = [x for x, y in game_data.get('LOSSES')[0]]
        previous_loss_value = [y for x, y in game_data.get('LOSSES')[0]]
    loss_rank = previous_loss_rank
    loss_value = previous_loss_value
    for choice in ranked_losing_choices:
        for i in range(len(choice)):
            if choice[i] not in loss_value:
                loss_value.append(choice[i])
                loss_rank.append(1)
            if choice[i] in loss_value:
                for j in range(len(loss_value)):
                    if choice[i] == loss_value[j]:
                        loss_rank[j] = loss_rank[j] + 1

    loss_value_plus_rank = []
    loss_value_rank = []
    for i in range(len(loss_rank)):
        loss_value_plus_rank.append(loss_rank[i])
        loss_value_plus_rank.append(loss_value[i])
        loss_value_rank.append(loss_value_plus_rank)
        loss_value_plus_rank = []

    new_wins_data = [win_value_rank]
    new_losses_data = [loss_value_rank]
    game_data.update({'WINS': new_wins_data})
    game_data.update({'LOSSES': new_losses_data})

    return game_data


def main():
    project_location = r'..\TicTacToe'
    name_of_file = r'\previous_game_data_2.0.json'
    total_games = 100_000

    previous_game_data = read_previous_game_data(project_location, name_of_file)

    run_game = play_game(VERTICAL_FORMAT, HORIZONTAL_FORMAT, previous_game_data, total_games)

    write_updated_game_data(project_location, name_of_file, run_game)


if __name__ == '__main__':
    main()
