def _cmake_to_bool(s):
    return s.upper() not in ['', '0','FALSE','OFF','N','NO','IGNORE','NOTFOUND']

is_python_package    = _cmake_to_bool("@SKBUILD@")

BUILD_STUB_FILES     = _cmake_to_bool("@BUILD_STUB_FILES@")
BUILD_UMFPACK        = _cmake_to_bool("@BUILD_UMFPACK@")
ENABLE_UNIT_TESTS    = _cmake_to_bool("@ENABLE_UNIT_TESTS@")
INSTALL_DEPENDENCIES = _cmake_to_bool("@INSTALL_DEPENDENCIES@")
USE_CCACHE           = _cmake_to_bool("@USE_CCACHE@")
USE_HYPRE            = _cmake_to_bool("@USE_HYPRE@")
USE_LAPACK           = _cmake_to_bool("@USE_LAPACK@")
USE_MKL              = _cmake_to_bool("@USE_MKL@")
USE_MKL              = _cmake_to_bool("@USE_MKL@")
USE_MUMPS            = _cmake_to_bool("@USE_MUMPS@")
USE_PARDISO          = _cmake_to_bool("@USE_PARDISO@")
USE_UMFPACK          = _cmake_to_bool("@USE_UMFPACK@")

NETGEN_DIR = "@NETGEN_DIR@"

NGSOLVE_COMPILE_DEFINITIONS         = "@NGSOLVE_COMPILE_DEFINITIONS@"
NGSOLVE_COMPILE_DEFINITIONS_PRIVATE = "@NGSOLVE_COMPILE_DEFINITIONS_PRIVATE@"
NGSOLVE_COMPILE_INCLUDE_DIRS        = "@NGSOLVE_COMPILE_INCLUDE_DIRS@"
NGSOLVE_COMPILE_OPTIONS             = "@NGSOLVE_COMPILE_OPTIONS@"

NGSOLVE_VERSION = "@NGSOLVE_VERSION@"
NGSOLVE_VERSION_GIT = "@git_version_string@"
NGSOLVE_VERSION_PYTHON = "@NGSOLVE_VERSION_PYTHON@"

NGSOLVE_VERSION_MAJOR = "@NGSOLVE_VERSION_MAJOR@"
NGSOLVE_VERSION_MINOR = "@NGSOLVE_VERSION_MINOR@"
NGSOLVE_VERSION_TWEAK = "@NGSOLVE_VERSION_TWEAK@"
NGSOLVE_VERSION_PATCH = "@NGSOLVE_VERSION_PATCH@"
NGSOLVE_VERSION_HASH = "@NGSOLVE_VERSION_HASH@"

CMAKE_CXX_COMPILER           = "@CMAKE_CXX_COMPILER@"
CMAKE_CUDA_COMPILER          = "@CMAKE_CUDA_COMPILER@"
CMAKE_C_COMPILER             = "@CMAKE_C_COMPILER@"
CMAKE_LINKER                 = "@CMAKE_LINKER@"
CMAKE_INSTALL_PREFIX         = "@CMAKE_INSTALL_PREFIX@"
CMAKE_CXX_COMPILER_LAUNCHER  = "@CMAKE_CXX_COMPILER_LAUNCHER@"

version = NGSOLVE_VERSION_GIT

def get_cmake_dir():
    import netgen.config as c
    import os.path as p
    d_python = p.dirname(p.dirname(__file__))
    py_to_cmake = p.relpath(
            p.dirname(c.NG_INSTALL_DIR_CMAKE),
            c.NG_INSTALL_DIR_PYTHON
            )
    return p.normpath(p.join(d_python,py_to_cmake, 'ngsolve'))
