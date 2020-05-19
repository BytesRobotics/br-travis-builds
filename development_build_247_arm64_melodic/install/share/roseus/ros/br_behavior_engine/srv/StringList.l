;; Auto-generated. Do not edit!


(when (boundp 'br_behavior_engine::StringList)
  (if (not (find-package "BR_BEHAVIOR_ENGINE"))
    (make-package "BR_BEHAVIOR_ENGINE"))
  (shadow 'StringList (find-package "BR_BEHAVIOR_ENGINE")))
(unless (find-package "BR_BEHAVIOR_ENGINE::STRINGLIST")
  (make-package "BR_BEHAVIOR_ENGINE::STRINGLIST"))
(unless (find-package "BR_BEHAVIOR_ENGINE::STRINGLISTREQUEST")
  (make-package "BR_BEHAVIOR_ENGINE::STRINGLISTREQUEST"))
(unless (find-package "BR_BEHAVIOR_ENGINE::STRINGLISTRESPONSE")
  (make-package "BR_BEHAVIOR_ENGINE::STRINGLISTRESPONSE"))

(in-package "ROS")





(defclass br_behavior_engine::StringListRequest
  :super ros::object
  :slots ())

(defmethod br_behavior_engine::StringListRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass br_behavior_engine::StringListResponse
  :super ros::object
  :slots (_data ))

(defmethod br_behavior_engine::StringListResponse
  (:init
   (&key
    ((:data __data) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string[] _data
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _data
     (write-long (length _data) s)
     (dolist (elem _data)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _data i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(defclass br_behavior_engine::StringList
  :super ros::object
  :slots ())

(setf (get br_behavior_engine::StringList :md5sum-) "cce5a364f3a3be12c9722c6dcad2fa94")
(setf (get br_behavior_engine::StringList :datatype-) "br_behavior_engine/StringList")
(setf (get br_behavior_engine::StringList :request) br_behavior_engine::StringListRequest)
(setf (get br_behavior_engine::StringList :response) br_behavior_engine::StringListResponse)

(defmethod br_behavior_engine::StringListRequest
  (:response () (instance br_behavior_engine::StringListResponse :init)))

(setf (get br_behavior_engine::StringListRequest :md5sum-) "cce5a364f3a3be12c9722c6dcad2fa94")
(setf (get br_behavior_engine::StringListRequest :datatype-) "br_behavior_engine/StringListRequest")
(setf (get br_behavior_engine::StringListRequest :definition-)
      "---
string[] data
")

(setf (get br_behavior_engine::StringListResponse :md5sum-) "cce5a364f3a3be12c9722c6dcad2fa94")
(setf (get br_behavior_engine::StringListResponse :datatype-) "br_behavior_engine/StringListResponse")
(setf (get br_behavior_engine::StringListResponse :definition-)
      "---
string[] data
")



(provide :br_behavior_engine/StringList "cce5a364f3a3be12c9722c6dcad2fa94")


