class PhysicalLayer:
    def send(self, data):
        print("[Physical Layer] Sending data as bits:", data)
        bits = ''.join(format(byte, '08b') for byte in data)
        print("[Physical Layer] Encoded bits:", bits)
        return bits
    
    def receive(self, bits):
        print("[Physical Layer] Receiving bits:", bits)
        bytes_data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
        print("[Physical Layer] Decoded bytes:", bytes_data)
        return bytes_data
