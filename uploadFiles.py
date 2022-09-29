import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from , file_to):
      dbx = dropbox.Dropbox(self.access_token)

      f = open(file_from,'rb')
      dbx.files_upload(f.read(),file_to)

def main():
       access_token = 'sl.BMo74VRCAUkc00ZRD9F_lfByquMuiJZp8teF6nyYuBYWc5L2lRd-Iuxl2VpcejDHEj2w3vxes3VDFvAuUY9mez_9pE8bkAm41l8Z0xxyXLVBriq5BlDY7R2EH1huCTQzq1OwtDI'
       transferData = TransferData(access_token)
       file_from = input("Enter the file part to transfer :- ")
       file_to = input("Enter the full path to upload to dropbox:- ")

       transferData.upload_file(file_from, file_to)
       print("File has been moved")

main()