#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gscam::subscriber_node" for configuration ""
set_property(TARGET gscam::subscriber_node APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(gscam::subscriber_node PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libsubscriber_node.so"
  IMPORTED_SONAME_NOCONFIG "libsubscriber_node.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS gscam::subscriber_node )
list(APPEND _IMPORT_CHECK_FILES_FOR_gscam::subscriber_node "${_IMPORT_PREFIX}/lib/libsubscriber_node.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
