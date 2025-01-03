import unittest
from real_llamacpp import CustomLlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.output_parsers import StrOutputParser

if __name__ == "__main__":
    model_path = "/home/minhtran/Projects/clinical_trial_llm_translation/models/Mistral-Nemo-Instruct-2407.Q5_K_S.gguf"
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = CustomLlamaCpp(model_path=model_path, temperature=0.,
        max_tokens=900,n_ctx=50000,
        n_gpu_layers=40,
        top_p=1,
        n_batch=64,
        callback_manager=callback_manager,
        verbose=True)
    print(llm)
    prompt = '### Instruction: How many R in the word strawberry?\n\n ### Response: \n'
    output = llm.invoke(prompt)
    print(output)
    
    