"""
Creating Custom Errors
"""

class TypeErrorWithCode(TypeError):
  """
  Exception raised when a specific error code is Needed
  """
  def __init__(self, message, code):
    super().__init__(f"Error code {code}: {message}")
    self.code = code


err = TypeErrorWithCode('An Error happened.', 500)
print(err.__doc__)