import os 
  
#function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("mouna noureddine")): 
        dst ="m" + str(count) + ".jpg"
        src ='mouna noureddine/'+ filename 
        dst ='mouna noureddine/'+ dst 

        os.rename(src, dst) 
  
if __name__ == '__main__': 
  
    main() 
