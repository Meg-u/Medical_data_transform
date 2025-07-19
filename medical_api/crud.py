from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models

def get_top_products(db: Session, limit: int = 10):
    return (
        db.query(models.FctMessages.product, func.count(models.FctMessages.product).label("mentions"))
        .group_by(models.FctMessages.product)
        .order_by(func.count(models.FctMessages.product).desc())
        .limit(limit)
        .all()
    )

def get_channel_activity(db: Session, channel_name: str):
    return (
        db.query(models.FctMessages.date, func.count(models.FctMessages.message_id).label("message_count"))
        .filter(models.FctMessages.channel_name == channel_name)
        .group_by(models.FctMessages.date)
        .order_by(models.FctMessages.date)
        .all()
    )

def search_messages_by_keyword(db: Session, keyword: str):
    return (
        db.query(models.FctMessages)
        .filter(models.FctMessages.message.ilike(f"%{keyword}%"))
        .all()
    )
