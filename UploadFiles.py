import os
import dropbox
from dropbox.files import WriteMode
class Tranferdata:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token="tCl1A5yQrKwAAAAAAAAAASVCl6cNj2FRsaUH2NolScoleO4xUPA0hRFJIlJh__Bg"
    tranferdata=Tranferdata(access_token)
    file_from='C:/Users/jaska/OneDrive/Desktop/data/python/class/c99.py'
    file_to='/test_dropbox/test.txt'
    tranferdata.upload_file(file_from,file_to)

if __name__ == '__main__':
    main()

