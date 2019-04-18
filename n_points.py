
# coding: utf-8


import unittest


class Graph():
    def __init__(self,N):
        self.N=N
        self.groups=[[x] for x in range(N)]
        
    def get_group_containing(self, p1):
        for x in self.groups:
            if p1 in x:
                return x

    def is_object_correct(self, p):
        return p in range(self.N)
    
    def union(self, p1, p2):
        if not (self.is_object_correct(p1) and self.is_object_correct(p2)):
            return False

        p1_group=self.get_group_containing(p1) 
        p2_group=self.get_group_containing(p2)
        
        # merge groups
        if not p1_group==p2_group:
            p1_group.extend(p2_group)
            self.groups.remove(p2_group)
            
        return True       
    
    def is_connected(self,p1,p2):
        if self.is_object_correct(p1) and self.is_object_correct(p2):
            return bool([x for x in self.groups if p1 in x and p2 in x])
        else:
            return "Invalid point"
                
        
        
        
class PointsTest(unittest.TestCase):
    def setUp(self):
            self.gr=Graph(10)
            self.gr.union(4,3)
            self.gr.union(3,8)
            self.gr.union(6,5)
            self.gr.union(9,4)
            self.gr.union(2,1)
                
    def test_0_7(self):
        self.assertFalse(self.gr.is_connected(0,7))
        
    def test_8_9(self):
        self.assertTrue(self.gr.is_connected(8,9))
        
    def test_invalid_points_8_15(self):
        actual_type=self.gr.is_connected(8,15)
        self.assertEqual("Invalid point",actual_type)
        
    def test_invalid_points_less_zero(self):
        actual_type=self.gr.is_connected(-1,15)
        self.assertEqual("Invalid point",actual_type)
        
    def test_add_valid_point(self):
        self.assertTrue(self.gr.union(2,5))
    
    def test_add_invalid_point(self):
        self.assertFalse(self.gr.union(-1,5))
    
    def test_connect_again(self):
        self.gr.union(9,5)
        self.assertTrue(self.gr.union(9,5))
        
    
if __name__=="__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

