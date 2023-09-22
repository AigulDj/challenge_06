class MusicTracker:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        if track == "":
            raise Exception("No track name provided")
        self.tracks.append(track)

    def list_tracks(self):
        return self.tracks