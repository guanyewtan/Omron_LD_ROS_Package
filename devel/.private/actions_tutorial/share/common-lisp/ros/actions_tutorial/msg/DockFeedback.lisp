; Auto-generated. Do not edit!


(cl:in-package actions_tutorial-msg)


;//! \htmlinclude DockFeedback.msg.html

(cl:defclass <DockFeedback> (roslisp-msg-protocol:ros-message)
  ((received_data
    :reader received_data
    :initarg :received_data
    :type cl:string
    :initform ""))
)

(cl:defclass DockFeedback (<DockFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DockFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DockFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name actions_tutorial-msg:<DockFeedback> is deprecated: use actions_tutorial-msg:DockFeedback instead.")))

(cl:ensure-generic-function 'received_data-val :lambda-list '(m))
(cl:defmethod received_data-val ((m <DockFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader actions_tutorial-msg:received_data-val is deprecated.  Use actions_tutorial-msg:received_data instead.")
  (received_data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DockFeedback>) ostream)
  "Serializes a message object of type '<DockFeedback>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'received_data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'received_data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DockFeedback>) istream)
  "Deserializes a message object of type '<DockFeedback>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'received_data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'received_data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DockFeedback>)))
  "Returns string type for a message object of type '<DockFeedback>"
  "actions_tutorial/DockFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DockFeedback)))
  "Returns string type for a message object of type 'DockFeedback"
  "actions_tutorial/DockFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DockFeedback>)))
  "Returns md5sum for a message object of type '<DockFeedback>"
  "0db3bc19eeede9e4ee493e93f03da761")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DockFeedback)))
  "Returns md5sum for a message object of type 'DockFeedback"
  "0db3bc19eeede9e4ee493e93f03da761")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DockFeedback>)))
  "Returns full string definition for message of type '<DockFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%string received_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DockFeedback)))
  "Returns full string definition for message of type 'DockFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Feedback~%string received_data~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DockFeedback>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'received_data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DockFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'DockFeedback
    (cl:cons ':received_data (received_data msg))
))
