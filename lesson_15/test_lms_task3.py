import unittest
from lms_task3 import TVController

class ChannelTestCase(unittest.TestCase):
    
    channels = TVController(['BBC', 'Discovery', 'TV1000'])
    
    def test_first_channel(self):
        ChannelTestCase.channels.next_channel()
        self.assertEqual(ChannelTestCase.channels.first_channel(), 'BBC')
        ChannelTestCase.channels.next_channel()
        self.assertNotEqual(ChannelTestCase.channels.first_channel(), 'Discovery')
    
    def test_last_channel(self):
        ChannelTestCase.channels.next_channel()
        self.assertEqual(ChannelTestCase.channels.last_channel(), 'TV1000')
        ChannelTestCase.channels.first_channel()
        self.assertNotEqual(ChannelTestCase.channels.last_channel(), 'BBC')
    
    def test_turn_channel(self):
        self.assertEqual(ChannelTestCase.channels.turn_channel(2), 'Discovery')
        self.assertNotEqual(ChannelTestCase.channels.current_channel(), 'TV1000')

unittest.main()