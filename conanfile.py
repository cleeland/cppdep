from conans import ConanFile, CMake, tools
import os

class CppdependenciesConan(ConanFile):
    name = "cppdep"
    version = "latest"
    license = "Apache License, Version 2.0"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    build_requires = "Boost/[>1.47]@local/testing"

    def source(self):
	self.run("git clone https://github.com/tomtom-international/cpp-dependencies.git")
        tools.replace_in_file("cpp-dependencies/CMakeLists.txt", "project(cpp_dependencies LANGUAGES CXX)", '''project(cpp_dependencies LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake cpp-dependencies %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
	self.copy("cpp-dependencies", src="bin", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.bindirs = ['bin']
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

