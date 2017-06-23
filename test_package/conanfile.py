from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "ccleeland")


class CppdepTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "cppdep/latest@%s/%s" % (username, channel)
    options = {"shared": [True, False]}
    default_options = "shared=False"
    description = "test package for cppdep"
    generators = "cmake"

    def build(self):
        pass

    def imports(self):
        pass

    def test(self):
        self.run("echo $PATH; cpp-dependencies")
