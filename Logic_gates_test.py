import unittest
import numpy as np
import logic as lg
import assembler as assem



class TestFunctions(unittest.TestCase):
    def test_get_bit_np_array(self):
        binary_string = "101011"
        expected_result = np.array([True, False, True, False, True, True])
        result = lg.get_bit_np_array(binary_string)
        self.assertTrue(np.array_equal(result, expected_result))

    def test_convert_np_array_to_in(self):
        self.assertEqual(0, lg.convert_boolean_np_array_to_a_int(lg.get_bit_np_array("0000000000000000")))
        self.assertEqual(55012, lg.convert_boolean_np_array_to_a_int(lg.get_bit_np_array("1101011011100100")))
        self.assertEqual(52876, lg.convert_boolean_np_array_to_a_int(lg.get_bit_np_array("1100111010001100")))
        self.assertEqual(21057, lg.convert_boolean_np_array_to_a_int(lg.get_bit_np_array("0101001001000001")))
        self.assertEqual(14804, lg.convert_boolean_np_array_to_a_int(lg.get_bit_np_array("0011100111010100")))

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

    def test_adder_16_bit_no_creation(self):
        a = lg.get_bit_np_array("0000000000000000")
        b = lg.get_bit_np_array("0000000000000000")
        result = lg.get_bit_np_array("0000000000000000")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit_no_creation(a, b)))

        a = lg.get_bit_np_array("1001101010100011")
        b = lg.get_bit_np_array("0111010110110011")
        result = lg.get_bit_np_array("0001000001010110")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit_no_creation(a, b)))

        a = lg.get_bit_np_array("1111111111111111")
        b = lg.get_bit_np_array("0000000000000001")
        result = lg.get_bit_np_array("0000000000000000")
        self.assertTrue(np.array_equal(result, lg.adder_16_bit_no_creation(a, b)))


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

    def test_cpu_16_bit(self):
        cpu = lg.cpu_16_bit()
        # a instruction
        inM = lg.get_bit_np_array("1010111000100011")
        instruction = lg.get_bit_np_array("0101011011111100")
        reset = False
        expected = [lg.get_bit_np_array("0101011011111100"), False, lg.get_bit_np_array("0101011011111100"), lg.get_bit_np_array("0000000000000001")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))
        self.assertEqual(expected[1], result[1])
        self.assertTrue(np.array_equal(expected[2], result[2]))
        self.assertTrue(np.array_equal(expected[3], result[3]))
        self.assertTrue(np.array_equal(cpu.a_register, instruction))

        cpu = lg.cpu_16_bit()
        # c instruction
        inM = lg.get_bit_np_array("1010111000100011")
        a = "0"
        comp = lg.alu_hashmap_to_binary["ZERO"]
        dest = lg.dest_hashmap_to_binary["null"]
        instruction = lg.get_bit_np_array("0101011011111100")
        reset = False
        expected = [lg.get_bit_np_array("0101011011111100"), False, lg.get_bit_np_array("0101011011111100"), lg.get_bit_np_array("0000000000000001")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))
        self.assertEqual(expected[1], result[1])
        self.assertTrue(np.array_equal(expected[2], result[2]))
        self.assertTrue(np.array_equal(expected[3], result[3]))

    # Given type_instruction, a, comp, dest, jmp, returns the binary instruction for that  
    def get_instruction(self, type_instruction, a, comp, dest, jump):
        instruction = type_instruction + "11" + a + comp + dest + jump
        instruction = lg.get_bit_np_array(instruction)
        return instruction


    def test_comp_cpu_16_bit(self):
        cpu = lg.cpu_16_bit()
        inM = lg.get_bit_np_array("1010111000100011")
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["ZERO"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        reset = False
        expected = [lg.get_bit_np_array("0000000000000000")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["ONE"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0000000000000001")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["NEGATIVE_1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1111111111111111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # Sets a 
        instruction = lg.get_bit_np_array("0110101010010100")
        expected = [lg.get_bit_np_array("0110101010010100")]
        zero = lg.get_bit_np_array("0000000000000000")
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))
        self.assertTrue(np.array_equal(cpu.a_register, instruction))
        self.assertTrue(np.array_equal(cpu.d_register, zero))

        # d = a
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y"], lg.dest_hashmap_to_binary["D"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0110101010010100")]
        zero = lg.get_bit_np_array("0000000000000000")
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))
        self.assertTrue(np.array_equal(cpu.a_register, lg.get_bit_np_array("0110101010010100")))
        self.assertTrue(np.array_equal(cpu.d_register, cpu.a_register))

        # sets a 
        instruction = lg.get_bit_np_array("0101110011111111")
        expected = [lg.get_bit_np_array("0101110011111111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))
        self.assertTrue(np.array_equal(cpu.a_register, instruction))
        self.assertTrue(np.array_equal(cpu.d_register, lg.get_bit_np_array("0110101010010100")))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0110101010010100")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0101110011111111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1010111000100011")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["!X"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1001010101101011")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["!Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1010001100000000")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["!Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0101000111011100")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["NEGATIVE_X"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1001010101101100")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["NEGATIVE_Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1010001100000001")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["NEGATIVE_Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0101000111011101")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X+1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0110101010010101")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y+1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0101110100000000")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["Y+1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1010111000100100")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X-1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0110101010010011")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y-1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0101110011111110")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["Y-1"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1010111000100010")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X+Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1100011110010011")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["X+Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0001100010110111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X-Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0000110110010101")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["X-Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1011110001110001")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y-X"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1111001001101011")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["Y-X"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0100001110001111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X&Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0100100010010100")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["X&Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0010101000000000")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        # a = 0101110011111111
        # d = 0110101010010100
        # inM = 1010111000100011
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["X|Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("0111111011111111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        instruction = self.get_instruction("1", "1", lg.alu_hashmap_to_binary["X|Y"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["null"])
        expected = [lg.get_bit_np_array("1110111010110111")]
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(expected[0], result[0]))

        self.assertTrue(np.array_equal(cpu.program_counter, lg.get_bit_np_array("0000000000011111")))

    def test_dest_cpu_16_bit(self):
        cpu = lg.cpu_16_bit()
        zero = lg.get_bit_np_array("0000000000000000")
        inM = lg.get_bit_np_array("1010111000100011")
        instruction = lg.get_bit_np_array("0001111110001001")
        reset = False
        cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(cpu.a_register, instruction))
        self.assertTrue(np.array_equal(cpu.d_register, zero))

        inM = lg.get_bit_np_array("1010111000100011")
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["Y"], lg.dest_hashmap_to_binary["MD"], lg.jmp_hashmap_to_binary["null"])
        reset = False
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(cpu.a_register, lg.get_bit_np_array("0001111110001001")))
        self.assertTrue(np.array_equal(cpu.d_register, lg.get_bit_np_array("0001111110001001")))
        self.assertEqual(result[1], True)

        inM = lg.get_bit_np_array("1010111000100011")
        instruction = lg.get_bit_np_array("0100101010101110")
        reset = False
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(cpu.a_register, lg.get_bit_np_array("0100101010101110")))
        self.assertTrue(np.array_equal(cpu.d_register, lg.get_bit_np_array("0001111110001001")))
        self.assertEqual(result[1], False)

    def test_jump_cpu_16_bit(self):
        cpu = lg.cpu_16_bit()
        inM = lg.get_bit_np_array("1010111000100011")
        reset = False

        instruction = lg.get_bit_np_array("0001111110001001")
        cpu.operation(inM, instruction, reset)
        instruction = self.get_instruction("1", "0", lg.alu_hashmap_to_binary["ZERO"], lg.dest_hashmap_to_binary["null"], lg.jmp_hashmap_to_binary["JMP"])
        
        result = cpu.operation(inM, instruction, reset)
        self.assertTrue(np.array_equal(lg.get_bit_np_array("0001111110001001"), cpu.program_counter))
        pass
    
    # We can set the a register correctly
    def test_a_instruction_assembly_code(self):
        assembly_code = """
            @10
        """
        cmp = lg.hack_computer()
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 1)
        expected = "0000000000001010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        assembly_code = """
            @20002
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 1)
        expected = "0100111000100010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        assembly_code = """
            @9210
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 1)
        expected = "0010001111111010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

    def test_dest_registers_assembly(self):
        cmp = lg.hack_computer()


        # null
        assembly_code = """
            @16
            null=A
            null=D
            null=M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected_a_register = "0000000000010000"
        expected_d_register = "0000000000000000"
        expected_M = "0000000000000000"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[16]))

        # M
        assembly_code = """
            @69
            D=A
            @22
            M=D
        """

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected_a_register = "0000000000010110"
        expected_d_register = "0000000001000101"
        expected_M = "0000000001000101"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[22]))

        # D
        assembly_code = """
            @2123
            D=A
        """

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected_a_register = "0000100001001011"
        expected_d_register = "0000100001001011"
        expected_M = "0000000000000000"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[2123]))

        # MD
        assembly_code = """
            @8005
            MD=A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected_a_register = "0001111101000101"
        expected_d_register = "0001111101000101"
        expected_M = "0001111101000101"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[8005]))

        # A
        assembly_code = """
            @4444
            D=A+1
            A=A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected_a_register = "0001000101011100"
        expected_d_register = "0001000101011101"
        expected_M = "0000000000000000"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[4444]))

        # AM
        assembly_code = """
            @6543
            AM=A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected_a_register = "0001100110001111"
        expected_d_register = "0001000101011101"
        expected_M = "0001100110001111"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[6543]))

        #AD
        assembly_code = """
            @23002
            AMD=A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected_a_register = "0101100111011010"
        expected_d_register = "0101100111011010"
        expected_M = "0101100111011010"
        self.assertEqual(expected_a_register, lg.get_binary_number(cmp.cpu.a_register))
        self.assertEqual(expected_d_register, lg.get_binary_number(cmp.cpu.d_register))
        self.assertEqual(expected_M, lg.get_binary_number(cmp.data_memory[23002]))


    def test_comp_assembly(self):
        cmp = lg.hack_computer()

        # 0
        assembly_code = """
            @12345
            A=0
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        # 1
        assembly_code = """
            @12345
            A=1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000001"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        # -1
        assembly_code = """
            @12345
            A=-1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        # D
        assembly_code = """
            @12345
            D=A
            @23
            A=D
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0011000000111001"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.a_register))

        # A
        assembly_code = """
            @2031
            D=A
            @2000
            M=D
            @2000
            D=A


        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6)
        expected = "0000011111010000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # M
        assembly_code = """
            @2031
            D=A
            @2000
            M=D
            @2000
            D=M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6)
        expected = "0000011111101111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))
           

        
        

        


if __name__ == '__main__':
    unittest.main()


