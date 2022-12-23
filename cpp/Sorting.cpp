#include "Sorting.h"

#include <iostream>
#include <chrono>
#include <deque>

size_t QuickSort(int arr[], size_t size)
{
  const auto start_time = std::chrono::high_resolution_clock::now();

  std::deque<std::pair<size_t, size_t>> interval_stack;
  interval_stack.push_back({ 0, size });

  while (!interval_stack.empty())
  {
    std::pair<size_t, size_t> cur = interval_stack.front();
    interval_stack.pop_front();

    if (cur.first >= cur.second)
      continue;

    const size_t pivot = arr[cur.first + ((cur.second - cur.first) / 2)];

    size_t write_idx = cur.first;

    for (size_t i = write_idx; i < cur.second; ++i)
      if (arr[i] < pivot)
        std::swap(arr[i], arr[write_idx++]);

    size_t mid = write_idx;

    for (size_t i = write_idx; i < cur.second; i++)
      if (arr[i] == pivot)
        std::swap(arr[i], arr[write_idx++]);

    interval_stack.push_back({ cur.first, mid });
    interval_stack.push_back({ write_idx, cur.second });
  }

  const auto end_time = std::chrono::high_resolution_clock::now();
  return std::chrono::duration_cast<std::chrono::nanoseconds>((end_time - start_time)).count();
}
