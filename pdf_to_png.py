from wand.image import Image as Img
import os



path = r'C:\Users\v119615\PycharmProjects\Text_Mining\data'
def search_dir(path):
    path_file = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                path_file.append(os.path.join(root,file))
    print(path_file)


def pdf2png(pdf):
    pdf = search_dir(path)
    with Img(filename=pdf, resolution=300) as img:
        img.compression_quality = 99
        return img.save(filename='test.tif')

print(pdf2png(pdf))

for i in path_file:
    print(i)
