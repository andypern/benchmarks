FROM nlknguyen/alpine-mpich
MAINTAINER andypern@gmail.com

RUN sudo apk add python3 python3-dev py-pip --no-cache
RUN sudo pip3 install mpi4py
RUN sudo rm /usr/bin/python
RUN sudo ln -s /usr/bin/python3 /usr/bin/python

ADD mpitestscratchBIGFILES.py /project/mpitestscratchBIGFILES.py
ADD mpitestscratchLOTSofFILES.py /project/mpitestscratchLOTSofFILES.py
RUN sudo chmod +x /project/mpi*py


# if you need to run as root
USER root

# run commands as root

# switch back to non-root user

CMD ["/bin/ash"]

