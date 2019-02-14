---
layout: post
title: "Gitlab Installation"
date: 2019-02-13
---

CentOs 7.3에서 Gitlab을 설치하고 설정하는 법을 적은 글입니다.

### Install and configure the necessary dependencies

On CentOS 7 (and RedHat/Oracle/Scientific Linux 7), the commands below will also open HTTP and SSH access in the system firewall.

```
sudo yum install -y curl policycoreutils-python openssh-server
sudo systemctl enable sshd
sudo systemctl start sshd
```

Next, install Postfix to send notification emails. If you want to use another solution to send emails please skip this step and configure an external SMTP server after GitLab has been installed.

```
sudo yum install postfix
=> already installed
sudo systemctl enable postfix
sudo systemctl start postfix
```

### Add the GitLab package repository and install the package

```
curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.rpm.sh | sudo bash
```

Next, install the GitLab package. Change `http://gitlab.example.com` to the URL at which you want to access your GitLab instance. Installation will automatically configure and start GitLab at that URL. HTTPS requires additional configuration after installation.

```
sudo EXTERNAL_URL="http://gitlab.[alias].com" yum install -y gitlab-ee
```


### Change Gitlab URL

First, change git repository url 
```
vi /var/opt/gitlab/gitlab-rails/etc/gitlab.yml
=> Web server setting 
=> host,port change
``` 

And then, change 
```
vi /etc/gitlab/gitlab.rb
=> external_url change
sudo gitlab-ctl reconfigure
```