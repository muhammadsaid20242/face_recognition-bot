# face_recognition
Face identity bot
1)Commands

/start -This command is to start the program. As the user sends start command bot will create 'bot_folder' in the path(os) where the code is running. And alse two txt documents will be created. (names, counter). name is for saving the names of new images. counter is used as a part of name not to resave image by deleting the previous one 

/all_data -This command is to get all datas. As the bot_folder is created. Bot will open names.txt and collect datas to a vareble called nam. If nam is empty bot will send message as  there is no dara else: the datas will be sent.

2)bottons
register -This botton is to register a person by sending the photo

photo -This botton is for sending the photo. As the moment this botton is sent the user_state dictionary is named as waiting_for_pic1 and waits for photo to be sent. Bot opens names and counter documents that are created by bot and used as a data. And as the photo is sent bot will identify how many faces in the image with face_recognition library. First bot will check weather this person in data or not. if yes bot notifies user that this person is in data else bot creates txt document by the name of image, ex({con}_im.jpg.txt)  bot  creates new vareble as cur_nams and  saves the face parts and gives name by changing only number part as ({con}_im.jpg) con is the number, and presents describe botton. 

describe -This botton is for describing the person. As the description is sent bot will open previously created txt docum and writes description and saves.

back -This botton opens main page

search -This botton is for searching and provides tho options as a botton. Picture and video

Picture -This botton is used to receive the photo, detects faces from the image that is sent by user and compares from data. if true sends datas of that person else sends face part of the person that is cut from givden photo and notifies user that this person isn't is data

Video -This botton is used for receivind video. As video received bot will creat video_folder in the bot_folder and saves the given video. The size mustn't be more than 30mb. It is telebot's limitation. once the video is saved bot notifies user that video is saved and it is in proccess. With cv2 library the video is played and taked frame_id if the number of frame(images that are taken from video) is devisible by 100 with no reminder so it will chack weather there is a face or faces in the image if yes, bot saves that frame else continiuos to play the video




