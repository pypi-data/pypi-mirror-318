import urllib.request
import json
from .logger import setup_logger

class NeuLogAPIClient:
    def __init__(self, host='localhost', port=22006):
        """Initialize API client
        
        Args:
            host (str): NeuLog server host
            port (int): NeuLog server port
        """
        self.logger = setup_logger(__name__)
        self.base_url = f"http://{host}:{port}/NeuLogAPI"
        self.logger.info(f"Initializing NeuLog API client at {self.base_url}")
        
    def send_request(self, command, params=""):
        """Send request to NeuLog API
        
        Args:
            command (str): API command (e.g., 'GetServerVersion', 'StartExperiment')
            params (str): Command parameters (e.g., '[Sound],[1],[Light],[1]')
            
        Returns:
            dict: Response from NeuLog server
        """
        # Construct URL exactly as it would appear in browser
        url = f"{self.base_url}?{command}"
        if params:
            url = f"{url}{params}"
            
        self.logger.debug(f"Sending request to: {url}")
        
        try:
            # Use urllib to make the request without any encoding
            request = urllib.request.Request(url)
            with urllib.request.urlopen(request) as response:
                raw_response = response.read().decode('utf-8')
                
            self.logger.debug(f"Raw response: {raw_response}")
            
            try:
                return json.loads(raw_response)
            except json.JSONDecodeError:
                self.logger.error(f"Failed to parse response as JSON: {raw_response}")
                return None
                
        except urllib.error.URLError as e:
            self.logger.error(f"Request failed: {e}")
            return None