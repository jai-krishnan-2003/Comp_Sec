P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]
 
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC2 = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
]
 
Perm1 = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
 
Perm_opp = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
 
Expansion = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
 
S_boxes = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
 
next_move = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def xor(a, b):
    return [x ^ y for x, y in zip(a, b)]

def left_rotate(bits, shift):
    return bits[shift:] + bits[:shift]
 
def calculate(block, table):
    return [block[i-1] for i in table]
 
def str_to_bit(s):
    return [int(bit) for bit in s]
 
def bits_to_string(bits):
    return ''.join(map(str, bits))
 
def generate_subkeys(key):
    def debug(message, value):
        print(f"{message}: {bits_to_string(value)}")
    
    debug("Given Key", key)
    key1 = calculate(key, PC1)
    debug("After applying PC1 to get 56 bits", key1)
    
    half1, half2 = key1[:28], key1[28:]
    debug("1st half", half1)
    debug("2nd half", half2)
    
    subkeys = []
    for i, shift in enumerate(next_move, start=1):
        half1, half2 = left_rotate(half1, shift), left_rotate(half2, shift)
        debug(f"half 1 - {i}", half1)
        debug(f"half 2 - {i}", half2)
        
        subkey = calculate(half1 + half2, PC2)
        subkeys.append(subkey)
        debug(f"Key {i}", subkey)
    
    return subkeys

def s_box_substitution(expanded_block):
    output = []
    
    print("  S-Box Substitution:")
    
    for i in range(8):
        block = expanded_block[i*6:(i+1)*6]
        
        row = (block[0] << 1) + block[5]
        col = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
        
        value = S_boxes[i][row][col]
        
        bits = [(value >> j) & 1 for j in range(3, -1, -1)]
        output.extend(bits)
        
        print(f"    S{i+1}: Input={bits_to_string(block)}, Row={row}, Col={col}, Output={bits_to_string(bits)}")
    
    return output
 
def f_function(R, subkey):
    def debug(message, value):
         print(f"{message}: {bits_to_string(value)}")

    debug("Below is the f-function calculations", "")
    expanded_R = calculate(R, Expansion)
    debug("Expanded R", expanded_R)

    xored = xor(expanded_R, subkey)
    debug("XOR with subkey", xored)

    substituted = s_box_substitution(xored)
    debug("After S-Box substitution", substituted)

    calculated = calculate(substituted, P)
    debug("After permutation", calculated)

    return calculated


def des_decrypt(ciphertext, key):
    def debug(message, value=""):
        print(f"{message}: {bits_to_string(value)}" if value else message)
    
    block = calculate(ciphertext, Perm1)
    debug("DES DECRYPT")
    debug("Initial Permuted Block", block)
    
    L, R = block[:32], block[32:]
    debug("L0", L)
    debug("R0", R)
    
    subkeys = generate_subkeys(key)
    
    for i in reversed(range(16)):
        debug(f"\nUsing Key {i+1}")
        old_L, L = L, R
        R = xor(old_L, f_function(R, subkeys[i]))
        debug(f"L{16-i}", L)
        debug(f"R{16-i}", R)
    
    combined = R + L
    debug("After 16 Rounds (R16 + L16)", combined)
    
    plaintext = calculate(combined, Perm_opp)
    debug("Final Result", plaintext)
    
    return plaintext


def main():
    ciphertext = str_to_bit("1100101011101101101000100110010101011111101101110011100001110011")
    key = str_to_bit("0100110001001111010101100100010101000011010100110100111001000100")
    
    plaintext = des_decrypt(ciphertext, key)
    plaintext_str = bits_to_string(plaintext)
    
    print("Ciphertext:", bits_to_string(ciphertext))
    print("Key:", bits_to_string(key))
    print("Decrypted text in binary:", plaintext_str)
    
    if all(c in '01' for c in plaintext_str) and len(plaintext_str) % 8 == 0:
        ascii_text = ''.join(chr(int(plaintext_str[i:i+8], 2)) for i in range(0, len(plaintext_str), 8))
        print("Decrypted text in letters:", ascii_text)
    else:
        print("Decrypted text cannot be converted to letters")
    
if __name__ == "__main__":
    main()
