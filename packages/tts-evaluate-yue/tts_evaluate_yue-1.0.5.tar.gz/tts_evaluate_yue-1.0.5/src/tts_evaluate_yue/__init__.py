def load_cer():
    import os

    import evaluate

    cer_asr = evaluate.load(os.path.join(os.path.dirname(__file__), "cer"))
    return cer_asr


class Normalizer:
    def __init__(self):
        from yue_normalizer.chinese_normalizer import TextNorm
        from yue_normalizer.tools import han_normalize

        self.text_norm = TextNorm(remove_fillers=True, remove_space=True)
        self.han_normalize = han_normalize

    def normalize(self, text):
        return self.text_norm(self.han_normalize(text))
