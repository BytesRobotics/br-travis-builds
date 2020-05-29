;; Auto-generated. Do not edit!


(when (boundp 'br_behavior_engine::Events)
  (if (not (find-package "BR_BEHAVIOR_ENGINE"))
    (make-package "BR_BEHAVIOR_ENGINE"))
  (shadow 'Events (find-package "BR_BEHAVIOR_ENGINE")))
(unless (find-package "BR_BEHAVIOR_ENGINE::EVENTS")
  (make-package "BR_BEHAVIOR_ENGINE::EVENTS"))

(in-package "ROS")
;;//! \htmlinclude Events.msg.html


(defclass br_behavior_engine::Events
  :super ros::object
  :slots (_video _wifi ))

(defmethod br_behavior_engine::Events
  (:init
   (&key
    ((:video __video) nil)
    ((:wifi __wifi) nil)
    )
   (send-super :init)
   (setq _video __video)
   (setq _wifi __wifi)
   self)
  (:video
   (&optional __video)
   (if __video (setq _video __video)) _video)
  (:wifi
   (&optional __wifi)
   (if __wifi (setq _wifi __wifi)) _wifi)
  (:serialization-length
   ()
   (+
    ;; bool _video
    1
    ;; bool _wifi
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _video
       (if _video (write-byte -1 s) (write-byte 0 s))
     ;; bool _wifi
       (if _wifi (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _video
     (setq _video (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _wifi
     (setq _wifi (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get br_behavior_engine::Events :md5sum-) "99fe8136a00e34efa272b67df2febcbb")
(setf (get br_behavior_engine::Events :datatype-) "br_behavior_engine/Events")
(setf (get br_behavior_engine::Events :definition-)
      "bool video
bool wifi
")



(provide :br_behavior_engine/Events "99fe8136a00e34efa272b67df2febcbb")


