from PIL import Image
cover = Image.open('ptu8_library/library/static/library/img/default_cover.jpg')
crop_box = (0, 333//2 - 217//2, 217, 333//2 - 217//2 + 217)
print(crop_box)
thumb_cover = cover.crop(crop_box)
thumb_cover.save('ptu8_library/library/static/library/img/default_cover_square.png')
