import sys
import time


def cycle(tlight):
    """
    displays the current_color_art for a TrafficLight object
      for the duration of current_color_time
    :param tlight: TrafficLight object
    """
    seconds = tlight.get_current_color_time()
    while seconds > 0:
        print chr(27) + "[2J"
        print " ~ " + str(seconds)
        print tlight.get_current_art()
        if seconds >= 1:
            time.sleep(1)
        elif seconds >= 0:
            time.sleep(seconds)
        seconds -= 1
    tlight.switch_light()


def run_cycles(tlight, cycles):
    """
    runs a certain number of cycles
    :param tlight: TrafficLight object
    :param cycles: number of cycles you want to run
    """
    if cycles == 'forever':
        while True:
            cycle(tlight)
    else:
        cycles *= 3
        while cycles > 0:
            cycle(tlight)
            cycles -= 1


def handle_input(prompt, outputtype='float'):
    """
    Handles user input, if 'exit' is typed exits program.
    If a non-float is entered it asks user to re-enter input
    :param prompt: string of text for the user prompt
    :param outputtype: a string specifying whether desired datatype of output is int or float
    """
    user_input = raw_input(prompt)
    while True:
        if user_input == 'exit':
            print "Exiting Traffic Light Simulator. Goodbye!"
            sys.exit()
        elif outputtype == 'int' and user_input == 'forever':
            return 'forever'
        try:
            output = float(user_input)
            if output > 0:
                return output
            else:
                raise ValueError('Negative numbers are not allowed')
        except ValueError:
            print "Whoops! That's not right! Please try again."
            user_input = raw_input(prompt)
