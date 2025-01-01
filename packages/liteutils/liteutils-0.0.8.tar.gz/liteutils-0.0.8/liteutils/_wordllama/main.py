from typing import List, Tuple, Union

from wordllama import WordLlama

__wllm = None
__dim = None


def __get_word_llama_model(dim: int = 256):
    global __wllm, __dim
    if __wllm is None or __dim != dim:
        __dim = dim
        __wllm = WordLlama.load(dim=dim)
    return __wllm


def wlsplit(text: str) -> List[str]:
    return __get_word_llama_model().split(text)


def wlscore(text1: str, text2: str) -> float:
    return __get_word_llama_model().similarity(text1, text2)


def wlrank(query: str, candidates: List[str], sort: bool = True, batch_size: int = 64) -> List[Tuple[str, float]]:
    return __get_word_llama_model().rank(query, candidates, sort=sort, batch_size=batch_size)


def wldeduplicate(docs: List[str], return_indices: bool = False, threshold: float = 0.5) -> List[str]:
    return __get_word_llama_model().deduplicate(docs, return_indices=return_indices, threshold=threshold)


def wlcluster(docs: List[str], k: int, max_iterations: int = 100, tolerance: float = 1e-4, n_init: int = 3) -> Tuple[
    List[int], float]:
    return __get_word_llama_model().cluster(docs, k=k, max_iterations=max_iterations, tolerance=tolerance, n_init=n_init)


def wlfilter(query: str, docs: List[str], threshold: float = 0.3) -> List[str]:
    return __get_word_llama_model().filter(query, docs, threshold=threshold)


def wltopk(query: str, docs: List[str], k: int) -> List[str]:
    return __get_word_llama_model().topk(query, docs, k=k)


def wlembed(texts: Union[str, List[str]]):
    return __get_word_llama_model().embed(texts)
