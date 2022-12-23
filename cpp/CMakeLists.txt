cmake_minimum_required(VERSION 3.20)

set(LIB_NAME "sorting")
set(EXE_NAME "sorting_test")

project(${LIB_NAME})

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/Output/Lib")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/Output/Bin")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/Output/Bin")

set(src ${src}
    Sorting.h
    Sorting.cpp
)

add_library(${LIB_NAME} SHARED ${src})
set_property(TARGET ${LIB_NAME} PROPERTY LINKER_LANGUAGE CXX)
set_property(TARGET ${LIB_NAME} PROPERTY CXX_STANDARD 20)

add_custom_command(TARGET ${LIB_NAME} POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${LIB_NAME}> "../../bench/"
)

add_executable(${EXE_NAME} main.cpp)
set_property(TARGET ${EXE_NAME} PROPERTY LINKER_LANGUAGE CXX)
set_property(TARGET ${EXE_NAME} PROPERTY CXX_STANDARD 20)
target_link_libraries(${EXE_NAME} PUBLIC ${LIB_NAME})
