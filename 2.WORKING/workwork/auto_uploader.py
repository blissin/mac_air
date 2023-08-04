import os
import sys
import requests

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.dirname(__file__)
    
owner = 'blissin'
repo = 'mac_air'
res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/releases/latest', headers={'Authorization':f'token {MY_API_KEY}'})
data = res.json()
print('latest version :',data['tag_name'])

script_directory = os.path.dirname(os.path.abspath(__file__))
absolute_path = os.path.join(script_directory, "version")
with open(absolute_path,"r") as f:
    now_version = f.readlines()
print(now_version[0],end='')

if now_version[1]<data['assets'][0]['updated_at']:
    print(data['assets'][0]['updated_at'])
    print('downloading...')
    download_url = data["assets"][0]["url"]
    contents = requests.get(download_url, auth=(owner, MY_API_KEY), headers={'Accept': 'application/octet-stream'}, stream=True)
    try:
        os.remove(os.path.join(application_path,'test.exe'))
    except:
        pass
    with open(os.path.join(application_path, f'''test.exe'''), "wb") as f:
        for chunk in contents.iter_content(chunk_size = 1024*1024):
            f.write(chunk)
    file_name = os.path.join(application_path,'test.exe')
    hidden_name = "."+os.path.join(application_path,'test.exe')
    
    os.rename(file_name, hidden_name)
os.startfile(os.path.join(application_path, ".test.exe"))
