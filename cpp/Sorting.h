#pragma once
#include <numeric>


//size_t QuickSort(int arr[], size_t size);

#ifdef WIN32
#ifdef sorting_EXPORTS
#define SORTING_API __declspec(dllexport)
#else
#define SORTING_API __declspec(dllimport)
#endif // sorting_EXPORTS
extern "C" { SORTING_API size_t QuickSort(int* arr, size_t size); } //c++ interface
extern "C" { __declspec(dllexport) size_t RunQuickSort(int* arr, size_t size) { return QuickSort(arr, size); }} //python interface
#else
extern "C" {
  void RunQSort() { QSort(); }
}
#endif // WIN32
