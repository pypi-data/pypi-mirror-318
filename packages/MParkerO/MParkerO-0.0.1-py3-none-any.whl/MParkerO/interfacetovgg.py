from abc import ABCMeta, abstractmethod
from scipy.fftpack import fft2, ifft2
import numpy as np
from math import factorial

class InterfaceToVgg(metaclass=ABCMeta):
    def __init__(self, delta_bnds, delta_rhos, reference_depths, longrkm, longckm):
        '''
        initialize the inputs and parameters
        :param delta_bnds: A dictionary that stores the undulations gridded data of the density
                           interface relative to its corresponding reference depth.
        :param delta_rhos: A dictionary that stores the density contrasts for the density interfaces.
        :param reference_depths: A dictionary that stores the reference depths of the density interfaces.
        :param longrkm: float for row length
        :param longckm: float for col length
        '''
        self.delta_bnds = delta_bnds
        self.delta_rhos = delta_rhos
        self.reference_depths = reference_depths
        self.longrkm, self.longckm = longrkm, longckm

    @abstractmethod
    def forward(self, t):
        pass


class MultiForward(InterfaceToVgg):
    def __init__(self, delta_bnds, delta_rhos, reference_depths, longrkm, longckm):
        super(MultiForward, self).__init__(delta_bnds, delta_rhos, reference_depths, longrkm, longckm)
        self.frequency = self.__frequency__()
        self.K = max(self.delta_bnds.keys())
        self.G = 6.67

    def __frequency__(self):
        """
        inner function for calculating the frequency
        :return: frequency matrix
        """
        nrow, ncol = self.delta_bnds[0].shape
        frequency = np.zeros((nrow, ncol))
        for i in range(nrow):
            for j in range(ncol):
                ii = i if i <= nrow / 2 else i - nrow
                jj = j if j <= ncol / 2 else j - ncol
                frequency[i, j] = 2 * np.pi * np.sqrt((ii / self.longrkm) ** 2 + (jj / self.longckm) ** 2)
        return frequency

    def forward(self, t):
        fft_all = 0
        for k in range(self.K + 1):
            factor_k = self.delta_rhos[k] * np.exp(-self.frequency * self.reference_depths[k])
            fft_k = 0
            for n in range(1, t + 1):
                fft_k = fft_k + self.frequency ** (n - 1) / factorial(n) * fft2(self.delta_bnds[k] ** n)
            fft_all = fft_all + factor_k * fft_k
        transformed_fft_all = -2 * np.pi * self.G * fft_all
        return ifft2(transformed_fft_all).real
