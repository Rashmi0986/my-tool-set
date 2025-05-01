def get_next_ip(ipaddr):
    parts = ipaddr.strip().split('.')
    
    # Validate IP address format
    if len(parts) != 4:
        return "Invalid IP: Incorrect number of octets"
    
    try:
        octets = [int(part) for part in parts]
    except ValueError:
        return "Invalid IP: Non-integer octet"

    if any(o < 0 or o > 255 for o in octets):
        return "Invalid IP: Octets must be between 0 and 255"

    # Convert to a single integer
    ip_num = (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

    if ip_num == 0xFFFFFFFF:  # 255.255.255.255
        return "Can't generate next IP"

    # Increment the IP
    ip_num += 1

    # Convert back to dotted format
    next_ip = ".".join(str((ip_num >> (8 * i)) & 0xFF) for i in reversed(range(4)))
    return next_ip

# Test cases
print(get_next_ip("192.168.10.1"))     # Should return 192.168.10.2
print(get_next_ip("192.168.10.255"))   # Should return 192.168.11.0
print(get_next_ip("255.255.255.255"))  # Should return Can't generate next IP
print(get_next_ip("10.0.0.255"))       # Should return 10.0.1.0
