# FROM debian:buster
FROM m8ttyb/debian10-test-iris:1.0
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y -f autoconf autoconf-archive libicu-dev \
  automake libcairo2-dev libgtk2.0-dev \
  libjpeg62-turbo-dev libopencv-contrib-dev libopencv-dev \
  libopencv-objdetect-dev libopencv-superres-dev \
  libopencv-videostab-dev libpango1.0-dev libpng-dev \
  libpng16-16 libtiff5-dev libtool p7zip-full pkg-config \
  python3.7-tk python3.7-dev python3-pip unzip wget wmctrl \
  xdotool xsel zlib1g-dev

RUN python3.7 -m pip install pipenv psutil zstandard

# Create a dir for the builds and install leptonica
# RUN mkdir -p /iris-tmp && cd /iris-tmp \
RUN cd /tmp \
  && wget http://www.leptonica.org/source/leptonica-1.76.0.tar.gz \
  && tar xopf leptonica-1.76.0.tar.gz \
  && cd leptonica-1.76.0 \
  && ./configure && make && make install

# Install Tesseract
# RUN cd /iris-tmp \
RUN cd /tmp \
  && wget https://github.com/tesseract-ocr/tesseract/archive/4.0.0.tar.gz \
  && tar xopf 4.0.0.tar.gz \
  && cd tesseract-4.0.0 \
  && ./autogen.sh \
  && ./configure --enable-debug \
  && LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make \
  && make install \
  && make install -langs \
  && ldconfig

# Install tessdata
#RUN cd /iris-tmp \
#  && wget https://github.com/tesseract-ocr/tessdata/archive/4.0.0.zip \
#  && unzip 4.0.0.zip \
#  && cd tessdata-4.0.0 \
#  && ls /usr/local/share/tessdata/ \
#  && mv ./* /usr/local/share/tessdata/

# Clean up
# RUN cd / && rm -rf /iris-tmp && rm -rf ~/.ccache \
RUN cd / && rm -rf /tmp/* && rm -rf ~/.ccache \
  && ls ~/.cache && rm -rf ~/.npm \
  && apt-get clean && apt-get autoclean

ADD docker/install_iris_deps.sh /
RUN bash -c "/install_iris_deps.sh"
