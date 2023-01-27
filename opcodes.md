# Memory Adress
An 8

# Registers
A number in the range of 0-7 with the prefix 'R'.
Example: `R7`

# Opcodes

## LD (Load)

| EXAMPLE         | OPCODE | REGISTER_ADDRESS         | DATA H | DATA L                   |
| --------------- | ------ | ------------------------ | ------ | ------------------------ |
| LD R1, 0xabcd   | 0x0000 | [A register](#registers) | 0xAB   | 0xCD                     |
| LD R1, R2       | 0x0001 | [A register](#registers) | 0x00   | [A register](#registers) |
| LD R1, $0xABCD  | 0x0002 | [A register](#registers) | 0xAB   | 0xCD                     |
| ST R1, $0xABCD  | 0x0010 | [A register](#registers) | 0xAB   | 0xCD                     |
| STL R1, $0xABCD | 0x0011 | [A register](#registers) | 0xAB   | 0xCD                     |
| STH R1, $0xABCD | 0x0012 | [A register](#registers) | 0xAB   | 0xCD                     |
| ST R1, R2       | 0x0013 | [A register](#registers) | 0x00   | [A register](#registers) |
| STL R1, R2      | 0x0014 | [A register](#registers) | 0x00   | [A register](#registers) |
| STH R1, R2      | 0x0015 | [A register](#registers) | 0x00   | [A register](#registers) |
| CMP R1, R2      | 0x0020 | [A register](#registers) | 0x00   | [A register](#registers) |
| CMP R1, 0xabcd  | 0x0021 | [A register](#registers) | 0xAB   | 0xCD                     |
| JEQ label       | 0x0030 | 0x00                     | 0xAB   | 0xCD                     |
| JGT label       | 0x0031 | 0x00                     | 0xAB   | 0xCD                     |
| JLT label       | 0x0032 | 0x00                     | 0xAB   | 0xCD                     |
| JMP label       | 0x0033 | 0x00                     | 0xAB   | 0xCD                     |
| ADD R1, 0xabcd  | 0x0040 | [A register](#registers) | 0xAB   | 0xCD                     |
| SUB R1, 0xabcd  | 0x0041 | [A register](#registers) | 0xAB   | 0xCD                     |
| ADD R1, R2      | 0x0042 | [A register](#registers) | 0x00   | [A register](#registers) |
| SUB R1, R2      | 0x0043 | [A register](#registers) | 0x00   | [A register](#registers) |
| HALT            | 0xFFFE | 0xFF                     | 0xFF   | 0xFF                     |
| NOOP            | 0xFFFF | 0xFF                     | 0xFF   | 0xFF                     |