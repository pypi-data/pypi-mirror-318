# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

from datetime import datetime, timedelta
from typing import Tuple

import numpy as np
from astropy.io import fits
from astropy.io.fits.hdu.image import PrimaryHDU
from astropy.io.fits.hdu.table import BinTableHDU
from astropy.io.fits.hdu.hdulist import HDUList

from spectre_core.spectrograms import Spectrogram, SpectrumTypes
from .._register import register_batch
from .._base import BaseBatch, BatchFile


@register_batch('callisto')
class _Batch(BaseBatch):
    def __init__(self,
                 start_time: str,
                 tag: str):
        super().__init__(start_time, tag) 
        self.add_file( FitsFile(self.parent_dir_path, self.name) )


class FitsFile(BatchFile):
    def __init__(self, 
                 parent_dir_path: str, 
                 base_file_name: str):
        super().__init__(parent_dir_path, base_file_name, "fits")


    def read(self) -> Spectrogram:
        with fits.open(self.file_path, mode='readonly') as hdulist:
            primary_hdu                = self._get_primary_hdu(hdulist)
            dynamic_spectra            = self._get_dynamic_spectra(primary_hdu)
            spectrogram_start_datetime = self._get_spectrogram_start_datetime(primary_hdu)
            bintable_hdu               = self._get_bintable_hdu(hdulist)
            times, frequencies         = self._get_time_and_frequency(bintable_hdu)
            spectrum_type              = self._get_spectrum_type(primary_hdu)

            if spectrum_type == SpectrumTypes.DIGITS:
                dynamic_spectra_linearised = self._convert_units_to_linearised(dynamic_spectra)
                return Spectrogram(dynamic_spectra_linearised[::-1, :], # reverse the spectra along the frequency axis
                        times, 
                        frequencies[::-1], # sort the frequencies in ascending order
                        self.tag, 
                        spectrogram_start_datetime,
                        spectrum_type)
            else:
                raise NotImplementedError(f"SPECTRE does not currently support spectrum type with BUNITS '{spectrum_type}'")


    @property
    def datetimes(self) -> np.ndarray:
        with fits.open(self.file_path, mode='readonly') as hdulist:
            bintable_data = hdulist[1].data
            times = bintable_data['TIME'][0]
            return [self.start_datetime + timedelta(seconds=t) for t in times]        


    def _get_primary_hdu(self, hdulist: HDUList) -> PrimaryHDU:
        return hdulist['PRIMARY']


    def _get_dynamic_spectra(self, primary_hdu: PrimaryHDU) -> np.ndarray:
        return primary_hdu.data


    def _get_spectrogram_start_datetime(self, primary_hdu: PrimaryHDU) -> datetime:
        date_obs = primary_hdu.header['DATE-OBS']
        time_obs = primary_hdu.header['TIME-OBS']
        return datetime.strptime(f"{date_obs}T{time_obs}", "%Y-%m-%dT%H:%M:%S.%f")


    def _get_bintable_hdu(self, hdulist: HDUList) -> BinTableHDU:
        return hdulist[1]


    def _get_time_and_frequency(self, bintable_hdu: BinTableHDU) -> Tuple[np.ndarray, np.ndarray]:
        data = bintable_hdu.data
        times = data['TIME'][0]
        frequencies_MHz = data['FREQUENCY'][0]
        frequencies = frequencies_MHz * 1e6 # convert to Hz
        return times, frequencies


    def _convert_units_to_linearised(self, dynamic_spectra: np.ndarray) -> np.ndarray:
        digits_floats = np.array(dynamic_spectra, dtype='float')
        # conversion as per ADC specs [see email from C. Monstein]
        dB = (digits_floats / 255) * (2500 / 25)
        return 10 ** (dB / 10)


