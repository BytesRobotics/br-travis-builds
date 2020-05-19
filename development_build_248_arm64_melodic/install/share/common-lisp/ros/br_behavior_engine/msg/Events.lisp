; Auto-generated. Do not edit!


(cl:in-package br_behavior_engine-msg)


;//! \htmlinclude Events.msg.html

(cl:defclass <Events> (roslisp-msg-protocol:ros-message)
  ((video
    :reader video
    :initarg :video
    :type cl:boolean
    :initform cl:nil)
   (wifi
    :reader wifi
    :initarg :wifi
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Events (<Events>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Events>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Events)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name br_behavior_engine-msg:<Events> is deprecated: use br_behavior_engine-msg:Events instead.")))

(cl:ensure-generic-function 'video-val :lambda-list '(m))
(cl:defmethod video-val ((m <Events>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader br_behavior_engine-msg:video-val is deprecated.  Use br_behavior_engine-msg:video instead.")
  (video m))

(cl:ensure-generic-function 'wifi-val :lambda-list '(m))
(cl:defmethod wifi-val ((m <Events>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader br_behavior_engine-msg:wifi-val is deprecated.  Use br_behavior_engine-msg:wifi instead.")
  (wifi m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Events>) ostream)
  "Serializes a message object of type '<Events>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'video) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'wifi) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Events>) istream)
  "Deserializes a message object of type '<Events>"
    (cl:setf (cl:slot-value msg 'video) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'wifi) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Events>)))
  "Returns string type for a message object of type '<Events>"
  "br_behavior_engine/Events")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Events)))
  "Returns string type for a message object of type 'Events"
  "br_behavior_engine/Events")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Events>)))
  "Returns md5sum for a message object of type '<Events>"
  "99fe8136a00e34efa272b67df2febcbb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Events)))
  "Returns md5sum for a message object of type 'Events"
  "99fe8136a00e34efa272b67df2febcbb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Events>)))
  "Returns full string definition for message of type '<Events>"
  (cl:format cl:nil "bool video~%bool wifi~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Events)))
  "Returns full string definition for message of type 'Events"
  (cl:format cl:nil "bool video~%bool wifi~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Events>))
  (cl:+ 0
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Events>))
  "Converts a ROS message object to a list"
  (cl:list 'Events
    (cl:cons ':video (video msg))
    (cl:cons ':wifi (wifi msg))
))
