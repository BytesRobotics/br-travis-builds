#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "image_proc::image_proc" for configuration ""
set_property(TARGET image_proc::image_proc APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(image_proc::image_proc PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libimage_proc.so"
  IMPORTED_SONAME_NOCONFIG "libimage_proc.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS image_proc::image_proc )
list(APPEND _IMPORT_CHECK_FILES_FOR_image_proc::image_proc "${_IMPORT_PREFIX}/lib/libimage_proc.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
