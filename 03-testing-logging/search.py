import logging

logger = logging.getLogger(__name__)

from time import perf_counter


def binary_search(numbers: list[int], target: int) -> int:
    if any(left > right for left, right in zip(numbers, numbers[1:])):
        raise ValueError("numbers must be sorted")
    logger.warning(f'start')
    
    time_start = perf_counter()
    left, right = 0, len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2

        logger.info(middle)
        if numbers[middle] == target:
            time_elapsed = perf_counter() - time_start
            # time_elapsed = perf_counter() - time_start
            logging.debug(f'elapsed {time_elapsed}', extra={'elapsed': time_elapsed})
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    logger.error(f'{target} missing')
    raise LookupError(f"{target} not found")
