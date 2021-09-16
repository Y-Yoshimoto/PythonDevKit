# build
FROM fedora:latest
# https://hub.docker.com/_/haskell?tab=description
LABEL  maintainer "y.yoshimoto"
RUN echo "fastestmirror=1" >> /etc/dnf/dnf.conf && \
    dnf update -y && \
    dnf install -y ghc cabal-install stack unzip nkf && \
    dnf clean all 
RUN cabal update && cabal install split --lib

RUN curl -O https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip && \
    unzip ken_all.zip && rm -f ken_all.zip && nkf -w --overwrite KEN_ALL.CSV

# add code
RUN mkdir -p /code/export
COPY ./code /code/
RUN ghc /code/convert.hs
WORKDIR /code
#&& /code/convert
#CMD ["/code/convert"]
CMD ["tail", "-f", "/dev/null"]