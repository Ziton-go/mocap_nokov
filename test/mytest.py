import rospy
import unittest

class TestExample(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)

if __name__ == '__main__':
    import rostest
    rostest.rosrun('mocap_nokov', 'mytest', TestExample)

