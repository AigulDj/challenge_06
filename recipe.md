
Music Tracker. Class Design Recipe


1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.


class MusicTracker:
    def __init__(self):
        # Parameters:
        #   tracks: empty list
        pass 

    def add(self, track):
        # Parameters:
        #   track: string representing a name of music listened
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the tracks_list
        pass 

    def list_tracks(self):
        # Returns:
        #   A list of tracks listened to     
        pass 

3. Create Examples as Tests

"""
Initally there is no trecks in the list
"""
tracker = MusicTracker()
tracker.list_tracks # => []

"""
When we add a single track name
It is reflected in the tracks list
"""
tracker = MusicTracker()
tracker.add("Track name 1")
tracker.list_tracks # => ["Track name 1"]

"""
When we add a multiple track names
It is reflected in the tracks list
"""
tracker = MusicTracker()
tracker.add("Track name 1")
tracker.add("Track name 2")
tracker.add("Track name 3")
tracker.list_tracks # => ["Track name 1", "Track name 2", "Track name 3"]

"""
When we add an empty string
It raises an error message "No track name provided"
"""
tracker = MusicTracker()
tracker.add("")
tracker.list_tracks # => "No track name provided"


4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.