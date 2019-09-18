from zlib import adler32
import struct
"""
parse dex

"""

BYTE = 1
UBYTE = 2
SHORT = 3
USHORT = 4
INT = 5
UINT = 6
LONG = 7
ULONG = 8
SLEB = 9
ULEB = 10
ULEBP1 = 11
STRING = 12

MAGIC = 13
SIGNATURE = 14


## def item, do not use instanceof() for speed
DEX_BASE = 0x100000
ITEM_HEADER = DEX_BASE | 1
STRING_ID_ITEM = DEX_BASE | 2
TYPE_ID_ITEM = DEX_BASE | 3
PROTO_ID_ITEM = DEX_BASE | 4
FIELD_ID_ITEM = DEX_BASE | 5
METHOD_ID_ITEM = DEX_BASE | 6
CLASS_DEF_ITEM = DEX_BASE | 7
CALL_SITE_ID_ITEM = DEX_BASE | 8
METHOD_HANDLE_ITEM = DEX_BASE | 9

ENCODED_VALUE = DEX_BASE | 10
ENCODED_ARRAY = DEX_BASE | 11
ENCODED_ANNOTATION = DEX_BASE | 12
ANNOTATION_ELEMENT = DEX_BASE | 13
ENCODED_FIELD = DEX_BASE | 14
ENCODED_METHOD = DEX_BASE | 15

#type codes
TYPE_HEADER_ITEM = 0x0000
TYPE_STRING_ID_ITEM = 0x0001
TYPE_TYPE_ID_ITEM = 0x0002
TYPE_PROTO_ID_ITEM = 0x0003
TYPE_FIELD_ID_ITEM = 0x0004
TYPE_METHOD_ID_ITEM = 0x0005
TYPE_CLASS_DEF_ITEM = 0x0006
TYPE_CALL_SITE_ID_ITEM = 0x0007
TYPE_METHOD_HANDLE_ITEM = 0x0008
TYPE_MAP_LIST = 0x1000
TYPE_TYPE_LIST = 0x1001
TYPE_ANNOTATION_SET_REF_LIST = 0x1002
TYPE_ANNOTATION_SET_ITEM = 0x1003
TYPE_CLASS_DATA_ITEM = 0x2000
TYPE_CODE_ITEM = 0x2001
TYPE_STRING_DATA_ITEM = 0x2002
TYPE_DEBUG_INFO_ITEM = 0x2003
TYPE_ANNOTATION_ITEM = 0x2004
TYPE_ENCODED_ARRAY_ITEM = 0x2005
TYPE_ANNOTATIONS_DIRECTORY_ITEM = 0x2006
TYPE_HIDDENAPI_CLASS_DATA_ITEM = 0xf000


#method handle type codes
METHOD_HANDLE_TYPE_STATIC_PUT = 0x00
METHOD_HANDLE_TYPE_STATIC_GET = 0x01
METHOD_HANDLE_TYPE_INSTANCE_PUT = 0x02
METHOD_HANDLE_TYPE_INSTANCE_GEt = 0x03
METHOD_HANDLE_TYPE_INVOKE_STATIC = 0x04
METHOD_HANDLE_TYPE_INVOKE_INSTANCE = 0x05
METHOD_HANDLE_TYPE_INVOKE_CONSTRUCTOR = 0x06
METHOD_HANDLE_TYPE_INVOKE_DIRECT = 0x07
METHOD_HANDLE_TYPE_INVOKE_INTERFACE = 0x08

# encoded value item
ENCODED_VALUE_BYTE = 0x00
ENCODED_VALUE_SHORT = 0x02
ENCODED_VALUE_CHAR = 0x03
ENCODED_VALUE_INT = 0x04
ENCODED_VALUE_LONG = 0x06
ENCODED_VALUE_FLOAT = 0x10
ENCODED_VALUE_DOUBLE = 0x11
ENCODED_VALUE_METHOD_TYPE = 0x15
ENCODED_VALUE_METHOD_HANDLE = 0x16
ENCODED_VALUE_STRING = 0x17
ENCODED_VALUE_TYPE = 0x18
ENCODED_VALUE_FIELD = 0x19
ENCODED_VALUE_METHOD = 0x1a
ENCODED_VALUE_ENUM = 0x1b
ENCODED_VALUE_ARRAY = 0x1c
ENCODED_VALUE_ANNOTATION = 0x1d
ENCODED_VALUE_NULL = 0x1e
ENCODED_VALUE_BOOLEAN = 0x1f


## ACCESS_FLAG
ACC_PUBLIC = 0x1
ACC_PRIVATE = 0x2
ACC_PROTECTED = 0x4
ACC_STATIC = 0x8
ACC_FINAL = 0x10
ACC_SYNCHRONIZED = 0x20
ACC_VOLATILE = 0x40
ACC_BRIDGE = 0x40
ACC_TRANSIENT = 0x80
ACC_VARARGS = 0x80
ACC_NATIVE = 0x100
ACC_INTERFACE = 0x200
ACC_ABSTRACT = 0x400
ACC_STRICT = 0x800
ACC_SYNTHETIC = 0x1000
ACC_ANNOTATION = 0x2000
ACC_ENUM = 0x4000
ACC_UNUSED = 0x8000
ACC_CONSTRUCTOR = 0x10000
ACC_DECLARED_SYNCHRONIZED = 0x20000

# VISIBILITY
VISIBILITY_BUILD = 0x00
VISIBILITY_RUNTIME = 0x01
VISIBILITY_SYSTEM = 0x02

# DEBUG_INFO_ITEM
NO_INDEX = 0xffffffff

MOD_ADLER = 65521

def calc_adler32(data, length):
  a = 1
  b = 0
  for i in range(length):
    a = (a + ord(data[i])) % MOD_ADLER
    b = (b + a) % MOD_ADLER
  return (b << 16) | a



class StreamReader(object):
  UINT_FMT = '<I'
  USHORT_FMT = '<H'
  INT_FMT = '<i'
  SHORT_FMT = '<h'
  LONG_FMT = '<l'
  ULONG_FMT = '<L'
  LONGLONG_FMT = '<q'
  ULONGLONG_FMT = '<Q'
  UBYTE_FMT = '<B'
  BYTE_FMT = '<b'

  def __init__(self, buf):
    self.buf = buf
    self.read_map = {
      BYTE: self.read_ubyte,
      UBYTE: self.read_ubyte,

      SHORT: self.read_ushort,
      USHORT: self.read_ushort,

      INT: self.read_uint,
      UINT: self.read_uint,

      LONG: self.read_ulong,
      ULONG: self.read_ulong,

      SLEB: self.read_sleb,
      ULEB: self.read_uleb,
      ULEBP1: self.read_ulebp1,
      STRING: self.read_string,

      MAGIC: self.read_magic,
      SIGNATURE: self.read_signature
    }
  def read_ubyte(self, index, *args):
    ret = self.__read(index, 1, *args)
    ret.value = struct.unpack(self.UBYTE_FMT, ret.value)[0]
    return ret
  
  def read_uint(self, index, *args):
    ret = self.__read(index, 4, *args)
    ret.value = struct.unpack(self.UINT_FMT, ret.value)[0]
    return ret

  def read_ushort(self, index, *args):
    ret = self.__read(index, 2, *args)
    ret.value = struct.unpack(self.USHORT_FMT, ret.value)[0]
    return ret

  def read_ulong(self, index, *args):
    ret = self.__read(index, 8, *args)
    ret.value = struct.unpack(self.ULONGLONG_FMT, ret.value)[0]
    return ret

  def read_magic(self, index, *args):
    ret = self.__read(index, 8, *args)
    return ret


  def read_signature(self, index, *args):
    ret = self.__read(index, 20, *args)
    return ret

  def read_string(self, index):
    s = 0
    size = 0
    ret = bytearray()
    while True:
      a = self.read_ubyte(index + size).value
      size += 1
      if a == 0:
        return DexPrimitive(ret.decode("utf-8"), size)
      if a < 0x80:
        ret.append(a)
      elif (a & 0xe0) == 0xc0:
        b = self.read_ubyte(index + size)
        size += 1
        if (b & 0xc0) != 0x80:
          raise Exception('BAD SECOND BYTE')
        data = (((a & 0x1f) << 6)) | (b & 0x3f)
        ret.append(data)
      elif a & 0xf0 == 0xe0:
        b = self.ubyte(index + size)
        c = self.ubyte(index + size)
        size += 2
        if ((b & 0xc0) != 0x80) or ((c & 0xc0) != 0x80):
          raise Exception('BAD THIRD BYTE')
        data = ((a & 0x0f) << 12) | ((b & 0x3f) << 6) | (c & 0x3f)
        ret.append(data)
      else:
        raise Exception('read_string error')

  def read_sleb(self, index):
    result = 0
    shift = 0
    size = 0
    while True:
      b = ord(self.read_ubyte(index + size))
      size += 1
      result |= ((b & 0x7f) << shift)
      shift += 7
      if b & 0x80 == 0: break
    
    if (b & 0x40):
      result |= -(1 << shift)
    return DexPrimitive(result, size)


  
  def read_uleb(self, index, *args):
    result = 0
    shift = 0
    size = 0
    while True:
      b = self.buf[index + size: index + size + 1][0]
      size += 1
      result |= ((b & 0x7f) << shift)
      shift += 7
      if b & 0x80 == 0: break
    
    return DexPrimitive(result, size)

  def read_ulebp1(self, index):
    ret = self.read_uleb(index)
    ret.val += 1
    return ret


  def __read(self, index, size, *args):
    return DexPrimitive(self.buf[index : index + size], size)

  def read_function(self, size):
    def __read(_self, index, *args):
      return DexPrimitive(self.buf[index : index + size], size)
    return __read


  def read(self, index, read_type, *args):
    fcn = self.read_map[read_type]
    return fcn(index, *args)
    
  def read_encoded_field(self, index):
    pass
  def read_encoded_method(self, index):
    pass
  def read_try_item(self, index):
    pass
  def read_encoded_catch_handler_list(self, index):
    pass
  def read_encoded_catch_handler(self, index):
    pass
  def read_encoded_type_addr_pair(self, index):
    pass
  def read_field_annotation(self, index):
    pass
  def read_method_annotation(self, index):
    pass
  def read_parameter_annotation(self, index):
    pass
  def read_annotation_set_item(self, index):
    pass
  def read_encoded_annotation(self, index):
    pass
  def read_encoded_array(self, index):
    pass
  def read_map_item(self, index):
    return MapItem(self, index)


class DexPrimitive(object):
  def __init__(self, val, size):
    self.value = val
    self.read_size = size


class DexItem(object):
  descriptor = None

  def __init__(self, root_stream, index):
    self.root_stream = root_stream
    self.base_index = index
    self.read_size = 0
    self.value_list = {}

    for name in self.descriptor:
      self.value_list[name] = None
    self.read_property()

  def read_property(self):
    for x in self.value_list:
      #print('read descriptor : {}'.format(x))
      #print('index : {} read_size : {}'.format(self.base_index, self.read_size))
      readobj = self.root_stream.read(self.base_index + self.read_size, self.descriptor[x])
      self.read_size += readobj.read_size
      self.value_list[x] = readobj.value

  def __getattr__(self, name):
    if name not in self.value_list:
      raise Exception('{} is not exist in {}'.format(name, self))

    return self.value_list[name]
  def __str__(self):
    ret = ''
    for x in self.value_list:
      ret += '{} : {}\n'.format(x, self.value_list[x])
    return ret
class EncodedValue(DexItem):
  def __init__(self, root_stream, index):
    self.read_size = 0
    value_type = root_stream.read_ubyte(index)
    self.read_size += value_type.size
    self.type = value_type.value & 0x1f
    self.value_size = ((value_type.value >> 5) & 0x7) + 1
    if self.type == ENCODED_VALUE_ARRAY:
      self.value = root_stream.read_encoded_array(index + self.read_size)
    elif self.type == ENCODED_VALUE_ANNOTATION:
      self.value = root_stream.read_encoded_annotation(index + self.read_size)
    elif self.type == ENCODED_VALUE_BOOLEAN:
      self.value = ((value_type.value >> 5) == 1)
    elif self.type == ENCODED_VALUE_NULL:
      self.value = None
    else: # later
      self.value = []
      for i in range(self.value_size):
        self.value.append(root_stream.read_ubyte(index + self.read_size).value)
        self.read_size += 1


class EncodedArray(DexItem):
  descriptor = {
    'size': ULEB
  }
  def __init__(self, root_stream, index):
    super(DexItem, self).__init__(self, root_stream, index)
    self.values = []
    for x in self.size:
      item = root_stream.read_encoded_value(index + self.read_size)
      self.values.append(item)
      self.read_size += item.size

class EncodedAnnotation(DexItem):
  descriptor = {
    'type_idx': ULEB,
    'size': ULEB
  }

  def __init__(self, root_stream, index):
    super(DexItem, self).__init__(self, root_stream, index)
    self.elements = []
    for x in self.size:
      item = root_stream.read_annotation_element(index + self.read_size)
      self.elements.append(item)
      self.read_size += item.size


class AnnotationElement(DexItem):
  descriptor = {
    'name_idx': ULEB,
    'value': ENCODED_VALUE
  }


class HeaderItem(DexItem):
  descriptor = {
    'magic': MAGIC,
    'checksum': UINT,
    'signature': SIGNATURE,
    'file_size': UINT,
    'header_size': UINT,
    'endian_tag': UINT,
    'link_size': UINT,
    'link_off': UINT,
    'map_off': UINT,
    'string_ids_off': UINT,
    'type_ids_size': UINT,
    'type_ids_off': UINT,
    'proto_ids_size': UINT,
    'proto_ids_off': UINT,
    'field_ids_size': UINT,
    'field_ids_off': UINT,
    'method_ids_size': UINT,
    'method_ids_off': UINT,
    'class_defs_size': UINT,
    'class_defs_off': UINT,
    'data_size': UINT,
    'data_off': UINT
  }

  def __init__(self, root_stream, index):
    super(HeaderItem, self).__init__(root_stream, index)
    if self.map_off != 0:
      self.map_list = MapList(root_stream, self.map_off)

class MapList(DexItem):
  descriptor = {
    'size': UINT
  }

  def __init__(self, root_stream, index):
    super(MapList, self).__init__(root_stream, index)
    self.list = {}

    for x in range(self.size):
      item = root_stream.read_map_item(index + self.read_size)
      item.parse_remain()
      self.list[item.type] = item
      self.read_size += item.read_size

  def __str__(self):
    base = super(MapList, self).__str__()
    for x in self.list:
      base += '{} : {}\n'.format(x, self.list[x])
    return base

  def get_string(self, index):
    string_id_items = self.list[TYPE_STRING_ID_ITEM]


class MapItem(DexItem):
  descriptor = {
    'type': USHORT,
    'unused': USHORT,
    'size': UINT,
    'offset': UINT
  }

  def parse_remain(self):
    if self.type == TYPE_HEADER_ITEM:
      pass
    if self.type == TYPE_STRING_ID_ITEM:
      index = self.offset
      for x in range(self.size):
        item = StringIdItem(self.root_stream, index)
        print(item.get_value().value)
        index += item.read_size
    elif self.type == TYPE_TYPE_ID_ITEM:
      pass
    elif self.type == TYPE_PROTO_ID_ITEM:
      pass
    elif self.type == TYPE_FIELD_ID_ITEM:
      pass
    elif self.type == TYPE_METHOD_ID_ITEM:
      pass
    elif self.type == TYPE_CLASS_DEF_ITEM:
      pass
    elif self.type == TYPE_CALL_SITE_ID_ITEM:
      pass
    elif self.type == TYPE_METHOD_HANDLE_ITEM:
      pass
    elif self.type == TYPE_MAP_LIST:
      pass
    elif self.type == TYPE_TYPE_LIST:
      pass
    elif self.type == TYPE_ANNOTATION_SET_REF_LIST:
      pass
    elif self.type == TYPE_ANNOTATION_SET_ITEM:
      pass
    elif self.type == TYPE_CLASS_DATA_ITEM:
      pass
    elif self.type == TYPE_CODE_ITEM:
      pass
    elif self.type == TYPE_STRING_DATA_ITEM:
      pass
    elif self.type == TYPE_DEBUG_INFO_ITEM:
      pass
    elif self.type == TYPE_ENCODED_ARRAY_ITEM:
      pass
    elif self.type == TYPE_ANNOTATIONS_DIRECTORY_ITEM:
      pass
    elif self.type == TYPE_HIDDENAPI_CLASS_DATA_ITEM:
      pass


class StringIdItem(DexItem):
  descriptor = {
    'string_data_off': UINT
  }
  def __init__(self, root_stream, index):
    super(StringIdItem, self).__init__(root_stream, index)
    self.string_value = None

  def get_value(self):
    if self.string_value is None:
      
      v = StringDataItem(self.root_stream, self.string_data_off)
      self.string_value = v.value
    return self.string_value

class StringDataItem(DexItem):
  descriptor = {
    'utf16_size': ULEB
  }
  def __init__(self, root_stream, index):
    super(StringDataItem, self).__init__(root_stream, index)
    self.value = root_stream.read_string(index + self.read_size)



def main():
  with open('classes.dex', 'rb') as f:
    x = f.read()
  stream = StreamReader(x)
  header = HeaderItem(stream, 0)
  print(header)
  print(hex(header.read_size))
  print(header.magic)
  print('map list : {}'.format(header.map_list))

if __name__ == '__main__':
  main()