# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "br_behavior_engine: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ibr_behavior_engine:/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(br_behavior_engine_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_custom_target(_br_behavior_engine_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "br_behavior_engine" "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" ""
)

get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_custom_target(_br_behavior_engine_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "br_behavior_engine" "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/br_behavior_engine
)

### Generating Services
_generate_srv_cpp(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/br_behavior_engine
)

### Generating Module File
_generate_module_cpp(br_behavior_engine
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/br_behavior_engine
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(br_behavior_engine_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(br_behavior_engine_generate_messages br_behavior_engine_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_cpp _br_behavior_engine_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_cpp _br_behavior_engine_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(br_behavior_engine_gencpp)
add_dependencies(br_behavior_engine_gencpp br_behavior_engine_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS br_behavior_engine_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/br_behavior_engine
)

### Generating Services
_generate_srv_eus(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/br_behavior_engine
)

### Generating Module File
_generate_module_eus(br_behavior_engine
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/br_behavior_engine
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(br_behavior_engine_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(br_behavior_engine_generate_messages br_behavior_engine_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_eus _br_behavior_engine_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_eus _br_behavior_engine_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(br_behavior_engine_geneus)
add_dependencies(br_behavior_engine_geneus br_behavior_engine_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS br_behavior_engine_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/br_behavior_engine
)

### Generating Services
_generate_srv_lisp(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/br_behavior_engine
)

### Generating Module File
_generate_module_lisp(br_behavior_engine
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/br_behavior_engine
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(br_behavior_engine_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(br_behavior_engine_generate_messages br_behavior_engine_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_lisp _br_behavior_engine_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_lisp _br_behavior_engine_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(br_behavior_engine_genlisp)
add_dependencies(br_behavior_engine_genlisp br_behavior_engine_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS br_behavior_engine_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/br_behavior_engine
)

### Generating Services
_generate_srv_nodejs(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/br_behavior_engine
)

### Generating Module File
_generate_module_nodejs(br_behavior_engine
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/br_behavior_engine
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(br_behavior_engine_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(br_behavior_engine_generate_messages br_behavior_engine_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_nodejs _br_behavior_engine_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_nodejs _br_behavior_engine_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(br_behavior_engine_gennodejs)
add_dependencies(br_behavior_engine_gennodejs br_behavior_engine_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS br_behavior_engine_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine
)

### Generating Services
_generate_srv_py(br_behavior_engine
  "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine
)

### Generating Module File
_generate_module_py(br_behavior_engine
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(br_behavior_engine_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(br_behavior_engine_generate_messages br_behavior_engine_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/srv/StringList.srv" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_py _br_behavior_engine_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/travis/build/BytesRobotics/br-core/catkin_ws/src/br-behavior-engine/msg/Events.msg" NAME_WE)
add_dependencies(br_behavior_engine_generate_messages_py _br_behavior_engine_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(br_behavior_engine_genpy)
add_dependencies(br_behavior_engine_genpy br_behavior_engine_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS br_behavior_engine_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/br_behavior_engine)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/br_behavior_engine
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(br_behavior_engine_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/br_behavior_engine)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/br_behavior_engine
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(br_behavior_engine_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/br_behavior_engine)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/br_behavior_engine
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(br_behavior_engine_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/br_behavior_engine)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/br_behavior_engine
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(br_behavior_engine_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine)
  install(CODE "execute_process(COMMAND \"/opt/pyenv/shims/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/br_behavior_engine
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(br_behavior_engine_generate_messages_py std_msgs_generate_messages_py)
endif()
