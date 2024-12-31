import abc
import dataclasses
from dataclasses import dataclass
from typing import Dict, Any, Union, Optional, Callable

from ovos_bus_client import MessageBusClient
from ovos_utils.fakebus import FakeBus
from ovos_utils.log import LOG

from hivemind_bus_client.identity import NodeIdentity


def on_disconnect(client: 'HiveMindClientConnection'):
    LOG.debug(f"callback: client disconnected: {client}")

def on_connect(client: 'HiveMindClientConnection'):
    LOG.debug(f"callback: client connected: {client}")

def on_invalid_key(client: 'HiveMindClientConnection'):
    LOG.debug(f"callback: invalid access key: {client}")

def on_invalid_protocol(client: 'HiveMindClientConnection'):
    LOG.debug(f"callback: protocol requirements failure: {client}")


@dataclass
class ClientCallbacks:
    on_connect: Callable[['HiveMindClientConnection'], None] = on_connect
    on_disconnect: Callable[['HiveMindClientConnection'], None] = on_disconnect
    on_invalid_key: Callable[['HiveMindClientConnection'], None] = on_invalid_key
    on_invalid_protocol: Callable[['HiveMindClientConnection'], None] = on_invalid_protocol


@dataclass
class _SubProtocol:
    """base class all protocols derive from"""
    config: Dict[str, Any] = dataclasses.field(default_factory=dict)
    hm_protocol: Optional['HiveMindListenerProtocol'] = None
    callbacks: ClientCallbacks = dataclasses.field(default_factory=ClientCallbacks)

    @property
    def identity(self) -> NodeIdentity:
        if not self.hm_protocol:
            return NodeIdentity()
        return self.hm_protocol.identity

    @property
    def database(self) -> Optional['ClientDatabase']:
        if not self.hm_protocol:
            return None
        return self.hm_protocol.db

    @property
    def clients(self) -> Dict[str, 'HiveMindClientConnection']:
        if not self.hm_protocol:
            return {}
        return self.hm_protocol.clients


@dataclass
class AgentProtocol(_SubProtocol):
    """protocol to handle Message objects, the payload of HiveMessage objects"""
    bus: Union[FakeBus, MessageBusClient] = dataclasses.field(default_factory=FakeBus)
    config: Dict[str, Any] = dataclasses.field(default_factory=dict)
    hm_protocol: Optional['HiveMindListenerProtocol'] = None # usually AgentProtocol is passed as kwarg to hm_protocol
                                                             # and only then assigned in hm_protocol.__post_init__
    callbacks: ClientCallbacks = dataclasses.field(default_factory=ClientCallbacks)

@dataclass
class NetworkProtocol(_SubProtocol):
    """protocol to transport HiveMessage objects around"""
    config: Dict[str, Any] = dataclasses.field(default_factory=dict)
    hm_protocol: Optional['HiveMindListenerProtocol'] = None
    callbacks: ClientCallbacks = dataclasses.field(default_factory=ClientCallbacks)

    @property
    def agent_protocol(self) -> Optional['AgentProtocol']:
        if not self.hm_protocol:
            return None
        return self.hm_protocol.agent_protocol

    @abc.abstractmethod
    def run(self):
        pass


@dataclass
class BinaryDataHandlerProtocol(_SubProtocol):
    """protocol to handle Binary data HiveMessage objects"""
    config: Dict[str, Any] = dataclasses.field(default_factory=dict)
    hm_protocol: Optional['HiveMindListenerProtocol'] = None # usually BinaryDataHandlerProtocol is passed as kwarg to hm_protocol
                                                             # and only then assigned in hm_protocol.__post_init__
    agent_protocol: Optional['AgentProtocol'] = None
    callbacks: ClientCallbacks = dataclasses.field(default_factory=ClientCallbacks)

    def __post_init__(self):
        # NOTE: the most common scenario is having self.agent_protocol but not having self.hm_protocol yet
        if not self.agent_protocol and self.hm_protocol:
            self.agent_protocol = self.hm_protocol.agent_protocol

    def handle_microphone_input(self, bin_data: bytes,
                                sample_rate: int,
                                sample_width: int,
                                client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary audio input: {len(bin_data)} bytes at sample_rate: {sample_rate}")

    def handle_stt_transcribe_request(self, bin_data: bytes,
                                      sample_rate: int,
                                      sample_width: int,
                                      lang: str,
                                      client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary STT input: {len(bin_data)} bytes")

    def handle_stt_handle_request(self, bin_data: bytes,
                                  sample_rate: int,
                                  sample_width: int,
                                  lang: str,
                                  client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary STT input: {len(bin_data)} bytes")

    def handle_numpy_image(self, bin_data: bytes,
                           camera_id: str,
                           client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary image: {len(bin_data)} bytes")

    def handle_receive_tts(self, bin_data: bytes,
                           utterance: str,
                           lang: str,
                           file_name: str,
                           client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary TTS audio: {utterance} with {len(bin_data)} bytes")

    def handle_receive_file(self, bin_data: bytes,
                            file_name: str,
                            client: 'HiveMindClientConnection'):
        LOG.warning(f"Ignoring received binary file: {file_name} with {len(bin_data)} bytes")
