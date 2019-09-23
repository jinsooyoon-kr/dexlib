


class DexWriter(object):
  def __init__(self, dex_class_pool):
    self.dex_class_pool = dex_class_pool

  def get_string_table(self):
    string_pool = set()
    for clazz in self.dex_class_pool:
      string_pool.update(clazz.get_access_strings())
      string_pool.update(clazz.get_type_as_string())
      string_pool.update([x.get_signature() for x in clazz.methods])
      string_pool.update([x.get_name() for x in clazz.methods])

      string_pool.update([x.get_signature() for x in clazz.fields])
      string_pool.update([x.get_name() for x in clazz.fields])


  def write_strings(self):
    pass

  def write_types(self):
    pass

  def write_type_lists(self):
    pass

  def write_protos(self):
    pass

  def write_fields(self):
    pass

  def write_methods(self):
    pass

  def write_method_handles(self):
    pass

  def write_method_arrays(self):
    pass

  def write_call_sites(self):
    pass

  def write_annotations(self):
    pass

  def write_annotation_sets(self):
    pass

  def write_annotation_set_refs(self):
    pass

  def write_annotation_directories(self):
    pass

  def write_debug_code_items(self):
    pass

  def write_classes(self):
    pass

  def write_map_item(self):
    pass

  def write_header(self):
    pass

  def update_signature(self):
    pass

  def update_checksum(self):
    pass