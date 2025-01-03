import requests
import signal
import logging
from audit_data import *
from . import __version__
from enum import Enum
from common import *

class SuperleapClient:
    api_key: str
    objects: dict[str, Object]

    session: requests.Session
    shutdown_signal: bool

    env: Environment

    base_urls = {
        Environment.PRODUCTION: "https://app.superleap.com",
        Environment.STAGING: "https://staging.superleap.com",
        Environment.DEVELOPMENT: "https://dev-app.dev.superleap.com",
        Environment.LOCAL: "http://localhost:8001"
    }

    def __init__(self, env:Environment, api_key:str):
        if api_key == "":
            raise ValueError("api_key can not be empty")
        else:
            # Setup logging
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s'
            )
            self.logger = logging.getLogger(__name__)
            
            # Register signal handlers
            signal.signal(signal.SIGTERM, self.handle_shutdown)
            signal.signal(signal.SIGINT, self.handle_shutdown)

            self.env = env
            self.api_key = api_key
            self.objects={}
            self.handler_function = None
            self.shutdown_signal = False
            self.session = requests.Session()
            self.session.headers.update({'Authorization': f'Bearer {self.api_key}','Content-Type': 'application/json'})

    def handle_shutdown(self, signum,frame):
        """Signal handler that sets the shutdown flag"""
        if not self.shutdown_signal:
            self.logger.info(f'Received signal {signum}. Starting graceful shutdown...\n')
            self.shutdown_signal = True

    def add_object(self,object:Object):
        self.objects[object.slug] = object

    def remove_object(self,slug:str):
        self.objects.pop(slug, 'Not found')

    def poll_audit_data(self):
        """function to continously poll audit data from Superleap"""
        while not self.shutdown_signal:
            url = f'{self.base_urls[self.env]}{POLL_AUDIT_DATA}'
            print(f"Making request to: {url}")

            # Convert objects to array of objects format
            payload = {
                "objects": [value.to_dict() for value in self.objects.values()]
            }
            try:
                response = self.session.post(url, json=payload)
                response.raise_for_status()
                self.handler_function([ObjectAuditData.from_dict(x) for x in response.json().get("data")],self.mark_message_as_read,self.commit_pointer)
            except requests.exceptions.RequestException as e:
                print(f"Error making request: {e}")
                return e
        # Commit the latest pointers automatically. Only if pointers are not None, commit them to SuperLeap
        self.logger.info(f'Trying to commit latest pointers for objects...\n')
        for object in self.objects.values():
            if object.pointer is not None and object.pointer.is_valid():
                self.commit_pointer(object) # Error handling

    def commit_pointer(self, object:Object):
        """
            Commits the pointer to Superleap and changes the pointer value of the object in the list of objects that is used for polling next
        """
        url = f'{self.base_urls[self.env]}{COMMIT_AUDIT_DATA_POINTER}'

        # Convert objects to dictionary format for JSON serialization
        payload = {
            "slug": object.slug,
            "pointer": object.pointer.to_dict()
        }
        try:
            response = self.session.post(url, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes
            if response.status_code == 202:
                # Also update the pointer of the object in the list that is being sent for poll. This ensures that new data will come from the latest pointer
                self.objects[object.slug] = object
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None
        
    def mark_message_as_read(self,object:Object):
        """Note: This does not commit the pointer to Superleap server. This only marks for the client session, commit_pointer has to be invoked before the session ends"""
        self.objects[object.slug] = object

    def set_handler(self,handlerFunc):
        """function that takes"""
        self.handler_function = handlerFunc
