Browser_Information_Collection
    Chrome Version less 80


███╗   ███╗██╗   ██╗███████╗ █████╗ ███████╗ █████╗
████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║   ██║███████╗███████║█████╗  ███████║
██║╚██╔╝██║██║   ██║╚════██║██╔══██║██╔══╝  ██╔══██║
██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Version: v.1.0  - Chrome Version less 80 Decode 12/02/25 - Mufasa @Dami



【	
	time:2025.2.12
	

	基于  mimikatz dpapi chrome ，python 脚本 密码导出工具
	
	Tools_Mufasa_Chrome_less80_decode.exe
	
	使用方法：	
	{
	            
	    ████╗ ████║██╗   ██╗███████╗ █████╗ ███████╗ █████╗
	    ████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
	    ██╔████╔██║██║   ██║███████╗███████║█████╗  ███████║
	    ██║╚██╔╝██║██║   ██║╚════██║██╔══██║██╔══╝  ██╔══██║
	    ██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║███████╗██║  ██║
	    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
	    Version: v.1.0  - Chrome Version less 80 Decode 12/02/25 - Mufasa @Dami
	    Usage:
	        1、从目标机器 将 Login Data  、Cookies 、History 文件 下载会本地
	        2、从目标机器机器上面把 lsass 进程转存 下载会本地
	        注意：文件路径不能有空格和中文     
	        3、 .exe -run get_Cookies  || .exe -run get_Password   || .exe -run get_History
	
	}
	
	使用事项：
	
	{	
	    从目标机器 将 Login Data  、Cookies 、 History 文件下载会本地
	    从目标机器机器上面把 lsass 进程转存 下载会本地
	    注意：文件路径不能有空格和中文
	    本程序直接调用当前计算机环境变量中的python.exe
	    使用到的 import包  （自行部署）
	                    import os
	                    import json
	                    import base64
	                    import sqlite3
	                    import win32crypt
	                    from Crypto.Cipher import AES
	                    import shutil
	
	要在高权限下使用
	}

】


Browser_Information_Collection
    Chrome Version more 80


███╗   ███╗██╗   ██╗███████╗ █████╗ ███████╗ █████╗
████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║   ██║███████╗███████║█████╗  ███████║
██║╚██╔╝██║██║   ██║╚════██║██╔══██║██╔══╝  ██╔══██║
██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

Version: v.1.0  - Chrome Version more 80 Decode 12/02/25 - Mufasa @Dami
Usage:
     1: exe -K <master_key_w_Cry>   Get Masterkey.txt
     2: exe -s <script_option>
           -s
             get_master_key_w_Cry || get_chrome_info

【	
	time:2025.2.12
	

	基于 python 提取、解密、Windows 中 DPAI 解密 脚本 工具
	
	 Tools_Mufasa_Chrome_decode.exe
	
	使用方法：
		
	{
	    E:\Nw\Browser_Information_Collection\Chrome\_More80>Tools_Mufasa_Chrome_decode.exe
	    ████╗ ████║██╗   ██╗███████╗ █████╗ ███████╗ █████╗
	    ████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝██╔══██╗
	    ██╔████╔██║██║   ██║███████╗███████║█████╗  ███████║
	    ██║╚██╔╝██║██║   ██║╚════██║██╔══██║██╔══╝  ██╔══██║
	    ██║ ╚═╝ ██║╚██████╔╝███████║██║  ██║███████╗██║  ██║
	    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
	    Version: v.1.0  - Chrome Version more 80 Decode 12/02/25 - Mufasa @Dami
	    Usage:
	        1: exe -K <master_key_w_Cry>   Get Masterkey.txt
	        2: exe -s <script_option>
	            -s
	                get_master_key_w_Cry || get_chrome_info
	
	}
	注意事项：
	    -K 参数：
	        在目标机器执行 指定的参数为使用 -s get_master_key_w_Cry 执行得到的 masterkey 中间值 得到 Masterkey.txt
	    -s 参数：
	        在本机执行
	        get_master_key_w_Cry || get_chrome_info
	        执行  get_master_key_w_Cry ，当前目录下要有 Local State 提取得到用于 解密的值
	        执行  get_chrome_info ，当前目录下要有 Login Data、History、Cookies
	
	    本程序直接调用当前计算机环境变量中的python.exe
	    使用到的 import包  （自行部署）
	                    import json
	                    import base64
	                    import os
	                    import json
	                    import base64
	                    import sqlite3
	                    import win32crypt
	                    from Crypto.Cipher import AES
	                    import shutil
	
	要在高权限下使用

】










































