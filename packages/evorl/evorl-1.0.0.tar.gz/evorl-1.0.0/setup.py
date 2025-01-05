from setuptools import setup, find_packages

# Try to read README.md, use empty string if it doesn't exist
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = ""

setup(
    name="evorl",
    version="1.0.0",
    author="Alex Zhang",
    author_email="zhangalex1237@gmail.com",
    description="An evolutionary reinforcement learning framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhangalex1/evorl",
    project_urls={
        "Bug Tracker": "https://github.com/zhangalex1/evorl/issues",
        "Documentation": "https://evorl.ai",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "torch>=1.8.0",
        "numpy>=1.19.0",
        "gymnasium>=0.26.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
            "mypy>=0.9",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "sphinx-autodoc-typehints>=1.12",
        ],
        "examples": [
            "wandb>=0.12.0",
            "mujoco>=2.2.0",
        ],
    }
) 