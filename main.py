from models import User
from mixins import JsonMixin, CreateMixin, ReadMixin

class CRUD(JsonMixin, CreateMixin, ReadMixin):
    _file_name = 'db.json'
    _model = User


crud = CRUD()
# crud.create()
# crud.list()
crud.get_user_by_id()