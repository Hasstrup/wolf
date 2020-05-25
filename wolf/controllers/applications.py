from ..models.application import Application
from ..models import db_session


class ApplicationsController:
    def index(self):
        """
          Return a list of applications registered on wolf
        """
        apps = db_session.query(Application).all()
        return {"applications": apps}
