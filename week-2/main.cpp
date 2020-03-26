#include "util/csv.h"
#include "util/intstring.h"
#include "sorts/stlsort.h"
#include "sorts/insertionsort.h"
#include "sorts/mergesort.h"
#include "sorts/shellsort.h"
#include "sorts/parallelmerge.h"
#include "sorts/selectionsort.h"
#include "sorts/heapsort.h"
#include "sorts/quicksort.h"

#include <array>
#include <iostream>
#include <memory>
#include <utility>

template <class T>
void measure_sorts(const std::string& csv_filename)
{
    constexpr int ondergrens = 10'000;
    constexpr int bovengrens = 10'000'000;


    CsvData csv_results{csv_filename, '.', ','};

    std::array<std::pair<std::string, std::unique_ptr<Sorteermethode<T>>>, 5> sorters = {
            std::make_pair("STL sort", std::make_unique<STLSort<T>>()),
//            std::make_pair("Insertion sort", std::make_unique<InsertionSort<T>>()),
//            std::make_pair("Selection Sort", std::make_unique<SelectionSort<T>>()),
            std::make_pair("Shell Sort", std::make_unique<ShellSort<T>>()),
//            std::make_pair("Quick Sort", std::make_unique<QuickSort<T>>()),
            std::make_pair("Heap Sort", std::make_unique<HeapSort<T>>()),
            std::make_pair("Merge Sort", std::make_unique<MergeSort<T>>()),
            std::make_pair("Parallel Merge Sort", std::make_unique<ParallelMerge<T>>()),
    };

    for (const auto& sorter : sorters)
    {

        std::cout << std::endl;
        std::cout << sorter.first << ":" << std::endl;
        std::cout << std::endl;

        sorter.second->meet(ondergrens, bovengrens, std::cout, csv_results);
    }

    std::cout << std::endl << "Writing data to \"" << csv_results.geef_bestandsnaam() << "\" ..." << std::endl;
    csv_results.write_to_file();
    std::cout << "Data written" << std::endl << std::endl;
}

int main()
{
    std::cout << "===== int =====" << std::endl;

    measure_sorts<int>("sort_int");

    std::cout << "===== double =====" << std::endl;

    measure_sorts<double>("sort_double");

    std::cout << "===== Intstring =====" << std::endl;

    measure_sorts<Intstring>("sort_intstring");

    return 0;
}
