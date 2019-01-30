from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("faces2.jpg")

# Find all facial features in all the faces in the image

face_locations = face_recognition.face_locations(image)
#face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image, 'RGBA')

for face in face_locations:

    d.rectangle( [face[1],face[0],face[3],face[2]]) 

pil_image.show()
