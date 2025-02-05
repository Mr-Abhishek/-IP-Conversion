def ipv4_to_ipv6(ipv4):
    # Split the IPv4 address into its four octets
    octets = ipv4.split('.')

    # Convert each octet to hexadecimal and ensure two digits
    hex_octets = [format(int(octet), '02x') for octet in octets]

    # Combine the hex values into the IPv6 format with leading zeros
    ipv6 = '0000:0000:0000:0000:0000:0000:ffff:' + hex_octets[0] + hex_octets[1] + ':' + hex_octets[2] + hex_octets[3]

    return ipv6

def ipv6_to_ipv4(ipv6):
    # Check if the IPv6 address is an IPv4-mapped IPv6 address
    if ipv6.startswith("0000:0000:0000:0000:0000:0000:ffff:"):
        try:
            # Extract the hexadecimal part
            hex_part = ipv6.split("0000:0000:0000:0000:0000:0000:ffff:")[1]
            # Split the hexadecimal part into two segments
            hex_segments = hex_part.split(':')
            # Convert each segment from hexadecimal to decimal
            octets = [str(int(segment[:2], 16)) for segment in hex_segments] + [str(int(segment[2:], 16)) for segment in hex_segments]
            # Combine the octets into an IPv4 address
            ipv4 = '.'.join(octets)
            return ipv4
        except ValueError:
            return "Invalid IPv4-mapped IPv6 address"
    else:
        return "Not an IPv4-mapped IPv6 address"

while True:
    choice = input("Enter '1' to convert IPv4 to IPv6, '2' to convert IPv6 to IPv4 (or type 'exit' to quit): ")
    if choice.lower() == 'exit':
        break
    elif choice == '1':
        ipv4_address = input("Enter an IPv4 address: ")
        try:
            ipv6_address = ipv4_to_ipv6(ipv4_address)
            print(f"IPv4 address: {ipv4_address}")
            print(f"IPv6 address: {ipv6_address}")
        except ValueError:
            print("Invalid IPv4 address. Please try again.")
    elif choice == '2':
        ipv6_address = input("Enter an IPv6 address: ")
        try:
            ipv4_address = ipv6_to_ipv4(ipv6_address)
            if ipv4_address in ["Not an IPv4-mapped IPv6 address", "Invalid IPv4-mapped IPv6 address"]:
                print(ipv4_address)
            else:
                print(f"IPv6 address: {ipv6_address}")
                print(f"IPv4 address: {ipv4_address}")
        except ValueError:
            print("Invalid IPv6 address. Please try again.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
