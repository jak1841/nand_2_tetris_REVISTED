import unittest
import numpy as np
import logic as lg


class TestFunctions(unittest.TestCase):
    def test_get_bit_np_array(self):
        binary_string = "101011"
        expected_result = np.array([True, False, True, False, True, True])
        result = lg.get_bit_np_array(binary_string)
        self.assertTrue(np.array_equal(result, expected_result))

    def test_multiplexor(self):
        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("0"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("0"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1"), lg.multiplexor(a, b, sel)))


        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("0"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("0"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1"), lg.multiplexor(a, b, sel)))


        """
        
            16 bit bus
        
        """

        a = lg.get_bit_np_array("1010101010100111")
        b = lg.get_bit_np_array("1000000000000001")
        sel = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1010101010100111"), lg.multiplexor(a, b, sel)))

        a = lg.get_bit_np_array("1010101010100111")
        b = lg.get_bit_np_array("1000000000000001")
        sel = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal(lg.get_bit_np_array("1000000000000001"), lg.multiplexor(a, b, sel)))

    def test_demultiplexor(self):
        data = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("0")
        result = lg.demultiplexor(data, sel)
        
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("1"), lg.get_bit_np_array("0")])))

        data = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("0")
        result = lg.demultiplexor(data, sel)
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("0"), lg.get_bit_np_array("0")])))

        data = lg.get_bit_np_array("0")
        sel = lg.get_bit_np_array("1")
        result = lg.demultiplexor(data, sel)
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("0"), lg.get_bit_np_array("0")])))

        data = lg.get_bit_np_array("1")
        sel = lg.get_bit_np_array("1")
        result = lg.demultiplexor(data, sel)
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("0"), lg.get_bit_np_array("1")])))

        """
        
            16 Bit bus
        
        """

        data = lg.get_bit_np_array("1011111111111111")
        sel = lg.get_bit_np_array("0")
        result = lg.demultiplexor(data, sel)
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("1011111111111111"), lg.get_bit_np_array("0000000000000000")])))

        data = lg.get_bit_np_array("1011111111111111")
        sel = lg.get_bit_np_array("1")
        result = lg.demultiplexor(data, sel)
        self.assertTrue(np.array_equal(result, np.array([lg.get_bit_np_array("0000000000000000"), lg.get_bit_np_array("1011111111111111")])))

    def test_full_adder(self):
        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("0")
        cin = lg.get_bit_np_array("0")
        expected_sum = lg.get_bit_np_array("0")
        expected_cout = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("0")
        cin = lg.get_bit_np_array("1")
        expected_sum = lg.get_bit_np_array("1")
        expected_cout = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("1")
        cin = lg.get_bit_np_array("0")
        expected_sum = lg.get_bit_np_array("1")
        expected_cout = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("0")
        cin = lg.get_bit_np_array("0")
        expected_sum = lg.get_bit_np_array("1")
        expected_cout = lg.get_bit_np_array("0")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("0")
        b = lg.get_bit_np_array("1")
        cin = lg.get_bit_np_array("1")
        expected_sum = lg.get_bit_np_array("0")
        expected_cout = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("0")
        cin = lg.get_bit_np_array("1")
        expected_sum = lg.get_bit_np_array("0")
        expected_cout = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("1")
        cin = lg.get_bit_np_array("0")
        expected_sum = lg.get_bit_np_array("0")
        expected_cout = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = lg.get_bit_np_array("1")
        b = lg.get_bit_np_array("1")
        cin = lg.get_bit_np_array("1")
        expected_sum = lg.get_bit_np_array("1")
        expected_cout = lg.get_bit_np_array("1")
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))




        


if __name__ == '__main__':
    unittest.main()


