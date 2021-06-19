from mlproject.distance import haversine

def test_distance_type():
    assert (haversine(50, 100, 30, 10)) > 0