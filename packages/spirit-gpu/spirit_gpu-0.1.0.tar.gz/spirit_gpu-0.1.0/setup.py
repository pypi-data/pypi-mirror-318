"""
Set up the package.
"""

from setuptools import setup, find_packages


def load_requirements():
    with open("requirements.txt", encoding="UTF-8") as requirements:
        return requirements.read().splitlines()


extras_require = {
    "test": [
        "pytest",
    ]
}

if __name__ == "__main__":

    setup(
        name="spirit-gpu",
        use_scm_version=True,
        setup_requires=["setuptools>=45", "setuptools_scm", "wheel"],
        install_requires=load_requirements(),
        extras_require=extras_require,
        packages=find_packages(),
        python_requires=">=3.9",
        description="Python serverless framework for Datastone Spirit GPU.",
        long_description="For more details, please visit https://github.com/datastone-spirit/spirit-gpu",
        long_description_content_type="text/markdown",
        author="spirit",
        author_email="pypi@datastone.cn",
        url="https://github.com/datastone-spirit",
        project_urls={
            "Documentation": "https://github.com/datastone-spirit/spirit-gpu/blob/main/README.md",
            "Source": "https://github.com/datastone-spirit/spirit-gpu",
            "Bug Tracker": "https://github.com/datastone-spirit/spirit-gpu/issues",
        },
        include_package_data=True,  # Include package data specified in MANIFEST.in or package_data
        package_data={
            "spirit_gpu": ["resources/worker-template/**/*"],
        },
        classifiers=[
            "Topic :: Software Development :: Libraries :: Application Frameworks",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.9",
            "Operating System :: OS Independent",
            "Environment :: GPU",
        ],
        keywords=[
            "serverless",
            "ai",
            "gpu",
            "machine learning",
            "SDK",
            "library",
            "python",
            "API",
        ],
        license="MIT",
        entry_points={
            "console_scripts": [
                "spirit-gpu-builder = spirit_gpu.cmd:main",
            ],
        },
    )
