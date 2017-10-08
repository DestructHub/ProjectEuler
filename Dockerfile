FROM ubuntu:trusty

RUN apt-get update \
  && apt-get -y upgrade \
  && apt-get install -y

RUN apt-get install -y software-properties-common \
                       python-software-properties \
                       python3-pip \
                       wget

RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
RUN dpkg -i erlang-solutions_1.0_all.deb
RUN add-apt-repository ppa:eugenesan/ppa -y
RUN apt-get update
RUN apt-get install elixir -y
RUN apt-get install php5 -y
RUN apt-get install golang -y
RUN apt-get install clojure1.4 -y
RUN apt-get install ghc -y
RUN apt-get install g++ gcc -y
RUN apt-get install lua5.2 -y
RUN apt-get install ruby-full -y
RUN apt-get install sbcl -y
RUN apt-get install python3-dev -y
RUN apt-get install python-dev -y
RUN pip3 install cython

ADD requirements.txt .
RUN pip3 install -r requirements.txt
WORKDIR /code
