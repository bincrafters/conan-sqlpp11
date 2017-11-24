from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")


class sqlpp11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "sqlpp11/0.38@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        os.chdir("bin")
        self.run(".%ssqlpp11_examples insert" % os.sep)
        self.run(".%ssqlpp11_examples update" % os.sep)
        self.run(".%ssqlpp11_examples select" % os.sep)
        self.run(".%ssqlpp11_examples remove" % os.sep)
