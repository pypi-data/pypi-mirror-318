import pandas
import plotly.express as px

from .base import Base, Result
from .types import (
    OptionTypeInt,
    OptionTypeResultColumn,
    OptionTypeSelect,
    OptionTypeString,
)

IGNORE_COLUMNS = ["latitude", "longitude", "lat", "lon"]


class ScatterMap(Base):
    limit = 100000
    example = "SELECT latitude,longitude, column FROM table"
    title = "Scatter Map"
    patterns = [
        ["..."],
    ]
    options = [
        OptionTypeString("title", "Title"),
        OptionTypeResultColumn("size", "Size", ignore_columns=IGNORE_COLUMNS),
        OptionTypeResultColumn("color", "Color", ignore_columns=IGNORE_COLUMNS),
        OptionTypeSelect(
            "map_style",
            "Map Style",
            choices=[
                "basic",
                "carto-darkmatter",
                "carto-darkmatter-nolabels",
                "carto-positron",
                "carto-positron-nolabels",
                "carto-voyager",
                "carto-voyager-nolabels",
                "dark",
                "light",
                "open-street-map",
                "outdoors",
                "satellite",
                "satellite-streets",
                "streets",
                "white-bg",
            ],
            default="basic",
        ),
        OptionTypeInt(
            "zoom",
            "Zoom",
            min=1,
            max=20,
            default=1,
        ),
    ]

    def _get_longitude(self, result) -> str:
        for colum in result.column_names:
            if colum.lower() == "longitude" or colum.lower() == "long":
                return colum
        raise ValueError("Missing longitude column")

    def _get_latitude(self, result) -> str:
        for colum in result.column_names:
            if colum.lower() == "latitude" or colum.lower() == "lat":
                return colum
        raise ValueError("Missing latitude column")

    def _render_options(self, result: Result):
        options = {
            "zoom": 1,
            "lat": self._get_latitude(result),
            "lon": self._get_longitude(result),
        }
        options.update(**self.user_options)
        return options

    async def render(self, result: Result, df: pandas.DataFrame) -> str:
        options = self._render_options(result)
        fig = px.scatter_map(df, **options)
        return await self.render_px(fig)
