import cv2
import numpy as np
import face_recognition 

def training_old_face(): #id = id phong
    #------get face from folder images
    training_image_file = './esp-img/20230819234147.jpg'
    img_modi=face_recognition.load_image_file(training_image_file)
    img_modi = cv2.cvtColor(img_modi,cv2.COLOR_BGR2RGB)
    
    #------to find the face location
    face = face_recognition.face_locations(img_modi)[0]
    
    #------draw the face
    ##cv2.rectangle(img_modi, (face[3], face[0]),(face[1], face[2]), (255,0,255), 1)
    ##cv2.imshow('img_modi', img_modi)
    #cv2.waitKey(0)

    #--Converting image into encodings
    train_encode = face_recognition.face_encodings(img_modi)[0]
    
    return train_encode
    
    
def is_valid_face(): #id = id phong, # file = file cua esp
##compare_image_file = './static/tuyen.jpg'
    compare_image_file = './static/uyen.jpg'
    #----- lets test an image
    test = face_recognition.load_image_file(compare_image_file)
    test = cv2.cvtColor(test, cv2.COLOR_BGR2RGB)
    test_encode = face_recognition.face_encodings(test)[0]
    return (face_recognition.compare_faces([training_old_face()],test_encode))
    


