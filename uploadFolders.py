import dropbox


class TransferData:
    def __init__(self,acessToken):
        self.accessToken = acessToken

    def uploadFolder(self,Folder_From,Folder_To):
        ""
        dbx=dropbox.Dropbox(self.accessToken)

        f = open(Folder_From,'rb')
        dbx.files_upload(f.read(),Folder_To)

def main():
    acessToken = "sru8syS53JIAAAAAAAAAAeDSZqG8f6kyqrexxLQjfLGN2JT7M4mq5Blvqvf3BE2n"
    transferData = TransferData(acessToken)

    Folder_From = input('enter a folder name')
    Folder_To = input('enter path')

    transferData.uploadFolder(Folder_From,Folder_To)
main()