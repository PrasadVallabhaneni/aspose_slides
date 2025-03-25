import aspose.slides as slides
from config import NUM_TO_ALPHA
import aspose.pydrawing as drawing

def replace_text_numbers(slide):
    for shape in slide.shapes:
        if isinstance(shape, slides.AutoShape) and shape.text_frame:
            text = shape.text_frame.text.strip()
            if text in NUM_TO_ALPHA:
                shape.text_frame.text = NUM_TO_ALPHA[text]

def change_header_color(slide):
    for shape in slide.shapes:
        if isinstance(shape, slides.AutoShape) and shape.text_frame and shape.text_frame.text.strip():
            for paragraph in shape.text_frame.paragraphs:
                for portion in paragraph.portions:
                    portion.portion_format.fill_format.fill_type = slides.FillType.SOLID
                    portion.portion_format.fill_format.solid_fill_color.color = drawing.Color.blue
            break  