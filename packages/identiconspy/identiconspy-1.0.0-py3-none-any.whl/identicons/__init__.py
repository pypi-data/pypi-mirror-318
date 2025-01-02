import hashlib
from PIL import Image, ImageDraw
from io import BytesIO

class Identicon:
    def __init__(self, grid_size=5, cell_size=30, background_color=(255, 255, 255)):
        """
        Initialize the Identicon generator.

        Args:
            grid_size (int): Number of cells in the grid (e.g., 5x5 grid).
            cell_size (int): Pixel size of each cell.
            background_color (tuple): RGB color of the background.
        """
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.background_color = background_color

    def _hash_text(self, text):
        """Hash the input text using MD5."""
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    def _generate_pattern(self, hash_str):
        """
        Generate a symmetrical grid pattern from the hash.

        Args:
            hash_str (str): The MD5 hash string.

        Returns:
            list: A 2D list representing the grid.
        """
        mid = self.grid_size // 2
        pattern = []
        for i in range(self.grid_size):
            row = [int(hash_str[i * self.grid_size + j], 16) % 2 for j in range(mid + 1)]
            row += row[:-1][::-1]  # Mirror the row
            pattern.append(row)
        return pattern

    def _color_from_hash(self, hash_str):
        """Generate an RGB color from the hash."""
        return tuple(int(hash_str[i:i + 2], 16) for i in (0, 2, 4))

    def generate(self, text):
        """
        Generate the identicon image as bytes.

        Args:
            text (str): The input text for generating the identicon.

        Returns:
            bytes: The generated identicon image in PNG format.
        """
        hash_str = self._hash_text(text)
        pattern = self._generate_pattern(hash_str)
        color = self._color_from_hash(hash_str[:6])

        image_size = self.grid_size * self.cell_size
        image = Image.new('RGB', (image_size, image_size), self.background_color)
        draw = ImageDraw.Draw(image)

        for y, row in enumerate(pattern):
            for x, cell in enumerate(row):
                if cell:
                    top_left = (x * self.cell_size, y * self.cell_size)
                    bottom_right = ((x + 1) * self.cell_size, (y + 1) * self.cell_size)
                    draw.rectangle([top_left, bottom_right], fill=color)

        # Save to bytes
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)
        return image_bytes.read()

    def generate_to_file(self, text, file_name):
        """
        Save the identicon image to a file.

        Args:
            text (str): The input text for generating the identicon.
            file_name (str): Path to save the generated image.
        """
        image_bytes = self.generate(text)
        with open(file_name, "wb") as file:
            file.write(image_bytes)
