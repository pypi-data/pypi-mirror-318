# Copyright (c) 2023 - 2024, Owners of https://github.com/ag2ai
#
# SPDX-License-Identifier: Apache-2.0
#
# Portions derived from  https://github.com/microsoft/autogen are under the MIT License.
# SPDX-License-Identifier: MIT
import os
import platform
import sys

import setuptools

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

# Get the code version
version = {}
with open(os.path.join(here, "autogen/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]


current_os = platform.system()

install_requires = [
    "openai>=1.58",
    "diskcache",
    "termcolor",
    "flaml",
    # numpy is installed by flaml, but we want to pin the version to below 2.x (see https://github.com/microsoft/autogen/issues/1960)
    "numpy>=2.1; python_version>='3.13'",  # numpy 2.1+ required for Python 3.13
    "numpy>=1.24.0,<2.0.0; python_version<'3.13'",  # numpy 1.24+ for older Python versions
    "python-dotenv",
    "tiktoken",
    # Disallowing 2.6.0 can be removed when this is fixed https://github.com/pydantic/pydantic/issues/8705
    "pydantic>=1.10,<3,!=2.6.0",  # could be both V1 and V2
    "docker",
    "packaging",
    "websockets>=14,<15",
    "asyncer>=0.0.8",
]

test = [
    "ipykernel",
    "nbconvert",
    "nbformat",
    "pre-commit",
    "pytest-cov>=5",
    "pytest-asyncio",
    "pytest>=8,<9",
    "pandas",
    "fastapi>=0.115.0,<1",
]

jupyter_executor = [
    "jupyter-kernel-gateway",
    "websocket-client",
    "requests",
    "jupyter-client>=8.6.0",
    "ipykernel>=6.29.0",
]

retrieve_chat = [
    "protobuf==4.25.3",
    "chromadb==0.5.3",
    "sentence_transformers",
    "pypdf",
    "ipython",
    "beautifulsoup4",
    "markdownify",
]

retrieve_chat_pgvector = [*retrieve_chat, "pgvector>=0.2.5"]

graph_rag_falkor_db = ["graphrag_sdk==0.3.3", "falkordb>=1.0.10"]

neo4j = [
    "docx2txt==0.8",
    "llama-index==0.12.5",
    "llama-index-graph-stores-neo4j==0.4.2",
    "llama-index-core==0.12.5",
]

# used for agentchat_realtime_swarm notebook and realtime agent twilio demo
twilio = ["fastapi>=0.115.0,<1", "uvicorn>=0.30.6,<1", "twilio>=9.3.2"]

interop_crewai = ["crewai[tools]>=0.86,<1; python_version>='3.10' and python_version<'3.13'"]
interop_langchain = ["langchain-community>=0.3.12,<1"]
interop_pydantic_ai = ["pydantic-ai==0.0.13"]
interop = interop_crewai + interop_langchain + interop_pydantic_ai

types = ["mypy==1.9.0"] + test + jupyter_executor + interop

if current_os in ["Windows", "Darwin"]:
    retrieve_chat_pgvector.extend(["psycopg[binary]>=3.1.18"])
elif current_os == "Linux":
    retrieve_chat_pgvector.extend(["psycopg>=3.1.18"])

# pysqlite3-binary used so it doesn't need to compile pysqlite3
autobuild = ["chromadb", "sentence-transformers", "huggingface-hub", "pysqlite3-binary"]

# NOTE: underscores in pip install, e.g. pip install ag2[graph_rag_falkor_db], will automatically
# convert to hyphens. So, do not include underscores in the name of extras.

# ** IMPORTANT: IF ADDING EXTRAS **
# PLEASE add them in the setup_ag2.py and setup_autogen.py files

extra_require = {
    "test": test,
    "blendsearch": ["flaml[blendsearch]"],
    "mathchat": ["sympy", "pydantic==1.10.9", "wolframalpha"],
    "retrievechat": retrieve_chat,
    "retrievechat-pgvector": retrieve_chat_pgvector,
    "retrievechat-mongodb": [*retrieve_chat, "pymongo>=4.0.0"],
    "retrievechat-qdrant": [*retrieve_chat, "qdrant_client", "fastembed>=0.3.1"],
    "graph-rag-falkor-db": graph_rag_falkor_db,
    "autobuild": autobuild,
    "captainagent": autobuild + ["pandas"],
    "teachable": ["chromadb"],
    "lmm": ["replicate", "pillow"],
    "graph": ["networkx", "matplotlib"],
    "gemini": [
        "google-generativeai>=0.5,<1",
        "google-cloud-aiplatform",
        "google-auth",
        "pillow",
        "pydantic",
        "jsonschema",
    ],
    "together": ["together>=1.2"],
    "websurfer": ["beautifulsoup4", "markdownify", "pdfminer.six", "pathvalidate"],
    "redis": ["redis"],
    "cosmosdb": ["azure-cosmos>=4.2.0"],
    "websockets": ["websockets>=14.0,<15"],
    "jupyter-executor": jupyter_executor,
    "types": types,
    "long-context": ["llmlingua<0.3"],
    "anthropic": ["anthropic>=0.23.1"],
    "cerebras": ["cerebras_cloud_sdk>=1.0.0"],
    "mistral": ["mistralai>=1.0.1"],
    "groq": ["groq>=0.9.0"],
    "cohere": ["cohere>=5.5.8"],
    "ollama": ["ollama>=0.3.3", "fix_busted_json>=0.0.18"],
    "bedrock": ["boto3>=1.34.149"],
    "twilio": twilio,
    "interop-crewai": interop_crewai,
    "interop-langchain": interop_langchain,
    "interop-pydantic-ai": interop_pydantic_ai,
    "interop": interop,
    "neo4j": neo4j,
}

setuptools.setup(
    name="pyautogen",
    version=__version__,
    author="Chi Wang & Qingyun Wu",
    author_email="support@ag2.ai",
    description="A programming framework for agentic AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ag2ai/ag2",
    packages=setuptools.find_namespace_packages(
        include=[
            "autogen*",
            "autogen.agentchat.contrib.captainagent.tools*",
        ],
        exclude=["test"],
    ),
    package_data={
        "autogen.agentchat.contrib.captainagent": [
            "tools/tool_description.tsv",
            "tools/requirements.txt",
        ]
    },
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extra_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    license="Apache Software License 2.0",
    python_requires=">=3.9,<3.14",
)
