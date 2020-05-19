# -*- coding: utf-8 -*-
'''  Tests for MPK.py '''


import unittest

import MPK
 
class TicketTest(unittest.TestCase):
    x=2.30
    y=4.60
    def test_ticketCosts(self):
        self.assertEqual(MPK.Traveler.ticketCosts("yes"),self.x)
        self.assertEqual(MPK.Traveler.ticketCosts("no"),self.x+self.y)
    
    def test_geTicketCosts(self):
        #MPK.Traveler.ticketCosts("yes")
        self.assertEqual(MPK.Traveler.getTicketCosts(),self.x)

    
if __name__ == '__main__':
    unittest.main()
    