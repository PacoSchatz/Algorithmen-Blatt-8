#include <iostream>
#include <chrono>
#include <vector>
#include <functional>
#include <numeric>

const int test1[] = { 1 };
const int test2[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200 };
const int test3[] = { 200, 199, 198, 197, 196, 195, 194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176, 175, 174, 173, 172, 171, 170, 169, 168, 167, 166, 165, 164, 163, 162, 161, 160, 159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133, 132, 131, 130, 129, 128, 127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
const int test4[] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };

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

static constexpr size_t pivot_median(const std::vector<int>& in, size_t start, size_t end)
{
  double sum = std::accumulate(in.cbegin() + start, in.cbegin() + start + end, 0);
  sum /= (end - start);
  size_t t = start;
  double dt = std::numeric_limits<float>::infinity();
  for (size_t i = start; i < end; i++) 
  {
    double d = std::abs(in[i] - sum);
    if (d < dt)
    {
      t = i;
      dt = d;
    }
  }
  return t;
}

static constexpr size_t pivot_start(const std::vector<int>& in, size_t start, size_t end)
{
  return  start;
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
  const auto test = [&](uint16_t t, const int* a, size_t s) {
    std::vector<int> v(a, a + s);
    auto start = std::chrono::high_resolution_clock::now();
    sortfunc(v, std::forward<Args>(sortargs)...);
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << "Test " << t << " took " << std::chrono::duration_cast<std::chrono::nanoseconds>((end - start)).count() << "ns\n" << std::endl;
    if (!std::is_sorted(v.begin(), v.end()))
      std::cout << "\tTest not passed" << std::endl;
  };

  test(1, test1, sizeof(test1) / sizeof(int));
  test(2, test2, sizeof(test2) / sizeof(int));
  test(3, test3, sizeof(test3) / sizeof(int));
  test(4, test4, sizeof(test4) / sizeof(int));

  size_t passed = 0, exetime = 0;

  for (size_t i = 0; i < itcount; i++)
  {
    std::vector<int> v = generate(samplesize);
    std::vector<int> s(v);
    std::sort(s.begin(), s.end());


    auto start = std::chrono::high_resolution_clock::now();
    sortfunc(v, std::forward<Args>(sortargs)...);
    auto end = std::chrono::high_resolution_clock::now();

    exetime += std::chrono::duration_cast<std::chrono::nanoseconds>((end - start)).count();

    if (std::equal(v.begin(), v.end(), s.begin()))
      passed++;
  }

  std::cout << "Executed " << typeid(F).name() << " " << itcount << " times with a Array-Size of " << samplesize << std::endl;
  std::cout << "Soring the Array took an avg. of " << (exetime / samplesize) << "ns" << std::endl;
  std::cout << "\tPassed: " << passed << std::endl;
  std::cout << "\tFailed: " << itcount - passed << "\n" << std::endl;
}

int main(int argc, char** argv)
{
  run(10, 10000, selection_sort);
  run(10, 10000, quick_sort, pivot_half);
  run(10, 10000, quick_sort, pivot_median);
  run(10, 10000, quick_sort, pivot_start);
  return 0;
}