from PIL import ImageGrab
from screeninfo import get_monitors
import pyautogui
import time
import os
#import datetime

def create_folder(folder_name):
    folder_path = os.path.join(os.getcwd(), folder_name) 
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")
    return folder_path #get name for variable

def get_width_prim():
     for monitor in get_monitors():
          if monitor.is_primary:
               return monitor.width
screen_width = get_width_prim()

def get_height_prim():
     for monitor in get_monitors():
          if monitor.is_primary:
               return monitor.height
screen_height = get_height_prim()

#set border
border = 150 #int(input("Enter the number of pixels of the frame border: "))

#bbox
bbox_l = border
bbox_t = border
bbox_r = screen_width - border
bbox_b = screen_height - border

if __name__ == "__main__":    

        folder_name = input("Enter the folder name: ")
        folder_path = create_folder(folder_name) #assign the name for the varible 

        screenshot_no = int(input("Enter the number of screenshots: ")) #number of screenshots
        column_no = int(input("Enter the number of columns: ")) #number of columns / vertical slices

            #random buttons and clicks that do nothing
        grab_x = (screen_width) // 2
        grab_y = (screen_height) // 2 #180
        pyautogui.moveTo(grab_x, grab_y)
        pyautogui.click()
        pyautogui.press('n') 
        pyautogui.press('r') 
        time.sleep(2) 
        #print("center coords",grab_x,",", grab_y)
        #print("drag distance x y",drag_d_x,"__", drag_d_y)


        for column in range(column_no):
            column_images = [] #for collage stitch down the line
            for i in range(screenshot_no): 
             
      
                #set grab location (bbox center)
                grab_x = (screen_width) // 2
                grab_y = (screen_height) // 2 #180
                drag_d_x = ((bbox_r-border) // 2)+21
                drag_d_y = ((bbox_b-border) // 2)






                #(left, top, right, bottom from the top left corner of primary monitor)
                screenshot = ImageGrab.grab(bbox=(bbox_l,bbox_t,bbox_r,bbox_b)) #set pixels to exclude interface of 
                #the software this will break the script if you put the wrong values



                #set the name for the capture
            #add timestampt if you want to avoid overwrites/need many of the same 
            ##timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')

                #delay tile-loading
                if i < screenshot_no :
                    print(f"holding for tiles ss[{i+1}] 5 sec")
                    time.sleep(5)      

                
                screenshot_name = os.path.join(folder_path, f"{folder_name}_{column+1}_screenshot_{i+1}.png")
                #screenshot_name = os.path.join(folder_path,"{}_{}.png".format(folder_name,timestamp))
                screenshot.save(screenshot_name)
                #add to list above
                column_images.append(screenshot_name)
                
                #click and drag
                pyautogui.moveTo(grab_x, grab_y)
                pyautogui.mouseDown()
                pyautogui.move(0,drag_d_y, duration=1)
                pyautogui.mouseUp()
                
                #2 test
                pyautogui.moveTo(grab_x, grab_y)
                pyautogui.mouseDown()
                pyautogui.move(0,drag_d_y, duration=1)
                pyautogui.mouseUp()







            #after column capture / reposition right (drag left)
            print("repositioning")
            time.sleep(1) 
            pyautogui.moveTo(grab_x, grab_y)
            pyautogui.mouseDown()
            pyautogui.move(-drag_d_x, 0, duration=1)  #half screen res drag because it errors its brains out #-1280
            pyautogui.mouseUp()
            time.sleep(1) 
            pyautogui.moveTo(grab_x, grab_y)
            pyautogui.mouseDown()
            pyautogui.move(-drag_d_x, 0, duration=1)  
            pyautogui.mouseUp()
            print("finished right")

            #go back down no screenshot
            for i in range(screenshot_no):
                pyautogui.moveTo(grab_x, grab_y)
                pyautogui.mouseDown()
                pyautogui.move(0, -drag_d_y, duration=1)  #reverse drag
                pyautogui.mouseUp()
                #2            
                pyautogui.moveTo(grab_x, grab_y)
                pyautogui.mouseDown()
                pyautogui.move(0, -drag_d_y, duration=1)  #reverse drag
                pyautogui.mouseUp()

            #imagemagick per column
                
            column_images.reverse() #changing the order of the iamges because they appeared top to bottom
                
            collage_name = f"Column_{column + 1}_collage.png"
            collage_command = "magick montage -mode concatenate -tile 1x" + str(screenshot_no) + " "
            collage_command += " ".join(column_images) + " " + os.path.join(folder_path, collage_name)
            os.system(collage_command)

