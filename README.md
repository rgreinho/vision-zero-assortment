# vision-zero-assortment
An assortment of tools that were used in vision zero related campaigns

## Goal

This is a mono repo of tools/scripts that were created to help with some Vision Zero related campaigns.

Most of the tools are a one-off type of deal, therefore the quality of the code/project is probably not optimal. However it did work for a campaign, and probably still has a few cool ideas that can be reused.

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
