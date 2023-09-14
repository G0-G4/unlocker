import zipfile
import re
import os
import shutil
import sys

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

if __name__ == '__main__':
    print(sys.argv)
    file = sys.argv[1]
    file_nm = file[:-5]
    crack(file, file_nm)
    shutil.rmtree(file_nm)
    os.rename(file_nm + '.docx' + '.zip', file_nm + '_cracked.docx')