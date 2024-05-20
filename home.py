import face_recognition
import streamlit as st
import os
from PIL import Image

st.header("Face recognition")

#upload iamge
# Load the jpg files into numpy arrays
#st.write("Loading the jpg files into numpy arrays")
#biden_image = face_recognition.load_image_file("data/photo_biden.jpg")
#obama_image = face_recognition.load_image_file("data/photo_obama.jpg")

known_images=[]
unknown_images=[]
know_encoding=[]
unknown_encoding=[]
result_list=[]

start=st.button("start")
if start:
    path_known="/Users/yassir2/code/Yassirbenj/face recognition/data/known"
    os.chdir(path_known)
    try:
        for file in os.listdir():
            if file.endswith(".jpg"):
                file_path = f"{path_known}/{file}"
                #st.write(file_path)
                image=face_recognition.load_image_file(file_path)
                known_images.append(image)
                result_list.append({"name":file,"unknown":[]})
                image_encoding=face_recognition.face_encodings(image)[0]
                know_encoding.append(image_encoding)
    except IndexError:
        st.write("I wasn't able to locate any faces in at least one of the known images. Check the image files. Aborting...")
        quit()

    #st.write(know_encoding)

    path_unknown="/Users/yassir2/code/Yassirbenj/face recognition/data/unknown"
    os.chdir(path_unknown)
    try:
        for file in os.listdir():
            filename=file
            #st.write(filename)
            if file.endswith(".jpg"):
                file_path = f"{path_unknown}/{filename}"
                #st.write(file_path)
                image=face_recognition.load_image_file(file_path)
                image_encoding=face_recognition.face_encodings(image)
                #st.write(image_encoding)
                for unknown_face in image_encoding:
                #    st.write(unknown_face)
                #   st.write(know_encoding["image"])
                    results = face_recognition.compare_faces(know_encoding, unknown_face)
                    for i,element in enumerate(results):
                        if element==True:
                             result_list[i]["unknown"].append(file)

        for item in result_list:
            st.write(item["name"])
            for photo in item['unknown']:
                img_path=f"/Users/yassir2/code/Yassirbenj/face recognition/data/unknown/{photo}"
                st.image(img_path)

    except IndexError:
        st.write("I wasn't able to locate any faces in at least one of the uknown images. Check the image files. Aborting...")
        quit()
