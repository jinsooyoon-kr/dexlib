

## define

NOP = 0x00
MOVE = 0x01
MOVE_FROM16 = 0x02
MOVE_16 = 0x03
MOVE_WIDE = 0x04
MOVE_WIDE_FROM16 = 0x05
MOVE_WIDE_16 = 0x06
MOVE_OBJECT = 0x07
MOVE_OBJECT_FROM16 = 0x08
MOVE_OBJECT_16 = 0x09
MOVE_RESULT = 0x0a
MOVE_RESULT_WIDE = 0x0b
MOVE_RESULT_OBJECT = 0x0c
MOVE_EXCEPTION = 0x0d
RETURN_VOID = 0x0e
RETURN = 0x0f
RETURN_WIDE = 0x10
RETURN_OBJECT = 0x11
CONST_4 = 0x12
CONST_16 = 0x13
CONST = 0x14
CONST_HIGH16 = 0x15
CONST_WIDE16 = 0x16
CONST_WIDE32 = 0x17
CONSD_WIDE = 0x18
CONST_WIDE_HIGH16 = 0x19
CONST_STRING = 0x1a
CONST_STRING_JUMBO = 0x1b
CONST_CLASS = 0x1c
MONITOR_ENTER = 0x1d
MONITOR_EXIT = 0x1e
CHECK_CAST = 0x1f
INSTANCE_OF = 0x20
ARRAY_LENGTH = 0x21
NEW_INSTANCE = 0x22
NEW_ARRAY = 0x23
FILLED_NEW_ARRAY = 0x24
FILLED_NEW_ARRAY_RANGE = 0x25
FILL_ARRAY_DATA = 0x26
THROW = 0x27
GOTO = 0x28
GOTO16 = 0x29
GOTO32 = 0x2a
PACKED_SIWTCH = 0x2b
SPARSE_SWITCH = 0x2c
CMPL_FLOAT = 0x2d
CMPL_FLOAT = 0x2e
CMPL_DOUBLE = 0x2f
CMPG_DOUBLE = 0x30
CMP_LONG = 0x31

IF_EQ = 0x32
IF_NE = 0x33
IF_LT = 0x34
IF_GE = 0x35
IF_GT = 0x36
IF_LE = 0x37

IF_EQZ = 0x38
IF_NEZ = 0x39
IF_LTZ = 0x3a
IF_GEZ = 0x3b
IF_GTZ = 0x3c
IF_LEZ = 0x3d

AGET = 0x44
AGET_WIDE = 0x45
AGET_OBJECT = 0x46
AGET_BOOLEAN = 0x47
AGET_BYTE = 0x48
AGET_CHAR = 0x49
AGET_SHORT = 0x4a

APUT = 0x4b
APUT_WIDE = 0x4c
APUT_OBJECT = 0x4d
APUT_BOOLEAN = 0x4e
APUT_BYTE = 0x4f
APUT_CHAR = 0x50
APUT_SHORT = 0x51

IGET = 0x52
IGET_WIDE = 0x53
IGET_OBJECT = 0x54
IGET_BOOLEAN = 0x55
IGET_BYTE = 0x56
IGET_CHAR = 0x57
IGET_SHORT = 0x58
IPUT = 0x59
IPUT_WIDE = 0x5a
IPUT_OBJECT = 0x5b
IPUT_BOOLEAN = 0x5c
IPUT_BYTE = 0x5d
IPUT_CHAR = 0x5e
IPUT_SHORT = 0x5f

SGET = 0x60
SGET_WIDE = 0x61
SGET_OBJECT = 0x62
SGET_BOOLEAN = 0x63
SGET_BYTE = 0x64
SGET_CHAR = 0x65
SGET_SHORT = 0x66
SPUT = 0x67
SPUT_WIDE = 0x68
SPUT_OBJECT = 0x69
SPUT_BOOLEAN = 0x6a
SPUT_BYTE = 0x6b
SPUT_CHAR = 0x6c
SPUT_SHORT = 0x6d

INVOKE_VIRTUAL = 0x6e
INVOKE_SUPER = 0x6f
INVOKE_DIRECT = 0x70
INVOKE_STATIC = 0x71
INVOKE_INTERFACE = 0x72

INVOKE_VIRTUAL_RANGE = 0x74
INVOKE_SUPER_RANGE = 0x75
INVOKE_DIRECT_RANGE = 0x76
INVOKE_STATIC_RANGE = 0x77
INVOKE_INTERFACE_RANGE = 0x78

NEG_INT = 0x7b
NOT_INT = 0x7c
NEG_LONG = 0x7d
NOT_LONG = 0x7e
NEG_FLOAT = 0x7f
NEG_DOUBLE = 0x80
INT_TO_LONG = 0x81
INT_TO_FLOAT = 0x82
INT_TO_DOUBLE = 0x83
LONG_TO_INT = 0x84
LONG_TO_FLOAT = 0x85
LONG_TO_DOUBLE = 0x86
FLOAT_TO_INT = 0x87
FLOAT_TO_LONG = 0x88
FLOAT_TO_DOUBLE = 0x89
DOUBLE_TO_INT = 0x8a
DOUBLE_TO_LONG = 0x8b
DOUBLE_TO_FLOAT = 0x8c
INT_TO_BYTE = 0x8d
INT_TO_CHAR = 0x8e
INT_TO_SHORT = 0x8f

ADD_INT = 0x90
SUB_INT = 0x91
MUL_INT = 0x92
DIV_INT = 0x93
REM_INT = 0x94
AND_INT = 0x95
OR_INT = 0x96
XOR_INT = 0x97
SHL_INT = 0x98
SHR_INT = 0x99
USHR_INT = 0x9a
ADD_LONG = 0x9b
SUB_LONG = 0x9c
MUL_LONG = 0x9d
DIV_LONG = 0x9e
REM_LONG = 0x9f
AND_LONG = 0xa0
OR_LONG = 0xa1
XOR_LONG = 0xa2
SHL_LONG = 0xa3
SHR_LONG = 0xa4
USHR_LONG = 0xa5
ADD_FLOAT = 0xa6



class ByteCodeHelper(object):

  @staticmethod
  def to_string(self, opcode):
    pass

  def to_opcode(self, string):
    pass




class DexByteCode(object):

  def __init__(self, manager):
    pass

  def get_op(self):
    raise Exception('get_op is not implemented')


class Instruction(object):

  def as_byte_stream(self):
    return bytes()
  
  def as_string(self):
    pass

  def from_string(self):
    pass

  def from_byte(self):
    pass

  def op_as_byte(self):
    return bytes(self.get_op())


class Instruction00x(Instruction):
  def as_byte_stream(self):
    return bytes()
  
  def as_string(self):
    pass

  def from_string(self):
    pass

  def from_byte(self):
    pass


class Instruction10x(Instruction):
  def as_byte_stream(self):
    return b'\x00' + self.op_as_byte

  def as_string(self):
    return self.get_opcode_string()

  def from_string(self):
    pass

  def from_byte(self):
    pass


