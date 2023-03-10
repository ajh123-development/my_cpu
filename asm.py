import sys
import re

labels = {}

def parselabels(fn):
	linenum = 0
	with open(sys.argv[1]) as f:
		for line in f:
			line = line.replace('\n', '').replace('\r', '')
			print(line)
			if line[0]=='#':
				# Note that linenum won't be increased, so the address
				# remains correct
				continue

			if line[0]=='.':
				labels[line[1:]] = linenum
				print("Label: " + line[1:] + " @ " + format(linenum, '#04x'))
			else:
				linenum = linenum + 1

def zerobin(fn):
	with open("rom.bin", "wb") as binary_file:
		binary_file.close()

def writebin(fn, b):
	with open("rom.bin", "ab") as binary_file:
        	binary_file.write(bytearray(b))

if len(sys.argv) != 2:
	print("Usage: asm.py file.asm")
	sys.exit()

zerobin("rom.bin")

parselabels(sys.argv[1])

with open(sys.argv[1]) as f:
	for line in f:

		# Ignore labels
		if line[0]=='.':
			continue

		# Ignore comments
		if line[0]=='#':
			continue

		line = line.replace('\n', '').replace('\r', '')
		tok = re.split(r'[, ]',line)

		if '' in tok:
			tok.remove('')
		
		if tok[0].upper() == "LD":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == '$':
					# Address
					addr = int(a1[1:], 0)
					b = [0x00, 0x02, r, addr >> 8, addr & 0xFF]
					writebin("rom.bin", b)
				elif a1[0] == 'R':
					# Register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x01, r, 0, r2]
					writebin("rom.bin", b)
				else:
					# Value
					v = int(a1, 0)
					b = [0x00, 0x00, r, v >> 8,  v & 0xFF]
					writebin("rom.bin", b)
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "ST":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == '$':
					# Address
					addr = int(a1[1:], 0)
					b = [0x00, 0x10, r, addr >> 8, addr & 0xFF]
					writebin("rom.bin", b)
				elif a1[0] == 'R':
					# Address in register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x13, r, 0, r2]
					writebin("rom.bin", b)
				else:
					print("Invalid mode")
					print(line)
					sys.exit()
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "STL":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == '$':
					# Address
					addr = int(a1[1:], 0)
					b = [0x00, 0x11, r, addr >> 8, addr & 0xFF]
					writebin("rom.bin", b)
				elif a1[0] == 'R':
					# Address in register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x14, r, 0, r2]
					writebin("rom.bin", b)
				else:
					print("Invalid mode")
					print(line)
					sys.exit()
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "STH":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == '$':
					# Address
					addr = int(a1[1:], 0)
					b = [0x00, 0x12, r, addr >> 8, addr & 0xFF]
					writebin("rom.bin", b)
				elif a1[0] == 'R':
					# Address in register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x14, r, 0, r2]
					writebin("rom.bin", b)
				else:
					print("Invalid mode")
					print(line)
					sys.exit()
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "CMP":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == 'R':
					# Register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x20, r, 0, r2]
					writebin("rom.bin", b)
				else:
					# Value
					v = int(a1, 0)
					b = [0x00, 0x21, r, v >> 8,  v & 0xFF]
					writebin("rom.bin", b)
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "JEQ":
			if tok[1] in labels:
				addr = labels[tok[1]]
				v = addr
				b = [0x00, 0x30, 0, v >> 8,  v & 0xFF]
				writebin("rom.bin", b)
			else:
				print("Unknown label")
				print(tok[1])
				sys.exit()
		elif tok[0].upper() == "JGT":
			if tok[1] in labels:
				addr = labels[tok[1]]
				v = addr
				b = [0x00, 0x31, 0, v >> 8,  v & 0xFF]
				writebin("rom.bin", b)
			else:
				print("Unknown label")
				print(tok[1])
				sys.exit()
		elif tok[0].upper() == "JLT":
			if tok[1] in labels:
				addr = labels[tok[1]]
				v = addr
				b = [0x00, 0x32, 0, v >> 8,  v & 0xFF]
				writebin("rom.bin", b)
			else:
				print("Unknown label")
				print(tok[1])
				sys.exit()
		elif tok[0].upper() == "JMP":
			if tok[1] in labels:
				addr = labels[tok[1]]
				v = addr
				b = [0x00, 0x33, 0, v >> 8,  v & 0xFF]
				writebin("rom.bin", b)
			else:
				print("Unknown label")
				print(tok[1])
				sys.exit()
		elif tok[0].upper() == "ADD":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == 'R':
					# Register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x42, r, 0, r2]
					writebin("rom.bin", b)
				else:
					# Value
					v = int(a1, 0)
					b = [0x00, 0x40, r, v >> 8,  v & 0xFF]
					writebin("rom.bin", b)
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "SUB":
			r = int(tok[1].upper()[1])
			if r >= 0 and r <= 7:
				a1 = tok[2]
				if a1[0] == 'R':
					# Register
					r2 = int(a1[1:], 0)
					b = [0x00, 0x43, r, 0, r2]
					writebin("rom.bin", b)
				else:
					# Value
					v = int(a1, 0)
					b = [0x00, 0x41, r, v >> 8,  v & 0xFF]
					writebin("rom.bin", b)
			else:
				print("Invalid register name")
				print(tok[1].upper())
				sys.exit()
		elif tok[0].upper() == "HALT":
				b = [0xFF, 0xFE, 0xFF, 0xFF, 0xFF]
				writebin("rom.bin", b)
		elif tok[0].upper() == "NOOP":
				b = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
				writebin("rom.bin", b)
		else:
			print("Unknown operand")
			print(tok[0])
			sys.exit()
