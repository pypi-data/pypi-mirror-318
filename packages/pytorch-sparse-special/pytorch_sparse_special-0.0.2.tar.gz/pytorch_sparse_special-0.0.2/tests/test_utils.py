import pytest
import torch

from pytorch_sparse_special.utils import area_of_bbox


@pytest.fixture()
def expect_area_bbox(request):
    if request.param == 1:
        return {
            "area": torch.tensor([0.36]),
        }
    elif request.param == 2:
        return {
            "area": torch.tensor([(5 / 6 - 1 / 6) * 0.6]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_bbox, expect_area_bbox",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_area_of_bbox(scenarios_bbox, expect_area_bbox):
    bbox = scenarios_bbox

    area = area_of_bbox(bbox)
    assert area == expect_area_bbox["area"]
