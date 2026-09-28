# career-platform

## Install dependencies
1. Install uv
  `pip install uv`

1. install dependency
  `uv sync`


## Run tests
`uv run pytest`

## Run the application
`uv run uvicorn --app-dir src career_platform.main:app --reload`