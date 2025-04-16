import paramiko

# Connection details
hostname = "remote_host_ip_or_name"
port = 22
username = "your_username"
password = "your_password"  # Or use SSH keys for better security

# Command to execute
command = "ls -l /home/your_username"

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Automatically add unknown hosts

try:
    # Connect to the remote server
    client.connect(hostname, port=port, username=username, password=password)

    # Execute command
    stdin, stdout, stderr = client.exec_command(command)

    # Read output
    print("STDOUT:\n", stdout.read().decode())
    print("STDERR:\n", stderr.read().decode())

finally:
    # Close connection
    client.close()
