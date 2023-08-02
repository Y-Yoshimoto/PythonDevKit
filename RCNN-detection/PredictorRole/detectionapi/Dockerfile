FROM python:3.10-slim-bullseye AS builder
LABEL maintaner='y-yoshimoto'
## Document
# https://detectron2.readthedocs.io/en/latest/tutorials/install.html
## Install build tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends git gcc g++ \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates
RUN pip install --upgrade pip \
    && pip install --no-cache-dir torch torchvision setuptools wheel Cython\
    && pip freeze > requirements.lock
# Build pycocotools
RUN pip download --no-dependencies pycocotools \
    && mkdir -p pycocotools && tar -xvf ./pycocotools-*.tar.gz -C pycocotools --strip-components 1
WORKDIR /pycocotools
RUN python setup.py bdist_wheel \
    && cp /pycocotools/dist/pycocotools-*.whl /tmp/
# Build detectron2
WORKDIR /
RUN git clone https://github.com/facebookresearch/detectron2.git
WORKDIR /detectron2
RUN python setup.py bdist_wheel && cp /detectron2/dist/detectron2-*.whl /tmp/

# Run Images
FROM python:3.10-slim-bullseye
COPY --from=builder /tmp/*.whl /tmp/
# Install OpenCV lib
RUN apt-get update \
    && apt-get install -y --no-install-recommends libopencv-dev libgl1-mesa-dev\
    && apt-get -y clean
# Install pip package
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir /tmp/pycocotools-*.whl \
    && pip install --no-cache-dir /tmp/detectron2-*.whl \
    && pip install --no-cache-dir -r requirements.txt \
    && pip freeze > requirements.lock \
    WORKDIR /usr/src
COPY ./src/* /usr/src
WORKDIR /usr/src/

RUN mkdir -p /labeldata
VOLUME ["/usr/src", "/labeldata"]

## 通常起動用
#CMD ["/usr/bin/python3", "app.py"]
## 検証用
CMD [ "tail", "-f", "/dev/null"]
