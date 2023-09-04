import marshmallow_dataclass


@marshmallow_dataclass.dataclass
class Config:
    """
    Holds all object-detection settings defined by user in config.yaml file.
    """

    dataset_file_format: str = "jpg"
    file_count_threshold: int = 20

    def save():
        pass

    @classmethod
    def load():
        pass


Config.SCHEMA = marshmallow_dataclass.class_schema(Config)()
