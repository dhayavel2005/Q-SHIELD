
"""
Session Management Module for Q-SHIELD

Implements:
1. Session Creation
2. Session Storage
3. Session Termination
4. Session Lookup

Author: Dhaya R.
"""


import uuid
import time


class SessionManager:

    def __init__(self):

        self.active_sessions = {}

    def create_session(self, session_key):

        session_id = str(uuid.uuid4())

        self.active_sessions[session_id] = {

            "session_key": session_key,

            "created_at": time.time(),

            "status": "ACTIVE"

        }

        print("\nSession Created")

        print("Session ID:", session_id)

        return session_id

    def get_session(self, session_id):

        if session_id in self.active_sessions:

            return self.active_sessions[session_id]

        else:

            print("Session Not Found")

            return None

    def destroy_session(self, session_id):

        if session_id in self.active_sessions:

            del self.active_sessions[session_id]

            print("\nSession Destroyed")

        else:

            print("\nInvalid Session ID")

    def get_active_sessions(self):

        return len(self.active_sessions)

    def display_sessions(self):

        print("\n===== ACTIVE SESSIONS =====")

        for sid, info in self.active_sessions.items():

            print("\nSession ID :", sid)

            print("Status     :", info["status"])

            print("Created At :", info["created_at"])

        print("\nTotal Sessions :",

              self.get_active_sessions())


if __name__ == "__main__":

    sm = SessionManager()

    key = b"sample_key"

    sid = sm.create_session(key)

    sm.display_sessions()

    sm.destroy_session(sid)

    sm.display_sessions()
