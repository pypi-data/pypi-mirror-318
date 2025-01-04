from setuptools import setup, find_packages
# sudo apt install libcudnn8
setup(
    name="fast-whisper-diarizer",
    version="0.1.24",
    license='MIT',
    author='Salim',
    author_email='salimkt25@gmail.com',
    description='A package for audio transcription and speaker diarization using Whisper and NeMo toolkit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/salimkt/fast-whisper-diarizer',
    packages=find_packages(),
    install_requires=[
        'faster-whisper==1.1.0',
        'ctranslate2==4.4.0',
        'nemo-toolkit==2.1.0rc0',
        'torch==2.5.1',
        'torchaudio==2.5.1',
        'omegaconf==2.3.0',
        'nltk==3.9.1',
        'wget==3.2',
        'deepmultilingualpunctuation==1.0.1',
        'demucs==4.0.1',
        'numpy==1.26.4',
        'hydra-core==1.3.2',
        'lhotse==1.29.0',
        'jiwer',
        'webdataset==0.2.100',
        'datasets==3.2.0',
        'editdistance',
        'IPython==8.31.0',
        'ctc_forced_aligner'
    ],
    entry_points={
        'console_scripts': [
            'whisper-diarize=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
