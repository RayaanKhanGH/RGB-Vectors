import unittest
from PIL import Image
from main import create

class TestCreate(unittest.TestCase):
    
    def test_create_image(self):
        # Create a test array of 100 white pixels
        array = [(16777215, 1) for i in range(100)]
        
        # Call the create function with the test array
        create(array)
        
        # Open the generated image file
        img = Image.open("test.png")
        
        # Check that the image has the expected size of 10x10 pixels
        self.assertEqual(img.size, (10, 10))
        
        # Check that all pixels in the image are white
        for pixel in img.getdata():
            self.assertEqual(pixel, (255, 255, 255))
        
if __name__ == '__main__':
    unittest.main()
