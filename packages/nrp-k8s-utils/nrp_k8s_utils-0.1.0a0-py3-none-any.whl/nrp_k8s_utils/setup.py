from setuptools import setup, find_packages

setup(
    name="nrp_k8s_utils",
    version="1.0.0b1",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "cryptography",
    ],
    description="A utility package for researchers using the NRP Kubernetes cluster.",
    author="Trevin Lee",
    author_email="trl008@ucsd.edu",
    url="https://gitlab.nrp-nautilus.io/Trevin/nrp_k8s_utils",
)