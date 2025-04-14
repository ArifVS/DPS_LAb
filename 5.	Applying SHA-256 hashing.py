import hashlib

def generate_sha256_hash(data):
  return hashlib.sha256(data.encode()).hexdigest()

def verify_data_integrity(original_data, received_data):
  original_hash = generate_sha256_hash(original_data)
  received_hash = generate_sha256_hash(received_data)
  if original_hash == received_hash:
    print("Data integrity verified! No tampering detected.")
  else:
    print("Data has been tampered with!")

original_data = "Secure Hash Algorithm ensures data integrity."
tampered_data = "Secure Hash Algorithm ensures data security."

verify_data_integrity(original_data, tampered_data)
verify_data_integrity(original_data, original_data)

original_hash = generate_sha256_hash(original_data)
print("Original Data Hash:", original_hash)
