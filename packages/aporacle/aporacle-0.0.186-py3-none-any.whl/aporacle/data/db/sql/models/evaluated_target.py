from datetime import datetime
from sqlalchemy import Column, Integer, inspect, Index, Float, String, event, func, UniqueConstraint, DateTime

from aporacle.data.db.sql.models import Base

class EvaluatedTarget(Base):
    __tablename__ = "EvaluatedTarget"
    __table_args__ = (
        UniqueConstraint('chain', 'model', name='uq_evaluated'),
        Index("et_chain_model_index", "chain", "model"),
    )
    # Change `id` to an auto-incrementing integer primary key
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    chain = Column(String(15), nullable=True)
    model = Column(String(50), nullable=False)
    target = Column(String(50), nullable=True)
    feed = Column(String(25), nullable=True)
    correction_factor = Column(Float, nullable=True)  # Correction Factor. Typically, the last observed Moving Average.
    correction_r2_score = Column(Float, nullable=True)
    correction_rmse_score = Column(Float, nullable=True)
    evaluation_voting_round = Column(Integer, nullable=True)
    status = Column(Integer, nullable=True)
    # Timestamp with default UTC now
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}