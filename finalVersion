from PIL import Image, ImageDraw
import face_recognition
import numpy as np

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("obama.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
im = Image.new('RGBA', (800, 800), (255, 255, 255,0))

#colors

#blue-yellow-red
lines1 = (0, 46, 210, 1000)
shadow1 = (255, 247, 64, 1000)
shadoweye1 = (255, 90, 67, 1000)
lipAeb1 = (255, 67, 67, 1000)
#purple-blue-pink
lines2 = (67, 0, 210, 1000)
shadow2 = (255, 64, 190, 1000)
shadoweye2 = (67, 244, 255, 1000)
lipAeb2 = (67, 221, 255, 1000)
#black-green-green
lines3 = (0, 0, 0, 1000)
shadow3 = (130, 255, 86, 1000)
shadoweye3 = (214, 255, 97, 1000)
lipAeb3 = (26, 130, 0, 1000)
#violet-yellow-green
lines4 = (116, 82, 254, 1000)
shadow4 = (255, 231, 14, 1000)
shadoweye4 = (0, 0, 0, 1000)
lipAeb4 = (69, 233, 76, 1000)

linesColor = lines1
shadowColor = shadow1
shadoweyeColor = shadoweye1
lipAebColor = lipAeb1

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
    d.line(shiftedLeft_eyebrow, fill=shadowColor, width=5)
    d.line(shiftedRight_eyebrow, fill=shadowColor, width=5)
    #draw the eyebrows
    d.line(face_landmarks['left_eyebrow'], fill=lipAebColor, width=5)
    d.line(face_landmarks['right_eyebrow'], fill=lipAebColor, width=5)

    #move the eyes
    left_eyelist = face_landmarks['left_eye']
    right_eyelist = face_landmarks['right_eye']
    shiftedLeft_eyes = positionShift(left_eyelist,6,4)
    shiftedRight_eyes = positionShift(right_eyelist,6,4)
    # Draw the eye shadows
    shiftedLeft_iris = shiftedLeft_eyes[1] + shiftedLeft_eyes[2] + shiftedLeft_eyes[4] + shiftedLeft_eyes[5]
    shiftedRight_iris = shiftedRight_eyes[1] + shiftedRight_eyes[2] + shiftedRight_eyes[4] + shiftedRight_eyes[5]
    d.polygon(shiftedLeft_iris, fill=shadoweyeColor)
    d.polygon(shiftedRight_iris, fill=shadoweyeColor)
    d.line(shiftedLeft_eyes + (shiftedLeft_eyes[0]), fill=shadoweyeColor, width=5)
    d.line(shiftedRight_eyes + (shiftedRight_eyes[0]), fill=shadoweyeColor, width=5)
    # Draw the eyes
    left_iris = left_eyelist[1] + left_eyelist[2] + left_eyelist[4] + left_eyelist[5]
    right_iris = right_eyelist[1] + right_eyelist[2] + right_eyelist[4] + right_eyelist[5]
    d.polygon(left_iris, fill=linesColor)
    d.polygon(right_iris, fill=linesColor)
    d.line(left_eyelist + [left_eyelist[0]], fill=linesColor, width=5)
    d.line(right_eyelist + [right_eyelist[0]], fill=linesColor, width=5)
  
    #Draw the nose shadow
    shadow_List_nose = [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_tip'][0]] + [face_landmarks['nose_tip'][4]] 
    tip_list_nose = [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_tip'][0]] + [face_landmarks['nose_tip'][4]] + [face_landmarks['nose_bridge'][0]] + [face_landmarks['nose_bridge'][3]] + [face_landmarks['nose_tip'][4]]
    shadow_List_nose = positionShift(shadow_List_nose,8,5)
    d.polygon(shadow_List_nose, fill=shadowColor)
    d.line(tip_list_nose, fill=linesColor, width=5)


    # Draw the lips shadow
    top_lip_list = [face_landmarks['top_lip'][0]] + [face_landmarks['top_lip'][2]] + [face_landmarks['top_lip'][3]] + [face_landmarks['top_lip'][4]] + [face_landmarks['top_lip'][6]] + [face_landmarks['top_lip'][8]] + [face_landmarks['top_lip'][9]] + [face_landmarks['top_lip'][10]] + [face_landmarks['top_lip'][0]] 
    bottom_lip_list = [face_landmarks['bottom_lip'][0]] + [face_landmarks['bottom_lip'][2]] + [face_landmarks['bottom_lip'][4]] + [face_landmarks['bottom_lip'][6]] + [face_landmarks['bottom_lip'][8]] + [face_landmarks['bottom_lip'][10]] + [face_landmarks['bottom_lip'][0]] 
    shifted_top_lip_list = positionShift(top_lip_list,3,4)
    shifted_bottom_lip_list = positionShift(bottom_lip_list,3,4)
    d.polygon(shifted_top_lip_list, fill=lipAebColor)
    d.polygon(shifted_bottom_lip_list, fill=lipAebColor)
    d.line(top_lip_list, fill=linesColor, width=5)
    d.line(bottom_lip_list, fill=linesColor, width=5)

    # draw the chin
    list_chin = [face_landmarks['chin'][0]] + [face_landmarks['chin'][5]] + [face_landmarks['chin'][7]] + [face_landmarks['chin'][9]] + [face_landmarks['chin'][11]] + [face_landmarks['chin'][16]]
    d.line(list_chin, fill=linesColor, width=5)

#    pil_image.show()
    display(im)
