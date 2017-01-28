#!/usr/bin/python3
import challenge4

pt = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"
ct_actual = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

pt_bytes = challenge4.string2bytes(pt)
pt_hex = challenge4.bytes2hex(pt_bytes)

ct_bytes = challenge4.repeating_char_xor(pt_bytes, challenge4.string2bytes(key))
ct_hex = challenge4.bytes2hex(ct_bytes)
ct = challenge4.bytes2string(ct_bytes)

print("Plaintext (chars) is:\n{}\n".format(pt))
print("Plaintext (bytes) is:\n{}\n".format(pt_bytes))
print("Plaintext (hex) is:\n{}\n".format(pt_hex))

print("Ciphertext (chars) is:\n{}\n".format(ct))
print("Ciphertext (bytes) is:\n{}\n".format(ct_bytes))
print("Ciphertext (hex) is:\n{}\n".format(ct_hex))

print("Ciphertext (hex) should be:\n{}\n".format(ct_actual))
print("Ciphertext is correct: {}".format(ct_actual == ct_hex))
