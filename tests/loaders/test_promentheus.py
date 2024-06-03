from unittest.mock import patch

from emica.loaders.prometheus import (
    PrometheusLoader,
    convert_to_metrics,
    group_by_instance_and_date,
)

testdata = {
    "status": "success",
    "data": {
        "resultType": "matrix",
        "result": [
            {
                "metric": {"instance": "127.0.0.1:9100", "job": "node_exporter", "metric": "memory_utilization"},
                "values": [
                    [1717406886, "35.778141021728516"],
                    [1717406946, "35.8729362487793"],
                    [1717407006, "35.843849182128906"],
                    [1717407066, "35.90679168701172"],
                    [1717407126, "36.11431121826172"],
                ],
            },
            {
                "metric": {"instance": "127.0.0.1:9100", "job": "node_exporter", "metric": "memory_capacity"},
                "values": [
                    [1717406886, "16"],
                    [1717406946, "16"],
                    [1717407006, "16"],
                    [1717407066, "16"],
                    [1717407126, "16"],
                ],
            },
            {
                "metric": {"instance": "127.0.0.1:9100", "metric": "cpu_utilization"},
                "values": [
                    [1717406946, "8.026309941773569"],
                    [1717407006, "9.366666666660928"],
                    [1717407066, "10.124219461792405"],
                    [1717407126, "11.765849647785187"],
                ],
            },
            {
                "metric": {"instance": "localhost:9100", "job": "node_exporter", "metric": "memory_utilization"},
                "values": [
                    [1717406886, "35.787200927734375"],
                    [1717406946, "36.065006256103516"],
                    [1717407006, "35.70375442504883"],
                    [1717407066, "35.822296142578125"],
                    [1717407126, "36.14702224731445"],
                ],
            },
            {
                "metric": {"instance": "localhost:9100", "job": "node_exporter", "metric": "memory_capacity"},
                "values": [
                    [1717406886, "16"],
                    [1717406946, "16"],
                    [1717407006, "16"],
                    [1717407066, "16"],
                    [1717407126, "16"],
                ],
            },
            {
                "metric": {"instance": "localhost:9100", "metric": "cpu_utilization"},
                "values": [
                    [1717406946, "8.18888888889383"],
                    [1717407006, "9.735339214680305"],
                    [1717407066, "10.478190342875326"],
                    [1717407126, "10.913888888891165"],
                ],
            },
        ],
    },
}


def test_convert_to_metrics():
    grouped = group_by_instance_and_date(testdata)
    instances = convert_to_metrics(grouped, 60)
    assert len(instances) == 2


def test_load_data():
    loader = PrometheusLoader(host="http://localhost:9090")
    with patch("emica.loaders.prometheus.PrometheusLoader._fetch_data") as mocked_method:
        mocked_method.return_value = testdata
        data = loader.load()
    assert len(data) == 2
