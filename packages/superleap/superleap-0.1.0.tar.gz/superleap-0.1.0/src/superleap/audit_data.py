from dataclasses import dataclass

@dataclass
class Pointer:
    randomId: str
    updatedAt: int
    def __init__(self, randomId:str,updatedAt:int):
        self.randomId=randomId
        self.updatedAt=updatedAt

    def is_valid(self):
        if self.randomId == "":
            return False
        if self.updatedAt == 0:
            return False
        return True
    
    def to_dict(self) -> dict[str, any]:
        return {
            "random_id": self.randomId,
            "updated_at": self.updatedAt
        }

@dataclass
class Object:
    slug:str
    pointer:Pointer

    def __init__(self,slug:str,pointer:Pointer):
        if slug == "":
            raise ValueError("slug can not be empty")
        if pointer is not None and not pointer.is_valid():
            raise ValueError("pointer is not valid")
        self.slug=slug
        self.pointer = pointer

    def to_dict(self) -> dict[str, any]:
        result = {"slug": self.slug}
        if self.pointer is not None:
            result["pointer"] = self.pointer.to_dict()
        return result
    
    def set_pointer(self,pointer:Pointer):
        self.pointer = pointer
    


@dataclass
class AuditDataChanges():
    before_data: dict[str,any]
    after_data: dict[str,any]
    diff: dict[str,any]


    @classmethod
    def from_dict(cls, data: dict[str, any]) -> 'AuditDataChanges':
        return cls(
            before_data=data.get('before_data'),
            after_data=data.get('after_data'),
            diff=data.get('diff')
        )

@dataclass
class AuditData():
    random_id: str
    record_id:str
    slug: str
    operation_type:str
    created_by: str
    created_at: int
    updated_by: str
    updated_at: int
    deleted_by: str
    deleted_at: int
    data: dict

    @classmethod
    def from_dict(cls, data: dict[str, any]) -> 'AuditData':
        return cls(
            random_id=data.get('random_id'),
            record_id=data.get('record_id'),
            slug=data.get('slug'),
            operation_type=data.get('operation_type'),
            created_by=data.get('created_by'),
            created_at=data.get('created_at'),
            updated_by=data.get('updated_by'),
            updated_at=data.get('updated_at'),
            deleted_by=data.get('deleted_by'),
            deleted_at=data.get('deleted_at'),
            data=AuditDataChanges.from_dict(data.get('data'))
        )
    
    def get_object_pointer(self) -> Object:
        return Object(self.slug,Pointer(self.random_id,self.updated_at))
        

@dataclass
class ObjectAuditData():
    slug: str
    audit_data_list: list[AuditData]

    @classmethod
    def from_dict(cls, data: dict[str, any]) -> 'ObjectAuditData':
        print(data)
        if data is not None:
            return cls(
                slug=data.get('slug'),
                audit_data_list=[AuditData.from_dict(item) for item in data.get('audit_data')]
            )