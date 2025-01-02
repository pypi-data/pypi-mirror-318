# SPDX-FileCopyrightText: © 2024 Jimmy Fitzpatrick <jcfitzpatrick12@gmail.com>
# This file is part of SPECTRE
# SPDX-License-Identifier: GPL-3.0-or-later

from abc import ABC, abstractmethod
from typing import Callable, Optional
from numbers import Number

from spectre_core.exceptions import ModeNotFoundError
from ._spec_names import SpecNames
from spectre_core.capture_configs import (
    CaptureTemplate, CaptureModes, Parameters, Bound, PValidators, PNames,
    get_base_capture_template, get_base_ptemplate, OneOf, CaptureConfig
)

class BaseReceiver(ABC):
    def __init__(self, 
                 name: str, 
                 mode: Optional[str] = None):
        self._name = name

        self._specs: dict[str, Number | list[Number]] = {}
        self._add_specs()
        
        self._capture_methods: dict[str, Callable] = {}
        self._add_capture_methods()
    
        self._pvalidators: dict[str, Callable] = {}
        self._add_pvalidators()

        self._capture_templates: dict[str, CaptureTemplate] = {}
        self._add_capture_templates()

        self.mode = mode


    @abstractmethod
    def _add_specs(self) -> None:
        pass
    

    @abstractmethod
    def _add_capture_methods(self) -> None:
        pass


    @abstractmethod
    def _add_pvalidators(self) -> None:
        pass


    @abstractmethod
    def _add_capture_templates(self) -> None:
        pass

    
    @property
    def name(self) -> str:
        return self._name
    

    @property
    def capture_methods(self) -> dict[str, Callable]:
        return self._capture_methods
    

    @property
    def pvalidators(self) -> dict[str, Callable]:
        return self._pvalidators


    @property
    def capture_templates(self) -> dict[str, CaptureTemplate]:
        return self._capture_templates


    @property
    def specs(self) -> dict[str, Number]:
        return self._specs


    @property
    def modes(self) -> list[str]:
        capture_method_modes    = list(self.capture_methods.keys())
        pvalidator_modes        = list(self.pvalidators.keys())
        capture_template_modes  = list(self.capture_templates.keys())

        if capture_method_modes == pvalidator_modes == capture_template_modes:
            return capture_method_modes
        else:
            raise ValueError(f"Mode mismatch for the receiver {self.name}.")


    @property
    def mode(self) -> str:
        return self._mode
    

    @mode.setter
    def mode(self, value: Optional[str]) -> None:
        if (value is not None) and value not in self.modes:
            raise ModeNotFoundError((f"{value} is not a defined mode for the receiver {self.name}. "
                                     f"Expected one of {self.modes}"))
        self._mode = value


    @property
    def capture_method(self) -> Callable:
        return self.capture_methods[self.mode]


    @property
    def pvalidator(self) -> Callable:
        return self.pvalidators[self.mode]


    @property
    def capture_template(self) -> CaptureTemplate:
        return self._capture_templates[self.mode]


    def add_capture_method(self,
                           mode: str,
                           capture_method: Callable) -> None:
        self._capture_methods[mode] = capture_method


    def add_pvalidator(self,
                      mode: str,
                      pvalidator: Callable) -> None:
        self._pvalidators[mode] = pvalidator


    def add_capture_template(self,
                             mode: str,
                             capture_template: CaptureTemplate) -> CaptureTemplate:
        self._capture_templates[mode] = capture_template


    def add_spec(self,
                 name: str,
                 value: Number) -> None:
        self.specs[name] = value


    def get_spec(self, 
                 spec_name: str) -> Number | list[Number]:
        if spec_name not in self.specs:
            raise KeyError(f"Spec not found with name '{spec_name}' "
                           f"for the receiver '{self.name}'")
        return self.specs[spec_name]


    def start_capture(self, 
                      tag: str) -> None:
        self.capture_method( tag, self.load_parameters(tag) )


    def save_parameters(self,
                        tag: str,
                        parameters: Parameters,
                        force: bool = False) -> None:
        
        parameters = self.capture_template.apply_template(parameters)
        self.pvalidator(parameters)

        capture_config = CaptureConfig(tag)
        capture_config.save_parameters(self.name,
                                       self.mode,
                                       parameters,
                                       force=force)

    def load_parameters(self,
                        tag: str) -> Parameters:
        capture_config = CaptureConfig(tag)

        parameters = self.capture_template.apply_template(capture_config.parameters)
        self.pvalidator(parameters)
        
        return parameters