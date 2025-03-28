from lab1_layers import application_layer, presentation_layer, session_layer, transport_layer, network_layer, datalink_layer, physical_layer
import socket
import uuid

def get_local_ip():
    """Retrieve the correct local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "127.0.0.1"



def get_mac_address():
    """Retrieve the correct MAC address."""
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02X}'.format((mac >> ele) & 0xFF)
                            for ele in range(0, 8 * 6, 8)][::-1])
    return mac_address

def main():
    string = input("Enter your message!\n")
    app = application_layer.ApplicationLayer()
    pres = presentation_layer.PresentationLayer()
    sess = session_layer.SessionLayer()
    trans = transport_layer.TransportLayer()
    net = network_layer.NetworkLayer()
    data_link = datalink_layer.DataLinkLayer()
    phys = physical_layer.PhysicalLayer()
    
    ip_address = get_local_ip()
    mac_address = get_mac_address()

    print(f"\nDetected IP Address: {ip_address}")
    print(f"Detected MAC Address: {mac_address}")

    print("\n--- Sending Data ---")
    encoded_request = pres.send(string)
    session_data = sess.send(encoded_request, session_id=123)
    transport_data = trans.send(session_data, seq_num=1)
    network_data = net.send(transport_data, ip_address=ip_address)
    data_link_frame = data_link.send(network_data, mac_address=mac_address)
    physical_bits = phys.send(data_link_frame)

    print("\n--- Receiving Data ---")
    received_data_link = phys.receive(physical_bits)
    received_network = data_link.receive(received_data_link)
    received_transport = net.receive(received_network)
    received_session = trans.receive(received_transport)
    received_presentation = sess.receive(received_session)
    response = pres.receive(received_presentation)
    final_response = app.send(response)

    print("\nFinal Response:")
    print(final_response)

if __name__ == "__main__":
    main()
