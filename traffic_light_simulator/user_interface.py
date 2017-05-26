from models import TrafficLight
from helpers import handle_input, run_cycles


def main():

    print " "
    print " "
    print "################"
    print " "
    print "Welcome to the Traffic Light Simulator!"
    print "If at any time you'd like to exit just type 'exit'"
    print " "
    print "################"
    print " "
    print " "

    while True:

        try:
            print "Remember, if you want to quit just type 'exit'"
            print "To run infinite cycles you can enter 'forever'"
            print "If you want to stop the cycles please use ctrl+c"
            print "--------------------------------"
            cycles = handle_input("How many cycles of lights would you like to run? ",
                                  outputtype='int')
            green = handle_input("How many seconds should a green light last? ")
            yellow = handle_input("How many seconds should a yellow light last? ")
            red = handle_input("How many seconds should a red light last? ")

            light = TrafficLight(initial_color='green', 
                                 green_time=green, 
                                 yellow_time=yellow, 
                                 red_time=red)
            run_cycles(light, cycles)
        except (KeyboardInterrupt, EOFError):
            print " "


    print " "
    print " "
    print "################"
    print " "
    print "Exiting Traffic Light Simulator. Goodbye!"
    print " "
    print "################"
    print " "
    print " "

if __name__ == "__main__":
    main()
