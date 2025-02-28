from lab1_layers import application_layer, presentation_layer, session_layer, transport_layer, network_layer, datalink_layer, physical_layer


def main():
    string = input("Enter your message!\n")
    app = application_layer.ApplicationLayer()
    pres = presentation_layer.PresentationLayer()
    sess = session_layer.SessionLayer()
    trans = transport_layer.TransportLayer()
    net = network_layer.NetworkLayer()
    data_link = datalink_layer.DataLinkLayer()
    phys = physical_layer.PhysicalLayer()
    
    print("\n--- Sending Data ---")
    encoded_request = pres.send(string)
    session_data = sess.send(encoded_request, session_id=123)
    transport_data = trans.send(session_data, seq_num=1)
    network_data = net.send(transport_data, ip_address="192.168.1.1")
    data_link_frame = data_link.send(network_data, mac_address="00:1B:44:11:3A:B7")
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