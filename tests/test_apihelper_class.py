import unittest

import telebot


class TestApiHelper(unittest.TestCase):

    def setUp(self):
        self.token = '929815979:AAE61Q9DOyln8E1RLkLvpIoAsF8Xn8nRFEc'
        self.valid_proxy = {'https': 'https://Selwebjon01:J7l2UoM@191.101.148.229:45785'}
        
        self.invalid_proxy = {'https': 'https://test:test@000.000.000.229:45785'} 

    def test_telebot(self):
        bot1 = telebot.TeleBot(self.token, proxy=self.valid_proxy)
        bot2 = telebot.TeleBot(self.token, proxy=self.invalid_proxy)

        print(bot1.get_me())
        print('*'*50)
        print(bot2.get_me())