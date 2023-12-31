import unittest
import numpy as np
import logic as lg
import assembler as assem
import vm 
import syntax_analayzer as sa



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
           
        # !D
        assembly_code = """
            @2031
            D=A
            D=!D
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "1111100000010000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # !A
        assembly_code = """
            @2031
            D=!A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "1111100000010000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        #!M
        assembly_code = """
            @7821
            M=A
            D=!M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "1110000101110010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        #-D
        assembly_code = """
            @1
            D=A
            D=-D
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # -A 
        assembly_code = """
            @128
            D=-A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "1111111110000000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # -M 
        assembly_code = """
            @22
            M=-A
            D=-M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "0000000000010110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D+1
        assembly_code = """
            @203
            D=A
            D=D+1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "0000000011001100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # A+1
        assembly_code = """
            @99
            D=A+1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "0000000001100100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # M+1
        assembly_code = """
            @99
            D=A
            M=D
            D=M+1

        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0000000001100100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D-1
        assembly_code = """
            @0
            D=A
            D=D-1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # A-1
        assembly_code = """
            @0
            D=A-1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # M-1
        assembly_code = """
            @8123
            M=A
            D=M-1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3)
        expected = "0001111110111010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D+A 
        assembly_code = """
            @2222
            D=A
            @3333
            D=D+A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0001010110110011"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D+M
        assembly_code = """
            @9999
            M=A
            @1111
            D=A
            @9999
            D=D+M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6)
        expected = "0010101101100110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D-A
        assembly_code = """
            @921
            D=A
            @21
            D=D-A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0000001110000100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D-M
        assembly_code = """
            @921
            D=A
            @2923
            M=A
            D=D-M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5)
        expected = "1111100000101110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # A-D
        assembly_code = """
            @911
            D=A
            @420
            D=A-D
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "1111111000010101"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # M-D
        assembly_code = """
            @911
            D=A
            @4266
            M=A
            D=M-D
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5)
        expected = "0000110100011011"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D&A
        assembly_code = """
            @911
            D=A
            @4266
            D=D&A
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0000000010001010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D&M
        assembly_code = """
            @911
            D=A
            @4266
            M=A
            D=D&M
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5)
        expected = "0000000010001010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D|M
        assembly_code = """
            @911
            D=A
            @4266
            M=A
            D=D|M
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5)
        expected = "0001001110101111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D|M
        assembly_code = """
            @1
            D=A
            @2000
            
            M=-D
            @0
            D=0
            @2000
            D=D|M


        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 8)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))


        # D|A
        assembly_code = """
            @911
            D=A
            @4266
            D=D|A
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "0001001110101111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D|A
        assembly_code = """
            @0
            D=A
            @1
            A=-A
            D=D|A
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5)
        expected = "1111111111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D*A
        assembly_code = """
            @3
            D=A
            @6
            D=D*A
            @2000
            D=D*A
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6)
        expected = "1000110010100000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D*M
        assembly_code = """
            @89
            D=A
            @2000
            
            M=D
            @23
            D=A
            @2000
            D=D*M
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 8)
        expected = "0000011111111111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))


        # D/A
        assembly_code = """
            @420
            D=A
            @20
            D=D/A          
            @7
            D=D/A  
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6)
        expected = "0000000000000011"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))


        # D/M
        assembly_code = """
            @2
            D=A
            @2000
            
            M=D
            @11
            D=A
            @2000
            D=D/M
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 8)
        expected = "0000000000000101"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D/M
        assembly_code = """
            @5
            D=A
            @2000
            
            M=D
            @12345
            D=A
            @2000
            D=D/M
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 8)
        expected = "0000100110100101"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D^A
        assembly_code = """
            @2
            D=A
            @15
            D=D^A
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 4)
        expected = "1000000000000000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))

        # D^M
        assembly_code = """
            @10
            D=A
            @2000
            
            M=D
            @3
            D=A
            @2000
            D=D^M
        """
       

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 8)
        expected = "1110011010101001"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.d_register))


        
    def test_jump_assembly(self):
        cmp = lg.hack_computer()

        # null
        expected = "0000000000000000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))
        assembly_code = """
            @1000
            D=D+1
            A=M
            D=-1
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 1)
        expected = "0000000000000001"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        cmp.do_n_operations(False, 1)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        cmp.do_n_operations(False, 1)
        expected = "0000000000000011"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        cmp.do_n_operations(False, 1)
        expected = "0000000000000100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        cmp.do_n_operations(False, 10000)
        expected = "0010011100010100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JGT
        assembly_code = """
            @1000
            A;JGT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000001111101000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @1000
            0;JGT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))
       
        assembly_code = """
            @1000
            -1;JGT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JEQ
        assembly_code = """
            @1000
            A;JEQ
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @1000
            -1;JEQ
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @7
            0;JGE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JGE
        assembly_code = """
            @8
            A;JGE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000001000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @15
            0;JGE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000001111"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @1000
            -1;JGE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))


        # JLT
        assembly_code = """
            @1000
            A;JLT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @1000
            0;JLT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @32
            -1;JLT
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000100000"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JNE
        assembly_code = """
            @1000
            0;JNE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @9
            1;JNE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000001001"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @6
            -1;JNE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JLE
        assembly_code = """
            @6
            A;JLE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000010"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @6
            0;JLE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @6
            -1;JLE
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000000000110"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        # JMP
        assembly_code = """
            @100
            A;JMP
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000001100100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @100
            0;JMP
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000001100100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))

        assembly_code = """
            @100
            -1;JMP
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2)
        expected = "0000000001100100"
        self.assertEqual(expected, lg.get_binary_number(cmp.cpu.program_counter))






        pass
    
    def test_assembly_code_test_sum_1_100_integers(self):
        cmp = lg.hack_computer()

        # 0
        assembly_code = """
                @i
                M=1
                @sum
                M=0
            (LOOP)
                @i
                D=M
                @100
                D=D-A
                @PRE_END
                D;JGT
                @i
                D=M
                @sum
                M=D+M
                @i
                M=M+1
                @LOOP
                0;JMP
            (PRE_END)
                @sum
                D=M
            (END)
                @END
                0;JMP
        """
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 2000)
        self.assertEqual("0001001110111010", lg.get_binary_number(cmp.cpu.d_register))
        pass

    def test_predefined_symbols(self):
        cmp = lg.hack_computer()

        assembly_code = """
            @SP
            M=A
            @LCL
            M=A
            @ARG
            M=A
            @THIS
            M=A
            @THAT
            M=A

            @R0
            M=M+1
            @R1
            M=M+1
            @R2
            M=M+1
            @R3
            M=M+1
            @R4
            M=M+1

            @R5
            M=A
            @R6
            M=A
            @R7
            M=A
            @R8
            M=A
            @R9
            M=A
            @R10
            M=A
            @R11
            M=A
            @R12
            M=A
            @R13
            M=A
            @R14
            M=A
            @R15
            M=A

            @SCREEN
            M=A
            @KBD
            M=A
            




        """

        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 10)
        expected = self.convert_list_ints_to_16_bit_binary([0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(expected, cmp.get_data_memory(0, 16))

        cmp.do_n_operations(False, 32)

        expected = self.convert_list_ints_to_16_bit_binary([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        self.assertEqual(expected, cmp.get_data_memory(0, 16))

        expected = self.convert_list_ints_to_16_bit_binary([0])
        self.assertEqual(expected, cmp.get_data_memory(16384, 16384 + 1))
        
        expected = self.convert_list_ints_to_16_bit_binary([0])
        self.assertEqual(expected, cmp.get_data_memory(24576, 24576 + 1))

        cmp.do_n_operations(False, 4)
        expected = self.convert_list_ints_to_16_bit_binary([16384])
        self.assertEqual(expected, cmp.get_data_memory(16384, 16384 + 1))
        expected = self.convert_list_ints_to_16_bit_binary([24576])
        self.assertEqual(expected, cmp.get_data_memory(24576, 24576 + 1))


        pass

    # Given an array of np array prints them in binary string format
    def show_array_of_np_arrays(self, array):
        for x in array:
            print(lg.get_binary_number(x))

    def int_to_16bit_binary(self, number):
        binary = bin(number & 0xFFFF)[2:]  # Convert to binary and remove '0b' prefix
        padded_binary = binary.zfill(16)   # Zero-pad to ensure 16 bits
        return padded_binary
    
    def convert_list_ints_to_16_bit_binary(self, array):
        ret = []
        for x in array:
            result = self.int_to_16bit_binary(x)
            ret.append(result)

        return ret

    def test_vm_stack_arithmetic(self):
        cmp = lg.hack_computer()

        vm_code = [
            "push constant 7500",
        ]

        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("0001110101001100", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))


        # Add
        vm_code = [
            "push constant 20000",
            "push constant 10000", 
            "add"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("0111010100110000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # Multiply 
        vm_code = [
            "push constant 400",
            "push constant 42", 
            "mult"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("0100000110100000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))


        # Divide
        vm_code = [
            "push constant 12345", 
            "push constant 5", 
            "div",
            "push constant 6", 
            "div",
        ]

        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000110011011", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))


        # Power
        vm_code = [
            "push constant 12345", 
            "push constant 0", 
            "power",
            "push constant 6", 
            "power",
            "push constant 3", 
            "add", 
            "push constant 7", 
            "power", 
        ]

        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)
        self.assertEqual("0100000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))



        vm_code = [
            "push constant 10000",
            "push constant 20000", 
            "add"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("0111010100110000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))


        # Sub 
        vm_code = [
            "push constant 10000",
            "push constant 20000", 
            "sub"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("1101100011110000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))


        vm_code = [
            "push constant 20000",
            "push constant 10000", 
            "sub"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("0010011100010000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # Neg
        vm_code = [
            "push constant 12345",
            "neg"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("1100111111000111", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # EQ
        vm_code = [
            "push constant 12345",
            "push constant 12344",
            "eq"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 12345",
            "push constant 12346",
            "eq"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 12345",
            "push constant 12345",
            "eq"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("1111111111111111", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # GT
        vm_code = [
            "push constant 8008",
            "push constant 420",
            "gt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 30)
        self.assertEqual("1111111111111111", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 8008",
            "push constant 11210",
            "gt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 8008",
            "push constant 8008",
            "gt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # LT
        vm_code = [
            "push constant 8008",
            "push constant 8008",
            "lt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 8009",
            "push constant 8008",
            "lt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        vm_code = [
            "push constant 8007",
            "push constant 8008",
            "lt"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 50)
        self.assertEqual("1111111111111111", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # AND
        vm_code = [
            "push constant 0",
            "push constant 1",
            "neg",
            "and"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)
        self.assertEqual("0000000000000000", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # OR 
        vm_code = [
            "push constant 0",
            "push constant 1",
            "neg",
            "or"     
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)
        self.assertEqual("1111111111111111", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # NOT
        vm_code = [
            "push constant 6372", 
            "not"
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)
        self.assertEqual("1110011100011011", lg.get_binary_number(cmp.data_memory[256]))
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(257)), lg.get_binary_number(cmp.data_memory[0]))

        # Pushing 10 items
        vm_code = [
            "push constant 0", 
            "push constant 1",
            "push constant 2",
            "push constant 3",
            "push constant 4",
            "push constant 5",
            "push constant 6",
            "push constant 7",
            "push constant 8",
            "push constant 9",
            "push constant 10",
        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)
        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(267)), lg.get_binary_number(cmp.data_memory[0]))



        pass

    def test_vm_lcl_arg_this_that_memory_segment_push_pop(self):
        cmp = lg.hack_computer()

        
        vm_code = [
            "push constant 1", 
            "pop local 0", 

            "push local 0",
            "push constant 1", 
            "add", 
            "pop argument 1",

            "push argument 1", 
            "push constant 2", 
            "add", 
            "pop this 2", 

            "push this 2", 
            "push constant 3", 
            "add", 
            "pop that 4",

            "push that 4", 
            "push that 4", 
            "add", 
            "pop that 5"




        ]
        # Setting the LCL, ARG, THIS, THAT to specefic values so we can actually test if push <memory segment> is working as intended
        cmp.data_memory[1] = assem.convert_int_to_np_array(8000)    # LCL
        cmp.data_memory[2] = assem.convert_int_to_np_array(9000)    # ARG   
        cmp.data_memory[3] = assem.convert_int_to_np_array(10000)   # THIS
        cmp.data_memory[4] = assem.convert_int_to_np_array(11000)   # THAT

        






        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 200)
        
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([1]), cmp.get_data_memory(8000, 8001))
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 2]), cmp.get_data_memory(9000, 9002))
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 0, 4]), cmp.get_data_memory(10000, 10003))

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 0, 0, 0, 7, 14]), cmp.get_data_memory(11000, 11006))

        self.assertEqual(lg.get_binary_number(assem.convert_int_to_np_array(256)), lg.get_binary_number(cmp.data_memory[0]))


        pass

    def test_vm_pointer_and_temp_push_pop(self):
        cmp = lg.hack_computer()

        # Split into two the first is manipulating temp 
        # The second is manipulating pointer
        vm_code = [
            "push constant 16", 
            "pop temp 0", 
            "push temp 0", 
            "push temp 0",
            "add",
            "pop temp 1", 
            "push temp 1", 
            "push temp 1",
            "add",
            "pop temp 2", 
            "push temp 2", 
            "push temp 2",
            "add",
            "pop temp 3", 
            "push temp 3", 
            "push temp 3",
            "add",
            "pop temp 4", 

            "push constant 2048", 
            "pop pointer 0", 
            "push constant 2049",
            "pop pointer 1", 

            


        ]
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 250)
        
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([16, 32, 64, 128, 256]), cmp.get_data_memory(5, 10))
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([2048, 2049]), cmp.get_data_memory(3, 5))
    

    def test_vm_static_push_pop(self):
        cmp = lg.hack_computer()

        vm_code = [
            "push constant 15", 
            "pop static 0", 
            "push static 0", 
            "push static 0", 
            "add", 

            "pop static 1", 
            "push static 1", 
            "push static 1", 
            "add", 

            "pop static 2", 
            "push static 2", 
            "push static 2", 
            "add", 

            "pop static 3", 
            "push static 3", 
            "push static 3", 
            "add", 

            "pop static 10", 
            "push static 10", 
            "push static 10", 
            "add",

            "pop static 9" 
        ]


        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 500)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([15, 30, 60, 120, 0, 0, 0, 0, 0, 480, 240]), cmp.get_data_memory(16, 27))


        pass

    def test_label_goto_ifgoto_program_flow_commands_vm(self):
        cmp = lg.hack_computer()

        # Program which adds 1, n - 1 the numbers
        VM_CODE = [
            "push constant 101", 
            "pop static 0",

            "push constant 1", 
            "pop static 1",

            "push constant 0",
            "pop static 2",

            "label loop", 

            "push static 2", 
            "push static 1", 
            "add", 
            "pop static 2",


            "push static 1", 
            "push constant 1",
            "add", 
            "pop static 1",

            "push static 1", 
            "push static 0",
            "lt", 
            "if-goto loop"
        ]
        assembly_code = vm.convert_VM_code_to_assembly(VM_CODE)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))

        cmp.do_n_operations(False, 9000)
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([101, 101, 5050]), cmp.get_data_memory(16, 19))

    def test_vm_function_calling_commands(self):
        cmp = lg.hack_computer()
        VM_CODE = [
            "push constant 2",
            "push constant 5",
            "call mult 2",
            "push constant 5", 
            "call mult 2",
            "push constant 5", 
            "call mult 2",
            "push constant 5", 
            "call mult 2",
            "push constant 5", 
            "call mult 2",
            "push constant 5", 
            "call mult 2",
            


            "label bruh", 
            "goto bruh",

            "function mult 2", 
            "push constant 0",
            "pop local 0", 
            "push argument 1", 
            "pop local 1", 
            "label loop", 
            "push constant 0", 
            "push local 1", 
            "eq", 
            "if-goto end", 
            "push local 0", 
            "push argument 0", 
            "add", 
            "pop local 0", 
            "push local 1", 
            "push constant 1", 
            "sub", 
            "pop local 1", 
            "goto loop", 
            "label end", 
            "push local 0",
            "return",

            
        ]

        assembly_code = vm.convert_VM_code_to_assembly(VM_CODE)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 5000)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([31250]), cmp.get_data_memory(256, 257))
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([257]), cmp.get_data_memory(0, 1))

        VM_CODE = [
            "push constant 4",
            "push constant 4",
            "call pow 2",
            


            "label bruh", 
            "goto bruh",

            "function mult 2", 
            "push constant 0",
            "pop local 0", 
            "push argument 1", 
            "pop local 1", 
            "label loop", 
            "push constant 0", 
            "push local 1", 
            "eq", 
            "if-goto end", 
            "push local 0", 
            "push argument 0", 
            "add", 
            "pop local 0", 
            "push local 1", 
            "push constant 1", 
            "sub", 
            "pop local 1", 
            "goto loop", 
            "label end", 
            "push local 0",
            "return",

            "function pow 2", 
            "push argument 0", 
            "push argument 1", 
            "call mult 2",
            "push argument 1",
            "call mult 2",
            "push argument 1",
            "call mult 2",
            "push argument 1",
            "call mult 2",
            "push argument 1",
            "call mult 2",
            "push argument 1", 
            "call mult 2",


            "return",

            
        ]

        assembly_code = vm.convert_VM_code_to_assembly(VM_CODE)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 6000)
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([16384]), cmp.get_data_memory(256, 257))
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([257]), cmp.get_data_memory(0, 1))


    """
    
        Jack coding tests

    """
    def test_let_statement(self):
        cmp = lg.hack_computer()
        code = """
            class bruh {
                static int ram, ll;
                function void d() {
                    let ram = 0;
                    let ram[8000] = 69;
                    let ram[8001] = 420;
                    let ram[8002] = 911;
                    let ram[8003] = 8008;
                    let ram[8004] = 5321;
                    let ram[8005] = 12345;
                    let ram[8006] = 30000;
                    let ram[8007] = 9009;
                    let ram[8008] = 211;
                    let ram[8009] = 1;
                }
            }

        """

        vm_code = sa.generate_vm_code(code)
        
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 600)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([69, 420, 911, 8008, 5321, 12345, 30000, 9009, 211, 1]), cmp.get_data_memory(8000, 8010))


        code = """
            class bruh {
                static int ram, ll, love, you, so;
                function void d() {
                    let ram = 99;
                    let ll = 100;
                    let love = 101;
                    let you = 102;
                    let so = 103;
                }
                    
            }

        """

        vm_code = sa.generate_vm_code(code)
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 100)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([99, 100, 101, 102, 103]), cmp.get_data_memory(16, 21))



        pass

    def test_expression(self):
        cmp = lg.hack_computer()
        code = """
            class bruh {
                static int ram, integer_constant_, kc1, kc2, kc3, array, varname_ident, unary_term, complex_computation, not_computation;
                function void d() {
                    let ram = 0;
                    let integer_constant_ = 230;
                    let kc1 = true;
                    let kc2 = false;
                    let kc3 = null;

                    let array = ram[17] + 2;
                    let varname_ident = kc1 + integer_constant_;
                    let unary_term = -kc1 + -1;
                    let complex_computation = (3 - 2) + 1 + 5;
                    let not_computation = !(true & false);

                }
            }

        """

        vm_code = sa.generate_vm_code(code)
        
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 1000)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 230, 131071, 0, 0, 232, 229, 0, 7, 131071]), cmp.get_data_memory(16, 26))


    def test_if_statement(self):
        cmp = lg.hack_computer()
        code = """
            class bruh {
                static int ram;
                function void d() {
                    let ram = 2008;
                    
                    if (true) {
                        let ram[0] = 15;
                    } else {
                        let ram[0] = 100;
                    }

                    if (false) {
                        let ram[1] = 69; 
                    } else {
                        let ram[1] = 96;
                    }

                    if (8181 = 8181) {
                        let ram[2] = 90;
                    } else {
                        let ram[2] = 91;
                    }

                    if (8 < 9){
                        let ram[4] = 9999;
                    }

                    if (8182 < 90) {
                        let ram[3] = 99;
                    } else {
                        let ram[3] = 999;
                    }

                    
                }
            }

        """

        vm_code = sa.generate_vm_code(code)       
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 600)



        self.assertEqual(self.convert_list_ints_to_16_bit_binary([15, 96, 90, 999, 9999]), cmp.get_data_memory(2008, 2013))

    def test_while_statement(self):
        cmp = lg.hack_computer()
        code = """
            class bruh {
                static int ram, s, i;
                function void d() {
                    let s = 0;
                    let i = 0;

                    while (i < 101) {
                        let s = s + i;
                        let i = i + 1;

                    }
                }
            }

        """    

        vm_code = sa.generate_vm_code(code)       
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 9500)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([5050]), cmp.get_data_memory(17, 18))

    def test_local_variables(self):
        cmp = lg.hack_computer()
        code = """
            class Main {
                static int ram, ram1, ram2;
                function void main () {
                    do Main.d();
                    return 0;
                }
                function void d() {
                    var int i, j, z;
                    let i = 30;
                    let i = i+i+i+i+i+i+i+i+i+i;
                    let i = i+i+i+i+i+i+i+i+i+i;

                    let j = i + -3000 + 6;

                    let z = i + j;

                    let ram = i;
                    let ram1 = j;
                    let ram2 = z;
                    return 0;
                }
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)        
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 800)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([3000, 6, 3006]), cmp.get_data_memory(16, 19))

    def test_function_calling(self):
        # Non recursive function 
        cmp = lg.hack_computer()
        code = """
            class Main {
                static int ram, ram1, ram2;
                function void main() {
                    let ram = Main.d(2);
                    let ram1 = Main.d(20);
                    let ram2 = Main.d(6912);

                    return 0;
                }
                function void d(int x) {
                    return x + x;
                }
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)        
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 800)
    
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([4, 40, 13824]), cmp.get_data_memory(16, 19))

        # Recursive function 
        code = """
            class Main {
                static int ram, ram1, ram2;
                function void main () {
                    let ram = Main.multiply(5, 2);
                    let ram1 = Main.multiply(30, 1);
                    let ram2 = Main.multiply(Main.multiply(3, 2), Main.multiply(5, 1));
                    

                    return 0;
                }
                function void multiply(int x, int y) {
                    if (y = 0) {
                        return 0;
                    }
                    return x + Main.multiply(x, y - 1);
                }
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)        
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 3000)

        self.assertEqual(self.convert_list_ints_to_16_bit_binary([10, 30, 30]), cmp.get_data_memory(16, 19))

    def test_math_libary(self):
        # Testing multiplication
        cmp = lg.hack_computer()
        code = """
            class Main {
                static int ram, ram1, ram2, ram3;
                function void main() {
                    let ram = 100*0;
                    let ram1 = 3*6;
                    let ram2 = 7500 * 4;
                    let ram3 = (7500*-1) + 7500;

                    return 0;
                }
                
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)      
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 300)
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 18, 30000, 0]), cmp.get_data_memory(16, 20))

        # Testing division 
        code = """
            class Main {
                static int ram, ram1, ram2, ram3;
                function void main() {
                    let ram = 0/2;
                    let ram1 = 18/3;
                    let ram2 = 7500/4;
                    let ram3 = -(16/8) + 2;

                    return 0;
                }
                
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)      
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 300)
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([0, 6, 1875, 0]), cmp.get_data_memory(16, 20))

        # Testing power 
        code = """
            class Main {
                static int ram, ram1, ram2, ram3;
                function void main() {
                    let ram = 91^ 0;
                    let ram1 = 1 ^1;
                    let ram2 = 3^3;
                    let ram3 = 9^4;
                    return 0;
                }
            }

        """

        vm_code = sa.generate_vm_code_with_bootstrap(code)      
        assembly_code = vm.convert_VM_code_to_assembly(vm_code)
        cmp.load_program(assem.get_binary_from_hack_assembly(assembly_code))
        cmp.do_n_operations(False, 300)
        self.assertEqual(self.convert_list_ints_to_16_bit_binary([1, 1, 27, 6561]), cmp.get_data_memory(16, 20))



if __name__ == '__main__':
    unittest.main()


