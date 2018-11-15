class ImageInfo():
    """
    container for all image info needed
    """
    def __init__(self, center, size):
        self.center = [center[0], center[1]]
        self.size = [size[0], size[1]]

    def get_center(self):
        """
        return image center value
        """
        return self.center

    def get_size(self):
        """
        return image size value
        """
        return self.size

class Magnifier():
    """
    create a magnifier glass
    """
    def __init__(self, image, pos, size):
        self.image = image
        self.pos = [pos[0], pos[1]]
        self.size = [size[0], size[1]]
        self.degree = 3.0
        self.center = [self.degree*self.pos[0], self.degree*self.pos[1]]

    def set_pos(self, pos):
        self.pos = pos

    def set_degree(self, degree):
        """
        change the degree of zoomming
        """
        self.degree = degree #TODO

    def get_position(self):
        """
        get the position
        """
        return self.pos

    def get_degree(self):
        """
        get the degree of zoomming
        """
        return self.degree

    def get_center(self):
        return self.center
    
    def get_size(self):
        return self.size