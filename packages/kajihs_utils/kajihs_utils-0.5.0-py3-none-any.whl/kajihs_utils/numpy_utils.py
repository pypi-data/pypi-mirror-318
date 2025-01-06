"""Tools for numpy."""

from collections.abc import Iterable
from typing import Any, Literal

import numpy as np
from numpy import dtype, int_, ndarray
from numpy.typing import ArrayLike, NDArray

type Norm = float | Literal["fro", "nuc"]


class IncompatibleShapeError(ValueError):
    """Shapes of input arrays are incompatible for a given function."""

    def __init__(self, arr1: NDArray[Any], arr2: NDArray[Any], obj: Any) -> None:
        super().__init__(
            f"Shapes of inputs arrays {arr1.shape} and {arr2.shape} are incompatible for {obj.__name__}"
        )


# TODO: Add axis parameters
def find_closest[T](
    x: Iterable[T] | ArrayLike,
    targets: Iterable[T] | T | ArrayLike,
    norm_ord: Norm | None = None,
) -> ndarray[tuple[int], dtype[int_]] | int_:
    """
    Find the index of the closest element(s) from `x` for each target in `targets`.

    Given one or multiple `targets` (vectors vectors or scalars),
    this function computes the distance to each element in `x` and returns the
    indices of the closest matches. If `targets` is of the same shape as an
    element of `x`, the function returns a single integer index. If `targets`
    contains multiple elements, it returns an array of indices corresponding to
    each target.

    If the dimensionality of the vectors in `x` is greater than 2, the vectors
    will be flattened into 1D before computing distances.

    Args:
        x: An iterable or array-like collection of elements (scalars, vectors,
            or higher-dimensional arrays). For example, `x` could be an array of
            shape `(N,)` (scalars), `(N, D)` (D-dimensional vectors),
            `(N, H, W)` (2D arrays), or higher-dimensional arrays.
        targets: One or multiple target elements for which you want to find the
            closest match in `x`. Can be a single scalar/vector/array or an
            iterable of them.
            Must be shape-compatible with the elements of `x`.
        norm_ord: The order of the norm used for distance computation.
            Uses the same conventions as `numpy.linalg.norm`.

    Returns:
        An array of indices. If a single target was given, a single index is
        returned. If multiple targets were given, an array of shape `(M,)` is
        returned, where `M` is the number of target elements. Each value is the
        index of the closest element in `x` to the corresponding target.

    Raises:
        IncompatibleShapeError: If `targets` cannot be broadcast or reshaped to
            match the shape structure of the elements in `x`.

    Examples:
        >>> import numpy as np
        >>> x = np.array([0, 10, 20, 30])
        >>> int(find_closest(x, 12))
        1
        >>> # Multiple targets
        >>> find_closest(x, [2, 26])
        array([0, 3])

        >>> # Using vectors
        >>> x = np.array([[0, 0], [10, 10], [20, 20]])
        >>> int(find_closest(x, [6, 5]))  # Single target vector
        1
        >>> find_closest(x, [[-1, -1], [15, 12]])  # Multiple target vectors
        array([0, 1])

        >>> # Higher dimensional arrays
        >>> x = np.array([[[0, 0], [0, 0]], [[10, 10], [10, 10]], [[20, 20], [20, 20]]])
        >>> int(find_closest(x, [[2, 2], [2, 2]]))
        0
        >>> find_closest(x, [[[0, 0], [1, 1]], [[19, 19], [19, 19]]])
        array([0, 2])
    """
    x = np.array(x)  # (N, vector_shape)
    targets = np.array(targets)
    vector_shape = x.shape[1:]

    # Check that shapes are compatible
    do_unsqueeze = False
    if targets.shape == vector_shape:
        targets = np.atleast_1d(targets)[np.newaxis, :]  # (M, vector_shape)
        do_unsqueeze = True
    elif targets.shape[1:] != vector_shape:
        raise IncompatibleShapeError(x, targets, find_closest)

    nb_vectors = x.shape[0]  # N
    nb_targets = targets.shape[0]  # M

    diffs = x[:, np.newaxis] - targets

    match vector_shape:
        case ():
            distances = np.linalg.norm(diffs[:, np.newaxis], ord=norm_ord, axis=1)
        case (_,):
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=2)
        case (_, _):
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=(2, 3))
        case _:  # Tensors
            # Reshape to 1d vectors
            diffs = diffs.reshape(nb_vectors, nb_targets, -1)
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=2)

    closest_indices = np.argmin(distances, axis=0)
    if do_unsqueeze:
        closest_indices = closest_indices[0]

    return closest_indices
