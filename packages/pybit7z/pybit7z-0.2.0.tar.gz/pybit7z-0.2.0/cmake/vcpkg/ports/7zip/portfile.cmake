vcpkg_check_linkage(ONLY_DYNAMIC_LIBRARY)

vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO ip7z/7zip
    REF "${VERSION}"
    SHA512 dc0241ed96907965445550912d1171fe32230a52997b089558a4cc73a662fc6a17940db8dcb0794b805268964899d9e5a48ddb444e92b56fd243bbaa17c20a1c
    HEAD_REF main
)

file(COPY "${CMAKE_CURRENT_LIST_DIR}/CMakeLists.txt" DESTINATION "${SOURCE_PATH}")
file(COPY "${CMAKE_CURRENT_LIST_DIR}/7zip-config.cmake.in" DESTINATION "${SOURCE_PATH}")

vcpkg_cmake_get_vars(cmake_vars_file)
include("${cmake_vars_file}")

if(VCPKG_TARGET_IS_ANDROID)
    message(STATUS "Disable TIME_UTC on android")
    vcpkg_replace_string("${SOURCE_PATH}/CPP/Windows/TimeUtils.cpp"
        [[if defined(TIME_UTC)]]
        [[if defined(TIME_UTC) && !defined(__ANDROID__)]]
    )
endif()

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
)

vcpkg_cmake_install()
vcpkg_copy_pdbs()

vcpkg_cmake_config_fixup()

vcpkg_install_copyright(FILE_LIST "${SOURCE_PATH}/DOC/License.txt")

file(REMOVE_RECURSE "${CURRENT_PACKAGES_DIR}/debug/include")
