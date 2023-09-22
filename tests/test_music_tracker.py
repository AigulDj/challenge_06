import pytest
from lib.music_tracker import MusicTracker

"""
Initally there is no trecks in the list
"""
def test_no_tracks_in_the_list():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

"""
When we add a single track name
It is reflected in the tracks list
"""
def test_added_single_track():
    tracker = MusicTracker()
    tracker.add("Track name 1")
    assert tracker.list_tracks()  == ["Track name 1"]

"""
When we add a multiple track names
It is reflected in the tracks list
"""
def test_added_multiple_tracks():
    tracker = MusicTracker()
    tracker.add("Track name 1")
    tracker.add("Track name 2")
    tracker.add("Track name 3")
    assert tracker.list_tracks() == ["Track name 1", "Track name 2", "Track name 3"]

"""
When we add an empty string
It raises an error message "No track name provided"
"""
def test_empty_string_added():
    tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        tracker.add("")
    error_msg = str(e.value)
    assert error_msg == "No track name provided"
    assert tracker.list_tracks() ==  []