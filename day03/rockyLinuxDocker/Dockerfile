# Use Rocky Linux as base image
FROM rockylinux:9

# Update system and install some basic packages
RUN dnf update -y && \
    dnf install -y --allowerasing \
    curl \
    wget \
    vim \
    && dnf clean all

# Set a welcome message
RUN echo "Welcome to Rocky Linux Container!" > /etc/motd

# Set the default command
CMD ["/bin/bash"]