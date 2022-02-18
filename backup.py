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
    #del my_list[1:5]

    #position movement
  #  left_eyebrowArray = np.array(face_landmarks['left_eyebrow'])
  #  right_eyebrowArray = np.array(face_landmarks['right_eyebrow'])
  #  left_eyeArray = np.array(face_landmarks['left_eye'])
  #  right_eyeArray = np.array(face_landmarks['right_eye'])

    #move the evebrow +(6,2)
    shiftEyebrow = np.array([6,2])
    shiftedLeft_eyebrow = np.add(left_eyebrowArray,shiftEyebrow)
    shiftedRight_eyebrow = np.add(right_eyebrowArray,shiftEyebrow)
    shiftedLeft_eye = np.add(left_eyeArray,shiftEyebrow)
    shiftedRight_eye = np.add(right_eyeArray,shiftEyebrow)
    #
    shiftedLeftIris = shiftedLeft_eye
    shiftedRightIris = shiftedRight_eye
    del leftIris[0]
    del leftIris[2]
    del rightIris[0]
    del rightIris[2]
    #convert to tuple
    shiftedLeft_eye = tuple(map(tuple, shiftedLeft_eye))
    ((2, 2), (2, -2))
    shiftedRight_eye = tuple(map(tuple, shiftedRight_eye))
    ((2, 2), (2, -2))
    shiftedLeft_eyebrow = tuple(map(tuple, shiftedLeft_eyebrow))
    ((2, 2), (2, -2))
    shiftedRight_eyebrow = tuple(map(tuple, shiftedRight_eyebrow))
    ((2, 2), (2, -2))


    #draw the yellow shadow of eyebrows
    d.line(shiftedLeft_eyebrow, fill=(255, 247, 64, 1000), width=5)
    d.line(shiftedRight_eyebrow, fill=(255, 247, 64, 1000), width=5)
    #draw the eyebrows
    d.line(face_landmarks['left_eyebrow'], fill=(255, 67, 67, 1000), width=5)
    d.line(face_landmarks['right_eyebrow'], fill=(255, 67, 67, 1000), width=5)

    # Draw the eye shadows

    #draw iris
    d.polygon(leftIris, fill=(255, 90, 67, 1000))
    d.polygon(leftIris, fill=(255, 90, 67, 1000))
    
    d.line(shiftedLeft_eye + [shiftedLeft_eye[0]], fill=(255, 90, 67, 1000), width=5)
    d.line(shiftedRight_eye + [shiftedRight_eye[0]], fill=(255, 90, 67, 1000), width=5)
    
    #Draw the eyes
    leftIris = face_landmarks['left_eye']
    rightIris = face_landmarks['right_eye']
    del leftIris[0]
    del leftIris[2]
    del rightIris[0]
    del rightIris[2]
    d.polygon(leftIris, fill=(0, 46, 210, 1000))
    d.polygon(leftIris, fill=(0, 46, 210, 1000))
    
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 46, 210, 1000), width=5)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 46, 210, 1000), width=5)
 


    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=1)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=1)

    # Gloss the lips
    #d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    #d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=2)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=2)
    
    #  for facial_feature in face_landmarks.keys():
    #     print(facial_feature)
    #     for i in face_landmarks[facial_feature]:
    #         print ("序号：%s   值：%s" % (face_landmarks[facial_feature].index(i), i))
    

    # Draw the noses
   # d.polygon(face_landmarks['nose_bridge'], fill=(150, 0, 0, 128))
    #d.polygon(face_landmarks['nose_tip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['nose_bridge'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['nose_tip'], fill=(150, 0, 0, 64), width=8)


    # draw the chin
    d.polygon(face_landmarks['chin'], fill=(255, 255, 255, 30))
    d.line(face_landmarks['chin'], fill=(150, 0, 0, 64), width=8)

#    pil_image.show()
    display(im)
