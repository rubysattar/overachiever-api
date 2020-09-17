from django.db import models
# from django.contrib.auth import get_user_model

class Card(models.Model):
  question = models.CharField(max_length=150)
  answer = models.CharField(max_length=150)

  # foreignkey fiel type accepts the model to relate to
  # and the option of what to do if that related object
  # the deck in this case, is deleted
  # cascade option will delete all cards tied to a certain
  # deck if that deck is deleted
  deck = models.ForeignKey("Deck", related_name="cards", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def as_dict(self):
    """Returns dictionary version of Card models"""
    return {
        'question': self.question,
        'answer': self.answer
    }

  def __str__(self):
    return f"The question on this card is '{self.question}'. The answer is '{self.answer}'."


