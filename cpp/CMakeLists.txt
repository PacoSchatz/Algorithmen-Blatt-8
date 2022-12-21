cmake_minimum_required(VERSION 3.20)

set(PROJECTNAME "sorting")

set(src ${src}
    #add new files here!
)

add_executable(${PROJECTNAME} WIN32 main.cpp ${src})
set_property(TARGET ${PROJECTNAME} PROPERTY LINKER_LANGUAGE CXX)
set_property(TARGET ${PROJECTNAME} PROPERTY CXX_STANDARD 20)
