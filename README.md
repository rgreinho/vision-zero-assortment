# vision-zero-assortment

An assortment of tools that were used in vision zero related campaigns

## Goal

This is a mono repo of tools/scripts that were created to help with some Vision Zero
related campaigns.

Most of the tools are a one-off type of deal, therefore the quality of the code/projects
is probably not optimal. However it did work for a campaign, and probably still has a
few cool ideas that can be reused, therefore is probably worth sharing.

## Conventions

### Python

* All the Python projects are managed with [Poetry](https://python-poetry.org/).
  * Each project must create a local virtual environment at its root
    ```bash
    poetry config virtualenvs.in-project true --local
    ```
* Scripts **WITHOUT** dependencies can be dropped in as is.
* Libraries:
  * CLI: [click](https://click.palletsprojects.com/en/7.x/)
  * HTTP client: [aiohttp](https://aiohttp.readthedocs.io/en/stable/)
  * Logging: [loguru](https://github.com/Delgan/loguru)
  * Retry: [tenacity](https://tenacity.readthedocs.io/en/latest/)

## Weird stuff

For some weird reason, it looks like poetry does not install all the deps in my venv,
therefore I have to add them manually:

```bash
source .venv/bin/activate
pip install -U pip
pip install -r <(poetry export -f requirements.txt --dev)
```
