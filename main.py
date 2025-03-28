import aspose.slides as slides
from config import PPTX_PATH, OUTPUT_PATH, CAR_IMAGE_PATH
from utils.image_utils import replace_slide_image
from utils.text_utils import replace_text_numbers,change_header_color
from utils.table_utils import update_table_header_color
from utils.chart_utils import update_chart_colors

with slides.Presentation(PPTX_PATH) as presentation:
    
    #slide 1 changes - replacing image with car, numbers to alphabatical
    slide1 = presentation.slides[0]
    replace_slide_image(slide1, CAR_IMAGE_PATH, presentation)
    replace_text_numbers(slide1)

    #slide 2 changes - update table header color from 2 - 7 columns as first column color
    slide2 = presentation.slides[1]
    update_table_header_color(slide2)

    #slide 3 changes - change title color and chart graph color
    slide3 = presentation.slides[2]
    change_header_color(slide3)
    update_chart_colors(slide3)
    

    presentation.save(OUTPUT_PATH, slides.export.SaveFormat.PPTX)

