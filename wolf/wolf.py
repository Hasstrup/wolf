from .model import Model

class Wolf:
    @classmethod
    def configure(cls, config={}):
        """ Takes in the config settings and returns a new instance of itself"""
        return cls(store_path=config["store_path"])
        pass

    def __init__(self, store_path=""):
        self.store_path = store_path

    @classmethod
    def define_model(cls, model_name, schema):
        model = Model(table_name=model_name.lower(), schema=schema)
        return model
