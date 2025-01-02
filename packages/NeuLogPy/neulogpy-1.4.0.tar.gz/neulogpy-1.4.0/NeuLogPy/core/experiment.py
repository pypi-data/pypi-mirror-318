from .logger import setup_logger

class Experiment:
    def __init__(self, api_client, sensors, rate, samples):
        self.api_client = api_client
        self.sensors = sensors
        self.rate = rate
        self.samples = samples
        self.logger = setup_logger(__name__)

    def start(self):
        """Start a new experiment"""
        # Build raw parameter string without any encoding
        params = ""
        for sensor, id in self.sensors:
            params += f"[{sensor.code}],[{id}],"
        params += f"[{self.rate}],[{self.samples}]"
        
        response = self.api_client.send_request("StartExperiment", f":{params}")
        if response and response.get("StartExperiment") == "True":
            return {"StartExperiment": True}
        return None

    def stop(self):
        """Stop the current experiment"""
        response = self.api_client.send_request("StopExperiment")
        if response and response.get("StopExperiment") == "True":
            return {"StopExperiment": True}
        return None

    def get_samples(self):
        """Get samples from the current experiment"""
        params = ""
        for sensor, id in self.sensors:
            params += f"[{sensor.code}],[{id}],"
        params = params.rstrip(",")  # Remove trailing comma
        
        return self.api_client.send_request("GetExperimentSamples", f":{params}")
