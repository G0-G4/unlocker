import zipfile
import re
import os
import shutil

def crack(name, folder):
    with zipfile.ZipFile(name) as z:
        z.extractall(folder)
    pattern = '<w:documentProtection[^>]*>'
    settings_path = os.path.join(folder, 'word', 'settings.xml')
    with open(settings_path) as f:
        xml = f.read()
        res = re.sub(pattern, '', xml, count=1)
    with open(settings_path, 'w') as f:
        f.write(res)
    shutil.make_archive(name, 'zip', folder)