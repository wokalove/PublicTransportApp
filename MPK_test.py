'''  Tests for MPK.py '''

import unittest
import MPK

class TravelerTest(unittest.TestCase):
    ''' Running tests for Traveler class'''
    def setUp(self):
        self.t = MPK.Traveler()
    def test_ticket_costs(self):
        self.t.ticket_costs = "yes"
        self.assertEqual(self.t.ticket_costs, MPK.Traveler.REDUCED_PRICE)

class FindPathTest(unittest.TestCase):
    ''' Running tests for find_shortest_path_function'''
    def setUp(self):
        self.graf = {'pktA':{'pktB':['1', '2'], 'pktD':['7', '8']},
                    'pktB':{'pktD':['9', '11']},
                    'pktD':{'pktA':['11', '12'],'pktC':['89', '83']},
                    'pktC':{'pktA':['3', '7']}
                    }

    def test_find_shortest_path_first(self):
        self.result1 = 'pktA, pktB'
        self.assertEqual(MPK.find_shortest_path(self.graf,'pktA','pktB'),
                                                         (self.result1))
    def test_find_shortest_path_second(self):
        self.result2 = 'pktB, pktD, pktC'
        self.assertEqual(MPK.find_shortest_path(self.graf,'pktB','pktC'),
                                                         (self.result2))
        
if __name__ == '__main__':
    unittest.main()
    