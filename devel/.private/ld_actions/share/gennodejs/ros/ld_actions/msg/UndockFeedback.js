// Auto-generated. Do not edit!

// (in-package ld_actions.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class UndockFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.received_data = null;
    }
    else {
      if (initObj.hasOwnProperty('received_data')) {
        this.received_data = initObj.received_data
      }
      else {
        this.received_data = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type UndockFeedback
    // Serialize message field [received_data]
    bufferOffset = _serializer.string(obj.received_data, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type UndockFeedback
    let len;
    let data = new UndockFeedback(null);
    // Deserialize message field [received_data]
    data.received_data = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.received_data.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ld_actions/UndockFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0db3bc19eeede9e4ee493e93f03da761';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    # Feedback
    string received_data
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new UndockFeedback(null);
    if (msg.received_data !== undefined) {
      resolved.received_data = msg.received_data;
    }
    else {
      resolved.received_data = ''
    }

    return resolved;
    }
};

module.exports = UndockFeedback;