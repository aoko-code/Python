import bits
import bitmask

print(bits.NOT(0b0101))
print(bin(bits.NOT(0b0101)))
print(bin(bits.NOT(0b0101) & 0xF))
print(bin(bits.AND(0b0101, 0b0011) & 0xF)) 
print(bin(bits.AND(0b0101, 0b0100) & 0xF))
print(bin(bits.OR(0b0101, 0b0100) & 0xF))
print(bin(bits.OR(0b0101, 0b0011) & 0xF))
print(bin(bits.XOR(0b0101, 0b11) & 0xF))

bml = bitmask.BitMask()
print(bml)
print(bin(bml.NOT() & 0xf))