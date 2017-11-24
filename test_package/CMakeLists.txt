PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_definitions(-std=c++11)

set(example_names
  #sample
  insert
  update
  remove
  select
  )

create_test_sourcelist(example_sources example_main.cpp ${example_names})
add_executable(sqlpp11_examples ${example_sources})
#target_link_libraries(sqlpp11_examples PRIVATE sqlpp11 sqlpp11_testing)

foreach(example IN LISTS example_names)
  add_test(NAME sqlpp11.examples.${example}
    COMMAND sqlpp11_examples ${example}
    )
endforeach()
