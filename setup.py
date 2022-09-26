from setuptools import setup, find_packages

install_requires = [
    "django ~= 3.2.1",
    "django-crispy-forms ~=1.14.0",
    "rdcore3",
    "rdcore3.install",
]

tests_require = [
    "pytest",
]

setup(name='debugging_cake_portal',
      version='1.0',
      description="Luminess debugging forum.",
      author="Python Intern Team Luminess",
      install_requires=install_requires,
      package_dir={"": "debugging_cake_portal"},
      packages=find_packages("debugging_cake_portal", exclude=("tests",)),
      test_suite="tests",
      tests_require=tests_require,
      extras_require={
          "test": tests_require,
      },
      )
