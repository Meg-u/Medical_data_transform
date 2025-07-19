from sqlalchemy import Column, Integer, String, Float
from .database import Base

class ImageDetection(Base):
    __tablename__ = "fct_image_detections"

    message_id = Column(String, primary_key=True)
    image_name = Column(String)
    detected_class = Column(String)
    confidence_score = Column(Float)
    channel = Column(String)

class FctMessages(Base):
    __tablename__ = "fct_messages"

    message_id = Column(String, primary_key=True)
    channel_name = Column(String)
    message = Column(String)
    product = Column(String)
    post_date = Column(String)

class MartTopProducts(Base):
    __tablename__ = "mart_top_products"

    product = Column(String, primary_key=True)
    mentions = Column(Integer)