from html.parser import HTMLParser
import urllib.request
import zipfile
import shutil
import os
import time
import sys
# import psutil
# import signal
import base64
import subprocess

class Updater(HTMLParser):
    def __init__(self):
        super().__init__()
        self.is_target = False  # Belirtilen id'yi bulmak için bayrak
        self.data_list = []  # Bulunan verileri saklamak için liste
        self.current_version = 2000 # Bu programın sürümü


    def handle_starttag(self, tag, attrs):
        """Başlangıç etiketini işleyerek id kontrolü yap"""
        if tag == "b":  # Sadece <b> etiketlerine odaklan
            for attr, value in attrs:
                if attr == "id" and value == "version":
                    self.is_target = True

    def handle_endtag(self, tag):
        """Kapanış etiketini işleyerek id kontrolünü sıfırla"""
        if tag == "b" and self.is_target:
            self.is_target = False

    def handle_data(self, data):
        """Etiket içindeki metni al"""
        if self.is_target:
            self.data_list.append(data.strip())

    def version(self):
        # Web sayfasından HTML içeriğini al
        url = "https://raw.githubusercontent.com/Ultrareflex8672/EyeOnU/refs/heads/main/CHANGELOG.md"
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode("utf-8")

        # Parser'ı çalıştır ve veriyi işle
        parser = Updater()
        parser.feed(html_content)

        new_version = int(parser.data_list[0].replace(".", ""))

        # Bulunan veriyi yazdır
        return new_version, self.current_version
    
# if __name__ == "__main__":
#     updater = Updater()
#     new_version, current_version = updater.version()
#     print("New version:", new_version)
#     print("Current version:", current_version)
