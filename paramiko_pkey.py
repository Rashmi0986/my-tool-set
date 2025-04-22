def key_based_connect(server):
     host = "192.0.2.0"
     special_account = "user1"
 pkey = paramiko.RSAKey.from_private_key_file("./id_rsa")
 client = paramiko.SSHClient()
 policy = paramiko.AutoAddPolicy()
 client.set_missing_host_key_policy(policy)
 client.connect(host, username=special_account, pkey=pkey)
 return client

def main():
     server_list = ["worker1", "worker2", "worker3"]
 for server in server_list:
         connection = key_based_connect(server)
         examine_last(server, connection)
