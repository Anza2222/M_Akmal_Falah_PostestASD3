class Musik:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Buat Getter untuk Atribut, Disebut get_title
  def get_title(self):
    return self.__title
  
  
  # TODO:
  def set_title(self, title):
    self.__title = str(title.title())


  # TODO: 
  def get_next_song(self):
    return self.__next_song


  # TODO: 
  def set_next_song(self, next_title):
      self.__next_song = next_title

  # TODO: 
  def __str__(self):
    return str(self.__title)


  # TODO:
  def __repr__(self):
    return f"{self.__title} -> {self.__next_song}"