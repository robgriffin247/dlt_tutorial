# [dlt Tutorial](https://dlthub.com/docs/tutorial/intro)

1. Basic setup of working environment to setup git, github and poetry

```{bash}
mkdir dlt_tutorial
cd dlt_tutorial

echo "# dlt tutorial" >> README.md
poetry init

git init
git add .
git commit -m "initial commit"
git remote add origin git@github.com:[username]/[repo]
git branch -M main
git push -u origin main
```

#### Setup 

1. Install dependencies

```{bash}
poetry add dlt
poetry add duckdb
poetry add pandas
poetry add streamlit
```

#### First pipeline

1. Create a pipeline called `github_issues.py`

```{python}
import dlt
from dlt.sources.helpers import requests

# Specify the URL of the API endpoint
url = "https://api.github.com/repos/dlt-hub/dlt/issues"
# Make a request and check if it was successful
response = requests.get(url)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="github_issues",
    destination="duckdb",
    dataset_name="github_data",
)
# The response contains a list of issues
load_info = pipeline.run(response.json(), table_name="issues")

print(load_info)
```

1. Run the pipeline to load the data

```{bash}
python github_issues.py
```

1. View the data 

```{bash}
dlt pipeline github_issues show
```

1. Open link in browser (quit with *ctrl* + *c* in the terminal)

#### Append or replace

Rerunning the above pipeline will append the same data to the old data. This can be avoided by adding `write_disposition="replace"` to the `pipeline.run()` statement.
