import numpy as np
from sympy import im

LANGUAGE = {
    "catonese": "yue",
    "english": "en",
    "mandarin": "zh",
}


class ASR:
    def __init__(
        self,
        model_path: str,
        processor_path: str,
        torch_dtype: str = "float32",
        low_cpu_mem_usage: bool = True,
        use_safetensors: bool = True,
        device: str = "cuda:0",
        batch_size: int = 16,
    ):
        from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_path,
            torch_dtype=torch_dtype,
            low_cpu_mem_usage=low_cpu_mem_usage,
            use_safetensors=use_safetensors,
        )
        self.model = self.model.to(device)
        self.processor = AutoProcessor.from_pretrained(processor_path)
        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=self.model,
            tokenizer=self.processor.tokenizer,
            feature_extractor=self.processor.feature_extractor,
            batch_size=batch_size,
            torch_dtype=torch_dtype,
            device=device,
        )

    def get_asr(self, audio, language, num_beams=1):
        if language == "yue":
            language = "catonese"
        generate_kw = {"num_beams": num_beams}
        return_language = language is None or language == "auto"

        if not return_language:
            generate_kw["language"] = language

        if not isinstance(audio, np.ndarray):
            # load audio from file
            import torchaudio
            from torchaudio import load

            audio, sr = load(audio)
            if sr != 16000:
                audio = torchaudio.transforms.Resample(sr, 16000)(audio)
                sr = 16000

            if len(audio.shape) > 1:
                if audio.shape[0] > 1:
                    raise ValueError("Only mono audio files are supported.")
                audio = audio[0]
            audio = audio.numpy()

        rs = self.pipe(
            audio, generate_kwargs=generate_kw, return_language=return_language
        )
        if return_language:
            language = rs["chunks"][0]["language"]
            language = LANGUAGE.get(language, language)

            return rs["text"], language
        return rs["text"], language
