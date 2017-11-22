class KParameters:
    def __init__(self, kernel=None, h=None, k=None, mse=None):
        self.kernel = kernel
        self.h = h
        self.k = k
        self.mse = mse
        
    def __str__(self):
        kernelName = 'None'
        if self.kernel is not None:
            if type(self.kernel) == tuple:
                kernelName = self.kernel[1]
            else:
                kernelName = self.kernel
        return '{kernel=%s, h=%s, k=%s, mse=%s}' % (kernelName, str(self.h), str(self.k), str(self.mse))
