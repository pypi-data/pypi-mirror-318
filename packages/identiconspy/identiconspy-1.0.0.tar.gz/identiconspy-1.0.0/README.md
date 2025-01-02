# identicons.py
Small library for generating identicons in python

## Usage
```py
from identicons import Identicon

# Create an Identicon generator
generator = Identicon(grid_size=5, cell_size=50)

# Get the identicon as bytes
image_bytes = generator.generate("Example")

print(image_bytes)
# result:
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xfa\x00\x00\x00\xfa\x...........

# Generate & save the identicon to a file
generator.generate_to_file("Example", "example.png")
```

## Install
`pip install identiconspy`