from pydantic import BaseModel


class TrackArgs:
    def __init__(self, track):
        self.track = track
        self.name = 'mdx_extra_q'
        self.out = "separated"
        self.repo = None


class TrackModel(BaseModel):
    id: int
    fileName: str
    title: str
    artist: str
    source: str
