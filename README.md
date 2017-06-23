A conan recipe for packaging cpp.dependencies.

Intended usage in a CentOS environment:
```
$ conan install --profile ./devtoolset-4.txt
$ conan test_package --profile ./devtoolset-4.txt
```

## NOTE

Assumes existence of a conan remote named "local" containing a Boost
version >1.47.