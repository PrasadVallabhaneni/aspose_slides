import aspose.slides as slides
from aspose.slides import FillType

def update_table_header_color(slide):
    for shape in slide.shapes:
        if isinstance(shape, slides.Table):
            first_col_color = shape.rows[0][0].cell_format.fill_format.solid_fill_color.color
            for col in range(1, 7):  
                shape.rows[0][col].cell_format.fill_format.fill_type = FillType.SOLID
                shape.rows[0][col].cell_format.fill_format.solid_fill_color.color = first_col_color
