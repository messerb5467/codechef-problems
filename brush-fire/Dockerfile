FROM gcr.io/google-appengine/python
ARG username
ARG uid
ARG gid
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN groupadd -g $GID $USER && \
    adduser --disabled-password \
            --uid $UID \
            --gid $GID \
            --home $HOME \
            $USER
USER $USER
COPY * $HOME/brush-fire/
WORKDIR $HOME/brush-fire
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 ${HOME}/brush-fire/test_driver.py 'bush_graph_data.txt'