cmake_minimum_required(VERSION 3.20)

set(PROJECTNAME "sorting")

project(${PROJECTNAME})

set(src ${src}
    #add new files here!
)

add_executable(${PROJECTNAME} main.cpp ${src})
set_property(TARGET ${PROJECTNAME} PROPERTY LINKER_LANGUAGE CXX)
set_property(TARGET ${PROJECTNAME} PROPERTY CXX_STANDARD 20)
