
(cl:in-package :asdf)

(defsystem "bno055-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "bno055_info" :depends-on ("_package_bno055_info"))
    (:file "_package_bno055_info" :depends-on ("_package"))
  ))