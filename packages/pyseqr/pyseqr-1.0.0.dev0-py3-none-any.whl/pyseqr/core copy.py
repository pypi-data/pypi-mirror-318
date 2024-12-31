from typing import List, Sequence, Any
from decimal import Decimal, getcontext, InvalidOperation, ROUND_HALF_UP
import bisect


def validate_inputs(sublist: Sequence[Any], target: Sequence[Any]) -> None:
    if not isinstance(sublist, (list, tuple)) or not isinstance(target, (list, tuple)):
        raise TypeError("Both sublist and target must be of type list or tuple.")
    if not sublist or not target:
        raise ValueError("Neither sublist nor target can be empty.")
    if len(sublist) > len(target):
        raise ValueError("Sublist cannot be longer than target.")


def round_as_decimal(num, decimal_places=2):
    """Round a number to a given precision and return as a Decimal

    Arguments:
    :param num: number
    :type num: int, float, decimal, or str
    :returns: Rounded Decimal
    :rtype: decimal.Decimal

    https://stackoverflow.com/questions/8868985/problems-with-rounding-decimals-python solution by kamalgill
    """

    getcontext().prec = decimal_places + 1
    precision = "1.{places}".format(places="0" * decimal_places)
    return Decimal(str(num)).quantize(Decimal(precision), rounding=ROUND_HALF_UP)


def make_hashable(
    element: Any, convert_unhashable, custom_objects, float_precision=None
) -> Any:
    """
    Convert certain unhashable elements to hashable types recursively.
    """
    if float_precision and isinstance(element, float):
        try:
            getcontext().prec = float_precision
            return round_as_decimal(element, float_precision)
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid float precision.")

    if convert_unhashable:
        if isinstance(element, list):
            return tuple(make_hashable(e) for e in element)
        elif isinstance(element, dict):
            return frozenset((k, make_hashable(v)) for k, v in element.items())
        elif isinstance(element, set):
            return frozenset(make_hashable(e) for e in element)

    if custom_objects:
        # Check if the element is a custom object (i.e., not a built-in type)
        if type(element).__module__ != "builtins":
            # Ensure the custom object has a string representation
            if hasattr(element, "__str__") and callable(getattr(element, "__str__")):
                return str(element)
            else:
                raise TypeError(
                    f"Custom object of type {type(element).__name__} lacks a string representation."
                )

    return element


import bisect


def find_element(overlap, element_map, max_index):
    """
    Finds and returns the first element from the given list `element_map` after optionally filtering it
    based on the `max_index`. The filtering is performed only if `overlap` is False, and the list is
    assumed to be sorted in ascending order.

    Parameters:
        overlap (bool): If True, no filtering is applied to `element_map`.
                        If False, removes elements less than or equal to `max_index`.
        element_map (list[int]): A list of integers (assumed to be sorted) to process.
        max_index (int): The threshold value used for filtering when `overlap` is False.

    Returns:
        int or None: The first element of the filtered list if it exists, or None if the list is empty.

    Side Effects:
        Modifies the input `element_map` in-place by removing elements if filtering is applied or
        when the first element is popped.

    Example:
        >>> my_list = [1, 2, 3, 4, 5]
        >>> find_element(False, my_list, 2)
        3
        >>> my_list
        [4, 5]
    """
    import bisect

    if not overlap:
        # Find the first index where the value is greater than max_index
        pos = bisect.bisect_right(element_map, max_index)
        element_map[:] = element_map[
            pos:
        ]  # In-place modification to keep reference intact
    if element_map:
        return element_map.pop(0)  # Operates on the original list
    else:
        return None


def find_in_list(
    sublist: Sequence[Any],
    target: Sequence[Any],
    convert_unhashable: bool = False,
    custom_objects: bool = False,
    float_precision: int = None,
    overlap: bool = True,
    ordered: bool = False,
) -> List[List[int]]:
    """
    Find all occurrences of the `sublist` in the `target` in O(n) time where n is target list size.

    This function returns a list of occurrences where each occurrence is represented
    by a list of indices corresponding to the elements of the `sublist` in `target`.

    Parameters:
        sublist (List[int]): The list of elements to find in `target`.
        target (List[int]): The list of elements to search in.
        convert_unhashable (bool): If True, convert unhashable elements to hashable types.
        custom_objects (bool): If True, use the string representation of custom objects.
            NOTE: Objects with a default string representation that are not the same instance will not match.
            The user can define a custom string representation for their objects to ensure matches on equivalent instances.
        float_precision (int): If provided, round floating-point numbers to this precision for better matching.

    Returns:
        List[List[int]]: A list of lists, where each sublist represents the indices of
        one occurrence of the `sublist` in `target`. Returns an empty list if any
        element of `sublist` is not found in `target` or if no occurrences exist.

    Examples:
        >>> find_in_list([2, 3, 2], [1, 2, 3, 2, 4])
        [[1, 2, 3]]

        >>> find_in_list([2, 3, 2], [3, 2, 6, 2, 4])
        []

        >>> find_in_list([1], [3, 1, 1, 5])
        [[1], [2]]

        >>> find_in_list([2, 3, 2], [1, 2, 3, 2, 4, 2, 3, 2])
        [[1, 2, 3], [5, 6, 7]]
    """

    validate_inputs(sublist, target)

    # Convert elements to hashable types
    if convert_unhashable or custom_objects or float_precision:
        sublist = [
            make_hashable(
                e,
                convert_unhashable=convert_unhashable,
                custom_objects=custom_objects,
                float_precision=float_precision,
            )
            for e in sublist
        ]
        target = [
            make_hashable(
                e,
                convert_unhashable=convert_unhashable,
                custom_objects=custom_objects,
                float_precision=float_precision,
            )
            for e in target
        ]

    try:
        # Attempt to create the index_map
        index_map = {element: [] for element in set(sublist)}
    except TypeError as e:
        raise ValueError("All elements in sublist must be hashable.") from e

    # Populate the index_map with indices of matching elements in the target
    for index, value in enumerate(target):
        if value in index_map:
            index_map[value].append(index)

    # Check if any element in the sublist has no matches in the target
    if any(not indices for indices in index_map.values()):
        return []

    occurrences = []
    max_index = -1
    while True:
        current_occurrence = []
        for element in sublist:
            index = find_element(overlap, index_map[element], max_index)
            if index is not None:
                current_occurrence.append(index)
                if ordered:
                    max_index = index

            else:
                return occurrences
        max_index = current_occurrence[-1]
        if overlap == False:
            occurrences.append(current_occurrence)
