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
        a = False
        b = False
        cin = False
        expected_sum = False
        expected_cout = False
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = False
        b = False
        cin = True
        expected_sum = True
        expected_cout = False
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = False
        b = True
        cin = False
        expected_sum = True
        expected_cout = False
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = True
        b = False
        cin = False
        expected_sum = True
        expected_cout = False
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = False
        b = True
        cin = True
        expected_sum = False
        expected_cout = True
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = True
        b = False
        cin = True
        expected_sum = False
        expected_cout = True
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = True
        b = True
        cin = False
        expected_sum = False
        expected_cout = True
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

        a = True
        b = True
        cin = True
        expected_sum = True
        expected_cout = True
        self.assertTrue(np.array_equal([expected_sum, expected_cout], lg.full_adder(a, b, cin)))

    def test_adder_16_bit(self):
        a = lg.get_bit_np_array("0000000000000000")
        b = lg.get_bit_np_array("0000000000000000")
        result = lg.get_bit_np_array("0000000000000000")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit(a, b)))

        a = lg.get_bit_np_array("1001101010100011")
        b = lg.get_bit_np_array("0111010110110011")
        result = lg.get_bit_np_array("0001000001010110")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit(a, b)))

        a = lg.get_bit_np_array("1111111111111111")
        b = lg.get_bit_np_array("0000000000000001")
        result = lg.get_bit_np_array("0000000000000000")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit(a, b)))
        
    def test_alu_16_bit(self):
        x = lg.get_bit_np_array("0101010101010101")
        y = lg.get_bit_np_array("1100110011001100")

        expected = ["0000000000000000", True, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["ZERO"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])


        expected = ["0000000000000001", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["ONE"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1111111111111111", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["NEGATIVE_1"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0101010101010101", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1100110011001100", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1010101010101010", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["!X"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0011001100110011", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["!Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1010101010101011", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["NEGATIVE_X"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0011001100110100", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["NEGATIVE_Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0101010101010110", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X+1"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1100110011001101", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["Y+1"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0101010101010100", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X-1"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1100110011001011", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["Y-1"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])
        
        expected = ["0010001000100001", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X+Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1000100010001001", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X-Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0111011101110111", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["Y-X"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["0100010001000100", False, False]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X&Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])

        expected = ["1101110111011101", False, True]
        result = lg.alu_binary_flags_16_bit(x, y, lg.get_bit_np_array(lg.alu_hashmap_to_binary["X|Y"]))
        self.assertEqual(expected, [lg.get_binary_number(result[0]), result[1], result[2]])


        


if __name__ == '__main__':
    unittest.main()


