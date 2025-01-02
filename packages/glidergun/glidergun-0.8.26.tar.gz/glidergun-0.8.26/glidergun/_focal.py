import sys
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, List, Optional, Union, cast

import numpy as np
from numpy import ndarray
from numpy.lib.stride_tricks import sliding_window_view

if TYPE_CHECKING:
    from glidergun._grid import Grid


@dataclass(frozen=True)
class Focal:
    def focal(
        self, func: Callable[[ndarray], Any], buffer: int, circle: bool
    ) -> "Grid":
        def f(g: "Grid") -> "Grid":
            size = 2 * buffer + 1
            mask = _mask(buffer) if circle else np.full((size, size), True)
            array = sliding_window_view(_pad(g.data, buffer), (size, size))
            result = func(array[:, :, mask])
            return g.update(result)

        return _batch(f, buffer, cast("Grid", self))

    def focal_python(
        self,
        func: Callable[[List[float]], float],
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
    ) -> "Grid":
        def f(a):
            values = [n for n in a if n != np.nan] if ignore_nan else list(a)
            return func(values)

        return self.focal(lambda a: np.apply_along_axis(f, 2, a), buffer, circle)

    def focal_count(
        self, value: Union[float, int], buffer: int = 1, circle: bool = False, **kwargs
    ):
        return self.focal(
            lambda a: np.count_nonzero(a == value, axis=2, **kwargs), buffer, circle
        )

    def focal_ptp(self, buffer: int = 1, circle: bool = False, **kwargs):
        return self.focal(lambda a: np.ptp(a, axis=2, **kwargs), buffer, circle)

    def focal_percentile(
        self,
        percentile: float,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        **kwargs,
    ):
        f = np.nanpercentile if ignore_nan else np.percentile
        return self.focal(lambda a: f(a, percentile, axis=2, **kwargs), buffer, circle)

    def focal_quantile(
        self,
        probability: float,
        buffer: int = 1,
        circle: bool = False,
        ignore_nan: bool = True,
        **kwargs,
    ):
        f = np.nanquantile if ignore_nan else np.quantile
        return self.focal(lambda a: f(a, probability, axis=2, **kwargs), buffer, circle)

    def focal_median(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanmedian if ignore_nan else np.median
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_mean(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanmean if ignore_nan else np.mean
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_std(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanstd if ignore_nan else np.std
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_var(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanvar if ignore_nan else np.var
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_min(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanmin if ignore_nan else np.min
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_max(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nanmax if ignore_nan else np.max
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def focal_sum(
        self, buffer: int = 1, circle: bool = False, ignore_nan: bool = True, **kwargs
    ):
        f = np.nansum if ignore_nan else np.sum
        return self.focal(lambda a: f(a, axis=2, **kwargs), buffer, circle)

    def fill_nan(self, max_exponent: int = 4):
        if not cast("Grid", self).has_nan:
            return self

        def f(g: "Grid"):
            n = 0
            while g.has_nan and n <= max_exponent:
                g = g.is_nan().con(g.focal_mean(2**n, True), g)
                n += 1
            return g

        return _batch(f, 2**max_exponent, cast("Grid", self))


def _mask(buffer: int) -> ndarray:
    size = 2 * buffer + 1
    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            d = ((x - buffer) ** 2 + (y - buffer) ** 2) ** (1 / 2)
            row.append(d <= buffer)
        rows.append(row)
    return np.array(rows)


def _pad(data: ndarray, buffer: int):
    row = np.zeros((buffer, data.shape[1])) * np.nan
    col = np.zeros((data.shape[0] + 2 * buffer, buffer)) * np.nan
    return np.hstack([col, np.vstack([row, data, row]), col], dtype="float32")


def _batch(func: Callable[["Grid"], "Grid"], buffer: int, grid: "Grid") -> "Grid":
    def tile():
        stride = 8000 // buffer
        for x in range(0, grid.width // stride + 1):
            xmin, xmax = x * stride, min((x + 1) * stride, grid.width)
            if xmin < xmax:
                for y in range(0, grid.height // stride + 1):
                    ymin, ymax = y * stride, min((y + 1) * stride, grid.height)
                    if ymin < ymax:
                        yield xmin, ymin, xmax, ymax

    tiles = list(tile())
    count = len(tiles)

    if count <= 4:
        return func(grid)

    result: Optional["Grid"] = None
    cell_size = grid.cell_size
    n = 0

    for xmin, ymin, xmax, ymax in tiles:
        n += 1
        sys.stdout.write(f"\rProcessing {n} of {count} tiles...")
        sys.stdout.flush()
        g1 = grid.clip(
            grid.xmin + (xmin - buffer) * cell_size.x,
            grid.ymin + (ymin - buffer) * cell_size.y,
            grid.xmin + (xmax + buffer) * cell_size.x,
            grid.ymin + (ymax + buffer) * cell_size.y,
        )
        g2 = func(g1)
        g3 = g2.clip(
            grid.xmin + xmin * cell_size.x,
            grid.ymin + ymin * cell_size.y,
            grid.xmin + xmax * cell_size.x,
            grid.ymin + ymax * cell_size.y,
        )
        result = result.mosaic(g3) if result else g3

    print()
    assert result
    return result
