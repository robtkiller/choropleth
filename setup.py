from setuptools import setup

setup(name='choropleth',
        version='0.1',
        description='Creates filled-map images for data analysis',
        url='http://github.com/robtkiller/choropleth',
        author='robtkiller',
        author_email='rtk@kilareski.net',
        license='MIT',
        packages=['choropleth'],
        install_requires=[
            'beautifulsoup4'
        ],
        include_package_data=True,
        zip_safe=False )

