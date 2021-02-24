class Pet:

    def __init__(self, pid, cid, name, status):
        self.petId = pid
        self.catId = cid
        self.status = status
        self.name = name

    def get_data(self):
        dict_pet = {"id": self.petId,
                    "category": {"id": self.catId, "name": "name_1"},
                    "name": self.name,
                    "photoUrls": ["test"],
                    "tags": [{"id": 301, "name": "string"}],
                    "status": self.status
                    }
        return dict_pet


