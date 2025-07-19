from pydantic import BaseModel

class Detection(BaseModel):
    message_id: str
    image_name: str
    detected_class: str
    confidence_score: float
    channel: str

    class Config:
        orm_mode = True
class TopProduct(BaseModel):
    product_name: str
    mention_count: int
    class Config:
        from_attributes = True
class ChannelActivity(BaseModel):
    date: str
    post_count: int

    class Config:
        from_attributes = True

class Message(BaseModel):
    message_id: str
    channel_name: str
    message_text: str
    post_date: str

    class Config:
        from_attributes = True

 
