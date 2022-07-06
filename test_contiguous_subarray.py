import unittest
import numpy as np
import contiguous_subarray

class TestContiguous(unittest.TestCase):
    
    def test_contiguous_subarray(self):
        self.assertEqual(contiguous_subarray.contiguous_subarray(np.array([-1, 5, 6, -5, -10, 5]))[1],  11)
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray(np.array([-1, 5, 6, -5, -10, 5]))[0],  np.array([5, 6]))
        
        self.assertEqual(contiguous_subarray.contiguous_subarray(np.array([40, 54, 16, 15, 100, 1]))[1], 226)
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray(np.array([40, 54, 16, 15, 100, 1]))[0],  np.array([40, 54, 16, 15, 100, 1]))
        
        self.assertEqual(contiguous_subarray.contiguous_subarray(np.array([-7, -1, -6, -5, -10, -5]))[1],  -1)      
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray(np.array([-7, -1, -6, -5, -10, -5]))[0],  np.array([-1]))  
    
    def test_contiguous_subarray_LC(self):
        self.assertEqual(contiguous_subarray.contiguous_subarray_LC(np.array([-1, 5, 6, -5, -10, 5]))[1],  11)
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray_LC(np.array([-1, 5, 6, -5, -10, 5]))[0],  np.array([5, 6]))
        
        self.assertEqual(contiguous_subarray.contiguous_subarray_LC(np.array([40, 54, 16, 15, 100, 1]))[1], 226)
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray_LC(np.array([40, 54, 16, 15, 100, 1]))[0],  np.array([40, 54, 16, 15, 100, 1]))
        
        self.assertEqual(contiguous_subarray.contiguous_subarray_LC(np.array([-7, -1, -6, -5, -10, -5]))[1],  -1)      
        np.testing.assert_array_equal(contiguous_subarray.contiguous_subarray_LC(np.array([-7, -1, -6, -5, -10, -5]))[0],  np.array([-1]))  
    
if __name__ == '__main__':
    unittest.main()
