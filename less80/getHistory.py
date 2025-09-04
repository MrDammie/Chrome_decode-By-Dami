import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil


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
    login_db_History = "History"
    extract_chrome_Historys(login_db_History)

