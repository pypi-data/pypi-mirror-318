# 🌍 pyquadkey2
[![Documentation](https://docs.muetsch.io/badge.svg)](https://docs.muetsch.io/pyquadkey2/)

![](https://docs.microsoft.com/en-us/bingmaps/articles/media/5cff54de-5133-4369-8680-52d2723eb756.jpg)

This is a feature-rich Python implementation of [QuadKeys](https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system), an approach to **geographical tiling**, popularized by Microsoft to be used for Bing Maps.

In essence, the concept is to **recursively** divide the flat, two-dimensional world map into squares. Each square contains **four squares** as children, which again contain four squares and so on, up **centimeter-level precision**. Each of these squares is **uniquely identifiable with a string** like `021030032`.

For more details on the concept, please refer to
the [original article](https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system).

[muety/pyquadkey2](https://github.com/muety/pyquadkey2) originates from a **fork**
of [buckhx/QuadKey](https://github.com/buckhx/QuadKey), which is not maintained anymore. It builds on top of that
project and adds:

* ✅ Several (critical) [bug fixes](https://github.com/buckhx/QuadKey/pull/15)
* ✅ Python 3 support
* ✅ [Type hints](https://docs.python.org/3.6/library/typing.html) for all methods
* ✅ Higher test coverage
* ✅ Cython backend for improved performance
* ✅ 64-bit integer representation of QuadKeys
* ✅ Additional features and convenience methods

**Please note:** This library is still in development and not considered 100 % stable. You may want to consider [mercantile](https://github.com/mapbox/mercantile/) as an alternative (pure Python) implementation of QuadKeys. Also check [_What the Tile?_](https://labs.mapbox.com/what-the-tile/).

## Installation
### Requirements

This library requires **Python 3.10** or higher. To compile it from source, Cython is required in addition.

### Using Pip
```bash
$ pip install pyquadkey2
```

Pip installation is only tested for Linux and Mac, yet. If you encounter problems with the installation on Windows, please report them as a new issue.

### From archive
```bash
$ wget https://github.com/muety/pyquadkey2/releases/download/0.3.2/pyquadkey2-0.3.2.tar.gz
$ pip install pyquadkey2-0.3.2.tar.gz
```

### From source
#### Prerequisites (`Linux`)
* `gcc`
    * Fedora: `dnf install @development-tools`
    * Ubuntu / Debian: `apt install build-essential`
* `python3-devel`
    * Fedora: `dnf install python3-devel`
    * Ubuntu / Debian: `apt install python3-dev`
    * Others: See [here](https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory/21530768#21530768)

#### Prerequisites (`Windows`)
* Visual C++ Build Tools 2015 (with Windows 10 SDK) (see [here](https://devblogs.microsoft.com/python/unable-to-find-vcvarsall-bat/#i-need-a-package-that-has-no-wheel-what-can-i-do))

#### Build
```bash
# Check out repo
$ git clone https://github.com/muety/pyquadkey2

# Create and active virtual environment (optional)
$ python -m venv ./venv
$ source venv/bin/activate

# Install depencencies
$ pip install -r requirements.txt

# Compile
$ cd src/pyquadkey2/quadkey/tilesystem && python setup.py build_ext --inplace && cd ../../../..

# Install as module
$ pip install .
```

## Developer Notes

### Unit Tests

```bash
python tests/__init__.py
```

### Release

See [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

```bash
pip install setuptools wheel auditwheel
python -m build
cd dist
auditwheel repair *.whl
twine upload --repository testpypi wheelhouse/* ../*.tar.gz
```

## License
Apache 2.0

[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/n1try)
