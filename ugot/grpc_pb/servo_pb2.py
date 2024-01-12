# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: servo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bservo.proto\x12\x0cServoPackage\"\x1c\n\x1aRoboticArmGetJointsRequest\"?\n\x17RoboticArmGetJointsInfo\x12\x12\n\njoint_name\x18\x01 \x01(\x05\x12\x10\n\x08joint_id\x18\x02 \x01(\t\"o\n\x1bRoboticArmGetJointsResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x35\n\x06joints\x18\x03 \x03(\x0b\x32%.ServoPackage.RoboticArmGetJointsInfo\"+\n\x19\x43ontrolSingleClampRequest\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x17\n\x15GetClampStatusRequest\"C\n\x16GetClampStatusResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\x05\"0\n\x13ServoCommonResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\">\n\x0eServoSpeedInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\r\n\x05speed\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x65v\x18\x03 \x01(\x05\"P\n\x0eServoAngleInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x05\x12\r\n\x05\x61ngle\x18\x03 \x01(\x05\x12\x0b\n\x03\x64\x65v\x18\x04 \x01(\x05\"@\n\x0cServoPWMInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x11\n\tpwm_speed\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x65v\x18\x03 \x01(\x05\"O\n\x19ServoRotateBySpeedRequest\x12\x32\n\x0cservo_rotate\x18\x01 \x03(\x0b\x32\x1c.ServoPackage.ServoSpeedInfo\"O\n\x19ServoRotateByAngleRequest\x12\x32\n\x0cservo_rotate\x18\x01 \x03(\x0b\x32\x1c.ServoPackage.ServoAngleInfo\"K\n\x17ServoRotateByPWMRequest\x12\x30\n\x0cservo_rotate\x18\x01 \x03(\x0b\x32\x1a.ServoPackage.ServoPWMInfo\"0\n\x13ServoRotateResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\";\n\x0cGetAngleInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\"F\n\x14ServoGetAngleRequest\x12.\n\nangle_info\x18\x01 \x03(\x0b\x32\x1a.ServoPackage.GetAngleInfo\"d\n\x15ServoGetAngleResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x30\n\nangle_list\x18\x03 \x03(\x0b\x32\x1c.ServoPackage.ServoAngleInfo\"0\n\x0fGetRotatingInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\"O\n\x17ServoGetRotatingRequest\x12\x34\n\rrotating_list\x18\x01 \x03(\x0b\x32\x1d.ServoPackage.GetRotatingInfo\"D\n\x11ServoRotatingInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x10\n\x08rotating\x18\x02 \x01(\x08\x12\x0b\n\x03\x64\x65v\x18\x03 \x01(\x05\"f\n\x18ServoGetRotatingResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12/\n\x06status\x18\x03 \x03(\x0b\x32\x1f.ServoPackage.ServoRotatingInfo\"<\n\rServoStopInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x65v\x18\x03 \x01(\x05\"Y\n\x16StopServoRotateRequest\x12/\n\nservo_list\x18\x01 \x03(\x0b\x32\x1b.ServoPackage.ServoStopInfo\x12\x0e\n\x06is_all\x18\x02 \x01(\x08\"_\n\rGetMotionInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\x12\x10\n\x08position\x18\x03 \x01(\x05\x12\r\n\x05speed\x18\x04 \x01(\x05\x12\x0e\n\x06torque\x18\x05 \x01(\x05\"H\n\x14GetMotionInfoRequest\x12\x30\n\x0bmotion_info\x18\x01 \x03(\x0b\x32\x1b.ServoPackage.GetMotionInfo\"d\n\x15GetMotionInfoResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x30\n\x0bmotion_list\x18\x03 \x03(\x0b\x32\x1b.ServoPackage.GetMotionInfo\"\x1a\n\x18RoboticArmRestoryRequest\"O\n\x1aRoboticArmMovePostionParam\x12\t\n\x01r\x18\x01 \x01(\x05\x12\t\n\x01h\x18\x02 \x01(\x05\x12\r\n\x05theta\x18\x03 \x01(\x01\x12\x0c\n\x04time\x18\x04 \x01(\x05\"X\n\x1cRoboticArmMovePostionRequest\x12\x38\n\x06params\x18\x01 \x01(\x0b\x32(.ServoPackage.RoboticArmMovePostionParam\"^\n\x1fRoboticArmSetJointPositionParam\x12\r\n\x05joint\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x05\x12\x0c\n\x04time\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\"b\n!RoboticArmSetJointPositionRequest\x12=\n\x06params\x18\x01 \x03(\x0b\x32-.ServoPackage.RoboticArmSetJointPositionParam\"?\n\x0fServoFaultClear\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\x12\r\n\x05\x66\x61ult\x18\x03 \x01(\x05\"G\n\x16ServoFaultClearRequest\x12-\n\x06params\x18\x01 \x03(\x0b\x32\x1d.ServoPackage.ServoFaultClear\"+\n\nServoFault\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\"=\n\x11ServoFaultRequest\x12(\n\x06params\x18\x01 \x03(\x0b\x32\x18.ServoPackage.ServoFault\"?\n\x0eServoFaultInfo\x12\x10\n\x08\x64\x65viceId\x18\x01 \x01(\t\x12\x0b\n\x03\x64\x65v\x18\x02 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\"[\n\x12ServoFaultResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12*\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x1c.ServoPackage.ServoFaultInfo2\xea\x0b\n\x10ServoServiceGrpc\x12\x65\n\x15setServoRotateBySpeed\x12\'.ServoPackage.ServoRotateBySpeedRequest\x1a!.ServoPackage.ServoRotateResponse\"\x00\x12\x65\n\x15setServoRotateByAngle\x12\'.ServoPackage.ServoRotateByAngleRequest\x1a!.ServoPackage.ServoRotateResponse\"\x00\x12\x61\n\x13setServoRotateByPWM\x12%.ServoPackage.ServoRotateByPWMRequest\x1a!.ServoPackage.ServoRotateResponse\"\x00\x12\\\n\x0fstopServoRotate\x12$.ServoPackage.StopServoRotateRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12Z\n\rgetServoAngle\x12\".ServoPackage.ServoGetAngleRequest\x1a#.ServoPackage.ServoGetAngleResponse\"\x00\x12\x62\n\x0fisServoRotating\x12%.ServoPackage.ServoGetRotatingRequest\x1a&.ServoPackage.ServoGetRotatingResponse\"\x00\x12\\\n\x0f\x63learServoFault\x12$.ServoPackage.ServoFaultClearRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12T\n\rgetServoFault\x12\x1f.ServoPackage.ServoFaultRequest\x1a .ServoPackage.ServoFaultResponse\"\x00\x12\x62\n\x12\x63ontrolSingleClamp\x12\'.ServoPackage.ControlSingleClampRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12]\n\x0egetClampStatus\x12#.ServoPackage.GetClampStatusRequest\x1a$.ServoPackage.GetClampStatusResponse\"\x00\x12Z\n\rgetMotionInfo\x12\".ServoPackage.GetMotionInfoRequest\x1a#.ServoPackage.GetMotionInfoResponse\"\x00\x12`\n\x11roboticArmRestory\x12&.ServoPackage.RoboticArmRestoryRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12p\n\x1droboticArmMoveToTargetPostion\x12*.ServoPackage.RoboticArmMovePostionRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12r\n\x1aroboticArmSetJointPosition\x12/.ServoPackage.RoboticArmSetJointPositionRequest\x1a!.ServoPackage.ServoCommonResponse\"\x00\x12l\n\x13roboticArmGetJoints\x12(.ServoPackage.RoboticArmGetJointsRequest\x1a).ServoPackage.RoboticArmGetJointsResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'servo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROBOTICARMGETJOINTSREQUEST._serialized_start=29
  _ROBOTICARMGETJOINTSREQUEST._serialized_end=57
  _ROBOTICARMGETJOINTSINFO._serialized_start=59
  _ROBOTICARMGETJOINTSINFO._serialized_end=122
  _ROBOTICARMGETJOINTSRESPONSE._serialized_start=124
  _ROBOTICARMGETJOINTSRESPONSE._serialized_end=235
  _CONTROLSINGLECLAMPREQUEST._serialized_start=237
  _CONTROLSINGLECLAMPREQUEST._serialized_end=280
  _GETCLAMPSTATUSREQUEST._serialized_start=282
  _GETCLAMPSTATUSREQUEST._serialized_end=305
  _GETCLAMPSTATUSRESPONSE._serialized_start=307
  _GETCLAMPSTATUSRESPONSE._serialized_end=374
  _SERVOCOMMONRESPONSE._serialized_start=376
  _SERVOCOMMONRESPONSE._serialized_end=424
  _SERVOSPEEDINFO._serialized_start=426
  _SERVOSPEEDINFO._serialized_end=488
  _SERVOANGLEINFO._serialized_start=490
  _SERVOANGLEINFO._serialized_end=570
  _SERVOPWMINFO._serialized_start=572
  _SERVOPWMINFO._serialized_end=636
  _SERVOROTATEBYSPEEDREQUEST._serialized_start=638
  _SERVOROTATEBYSPEEDREQUEST._serialized_end=717
  _SERVOROTATEBYANGLEREQUEST._serialized_start=719
  _SERVOROTATEBYANGLEREQUEST._serialized_end=798
  _SERVOROTATEBYPWMREQUEST._serialized_start=800
  _SERVOROTATEBYPWMREQUEST._serialized_end=875
  _SERVOROTATERESPONSE._serialized_start=877
  _SERVOROTATERESPONSE._serialized_end=925
  _GETANGLEINFO._serialized_start=927
  _GETANGLEINFO._serialized_end=986
  _SERVOGETANGLEREQUEST._serialized_start=988
  _SERVOGETANGLEREQUEST._serialized_end=1058
  _SERVOGETANGLERESPONSE._serialized_start=1060
  _SERVOGETANGLERESPONSE._serialized_end=1160
  _GETROTATINGINFO._serialized_start=1162
  _GETROTATINGINFO._serialized_end=1210
  _SERVOGETROTATINGREQUEST._serialized_start=1212
  _SERVOGETROTATINGREQUEST._serialized_end=1291
  _SERVOROTATINGINFO._serialized_start=1293
  _SERVOROTATINGINFO._serialized_end=1361
  _SERVOGETROTATINGRESPONSE._serialized_start=1363
  _SERVOGETROTATINGRESPONSE._serialized_end=1465
  _SERVOSTOPINFO._serialized_start=1467
  _SERVOSTOPINFO._serialized_end=1527
  _STOPSERVOROTATEREQUEST._serialized_start=1529
  _STOPSERVOROTATEREQUEST._serialized_end=1618
  _GETMOTIONINFO._serialized_start=1620
  _GETMOTIONINFO._serialized_end=1715
  _GETMOTIONINFOREQUEST._serialized_start=1717
  _GETMOTIONINFOREQUEST._serialized_end=1789
  _GETMOTIONINFORESPONSE._serialized_start=1791
  _GETMOTIONINFORESPONSE._serialized_end=1891
  _ROBOTICARMRESTORYREQUEST._serialized_start=1893
  _ROBOTICARMRESTORYREQUEST._serialized_end=1919
  _ROBOTICARMMOVEPOSTIONPARAM._serialized_start=1921
  _ROBOTICARMMOVEPOSTIONPARAM._serialized_end=2000
  _ROBOTICARMMOVEPOSTIONREQUEST._serialized_start=2002
  _ROBOTICARMMOVEPOSTIONREQUEST._serialized_end=2090
  _ROBOTICARMSETJOINTPOSITIONPARAM._serialized_start=2092
  _ROBOTICARMSETJOINTPOSITIONPARAM._serialized_end=2186
  _ROBOTICARMSETJOINTPOSITIONREQUEST._serialized_start=2188
  _ROBOTICARMSETJOINTPOSITIONREQUEST._serialized_end=2286
  _SERVOFAULTCLEAR._serialized_start=2288
  _SERVOFAULTCLEAR._serialized_end=2351
  _SERVOFAULTCLEARREQUEST._serialized_start=2353
  _SERVOFAULTCLEARREQUEST._serialized_end=2424
  _SERVOFAULT._serialized_start=2426
  _SERVOFAULT._serialized_end=2469
  _SERVOFAULTREQUEST._serialized_start=2471
  _SERVOFAULTREQUEST._serialized_end=2532
  _SERVOFAULTINFO._serialized_start=2534
  _SERVOFAULTINFO._serialized_end=2597
  _SERVOFAULTRESPONSE._serialized_start=2599
  _SERVOFAULTRESPONSE._serialized_end=2690
  _SERVOSERVICEGRPC._serialized_start=2693
  _SERVOSERVICEGRPC._serialized_end=4207
# @@protoc_insertion_point(module_scope)