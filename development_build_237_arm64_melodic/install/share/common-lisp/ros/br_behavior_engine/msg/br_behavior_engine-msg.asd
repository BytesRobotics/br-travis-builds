
(cl:in-package :asdf)

(defsystem "br_behavior_engine-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Events" :depends-on ("_package_Events"))
    (:file "_package_Events" :depends-on ("_package"))
  ))