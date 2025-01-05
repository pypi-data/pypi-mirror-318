import aiohttp_jinja2
from aiohttp import web

import colvert.ui.charts

routes = web.RouteTableDef()

@routes.get("/")
@aiohttp_jinja2.template("index.html.j2")
async def index(request) -> dict[str, str]:
    query = request.query.get("q", "")
    if query == "":
        tables = await request.app["db"].tables()
        if len(tables) > 0:
            first_table = tables[0]
            query = f"SELECT *\nFROM {first_table}\nLIMIT 10"
        else:
            query = "CREATE TABLE t1 (id INTEGER PRIMARY KEY, j VARCHAR)"

    # Get the list of all available chart types sorted by name with Table as the first entry
    charts = []
    for chart in colvert.ui.charts.get_all():
        if chart.__qualname__ != "Table":
            charts.append((chart.__qualname__.lower(), chart.title, ))
    charts.sort(key=lambda x: x[1])
    charts.insert(0, ("table", "Table", ))

    return {
        "query": query,
        "charts": charts, # type: ignore
    }



@routes.get("/tables")
@aiohttp_jinja2.template(template_name="tables.html.j2")
async def tables(request):
    tables = []
    for table in await request.app["db"].tables():
        tables.append({
            "name": table,
            "columns": await request.app["db"].describe(table),
        })
    return {
        "tables": tables,
    }