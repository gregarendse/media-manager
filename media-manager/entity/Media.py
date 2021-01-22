from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

base = declarative_base()


class Video(base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey("media.id"))

    codec_id = Column(String)
    media_type = Column(String)
    duration = Column(Float)
    bit_rate = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)

    frame_rate_mode = Column(String)
    frame_rate = Column(Float)
    frame_count = Column(Integer)

    bit_depth = Column(Integer)

    size = Column(Integer)


class Audio(base):
    __tablename__ = "audio"

    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey("media.id"))

    format = Column(String)
    codec_id = Column(String)
    duration = Column(Float)

    bit_rate_mode = Column(String)
    bit_rate = Column(Integer)

    channels = Column(Integer)

    sample_rate = Column(Integer)
    bit_depth = Column(Integer)
    size = Column(Integer)

    language = Column(String)


class Media(base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    extension = Column(String)
    format = Column(String)
    location = Column(String)

    videos = relationship(Video)
    audios = relationship(Audio)
