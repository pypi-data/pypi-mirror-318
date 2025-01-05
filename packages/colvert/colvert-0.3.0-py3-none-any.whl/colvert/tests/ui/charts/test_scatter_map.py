
import pytest

from ....ui.charts import ScatterMap


@pytest.mark.asyncio
async def test_render_scatter_map(get_request, sample_db):
    result = await sample_db.sql("SELECT Latitude,Longitude,\"First Name\" FROM test")
    response = await ScatterMap(get_request, result, {}).build()
    assert "plotly-graph-div" in response



@pytest.mark.asyncio
async def test_render_options(get_request, sample_db):
    result = await sample_db.sql("SELECT Latitude,Longitude as longitude,\"First Name\" FROM test")
    scatter =  ScatterMap(get_request, result, {})
    options = scatter._render_options(result)
    assert options == {
        "zoom": 1,
        "lat": "Latitude",
        "lon": "longitude",
        "map_style": "basic",
    }

@pytest.mark.asyncio
async def test_render_options_short(get_request, sample_db):
    result = await sample_db.sql("SELECT Latitude as LAT,Longitude as long,\"First Name\" FROM test")
    scatter =  ScatterMap(get_request, result, {})
    options = scatter._render_options(result)
    assert options == {
        "zoom": 1,
        "lat": "LAT",
        "lon": "long",
        "map_style": "basic",
    }


@pytest.mark.asyncio
async def test_render_options_missing_latitude(get_request, sample_db):
    result = await sample_db.sql("SELECT \"First Name\" FROM test")
    scatter =  ScatterMap(get_request, result, {})
    with pytest.raises(ValueError):
        scatter._render_options(result)

