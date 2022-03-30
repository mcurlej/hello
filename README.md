* Hello

prints "Hello Pyvo!" to the command line.

* Package to RPM

This packaging was run on a Fedora machine.


Install necessary packages:

```
$ dnf install rpmbuild mock pip python3
```

Git clone this repository.

Inside the dir run the `sdist` command:

```
$ python setup.py sdist
```

It will generate the source `*.gz` files necessary for source RPM generation:

Create source RPM:

```
$ mock --buildsrpm --spec=hello.spec --source=dist/hello-0.1.0.tar.gz -r /etc/mock/fedora-35-x86_64.cfg --result=./
```

The result source RPM will be placed in the dir defined by the `--result` argument.

When source RPM is generated to create binary RPM run:

```
$ mock -r /etc/mock/fedora-35-x86_64.cfg --result=./ --rebuild hello-0.1.0-1.fc35.src.rpm
```
