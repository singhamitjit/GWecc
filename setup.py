from setuptools import setup, Extension
import os

GWecc_sources = (   "AntennaPattern.cpp",
                    "EccentricResiduals_Anl.cpp",
                    "EccentricResiduals.cpp",
                    "EccentricResiduals_Num.cpp",
                    "GWecc.cpp",
                    "Evolve.cpp",
                    "FourierWaveform.cpp",
                    "mikkola.cpp",
                    "OrbitalEvolution.cpp",
                    "PN.cpp",
                    "Precompute_Orbit.cpp",
                    "EccentricWaveform.cpp",
                    "FeStat.cpp"
                )
src_dir = "GWecc/"
current_dir = os.path.dirname(os.path.realpath(__file__))
include_dir = current_dir+'/'+"GWecc/"
GWecc_sources = [src_dir+src_file for src_file in GWecc_sources] + ['enterprise_GWecc/GWecc.i']

GWecc_cpp_module = Extension('enterprise_GWecc._GWecc', 
                             sources=GWecc_sources,
                             include_dirs=[include_dir, current_dir, '/usr/include/eigen3/'],
                             libraries=['gsl','gslcblas'],
                             swig_opts=['-c++'],
                             extra_compile_args=['-std=c++17', '-Wno-unused-result']
                            )

setup(  name = 'enterprise_GWecc',
        version = '0.1',
        description = "Computes pulsar TOA delays due to gravitational waves from eccentric supermassive binary sources.",
        author = "Abhimanyu Susobhanan",
        author_email = "s.abhimanyu@tifr.res.in",
        ext_modules = [GWecc_cpp_module],
        py_modules = ['enterprise_GWecc.GWecc', 'enterprise_GWecc.enterprise_GWecc'],
        scripts = ['examples/Example1.py']
    )
