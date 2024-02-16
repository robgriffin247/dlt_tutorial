import dlt

from dlt.sources.helpers import requests

url = "https://api.github.com/repos/dlt-hub/dlt/issues"

response = requests.get(url)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="github_issues",
    destination="duckdb",
    dataset_name="github_data",
)

load_info = pipeline.run(response.json(), 
                         table_name="issues",
                         write_disposition="replace")

print(load_info)