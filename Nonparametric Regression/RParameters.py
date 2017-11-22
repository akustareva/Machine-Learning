class RParameters:
    def __init__(self, kernel=None, k=None, ds=None, mse=None):
        self.kernel = kernel
        self.k = k
        self.ds = ds
        self.mse = mse
        
    def __str__(self):
        kernelName = 'None'
        if self.kernel is not None:
            if type(self.kernel) == tuple:
                kernelName = self.kernel[1]
            else:
                kernelName = self.kernel
        return '{kernel=%s, k=%s, mse=%s}' % (kernelName, str(self.k), str(self.mse))
