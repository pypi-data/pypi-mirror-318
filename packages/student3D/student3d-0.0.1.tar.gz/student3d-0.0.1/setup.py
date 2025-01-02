
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="student3D",
    version="0.0.1",
    author="student_v",
    author_email="13974164156@163.com",
    description="none",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vtongxue/student3D",
    project_urls={'bug tracker': 'https://github.com/vtongxue/student3D/issues'},
    classifiers=['Programming Language :: Python :: 3', 'License :: OSI Approved :: MIT License', 'Operating System :: OS Independent'],
    packages=["第三方库/"],
    python_requires=">=3.6",
    install_requires = ['ursina>=3.0.0'],
    entry_points=""
        )