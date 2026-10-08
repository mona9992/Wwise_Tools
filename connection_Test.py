from waapi import WaapiClient, CannotConnectToWaapiException

try:
    with WaapiClient() as client:
        info = client.call("ak.wwise.core.getInfo")
        print("Connected to", info["displayName"])
        print("Wwise version:", info["version"]["displayName"])
except CannotConnectToWaapiException:
    print("Could not connect. Is Wwise open with WAAPI enabled?")