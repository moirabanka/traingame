import os
import sys
import termios
import time
import tty
import select

def flush_input(fd):
    """Flush any input typed during raw mode."""
    while True:
        # Check if there's data to read
        rlist, _, _ = select.select([fd], [], [], 0)
        if rlist:
            os.read(fd, 1024)  # discard up to 1024 bytes
        else:
            break

def main():
    global time_elapsed
    time_elapsed = 0
    while True:
    # Prompt and read from stdin
        prompt = "Enter something: "
        sys.stdout.write(prompt)
        sys.stdout.flush()
        user_input = sys.stdin.readline().strip()  # read input from terminal



        fd=sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)

            # Simulate streaming the alphabet one character at a time
            response = "abcdefghijklmnopqrstuvwxyz"
            for char in response:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)  # 10ms delay

            sys.stdout.write('\r\n')  # for a clean newline after the stream
            sys.stdout.flush()

        finally:
            flush_input(fd)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    main()
