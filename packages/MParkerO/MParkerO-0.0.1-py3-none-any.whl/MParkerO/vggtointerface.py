from scipy.fftpack import fft2, ifft2
import numpy as np
from abc import ABCMeta, abstractmethod
from math import factorial
from scipy.signal.windows import tukey


class VggToMultiInterface(metaclass=ABCMeta):
    def __init__(self, vgg, delta_bnds, delta_rhos, reference_depths, longrkm, longckm):
        """
        initialize the inputs and parameters
        :param vgg: A matrix for vertical gravity anomalies.
        :param delta_bnds: A dictionary that stores the undulations of the density interfaces
                           except for the density interface to be inverted.
        :param delta_rhos: A dictionary that stores the density contrasts for the density interfaces.
        :param reference_depths: A dictionary that stores the reference depths of the density interfaces.
        :param longrkm: float for row length
        :param longckm: float for col length
        """
        self.vgg = vgg
        self.delta_bnds = delta_bnds
        self.delta_rhos = delta_rhos
        self.reference_depths = reference_depths
        self.longrkm, self.longckm = longrkm, longckm


    @abstractmethod
    def downward(self, t, criteria):
        """
        calculate the density interface of interest with downward iteration steps
        :param t: iteration for downwards
        :param criteria: criteria for downwards iteration
        :return: matrix for undulation of density interface of interest
        """
        pass

    @classmethod
    def twkey(cls, matrix, edge=0.02):
        """
        tukey the border values for smoothness with outside values 0
        :param matrix: matrix for tukey
        :param edge: float for definition of border
        :return: tukey matrix
        """
        nrow, ncol = matrix.shape
        tky = np.array([row_tky * col_tky for row_tky in tukey(nrow, edge)
                        for col_tky in tukey(ncol, edge)]).reshape(matrix.shape)
        return tky * matrix


class MultiInverse(VggToMultiInterface):
    def __init__(self, vgg, delta_bnds, delta_rhos, reference_depths, longrkm, longckm, wh, alpha, target_interface):
        """
        initialize the inputs and parameters
        :param vgg: A matrix for vertical gravity anomalies.
        :param delta_bnds: A dictionary that stores the undulations of the density interfaces
                           except for the density interface to be inverted.
        :param delta_rhos: A dictionary that stores the density contrasts for the density interfaces.
        :param reference_depths: A dictionary that stores the reference depths of the density interfaces.
        :param longrkm: float for row length
        :param longckm: float for col length
        :param wh: float for the thresh hold for low pass filiter e.g. 0.1
        :param alpha: int for pass by some high order frequency, stands for the punishment on high older frequency
        :param target_interface: An integer number indicates density interface to be calculated.
        """
        super(MultiInverse, self).__init__(vgg, delta_bnds, delta_rhos, reference_depths, longrkm, longckm)
        self.K = max(self.delta_rhos.keys())
        self.G = 6.67
        self.wh = wh
        self.alpha = alpha
        self.target_interface = target_interface
        self.frequency = self.__frequency__()
        self.filter = self.__filter__()
        # temp
        self.temp = {}

    def __frequency__(self):
        """
        inner function for calculating the frequency
        :return: frequency matrix
        """
        nrow, ncol = self.vgg.shape
        frequency = np.zeros((nrow, ncol))
        for i in range(nrow):
            for j in range(ncol):
                ii = i if i <= nrow / 2 else i - nrow
                jj = j if j <= ncol / 2 else j - ncol
                frequency[i, j] = 2 * np.pi * np.sqrt((ii / self.longrkm) ** 2 + (jj / self.longckm) ** 2)
        return frequency

    def __filter__(self):
        """
        inner function for calculating the filter that lowpass the frequency value
        :return: a filter matrix
        """
        nrow, ncol = self.vgg.shape
        filter = np.ones(self.vgg.shape)
        for i in range(nrow):
            for j in range(ncol):
                if self.frequency[i, j] > self.wh:
                    ratio = self.frequency[i, j] / self.wh
                    filter[i, j] = ratio ** (1 - self.alpha) - (1 - self.alpha) * np.log(ratio) * ratio ** (
                                1 - self.alpha)
        return filter

    def bnd_k_n(self, k, n):
        name = '%d-%d' % (k, n)
        if self.temp.get(name) is None:
            bnd_twkey = self.twkey(self.delta_bnds[k])
            bnd_twkey_n = bnd_twkey ** n
            bnd_fourier = fft2(bnd_twkey_n)
            self.temp[name] = bnd_fourier
        else:
            bnd_fourier = self.temp.get(name)
        return bnd_fourier * self.filter

    def vgg_fft(self):
        name = 'vgg-ft'
        if self.temp.get(name) is None:
            vgg_ft = fft2(self.twkey(self.vgg))
            self.temp[name] = vgg_ft
        else:
            vgg_ft = self.temp.get(name)
        return vgg_ft * self.filter

    def once_downward(self, target_bnd, t):
        self.delta_bnds[self.target_interface] = target_bnd
        fft = -self.vgg_fft() / 2 / np.pi / self.G / self.delta_rhos[self.target_interface]/ \
            np.exp(-self.frequency * self.reference_depths[self.target_interface])
        for k in range(self.K + 1):
            if k != self.target_interface:
                fft = fft - self.delta_rhos[k] / self.delta_rhos[self.target_interface] * \
                      self.bnd_k_n(k, n=1) * np.exp(-self.frequency * (self.reference_depths[k] - self.reference_depths[self.target_interface]))
        fft_2 = 0
        for k in range(self.K + 1):
            factor_kj = self.delta_rhos[k] / self.delta_rhos[self.target_interface] * \
                        np.exp(-self.frequency * (self.reference_depths[k] - self.reference_depths[self.target_interface]))
            for n in range(2, t + 1):
                fft_2 = fft_2 + factor_kj * self.frequency ** (n - 1) / factorial(n) * self.bnd_k_n(k, n=n)
        fft3 = (fft - fft_2) * self.filter
        fft3[0, 0] = 0
        return ifft2(fft3).real

    def downward(self, t=10, criteria=0):
        target_bnd = self.once_downward(target_bnd=0, t=1)
        target_bnd_temp = 0
        if t == 1:
            return target_bnd - self.reference_depths[self.target_interface]
        else:
            for n in range(2, t+1):
                target_bnd = self.once_downward(target_bnd=target_bnd, t=n)
                rmse = np.sqrt(np.mean((target_bnd - target_bnd_temp) ** 2))
                if rmse < criteria:
                    print(f'无穷级数项的前 {n} 项与前 {n - 1} 项的误差:{rmse} 小于阈值 {criteria} \n -------------完成迭代!!!------------')
                    print(f'共计迭代次数:{n}')
                    break
                else:
                    print(f'无穷级数项的前 {n} 项与前 {n-1} 项的误差:{rmse}')
                    target_bnd_temp = target_bnd
            return target_bnd - self.reference_depths[self.target_interface]
