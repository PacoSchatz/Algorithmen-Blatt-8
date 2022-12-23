#include <iostream>
#include <vector>
#include "Sorting.h"
int main()
{
  std::vector<int> v = { 7, 5, 2, 6, 5, 0, 0, 7, 8, 1 };

  const size_t t = QuickSort(v.data(), v.size());

  for (const auto& i : v)
  {
    std::cout << i << " ";
  }
  std::cout << "\n" << "Time: " << t << std::endl;
  return 0;
}