; Auto-generated. Do not edit!


(cl:in-package br_behavior_engine-srv)


;//! \htmlinclude StringList-request.msg.html

(cl:defclass <StringList-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StringList-request (<StringList-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StringList-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StringList-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name br_behavior_engine-srv:<StringList-request> is deprecated: use br_behavior_engine-srv:StringList-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StringList-request>) ostream)
  "Serializes a message object of type '<StringList-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StringList-request>) istream)
  "Deserializes a message object of type '<StringList-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StringList-request>)))
  "Returns string type for a service object of type '<StringList-request>"
  "br_behavior_engine/StringListRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StringList-request)))
  "Returns string type for a service object of type 'StringList-request"
  "br_behavior_engine/StringListRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StringList-request>)))
  "Returns md5sum for a message object of type '<StringList-request>"
  "cce5a364f3a3be12c9722c6dcad2fa94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StringList-request)))
  "Returns md5sum for a message object of type 'StringList-request"
  "cce5a364f3a3be12c9722c6dcad2fa94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StringList-request>)))
  "Returns full string definition for message of type '<StringList-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StringList-request)))
  "Returns full string definition for message of type 'StringList-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StringList-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StringList-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StringList-request
))
;//! \htmlinclude StringList-response.msg.html

(cl:defclass <StringList-response> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass StringList-response (<StringList-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StringList-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StringList-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name br_behavior_engine-srv:<StringList-response> is deprecated: use br_behavior_engine-srv:StringList-response instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <StringList-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader br_behavior_engine-srv:data-val is deprecated.  Use br_behavior_engine-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StringList-response>) ostream)
  "Serializes a message object of type '<StringList-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StringList-response>) istream)
  "Deserializes a message object of type '<StringList-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StringList-response>)))
  "Returns string type for a service object of type '<StringList-response>"
  "br_behavior_engine/StringListResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StringList-response)))
  "Returns string type for a service object of type 'StringList-response"
  "br_behavior_engine/StringListResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StringList-response>)))
  "Returns md5sum for a message object of type '<StringList-response>"
  "cce5a364f3a3be12c9722c6dcad2fa94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StringList-response)))
  "Returns md5sum for a message object of type 'StringList-response"
  "cce5a364f3a3be12c9722c6dcad2fa94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StringList-response>)))
  "Returns full string definition for message of type '<StringList-response>"
  (cl:format cl:nil "string[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StringList-response)))
  "Returns full string definition for message of type 'StringList-response"
  (cl:format cl:nil "string[] data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StringList-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StringList-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StringList-response
    (cl:cons ':data (data msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StringList)))
  'StringList-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StringList)))
  'StringList-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StringList)))
  "Returns string type for a service object of type '<StringList>"
  "br_behavior_engine/StringList")