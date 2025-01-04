import pytest
import torch

from pytorch_sparse_special.metrics import iou_sparse_masks_bbox
from pytorch_sparse_special.special.sparse_mask import SparseMasksTensor


@pytest.fixture()
def expect_iou(request):
    if request.param == 1:
        return {
            "iou": torch.tensor([0.2, 5 / 9, 1 / 3]),
        }
    elif request.param == 2:
        return {
            "iou": torch.tensor([2 / 9, 0.5, 0.4]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse_bbox, expect_iou",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_iou_sparse_masks_bbox(scenarios_sparse_bbox, expect_iou):
    indices = scenarios_sparse_bbox["sparse"][0]
    values = scenarios_sparse_bbox["sparse"][1]
    size = scenarios_sparse_bbox["sparse"][2]
    bbox = scenarios_sparse_bbox["bbox"]

    instance = SparseMasksTensor(indices, values, size)
    iou = iou_sparse_masks_bbox(instance, bbox)
    assert torch.isclose(iou, expect_iou["iou"]).all()
