
(cl:in-package :asdf)

(defsystem "br_behavior_engine-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "StringList" :depends-on ("_package_StringList"))
    (:file "_package_StringList" :depends-on ("_package"))
  ))