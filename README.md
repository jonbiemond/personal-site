# Personal Site
My website. Copied from https://github.com/duarteocarmo/duarteocarmo.com

## Serve locally
```bash
uv run make html
uv run make serve
```

## Update dependencies on host
Currently deployed to [Cloudflare Pages](https://www.cloudflare.com/products/pages/)
which installs dependencies from `requirements.txt`.
```bash
uv export --format requirements.txt > requirements.txt
```

## Install
```bash
uv sync
```
