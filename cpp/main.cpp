#include <iostream>
#include <chrono>
#include <vector>
#include <functional>

static constexpr void selection_sort(std::vector<int>& in)
{
  for (size_t i = 0; i < in.size() - 1; ++i)
  {
    int p = i;
    for (size_t j = i + 1; j < in.size(); j++)
      if (in[j] < in[p])
        p = j;

    std::swap(in[p], in[i]);
  }
}

static void _quick_sort(std::vector<int>& in, size_t start, size_t end, std::function<size_t(const std::vector<int>&, size_t, size_t)> pivot_func)
{
  if (start >= end)
    return;

  const int p = in.at(pivot_func(in, start, end));

  size_t mid_start = 0;

  size_t cur_idx = start;
  for (size_t i = cur_idx; i < end; ++i)
    if (in[i] < p)
      std::swap(in[i], in[cur_idx++]);

  mid_start = cur_idx;

  for (size_t i = cur_idx; i < end; ++i)
    if (in[i] == p)
      std::swap(in[i], in[cur_idx++]);

  _quick_sort(in, start, mid_start, pivot_func);
  _quick_sort(in, cur_idx, end, pivot_func);
}

void quick_sort(std::vector<int>& in, std::function<size_t(const std::vector<int>&, size_t, size_t)> pivot_func)
{
  _quick_sort(in, 0, in.size(), pivot_func);
}

static constexpr size_t pivot_half(const std::vector<int>& in, size_t start, size_t end)
{
  return  start + ((end - start) / 2);
}

std::vector<int> generate(size_t size)
{
  std::srand(unsigned(std::time(nullptr)));
  std::vector<int> v(1000);
  std::generate(v.begin(), v.end(), std::rand);
  return v;
}
template<typename F, typename ... Args>
static void run(size_t itcount, size_t samplesize, const F& sortfunc, Args&& ... sortargs)
{
  size_t passed = 0, exetime = 0;

  for (size_t i = 0; i < itcount; i++)
  {
    std::vector<int> v = generate(samplesize);

    auto start = std::chrono::high_resolution_clock::now();
    sortfunc(v, std::forward<Args>(sortargs)...);
    auto end = std::chrono::high_resolution_clock::now();

    exetime += std::chrono::duration_cast<std::chrono::nanoseconds>((end - start)).count();

    if (std::is_sorted(v.begin(), v.end()))
      passed++;
  }

  std::cout << "Executed " << typeid(F).name() << " " << itcount << " times with a Array-Size of " << samplesize << std::endl;
  std::cout << "Soring the Array took an avg. of " << (exetime / samplesize) << "ns" << std::endl;
  std::cout << "\tPassed: " << passed << std::endl;
  std::cout << "\tFailed: " << itcount - passed << "\n" << std::endl;
}

int main(int argc, char** argv)
{
  run(10, 1000, selection_sort);
  run(10, 1000, quick_sort, pivot_half);
  return 0;
}