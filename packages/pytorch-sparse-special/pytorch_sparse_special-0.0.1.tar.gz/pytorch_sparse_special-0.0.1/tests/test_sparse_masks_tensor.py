import pytest
import torch

from pytorch_sparse_special.errors import SizeValueError
from pytorch_sparse_special.special.sparse_mask import SparseMasksTensor


@pytest.mark.parametrize(
    "scenarios_sparse",
    [1, 2],
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_create(scenarios_sparse):
    indices = scenarios_sparse[0]
    values = scenarios_sparse[1]
    size = scenarios_sparse[2]

    instance = SparseMasksTensor(indices, values, size)
    assert isinstance(instance, SparseMasksTensor)


@pytest.fixture()
def expect_errors(request):
    if request.param in [1, 2]:
        return SizeValueError
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse_fails, expect_errors",
    ([1, 1], [2, 2]),
    ids=["scenario3", "scenario4"],
    indirect=True,
)
def test_create_fails(scenarios_sparse_fails, expect_errors):
    indices = scenarios_sparse_fails[0]
    values = scenarios_sparse_fails[1]
    size = scenarios_sparse_fails[2]

    with pytest.raises(expect_errors):
        SparseMasksTensor(indices, values, size)


@pytest.fixture()
def expect_extract(request):
    if request.param == 1:
        return {
            "shape_idx": torch.Size([3, 12]),
            "shape_val": torch.Size([12]),
        }
    elif request.param == 2:
        return {
            "shape_idx": torch.Size([3, 16]),
            "shape_val": torch.Size([16]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse_bbox, expect_extract",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_extract_sparse_region(scenarios_sparse_bbox, expect_extract):
    indices = scenarios_sparse_bbox["sparse"][0]
    values = scenarios_sparse_bbox["sparse"][1]
    size = scenarios_sparse_bbox["sparse"][2]
    bbox = scenarios_sparse_bbox["bbox"]

    instance = SparseMasksTensor(indices, values, size)
    filtered_idx, filtered_val = instance.extract_sparse_region(bbox)
    assert filtered_idx.shape == expect_extract["shape_idx"]
    assert filtered_val.shape == expect_extract["shape_val"]


@pytest.fixture()
def expect_ppm(request):
    if request.param == 1:
        return {
            "pixel_count": torch.tensor([9, 5, 7]),
        }
    elif request.param == 2:
        return {
            "pixel_count": torch.tensor([10, 6, 9]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse, expect_ppm",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_pixel_per_mask(scenarios_sparse, expect_ppm):
    indices = scenarios_sparse[0]
    values = scenarios_sparse[1]
    size = scenarios_sparse[2]

    instance = SparseMasksTensor(indices, values, size)
    pixel_count = instance.pixel_per_mask()
    assert torch.eq(pixel_count, expect_ppm["pixel_count"]).all()


@pytest.fixture()
def expect_ppmi(request):
    if request.param == 1:
        return {
            "pixel_count": torch.tensor([3, 5, 4]),
        }
    elif request.param == 2:
        return {
            "pixel_count": torch.tensor([4, 6, 6]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse_bbox, expect_ppmi",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_pixel_per_mask_inside(scenarios_sparse_bbox, expect_ppmi):
    indices = scenarios_sparse_bbox["sparse"][0]
    values = scenarios_sparse_bbox["sparse"][1]
    size = scenarios_sparse_bbox["sparse"][2]
    bbox = scenarios_sparse_bbox["bbox"]

    instance = SparseMasksTensor(indices, values, size)
    pixel_count = instance.pixel_per_mask_inside(bbox)
    assert torch.eq(pixel_count, expect_ppmi["pixel_count"]).all()


@pytest.fixture()
def expect_apm(request):
    if request.param == 1:
        return {
            "area_sizes": torch.tensor([0.36, 0.2, 0.28]),
        }
    elif request.param == 2:
        return {
            "area_sizes": torch.tensor([1 / 3, 0.2, 0.3]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse, expect_apm",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_area_per_mask(scenarios_sparse, expect_apm):
    indices = scenarios_sparse[0]
    values = scenarios_sparse[1]
    size = scenarios_sparse[2]

    instance = SparseMasksTensor(indices, values, size)
    area_sizes = instance.area_per_mask()
    assert torch.isclose(area_sizes, expect_apm["area_sizes"]).all()


@pytest.fixture()
def expect_apmi(request):
    if request.param == 1:
        return {
            "area_sizes": torch.tensor([0.12, 0.2, 0.16]),
        }
    elif request.param == 2:
        return {
            "area_sizes": torch.tensor([2 / 15, 0.2, 0.2]),
        }
    raise NotImplementedError(f"No such scenario: {request.param!r}")


@pytest.mark.parametrize(
    "scenarios_sparse_bbox, expect_apmi",
    ([1, 1], [2, 2]),
    ids=["scenario1", "scenario2"],
    indirect=True,
)
def test_area_per_mask_inside(scenarios_sparse_bbox, expect_apmi):
    indices = scenarios_sparse_bbox["sparse"][0]
    values = scenarios_sparse_bbox["sparse"][1]
    size = scenarios_sparse_bbox["sparse"][2]
    bbox = scenarios_sparse_bbox["bbox"]

    instance = SparseMasksTensor(indices, values, size)
    area_sizes = instance.area_per_mask_inside(bbox)
    assert torch.isclose(area_sizes, expect_apmi["area_sizes"]).all()
