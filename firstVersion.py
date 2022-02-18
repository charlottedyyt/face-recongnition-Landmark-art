from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("fbb.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
im = Image.new('RGB', (800, 800), (255, 255, 255))
for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Make the eyebrows into a nightmare
    #d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
    #d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(0,0,0), width=4)
    d.line(face_landmarks['right_eyebrow'], fill=(0,0,0), width=4)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(255,0,0,50))
    d.polygon(face_landmarks['bottom_lip'], fill=(255,0,0,50))
    d.line(face_landmarks['top_lip'], fill=(0,0,0), width=4)
    d.line(face_landmarks['bottom_lip'], fill=(0,0,0), width=4)

    # Draw the noses
   # d.polygon(face_landmarks['nose_bridge'], fill=(150, 0, 0, 128))
    #d.polygon(face_landmarks['nose_tip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['nose_bridge'], fill=(0,0,0), width=4)
    d.line(face_landmarks['nose_tip'], fill=(0,0,0), width=4)

    # Sparkle the eyes
   # d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
   # d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]],fill=(0,0,0), width=4)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]],fill=(0,0,0), width=4)

    # draw the chin
   
    d.line(face_landmarks['chin'], fill=(0,0,0), width=4)

    pil_image.show()

    display(pil_image)
    #display(im)