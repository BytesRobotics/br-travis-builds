// Auto-generated. Do not edit!

// (in-package bno055.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class bno055_info {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.tempC = null;
      this.accelCalibration = null;
      this.gyroCalibration = null;
      this.magnoCalibration = null;
      this.sysCalibration = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('tempC')) {
        this.tempC = initObj.tempC
      }
      else {
        this.tempC = 0.0;
      }
      if (initObj.hasOwnProperty('accelCalibration')) {
        this.accelCalibration = initObj.accelCalibration
      }
      else {
        this.accelCalibration = 0;
      }
      if (initObj.hasOwnProperty('gyroCalibration')) {
        this.gyroCalibration = initObj.gyroCalibration
      }
      else {
        this.gyroCalibration = 0;
      }
      if (initObj.hasOwnProperty('magnoCalibration')) {
        this.magnoCalibration = initObj.magnoCalibration
      }
      else {
        this.magnoCalibration = 0;
      }
      if (initObj.hasOwnProperty('sysCalibration')) {
        this.sysCalibration = initObj.sysCalibration
      }
      else {
        this.sysCalibration = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type bno055_info
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [tempC]
    bufferOffset = _serializer.float64(obj.tempC, buffer, bufferOffset);
    // Serialize message field [accelCalibration]
    bufferOffset = _serializer.uint8(obj.accelCalibration, buffer, bufferOffset);
    // Serialize message field [gyroCalibration]
    bufferOffset = _serializer.uint8(obj.gyroCalibration, buffer, bufferOffset);
    // Serialize message field [magnoCalibration]
    bufferOffset = _serializer.uint8(obj.magnoCalibration, buffer, bufferOffset);
    // Serialize message field [sysCalibration]
    bufferOffset = _serializer.uint8(obj.sysCalibration, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type bno055_info
    let len;
    let data = new bno055_info(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [tempC]
    data.tempC = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [accelCalibration]
    data.accelCalibration = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [gyroCalibration]
    data.gyroCalibration = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [magnoCalibration]
    data.magnoCalibration = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [sysCalibration]
    data.sysCalibration = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bno055/bno055_info';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c1818d2af59dc79e8470c9bf920f48a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new bno055_info(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.tempC !== undefined) {
      resolved.tempC = msg.tempC;
    }
    else {
      resolved.tempC = 0.0
    }

    if (msg.accelCalibration !== undefined) {
      resolved.accelCalibration = msg.accelCalibration;
    }
    else {
      resolved.accelCalibration = 0
    }

    if (msg.gyroCalibration !== undefined) {
      resolved.gyroCalibration = msg.gyroCalibration;
    }
    else {
      resolved.gyroCalibration = 0
    }

    if (msg.magnoCalibration !== undefined) {
      resolved.magnoCalibration = msg.magnoCalibration;
    }
    else {
      resolved.magnoCalibration = 0
    }

    if (msg.sysCalibration !== undefined) {
      resolved.sysCalibration = msg.sysCalibration;
    }
    else {
      resolved.sysCalibration = 0
    }

    return resolved;
    }
};

module.exports = bno055_info;
