import json
import torch
import faster_whisper
import logging
from typing import Dict, Any, Tuple, List
from .utils import process_language_arg


def find_numeral_symbol_tokens(tokenizer) -> List[int]:
    """Find tokens containing numerals or symbols."""
    numeral_symbol_tokens = [-1]
    for token, token_id in tokenizer.get_vocab().items():
        if any(c in "0123456789%$£" for c in token):
            numeral_symbol_tokens.append(token_id)
    return numeral_symbol_tokens


# Global variable for the Whisper model
whisper_model = None


def initialize_transcriber_model(whisper_model_name, computation_device="cuda" if torch.cuda.is_available() else "cpu"):
    global whisper_model
    if whisper_model is None:
        whisper_model = faster_whisper.WhisperModel(
            model_size_or_path=whisper_model_name,
            device=computation_device,
            compute_type="float32"
        )


def transcribe_audio(
    audio_path: str,
    model_name: str = "tiny.en",
    language: str = "en",  # Default to English if not specified
    device: str = "cuda" if torch.cuda.is_available() else "cpu",
    compute_type: str = "float32",
    batch_size: int = 8,
    suppress_numerals: bool = True
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """
    Transcribe audio using the initialized Whisper model.
    """
    if whisper_model is None:
        raise RuntimeError("Whisper model is not initialized.")

    # Ensure a valid language is set
    language = process_language_arg(language, model_name)

    # Get tokens to suppress
    suppress_tokens = (
        find_numeral_symbol_tokens(whisper_model.hf_tokenizer)
        if suppress_numerals
        else [-1]
    )

    # Load and resample audio
    audio_waveform = faster_whisper.decode_audio(audio_path)

    # Transcribe audio
    if batch_size > 0:
        # Using the BatchedInferencePipeline when batch_size is positive
        segments, info = faster_whisper.BatchedInferencePipeline(whisper_model).transcribe(
            audio_waveform,
            language,
            suppress_tokens=suppress_tokens,
            batch_size=batch_size,
            # Retain timestamps if needed, adjust to True if no timestamps required
            without_timestamps=False,
            vad_filter=True,  # Enable VAD to remove non-speech segments
            language_detection_threshold=0.5,  # Threshold for language detection
            language_detection_segments=3,  # Number of segments for better language detection
            word_timestamps=True,  # Extract word-level timestamps
            chunk_length=30,  # Process audio in 30-second chunks, adjust as necessary
            prepend_punctuations='\"\'“¿([{-',  # Handle punctuation
            append_punctuations='\".。,，!！?？:：”)]}、',  # Handle punctuation
            multilingual=False,  # Enable multilingual support for mixed languages
        )
    else:
        # Using the regular inference model when batch_size is 0
        segments, info = whisper_model.transcribe(
            audio_waveform,
            language,
            suppress_tokens=suppress_tokens,
            # Retain timestamps if needed, adjust to True if no timestamps required
            without_timestamps=False,
            vad_filter=True,  # Enable VAD to remove non-speech segments
            language_detection_threshold=0.5,  # Threshold for language detection
            language_detection_segments=3,  # Number of segments for better language detection
            word_timestamps=True,  # Extract word-level timestamps
            chunk_length=30,  # Process audio in 30-second chunks
            prepend_punctuations='\"\'“¿([{-',  # Handle punctuation
            append_punctuations='\".。,，!！?？:：”)]}、',  # Handle punctuation
            multilingual=False,  # Enable multilingual support for mixed languages
        )

    return segments, info, audio_waveform
