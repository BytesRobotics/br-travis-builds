// Auto-generated. Do not edit!

// (in-package br_behavior_engine.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Events {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.video = null;
      this.wifi = null;
    }
    else {
      if (initObj.hasOwnProperty('video')) {
        this.video = initObj.video
      }
      else {
        this.video = false;
      }
      if (initObj.hasOwnProperty('wifi')) {
        this.wifi = initObj.wifi
      }
      else {
        this.wifi = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Events
    // Serialize message field [video]
    bufferOffset = _serializer.bool(obj.video, buffer, bufferOffset);
    // Serialize message field [wifi]
    bufferOffset = _serializer.bool(obj.wifi, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Events
    let len;
    let data = new Events(null);
    // Deserialize message field [video]
    data.video = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [wifi]
    data.wifi = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a message object
    return 'br_behavior_engine/Events';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99fe8136a00e34efa272b67df2febcbb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool video
    bool wifi
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Events(null);
    if (msg.video !== undefined) {
      resolved.video = msg.video;
    }
    else {
      resolved.video = false
    }

    if (msg.wifi !== undefined) {
      resolved.wifi = msg.wifi;
    }
    else {
      resolved.wifi = false
    }

    return resolved;
    }
};

module.exports = Events;
