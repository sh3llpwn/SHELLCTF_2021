FROM debian:buster-slim

RUN apt update && apt install openssh-server supervisor -y && adduser shell && mkdir -p /var/run/sshd /var/log/supervisor

COPY container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN ssh-keygen -A

USER shell

WORKDIR /home/shell
RUN mkdir .ssh/ 
COPY container/authorized_keys /home/shell/.ssh/authorized_keys
COPY container/flag.txt /home/shell/flag.txt

USER root

EXPOSE 22
CMD ["/usr/bin/supervisord"]