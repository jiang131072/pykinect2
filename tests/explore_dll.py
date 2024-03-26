import comtypes.client

# Get the module object for the Kinect COM library
kinect_module = comtypes.client.GetModule("appinfo.dll")

# Iterate over the available interfaces
for interface in kinect_module._types_:
    print(f"Interface: {interface}")
