
FROM python:3.12-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install fakenos
WORKDIR /app
COPY . /app

CMD ["python3", "app.py"]

# ARG ssh_user=admin
# ENV SSH_USER=${ssh_user}
# ARG ssh_password=admin
# ENV SSH_PASSWORD=${ssh_password}
# ARG ssh_public_key_file=vagrant.pub
# ENV SSH_PUBLIC_KEY_FILE=${ssh_public_key_file}
# ARG ssh_path=/home/${ssh_user}/.ssh

# RUN useradd -rm -d /home/${SSH_USER} -s /bin/bash -g root -G sudo -u 2000 ${SSH_USER} 
# RUN echo "${SSH_USER}:${SSH_PASSWORD}" | chpasswd
# RUN mkdir ${ssh_path}
# RUN chown ${SSH_USER} ${ssh_path}
# RUN chmod 700 ${ssh_path}
# COPY ${SSH_PUBLIC_KEY_FILE} ${ssh_path}/authorized_keys
# RUN chmod 400 ${ssh_path}/authorized_keys
# RUN chown ${SSH_USER} ${ssh_path}/authorized_keys


# EXPOSE 22

# CMD ["/usr/sbin/sshd","-D"]