import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil


def get_master_key():
    with open("MasterKey.txt", "rb") as ms:
        buf = ms.read()
        print(buf)
        return buf


def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)


def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)


def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # 去掉后缀字节
        return decrypted_pass
    except Exception as e:
        # print("可能是Chrome版本低于v80保存的密码\n")
        # print(str(e))
        return "Chrome < 80"


def extract_chrome_passwords(master_key, login_db_path):
    """
    从Chrome的Login Data数据库中提取并解密保存的密码。

    参数:
    - master_key (bytes): 解密用的主密钥。
    - login_db_path (str): Login Data数据库的路径。

    返回:
    - None: 打印提取并解密后的密码。
    """
    shutil.copy2(login_db_path, "Loginvault.db")  # 复制一份临时文件，因为Chrome正在运行时Login Data DB是被锁住的
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            print("URL: " + url + "\n用户名: " + username + "\n密码: " + decrypted_password + "\n" + "*" * 50 + "\n")
    except Exception as e:
        print(f"获取密码时出错: {e}")
    finally:
        cursor.close()
        conn.close()

    try:
        os.remove("Loginvault.db")
    except Exception as e:
        pass


def extract_chrome_Cookies(master_key, login_db_path):
    """
    从Chrome的Cookies数据库中提取并解密保存的密码。

    参数:
    - master_key (bytes): 解密用的主密钥。
    - login_db_path (str): Cookies数据库的路径。

    返回:
    - None: 打印提取并解密后的密码。
    """
    shutil.copy2(login_db_path, "Loginvault_Cookies.db")  # 复制一份临时文件，因为Chrome正在运行时Login Data DB是被锁住的
    conn = sqlite3.connect("Loginvault_Cookies.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT host_key, encrypted_value,name FROM cookies")
        for r in cursor.fetchall():
            host_url = r[0]
            encrypted_host_Cookies = r[1]
            host_Cookies_name=r[2]
            decrypted_host_Cookies = decrypt_password(encrypted_host_Cookies, master_key)
            print("URL: " + host_url + "\n " +"Cookies_Name："+host_Cookies_name+"\n Cookies: " + decrypted_host_Cookies+ "\n" + "————" * 100 + "\n")
    except Exception as e:
        print(f"获取Cookies时出错: {e}")
    finally:
        cursor.close()
        conn.close()

    try:
        os.remove("Loginvault_Cookies.db")
    except Exception as e:
        pass

def extract_chrome_Historys(login_db_path):
    """
    从Chrome的 History 记录数据库中提取并解密保存的密码。

    参数:

    - login_db_path (str): History 数据库的路径。

    返回:
    - None: 打印提取并解密后的密码。
    """
    shutil.copy2(login_db_path, "Loginvault_History.db")  # 复制一份临时文件，因为Chrome正在运行时Login Data DB是被锁住的
    conn = sqlite3.connect("Loginvault_History.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT url,title FROM urls")
        for r in cursor.fetchall():
            History_url = r[0]
            History_title = r[1]

            print(" History_url: " + History_url + "\n "+"History_title: "+History_title+"\n"+"————" * 100 + "\n")
    except Exception as e:
        print(f"获取History时出错: {e}")
    finally:
        cursor.close()
        conn.close()

    try:
        os.remove("Loginvault_History.db")
    except Exception as e:
        pass


if __name__ == '__main__':
    master_key = base64.b64decode(get_master_key())
    login_db_Password = "Login Data"  # os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\default\Login Data'
    login_db_Cookies = "Cookies"
    login_db_History = "History"
    # 调用函数提取并打印Chrome密码
    extract_chrome_passwords(master_key, login_db_Password)
    extract_chrome_Cookies(master_key, login_db_Cookies)
    extract_chrome_Historys(login_db_History)

