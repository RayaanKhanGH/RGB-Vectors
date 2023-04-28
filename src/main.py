from PIL import Image
from collections import Counter


def combine(r, g, b):
    combined = r + g * 256 + b * 256 * 256

    return combined


class vector():

    def __init__(self, path):
        self.path = path
        self.colors = []
        self.vals = []

    def encode(self):
        """
        This function opens an image file, converts its pixels to RGB format, and then combines the RGB
        values of each pixel into a single integer value, which is then appended to a list along with
        its corresponding index. 
        """

        img = Image.open(self.path)

        rgb_pixels = img.convert("RGB")
        pixel_values = list(rgb_pixels.getdata())


        
        count = 1
        for pixel in pixel_values:
            r, g, b = pixel
        
            combined = r + g * 256 + b * 256 * 256
            
            self.vals.append((combined, count))
            count = count + 1

    def get_dominant(self):
        """
        This function takes a list of vectors, decodes the vectors rgb values from combined value,
        appends the rgb values to a list,
        counts the occurrences of each color, and returns the
        RGB value with the largest count as the dominant color.
        :return: A dictionary with the dominant color as the key (in string format) and its count as the
        value.
        """ 

        for item in self.vals:
            rgb = decode_combined(item[0])
            self.colors.append(rgb)


        counts = Counter(self.colors)
        rec = {}

        # Store the counts for each RGB value as a string in the rec dictionary
        for color, count in counts.items():
            rec[str(color)] = count

        # Find the RGB value with the largest count
        largest_count = 0
        dominant_color = None
        for color, count in rec.items():
            if count > largest_count:
                largest_count = count
                dominant_color = color

        return dominant_color, largest_count


    def __vector__(self):
        """
        This function returns the values of a vector.
        :return: The method `__vector__` is returning the attribute `vals` of the object.
        """
        return self.vals
    
    def __str__(self):
        """
        This function returns a string representation of the object.
        :return: The method `__str__` is returning a string representation of the `path` attribute of
        the vector.
        """
        return f"{self.path}"




def decode_combined(combined):
        """
        These lines of code are decoding the combined RGB value of a pixel into its individual red,
        green, and blue values.
        """
        b_ = combined // (256 * 256)
        g_ = (combined // 256) % 256
        r_ = combined % 256

        return r_, g_, b_


def create(self, array: list):
    # Calculate the size of the image based on the length of the input array
    width = 10
    height = len(array) // width

    # Create a new RGB image with the specified size
    img = Image.new("RGB", (width, height))

    # Loop through the input array and color each pixel in the image
    for i, pixel in enumerate(array):
        # Decode the combined RGB value
        r, g, b = decode_combined(pixel[0])
        # Calculate the x and y coordinates of the pixel
        x = i % width
        y = i // width
        # Set the color of the pixel in the image
        img.putpixel((x, y), (r, g, b))

    # Save the image to disk
    img.save("output.png")
