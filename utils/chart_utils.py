import aspose.slides as slides
from aspose.slides import FillType
import aspose.pydrawing as drawing
from config import TARGET_CHART_COLOR, NEW_CHART_COLOR

def update_chart_colors(slide):
    for shape in slide.shapes:
        if hasattr(shape, "chart"):
            chart = shape.chart
            for series in chart.chart_data.series:
                color = series.format.fill.solid_fill_color.color
                if color == drawing.Color.from_argb(255, *TARGET_CHART_COLOR):
                    series.format.fill.solid_fill_color.color = drawing.Color.from_argb(255, *NEW_CHART_COLOR)
