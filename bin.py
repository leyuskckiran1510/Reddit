from PIL import Image

# load color names from ./palette.png into list

# this is the index used by reddit in r/place to identify the color
colors = ["red","yellow","lime","darkgreen","green","DarkBlue","LoghtBlue","Cyan",
          "Purple","LightPurple","Pink","Brown","Black","Grey","lightgrey","white"]




class Run:
    # this is the hex format of above color list
    new_hex = ['#e50000', '#e59500', '#e5d900', '#02be01', '#94e044', '#0000ea', '#0083c7',
               '#00d3dd', '#820080', '#cf6ee4', '#ffa7d1', '#a06a42', '#222222', '#888888', '#e4e4e4', '#ffffff']

    def __init__(self):
        self.convert_to_color_space()

    def evaluate_image(self):
        img = Image.open('./final.png')
        img = img.convert('RGB')
        array = []
        for x in range(0,img.size[0]):
            pseudo=[]
            for y in range(0,img.size[1]):
                r, g, b = img.getpixel((x, y))
                hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
                try:
                    pseudo.append(self.new_hex.index(hex))
                except:
                    print("not found",hex)
                    pseudo.append(0)
            array.append(pseudo)
                #print(new_hex.index(hex))
        # Return Two Dimensional array of color indexes to be used by redditplaceputter
        #x and y are the indexes of the array
        return array



# Convert image to avilabe color space aka into the palette.png color space and convert into 50*50 image size
    def convert_to_color_space(self):
        # the color space or pallates available in the form of pallate .png
        # just use this pallate
        src = Image.open("./pallate.png")
        # image to be drawen in canvas
        # normal image
        new = Image.open("image.jpg")
        new = new.resize((50,50)) # resizing to 50*50 height and width as you can make 1 request per 5 minutes
        # and big imahe pixells means more time or more users to complete
        # for 50*50 it take approx. 9 days to complete if not intrupted by any other reddit users
        converted = new.quantize(palette=src,dither=0)
        # final image that goes in the reddit canvas
        converted.save("./final.png")
        return 1



if __name__ == "__main__":
    convert_to_color_space()