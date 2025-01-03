from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Sequence,
    Type, List,
    Union, Iterator,
    Mapping, 
    Optional
)
from pathlib import Path
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk
from pydantic import Field, model_validator
from langchain_core.callbacks.manager import CallbackManagerForLLMRun

class CustomLlamaCpp(LLM):
    """llama.cpp model.

    To use, you should have the llama.cpp library installed (no need to install llama-cpp-python), 
    Check out: https://github.com/ggerganov/llama.cpp
    """
    client: Any = None  #: :meta private:
    model_path: str
    """REQUIRED: The path to the Llama model file."""

    lora_base: Optional[str] = None
    """The path to the Llama LoRA base model."""

    lora_path: Optional[str] = None
    """The path to the Llama LoRA. If None, no LoRa is loaded."""

    n_ctx: int = Field(512, alias="n_ctx")
    """Token context size, Default 512"""

    n_parts: int = Field(-1, alias="n_parts")
    """ Number of parts to split the model into.
    If -1, the number of parts is automatically determined."""

    seed: int = Field(-1, alias="seed")
    """Seed. If -1, a random seed is used."""

    # f16_kv: bool = Field(True, alias="f16_kv")
    # """Use half-precision for key/value cache."""

    logits_all: bool = Field(False, alias="logits_all")
    """Return logits for all tokens, not just the last token."""

    vocab_only: bool = Field(False, alias="vocab_only")
    """Only load the vocabulary, no weights."""

    use_mlock: bool = Field(False, alias="use_mlock")
    """Force system to keep model in RAM."""

    n_threads: Optional[int] = Field(None, alias="n_threads")
    """Number of threads to use.
    If None, the number of threads is automatically determined."""

    n_batch: Optional[int] = Field(8, alias="n_batch")
    """Number of tokens to process in parallel.
    Should be a number between 1 and n_ctx."""

    n_gpu_layers: Optional[int] = Field(None, alias="n_gpu_layers")
    """Number of layers to be loaded into gpu memory. Default None."""

    suffix: Optional[str] = Field(None)
    """A suffix to append to the generated text. If None, no suffix is appended."""

    max_tokens: Optional[int] = 256
    """The maximum number of tokens to generate."""

    temperature: Optional[float] = 0.8
    """The temperature to use for sampling."""

    top_p: Optional[float] = 0.95
    """The top-p value to use for sampling."""

    logprobs: Optional[int] = Field(None)
    """The number of logprobs to return. If None, no logprobs are returned."""

    echo: Optional[bool] = False
    """Whether to echo the prompt."""

    stop: Optional[List[str]] = []
    """A list of strings to stop generation when encountered."""

    repeat_penalty: Optional[float] = 1.1
    """The penalty to apply to repeated tokens."""

    top_k: Optional[int] = 40
    """The top-k value to use for sampling."""

    # last_n_tokens_size: Optional[int] = 64
    # """The number of tokens to look back when applying the repeat_penalty."""

    use_mmap: Optional[bool] = True
    """Whether to keep the model loaded in RAM"""

    rope_freq_scale: Optional[float] = 1.0
    """Scale factor for rope sampling."""

    rope_freq_base: Optional[float] = 10000.0
    """Base frequency for rope sampling."""

    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Any additional parameters to pass to llama.cpp"""

    streaming: Optional[bool] = False
    """Whether to stream the results, token by token."""

    grammar_path: Optional[Union[str, Path]] = None
    """
    grammar_path: Path to the .gbnf file that defines formal grammars
    for constraining model outputs. For instance, the grammar can be used
    to force the model to generate valid JSON or to speak exclusively in emojis. At most
    one of grammar_path and grammar should be passed in.
    """
    grammar: Optional[Union[str, Any]] = None
    """
    grammar: formal grammar for constraining model outputs. For instance, the grammar 
    can be used to force the model to generate valid JSON or to speak exclusively in 
    emojis. At most one of grammar_path and grammar should be passed in.
    """

    verbose: bool = True
    """Print verbose output to stderr."""
    """A custom chat model that echoes the first `n` characters of the input.

    When contributing an implementation to LangChain, carefully document
    the model including the initialization parameters, include
    an example of how to initialize the model and include any relevant
    links to the underlying models documentation or API.

    Example:

        .. code-block:: python

            model = CustomLlamaCpp(model='Mistral-Nemo-Instruct-2407.Q5_K_S.gguf')
            result = model.invoke([HumanMessage(content="hello")])
            result = model.batch([[HumanMessage(content="hello")],
                                 [HumanMessage(content="world")]])
    """
    verbosity: Optional[float] = 0.
    

    # n: int
    # """The number of characters from the last message of the prompt to be echoed."""
    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling llama_cpp."""
        params = {
            "suffix": self.suffix,
            "temp": self.temperature,
            "top_p": self.top_p,
            "logprobs": self.logprobs,
            "echo": self.echo,
            "stop_sequences": self.stop,  # Consistent with LLM class convention
            "repeat_penalty": self.repeat_penalty,
            "top_k": self.top_k,
            "ctx_size": self.n_ctx,
            "batch-size": self.n_batch,
            "n_gpu_layers": self.n_gpu_layers,
            "logits_all": self.logits_all,
            "vocab_only": self.vocab_only,
            "use_mlock": self.use_mlock,
            "seed": self.seed,
            "verbosity": self.verbosity,
        }
    
        # Add grammar-specific parameters
        if self.grammar_path:
            params["grammar_path"] = self.grammar_path
        if self.grammar:
            params["grammar"] = self.grammar
    
        # Include additional kwargs if provided
        params.update(self.model_kwargs)
    
        return params
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Run the LLM on the given input.

        Override this method to implement the LLM logic.

        Args:
            prompt: The prompt to generate from.
            stop: Stop words to use when generating. Model output is cut off at the
                first occurrence of any of the stop substrings.
                If stop tokens are not supported consider raising NotImplementedError.
            run_manager: Callback manager for the run.
            **kwargs: Arbitrary additional keyword arguments. These are usually passed
                to the model provider API call.

        Returns:
            The model output as a string. Actual completions SHOULD NOT include the prompt.
        """
        import subprocess
        print('I am jumping around here')
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        # Combine default parameters with any overrides provided via kwargs
        params = {**self._default_params, **kwargs}
        params["prompt"] = prompt  # Add the input prompt explicitly
        # execute llama-cli
        command = ["llama-cli", "-m", self.model_path]
        # Add parameters 
        for key, value in params.items():
            if value is None:
                continue  
            if isinstance(value, bool):  
                if value:
                    command.extend([f"--{key.replace('_', '-')}", str(value)])
            elif isinstance(value, list):  
                for item in value:
                    command.extend([f"--{key.replace('_', '-')}", str(item)])
            else:  # Handle standard key-value parameters
                command.extend([f"--{key.replace('_', '-')}", str(value)])
        # print(command)
        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return result.stdout.strip()  # Return the model's output
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Error running llama-cli: {e.stderr.strip()}"
            ) 
        except FileNotFoundError as e:
            raise RuntimeError(
                f"Command '{command[0]}' not found. Make sure it is installed llama.cpp and added llama.cpp to PATH."
            ) from e
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {str(e)}") from e

    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        """Stream the LLM on the given prompt.

        This method should be overridden by subclasses that support streaming.

        If not implemented, the default behavior of calls to stream will be to
        fallback to the non-streaming version of the model and return
        the output as a single chunk.

        Args:
            prompt: The prompt to generate from.
            stop: Stop words to use when generating. Model output is cut off at the
                first occurrence of any of these substrings.
            run_manager: Callback manager for the run.
            **kwargs: Arbitrary additional keyword arguments. These are usually passed
                to the model provider API call.

        Returns:
            An iterator of GenerationChunks.
        """
        raise Exception("Not yet support streamming (I suppose that this should trigger the llama-server command). Wait for the next update")
        for char in prompt[: self.n]:
            chunk = GenerationChunk(text=char)
            if run_manager:
                run_manager.on_llm_new_token(chunk.text, chunk=chunk)

            yield chunk

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Return a dictionary of identifying parameters."""
        return {**self._default_params}

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "CustomLlamaCpp"