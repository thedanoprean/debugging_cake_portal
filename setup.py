from setuptools import setup, find_packages

install_requires = [
    "django ~= 4.0",
    "django-crispy-forms ~=1.14.0",
    "jadecore3",
    "jadestream",
    "rdcore3",
    "rdcore3.install",
    "rdcore3.qronos",
]

tests_require = [
    "pytest",
]

setup(name='debugging_cake_portal',
      version='0.1.1',
      description="Luminess debugging forum.",
      author="Python Intern Team Luminess",
      install_requires=install_requires,
      package_dir={"": "src"},
      packages=find_packages("src", exclude=("tests",)),
      test_suite="tests",
      tests_require=tests_require,
      extras_require={
          "test": tests_require,
      },
)
