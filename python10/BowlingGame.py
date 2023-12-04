import unittest
class BowlingGame:
    def __init__(self):
        self.rolls=[]
        """Initialize the BowlingGame"""

    def roll(self,pins):
        self.rolls.append(pins)
        """
        Record a roll
        
        Parameters:
        pins(int): The number of pins
        """
        

    def score(self):
        """
        Calculate the total score

        Returns:
            int: The total score
        """
        result = 0
        roll_index=0
        for frame_index in range(10):
            if  self.is_strike(roll_index):
                result += self.strike_score(roll_index)
                roll_index +=1
            elif self.is_spare(roll_index):
                result += self.spare_score(roll_index)
                roll_index +=2
            else:
                result += self.frame_score(roll_index)
                roll_index +=2
        return result

    def is_strike(self, roll_index):
        """Check if a roll is strike.

        Args:
            roll_index (int): The index of the roll

        Returns:
            bool: True strike,False otherwise
        """
        return self.rolls[roll_index] == 10
    def is_spare(self, roll_index):
        """
        Check if a spare
        

        Args:
            
            roll_index (int): The index of the roll

        Returns:
            bool:True if a spare, False otherwise
        """
        return self.rolls[roll_index]+ self.rolls[roll_index+1]==10
    def strike_score(self,roll_index):
        """Calculate the score for a frame with a strike

        Args:
            roll_index (int): The index of the roll

        Returns:
            int: The score for the frame with a strike
        """
        return  10+ self.rolls[roll_index+1]+ self.rolls[roll_index+2]

    def spare_score(self,roll_index):
        """Calculate the score for a frame with a spare.

        Args:
            roll_index (int): The index of the roll

        Returns:
            int: The score for the frame with a spare
        """
        return  10+ self.rolls[roll_index+2]

    def frame_score(self, roll_index):
        """Calculate a regular frame

        Args:
            roll_index (int): The index of the roll

        Returns:
            int: The score for the regular frame
        """
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
		
class TestBowlingGame(unittest.TestCase):
    
    def setUp(self):
        """Set up a new test case"""
        self.game = BowlingGame()
  
    def test_all_strikes(self):
        """ Test all strikes"""
        
        for i in range(12):  
         self.game.roll(10)
        assert self.game.score() == 300

    def test_all_spares(self):
        """Test all spares"""
        for i in range(21):  
         self.game.roll(5)
        assert self.game.score() == 150
        
if __name__ == '__main__':
    unittest.main()