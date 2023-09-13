FROM jenkins/jenkins:lts
USER root
# RUN apt-get update -qq \
# && apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common python3.11-venv
# RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
# RUN add-apt-repository \
# "deb [arch=amd64] https://download.docker.com/linux/debian \
# $(lsb_release -cs) \
# stable"
# RUN apt-get update  -qq \
#     && apt-get -y install docker-ce
# RUN usermod -aG docker jenkins

RUN chown -R jenkins:jenkins /var/jenkins_home/

WORKDIR /var/jenkins_home/

# RUN curl -O https://dlcdn.apache.org//jmeter/binaries/apache-jmeter-5.6.2.tgz
# RUN tar -xvf apache-jmeter-5.6.2.tgz

# COPY --chown=jenkins:jenkins charge.jmx /var/jenkins_home/apache-jmeter-5.6.2/bin/charge.jmx
# COPY --chown=jenkins:jenkins user.properties /var/jenkins_home/apache-jmeter-5.6.2/bin/user.properties

USER jenkins



