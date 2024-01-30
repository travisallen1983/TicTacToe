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


def make_selection(opponent, previous_win_data, available_moves, current_iteration
                   , string_one, string_two, string_three) -> list:
    selection = []
    best_choice = 0
    if previous_win_data != []:
        for i in range(len(previous_win_data[0])):
            if previous_win_data[0][i][0] > best_choice and previous_win_data[0][i][1] in available_moves:
                selection = previous_win_data[0][i][1]
                best_choice = previous_win_data[0][i][0]
    if current_iteration > 1:
        defense = play_defense(opponent, string_one, string_two, string_three)
        if defense != [] and defense[0] in available_moves:
            selection = defense[0]
    if selection == []:
        selection = random.choice(available_moves)
    return selection


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


def check_for_win(current_player, current_players_selections, ways_to_win) -> bool:
    player_wins = False
    match_one = False
    match_two = False
    match_three = False
    for groups in ways_to_win:
        for cell in groups:
            for player_selection in current_players_selections:
                if player_selection == cell and match_one is False:
                    match_one = True
                elif player_selection == cell and match_two is False:
                    match_two = True
                elif player_selection == cell and match_three is False:
                    match_three = True
        if match_one is True and match_two is True and match_three is True:
            player_wins = True
            print_message('*', 11
                            , current_player + " WINS!", 2)
            break
        else:
            match_one = False
            match_two = False
            match_three = False

    return player_wins


def record_wins_and_losses(get_games_data, game_outcome, ranked_choices):
    value_plus_rank = []
    value_rank = []

    previous_game_data = get_games_data.get(game_outcome)

    if previous_game_data  == []:
        previous_rank = []
        previous_value = []
    else:
        previous_rank = [x for x, y in previous_game_data[0]]
        previous_value = [y for x, y in previous_game_data[0]]
    rank = previous_rank
    value = previous_value
    for choice in ranked_choices:
        for i in range(len(choice)):
            if choice[i] not in value:
                value.append(choice[i])
                rank.append(1)
            elif choice[i] in value:
                for j in range(len(value)):
                    if choice[i] == value[j]:
                        rank[j] = rank[j] + 1
    for i in range(len(rank)):
        value_plus_rank.append(rank[i])
        value_plus_rank.append(value[i])
        value_rank.append(value_plus_rank)
        value_plus_rank = []

    return value_rank


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
                selection = make_selection('O', get_wins_data, available_selection, i
                                           , vertical_string_one, vertical_string_two, vertical_string_three)
                available_selection.remove(selection)
                x_selected_cells.append(selection)
                player_mark = 'X'
            elif o_turn_to_play is True:
                selection = make_selection('X', get_wins_data, available_selection, i
                                           , vertical_string_one, vertical_string_two, vertical_string_three)
                available_selection.remove(selection)
                o_selected_cells.append(selection)
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

            if i >= 4:
                x_wins = check_for_win('X', x_selected_cells, WAYS_TO_WIN)

                o_wins = check_for_win('O', o_selected_cells, WAYS_TO_WIN)

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

    win_value_rank = record_wins_and_losses(game_data, 'WINS', ranked_winning_choices)
    loss_value_rank = record_wins_and_losses(game_data, 'LOSSES', ranked_losing_choices)

    new_wins_data = [win_value_rank]
    new_losses_data = [loss_value_rank]
    game_data.update({'WINS': new_wins_data})
    game_data.update({'LOSSES': new_losses_data})

    return game_data


def main():
    project_location = r'..\TicTacToe'
    name_of_file = r'\previous_game_data_2.0.json'
    total_games = 10_000

    previous_game_data = read_previous_game_data(project_location, name_of_file)

    run_game = play_game(VERTICAL_FORMAT, HORIZONTAL_FORMAT, previous_game_data, total_games)

    write_updated_game_data(project_location, name_of_file, run_game)


if __name__ == '__main__':
    main()
