FROM gcr.io/distroless/python3
ARG UID
ARG GID
ENV USER=$UID
ENV GROUP=$GID
RUN useradd -m -u $USER -g $GROUP
USER $USER
RUN cd ~ && mkdir brush-fire
WORKDIR ~/brush-fire
COPY * .
RUN pip3 install -r requirements.txt
CMD ['./test.py', 'bush_graph_data.txt']