from PIL import Image

def background_reduction():
    background = Image.open("images/background1.png")
    background_pixels = background.getdata()

    test = Image.open("images/test2.png")
    test_pixels = test.getdata()

    reduction_pixels = [0] * len(test_pixels)

    for i in range(len(test_pixels)):
        background_pixel = background_pixels[i]
        test_pixel = test_pixels[i]

        delta_p = abs(test_pixel[0] - background_pixel[0]) / 3 + abs(test_pixel[1] - background_pixel[1]) / 3 + abs(test_pixel[2] - background_pixel[2]) / 3

        if delta_p > 9:
            reduction_pixels[i] = 255
        else:
            reduction_pixels[i] = 0

    reduction = Image.new("1", background.size)
    reduction.putdata(reduction_pixels)
    reduction.show()

background_reduction()