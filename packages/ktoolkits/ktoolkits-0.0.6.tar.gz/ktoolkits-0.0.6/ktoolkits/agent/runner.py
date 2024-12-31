from ktoolkits.client.base_api import BaseApi
from ktoolkits.api_entities.ktool_response import RunnerResponse

class Runner(BaseApi):
    task = 'tool-runner'
    """
    API for ktoolkits Runner.
    """
    @classmethod
    def call(
        cls,
        tool_name: str,
        tool_input: str,
        **kwargs
    ) -> RunnerResponse:
        """Call tool runner service.

        Args:
            tool_name (str): The name of requested tool, such as nmap
            tool_input (str): The input for requested tool, such as: scan_target,root_domain etc

        Returns:
            RunnerResponse.
        """
        response = super().call(tool_name=tool_name,
                                tool_input=tool_input)
        
        is_stream = kwargs.get('stream', False)
        if is_stream:
            return (RunnerResponse.from_api_response(rsp)
                    for rsp in response)
        else:
            return RunnerResponse.from_api_response(response)