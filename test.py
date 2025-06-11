import shutil, textwrap, threading, time, sys
from game_data import new_game

#this should be made to run in another thread so that it can be canceled by player input
def slow_print(input_text):
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
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        termios.tcflush(fd, termios.tcgetattr(fd))
        # this try/finally probably is not necessary and can be simplified
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

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
            slow_print(formatted_narration)
            print('\n')
        else:
            sys.stdout.write('\r' + '                               ' + '\r')
            sys.stdout.flush()
            slow_print(formatted_narration)
            print('\n')
        if int(sequence) < len(narration_dict):
            wait_for_keypress()
            # stop_event = threading.Event()

            # def flashing_prompt(text=' >', interval=0.5):
            #     visible = True
            #     while not stop_event.is_set():
            #         #print('\r' + (text if visible else '  '), end='', flush=True)
            #         sys.stdout.write('\r' + (text if visible else '  '))
            #         sys.stdout.flush()
            #         visible = not visible
            #         time.sleep(interval)
            #     else:
            #         if visible == True:
            #             sys.stdout.write('\r' + (text if visible else '  '))
            #             sys.stdout.flush()    

            # flasher = threading.Thread(target=flashing_prompt, daemon=False)
            # flasher.start()
            # if input():
            #     stop_event.set()
            # flasher.join()


            

narrate(new_game['narration'])