"""
121. Best Time to Buy and Sell Stock (Easy)
"""
import unittest

def maxProfit(prices):
    buy = float('inf')
    profit = 0
    for p in prices:
        buy = min(buy, p)
        profit = max(profit, p - buy)
    return profit

class TestCase(unittest.TestCase):
    def test_1(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(maxProfit(prices), 5)
    
    def test_2(self):
        prices = [7,6,4,3,1]
        self.assertEqual(maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()