from Crypto.Cipher import AES, ARC4

aes_key = bytes(b'\xFF') * 16 
rc4_key = bytes(b'\xFF') * 5
data = "This is da wireless security lab"

aes_cipher = AES.new(aes_key, AES.MODE_ECB)
aes_encrypted_data = aes_cipher.encrypt(bytes(data, 'utf-8'))
rc4_cipher = ARC4.new(rc4_key)
rc4_encrypted_data = rc4_cipher.encrypt(bytes(data, 'utf-8'))

# 0a61bca4a30a30ba2c65ab208abbd783296d960f80c231720e119982098d30d3
print(aes_encrypted_data.hex())
# 394d4657503a68905d2ab3c3ad1db8f08dcf83d11dbed8a69f2c079571f4d984
print(rc4_encrypted_data.hex())

def brute_force_aes(key_size_bits, encrypted_text):
	key_int = a = pow(2, 128) - 1
	for _ in range(pow(2, key_size_bits)):
		key = key_int.to_bytes(16, 'big')
		aes_cipher = AES.new(key, AES.MODE_ECB)
		decrypted_text = aes_cipher.decrypt(encrypted_text)
		# use package like nltk to see if decrypted_text looks like a real sentence
		is_english = False
		if is_english:
			print(decrypted_text)
		key_int -= 1


def brute_force_rc4(key_size_bits, encrypted_text):
	key_int = a = pow(2, 40) - 1
	for _ in range(pow(2, key_size_bits)):
		key = key_int.to_bytes(5, 'big')		
		rc4_cipher = ARC4.new(key)
		decrypted_text = rc4_cipher.decrypt(encrypted_text)
		# use package like nltk to see if decrypted_text looks like a real sentence
		is_english = False
		if is_english:
			print(decrypted_text)
		key_int -= 1

brute_force_aes(128, aes_encrypted_data)
brute_force_rc4(40, rc4_encrypted_data)