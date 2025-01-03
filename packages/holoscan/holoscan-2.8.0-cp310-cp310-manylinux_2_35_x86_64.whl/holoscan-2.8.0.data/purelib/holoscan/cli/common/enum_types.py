"""
SPDX-FileCopyrightText: Copyright (c) 2023-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""  # noqa: E501

from enum import Enum


class ApplicationType(Enum):
    PythonModule = "Python Module"
    PythonFile = "Python File"
    CppCMake = "C++"
    Binary = "Binary"


class SdkType(Enum):
    """
    Note the values assigned are used as entry_points in setup.py for detecting the SDK to use.
    """

    Holoscan = "holoscan"
    MonaiDeploy = "monai-deploy"


class Arch(Enum):
    amd64 = "linux/amd64"
    arm64 = "linux/arm64"


class Platform(Enum):
    IGXOrinDevIt = "igx-orin-devkit"
    JetsonAgxOrinDevKit = "jetson-agx-orin-devkit"
    X64Workstation = "x64-workstation"
    SBSA = "sbsa"


class PlatformConfiguration(Enum):
    iGPU = "igpu"  # noqa: N815
    dGPU = "dgpu"  # noqa: N815
    CPU = "cpu"
