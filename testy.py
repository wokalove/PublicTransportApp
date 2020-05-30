'''  Tests for MPK.py '''

import unittest
import MPK

class TravelerTest(unittest.TestCase):
    def setUp(self):
        self.t = MPK.Traveler()
    def test_ticket_costs(self):
        self.t.ticket_costs = "yes"
        self.assertEqual(self.t.ticket_costs,MPK.Traveler.REDUCED_PRICE)

if __name__ == '__main__':
    unittest.main()
    