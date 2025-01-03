# real-llama-cpp-python
A simple custom wrapper for llama.cpp models in Python, support seamlessly interaction with LangChain. As the name suggests, it is truly a wrapper for llama.cpp, you should have installed llama.cpp into your machine prior to this.

## Background

While it might seem intuitive that llama-cpp-python would seamlessly integrate with llama.cpp, the reality is that installing llama-cpp-python is a pain in the bum. It is NOT simple as described `pip install llama-cpp-python`.  

Langchain, by default, supports [llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp/). real-llama-cpp-python is a simplified and an alternative library designed to seamlessly integrate with LangChain while avoiding the pain of installing the library llama-cpp-python. 

llama.cpp can be installed or built easily. The llama.cpp community is also very active that any issue with the installation can be resolved in a few days (unlike llama-cpp-python).  

## Installation
As the name said, it is truly a wrapper for llama.cpp, you should first install llama.cpp into your machine. 

### 1 Install llama.cpp first

- **Highly recommend this method** Clone [llama.cpp](https://github.com/ggerganov/llama.cpp/tree/master) repository and build locally, see [how to build](https://github.com/ggerganov/llama.cpp/blob/master/docs/build.md)
- On MacOS or Linux, install `llama.cpp` via [brew, flox or nix](https://github.com/ggerganov/llama.cpp/blob/master/docs/install.md). Noted that, this brew install may not support GPU.
- Use a ``llama.cpp`` Docker image, see [documentation for Docker](https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md). 
- **Have not tested yet** Download pre-built binaries from [releases](https://github.com/ggerganov/llama.cpp/releases).

After successfully built/installed llama.cpp. You want to add llama.cpp directory to your `PATH` permanently by editing your shell configuration file:
```
vim ~/.bashrc 
```
or
```
source ~/.zshrc
```
Add the following line: 
```
export PATH=$PATH:/path/to/your/llama.cpp/build/bin
```

Save and run `source ~/.bashrc`  or `source ~/.zshrc`
You should be able to run `llama-cli` and `llama-server` from any directory. Verify the accessibility, run the following commands in any directory 

```
llama-cli --help
llama-server --help
```

### 2 Install llama.cpp
Now, you can install real-llama-cpp-python by either install the stable version through `pip install`
```bash
pip install real-llama-cpp-python
```
or clone the github repository for the developing features.

```
git clone https://github.com/minhtran1309/real-llama-cpp-python.git
cd real-llama-cpp-python
pip install -e .
```

### 3 Running the tests