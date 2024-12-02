

import telebot
import face_recognition
from PIL import Image, ImageDraw
import io
import cv2
from telebot import types
import os
import numpy as np



bot =telebot.TeleBot("7948796136:AAF3Wja3B1L3gPkHs2_jPjsNyjSW12Z1XpE")
user_state = {}
count_11 = -1
per_count = -1


@bot.message_handler(commands =['all_data'])
def all_members(message):
    if not os.path.exists("bot_folder"):
        os.mkdir("bot_folder")
    
    
    names =os.path.join("bot_folder",'names')
    if not os.path.exists("names"):
        with open(f"{names}.txt",'a') as f:
            pass
    
    
    counter =os.path.join("bot_folder",'counter')
    if not os.path.exists("counter"):
        cur_state =False
        try:
            with open(f"{counter}.txt") as f:
                for i in f:
                    i =i.strip()
                    if i =="":
                        cur_state =True
                    else:
                        pass
            
            with open(f"{counter}.txt",'a') as f:
                if cur_state ==True:
                    f.write("0")
                else:
                    pass
        except:
                            
            with open(f"{counter}.txt",'a') as f:
                f.write("0")
        
    q =""
    con =int(0)
    nam =""
    
    with open(f"bot_folder/counter.txt") as f:
        for i in f:
            i =i.strip()
            q +=i
    
    
    with open(f"bot_folder/names.txt") as f:
        for i in f:
            i =i.strip()
            nam +=str(i)+"\n"
    
    
    for i in q:
        con +=int(i)
    
    if nam.strip() =="":
        bot.send_message(message.chat.id, "There isn't any data")
    else:
        nam =nam.strip().split()
        info =""
        for i in nam:
            bot.send_photo(message.chat.id, open(f"bot_folder/{i}", 'rb'))
            
            with open(f"bot_folder/{i}.txt") as f:
                for j in f:
                    j =j.strip()
                    info +=j+"\n"
            
            bot.send_message(message.chat.id, info)
            info =""
        bot.send_message(message.chat.id, "☑️Finished")
        
        
    
    
    
    
    




@bot.message_handler(commands =['start'])
def main(message):
            
    if not os.path.exists("bot_folder"):
        os.mkdir("bot_folder")
    
    
    names =os.path.join("bot_folder",'names')
    if not os.path.exists("names"):
        with open(f"{names}.txt",'a') as f:
            pass
    
    
    counter =os.path.join("bot_folder",'counter')
    if not os.path.exists("counter"):
        cur_state =False
        try:
            with open(f"{counter}.txt") as f:
                for i in f:
                    i =i.strip()
                    if i =="":
                        cur_state =True
                    else:
                        pass
            
            with open(f"{counter}.txt",'a') as f:
                if cur_state ==True:
                    f.write("0")
                else:
                    pass
        except:
                            
            with open(f"{counter}.txt",'a') as f:
                f.write("0")
        
    
    markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
    
    btn1 =types.KeyboardButton("📜Register")
    btn2 =types.KeyboardButton("🔍Search")
    markup1.row(btn1)
    markup1.row(btn2)
    
    
    bot.send_message(message.chat.id, "Hello world", reply_markup =markup1)




@bot.message_handler(func =lambda message: True)
def main2(message):
    if message.text.strip().lower() =="📜register":
        markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        btn1 =types.KeyboardButton("🌄Photo")
        btn3 =types.KeyboardButton("⬅️Back")
        markup1.row(btn1)
        markup1.row(btn3)
        
        bot.send_message(message.chat.id, "You have following options",reply_markup=markup1)
    
    elif message.text.strip().lower() =="🌄photo":
        bot.send_message(message.chat.id, "Send photo. Pls ensure that image's quality is good!")
        user_state[message.chat.id] = 'waiting_for_pic1'

    elif message.text.strip().lower() =="🎥video":
        bot.send_message(message.chat.id, "Send video. Pls ensure that image's quality is good!")
        bot.send_message(message.chat.id, "Note that video musn't be more than 30mb")
        user_state[message.chat.id] = 'waiting_for_video1'

    
    
    elif message.text.strip().lower() =="🔍search":
        markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        
        btn1 =types.KeyboardButton("🏙Picture")
        btn2 =types.KeyboardButton("🎥Video")
        btn3 =types.KeyboardButton("⬅️Back")

        markup1.row(btn1, btn2)
        # markup1.row(btn2)
        markup1.row(btn3)
        
        bot.send_message(message.chat.id, "Pls select category so search", reply_markup =markup1)

    elif message.text.lower().strip() =="🏙picture":
        
        bot.send_message(message.chat.id, "Send photo. Pls ensure that image's quality is good!")
        user_state[message.chat.id] = 'waiting_for_pic2'
    
    elif message.text.strip().lower() =="⬅️back":
        markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
        
        btn1 =types.KeyboardButton("📜Register")
        btn2 =types.KeyboardButton("🔍Search")
        markup1.row(btn1)
        markup1.row(btn2)
        
        
        bot.send_message(message.chat.id, "Main page", reply_markup =markup1)



@bot.message_handler(content_types=['photo'])
def name_handler(message):
    global user_state
     
    def compare_faces(message_1, message_2):
        try:
                
            im2 =face_recognition.load_image_file(message_2)
            im2_encodings =face_recognition.face_encodings(im2)[0]
            
            new_im_array1 = np.array(message_1) #for encoding cut faces
            im1_encoding =face_recognition.face_encodings(new_im_array1)[0]
            
            result =face_recognition.compare_faces([im1_encoding], im2_encodings)
            if result:
                print("False was printed")
            else:
                print("False was printed")
            print(result)
            return result[0]
        except:
            result =['Error1_encoding']
            print(result)
            return result[0]

    
    if message.photo:
                   
        if not os.path.exists("bot_folder"):
            os.mkdir("bot_folder")
        
        
        names =os.path.join("bot_folder",'names')
        if not os.path.exists("names"):
            with open(f"{names}.txt",'a') as f:
                pass
        
        
        counter =os.path.join("bot_folder",'counter')
        if not os.path.exists("counter"):
            cur_state =False
            try:
                with open(f"{counter}.txt") as f:
                    for i in f:
                        i =i.strip()
                        if i =="":
                            cur_state =True
                        else:
                            pass
                
                with open(f"{counter}.txt",'a') as f:
                    if cur_state ==True:
                        f.write("0")
                    else:
                        pass
            except:
                                
                with open(f"{counter}.txt",'a') as f:
                    f.write("0")
            
        
        
        
        
        
        
        if user_state.get(message.chat.id) =="waiting_for_pic1":
            bot.send_message(message.chat.id, "🔄Loading....")
            
            file_info = bot.get_file(message.photo[-1].file_id)        
            downloaded_file = bot.download_file(file_info.file_path)            
            im = face_recognition.load_image_file(io.BytesIO(downloaded_file))
            
            
            
            
            
            im_location =face_recognition.face_locations(im)
            cur_nams =[]
            desctiption_manager =False
            if len(im_location)>0:
                    
                
                for img in im_location:
                    top, right, bottom, left =img
                    
                    new_im =im[top:bottom, left:right]
                    pil_im =Image.fromarray(new_im)
                    nor_im1 =np.array(pil_im)
                    # bot.send_photo(message.chat.id, pil_im)
                    
                   
                    q =""
                    con =int(0)
                    nam =""
                    
                    with open(f"bot_folder/counter.txt") as f:
                        for i in f:
                            i =i.strip()
                            q +=i
                    
                    
                    with open(f"bot_folder/names.txt") as f:
                        for i in f:
                            i =i.strip()
                            nam +=str(i)+"\n"
                    
                    
                    for i in q:
                        con +=int(i)
                    
                    if nam.strip() =="":
                        pil_im.save(f"bot_folder/{con}_im.jpg")
                        cur_nams.append(f"{con}_im.jpg")
                        
                        
                        with open(f"bot_folder/names.txt",'a') as f:
                            f.write(f" {con}_im.jpg ")
                        
                        
                        with open(f"bot_folder/counter.txt",'a') as f:
                            f.write("1")
                        
                        
                        with open(f"bot_folder/{con}_im.jpg.txt",'w') as f:
                            pass
                        
                        bot.send_message(message.chat.id, "Success")
                    else:
                        nam =nam.strip().split()
                        print(nam)
                        
                        current_state_1 =False
                        for i in nam:
                            im2 =face_recognition.load_image_file(f"bot_folder/{i}")
                            im2_location =face_recognition.face_locations(im2)
                            if len(im2_location) >0:
                                try:
                                        
                                    im2_encoding =face_recognition.face_encodings(im2)[0]
                                    nor_im1_encoding =face_recognition.face_encodings(nor_im1)[0]
                                    p =face_recognition.compare_faces([im2_encoding], nor_im1_encoding)
                                    p =p[0]
                                    
                                    print("p: ", p)
                                except:
                                    p =False
                                    
                                    
                            else:
                                p =False
                            
                            
                            
                            
                            
                            # p =compare_faces(pil_im, f"bot_folder/{i}")                        
                            # print("p: ",p)
                            print(f"cur_names: ",cur_nams)
                            
                            if p =="Error1_encoding":
                                bot.send_message(message.chat.id, "Error1_encoding. Weather img quality is unsatisfactfull or problem in identity module")
                                current_state_1 =True
                                break
                            elif p:
                                # bot.send_message(message.chat.id, "This person exists in database")
                                current_state_1 =True
                                break
                            else:
                                current_state_1 =False
                        
                        
                        if current_state_1:                        
                            bot.send_message(message.chat.id, "There are matches")
                            desctiption_manager =True
                        else:    
                            desctiption_manager =False
                            cur_nams.append(f"{con}_im.jpg")                            
                            pil_im.save(f"bot_folder/{con}_im.jpg")
                            
                            with open(f"bot_folder/{con}_im.jpg.txt",'w') as f:
                                pass
                            
                            with open(f"bot_folder/names.txt",'a') as f:
                                f.write(f" {con}_im.jpg ")
                            
                            with open(f"bot_folder/counter.txt",'a') as f:
                                f.write("1")
                            
                            print("\n\ncur_names: ", cur_nams)
                
                if not cur_nams:
                    print("cur_nams is empty")
                    pass
                else:
                    
    
                    def user_info(message):
                        markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
                        btn1 =types.KeyboardButton("🌄Photo")
                        btn3 =types.KeyboardButton("⬅️Back")
                        markup1.row(btn1)
                        markup1.row(btn3)
                        
                        if message.text.lower().strip() =="📜descibe":
                            print("per_count: ", per_count)
                            def next_image(message):
                                global count_11, per_count
    
                                count_11 += 1
                                per_count += 1
                                
                                if per_count < len(cur_nams):
                                    with open(f"bot_folder/{cur_nams[count_11]}", "rb") as photo:
                                        bot.send_photo(message.chat.id, photo)
                                    
                                    
                                    bot.send_message(message.chat.id, f"Write description for {cur_nams[count_11]}: ",reply_markup =markup1)
                                    bot.register_next_step_handler(message, user_desk)
                                else:
                                    bot.send_message(message.chat.id, "✅All images processed.",reply_markup =markup1)
                                    return
    
                            def user_desk(message):
                                global count_11
    
                                desk = message.text.strip()
                                with open(f"bot_folder/{cur_nams[count_11]}.txt", 'w') as f:
                                    f.write(desk)
    
                                next_image(message)  # Move to the next image after processing input
    
                            next_image(message)  # Start with the first image
    
                            
                            
                    
                    # bot.send_message(message.chat.id, "Hello world", reply_markup =markup1)
    
                    
                    
                
                
                
                markup1 =types.ReplyKeyboardMarkup(resize_keyboard =True)
                btn1 =types.KeyboardButton("📜Descibe")
                markup1.row(btn1)
                
                
    
                if not cur_nams:
                    bot.send_message(message.chat.id, "All person(s) is/are in database")
                else:
                    global count_11, per_count
                    count_11 =-1
                    per_count =-1
                    
                    
                    
                    bot.send_message(message.chat.id, "pls use botton below to write desk",reply_markup =markup1)
                    bot.register_next_step_handler(message, user_info)
            else:
                bot.send_message(message.chat.id, "There aren't any people in the img")

                
                            
                        
                        
                            
                        
                    
                    
                    
            
            
            
            
                
                            
            user_state.pop(message.chat.id, None)
    
        elif user_state.get(message.chat.id) =="waiting_for_pic2":
              
                    
            def compare_faces(message_1, message_2):
                try:
                        
                    im2 =face_recognition.load_image_file(message_2)
                    im2_encodings =face_recognition.face_encodings(im2)[0]
                    
                    new_im_array1 = np.array(message_1) #for encoding cut faces
                    im1_encoding =face_recognition.face_encodings(new_im_array1)[0]
                    
                    result =face_recognition.compare_faces([im1_encoding], im2_encodings)
                    if result:
                        print("False was printed")
                    else:
                        print("False was printed")
                    print(result)
                    return result[0]
                except:
                    result =['Error1_encoding']
                    print(result)
                    return result[0]
               
            file_info = bot.get_file(message.photo[-1].file_id)        
            downloaded_file = bot.download_file(file_info.file_path)            
            im = face_recognition.load_image_file(io.BytesIO(downloaded_file))

            im_location =face_recognition.face_locations(im)


            bot.send_message(message.chat.id, "🔄Loading....")
            
            nam =""
            with open(f"bot_folder/names.txt") as f:
                for i in f:
                    i =i.strip()
                    nam +=str(i)+"\n"
            
            
            if nam.strip() =="":
                bot.send_message(message.chat.id, "There isn't any data to compare!")
            else:
                nam =nam.strip().split()
                if len(im_location)>0:
                        
                    
                    for img in im_location:
                        
                        top, right, bottom, left =img
                        
                        new_im =im[top:bottom, left:right]
                        pil_im =Image.fromarray(new_im)
                        
                        nor_im1 =np.array(pil_im)
                        current_state_2 =False
                        for i in nam:
                            i =i.strip()
                            
                            im2 =face_recognition.load_image_file(f"bot_folder/{i}")
                            im2_location =face_recognition.face_locations(im2)
                            if len(im2_location) >0:
                                try:
                                        
                                    im2_encoding =face_recognition.face_encodings(im2)[0]
                                    nor_im1_encoding =face_recognition.face_encodings(nor_im1)[0]
                                    p =face_recognition.compare_faces([im2_encoding], nor_im1_encoding)
                                    p =p[0]
                                    
                                    print("p: ", p)
                                except:
                                    p =False
                                    
                            else:
                                p =False
                            
                            
                            
                            
                            
                            # p =compare_faces(pil_im, f"bot_folder/{i}")                        
                            
                            if p =="Error1_encoding":
                                # bot.send_message(message.chat.id, "Error1_encoding. Weather img quality is unsatisfactfull or problem in identity module")
                                current_state_2 ="False1"
                                break
                            elif p:
                                # bot.send_message(message.chat.id, "This person exists in database")
                                current_state_2 =True                                                      
                                break
                            else:
                                current_state_2 =False
                        
                        if current_state_2 =="False1":
                            bot.send_photo(message.chat.id, pil_im)
                            bot.send_message(message.chat.id, "Error1_encoding. Weather img quality is unsatisfactfull or problem in identity module")

                        
                        elif current_state_2 ==True:
                            
                            info =""
                            bot.send_photo(message.chat.id, pil_im)
                            with open(f"bot_folder/{i}", "rb") as photo:
                                bot.send_photo(message.chat.id, photo)
                            
                            with open(f"bot_folder/{i}.txt") as f:
                                for i in f:
                                    i =i.strip()
                                    info +=str(i)+"\n"
                                
                            bot.send_message(message.chat.id, info)  
                        
                        else:
                            bot.send_photo(message.chat.id, pil_im)
                            bot.send_message(message.chat.id, "This person isn't in data")
                    bot.send_message(message.chat.id, "☑️Finished")
                else:
                    bot.send_message(message.chat.id, "There aren't any people in the img")
                        
       




# Handler for video messages
@bot.message_handler(content_types=['video'])
def main2(message):
    def compare_faces(message_1, message_2):
        try:
                
            im2 =face_recognition.load_image_file(message_2)
            im2_encodings =face_recognition.face_encodings(im2)[0]
            
            new_im_array1 = np.array(message_1) #for encoding cut faces
            im1_encoding =face_recognition.face_encodings(new_im_array1)[0]
            
            result =face_recognition.compare_faces([im1_encoding], im2_encodings)
            if result:
                pass
                # print("True was printed")
            else:
                pass
                # print("True was printed")
            print(result)
            return result[0]
        except:
            result =['Error1_encoding']
            print(result)
            return result[0]

         
        
        
    
    
    if message.video:
        
        video_folder =os.path.join(f"bot_folder","video_folder")
        if not os.path.exists(video_folder):
            os.mkdir(video_folder)
        
        
        if user_state.get(message.chat.id) == "waiting_for_video1":
            
        
            counter =os.path.join("bot_folder",'counter')
            if not os.path.exists("counter"):
                cur_state =False
                try:
                    with open(f"{counter}.txt") as f:
                        for i in f:
                            i =i.strip()
                            if i =="":
                                cur_state =True
                            else:
                                pass
                    
                    with open(f"{counter}.txt",'a') as f:
                        if cur_state ==True:
                            f.write("0")
                        else:
                            pass
                except:
                                    
                    with open(f"{counter}.txt",'a') as f:
                        f.write("0")
                            
            q =""
            con =int(0)
            nam =""
            with open(f"bot_folder/counter.txt") as f:
                for i in f:
                    i =i.strip()
                    q +=i
            
            
            with open(f"bot_folder/names.txt") as f:
                for i in f:
                    i =i.strip()
                    nam +=str(i)+"\n"
            
            
            
            for i in q:
                con +=int(i)
            
            
            
            video_nam =[]
            count_2 = 0
            bot.send_message(message.chat.id, "🔄Loading....")
            try:
                file_info = bot.get_file(message.video.file_id)
                file_path = file_info.file_path
        
                downloaded_file = bot.download_file(file_path)
        
                video_file_path = os.path.join(video_folder, f"{count_2}.mp4")
        
                # Save the video
                with open(video_file_path, 'wb') as video_file:
                    video_file.write(downloaded_file)
        
                cap = cv2.VideoCapture(video_file_path)
                
                if not cap.isOpened():
                    bot.send_message(message.chat.id, "[Error] Unable to open the video file.")
                    return
        
                known_face_encodings = []  # List to store known face encodings
        
                while True:
                    ret, frame = cap.read()
        
                    if not ret:
                        print("[Error] Can't get frame or end of video reached.")
                        break  # Exit the loop if no more frames
        
                    # Get the current frame ID
                    frame_id = int(round(cap.get(1)))
        
                    # Process every 100th frame
                    if frame_id % 100 == 0:
                        # Find all face locations in the current frame
                        face_locations = face_recognition.face_locations(frame)
        
                        if len(face_locations) > 0:
                            for face_location in face_locations:
                                # Get the face encoding for the current frame
                                face_encoding = face_recognition.face_encodings(frame, [face_location])[0]
        
                                # Check if the face has already been processed
                                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
                                if True not in matches:
                                    
                                    count_2 += 1
                                    video_nam.append(f"{count_2}_im.jpg")
                                    cv2.imwrite(f"bot_folder/video_folder/{count_2}_im.jpg", frame)
                                    print(f"New face recorded. Screenshot: {count_2}")
    
                                    # Add the new face encoding to known_face_encodings
                                    known_face_encodings.append(face_encoding)
        
                    # Optionally display the frame (remove if not needed in production)
                    cv2.imshow("frame", frame)
                    cv2.waitKey(1)  # Adjust delay if needed for smoother video
        
                # Release the video capture object and close windows
                cap.release()
                cv2.destroyAllWindows()
        
                bot.send_message(message.chat.id, "Video received and now it is in process!")
        
            except Exception as e:
                bot.send_message(message.chat.id, f"An error occurred: {e}")
            nam =nam.strip().split()
            print(video_nam)
            
            control_video =False
            print("names: ",nam)
            info =""

            for i in video_nam:                
                i =i.strip()
                print(i)
                file_path = f"bot_folder/video_folder/{i}"  # Create the file path
                cur_im =face_recognition.load_image_file(file_path)
                cur_im_location =face_recognition.face_locations(cur_im)
                
                for now_img in cur_im_location:
                    top, right, bottom, left =now_img
                                
                    new_im =cur_im[top:bottom, left:right]
                    pil_im =Image.fromarray(new_im)
                    # bot.send_photo(message.chat.id, pil_im)
                    nor_im1 =np.array(pil_im)
                    for j in nam:
                    
                        im2 =face_recognition.load_image_file(f"bot_folder/{j}")
                        im2_location =face_recognition.face_locations(im2)
                        if len(im2_location) >0:
                            try:
                                    
                                im2_encoding =face_recognition.face_encodings(im2)[0]
                                nor_im1_encoding =face_recognition.face_encodings(nor_im1)[0]
                                p =face_recognition.compare_faces([im2_encoding], nor_im1_encoding)
                                p =p[0]
                                
                                print("p: ", p)
                            except Exception as e:
                                print(e)
                        else:
                            p =False
                        
                        
                        
                        
                        # p =compare_faces(pil_im, f"bot_folder/{j}")
                        
                        if p =="Error1_encoding":
                            control_video ="False2"
                        elif p:
                            control_video =True
                            break
                        else:
                            control_video =False
                    
                    if control_video =="False2":
                        bot.send_photo(message.chat.id, pil_im)
                        bot.send_message(message.chat.id, "Error1_encoding. Weather img quality is unsatisfactfull or problem in identity module")

                    elif control_video:
                        # bot.send_photo(message.chat.id, open(f"bot_folder/video_folder/{i}", 'rb'))  # Open the image file
                        bot.send_photo(message.chat.id, pil_im)
                        bot.send_photo(message.chat.id, open(f"bot_folder/{j}", 'rb'))  # Open the image file
                        print("j: ",j)
                        print(i)

                        with open(f"bot_folder/{j}.txt") as f:
                            for q in f:
                                q =q.strip()
                                info +=q+"\n"
                        
                        bot.send_message(message.chat.id, info)
                        info =""
                    
                    else:
                        # bot.send_photo(message.chat.id, open(f"bot_folder/video_folder/{i}", 'rb'))  # Open the image file
                        bot.send_photo(message.chat.id, pil_im)
                        bot.send_message(message.chat.id, "Non identified person")
                        

                                        
                
                
            #     for j in nam:
            #         p =comp_faces(f"{file_path}", f"bot_folder/{j}")
                    
            #         if p:
            #             control_video =True
            #             break
            #         else:
            #             control_video =False
            #     if p:
            #         bot.send_photo(message.chat.id, open(file_path, 'rb'))
            #         bot.send_photo(message.chat.id, open(f"bot_folder/{j}", "rb"))

            #         with open(f"bot_folder/{j}.txt") as f:
            #             for t in f:
            #                 info +=t
            #     else:
            #         bot.send_photo(message.chat.id, open(file_path, 'rb'))
            #         bot.send_message(message.chat.id, "Unidentified person(s)")

            # if info.strip() =="":
            #     pass
            # else:
                    
            #     bot.send_message(message.chat.id, info)
                        
            bot.send_message(message.chat.id, "☑️Finished")
                
                
                






bot.polling(none_stop=True)








