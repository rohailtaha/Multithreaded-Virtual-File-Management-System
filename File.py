import uuid;


class File:
  def __init__(self, file):
    self.inode = uuid.uuid4().__int__().__str__()[0:6];
    self.name = file['name'];
    self.size = file['size'];
    self.pages = file['pages'];
    self.content = file['content'];
    self.starting_page_address = file['starting_page_address'];
    # permissions = ['r', 'w'] for read, write.
    self.permissions= ['r', 'w'];

  def update_size(self):
    self.size = len(self.content) + 1;   

  def write_permission(self):
    return 'w' in self.permissions;

  def read_permission(self):
    return 'r' in self.permissions;  

  def read(self):
    if(self.read_permission()):
      print(self.content);  

  def append(self, content):  
    if(self.write_permission()):
      self.content += (" " + content);
      self.update_size();

  def write(self, content):
    if(self.write_permission()):
      self.content = content;
      self.update_size();

  def read_permissions(self):
    permissions = "Permissions: ";
    for permission in self.permissions:
      permissions += (permission + " ");
    print(permissions); 

  def grant_permission(self, permission):
    if(permission not in self.permissions):
      self.permissions.append(permission);

  def remove_permission(self, permission):
    def check(apermission):
      return apermission != permission

    self.permissions = list(filter(check, self.permissions));
    


