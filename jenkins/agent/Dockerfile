FROM jenkins/ssh-agent:alpine-jdk17
RUN apk update
RUN apk upgrade
RUN apk add curl gnupg python3 py3-virtualenv docker docker-compose

RUN chown -R jenkins:jenkins /home/jenkins
RUN chown jenkins:jenkins /etc
RUN chown jenkins:jenkins /etc/ssh/
RUN chown jenkins:jenkins /run

WORKDIR /home/jenkins

# installation trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.45.0
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl

USER jenkins

RUN curl -O https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.2.tgz
RUN tar -xvf apache-jmeter-5.6.2.tgz

COPY --chown=jenkins:jenkins charge.jmx /home/jenkins/apache-jmeter-5.6.2/bin/charge.jmx
COPY --chown=jenkins:jenkins user.properties /home/jenkins/apache-jmeter-5.6.2/bin/user.properties



