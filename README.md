# My CPU

## Data

### Memory Adress
An 16 bit address for a location in memory. This uses the the "data" area of an [instruction](#instructions)

### Registers
General purpose registers addresses are a number in the range of 0-7 with the prefix 'R'. This is in 8 bits.

Example: `R7`

Result: 00000111 (0x07)

## Instructions

An instruction is made up of a 16 bit opcode and has two paramaters.

* Paramater one (P1)
    An 8 bit data format normaly used for a register address.

* Paramater two (P2)
    A 16 bit data format normally split into an upper byte (P2 U) and a lower byte (P2 L).


You may use the [assembler](asm.py) to assemble a program for the CPU.

### Load a value into a register

Example: LD R1, 0xabcd

Result:
| Opcode   | P1     | P2 U   | P2 L   |
| -------- | ------ | ------ | ------ |
| `0x0000` | `0x01` | `0xab` | `0xcd` |

Combined Result: `0x000001abcd`

### Load the value of a register into another register

Example: LD R1, R2

Result:
| Opcode   | P1     | P2 U   | P2 L   |
| -------- | ------ | ------ | ------ |
| `0x0001` | `0x01` | `0x00` | `0x02` |

Combined Result: `0x0001010002`

### Load the value from memory into a register

Example: LD R1, $0xABCD

Result:
| Opcode   | P1     | P2 U   | P2 L   |
| -------- | ------ | ------ | ------ |
| `0x0002` | `0x01` | `0xab` | `0xcd` |

Combined Result: `0x000201abcd`













## A simplified table for all instructions.

| EXAMPLE         | OPCODE | P1                       | P2 U | P2 L                     |
| --------------- | ------ | ------------------------ | ---- | ------------------------ |
| LD R1, 0xabcd   | 0x0000 | [A register](#registers) | 0xAB | 0xCD                     |
| LD R1, R2       | 0x0001 | [A register](#registers) | 0x00 | [A register](#registers) |
| LD R1, $0xABCD  | 0x0002 | [A register](#registers) | 0xAB | 0xCD                     |
| ST R1, $0xABCD  | 0x0010 | [A register](#registers) | 0xAB | 0xCD                     |
| STL R1, $0xABCD | 0x0011 | [A register](#registers) | 0xAB | 0xCD                     |
| STH R1, $0xABCD | 0x0012 | [A register](#registers) | 0xAB | 0xCD                     |
| ST R1, R2       | 0x0013 | [A register](#registers) | 0x00 | [A register](#registers) |
| STL R1, R2      | 0x0014 | [A register](#registers) | 0x00 | [A register](#registers) |
| STH R1, R2      | 0x0015 | [A register](#registers) | 0x00 | [A register](#registers) |
| CMP R1, R2      | 0x0020 | [A register](#registers) | 0x00 | [A register](#registers) |
| CMP R1, 0xabcd  | 0x0021 | [A register](#registers) | 0xAB | 0xCD                     |
| JEQ label       | 0x0030 | 0x00                     | 0xAB | 0xCD                     |
| JGT label       | 0x0031 | 0x00                     | 0xAB | 0xCD                     |
| JLT label       | 0x0032 | 0x00                     | 0xAB | 0xCD                     |
| JMP label       | 0x0033 | 0x00                     | 0xAB | 0xCD                     |
| ADD R1, 0xabcd  | 0x0040 | [A register](#registers) | 0xAB | 0xCD                     |
| SUB R1, 0xabcd  | 0x0041 | [A register](#registers) | 0xAB | 0xCD                     |
| ADD R1, R2      | 0x0042 | [A register](#registers) | 0x00 | [A register](#registers) |
| SUB R1, R2      | 0x0043 | [A register](#registers) | 0x00 | [A register](#registers) |
| HALT            | 0xFFFE | 0xFF                     | 0xFF | 0xFF                     |
| NOOP            | 0xFFFF | 0xFF                     | 0xFF | 0xFF                     |
