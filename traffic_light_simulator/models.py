import os

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))


class TrafficLight():
    """ Traffic Light object to load artwork and keep track of state """

    def __init__(self, initial_color='red', red_time=1, yellow_time=1, green_time=1):
        """
        load artwork and set initial color
        :param initial_color: sets initial value for current_color color property
        :param red_time: sets amount of time for a red light to last
        :param yellow_time: sets amount of time for a yello light to last
        :param green_time: sets amount of time for a green light to last
        """
        red = open(PACKAGE_ROOT + '/light_art/red.txt', 'r').read()
        yellow = open(PACKAGE_ROOT + '/light_art/yellow.txt', 'r').read()
        green = open(PACKAGE_ROOT + '/light_art/green.txt', 'r').read()
        self.light_art = {
            'red': red,
            'yellow': yellow,
            'green': green
        }
        self.light_time = {
            'red': red_time,
            'yellow': yellow_time,
            'green': green_time
        }
        self.current_color = initial_color

    def switch_light(self):
        """ sets current_color to next color in the sequence """
        if self.current_color == 'red':
            self.current_color = 'green'
        elif self.current_color == 'green':
            self.current_color = 'yellow'
        elif self.current_color == 'yellow':
            self.current_color = 'red'

    def get_current_art(self):
        """ returns art for the current color """
        return self.light_art[self.current_color]

    def get_current_color(self):
        """ returns text representation of the current color """
        return self.current_color

    def get_current_color_time(self):
        """ returns the time for the current color """
        return self.light_time[self.current_color]
