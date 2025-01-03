# Copyright(c) 2024 by FEI Company, part of Thermo Fisher Scientific.
# All rights reserved. This file includes confidential and proprietary
# information of FEI Company.
import os
import test
from datetime import datetime

from elasticsearch import Elasticsearch

ES_URL = "https://czbrn-sqa-elk.emea.thermo.com"
ES_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
ES_USER = "velox_endurance"
ES_PWD = os.environ.get("ES_PWD")


def get_endurance_test_dashboard_url(start_time: datetime, end_time: datetime, mpc_name: str) -> str:
    """Gets a link to the Velox endurance test metrics dashboard in Kibana for the times and MPC specified.

    Parameters
    ----------
    start_time: the start time of the endurance test
    end_time: the end time of the endurance test
    mpc_name: the name of the MPC used for the endurance test

    Returns
    -------
    The URL to the Velox endurance test metrics dashboard in Kibana
    """
    start_time_formatted = start_time.strftime(ES_DATETIME_FORMAT)
    end_time_formatted = end_time.strftime(ES_DATETIME_FORMAT)
    return (
        f"{ES_URL}:5602/s/sqa-reporting/app/dashboards"
        "#/view/3e8aa320-b523-11ee-9832-658c73134a6d"
        f"?_g=(filters:!((query:(match_phrase:(agent.name:{mpc_name})))),refreshInterval:(pause:!t,value:0),"
        f"time:(from:'{start_time_formatted}',to:'{end_time_formatted}'))"
    )


def reindex_velox_endurance(start_time: datetime, end_time: datetime, mpc_name: str):
    """Reindex velox endurance data from metrics-* to velox-endurance index using defined time interval and hostname.

    Parameters
    ----------
    start_time: start time of the endurance test
    end_time: end time of the endurance test
    mpc_name: name of the microscope the endurance test was run on
    """
    if not ES_PWD:
        test.fail("ES_PWD environment variable must be set on the Squish runner system")

    start_time_formatted = start_time.strftime(ES_DATETIME_FORMAT)
    end_time_formatted = end_time.strftime(ES_DATETIME_FORMAT)
    elasticsearch_connection = Elasticsearch([f"{ES_URL}:9200"], basic_auth=(ES_USER, ES_PWD), verify_certs=False)

    elasticsearch_connection.reindex(
        source={
            "index": "metrics-*",
            "query": {
                "bool": {
                    "must": [
                        {"match": {"agent.parsed_name": mpc_name}},
                        {"match": {"data_stream.dataset": "windows.perfmon"}},
                        {"range": {"@timestamp": {"gte": start_time_formatted, "lt": end_time_formatted}}},
                    ]
                }
            },
        },
        dest={"index": "velox-endurance"},
        request_timeout=10000,
    )
