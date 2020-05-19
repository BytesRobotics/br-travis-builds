; Auto-generated. Do not edit!


(cl:in-package bno055-msg)


;//! \htmlinclude bno055_info.msg.html

(cl:defclass <bno055_info> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (tempC
    :reader tempC
    :initarg :tempC
    :type cl:float
    :initform 0.0)
   (accelCalibration
    :reader accelCalibration
    :initarg :accelCalibration
    :type cl:fixnum
    :initform 0)
   (gyroCalibration
    :reader gyroCalibration
    :initarg :gyroCalibration
    :type cl:fixnum
    :initform 0)
   (magnoCalibration
    :reader magnoCalibration
    :initarg :magnoCalibration
    :type cl:fixnum
    :initform 0)
   (sysCalibration
    :reader sysCalibration
    :initarg :sysCalibration
    :type cl:fixnum
    :initform 0))
)

(cl:defclass bno055_info (<bno055_info>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bno055_info>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bno055_info)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bno055-msg:<bno055_info> is deprecated: use bno055-msg:bno055_info instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:header-val is deprecated.  Use bno055-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'tempC-val :lambda-list '(m))
(cl:defmethod tempC-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:tempC-val is deprecated.  Use bno055-msg:tempC instead.")
  (tempC m))

(cl:ensure-generic-function 'accelCalibration-val :lambda-list '(m))
(cl:defmethod accelCalibration-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:accelCalibration-val is deprecated.  Use bno055-msg:accelCalibration instead.")
  (accelCalibration m))

(cl:ensure-generic-function 'gyroCalibration-val :lambda-list '(m))
(cl:defmethod gyroCalibration-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:gyroCalibration-val is deprecated.  Use bno055-msg:gyroCalibration instead.")
  (gyroCalibration m))

(cl:ensure-generic-function 'magnoCalibration-val :lambda-list '(m))
(cl:defmethod magnoCalibration-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:magnoCalibration-val is deprecated.  Use bno055-msg:magnoCalibration instead.")
  (magnoCalibration m))

(cl:ensure-generic-function 'sysCalibration-val :lambda-list '(m))
(cl:defmethod sysCalibration-val ((m <bno055_info>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055-msg:sysCalibration-val is deprecated.  Use bno055-msg:sysCalibration instead.")
  (sysCalibration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bno055_info>) ostream)
  "Serializes a message object of type '<bno055_info>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'tempC))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accelCalibration)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gyroCalibration)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'magnoCalibration)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'sysCalibration)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bno055_info>) istream)
  "Deserializes a message object of type '<bno055_info>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'tempC) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accelCalibration)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gyroCalibration)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'magnoCalibration)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'sysCalibration)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bno055_info>)))
  "Returns string type for a message object of type '<bno055_info>"
  "bno055/bno055_info")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bno055_info)))
  "Returns string type for a message object of type 'bno055_info"
  "bno055/bno055_info")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bno055_info>)))
  "Returns md5sum for a message object of type '<bno055_info>"
  "c1818d2af59dc79e8470c9bf920f48a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bno055_info)))
  "Returns md5sum for a message object of type 'bno055_info"
  "c1818d2af59dc79e8470c9bf920f48a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bno055_info>)))
  "Returns full string definition for message of type '<bno055_info>"
  (cl:format cl:nil "Header header~%~%float64 tempC~%uint8 accelCalibration~%uint8 gyroCalibration~%uint8 magnoCalibration~%uint8 sysCalibration~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bno055_info)))
  "Returns full string definition for message of type 'bno055_info"
  (cl:format cl:nil "Header header~%~%float64 tempC~%uint8 accelCalibration~%uint8 gyroCalibration~%uint8 magnoCalibration~%uint8 sysCalibration~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bno055_info>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     8
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bno055_info>))
  "Converts a ROS message object to a list"
  (cl:list 'bno055_info
    (cl:cons ':header (header msg))
    (cl:cons ':tempC (tempC msg))
    (cl:cons ':accelCalibration (accelCalibration msg))
    (cl:cons ':gyroCalibration (gyroCalibration msg))
    (cl:cons ':magnoCalibration (magnoCalibration msg))
    (cl:cons ':sysCalibration (sysCalibration msg))
))
