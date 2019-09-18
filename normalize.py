


class DexClassItem(self):
  def __init__(self):
    self.annotations = []
    self.methods = []
    self.fields = []


class DexFieldItem(self):
  def __init__(self):
    self.annotations = []
    self.type = ''
    self.value = ''


class DexMethodItem(self):
  def __init__(self):
    self.annotations = []
    self.type = ''
    self.return_type = ''
    self.codes = None


class DexCodeItem(self):
  def __init__(self):
    self.editor = None


class DexCodeEditor(self):
  def __init__(self):
    self.bytecodes = []
  
  def set_label(self, bytecode):
    pass

