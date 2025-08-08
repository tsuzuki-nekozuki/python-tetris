import os

from tetris.scenes.tetris_cli_controller import TetrisCli


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def render_board(data: dict) -> str:
    lines = []
    for y in range(data['board'].shape[0]):
        line = ''
        for x in range(data['board'].shape[1]):
            cell1 = data['board'][y, x]
            cell2 = data['active'][y, x]
            if cell1 != 0:
                line += '#'
            elif cell2 != 0:
                line += 'o'
            else:
                line += '.'
        lines.append(line)
    return '\n'.join(lines)


def render_status(data: dict) -> str:
    return '\n SCORE: {}\n'.format(data['score'])


def tetris_cli():
    controller = TetrisCli()

    controller.create_new_tetrimino()
    while True:
        clear_screen()

        view_data = controller.render_data()
        print(render_board(view_data))
        print(render_status(view_data))
        print('ACTIONS: a=LEFT, d=RIGHT, s=DOWN, e=CLOCKWISE, '
              'w=COUNTERCLOCKWISE, q=EXIT')

        if controller.is_game_over():
            print('Game Over!')
            break

        key = input('>> ').strip()

        if key == 'q':
            print('Exit tetris CLI. See again!')
            break
        elif key == 'a':
            controller.move_left()
        elif key == 'd':
            controller.move_right()
        elif key == 's':
            controller.move_down()
        elif key == 'e':
            controller.rotate_cw()
        elif key == 'w':
            controller.rotate_ccw()
        controller.step()


if __name__ == '__main__':
    tetris_cli()
