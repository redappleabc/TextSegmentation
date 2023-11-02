import os
import requests
import json
import shutil

import requests

def ocr(filename):
    with open(filename, 'rb') as f:
        img_data = f.read()
        try:
            files=[('file',('file',f,'image/png'))
]
            r = requests.post('https://portal.vision.cognitive.azure.com/api/demo/analyze?features=read',
                              files=files,
                              payload={}
                              )
            return json.loads(r.content.decode())
        except requests.exceptions.RequestException as err:
            print("Error connecting to OCR Space API: ", err)
            return None
        except Exception as e:
            print("Unexpected error: ", e)
            return None

def main():
    directory_path = './images'
    temp_path = './ocr'
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.makedirs(temp_path)

    files = os.listdir(directory_path)
    files.sort()

    url = "https://portal.vision.cognitive.azure.com/api/demo/analyze?features=read"
    
    for file in files:
        try:
            file_path = os.path.join(directory_path, file)
            print("ocr processing: ", file_path)
            with open(file_path, 'rb') as f:
                files=[('file',(file,f,'image/png'))]
                response = requests.request("POST", url, data={}, files=files)
                # print(response.text)
                temp_file = os.path.join(temp_path, file + '.json')
                with open(temp_file, 'w', encoding='utf-8-sig') as ff:
                    ff.write(response.text)

        except Exception as err:
            print('Error:', err)

if __name__ == "__main__":
    main()
