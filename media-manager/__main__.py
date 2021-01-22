import sys
from typing import List

import magic
from pymediainfo import MediaInfo

from database import session
from entity.Media import Media, Audio, Video

try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


def main(argv: List[str]):
    for entry in scandir(argv[1]):
        if entry.is_file():
            mime_type: str = magic.from_file(entry.path, mime=True)
            if mime_type.startswith("video"):
                print(entry.path)
                media_info = MediaInfo.parse(entry.path)
                media = to_media(media_info)
                session.add(media)

    session.commit()


def to_media(media_info) -> Media:
    audios: List[Audio] = []
    videos: List[Video] = []
    for track in media_info.tracks:
        if track.track_type == 'Video':
            video: Video = Video(
                codec_id=track.codec_id,
                media_type=track.internet_media_type,
                duration=track.duration,
                bit_rate=track.bit_rate,
                width=track.width,
                height=track.height,
                frame_rate_mode=track.frame_rate_mode,
                frame_rate=track.frame_rate,
                frame_count=track.frame_count,
                bit_depth=track.bit_depth,
                size=track.stram_size
            )
            videos.append(video)
        elif track.track_type == 'Audio':
            audio: Audio = Audio(
                format=track.format,
                codec_id=track.codec_id,
                duration=track.duration,
                bit_rate_mode=track.bit_rate_mode,
                bit_rate=track.bit_rate,
                channels=track.channel_s,
                sample_rate=track.sampling_rate,
                bit_depth=track.bit_depth,
                size=track.stream_size,
                language=track.language
            )
            audios.append(audio)
    media: Media = Media(
        title=media_info.general_tracks[0].file_name,
        format=media_info.general_tracks[0].format,
        extension=media_info.general_tracks[0].file_extension,
        location=media_info.general_tracks[0].complete_name,
        audios=audios,
        videos=videos
    )
    return media


if __name__ == '__main__':
    main(sys.argv)
