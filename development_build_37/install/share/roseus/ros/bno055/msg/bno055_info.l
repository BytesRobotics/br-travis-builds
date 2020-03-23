;; Auto-generated. Do not edit!


(when (boundp 'bno055::bno055_info)
  (if (not (find-package "BNO055"))
    (make-package "BNO055"))
  (shadow 'bno055_info (find-package "BNO055")))
(unless (find-package "BNO055::BNO055_INFO")
  (make-package "BNO055::BNO055_INFO"))

(in-package "ROS")
;;//! \htmlinclude bno055_info.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass bno055::bno055_info
  :super ros::object
  :slots (_header _tempC _accelCalibration _gyroCalibration _magnoCalibration _sysCalibration ))

(defmethod bno055::bno055_info
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:tempC __tempC) 0.0)
    ((:accelCalibration __accelCalibration) 0)
    ((:gyroCalibration __gyroCalibration) 0)
    ((:magnoCalibration __magnoCalibration) 0)
    ((:sysCalibration __sysCalibration) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _tempC (float __tempC))
   (setq _accelCalibration (round __accelCalibration))
   (setq _gyroCalibration (round __gyroCalibration))
   (setq _magnoCalibration (round __magnoCalibration))
   (setq _sysCalibration (round __sysCalibration))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:tempC
   (&optional __tempC)
   (if __tempC (setq _tempC __tempC)) _tempC)
  (:accelCalibration
   (&optional __accelCalibration)
   (if __accelCalibration (setq _accelCalibration __accelCalibration)) _accelCalibration)
  (:gyroCalibration
   (&optional __gyroCalibration)
   (if __gyroCalibration (setq _gyroCalibration __gyroCalibration)) _gyroCalibration)
  (:magnoCalibration
   (&optional __magnoCalibration)
   (if __magnoCalibration (setq _magnoCalibration __magnoCalibration)) _magnoCalibration)
  (:sysCalibration
   (&optional __sysCalibration)
   (if __sysCalibration (setq _sysCalibration __sysCalibration)) _sysCalibration)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _tempC
    8
    ;; uint8 _accelCalibration
    1
    ;; uint8 _gyroCalibration
    1
    ;; uint8 _magnoCalibration
    1
    ;; uint8 _sysCalibration
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _tempC
       (sys::poke _tempC (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint8 _accelCalibration
       (write-byte _accelCalibration s)
     ;; uint8 _gyroCalibration
       (write-byte _gyroCalibration s)
     ;; uint8 _magnoCalibration
       (write-byte _magnoCalibration s)
     ;; uint8 _sysCalibration
       (write-byte _sysCalibration s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _tempC
     (setq _tempC (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint8 _accelCalibration
     (setq _accelCalibration (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _gyroCalibration
     (setq _gyroCalibration (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _magnoCalibration
     (setq _magnoCalibration (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _sysCalibration
     (setq _sysCalibration (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get bno055::bno055_info :md5sum-) "c1818d2af59dc79e8470c9bf920f48a8")
(setf (get bno055::bno055_info :datatype-) "bno055/bno055_info")
(setf (get bno055::bno055_info :definition-)
      "Header header

float64 tempC
uint8 accelCalibration
uint8 gyroCalibration
uint8 magnoCalibration
uint8 sysCalibration


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :bno055/bno055_info "c1818d2af59dc79e8470c9bf920f48a8")


