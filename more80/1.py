import json
import base64

def get_master_key_w_Cry():
    with open('.\Local State', "r") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key_w_Cry = master_key[5:]  # Removing DPAPI
    return base64.b64encode(master_key_w_Cry)

# Save master_key_w_Cry to a file
with open(".\master_key_w_Cry.txt", "wb") as ms:
    ms.write(get_master_key_w_Cry())
