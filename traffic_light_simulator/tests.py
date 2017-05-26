import unittest
from models import TrafficLight

class TrafficLightTestCase(unittest.TestCase):
    
    def test_if_green_light_art_set(self):
        light = TrafficLight()
        self.assertIsNotNone(light.light_art['green'])

    def test_if_yellow_light_art_set(self):
        light = TrafficLight()
        self.assertIsNotNone(light.light_art['yellow'])

    def test_if_red_light_art_set(self):
        light = TrafficLight()
        self.assertIsNotNone(light.light_art['red'])

    def test_if_green_light_time_set(self):
        light = TrafficLight(green_time=2)
        self.assertEqual(light.light_time['green'], 2)

    def test_if_yellow_light_time_set(self):
        light = TrafficLight(yellow_time=3)
        self.assertEqual(light.light_time['yellow'], 3)

    def test_if_red_light_time_set(self):
        light = TrafficLight(red_time=1)
        self.assertEqual(light.light_time['red'], 1)

    def test_if_red_goes_to_green(self):
        light = TrafficLight(initial_color='red')
        light.switch_light()
        self.assertEqual(light.current_color, 'green')

    def test_if_green_goes_to_yellow(self):
        light = TrafficLight(initial_color='green')
        light.switch_light()
        self.assertEqual(light.current_color, 'yellow')

    def test_if_yellow_goes_to_red(self):
        light = TrafficLight(initial_color='yellow')
        light.switch_light()
        self.assertEqual(light.current_color, 'red')
    
    def test_if_get_current_art_returns_something(self):
        light = TrafficLight(initial_color='green')
        current_color = light.get_current_art()
        self.assertIsNotNone(current_color)

    def test_if_get_current_color_returns_green_after_initializing_green(self):
        light = TrafficLight(initial_color='green')
        current_color = light.get_current_color()
        self.assertEqual(current_color, 'green')

    def test_if_get_current_color_time_returns_correct_time(self):
        light = TrafficLight(initial_color='green', green_time=3)
        current_color_time = light.get_current_color_time()
        self.assertEqual(current_color_time, 3)
        
        


if __name__ == '__main__':
    unittest.main()
