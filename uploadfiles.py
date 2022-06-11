class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(filefrom,"overwrite")
        dbx.files_upload(f.read(),fileto)
def main():
    access_token="sl.BG0Fyr_wCQ3Ipgnc6ni0pnsmbbs1MBEo3SXCNIomffuqafpzUaV20bgszypZmFp5TbFxEelM2l4VSgdf740dLB_uXiTGi3PcWBFvoh3fwdQ2IqYwMg77Z7vj9cIFwF--xRgzGfoL_ock"
    filefrom = input("Where is the file from?")
    fileto = input("Where should the file be put?")
    transferdata.upload_file(filefrom,fileto)
    print("Flie moved")
main()