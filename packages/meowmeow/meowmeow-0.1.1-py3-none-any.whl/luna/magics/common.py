from __future__ import print_function

import functools
import logging

import pandas as pd
from attrs import define
from google import auth
from google.auth.credentials import Credentials
from google.cloud import bigquery
from google.cloud.bigquery_storage import BigQueryReadClient
from sqlalchemy.engine import Engine

from ..utils.bigquery.tracker import ProgressTracker, TqdmTracker

log = logging.getLogger(__name__)


@functools.lru_cache(maxsize=None)
def get_bqstorage_client(client: bigquery.Client) -> BigQueryReadClient:
    log.debug("creating bq storage client")
    from google.api_core.gapic_v1 import client_info as gapic_client_info

    return client._ensure_bqstorage_client(
        client_info=gapic_client_info.ClientInfo(user_agent="xpkgs"),
    )


@functools.lru_cache(maxsize=None)
def get_bigquery_client(*args, **kwargs):
    bqclient = bigquery.Client(*args, **kwargs)
    log.debug("created bq client for %s", bqclient.project)
    return bqclient


@functools.lru_cache(maxsize=None)
def get_default_credentials():
    log.debug("getting default credentials")
    credentials, project = auth.default()
    return credentials, project


_current_pandas_max_rows_shown = 5


# def show_dataframe(df: pd.DataFrame, max_rows: int = 5):
#     global _current_pandas_max_rows_shown
#     _current_pandas_max_rows_shown = pd.options.display.max_rows
#     pd.options.display.max_rows = max(pd.options.display.max_rows, max_rows) + 10
#     return df.head(max_rows)


# def reset():
#     pd.options.display.max_rows = _current_pandas_max_rows_shown


@define(slots=False)
class _MagicsContext:
    project: str = None
    dataset: str = None
    credentials: Credentials = None
    tracker: ProgressTracker = TqdmTracker()

    # sqlx
    engine: Engine = None

    # copy
    max_rows_copy: int = 2 << 9

    def copy(self) -> "_MagicsContext":
        return _MagicsContext(**vars(self))


bq_ctx = _MagicsContext()


def copy_dataframe(df: pd.DataFrame, max_rows: int = 1000):
    if df.shape[0] > max_rows:
        log.warning(
            "dataframe has %s rows - copying only %s rows to clipboard",
            df.shape[0],
            max_rows,
        )
    df.iloc[:max_rows, :].to_clipboard()


# def prepare_clients(project: str = None, tracker=None):
#     project = project or bq_ctx.project
#     assert project, "project must be set"

#     credentials = bq_ctx.credentials
#     if not credentials:
#         log.debug("using default credentials")
#         default_credentials, _ = get_default_credentials()
#         credentials = default_credentials

#     bqclient = get_bigquery_client(project=project, credentials=credentials)
#     bqstorage_client = get_bqstorage_client(bqclient)
#     downloader = BigQueryDownloader(bqclient, bqstorage_client, tracker=tracker)

#     return bqclient, bqstorage_client, downloader
