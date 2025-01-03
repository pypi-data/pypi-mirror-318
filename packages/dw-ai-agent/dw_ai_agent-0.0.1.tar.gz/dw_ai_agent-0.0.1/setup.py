from setuptools import setup, find_packages

setup(
    name='dw-ai-agent',  # Replace with your project name
    version='0.0.1',  # Replace with your project's version
    description='AI Agent for Mobile Codebases',
    author='Dashwave Inc',  # Replace with your name
    author_email='hello@dashwave.io',  # Replace with your email
    url='https://github.com/dashwave/ai-agent',  # Replace with your project's URL
    packages=find_packages(),
    install_requires=[
        'chromadb==0.5.5',
        'numpy==1.26.4',
        'openai==1.55.3',
        'Requests==2.32.3',
        'scikit_learn==1.5.1',
        'tiktoken==0.7.0',
        'fastapi==0.115.2',
        'pydantic==2.9.2',
        'python-dotenv==1.0.1',
        'setuptools==75.1.0',
        'tree_sitter==0.21.3',
        'tree_sitter_languages==1.10.2',
        'voyageai==0.2.3',
        'wheel==0.44.0',
        'compextAI==0.0.18',
        'grpcio==1.68.1',
        'grpcio-tools==1.68.1',
        'bs4==0.0.2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your project's license
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'dw-ai-agent=main:main',  # Replace 'your-command-name' with your desired shell command
        ],
    },
    python_requires='>=3.10',  # Replace with your project's Python version requirements
)
