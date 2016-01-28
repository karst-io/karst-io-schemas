package schemas.karst.io;

message Vector {
  required string uuid = 0;
  required float distance = 1;
  required float azimuth = 2;
  required float inclination = 3;
}

message Station {
  required string uuid = 0;
  required string name = 1;
  int32 dimension_left = 2;
  int32 dimension_right = 3;
  int32 dimension_up = 4;
  int32 dimension_down = 5;
  string description = 6;
}

message Shot {
  required string uuid = 0;
  required Station from = 1;
  required Station to = 2;
  Vector frontsight = 3;
  Vector backsight = 4;
  string comments = 5;
}

message Survey {
  required string uuid = 0;
  required string name = 1;
  string date = 2;
  repeated Shot shots = 3;
}