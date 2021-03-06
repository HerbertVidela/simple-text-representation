from .Paragraph import Paragraph
from ..models.TextModel import TextModel

class Text:
  def __init__(self):
    self.paragraphs = list()
    self.unformatedParagraphs = list()
    self.title = ''
    self.grade = -1

  def toString(self):
    text = ''

    for paragraph in self.paragraphs:
      text = text + paragraph.join(' ') + '\n'

    return text

  def setGrade(self, grade):
    self.grade = grade
  
  def getGrade(self):
    return self.grade

  def setTitle(self, newTitle):
    self.title = newTitle

  def getTitle(self):
      return self.title

  def addParagraph(self, paragrah):
    return self.paragraphs.append(paragrah)

  def setUnformatedParagraphs(self, unformatedParagraphs):
    self.unformatedParagraphs = unformatedParagraphs

  def formatParagraphs(self):
    for uParagraph in self.unformatedParagraphs:
      paragraph = Paragraph(uParagraph, True)
      self.paragraphs.append(paragraph)

  def save(self, database):
    try:
      database.establishConnection()

      with database.getDatabase().transaction():
        text = TextModel.create(
          title=self.title,
          grade=self.grade
        )
        for paragraph in self.paragraphs:
          paragraph.save(database, text.id)
      database.closeConnetion()
    except:
      print('Somethinig went wrong!')

  @staticmethod
  def getText(database, id=1):
    try:
      database.establishConnection()
      textArr = list()

      with database.getDatabase():
        text = TextModel.get(TextModel.id == id)
        paragraphs = text.paragraphs
        for paragraph in paragraphs:
          paragraphArr = list()
          sentences = paragraph.sentences
          for sentence in sentences:
            paragraphArr.append(sentence.value)
          paragraphArr.reverse()
          textArr.append(paragraphArr)
      database.closeConnetion()

      return textArr
    except ValueError:
      database.closeConnetion()
      print(ValueError)
      print('Something went wrong')

  @staticmethod
  def getTexts(database, grade=7):
    try:
      database.establishConnection()
      texts = list()

      with database.getDatabase():
        for text in TextModel.select().where(TextModel.grade == f'{grade}'):
          textArr = list()
          for paragraph in text.paragraphs:
            paragraphArr = list()
            for sentence in paragraph.sentences:
              paragraphArr.append(sentence.value)
            paragraphArr.reverse()
            textArr.append(paragraphArr)
          texts.append(textArr)
      database.closeConnetion()

      return texts
    except ValueError:
      database.closeConnetion()
      print(ValueError)
      print('Something went wrong')

  @staticmethod
  def getAllTexts(database):
    try:
      database.establishConnection()
      texts = list()

      with database.getDatabase():
        for text in TextModel.select():
          textArr = list()
          for paragraph in text.paragraphs:
            paragraphArr = list()
            for sentence in paragraph.sentences:
              paragraphArr.append(sentence.value)
            paragraphArr.reverse()
            textArr.append(paragraphArr)
          texts.append(textArr)
      database.closeConnetion()

      return texts
    except ValueError:
      database.closeConnetion()
      print(ValueError)
      print('Something went wrong')
