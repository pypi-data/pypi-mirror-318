# langchain-s3-cached-embeddings

Proxies _**any**_ langchain `Embeddings` class such as `OpenAIEmbeddings`, `GoogleGenerativeAIEmbeddings`, persisting all generated embeddings to S3. This allows subsequent calls to _optionally_ leverage the cached embeddings, avoiding additional and unecessary cost of re-embedding. 
## Install

```bash
pip install langchain-s3-cached-embeddings
```

## Usage

```python
from langchain_s3_text_loaders import S3DirectoryLoader

   embeddings = S3EmbeddingsConduit(
        embeddings=OpenAIEmbeddings(model=model), # required
        bucket="my-embeddings-bucket", # required
        prefix="my-optional-prefix"
    )

```

## Advanced Usage

```python
   embeddings = S3EmbeddingsConduit(
        embeddings=OpenAIEmbeddings(model=model), # required
        bucket="my-embeddings-bucket", # required
        prefix="my-optional-prefix"
        filenaming_function: Optional[Callable[[str, int], str]] = None,
        cache_behavior = CacheBehavior.NO_CACHE):

```

## Usage Options

- `embeddings` - (required) any class implementing `langchain_core.embeddings.Embeddings`
- `bucket` - (required) the s3 bucket name
- `prefix` - (required) the s3 key name
- `filenaming_function` - (optional) redeives two arguments, 1. the file contents (`str`), 2. the index (`int`) e.g. `9` for the `10`the document and returns the filename ()`str`)
- `cache_behavior` - (optional) 
    - `CacheBehavior.NO_CACHE` - do not use cached embeddings, instead embed using the `embeddings` class' standard `embed_documents(...)` method
    - `CacheBehavior.ONLY_CACHE` - use cached embeddings. if the embeddings are no present, it raises an exception

## License
MIT
