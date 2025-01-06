# TODO: Add axis parameters
def find_closest_bk[T](
    x: Iterable[T] | ArrayLike,
    targets: Iterable[T] | T | ArrayLike,
    norm_ord: Norm | None = None,
) -> ndarray[tuple[int], dtype[int_]]:
    """
    Find the index of the closest element of x for each target.

    If the dimension of input vectors is more than 2, so the dimension of x > 3,
    they will be flattened to dimension 1.
    """
    x = np.array(x)  # (N, vector_shape)
    targets = np.array(targets)
    vector_shape = x.shape[1:]

    original_targets = targets
    # print(f"{x.shape = }")
    # print(f"{x.shape[1:] = }")
    # print(f"{targets.shape == x.shape[1:] = }")
    # print(f"{targets.shape = }")

    # Check that shapes are compatible
    do_unsqueeze = False
    if targets.shape == vector_shape:
        targets = np.atleast_1d(targets)[np.newaxis, :]  # (M, vector_shape)
        do_unsqueeze = True
    elif targets.shape[1:] != vector_shape:
        raise IncompatibleShapeError(x, targets, find_closest)

    nb_vectors = x.shape[0]
    nb_targets = targets.shape[0]

    diffs = x[:, np.newaxis] - targets
    # print(diffs.shape)
    assert diffs.shape == (nb_vectors, nb_targets, *vector_shape)

    match vector_shape:
        case ():
            distances = np.linalg.norm(diffs[:, np.newaxis], ord=norm_ord, axis=1)
        case (_,):
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=2)
        case (_, _):
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=(2, 3))  # TODO: Solve
        case _:  # Tensors
            # Reshape to 1d vectors
            diffs = diffs.reshape(nb_vectors, nb_targets, -1)
            distances = np.linalg.norm(diffs, ord=norm_ord, axis=2)

    # match targets.shape:
    #     case x.shape:
    #         pass
    #     case s if s == x.shape[1:]:
    #         targets = np.atleast_1d(targets)
    #     case _:
    #         raise IncompatibleShapeError(x, targets, find_closest)

    # match x.ndim - targets.ndim:
    #     case 1:
    #         targets = np.atleast_1d(targets)[:, np.newaxis]
    #     case 0:
    #         pass
    #     case _:
    #         raise IncompatibleDimensionsError(x, targets, find_closest)

    # print("vectors\n", x)
    # print("targets\n", targets)
    closest_indexes = np.argmin(distances, axis=0)
    if do_unsqueeze:
        closest_indexes = closest_indexes[0]
    # print("distances\n", distances)
    # assert distances.shape == (nb_vectors, nb_targets)
    print(f"argmin: {closest_indexes}")
    assert closest_indexes.shape == (() if do_unsqueeze else (original_targets.shape[0],))
    return closest_indexes


x_scalar = [1, 1, 2, 3, 4]
x_1d = [
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
]
x_2d = [
    [
        [2, 2],
        [2, 1],
        [3, 1],
        [4, 1],
    ],
    [
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 1],
    ],
]

x_3d = [
    [
        [[2, 2], [2, 1], [3, 1]],
        [[1, 1], [2, 1], [3, 1]],
        [[2, 2], [2, 1], [3, 1]],
    ],
    [
        [[2, 2], [2, 1], [3, 1]],
        [[2, 2], [3, 2], [4, 2]],
        [[2, 2], [2, 1], [3, 1]],
    ],
]
target_scalar = 2.2
target_1d = [1, 2]
targets_1d = [[2, 2], [1, 1]]
target_2d = [
    [1, 1],
    [1, 1],
    [1, 2],
    [1, 1],
]
targets_2d = [
    [
        [2, 2],
        [1, 1],
        [1, 2],
        [2, 1],
    ],
    [
        [1, 1],
        [1, 1],
        [1, 2],
        [2, 1],
    ],
]

target_3d = [
    [[2, 2], [2, 1], [3, 1]],
    [[2, 2], [2, 1], [3, 1]],
    [[2, 2], [2, 1], [3, 1]],
]

targets_3d = [
    [
        [[2, 2], [2, 1], [3, 1]],
        [[1, 1], [2, 1], [3, 1]],
        [[2, 2], [2, 1], [3, 1]],
    ],
    [
        [[2, 2], [2, 1], [3, 1]],
        [[2, 2], [3, 2], [4, 2]],
        [[2, 2], [2, 1], [3, 1]],
    ],
    [
        [[2, 2], [2, 1], [3, 1]],
        [[2, 2], [0, 0], [0, 0]],
        [[2, 2], [2, 1], [3, 1]],
    ],
]

norm_ord = 2

# distances = np.linalg.norm(x[:, np.newaxis] - targets, axis=-1, ord=norm_ord)
# print("distances\n", distances)

# Test errors
arr1 = np.array([
    [1, 1],
    [2, 1],
    [3, 1],
    [4, 1],
])

arr2 = np.array([
    [1, 1, 1],
])


assert find_closest(x_scalar, target_scalar, 2) == 2
# find_closest(x_scalar, target_scalar, "fro")
assert all(find_closest(x_scalar, target_1d, 2) == np.array([0, 2]))
assert find_closest(x_1d, target_1d, 2) == 0
# find_closest(x_1d, target_1d, "fro")
assert all(find_closest(x_1d, targets_1d, 2) == np.array([1, 0]))
assert find_closest(x_2d, target_2d, None) == 1
# find_closest(x_2d, target_2d, 4)
assert all(find_closest(x_2d, targets_2d, None) == np.array([0, 1]))
assert find_closest(x_3d, target_3d, None) == 0
assert all(find_closest(x_3d, targets_3d, None) == np.array([0, 1, 0]))


# find_closest_vectors_with_flatten(x_scalar, target_scalar, 2)
# assert all(find_closest_vectors_with_flatten(x_scalar, target_1d, 2) == np.array([0, 2]))
# find_closest_vectors_with_flatten(x_1d, target_1d, 2)
# find_closest_vectors_with_flatten(x_1d, targets_1d, 2)
# find_closest_vectors_with_flatten(x_2d, target_2d, None)
# find_closest_vectors_with_flatten(x_2d, targets_2d, None)

# END
