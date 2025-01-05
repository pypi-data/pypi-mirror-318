from pandas import concat, DataFrame, read_json


def fixture_json_to_df(path: str) -> DataFrame:
    """Get a dataframe from a fixture in json format."""
    fixture = read_json(path)
    model = fixture["model"]
    pk = fixture["pk"]
    fields = DataFrame(fixture["fields"].to_dict()).T
    return concat([model, pk, fields], axis=1)
