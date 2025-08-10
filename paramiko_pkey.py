import paramiko

def key_based_connect(server):
    host = "192.0.2.0"  # You can replace this with server-specific IP mapping
    special_account = "user1"
    
    pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=special_account, pkey=pkey)
    return client

def examine_last(server, connection, log_file="/var/log/syslog", lines=10):
    """
    Retrieves the last 'n' lines from a log file on the remote server.
    """
    try:
        stdin, stdout, stderr = connection.exec_command(f"tail -n {lines} {log_file}")
        output = stdout.read().decode()
        error = stderr.read().decode()

        print(f"\n--- {server} ---")
        if output:
            print(output)
        if error:
            print(f"Error: {error}")

    except Exception as e:
        print(f"Error examining logs on {server}: {e}")
    finally:
        connection.close()

def main():
    server_list = ["worker1", "worker2", "worker3"]
    for server in server_list:
        connection = key_based_connect(server)
        examine_last(server, connection)

if __name__ == "__main__":
    main()
