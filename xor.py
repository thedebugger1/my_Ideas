import base64
from itertools import cycle

message = "CEYGGBoCDkNGFxZJQVIKCwQKRBIcFlQCGgEVBApXQFURU1tVShwSH1VQXVMXRllNXgQNVlpCQgBG VVdZRgJeVkJTFwgXARxGRxASUVUbCBAbHAwOXkEXFklBUhgXDQRTXlVSVE1VSgsACVJcREVUQU9N XhIKVlAXGlNGEwIWRksKFRdBGg9USgQ="
key = bytes("saumyak0506", "utf8")
print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))

