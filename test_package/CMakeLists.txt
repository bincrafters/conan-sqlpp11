project(test_package)
cmake_minimum_required(VERSION 2.8.11)

set(CMAKE_VERBOSE_MAKEFILE TRUE)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(example_names
  insert
  update
  remove
  select
  )

create_test_sourcelist(example_sources example_main.cpp ${example_names})
add_executable(sqlpp11_examples ${example_sources})

foreach(example IN LISTS example_names)
  add_test(NAME sqlpp11.examples.${example}
    COMMAND sqlpp11_examples ${example}
    )
endforeach()
