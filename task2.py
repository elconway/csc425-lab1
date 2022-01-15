from Crypto.Util import Counter
from Crypto.Cipher import AES, ARC4

aes_key = bytes(b'\xFF') * 16
aes_iv = bytes(b'\xFF') * 16
ctr_counter = Counter.new(128)
data = "ABCDEFGHIJKLMNOPABCDEFGHIJKLMNOP"


ecb_cipher = AES.new(aes_key, AES.MODE_ECB)
cbc_cipher = AES.new(aes_key, AES.MODE_CBC, aes_iv)
cfb_cipher = AES.new(aes_key, AES.MODE_CFB, aes_iv)
ofb_cipher = AES.new(aes_key, AES.MODE_OFB, aes_iv)
ctr_cipher = AES.new(aes_key, AES.MODE_CTR, counter=ctr_counter)

ecb_encrypted_data = ecb_cipher.encrypt(data)
cbc_encrypted_data = cbc_cipher.encrypt(data)
cfb_encrypted_data = cfb_cipher.encrypt(data)
ofb_encrypted_data = ofb_cipher.encrypt(data)
ctr_encrypted_data = ctr_cipher.encrypt(data)

def bytes_to_bits(b):
	return bin(int(b.hex(), base=16))

print("ENCRYPTED:")
print("----------------HEX----------------")
print("ECB (1 / 2):", ecb_encrypted_data.hex()[:32])
print("ECB (2 / 2):", ecb_encrypted_data.hex()[32:])
print("CBC (1 / 2):", cbc_encrypted_data.hex()[:32])
print("CBC (2 / 2):", cbc_encrypted_data.hex()[32:])
print("CFB (1 / 2):", cfb_encrypted_data.hex()[:32])
print("CFB (2 / 2):", cfb_encrypted_data.hex()[32:])
print("OFB (1 / 2):", ofb_encrypted_data.hex()[:32])
print("OFB (2 / 2):", ofb_encrypted_data.hex()[32:])
print("CTR (1 / 2):", ctr_encrypted_data.hex()[:32])
print("CTR (2 / 2):", ctr_encrypted_data.hex()[32:])


print("\n----------------BIN----------------")
print("ECB (1 / 2):", bytes_to_bits(ecb_encrypted_data)[2:130])
print("ECB (2 / 2):", bytes_to_bits(ecb_encrypted_data)[130:])

print("CBC (1 / 2):", bytes_to_bits(cbc_encrypted_data)[2:130])
print("CBC (2 / 2):", bytes_to_bits(cbc_encrypted_data)[130:])

print("CFB (1 / 2):", bytes_to_bits(cfb_encrypted_data)[2:130])
print("CFB (2 / 2):", bytes_to_bits(cfb_encrypted_data)[130:])

print("OFB (1 / 2):", bytes_to_bits(ofb_encrypted_data)[2:130])
print("OFB (2 / 2):", bytes_to_bits(ofb_encrypted_data)[130:])

print("CTR (1 / 2):", bytes_to_bits(ctr_encrypted_data)[2:130])
print("CTR (2 / 2):", bytes_to_bits(ctr_encrypted_data)[130:])


def flip_first_bit(encrypted_data):
	return bytes.fromhex(hex(encrypted_data[0] ^ 128)[2:].upper()) + encrypted_data[1:]

print("\n--------------------------------------------------------------------------------------------------------------------------------\n")

print("DECRYPTED (with flipped bit in encrypted data)")
print("ECB:", ecb_cipher.decrypt(flip_first_bit(ecb_encrypted_data)))
print("CBC:", cbc_cipher.decrypt(flip_first_bit(cbc_encrypted_data)))
print("CFB:", cfb_cipher.decrypt(flip_first_bit(cfb_encrypted_data)))
print("OFB:", ofb_cipher.decrypt(flip_first_bit(ofb_encrypted_data)))
print("CTR:", ctr_cipher.decrypt(flip_first_bit(ctr_encrypted_data)))
