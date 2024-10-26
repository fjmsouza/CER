FROM python:3.12.4-alpine3.20

RUN apk update && apk add --no-cache \
    make \
    gcc \
    g++ \
    python3-dev \
    musl-dev \
    linux-headers \
    git \
    curl \
    bash \
    openssh \
    zsh \
    starship \
    && adduser -D -s /bin/zsh -u 1000 cer_usr \
    && mkdir -p /data/input /data/output /data/train /model/params \
    && chown -R cer_usr:cer_usr /data \
    && chown -R cer_usr:cer_usr /model/params

USER cer_usr

ENV PATH="/home/cer_usr/.local/bin:${PATH}"
ENV ZSH_THEME starship

COPY --chown=cer_usr .zshrc /home/cer_usr/
COPY --chown=cer_usr starship.toml /home/cer_usr/.config/

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create true \
    && poetry config virtualenvs.prefer-active-python true \
    && poetry config virtualenvs.in-project true

WORKDIR /workspace
COPY ../ .

CMD ["tail", "-f", "/dev/null"]