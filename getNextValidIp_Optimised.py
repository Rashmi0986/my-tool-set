def get_next_ip(ipaddr):
    parts = ipaddr.strip().split('.')

    # Validate IP
    if len(parts) != 4:
        return "Invalid IP: Should have 4 octets"
    
    try:
        octets = [int(part) for part in parts]
    except ValueError:
        return "Invalid IP: All parts must be numbers"

    if any(o < 0 or o > 255 for o in octets):
        return "Invalid IP: Octets must be between 0 and 255"

    # Increment IP from last octet and handle carry-over
    for i in range(3, -1, -1):  # Start from last octet
        if octets[i] < 255:
            octets[i] += 1
            break
        else:
            octets[i] = 0
    else:
        return "Can't generate next IP"

    return ".".join(str(o) for o in octets)

# Test cases
print(get_next_ip("192.168.10.1"))     # 192.168.10.2
print(get_next_ip("192.168.10.255"))   # 192.168.11.0
print(get_next_ip("255.255.255.255"))  # Can't generate next IP
print(get_next_ip("10.0.0.255"))       # 10.0.1.0


# Test cases
print(get_next_ip("192.168.10.1"))     # Should return 192.168.10.2
print(get_next_ip("192.168.10.255"))   # Should return 192.168.11.0
print(get_next_ip("255.255.255.255"))  # Should return Can't generate next IP
print(get_next_ip("10.0.0.255"))       # Should return 10.0.1.0
