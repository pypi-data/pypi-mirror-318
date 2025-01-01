class SceneNotFoundError(Exception):
	def __init__(self, key: str):
		super().__init__(f"{key} has not been added yet!")


class NoSceneCreatedError(Exception):
	def __init__(self):
		super().__init__("No scene has been created")
