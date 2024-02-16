import dlt
from dlt.sources.helpers import requests

@dlt.resource(
    table_name="raw_planets",
    write_disposition="merge",
    primary_key="title"
)
def get_planets():
    url = "https://swapi.dev/api/planets/?page=1"
    while True:
        response = requests.get(url)
        response.raise_for_status()
        yield response.json()["results"]
        print('Data ingested from ' + url)

        if response.json()["next"] == None:
            break
        url = response.json()["next"]


pipeline = dlt.pipeline(
    pipeline_name="swapi_pipeline",
    destination="duckdb",
    dataset_name="swapi_raw"
)

load_info = pipeline.run(get_planets)

print(load_info)