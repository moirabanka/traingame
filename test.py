import shutil, textwrap, time, sys, termios, tty
from game_data import new_game

#this should be made to run in another thread so that it can be canceled by player input
def slow_print(input_text):
    global operating_system
    if operating_system == 'unix':
        global file_descriptor, stdin_settings
        new_settings = list(stdin_settings)
        new_settings[3] &= ~(termios.ICANON | termios.ECHO)
        try:
            #tty.setraw(file_descriptor)
            termios.tcsetattr(file_descriptor, termios.TCSAFLUSH, new_settings)
            for character in input_text:
                sys.stdout.write(character)
                sys.stdout.flush()
                match character:
                    case ',' | '.' | '!' | '?' |';':
                        time.sleep(.2)
                    case ' ':
                        continue
                    case _:
                        time.sleep(.025)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSANOW, stdin_settings)
    else:
        for character in input_text:
            sys.stdout.write(character)
            sys.stdout.flush()
            match character:
                case ',' | '.' | '!' | '?' |';':
                    time.sleep(.2)
                case ' ':
                    continue
                case _:
                    time.sleep(.025)


def wait_for_keypress(prompt="    (Press any key to continue)"):
    print(prompt, end='', flush=True)
    if sys.platform.startswith('win'):
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
        msvcrt.getch()
    else:
        global file_descriptor, stdin_settings
        try:
            tty.setraw(file_descriptor)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(file_descriptor, termios.TCSADRAIN, stdin_settings)

def narrate(narration_dict):
    terminal_width = shutil.get_terminal_size(fallback = 70).columns
    if terminal_width >= 74: 
        terminal_width = 70
    else:
        terminal_width -= 4
    if type(narration_dict) == str:
        narration_dict = {1:narration_dict}
    for sequence, text in narration_dict.items():
        formatted_narration = textwrap.fill(
            text,
            width=terminal_width,
            initial_indent='   ',
            subsequent_indent='    ',
            replace_whitespace=True,
            drop_whitespace=True,
            break_long_words=False,
            break_on_hyphens=False
        )
        if sequence == 1:
            print('\n', end='')
            slow_print(formatted_narration)
            print('\n')
        else:
            sys.stdout.write('\r' + '                               ' + '\r')
            sys.stdout.flush()
            slow_print(formatted_narration)
            print('\n')
        if int(sequence) < len(narration_dict):
            wait_for_keypress()


if sys.platform.startswith('win'):
    operating_system = 'windows'
else:
    operating_system = 'unix'
    file_descriptor = sys.stdin.fileno()
    stdin_settings = termios.tcgetattr(file_descriptor)

print(operating_system)
narrate(new_game['narration'])