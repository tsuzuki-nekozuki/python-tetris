import unittest

from tetris.core.player_status import PlayerStatus


class TestPlayerStatus(unittest.TestCase):
    def test_add_score(self):
        """Test score calculation."""
        pl_status1 = PlayerStatus(score=0, lines=5, level=0)
        # Add (300 * 1)
        pl_status1.add_score(3)
        self.assertEqual(pl_status1.score, 300)
        pl_status2 = PlayerStatus(score=1000, lines=15, level=3)
        # Add 1000 + 100 * (3 * 1) + 1200 * (3 * 1)
        pl_status2.add_score(2)
        pl_status2.add_score(4)
        self.assertEqual(pl_status2.score, 6200)

    def test_calculate_level(self):
        """Test level calculation."""
        # No update
        pl_status1 = PlayerStatus(score=0, lines=5, level=0)
        pl_status1.calculate_level()
        self.assertEqual(pl_status1.level, 0)
        # Need update
        pl_status2 = PlayerStatus(score=0, lines=33, level=0)
        pl_status2.calculate_level()
        self.assertEqual(pl_status2.level, 3)
        # Need update
        pl_status3 = PlayerStatus(score=0, lines=5, level=3)
        pl_status3.calculate_level()
        self.assertEqual(pl_status3.level, 0)
        # Reach maximum
        pl_status4 = PlayerStatus(score=0, lines=300, level=20)
        pl_status4.calculate_level()
        self.assertEqual(pl_status4.level, 20)

    def test_add_score_raises_value_error(self):
        """Test wrong cleared lines."""
        pl_status1 = PlayerStatus(score=0, lines=0, level=0)
        with self.assertRaises(ValueError) as cm:
            pl_status1.add_score(5)
        self.assertIn('Wrong cleared lines: 5', str(cm.exception))

        pl_status2 = PlayerStatus(score=0, lines=0, level=0)
        with self.assertRaises(ValueError) as cm:
            pl_status2.add_score(-1)
        self.assertIn('Wrong cleared lines: -1', str(cm.exception))


if __name__ == '__main__':
    unittest.main()
