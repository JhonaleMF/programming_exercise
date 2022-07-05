import unittest
import contiguous_subarray

class TestCalc(unittest.TestCase):
    
    def test_contiguous_subarray(self):
        self.assert_Equal(contiguous_subarray.contiguous_subarray(0,5), 15)
        self.assert_Equal(contiguous_subarray.contiguous_subarray(0,5), 15)
        self.assert_Equal(contiguous_subarray.contiguous_subarray(0,5), 15)
    
    def test_contiguous_subarray_LC(self):
        self.assert_Equal(contiguous_subarray.contiguous_subarray_LC(0,5), 15)
        self.assert_Equal(contiguous_subarray.contiguous_subarray_LC(0,5), 15)
        self.assert_Equal(contiguous_subarray.contiguous_subarray_LC(0,5), 15)        
    
if __name__ == '__main__':
    unittest.main()