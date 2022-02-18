from PIL import Image, ImageDraw
import face_recognition
import numpy as np

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("obama.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
im = Image.new('RGB', (800, 800), (255, 255, 255))

def positionShift(originalList,x,y):
    #returnList
    newList = np.array(originalList)
    movement = np.array([x,y])
    newList = np.add(newList,movement)
    newList = tuple(map(tuple, newList))
    ((2, 2), (2, -2))
    return newList


for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(im, 'RGBA')

    #move the evebrow +(6,2)
    shiftedLeft_eyebrow = positionShift(face_landmarks['left_eyebrow'],6,2)
    shiftedRight_eyebrow = positionShift(face_landmarks['right_eyebrow'],6,2)
    #draw the yellow shadow of eyebrows
    d.line(shiftedLeft_eyebrow, fill=(255, 247, 64, 1000), width=5)
    d.line(shiftedRight_eyebrow, fill=(255, 247, 64, 1000), width=5)
    #draw the eyebrows
    d.line(face_landmarks['left_eyebrow'], fill=(255, 67, 67, 1000), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(255, 67, 67, 1000), width=5)

    #move the eyes
    left_eyelist = face_landmarks['left_eye']
    right_eyelist = face_landmarks['right_eye']
    shiftedLeft_eyes = positionShift(left_eyelist,6,4)
    shiftedRight_eyes = positionShift(right_eyelist,6,4)
    # Draw the eye shadows
    shiftedLeft_iris = shiftedLeft_eyes[1] + shiftedLeft_eyes[2] + shiftedLeft_eyes[4] + shiftedLeft_eyes[5]
    shiftedRight_iris = shiftedRight_eyes[1] + shiftedRight_eyes[2] + shiftedRight_eyes[4] + shiftedRight_eyes[5]
    d.polygon(shiftedLeft_iris, fill=(255, 90, 67, 1000))
    d.polygon(shiftedRight_iris, fill=(255, 90, 67, 1000))
    d.line(shiftedLeft_eyes + (shiftedLeft_eyes[0]), fill=(255, 90, 67, 1000), width=5)
    d.line(shiftedRight_eyes + (shiftedRight_eyes[0]), fill=(255, 90, 67, 1000), width=5)
    # Draw the eyes
    left_iris = left_eyelist[1] + left_eyelist[2] + left_eyelist[4] + left_eyelist[5]
    right_iris = right_eyelist[1] + right_eyelist[2] + right_eyelist[4] + right_eyelist[5]
    d.polygon(left_iris, fill=(0, 46, 210, 1000))
    d.polygon(right_iris, fill=(0, 46, 210, 1000))
    d.line(left_eyelist + [left_eyelist[0]], fill=(0, 46, 210, 1000), width=5)
    d.line(right_eyelist + [right_eyelist[0]], fill=(0, 46, 210, 1000), width=5)
  
    #Draw the nose shadow
    shadow_List_nose = [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_tip'][0]] + [face_landmarks['nose_tip'][4]] 
    tip_list_nose = [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_tip'][0]] + [face_landmarks['nose_tip'][4]] + [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_bridge'][3]] + [face_landmarks['nose_tip'][4]]
    shadow_List_nose = positionShift(shadow_List_nose,8,5)
    d.polygon(shadow_List_nose, fill=(255, 247, 64, 1000))
    d.line(tip_list_nose, fill=(0, 46, 210, 1000), width=5)


    # Gloss the lips
    #d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    #d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(0, 46, 210, 1000), width=5)
    d.line(face_landmarks['bottom_lip'], fill=(0, 46, 210, 1000), width=5)
    
    #  for facial_feature in face_landmarks.keys():
    #     print(facial_feature)
    #     for i in face_landmarks[facial_feature]:
    #         print ("序号：%s   值：%s" % (face_landmarks[facial_feature].index(i), i))
    

    # draw the chin
    list_chin = [face_landmarks['chin'][0]] + [face_landmarks['chin'][5]] + [face_landmarks['chin'][7]] + [face_landmarks['chin'][9]] + [face_landmarks['chin'][11]] + [face_landmarks['chin'][16]]
    d.line(list_chin, fill=(0, 46, 210, 1000), width=5)

#    pil_image.show()
    display(im)
