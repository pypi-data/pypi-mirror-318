from setuptools import setup, find_packages

setup(

    name="adaletCleaning",
    version= "0.1.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'adaletCleaning': ['resources/*.txt','resources/*.json','resources/*.xml'],
    },
    install_requires=[],
    description="Veri temizleme işlemleri içeren kütüphane",
    author="Murat Tekdemir",
    python_requires='>=3.6',
)
