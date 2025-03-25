import aspose.slides as slides

def replace_slide_image(slide, image_path, presentation):
    with open(image_path, "rb") as img_stream:
        new_image = presentation.images.add_image(img_stream)
        for shape in slide.shapes:
            if isinstance(shape, slides.PictureFrame):
                shape.picture_format.picture.image = new_image
                return True
    return False
