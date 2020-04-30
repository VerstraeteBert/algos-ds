cmake_minimum_required(VERSION 3.15)
project(oefeningen)

set(CMAKE_CXX_STANDARD 20)

add_executable(lijsttest_les week-1/lijsttest.cpp)
add_executable(les2 algo_implementations/main.cpp)
add_executable(test1 test/vraag1/lijsttest.cpp)
add_executable(test2 test/vraag2/test.cpp)
add_executable(test3 test/vraag3/src/main.cpp)
add_executable(test4 test/vraag4/src/main.cpp)