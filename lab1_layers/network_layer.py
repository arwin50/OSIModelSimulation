import json

class NetworkLayer:
    def send(self, data, ip_address):
        print("[Network Layer] Adding IP address:", ip_address)
        packet = {'IP': ip_address, 'Data': data}
        print("[Network Layer] Packet content:", packet)
        return json.dumps(packet)
    
    def receive(self, packet):
        print("[Network Layer] Extracting data from packet")
        packet = json.loads(packet)
        print("[Network Layer] Extracted Data:", packet['Data'])
        return packet['Data']