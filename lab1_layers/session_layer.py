import json

class SessionLayer:
    def send(self, data, session_id):
        print("[Session Layer] Managing connection state, Session ID:", session_id)
        session_packet = {'Session': session_id, 'Data': data}
        print("[Session Layer] Session packet content:", session_packet)
        return json.dumps(session_packet)
    
    def receive(self, session_packet):
        print("[Session Layer] Extracting session data")
        session_packet = json.loads(session_packet)
        print("[Session Layer] Extracted Data:", session_packet['Data'])
        return session_packet['Data']