#!/usr/bin/env python3

"""
CTF Problem (Modified padding oracle attack):
  I have another secret service for you.
  This time it does FREE AES-128-CBC DECRYPTION!
  However, I heard that the PKSC#7 padding scheme is prone to attacks.
  So I decided to implement my own padding scheme instead.

  For example, instead of ...\x04\x04\x04\x04, the padding looks like this ...\x01\x02\x03\x04.
  Or, instead of ...\x06\x06\x06\x06\x06\x06, I have ...\x01\x02\x03\x04\x05\x06.

  DOES NOT TAKE INTO ACCOUNT MULTIPLE MATCHES PER ITERATION!!!
"""

from requests import post
from binascii import hexlify, unhexlify

hex_values = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')


def xor(x, y):
    return bytes([x[i] ^ y[i] for i in range(len(x))])


def get_hex_pad(i):
    out = ""
    for j in range(len(i)//2):
        i_byte = unhexlify(i[2*j:2*j+2])
        out += xor(i_byte, (j+2).to_bytes(1, 'big')).hex()
    return out


def main():
    cipher = "b12c3f6a001ab28eb3dafbfa2d634dc20419370e98feeedfdb2d679bddf49f3047525527b5dbf890ae7bb8edcbc33b82b652a8d4b7d6dedb343b605e0d340d48ac0b5f7190fe1bc7156962f88367d098c60e7e1815dbc964a5784a7f908142bb3c5f80f9917b982de84f6da930d6fe85"
    plaintext = ""
    
    block_size = 16
    url = "http://cs2107-ctfd-i.comp.nus.edu.sg:4004/"
    
    for k in reversed(range(len(cipher) // (block_size * 2) - 1)):
        c0 = cipher[(block_size * 2)*k:(block_size * 2)*(k+1)]
        c1 = cipher[(block_size * 2)*(k+1):(block_size * 2)*(k+2)]
        intermediate = ""

        print(f"Block number {k}")
        for j in range(len(c0)//2):
            has_match = False
            for x in hex_values:
                if not has_match:
                    for y in hex_values:
                        test_cipher = c0[:32-2*(j+1)] + x + y + get_hex_pad(intermediate) + c1
                        output = post(url, data = {'data': test_cipher})
                        if "Successful!" in output.text:  # html contains "Successful!" if the cipher is valid
                            byte = bytes.fromhex(x + y)
                            intermediate_byte = xor(byte, bytes.fromhex('01'))
                            intermediate = intermediate_byte.hex() + intermediate
                            letter = xor(intermediate_byte, bytes.fromhex(c0[30-2*j:32-2*j]))  # xor with original byte from previous block
                            has_match = True
                            # print(f"\tintermediate_byte: {intermediate_byte.hex()}\tletter: {letter}")  # Debugging purposes
                            plaintext = letter.hex() + plaintext
                            break
            if not has_match:
                print("INCOMPLETE!")
                print(intermediate)
                return
    print(f"hex: {plaintext}")
    print(bytes.fromhex(plaintext).decode("ASCII"))


if __name__ == "__main__":
    main()
