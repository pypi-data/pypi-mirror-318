# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Callable
from dataclasses import dataclass

import numpy as np

from spectre_core.capture_configs import CaptureConfig, PNames
from spectre_core.exceptions import ModeNotFoundError
from ._spectrogram import Spectrogram
from ._array_operations import is_close

@dataclass
class TestResults:
    # Whether the times array matches analytically 
    times_validated: bool = False  
    # Whether the frequencies array matches analytically
    frequencies_validated: bool = False  
    # Maps each time to whether the corresponding spectrum matched analytically
    spectrum_validated: dict[float, bool] = None


    @property
    def num_validated_spectrums(self) -> int:
        """Counts the number of validated spectrums."""
        return sum(is_validated for is_validated in self.spectrum_validated.values())


    @property
    def num_invalid_spectrums(self) -> int:
        """Counts the number of spectrums that are not validated."""
        return len(self.spectrum_validated) - self.num_validated_spectrums
    

    def to_dict(self) -> dict[str, bool | dict[float, bool]]:
        return {
            "times_validated": self.times_validated,
            "frequencies_validated": self.frequencies_validated,
            "spectrum_validated": self.spectrum_validated
        }


class _AnalyticalFactory:
    def __init__(self):
        self._builders: dict[str, Callable] = {
            "cosine-signal-1": self.cosine_signal_1,
            "tagged-staircase": self.tagged_staircase
        }
        self._test_modes = list(self.builders.keys())


    @property
    def builders(self) -> dict[str, Callable]:
        return self._builders
    

    @property
    def test_modes(self) -> list[str]:
        return self._test_modes
    

    def get_spectrogram(self, 
                        num_spectrums: int, 
                        capture_config: CaptureConfig) -> Spectrogram:
        """Get an analytical spectrogram based on a test receiver capture config.
        
        The anaytically derived spectrogram should be able to be fully determined
        by parameters in the corresponding capture config and the number of spectrums
        in the output spectrogram.
        """

        if capture_config.receiver_name != "test":
            raise ValueError(f"Input capture config must correspond to the test receiver")
        
        builder_method = self.builders.get(capture_config.receiver_mode)
        if builder_method is None:
            raise ModeNotFoundError(f"Test mode not found. Expected one of {self.test_modes}, but received {capture_config.receiver_mode}")
        return builder_method(num_spectrums, 
                              capture_config)
    

    def cosine_signal_1(self, 
                        num_spectrums: int,
                        capture_config: CaptureConfig) -> Spectrogram:
        # Extract necessary parameters from the capture configuration.
        window_size      = capture_config.get_parameter_value(PNames.WINDOW_SIZE)
        sample_rate      = capture_config.get_parameter_value(PNames.SAMPLE_RATE)
        amplitude        = capture_config.get_parameter_value(PNames.AMPLITUDE)
        frequency        = capture_config.get_parameter_value(PNames.FREQUENCY)
        window_hop       = capture_config.get_parameter_value(PNames.WINDOW_HOP)
        center_frequency = capture_config.get_parameter_value(PNames.CENTER_FREQUENCY)
        # Calculate derived parameters a (sampling rate ratio) and p (sampled periods).
        a = int(sample_rate / frequency)
        p = int(window_size / a)

        # Create the analytical spectrum, which is constant in time.
        spectrum = np.zeros(window_size)
        spectral_amplitude = amplitude * window_size / 2
        spectrum[p] = spectral_amplitude
        spectrum[window_size - p] = spectral_amplitude

        # Align spectrum to naturally ordered frequency array.
        spectrum = np.fft.fftshift(spectrum)

        # Populate the spectrogram with identical spectra.
        analytical_dynamic_spectra = np.ones((window_size, num_spectrums)) * spectrum[:, np.newaxis]

        # Compute time array.
        sampling_interval = 1 / sample_rate
        times = np.arange(num_spectrums) * window_hop * sampling_interval

        # compute the frequency array.
        frequencies = np.fft.fftshift(np.fft.fftfreq(window_size, sampling_interval)) + center_frequency

        # Return the spectrogram.
        return Spectrogram(analytical_dynamic_spectra,
                           times,
                           frequencies,
                           'analytically-derived-spectrogram',
                           spectrum_type="amplitude")


    def tagged_staircase(self, 
                        num_spectrums: int,
                        capture_config: CaptureConfig) -> Spectrogram:
        # Extract necessary parameters from the capture configuration.
        window_size          = capture_config.get_parameter_value(PNames.WINDOW_SIZE)
        min_samples_per_step = capture_config.get_parameter_value(PNames.MIN_SAMPLES_PER_STEP)
        max_samples_per_step = capture_config.get_parameter_value(PNames.MAX_SAMPLES_PER_STEP)
        step_increment       = capture_config.get_parameter_value(PNames.STEP_INCREMENT)
        samp_rate            = capture_config.get_parameter_value(PNames.SAMPLE_RATE)

        # Calculate step sizes and derived parameters.
        num_samples_per_step = np.arange(min_samples_per_step, max_samples_per_step + 1, step_increment)
        num_steps = len(num_samples_per_step)

        # Create the analytical spectrum, constant in time.
        spectrum = np.zeros(window_size * num_steps)
        step_count = 0
        for i in range(num_steps):
            step_count += 1
            spectral_amplitude = window_size * step_count
            spectrum[int(window_size/2) + i*window_size] = spectral_amplitude

        # Populate the spectrogram with identical spectra.
        analytical_dynamic_spectra = np.ones((window_size * num_steps, num_spectrums)) * spectrum[:, np.newaxis]

        # Compute time array
        num_samples_per_sweep = sum(num_samples_per_step)
        sampling_interval = 1 / samp_rate
        # compute the sample index we are "assigning" to each spectrum
        # and multiply by the sampling interval to get the equivalent physical time
        times = np.array([(i * num_samples_per_sweep) for i in range(num_spectrums) ]) * sampling_interval

        # Compute the frequency array
        baseband_frequencies = np.fft.fftshift(np.fft.fftfreq(window_size, sampling_interval))
        frequencies = np.empty((window_size * num_steps))
        for i in range(num_steps):
            lower_bound = i * window_size
            upper_bound = (i + 1) * window_size
            frequencies[lower_bound:upper_bound] = baseband_frequencies + (samp_rate / 2) + (samp_rate * i)

        # Return the spectrogram.
        return Spectrogram(analytical_dynamic_spectra,
                           times,
                           frequencies,
                           'analytically-derived-spectrogram',
                           spectrum_type="amplitude")
    

def get_analytical_spectrogram(num_spectrums: int,
                               capture_config: CaptureConfig) -> Spectrogram:
    
    factory = _AnalyticalFactory()
    return factory.get_spectrogram(num_spectrums,
                                   capture_config)


def validate_analytically(spectrogram: Spectrogram,
                          capture_config: CaptureConfig,
                          absolute_tolerance: float) -> TestResults:

    analytical_spectrogram = get_analytical_spectrogram(spectrogram.num_times,
                                                        capture_config)


    test_results = TestResults()

    test_results.times_validated = bool(is_close(analytical_spectrogram.times,
                                                 spectrogram.times,
                                                 absolute_tolerance))

    test_results.frequencies_validated = bool(is_close(analytical_spectrogram.frequencies,
                                                       spectrogram.frequencies,
                                                       absolute_tolerance))

    test_results.spectrum_validated = {}
    for i in range(spectrogram.num_times):
        time = spectrogram.times[i]
        analytical_spectrum = analytical_spectrogram.dynamic_spectra[:, i]
        spectrum = spectrogram.dynamic_spectra[:, i]
        test_results.spectrum_validated[time] = bool(is_close(analytical_spectrum, 
                                                              spectrum,
                                                              absolute_tolerance))

    return test_results